#!/usr/bin/env python

from distutils.core import setup
import os, sys

data_files = []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)

less_dir = os.path.join('less.js')
os.chdir(less_dir)

# Copy the lib js files
for dirpath, dirnames, filenames in os.walk(os.path.join('lib', 'less')):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    # Add all the js files
    for f in filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

# Copy the binary script too
scripts = [os.path.join('bin', 'lessc')]

setup(name='less',
    version = '1.0',
    description = 'Use pip to install LESS the nice way',
    author = 'Wil Linssen',
    url = 'http://github.com/linssen/',
    license = 'GNU GPL v3',
    scripts = scripts,
    data_files = data_files,
)
