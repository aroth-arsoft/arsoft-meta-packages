#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

microcode = [
    {'name':'intel', 
    'shortdesc':'Installs the microcode package for Intel CPUs', 
    'description':'', 
    'depends':['common'],
    'packages':['intel-microcode']
    },
    {'name':'amd', 
    'shortdesc':'Installs the microcode package for AMD CPUs', 
    'description':'', 
    'depends':['common'],
    'packages':[('amd64-microcode', 'linux-firmware')]
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Java', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
