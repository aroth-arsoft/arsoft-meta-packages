#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

sddm = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Simple Desktop Display Manager (SDDM)',
    'description':'', 
    'packages':['sddm', 'sddm-theme-elarun', 'sddm-theme-maldives', 'sddm-theme-maui', 'sddm-theme-breeze']
    'packages-xenial': ['sddm-theme-circles' ],
    'packages-bionic': ['sddm-theme-debian-elarun', 'sddm-theme-debian-maui', 'sddm-theme-maya'],
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Simple Desktop Display Manager (SDDM)',
    'description':'', 
    'packages':[]
    },
]
