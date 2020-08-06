#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

chrome = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Google Chrome', 
    'packages':['google-chrome-stable'],
    'conflicts':['google-chrome-unstable', 'google-chrome-beta'],
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Google Chrome', 
    'packages':[], 
    'noconflicts':[]
    },
]
 
