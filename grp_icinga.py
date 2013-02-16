#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

icinga = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the Icinga monitoring solution', 
    'description':'This package installs the latest version of Icinga monitoring solution.', 
    'packages':['arsoft-base', 'icinga-common', 'icinga-core', 'icinga-cgi', 'icinga-doc', 'icinga-web', 'icinga-idoutils', 'icinga' ]
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Icinga monitoring solution', 
    'description':'This package removes all versions of Icinga monitoring solution.', 
    'packages':[],
    'noconflicts':['arsoft-base']
    },
]
 
