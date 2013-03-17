#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

nagios = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the common nagios files', 
    'description':'This package installs the latest version of Nagios.', 
    'packages':['arsoft-base', 'nagios-nrpe-plugin']
    },
    {'name':'agent', 
    'shortdesc':'Installs Nagios agent', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['server'],
    'packages':['arsoft-nagios-plugins', 'nagios-nrpe-server', 'nagios-plugins-basic', 'nagios-plugins-extra', 'nagios-plugins-standard', 'nagios-plugins-contrib']
    },
    {'name':'server', 
    'shortdesc':'Installs Nagios server', 
    'description':'', 
    'depends':['common', 'agent'],
    'side-by-side':['agent'],
    'packages':['nagios3', 'nagios3-cgi', 'nagios3-core']
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Nagios monitoring solution', 
    'description':'This package removes all versions of Nagios monitoring solution.', 
    'packages':[],
    'noconflicts':['arsoft-base']
    },
]
 
