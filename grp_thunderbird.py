#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

thunderbird = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Thunderbird', 
    'description':'', 
    'packages':['thunderbird', 'thunderbird-locale-en', 'thunderbird-locale-de', 'browser-plugin-packagekit']
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME support files for Mozilla Thunderbird', 
    'description':'This package installs Mozilla Thunderbird GNome support.', 
    'depends':['common'],
    'packages':['thunderbird-gnome-support'], 
    'side-by-side':['gnome', 'kde']
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE support files for Mozilla Thunderbird', 
    'description':'This package installs Mozilla Thunderbird KDE support.', 
    'depends':['common'],
    'side-by-side':['gnome', 'kde']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Thunderbird', 
    'description':'', 
    'packages':[], 
    'noconflicts':['browser-plugin-packagekit']
    },
]
