#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

firefox = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Firefox', 
    'description':'', 
    'packages':['firefox', 'xul-ext-ubufox',
                'firefox-locale-en', 'firefox-locale-de']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Firefox', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
