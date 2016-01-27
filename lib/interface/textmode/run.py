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
from lib.gpglib.GPGPyAPI import API
from lib.util.ColorOutput import Colors
from lib.util.ErrorCodes import Codes

__author__ = 'D Latham'


class Choice:
    @staticmethod
    def encrypt():
        print(Colors.okay_green('Encryption Scheme'))

    @staticmethod
    def decrypt():
        print('Decryption Scheme')

    @staticmethod
    def sign():
        pass

    @staticmethod
    def clear_sign():
        pass


def loop():
    stop = False
    while not stop:
        _in = input(Colors.okay_blue('What would you like to do? GPG Commands '
                                     'Only.: '))
        if _in[0].lower() == 'e':
            Choice.encrypt()
        elif _in[0].lower() == 'd':
            Choice.decrypt()
        elif _in[0].lower() == 'q' or _in.lower() == 'quit':
            print(Colors.bold('Exiting...'))
            exit(Codes.chosen_exit)


def main():
    pass

if __name__ == '__main__':
    main()