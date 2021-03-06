#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

networkmanager = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'installs the network manager', 
    'description':'basic network manager', 
    'packages':[ 'network-manager'],
    },
    {'name':'console', 
    'shortdesc':'Installs console interface for network manager', 
    'description':'Installs console interface for network manager.', 
    'depends':['common'],
    'side-by-side':['gnome', 'kde'],
    'packages':[],
    },
    {'name':'kde',
    'shortdesc':'Installs KDE plasma interface for network manager', 
    'description':'Installs KDE plasma interface for network manager.', 
    'depends':['common'],
    'side-by-side':['gnome', 'console', 'kde'],
    'packages':['plasma-widget-networkmanagement']
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME interface for network manager', 
    'description':'Installs GNOME interface for network manager.', 
    'depends':['common'],
    'side-by-side':['console', 'kde'],
    'packages':['network-manager-gnome', 'network-manager-pptp-gnome', 'network-manager-openvpn-gnome', 'network-manager-vpnc-gnome']
    },
    {'name':'none', 
    'shortdesc':'removes the network manager completely.', 
    'description':'removes the network manager completely.', 
    'packages':[], 
    'noconflicts':[]
    },
]
