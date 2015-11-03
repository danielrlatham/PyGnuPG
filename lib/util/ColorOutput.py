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


class Colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def warn(arg):
        return Colors.WARNING + arg + Colors.ENDC

    @staticmethod
    def fail(arg):
        return Colors.FAIL + arg + Colors.ENDC

    @staticmethod
    def okay_green(arg):
        return Colors.OKGREEN + arg + Colors.ENDC

    @staticmethod
    def okay_blue(arg):
        return Colors.OKBLUE + arg + Colors.ENDC

    @staticmethod
    def extra_purple(arg):
        return Colors.HEADER + arg + Colors.ENDC

    @staticmethod
    def underline(arg):
        return Colors.UNDERLINE + arg + Colors.ENDC

    @staticmethod
    def bold(arg):
        return Colors.BOLD + arg + Colors.ENDC

