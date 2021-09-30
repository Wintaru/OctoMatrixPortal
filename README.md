<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Wintaru/OctoMatrixPortal">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">OctoMatrixPortal</h3>

  <p align="center">
    An Octoprint monitor using the Adafruit Matrix Portal display.
    <br />
    <a href="https://github.com/Wintaru/OctoMatrixPortal"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Wintaru/OctoMatrixPortal">View Demo</a>
    ·
    <a href="https://github.com/Wintaru/OctoMatrixPortal/issues">Report Bug</a>
    ·
    <a href="https://github.com/Wintaru/OctoMatrixPortal/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src=./images/demo.gif alt="product image" width="600" />

I wanted a way to monitor my printer in the other room at a glance and the Adafruit Matrix Portal is a great way to do just that!

### Built With

* [Adafruit Matrix Portal Starter Kit](https://www.adafruit.com/product/4812)
* [Octoprint](https://octoprint.org/)
* [DisplayLayerProgress Octoprint Plugin](https://github.com/OllisGit/OctoPrint-DisplayLayerProgress)

There are myriad guides for getting Octoprint going, I run mine on a RaspberryPI 3, and the DisplayLayerProgress plugin is easy to find an enable once you have your octoprint instance going.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* A running instance of OctoPi connected to your printer
* The DisplayLayerProgress plugin installed and enabled

### Installation

1. Connect your MatrixPortal to your computer, you may need to perform additional steps to get it ready for use (see [Adafruit's wonderful guides](https://learn.adafruit.com/adabox016)).
2. Copy code.py to your `CIRCUITPYTHON` drive
3. Set up your secrets.py

#### Secrets

Aside from the usual things that your MatrixPortal will need in the secrets file (ssid, password, timezone), you will also need two additional settings.

* octopi_host
    * This is the IP address of your OctoPi (http://octopi.local will not work).

* octopi_api_key
    * This is a key you need to get, it is in your OctoPi's settings under API, Global API Key.

<!-- USAGE EXAMPLES -->
## Usage

There are a few different configurations you can make:

### ETA

The ETA defaults to being shown as the expected time of completion in 12h format. If you set `USE_TWELVE_HOUR_FORMAT` to false it will display using 24h format. If you set `SHOW_ETA_AS_TIME` to false it will instead show you how many Days/Hours/Minutes are left until the print is expected to be done. Note that these are estimates and will change as the print goes on.

### Display Colors

There are 3 variables that let you change the display colors: `TOP_ROW_COLOR`, `MID_ROW_COLOR` and `BOT_ROW_COLOR`. Also included are helper color variables for standard web colors.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Wintaru/OctoMatrixPortal/issues) for a list of proposed features (and known issues).

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Josh Donner - [@wintaru](https://twitter.com/wintaru) - joshua.j.donner@gmail.com

Project Link: [https://github.com/Wintaru/OctoMatrixPortal](https://github.com/Wintaru/OctoMatrixPortal)



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Wintaru/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/Wintaru/OctoMatrixPortal/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Wintaru/repo.svg?style=for-the-badge
[forks-url]: https://github.com/Wintaru/OctoMatrixPortal/network/members
[stars-shield]: https://img.shields.io/github/stars/Wintaru/repo.svg?style=for-the-badge
[stars-url]: https://github.com/Wintaru/OctoMatrixPortal/stargazers
[issues-shield]: https://img.shields.io/github/issues/Wintaru/repo.svg?style=for-the-badge
[issues-url]: https://github.com/Wintaru/OctoMatrixPortal/issues
[license-shield]: https://img.shields.io/github/license/Wintaru/repo.svg?style=for-the-badge
[license-url]: https://github.com/Wintaru/OctoMatrixPortal/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Wintaru
