#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

thunderbird = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Thunderbird', 
    'description':'', 
    'packages':['thunderbird', 'thunderbird-locale-en', 'thunderbird-locale-de',
                'browser-plugin-packagekit',
                'xul-ext-lightning', 'xul-ext-gdata-provider']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Thunderbird', 
    'description':'', 
    'packages':[], 
    'noconflicts':['browser-plugin-packagekit']
    },
]
