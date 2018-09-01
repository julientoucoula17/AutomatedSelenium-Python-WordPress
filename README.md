# Automated Selenium with Python on WordPress [![](https://img.shields.io/github/license/sourcerer-io/hall-of-fame.svg?colorB=ff0000)](https://github.com/julientoucoula17/AutomatedSelenium-Python-WordPress/blob/master/LICENSE) [![](https://img.shields.io/badge/Toucoula-Julien-brightgreen.svg?colorB=ff0000)](https://www.linkedin.com/in/julien-t-870b7613a)

This code uses selenium for web browser automation and a module of Python who extract the data.

### Code Requirements
The example code is in Python ([version 3.6](https://www.python.org/downloads/release/python-362/) or higher will work). 
1) import selenium (For more information, [see](https://selenium-python.readthedocs.io/installation.html#introduction))
2) import time
3) import xlrd ([module is used to extract data from a spreadsheet](https://www.geeksforgeeks.org/reading-excel-file-using-python/))

```
ex: pip install selenium
```
### Description

Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.

Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 2.7, 3.5 and above.

### Drivers
Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.

Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

1) Firefox: 	https://github.com/mozilla/geckodriver/releases
2) Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads
3) Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
4) Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10


<img src="Automated-Selenium.gif">


### Application

<b> I used it  for internships for add users who were in a spreadsheet or articles on wordpress and other things. 😎 </b>

### Execution
To run the code, type `python Automated_Form.py`

```
python Automated_Add_User.py
```

