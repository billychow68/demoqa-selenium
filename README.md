# demoqa-selenium
__Description__: Demonstrate UI test automation of [http://demoqa.com](http://demoqa.com) website in Python, PyTest and Selenium WebDriver.

__Platform__ (at this time): Darwin

__Supported Browser__ (at this time): Chrome version 86.0.4240.80

## Prerequisite Software

1. Download and install [Python 3.9.0](https://www.python.org/downloads/release/python-390/) for Mac.
1. Download and install [Chrome browser](https://www.google.com/chrome)
1. Download and install [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) to a directory in your system path (i.e., /usr/local/bin)

## Setup

1. Setup Virtual Environment
```
make setup
```
2. Install Dependencies
```
make install
```
3. Activate Your Virtual Environment
```
demoqa
```
You should see ```(.demoqa-selenium)``` in your command prompt.

## Execute the Tests
```
make
```

## View the HTML Test Results Report
```
reports/report.html
```
## Deactivate Your Virtual Environment
```
deactivate
```
## Demo
[demo.mov](https://github.com/billychow68/demoqa-selenium/blob/main/demo/demo.mov)
