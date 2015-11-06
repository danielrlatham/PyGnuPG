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
import sys
import lib.util.ErrorBuilder as Error
import lib.util.ColorOutput as ColorO
import lib.util.ErrorCodes as ECodes

try:
    # Python version must be >= 3.3
    assert sys.version_info.major >= 3 and sys.version_info.minor >= 3
except AssertionError:
    # Print error, exit with error code
    Error.build_error('Incorrect Python version. Require \'3.3+\'')
    exit(ECodes.Codes.py_version)

__author__ = 'D Latham'





def main():
    if sys.argv[1] == '--text-mode':
        print(ColorO.Colors.okay_blue('\'--text-mode\' option chosen'))
        print()
        ans = input('This option is for experimental and development only. '
                    'Are you sure you want to continue?')
        if ans[0].lower() == 'y':
            print('Chosen YES, continuing...')
        else:
            exit(ECodes.Codes.no_text_mode)


if __name__ == '__main__':
    main()
