#!/usr/bin/env python
"Usage: python make_virtualenv.py [.venv]"

import os
import sys
import md5
import urllib2
import tarfile
from subprocess import Popen

DEFAULT_VENV_PREFIX = ".venv"
DEFAULT_VENV_VERSION = '1.10.1'
DEFAULT_VIRTUALENV_MD5 = '3a04aa2b32c76c83725ed4d9918e362e'

VENV_PREFIX_FILE = "venv_prefix"


def write_venv_prefix(prefix, venv_prefix_file=VENV_PREFIX_FILE):
    print('Writing virtualenv prefix into file "{}"'.format(venv_prefix_file))
    with open(venv_prefix_file, 'wb') as f:
        f.write(prefix)

def get_venv_prefix(venv_prefix_file=VENV_PREFIX_FILE):
    if os.path.exists(venv_prefix_file):
        with open(venv_prefix_file, 'rb') as f:
            venv_prefix = f.readline().strip()
        if not venv_prefix:
            print("Warning: blank first line of {}".format(venv_prefix_file))
            venv_prefix = DEFAULT_VENV_PREFIX
    else:
        venv_prefix = DEFAULT_VENV_PREFIX
    abspath = os.path.abspath(os.path.expanduser(venv_prefix))
    print("Using virtualenv prefix: {}".format(abspath))
    return abspath


def cmd(args):
    Popen(args).wait()


def checkMD5(fb, md5str):
    md5obj = md5.new(fb)
    return md5obj.hexdigest() == md5str


def get_virtualenv_file(fileurl):
    filename = fileurl.split('/')[-1]
    req = urllib2.Request(fileurl)
    print('Fetching %s' % fileurl)
    conn = urllib2.urlopen(req)
    fb = conn.read()
    conn.close()
    with open(filename, 'w') as f:
        print('Checking MD5')
        if not checkMD5(fb, DEFAULT_VIRTUALENV_MD5):
            raise Exception('MD5 Error! Be Careful.')
        print('Writing to %s' % filename)
        f.write(fb)


def extract_virtual_env_tarball(filename):
    with tarfile.open(filename) as tar:
        print('Extracting %s' % filename)
        tar.extractall()


def print_summary(venv_prefix):
    summary = """
PyConTW environment setup is complete.

To activate the virtualenv for the extent of your current shell session you
can run:

$ source %s/bin/activate
""" % venv_prefix
    print summary


def make_virtualenv(venv_prefix):
    fileurl = (
        'https://pypi.python.org/'
        'packages/source/v/virtualenv/virtualenv-{}.tar.gz'.format(
            DEFAULT_VENV_VERSION
        ))
    filename = fileurl.split('/')[-1]
    try:
        import virtualenv
    except ImportError:
        if not os.path.exists(filename):
            get_virtualenv_file(fileurl)
        if not os.path.exists(filename.split('.')[1]):
            extract_virtual_env_tarball(filename)
        cmd(['python', '{}/virtualenv.py'.format(filename[:-7]), venv_prefix])
        cmd(['rm', '-rf', '{}/'.format(filename[:-7])])
    else:
        virtualenv.create_environment(venv_prefix)
        print_summary(venv_prefix)


def main():
    if len(sys.argv) > 1:
        venv_prefix = sys.argv[1]
        if venv_prefix != DEFAULT_VENV_PREFIX:
            write_venv_prefix(venv_prefix)
    else:
        venv_prefix = get_venv_prefix()
    make_virtualenv(venv_prefix)


if __name__ == '__main__':
    main()
