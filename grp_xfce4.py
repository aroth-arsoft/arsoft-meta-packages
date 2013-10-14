#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

xfce4 = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the XFCE desktop environment', 
    'description':'This package installs the latest version of XFCE desktop environment and removes obsolete and old packages of XFCE desktop environment.', 
    'packages':['arsoft-desktop',
                'xfce4-session', 'xfce4-mixer', 'xfce4-panel', 'xfce4-appfinder', 'xfce4-settings', 'xfwm4', 'gtk2-engines-xfce', 
                'xfce-keyboard-shortcuts', 'xfce4-screenshooter', 'xfce4-volumed', 
                'xfce4-notifyd', 'xfdesktop4', 'thunar', 'tumbler',
                'xfce4-taskmanager', 'xfce4-terminal', 'xfce4-places-plugin', 'xfce4-indicator-plugin'
                ], 
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the XFCE desktop environment', 
    'description':'This package removes all versions of XFCE desktop environment.', 
    'packages':[],
    'noconflicts':['arsoft-desktop']
    },
]
