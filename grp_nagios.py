#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

nagios = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the common nagios files', 
    'description':'This package installs the latest version of Nagios.', 
    'packages':['arsoft-base']
    },
    {'name':'plugins',
    'shortdesc':'Installs Nagios plugins',
    'description':'Installs the basic, standard, extra and contrib plugins.',
    'depends':[],
    'packages':['nagios-plugins-basic', 'nagios-plugins-extra', 'nagios-plugins-standard', 'nagios-plugins-contrib'],
    },
    {'name':'agent', 
    'shortdesc':'Installs Nagios agent', 
    'description':'', 
    'depends':['common', 'plugins'],
    'packages':['nagios-plugins-arsoft', 'nagios-nrpe-server'],
    'noconflicts': ['nagios-images']
    },
    {'name':'server', 
    'shortdesc':'Installs Nagios server', 
    'description':'', 
    'depends':['common', 'plugins'],
    'packages':['arsoft-nagios-plugins', 'nagios-nrpe-plugin', 'nagios-nrpe-server',
                'nagios3', 'nagios3-cgi', 'nagios3-core', 'nagios-images']
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Nagios monitoring solution', 
    'description':'This package removes all versions of Nagios monitoring solution.', 
    'packages':[],
    'noconflicts':['arsoft-base', 'nagios-images']
    },
]
 
