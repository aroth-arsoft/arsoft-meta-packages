#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

thunderbird = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Thunderbird', 
    'description':'', 
    'packages':['thunderbird', 'browser-plugin-packagekit']
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME support files for Mozilla Thunderbird', 
    'description':'This package installs Mozilla Thunderbird GNome support.', 
    'depends':['common'],
    'packages':['thunderbird-gnome-support'], 
    'side-by-side':['english', 'german'],
    'noconflicts':['kmozillahelper', 'kde-config-gtk']
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE support files for Mozilla Thunderbird', 
    'description':'This package installs Mozilla Thunderbird KDE support.', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':['kmozillahelper', 'kde-config-gtk'], 
    },
    {'name':'english', 
    'shortdesc':'Installs the english languages files for Mozilla Thunderbird', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['kde', 'gnome', 'german'],
    'packages':['thunderbird-locale-en-us']
    },
    {'name':'german', 
    'shortdesc':'Installs the german languages files for Mozilla Thunderbird', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['kde', 'gnome', 'english'],
    'packages':['thunderbird-locale-de']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Thunderbird', 
    'description':'', 
    'packages':[], 
    'noconflicts':['kmozillahelper', 'kde-config-gtk', 'browser-plugin-packagekit']
    },
]
 
