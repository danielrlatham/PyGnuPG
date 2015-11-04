#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Holds functions to call OS specific GPG calls
Currently only supporting Linux(no apple computer nearby)
"""
__author__ = 'D Latham'

import os
import platform
import subprocess
from GPGDictionary import Commands, Options


class API(object):
    def __init__(self):
        self.OS = platform.system()
        self.RELEASE = platform.release()
        self.RUN_LEVEL = os.getuid()
        self.GPG = 'gpg'

    def execute(self, command=()):
        assert command.__class__ is [].__class__
        assert len(command) >= 1
        command.insert(0, self.GPG)
        print(command)
        subprocess.call(command)

    # Function to encrypt and encrypt/sign a file
    # assumed in_file and out_file are paths to files
    def encrypt(self, id, in_file, out_file, default_key=None, sign=False, is_armor=False, fyeo=False,
                mdc=False, nev=False, notty=False, quiet=True, yes=True ):
        e = Commands.e
        r = Options.r
        o = Options.o
        # Initialize list
        temp = []
        # Add encryption command
        temp.append(e)
        # Add possible sign command
        if sign and default_key:
            temp.append(Commands.s)
            temp.append(Options.default_key)
            temp.append(default_key)
        # Add definite options
        temp.append(r)
        temp.append(id)
        temp.append(o)
        temp.append(out_file)
        # Add possible options
        if is_armor:
            temp.append(Options.armor)
            if nev:
                temp.append(Options.no_emi)
        else:
            temp.append(Options.no_armor)
        if fyeo:
            temp.append(Options.for_your_eyes_only)
        if mdc:
            temp.append(Options.force_mdc)
        if notty:
            temp.append(Options.no_tty)
        if quiet:
            temp.append(Options.quiet)
        if yes:
            temp.append(Options.yes)
        # Add file to encrypt
        temp.append(in_file)
        # Send to execute
        self.execute(temp)

    def decrypt(self, id, in_file, out_file):
        d = Commands.decrypt
        r = Options.r


def test_encrypt():
    api = API()
    api.encrypt('AC8F1D60',
                '/home/dan/PycharmProjects/PyGnuPG/test_data/generic.txt',
                '/home/dan/PycharmProjects/PyGnuPG/test_data/generic.txt.gpg1',
                default_key='C2C33946', sign=True, is_armor=True, yes=False)

def __main__():
    api = API()
    print(api.OS)
    print(api.RUN_LEVEL)



if __name__ == '__main__':
    __main__()
