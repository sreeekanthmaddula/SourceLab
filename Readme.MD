# Swag Labs UI Automation
# PetStore API Automation


## Table of Contents
* [Introduction]()
* [Features]()
* [Installation]()
* [Usage]()
* [Contributing]()

## First Time Setup
### Software used
[Python 3.11](https://docs.python.org/2/)  

Pytest Framework

Requests Library

Selenium


### Install Dependencies
Determine if Python is installed: In a terminal, run the following command
```
$ python --version
```

####Clone Repository  
```
$ cd saucedemo_e-commerce
$ git clone https://github.com/sreeekanthmaddula/SourceLab.git
$ cd SourceLab
```
####Install requirements
```
$ pip install -r requirements.txt
```

####Install chrome  
* Windows

## Running Tests
Run all tests locally
```
pytest -s -v -m "login" --log-file=./Logs/automation.log --html=./Reports/report.html --self-contained-html --capture sys -rP  --disable-warnings testCases/test_login.py --browser chrome

```
####Contributing
To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.
5. Please ensure all tests pass before submitting a pull request.

