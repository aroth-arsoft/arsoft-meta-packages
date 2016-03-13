#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

firefox = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Firefox', 
    'description':'', 
    'packages':['firefox', 'firefox-launchpad-plugin', 'xul-ext-ubufox',
                'firefox-locale-en', 'firefox-locale-de',
                'browser-plugin-packagekit', 'browser-plugin-vlc', 'icedtea-plugin'],
    'conflicts': ['gnash', 'gnash-common', 'browser-plugin-gnash'],
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Firefox', 
    'description':'', 
    'packages':[], 
    'noconflicts':['browser-plugin-packagekit', 'browser-plugin-vlc', 'icedtea-plugin']
    },
]
