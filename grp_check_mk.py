#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

check_mk = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the check_mk',
    'description':'', 
    'packages':[],
    'side-by-side':['agent', 'icinga']
    },
    {'name':'agent',
    'shortdesc':'Installs the agent for check_mk',
    'description':'', 
    'depends':['common'],
    'packages':['check-mk-agent', 'arsoft-check-mk-plugins']
    },
    {'name':'server',
    'shortdesc':'Installs the check_mk server component',
    'description':'',
    'depends':['agent'],
    'packages':['check-mk-server', 'arsoft-check-mk-checks']
    },
    {'name':'icinga',
    'shortdesc':'Installs the check_mk for Icinga',
    'description':'', 
    'depends':['server'],
    'packages':['check-mk-config-icinga', 'check-mk-livestatus']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of check_mk',
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
