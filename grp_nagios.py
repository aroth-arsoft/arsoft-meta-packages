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
    'packages':['arsoft-nagios-plugins', 'nagios-nrpe-server', 'nagios-plugins-basic', 'nagios-plugins-extra', 'nagios-plugins-standard', 'nagios-plugins-contrib'],
    'noconflicts': ['nagios-images']
    },
    {'name':'server', 
    'shortdesc':'Installs Nagios server', 
    'description':'', 
    'depends':['common'],
    'packages':['arsoft-nagios-plugins', 'nagios-nrpe-server', 'nagios-plugins-basic', 'nagios-plugins-extra', 'nagios-plugins-standard', 'nagios-plugins-contrib', 
                'nagios3', 'nagios3-cgi', 'nagios3-core', 'nagios-images']
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Nagios monitoring solution', 
    'description':'This package removes all versions of Nagios monitoring solution.', 
    'packages':[],
    'noconflicts':['arsoft-base']
    },
]
 
