#!/usr/bin/env python
import md5
import urllib2
import tarfile
import os
from subprocess import Popen

VIRTUALENV_PATH = '.virtualenvs/pycontw'
VIRTUALENV_VERSION = '1.10.1'
VIRTUALENV_MD5 = '3a04aa2b32c76c83725ed4d9918e362e'
TEMP_DIR = '/tmp'


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
        if not checkMD5(fb, VIRTUALENV_MD5):
            raise Exception('MD5 Error! Be Careful.')
        print('Writing to %s' % filename)
        f.write(fb)
    with tarfile.open(filename) as tar:
        print('Extracting %s' % filename)
        tar.extractall()


def make_virtualenv():
    fileurl = (
        'https://pypi.python.org/'
        'packages/source/v/virtualenv/virtualenv-{}.tar.gz'.format(
            VIRTUALENV_VERSION
        ))
    filename = fileurl.split('/')[-1]
    if not os.path.exists(filename):
        get_virtualenv_file(fileurl)
    cmd(['python', '{}/virtualenv.py'.format(filename[:-7]), VIRTUALENV_PATH])
    cmd(['rm', '-rf', '{}/'.format(filename[:-7])])


def main():
    make_virtualenv()
    cmd(['{}/bin/pip'.format(VIRTUALENV_PATH),
         'install', '-r', 'requirements/project.txt'])
    cmd(['{}/bin/fab'.format(VIRTUALENV_PATH), 'deploy:developer'])


if __name__ == '__main__':
    main()
