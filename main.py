#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module's docstring summary line.
This is a multi-line docstring. Paragraphs are separated with blank lines.
Lines conform to 79-column limit.
Module and packages names should be short, lower_case_with_underscores.
See http://www.python.org/dev/peps/pep-0008/ for more PEP-8 details and
http://wwd.ca/blog/2009/07/09/pep-8-cheatsheet/ for an up-to-date version
of this cheatsheet.
"""
__author__ = 'D Latham'

import sys
import lib.util.ErrorBuilder as Error
import lib.util.ErrorCodes as ECodes

try:
    # Python version must be >= 3.3
    assert sys.version_info.major >= 3 and sys.version_info.minor >= 3
except AssertionError:
    # Print error, exit with error code
    Error.build_error('Incorrect Python version. Require \'3.3+\'')
    exit(ECodes.Codes.py_version)

from kivy import require
require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
