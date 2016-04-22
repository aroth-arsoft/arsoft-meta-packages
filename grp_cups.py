#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

cups = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the cups',
    'description':'', 
    'packages':['cups-client'],
    },
    {'name':'server',
    'shortdesc':'Installs the server part of cups',
    'description':'', 
    'depends':['common'],
    'packages':['cups', 'printer-driver-postscript-hp', 'printer-driver-hpijs'],
    'packages-wily':['printer-driver-cups-pdf'],
    'packages-xenial':['printer-driver-cups-pdf'],
    },
    {'name':'none',
    'shortdesc':'Uninstalls cups',
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
