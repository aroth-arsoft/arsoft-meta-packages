#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

desktop = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the common packages for desktop workstations', 
    'description':'', 
    'packages':['ttf-mscorefonts-installer', 
                'policykit-desktop-privileges',
                ],
    'conflicts':[
                    'unclutter',
                    'ibus-qt4', 'ibus-gtk', 'libibus-qt1',
                    'scim', 'scim-qtimm', 'scim-modules-socket']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all common desktop packages', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    }
]
