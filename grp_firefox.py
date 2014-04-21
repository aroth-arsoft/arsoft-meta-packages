#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

firefox = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Mozilla Firefox', 
    'description':'', 
    'packages':['firefox', 'firefox-launchpad-plugin', 'xul-ext-ubufox',
                'firefox-locale-en', 'firefox-locale-de',
                'browser-plugin-packagekit', 'browser-plugin-vlc', 'icedtea-7-plugin'],
    'conflicts': ['gnash', 'gnash-common', 'browser-plugin-gnash', 'browser-plugin-lightspark', 'swfdec-mozilla', 'adblock-plus', 'xul-ext-adblock-plus', 'kubuntu-firefox-installer' ],
    'replaces': ['firefox-3.5', 'firefox-3.1', 'firefox-3.0']
    # 'xul-ext-ubufox' pulls in 'apturl'
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME support files for Mozilla Firefox', 
    'description':'This package installs Mozilla Firefox GNome support.', 
    'depends':['common'],
    'packages':['firefox-gnome-support', 'xul-ext-gnome-pm'], 
    'side-by-side':['gnome', 'kde']
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE support files for Mozilla Firefox', 
    'description':'This package installs Mozilla Firefox KDE support.', 
    'depends':['common'],
    'side-by-side':['gnome', 'kde']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Mozilla Firefox', 
    'description':'', 
    'packages':[], 
    'noconflicts':['browser-plugin-packagekit', 'browser-plugin-vlc', 'icedtea-7-plugin']
    },
]
