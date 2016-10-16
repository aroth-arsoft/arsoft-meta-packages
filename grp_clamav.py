#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

clamav = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the ClamAV',
    'description':'', 
    'packages':['clamav', 'clamav-freshclam', 'clamav-daemon'],
    },
    {'name':'none',
    'shortdesc':'Uninstalls ClamAV',
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
