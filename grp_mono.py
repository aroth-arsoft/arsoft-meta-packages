#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

mono = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mono', 
    'description':'', 
    'packages':['mono-runtime', 'cli-common' ]
    },
    {'name':'developer', 
    'shortdesc':'Installs the Mono development tools', 
    'description':'', 
    'packages':['mono-devel' ]
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mono', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
 
