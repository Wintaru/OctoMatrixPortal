import microcontroller
import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal

try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Setup stuff
SCROLL_DELAY = 0.02
SLEEP_DURATION = 5.0
OCTOPI_SRC = secrets['octopi_host']
JOB_DATA_SRC = OCTOPI_SRC + '/api/job'
PLUGIN_DATA_SRC = OCTOPI_SRC + '/plugin/DisplayLayerProgress/values'
SETTINGS_DATA_SRC = OCTOPI_SRC + '/api/settings' # Unused for now
API_KEY = secrets['octopi_api_key']

# Set up headers for Octoprint
HEADERS = {'X-Api-Key' : API_KEY}

# --- Display setup ---
matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
    debug=False)

PROGRESS_WIDTH = 10

# idx = 0 (Scrolling text that shows the file being printed)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(1, 6),
    text_color=0x0000FF,
    scrolling=True,
)

# idx = 1 (Static text that shows the time remaining)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(1, 16),
    text_color=0xFF0000,
)

# idx = 2 (Progress bar that shows progress in a different way)
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(1, 26),
    text_color=0x00FF00,
)

# Show them we're doing something while the wifi fails to connect once
# then actually connects...
matrixportal.set_text("Connecting", 1)

# Converts and stores the number of seconds remaining into Days, hours, minutes, seconds
class TimeStruct:
    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, time_left) -> None:
        self.days = time_left // (24 * 3600)
        time_left = time_left % (24 * 3600)
        self.hours = time_left // 3600
        time_left %= 3600
        self.minutes = time_left // 60
        time_left % 60
        self.seconds = time_left

# Makes TimeStruct something that can be displayed
def ConvertTimeStructToDisplayString(time_left):

    tl_str = ""

    if time_left.days > 0:
        tl_str += str(time_left.days) + "D "
    if time_left.hours > 0:
        tl_str += str(time_left.hours) + "H "
    if time_left.minutes > 0:
        tl_str += str(time_left.minutes) + "M "
    # Optionally display seconds as well, but it feels unuseful.
    # if time_left.seconds > 0 and time_left.minutes == 0:
    #     tl_str += str(time_left.seconds) + "S "

    return tl_str

# Creates a progress bar for the bottom "row"
def CreateProgressBar(progress):
    progress_bar = ""
    for x in range(progress):
        progress_bar += "|"
    return progress_bar

refresh_time = None
now_printing_str = ""
print_left_str = ""
progress_bar = ""

while True:
    try:
        # No need to hammer Octoprint for updates, every minute seems reasonable
        if (not refresh_time) or (time.monotonic() - refresh_time) > 60:
            # Fetch job data first
            response = matrixportal.network.fetch(JOB_DATA_SRC, headers=HEADERS)
            job_info = response.json()
            response.close()
            response = matrixportal.network.fetch(PLUGIN_DATA_SRC, headers=HEADERS)
            layer_info = response.json()
            response.close()

            # This is usually encountered if you have the API key wrong
            if 'error' in job_info:
                now_printing_str = "Configuration Error (check your API key?)"
                print_left_str = ""
                progress_bar = ""
            # If Octoprint is idle, this is what you get, some stuff is null
            elif job_info['state'] != "Printing":
                now_printing_str = "Not Printing"
                print_left_str = ""
                progress_bar = ""
            # Hopefully you really are printing
            else:
                pt_left = job_info['progress']['printTimeLeft']
                # It can take a while for Octoprint to come up with an estimate so we
                # display 'Calculating' until this is ready to show
                print_left_str = "Calculating"
                if pt_left:
                    time_left = TimeStruct(pt_left)
                    print_left_str = ConvertTimeStructToDisplayString(time_left)

                # prepare the strings for display and create progress bar
                now_printing_str = "Now Printing: " + job_info['job']['file']['name']
                progress_bar = str((int)(job_info['progress']['completion'])) + "%"
                cur_layer = (int)(layer_info['layer']['current'])
                tot_layer = (int)(layer_info['layer']['total'])
                progress_bar += " " + str(cur_layer) + "/" + str(tot_layer)

            refresh_time = time.monotonic()

        # Update text
        matrixportal.set_text(now_printing_str, 0)
        matrixportal.set_text(print_left_str, 1)
        matrixportal.set_text(progress_bar, 2)
        matrixportal.scroll_text(SCROLL_DELAY)

    except Exception as e:
        print("Error: " + str(e))
        refresh_time = None
        matrixportal.set_text(str(e), 0)
        matrixportal.scroll_text(SCROLL_DELAY)

    time.sleep(1)
