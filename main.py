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

__author__ = 'D Latham'


class ArgumentBranch(object):
    def __init__(self):
        # List of arguments
        self.args = sys.argv

    @staticmethod
    def run_gui():
        import lib.interface.graphicsmode.run as GraphicsLoop
        GraphicsLoop.run_gui()

    # Display version info and exit with user_closed error code
    def disp_version_info(self):
        f = open('VERSION', mode='r')
        for line in f:
            print(line)

    def help(self):
        help_string = 'Thanks for using PyGnuPG.\n'+\
                      'Basic help can be given with the \'-h\' flag.\n'+\
                      'More advanced help is given with \'-h [other_flag]\' to learn\n'+\
                      ' about a specific other flag'
        # print('Help Method')
        print(ColorO.Colors.okay_green(help_string))

    def decide(self):
        if len(self.args) > 1:
            pass
        else:
            # no arguments
            self.run_gui()

        # Test args values
        print(self.args)

        # Check if '--version' or '-v' is present
        for arg in self.args:
            if arg == '-v' or arg == '--version':
                self.disp_version_info()

        if self.args[1] == '-h':
            # Check to make sure -h is alone
            self.help()

            # Provide help text based on following flags
            #TODO: Following flags

        if self.args[1] == '--text-mode':
            print(ColorO.Colors.okay_blue('\'--text-mode\' option chosen\n'))
            ans = input('This option is for experimental and development only.'+
                        'Are you sure you want to continue?: ')
            if ans[0].lower() == 'y':
                print('Chosen YES, continuing...')
                import lib.interface.textmode.run as TextLoop
                TextLoop.loop()
            else:
                exit(ECodes.Codes.no_text_mode)
        else:
            pass

class Depends(object):
    def __init__(self):
        pass

    def python3(self):
        try:
            # Python version must be >= 3.3
            assert sys.version_info.major >= 3 and sys.version_info.minor >= 3
        except AssertionError:
            # Print error, exit with error code
            Error.build_error('Incorrect Python version. Require \'3.3+\'')
            exit(ECodes.Codes.py_version)

    def test(self):
        print('How do I jedi?')
        print('yee')

def main():
    ab = ArgumentBranch()
    ab.decide()


if __name__ == '__main__':
    main()
