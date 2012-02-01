#!/usr/bin/env python

from distutils.core import setup
import os, shutil

def install_lib():
    """
    Copies the less lib files into where lessc can read them
    """
    src = os.path.join('less.js', 'lib', 'less')
    dst = os.path.join('lib', 'less')
    try:
        shutil.copytree(src, dst)
    except:
        # directory already exists, so we're good
        pass

install_lib()

setup(name='less',
    version = '1.0',
    description = 'Use pip to install LESS the nice way',
    author = 'Wil Linssen',
    url = 'http://github.com/linssen/',
    license = 'GNU GPL v3',
    scripts = ['less.js/bin/lessc'],
)
