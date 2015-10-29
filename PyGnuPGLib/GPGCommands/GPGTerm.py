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

import os


"""Holds python calls to operating system using preconfigured commands in
__commands class
"""


class GPG(object):
    def __init__(self):
        gpg = 'gpg'

    def encrypt(self, keyid, inputfile_path, outputfile_path):
        basic_encrypt = '{0} '

    def decrypt(self, keyid, inputfile_path, outputfile_path):
        pass

"""Holds all gpg commands and calls to OS
Includes documentation
"""


class __commands:
    # Make a signature. This command may be combined with –encrypt.
    sign = '-sign'

    # Make a clear text signature.
    clear_sign = '–clearsign'

    # Make a detached signature.
    detach_sign = '–detach-sign'

    # Encrypt data. This option may be combined with –sign.
    encrypt = '–encrypt'

    # Encrypt with symmetric cipher only This command asks for passphrase.
    symmetric = '–symmetric'

    # Store only (make a simple RFC1991 packet).
    store = '–store'

    # Decrypt file (or stdin if no file is specified) and write it to
    # stdout (or the file specified with –output). If the decrypted file is
    # signed, the signature is also verified. This command differs from the
    # default operation, as it never writes to the filename which is
    # included in the file and it rejects files which don't begin with an
    # encrypted message.
    decrypt = '–decrypt'

    # Assume that sigfile is a signature and verify it without generating
    # any output. With no arguments, the signature packet is read from
    # stdin (it may be a detached signature when not used in batch mode).
    # If only a sigfile is given, it may be a complete signature or a
    # detached signature, in which case the signed stuff is expected in a
    # file without the ".sig" or ".asc" extension (if such a file does not
    # exist it is expected at stdin; use a single dash ("-") as filename to
    # force a read from stdin). With more than 1 argument, the first should
    # be a detached signature and the remaining files are the signed stuff.
    verify = '–verify'

    # This is a special version of the –verify command which does not work
    # with detached signatures. The command expects the files to bee
    # verified either on the commandline or reads the filenames from stdin;
    # each anem muts be on separate line. The command is intended for quick
    # checking of many files.
    verify_files = '–verify-files'

    # List all keys from the public keyrings, or just the ones given on the
    # command line.
    list_public_keys = '–list-public-keys'

    # List all keys from the secret keyrings, or just the ones given on the
    # command line.
    list_secret_keys = '–list-secret-keys'

    # Same as –list-keys, but the signatures are listed too.
    list_sigs = '–list-sigs'

    # Same as –list-sigs, but the signatures are verified.
    check_sigs = '–check-sigs'

    # List all keys with their fingerprints. This is the same output as
    # –list-keys but with the additional output of a line with the
    # fingerprint. May also be combined with –list-sigs or –check-sigs.
    # If this command is given twice, the fingerprints of all secondary
    # keys are listed too.
    fingerprint = '–fingerprint'

    # List only the sequence of packets. This is mainly useful for
    # debugging.
    list_packets = '–list-packets'

    # Generate a new key pair. This command is normally only used
    # interactive.
    # There is an experimental feature which allows to create keys in
    # batch mode. See the file doc/DETAILS in the source distribution on
    # how to use this.
    gen_key = '–gen-key'

    # Sign a public key with you secret key. This is a shortcut version of the
    # subcommand "sign" from –edit.
    sign_key = '–sign-key'

    # Sign a public key with you secret key but mark it as non-exportable.
    # This is a shortcut version of the subcommand "lsign" from –edit.
    lsign_key = '–lsign-key'

    # Assume that the specified key (which must be given as a full 8 byte key
    # ID) is as trustworthy as one of your own secret keys. This option is
    # useful if you don't want to keep your secret keys (or one of them)
    # online but still be able to check the validity of a given recipient's or
    # signator's key.
    trust_key = '–trusted-key'

    # Remove key from the public keyring
    delete_key = '–delete-key'

    # Remove key from the secret and public keyring
    delete_secret_key = '–delete-secret-key'

    # Generate a revocation certificate for the complete key. To revoke a
    # subkey or a signature, use the –edit command.
    gen_revoke = '–gen-revoke'

    # Either export all keys from all keyrings (default keyrings and those
    # registered via option –keyring), or if at least one name is given, those
    # of the given name. The new keyring is written to stdout or to the file
    # given with option "output". Use together with –armor to mail those keys.
    export = '–export'

    # Same as –export but sends the keys to a keyserver. Option –keyserver must
    # be used to give the name of this keyserver. Don't send your complete
    # keyring to a keyserver - select only those keys which are new or changed
    # by you.
    send_keys = '–send-keys'

    # Same as –export, but does also export keys which are not compatible to
    # OpenPGP.
    export_all = '–export-all'

    # Same as –export, but does export the secret keys. This is normally not
    # very useful and a security risk. the second form of the command has the
    # special property to render the secret part of the primary key useless;
    # this is a GNU extension to OpenPGP and other implementations can not be
    # expected to successful import such a key.
    export_secret_keys = '–export-secret-keys'
    export_secret_subkeys = '–export-secret-subkeys'

    # Import/merge keys. This adds the given keys to the keyring. The fast
    # version does not build the trustdb; this can be done at any time with the
    # command –update-trustdb.
    # There are a few other options which control how this command works. Most
    # notable here is the –merge-only options which does not insert new keys
    # but does only the merging of new signatures, user-IDs and subkeys.
    import_ = '–import'
    fast_import_ = '–fast-import'

    # Import the keys with the given key IDs from a HKP keyserver. Option
    # –keyserver must be used to give the name of this keyserver.
    recv_keys = '–recv-keys'

    # List the assigned ownertrust values in ASCII format for backup purposes
    export_ownertrust = '–export-ownertrust'

    # Update the trustdb with the ownertrust values stored in files (or stdin
    # if not given); existing values will be overwritten.
    import_ownertrust = '–import-ownertrust'

    # Print message digest of algorithm ALGO for all given files of stdin.
    # If "*" is used for the algorithm, digests for all available algorithms
    # are printed.
    print_md = '–print-md'

    # Emit COUNT random bytes of the given quality level. If count is not given
    #  or zero, an endless sequence of random bytes will be emitted. PLEASE,
    # don't use this command unless you know what you are doing, it may remove
    # precious entropy from the system!
    gen_random = '–gen-random'

    # Use the source, Luke :-). The output format is still subject to change.
    gen_prime = '–gen-prime'

    # Print version information along with a list of supported algorithms.
    version = '–version'

    # Print warranty information.
    warranty = '–warranty'

    # Print usage information. This is a really long list even it does list
    # not all options.
    h = '-h'


class __options:
    pass
