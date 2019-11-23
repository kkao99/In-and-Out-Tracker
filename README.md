# In-and-Out-Tracker
A desktop GUI that tracks people going in and out of a place.


## Getting Started
The following instruction can get you a copy of the project.

### Prerequisites
* You will need python `3.x` installed on your machine.
* To check the python version, simply type `$ python --version` in your terminal.
* Make sure you have `alias python='python3'` in your `~/.bash_profile` file.

### Installing
Run the following in your terminal.

```bash
$ git clone https://github.com/kkao99/In-and-Out-Tracker
$ cd In-and-Out-Tracker              # navigate to the directory
$ python -m venv kivy_venv           # create a virtual env
$ source kivy_venv/bin/activate      # activate the virtual env
$ pip install --upgrade pip          # upgrade pip to latest version
$ pip install -r requirements.txt    # install necessary dependencies
$ python main.py
```
After issuing these commands, you should be able to see the application running.

To close the app, simply click on the :x: button on the top left and run `$ deactivate` to deactivate the virtual env.

## Features
* Minimize the use of paper (digital)
* Save records in a csv format file
* Support login verification

## About
* Created by [Kevin Kao](https://github.com/kkao99) on 08/03/2019
* MIT License
* Just a random project for fun :trollface: ~
