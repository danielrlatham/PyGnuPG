#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Holds declarations of all GPG commands/options with man-page summaries
This is not meant to be changed except early in the project
@WARN: DO NO CHANGE THIS UNLESS YOU REALLY, REALLY KNOW WHAT YOU ARE DOING
"""
__author__ = 'D Latham'


"""Holds all gpg commands and calls to OS
Includes documentation
"""
class Commands:
    # Make a signature. This command may be combined with –encrypt.
    s = '-s'
    sign = '-sign'

    # Make a clear text signature.
    clear_sign = '–clearsign'

    # Make a detached signature.
    b = '-b'
    detach_sign = '–detach-sign'

    # Encrypt data. This option may be combined with –sign.
    e = '-e'
    encrypt = '–encrypt'

    # Encrypt with symmetric cipher only This command asks for passphrase.
    c = '-c'
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
    help = '-help'


class Options:
    # Long options can be put in an options file (default "~/.gnupg/options").
    # Do not write the 2 dashes, but simply the name of the option and any
    # required arguments. Lines with a hash as the first non-white-space
    # character are ignored. Commands may be put in this file too, but that
    # does not make sense.

    # gpg recognizes these options:

    # Create ASCII armored output.
    a = '-a'
    armor = '–armor'

    # Write output to file.
    o = '-o'
    output = '–output'

    # Use name as the user ID to sign. This option is silently ignored for the
    # list commands, so that it can be used in an options file.
    u = '-u'
    local_user = '–local-user'

    # Use name as default user ID for signatures. If this is not used the
    # default user ID is the first user ID found in the secret keyring.
    default_key = '–default-key'

    # Encrypt for user id name. If this option is not specified, GnuPG asks for
    # the user-id unless –default-recipient is given
    r = '-r'
    recipient = '–recipient'

    # Use name as default recipient if option –recipient is not used and don't
    # ask if this is a valid one. name must be a non empty.
    default_recipient = '–default-recipient'

    # Use the default key as default recipient if option –recipient is not used
    # and don't ask if this is a valid one. The default key is the first one
    # from the secret keyring or the one set with –default-key.
    default_recipient_self = '–default-recipient-self'

    # Reset –default-recipient and –default-recipient-self.
    no_default_recipient = '–no-default-recipient'

    # Same as –recipient but this one is intended for in the options file and
    # may be used together with an own user-id as an "encrypt-to-self". These
    # keys are only used when there are other recipients given either by use
    # of –recipient or by the asked user id. No trust checking is performed
    # for these user ids and even disabled keys can be used.
    encrypt_to = '–encrypt-to'

    # Disable the use of all –encrypt-to keys.
    no_encrypt_to = '–no-encrypt-to'

    # Give more information during processing. If used twice, the input data is
    #  listed in detail.
    v = '-v'
    verbose = '–verbose'

    # Try to be as quiet as possible.
    q = '-q'
    quiet = '–quiet'

    # Set compression level to n. A value of 0 for n disables compression.
    # Default is to use the default compression level of zlib (normally 6).
    z = '-z'

    # Use canonical text mode. If -t (but not –textmode) is used together with
    # armoring and signing, this enables clearsigned messages. This kludge is
    # needed for PGP compatibility; normally you would use –sign or –clearsign
    # to selected the type of the signature.
    t = '-t'
    textmode = '–textmode'

    # Don't make any changes (this is not completely implemented).
    n = '-n'
    dry_run = '–dry-run'

    # Prompt before overwriting any files.
    i = '-i'
    interactive = '–interactive'

    # Use batch mode. Never ask, do not allow interactive commands.
    batch = '–batch'

    # Make sure that the TTY (terminal) is never used for any output. This
    # option is needed in some cases because GnuPG sometimes prints warnings
    # to the TTY if if –batch is used.
    no_tty = '–no-tty'

    # Disable batch mode. This may be of use if –batch is enabled from an
    # options file.
    no_batch = '–no-batch'

    # Assume "yes" on most questions.
    yes = '–yes'

    # Assume "no" on most questions.
    no = '–no'

    # Skip key validation and assume that used keys are always fully trusted.
    # You won't use this unless you have installed some external validation
    # scheme.
    always_trust = '–always-trust'

    # Use name to lookup keys which are not yet in your keyring. This is only
    # done while verifying messages with signatures. The option is also
    # required for the command –send-keys to specify the keyserver to where
    # the keys should be send. All keyservers synchronize with each other - so
    # there is no need to send keys to more than one server. Using the command
    # "host -l pgp.net | grep wwwkeys" gives you a list of keyservers. Because
    # there is load balancing using round-robin DNS you may notice that you get
    # different key servers.
    keyserver = '–keyserver'

    # This option disables the automatic retrieving of keys from a keyserver
    # while verifying signatures. This option allows to keep a keyserver in the
    # options file or the –send-keys and –recv-keys commands.
    no_auto_key_retrieve = '–no-auto-key-retrieve'

    # Try to access the keyserver over the proxy set with the variable
    # "http\proxy".
    honor_http_proxy = '–honor-http-proxy'

    # Add file to the list of keyrings. If file begins with a tilde and a
    # slash, these are replaced by the HOME directory. If the filename does
    # not contain a slash, it is assumed to be in the home-directory
    # ("~/.gnupg" if –homedir is not used). The filename may be prefixed with
    # a scheme:
    keyring = '–keyring'

    # Same as –keyring but for the secret keyrings.
    secret_keyring = '–secret-keyring'

    # Set the name of the home directory to directory If this option is not
    # used it defaults to "~/.gnupg". It does not make sense to use this in a
    # options file. This also overrides the environment variable "GNUPGHOME".
    homedir = '–homedir'

    # Set the name of the native character set. This is used to convert some
    # strings to proper UTF-8 encoding. Valid values for name are:
    charset = '–charset'

    # Assume that the arguments are already given as UTF8 strings. The default
    # (–no-utf8-strings) is to assume that arguments are encoded in the
    # character set as specified by –charset. These options effects all
    # following arguments. Both options may used multiple times.
    utf8_strings = '–utf8-strings'
    no_utf8_strings = '–no-utf8-strings'

    # Read options from file and do not try to read them from the default
    # options file in the homedir (see –homedir). This option is ignored if
    # used in an options file.
    options = '–options'

    # Shortcut for "–options /dev/null". This option is detected before an
    # attempt to open an option file.
    no_options = '–no-options'

    # Load an extension module. If name does not contain a slash it is
    # searched in "/usr/local/lib/gnupg" See the manual for more information
    # about extensions.
    load_extension = '–load-extension'

    # Set debugging flags. All flags are or-ed and flags may be given in
    # C syntax (e.g. 0x0042).
    debug = '–debug'

    # Set all useful debugging flags.
    debug_all = '–debug-all'

    # Write special status strings to the file descriptor n. See the file
    # DETAILS in the documentation for a listing of them.
    status_fd = '–status-fd'

    # Write log output to file descriptor n and not to stderr.
    logger_fd = '–logger-fd'

    # Do not write comment packets. This option affects only the generation
    # of secret keys. Please note, that this has nothing to do with the
    # comments in clear text signatures.
    no_comment = '–no-comment'

    # Use string as comment string in clear text signatures. To suppress those
    # comment strings entirely, use an empty string here.
    comment = '–comment'

    # Force to write the standard comment string in clear text signatures. Use
    # this to overwrite a –comment from a config file.
    default_comment = '–default-comment'

    # Omit the version string in clear text signatures.
    no_version = '–no-version'

    # Force to write the version string in clear text signatures. Use this to
    # overwrite a previous –no-version from a config file.
    emit_version = '–emit-version'

    # Put the name value pair into the signature as notation data. name must
    # consists only of alphanumeric characters, digits or the underscore; the
    # first character must not be a digit. value may be any printable string;
    # it will encoded in UTF8, so sou should have check that your –charset is
    # set right. If you prefix name with an exclamation mark, the notation data
    # will be flagged as critical (rfc2440:5.2.3.15).
    N = '-N'
    notation_data = '–notation-data'

    # Use string as Policy URL for signatures (rfc2440:5.2.3.19). If you prefix
    # it with an exclamation mark, the policy URL packet will be flagged as
    # critical.
    set_policy_url = '–set-policy-url'

    # Use string as the name of file which is stored in messages.
    set_filename = '–set-filename'

    # Try to create a file with a name as embedded in the data. This can be a
    # dangerous option as it allows to overwrite files.
    use_embedded_filename = '–use-embedded-filename'

    # Number of completely trusted users to introduce a new key signer
    # (defaults to 1).
    completes_needed = '–completes-needed'

    # Number of marginally trusted users to introduce a new key signer
    # (defaults to 3)
    marginals_needed = '–marginals-needed'

    # Maximum depth of a certification chain (default is 5).
    max_cert_depth = '–max-cert-depth'

    # Use name as cipher algorithm. Running the program with the command
    # –version yields a list of supported algorithms. If this is not used the
    # cipher algorithm is selected from the preferences stored with the key.
    cipher_algo = '–cipher-algo'

    # Use name as message digest algorithm. Running the program with the
    # command –version yields a list of supported algorithms. Please note that
    # using this option may violate the OpenPGP requirement, that a 160 bit
    # hash is to be used for DSA.
    digest_algo = '–digest-algo'

    # Use name as the cipher algorithm used to protect secret keys. The
    # default cipher is BLOWFISH. This cipher is also used for conventional
    # encryption if –cipher-algo is not given.
    s2k_cipher_algo = '–s2k-cipher-algo'

    # Use name as the digest algorithm used to mangle the passphrases. The
    # default algorithm is RIPE-MD-160. This digest algorithm is also used
    # for conventional encryption if –digest-algo is not given.
    s2k_digest_algo = '–s2k-digest-algo'

    # Selects how passphrases are mangled. If n is 0 a plain passphrase (which
    # is not recommended) will be used, a 1 (default) adds a salt to the
    # passphrase and a 3 iterates the whole process a couple of times. Unless
    # –rfc1991 is used, this mode is also used for conventional encryption.
    s2k_mode = '–s2k-mode'

    # Use compress algorithm n. Default is 2 which is RFC1950 compression. You
    # may use 1 to use the old zlib version (RFC1951) which is used by PGP. The
    # default algorithm may give better results because the window size is not
    # limited to 8K. If this is not used the OpenPGP behavior is used, i.e. the
    # compression algorithm is selected from the preferences; note, that this
    # can't be done if you do not encrypt the data.
    compress_algo = '–compress-algo'

    # Never allow the use of name as cipher algorithm. The given name will not
    # be checked so that a later loaded algorithm will still get disabled.
    disable_cipher_algo = '–disable-cipher-algo'

    # Never allow the use of name as public key algorithm. The given name will
    # not be checked so that a later loaded algorithm will still get disabled.
    disable_pubkey_algo = '–disable-pubkey-algo'

    # Do not put the keyid into encrypted packets. This option hides the
    # receiver of the message and is a countermeasure against traffic analysis.
    # It may slow down the decryption process because all available secret keys
    # are tried.
    throw_keyid = '–throw-keyid'

    # This option changes the behavior of cleartext signatures so that they
    # can be used for patch files. You should not send such an armored file via
    # email because all spaces and line endings are hashed too. You can not use
    # this option for data which has 5 dashes at the beginning of a line, patch
    # files don't have this. A special armor header line tells GnuPG about this
    # cleartext signature option.
    not_dash_escaped = '–not-dash-escaped'

    # Because some mailers change lines starting with "From " to "<From " it is
    # good to handle such lines in a special way when creating cleartext
    # signatures. All other PGP versions do it this way too. This option is not
    # enabled by default because it would violate rfc2440.
    escape_from_lines = '–escape-from-lines'

    # Read the passphrase from file descriptor n. If you use 0 for n, the
    # passphrase will be read from stdin. This can only be used if only one
    # passphrase is supplied. Don't use this option if you can avoid it.
    passphrase_fd = '–passphrase-fd'

    # This is a replacement for the depreciated shared-memory IPC mode. If this
    #  option is enabled, user input on questions is not expected from the TTY
    # but from the given file descriptor. It should be used together with
    # –status-fd. See the file doc/DETAILS in the source distribution for
    # details on how to use it.
    command_fd = '–command-fd'

    # Try to be more RFC1991 (PGP 2.x) compliant.
    rfc1991 = '–rfc1991'

    # Reset all packet, cipher and digest options to OpenPGP behavior. Use this
    # option to reset all previous options like –rfc1991, –force-v3-sigs,
    # –s2k-*, –cipher-algo, –digest-algo and –compress-algo to OpenPGP
    # compliant values. All PGP workarounds are also disabled.
    openpgp = '–openpgp'

    # OpenPGP states that an implementation should generate v4 signatures but
    # PGP 5.x recognizes v4 signatures only on key material. This options
    # forces v3 signatures for signatures on data.
    force_v3_sigs = '–force-v3-sigs'

    # Force the use of encryption with appended manipulation code. This is
    # always used with the newer cipher (those with a blocksize greater than
    # 64 bit). This option might not be implemented yet.
    force_mdc = '–force-mdc'

    # Allow the import of keys with user IDs which are not self-signed. This is
    #  only allows the import - key validation will fail and you have to check
    # the validity of the key my other means. This hack is needed for some
    # German keys generated with pgp 2.6.3in. You should really avoid using it,
    # because OpenPGP has better mechanics to do separate signing and
    # encryption keys.
    allow_non_selfsigned_uid = '–allow-non-selfsigned-uid'

    # Disable all checks on the form of the user ID while generating a new one.
    # This option should only be used in very special environments as it does
    # not ensure the de-facto standard format of user IDs.
    allow_freeform_uid = '–allow-freeform-uid'

    # GnuPG normally checks that the timestamps associated with keys and
    # signatures have plausible values. However, sometimes a signature seems
    # to be older than the key due to clock problems. This option makes these
    # checks just a warning.
    ignore_time_conflict = '–ignore-time-conflict'

    # Lock the databases the first time a lock is requested and do not release
    # the lock until the process terminates.
    lock_once = '–lock-once'

    # Release the locks every time a lock is no longer needed. Use this to
    # override a previous –lock-once from a config file.
    lock_multiple = '–lock-multiple'

    # Disable locking entirely. This option should be used only in very special
    # environments, where it can be assured that only one process is accessing
    # those files. A bootable floppy with a standalone encryption system will
    # probably use this. Improper usage of this option may lead to data and key
    # corruption.
    lock_never = '–lock-never'

    # GnuPG uses a file to store it's internal random pool over invocations.
    # This makes random generation faster; however sometimes write operations
    # are not desired. This option can be used to achive that with the cost of
    # slower random generation.
    no_random_seed_file = '–no-random-seed-file'

    # Reset verbose level to 0.
    no_verbose = '–no-verbose'

    # Suppress the initial copyright message but do not enter batch mode.
    no_greeting = '–no-greeting'

    # Suppress the warning about "using insecure memory".
    no_secmem_warning = '–no-secmem-warning'

    # Assume the input data is not in ASCII armored format.
    no_armor = '–no-armor'

    # Do not add the default keyrings to the list of keyrings.
    no_default_keyring = '–no-default-keyring'

    # Skip the signature verification step. This may be used to make the
    # decryption faster if the signature verification is not needed.
    skip_verify = '–skip-verify'

    # Print key listings delimited by colons.
    with_colons = '–with-colons'

    # Print key listings delimited by colons and print the public key data.
    with_key_data = '–with-key-data'

    # Same as the command –fingerprint but changes only the format of the
    # output and may be used together with another command.
    with_fingerprint = '–with-fingerprint'

    # Changes the output of the list commands to work faster; this is achieved
    # by leaving some parts empty. Some applications don't need the user ID and
    # the trust information given in the listings. By using this options they
    # can get a faster listing. The excact behaviour of this option may change
    # in future versions.
    fast_list_mode = '–fast-list-mode'

    # Changes the behaviour of some commands. This is like –dry-run but
    # different in some cases. The semantic of this command may be extended in
    # the future. Currently it does only skip the actual decryption pass and
    # therefore enables a fast listing of the encryption keys.
    list_only = '–list-only'

    # This is not for normal use. Use the source to see for what it might be
    # useful.
    no_literal = '–no-literal'

    # This is not for normal use. Use the source to see for what it might be
    # useful.
    set_filesize = '–set-filesize'

    # GnuPG versions prior to 1.0.2 had a bug in the way a signature was
    # encode. This options enables a workaround by checking faulty signatures
    # again with the encoding used in old versions. This may only happen for
    # ElGamal signatures which are not widely used.
    emulate_md_encode_bug = '–emulate-md-encode-bug'

    # Display the session key used for one message. See –override-session-key
    # for the counterpart of this option. We think that Key-Escrow is a
    # Bad Thing; however the user should have the freedom to decide whether
    # to go to prison or to reveal the content of one specific message without
    # compromising all messages ever encrypted for one secret key.
    # DON'T USE IT UNLESS YOU ARE REALLY FORCED TO DO SO.
    show_session_key = '–show-session-key'

    # Don't use the public key but the session key string. The format of this
    # string is the same as the one printed by –show-session-key. This option
    # is normally not used but comes handy in case someone forces you to reveal
    # the content of an encrypted message; using this option you can do this
    # without handing out the secret key.
    override_session_key = '–override-session-key'

    # Don't insert new keys into the keyrings while doing an import.
    merge_only = '–merge-only'

    # Don't look at the key ID as stored in the message but try all secret keys
    # in turn to find the right decryption key. This option forces the
    # behaviour as used by anonymous recipients (created by using –throw-keyid)
    #  and might come handy in case where an encrypted message contains a
    # bogus key ID.
    try_all_secrets = '–try-all-secrets'
