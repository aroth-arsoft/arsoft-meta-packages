#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

unity = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the Unity desktop environment', 
    'description':'This package installs the latest version of Unity desktop environment and removes obsolete and old packages of Unity desktop environment.', 
    'packages':['arsoft-desktop',
                'unity', 'unity-common'],
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Unity desktop environment', 
    'description':'This package removes all versions of Unity desktop environment.', 
    'packages':[],
    'noconflicts':['arsoft-desktop']
    },
]
