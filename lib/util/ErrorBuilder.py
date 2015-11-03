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

import inspect
from ..util.ColorOutput import Colors


def build_error(error_string='', error_obj=None):
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                              # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)

    out = 'Error at file ' + info.filename + ',\nFunction ' + info.function + \
          ',\nline #' + str(info.lineno) + '.'

    print(Colors.warn(out))
    print(Colors.fail(error_string + '\n'))

if __name__ == '__main__':
    build_error('I am an Error')
    print('ran')
