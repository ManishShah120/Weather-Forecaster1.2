[![build](https://travis-ci.org/ikatyang/emoji-cheat-sheet.svg?branch=master)](https://travis-ci.org/ikatyang/emoji-cheat-sheet)  [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  [![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/watchers/) 
## **Weather-Forecaster1.2**
- A simple python web crawler to fetch Weather report of any state in India.
# Getting Started
### Installation
After downloading or cloning the repo, Navigate to the directory containing the files and double click on **setup.py** or **run** <br>
```python setup.py install```
or if you have different versions of python then <br>
```python3 setup.py install``` 
###### If the above Commands produces error Try installing the dependnecies
# To install the dependencies
> ```Pip3 install requirements.txt``` or<br>
> ```pip3 install bs4 | pip3 install requests``` 
# How to run
From the project directory **run**
``` python3 forecastmain.py```
![alt text](https://github.com/ManishShah120/Weather-Forecaster1.2/blob/master/Weather%20Forecaster1.2.png)
### HOW IT WORKS
- It prompts to select a state from the dropdown and then select a city from that  state to get the forecast and **Voila** You get the required Weather Report of that particualr city.
- An algorithm is being designed for scraping the data and laying out in the desired format
- The source code of the requested webpage is decoded and `<div>` containing the forecast string is searched, manipulated a little, fomatted to display

## Built With
1. Python 3.6
2. Linux

## Dependencies & packages
1. BeautifulSoup
2. Requests
3. Os
4. Sys
5. re
6. citiesurl(Self Built)

## Contributing

> 1.Feel free to FORK<br>
> 2.Create your feature branch: ```git checkout -b my-new-feature```<br>
> 3.Beautify/Format your code before making a PR. Poorly stuctured code with inconsistent spacing and bad variable name will not be merged.<br>
> 4.Use this tool to beautify your code :[Click](https://codebeautify.org/c-formatter-beautifier)<br>
> 5.Make sure your program works after beautifying it.<br>
> 6.Please check your spellings before making a PR<br>
> 7.Comment code properly.<br>
> 8.Commit your changes: ```git commit -m 'Add some feature'```<br>
> 9.Push to the branch: ```git push origin my-new-feature```<br>
> 10.Submit a ```pull``` request.

## Authors
[**Manish Kumar Shah**](https://github.com/ManishShah120)

# License [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[**MIT**](https://github.com/ManishShah120/Weather-Forecaster1.2/blob/master/LICENSE)

# Project Status
Till now this project has been 95% completed. Everyone is Welcomed to fork this repo and work on it and submit a pull request.
