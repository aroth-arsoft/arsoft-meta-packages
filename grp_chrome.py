#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

chrome = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Google Chrome', 
    'packages':['google-chrome-stable', 'icedtea-7-plugin'],
    'conflicts':['google-chrome-unstable', 'google-chrome-beta'],
    'files': [
        ('chrome/google-chrome', 'google-chrome', 0755),
        ('chrome/google-chrome-stable', 'google-chrome-stable', 0755),
        ],
    'divert': [
        ('/usr/bin/google-chrome', 'google-chrome'),
        ('/usr/bin/google-chrome-stable', 'google-chrome-stable'),
        ]
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Google Chrome', 
    'packages':[], 
    'noconflicts':['icedtea-7-plugin']
    },
]
 
