#!/usr/bin/env python

from distutils.core import setup
import os, sys

data_files = [
        ('lib/less', [
            'less.js/lib/less/browser.js',
            'less.js/lib/less/colors.js',
            'less.js/lib/less/cssmin.js',
            'less.js/lib/less/functions.js',
            'less.js/lib/less/index.js',
            'less.js/lib/less/parser.js',
            'less.js/lib/less/rhino.js',
            'less.js/lib/less/tree.js',
        ]),
        ('lib/less/tree', [
            'less.js/lib/less/tree/alpha.js',
            'less.js/lib/less/tree/anonymous.js',
            'less.js/lib/less/tree/assignment.js',
            'less.js/lib/less/tree/call.js',
            'less.js/lib/less/tree/color.js',
            'less.js/lib/less/tree/comment.js',
            'less.js/lib/less/tree/condition.js',
            'less.js/lib/less/tree/dimension.js',
            'less.js/lib/less/tree/directive.js',
            'less.js/lib/less/tree/element.js',
            'less.js/lib/less/tree/expression.js',
            'less.js/lib/less/tree/import.js',
            'less.js/lib/less/tree/javascript.js',
            'less.js/lib/less/tree/keyword.js',
            'less.js/lib/less/tree/mixin.js',
            'less.js/lib/less/tree/operation.js',
            'less.js/lib/less/tree/paren.js',
            'less.js/lib/less/tree/quoted.js',
            'less.js/lib/less/tree/rule.js',
            'less.js/lib/less/tree/ruleset.js',
            'less.js/lib/less/tree/selector.js',
            'less.js/lib/less/tree/url.js',
            'less.js/lib/less/tree/value.js',
            'less.js/lib/less/tree/variable.js',
        ]),
    ]

setup(name='less',
    version = '1.0',
    description = 'Use pip to install LESS the nice way',
    author = 'Wil Linssen',
    url = 'http://github.com/linssen/',
    license = 'GNU GPL v3',
    scripts = ['less.js/bin/lessc'],
    data_files = data_files,
)
