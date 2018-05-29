#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

trac = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of trac',
    'description':'', 
    'packages':['trac',
                'trac-mastertickets', 'trac-workflowadmin', 'trac-xmlrpc', 'trac-advancedworkflow', 'trac-announcer',
                'trac-navadd', 'trac-customfieldadmin', 'trac-iniadmin',
                'trac-hudson', 'trac-timingandestimation', 'trac-crashdump',
                'trac-clients',
                'arsoft-trac-commitupdater'
                ]
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of trac',
    'description':'', 
    'packages':[]
    },
]
