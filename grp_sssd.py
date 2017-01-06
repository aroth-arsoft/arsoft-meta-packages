#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

sssd = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of System Security Services Daemon (SSSD)',
    'description':'', 
    'packages':['sssd', 'sssd-tools', 'adcli']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of System Security Services Daemon (SSSD)',
    'description':'', 
    'packages':[]
    },
]
