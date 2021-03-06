#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

icinga = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the Icinga monitoring solution', 
    'description':'This package installs the latest version of Icinga monitoring solution.', 
    'packages':['arsoft-base', 'arsoft-nagios-plugins', 'nagios-notifications',
                'arsoft-pnp4nagios', 'nagios-images',
                'pnp4nagios',
                'arsoft-python-nagios',
                ],
    'conflicts':['arsoft-nagios-server', 'nagios3', 'nagios3-cgi', 'nagios3-core']
    },
    {'name':'v1',
    'shortdesc':'Installs version 1.x of Icinga',
    'description':'This package installs version 1.x of Icinga.',
    'depends':['common'],
    'packages':['icinga',
                'icinga-common',
                'icinga-core',
                'icinga-cgi',
                'icinga-doc',
                'icinga-idoutils'],
    'side-by-side':['v2']
    },
    {'name':'v2',
    'shortdesc':'Installs version 2.x of Icinga',
    'description':'This package installs version 2.x of Icinga.',
    'depends':['common'],
    'packages':['icinga2',
                'icinga2-bin',
                'icinga2-classicui',
                'icinga2-common',
                'icinga2-doc',
                'icinga2-ido-mysql'],
    'side-by-side':['v1']
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the Icinga monitoring solution', 
    'description':'This package removes all versions of Icinga monitoring solution.', 
    'packages':[],
    'noconflicts':['arsoft-base', 'arsoft-nagios-plugins', 'nagios-notifications', 'nagios-images']
    },
]
