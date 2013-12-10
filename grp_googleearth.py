#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

googleearth = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Google Earth', 
    'description':'', 
    'packages':[('google-earth-stable', 'googleearth', 'googleearth-package')],
    'conflicts':[]
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Google Earth', 
    'description':'', 
    'packages':[], 
    'noconflicts':[],
    'conflicts':[]
    },
]
 
