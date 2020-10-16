# demoqa-selenium
__Description__: Demonstrate test automation of [http://demoqa.com](http://demoqa.com) website using Python, PyTest and Selenium WebDriver.

__Platform__: Darwin

__Supported Browser__ (at this time): Chrome version 86.0.4240.80

## Prerequisite Software:

1. Download and install [Python 3.9.0](https://www.python.org/downloads/release/python-390/) for Mac.
1. Download [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and install to a directory in your system path (i.e., /usr/local/bin)

## Setup:

1. Setup Virtual Environment
```
make setup
```
1. Install Dependencies
```
make install
```
1. Activate Your Virtual Environment
```
demoqa
```
You should see ```(.demoqa-selenium)``` in your command prompt.

## Execute the Tests
```
make
```

## Deactivate Your Virtual Environment
```
deactivate
```
