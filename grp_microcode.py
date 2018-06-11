#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

microcode = [
    {'name':'generic', 
    'shortdesc':'generic microcode/firmware package', 
    'description':'Installs the microcode/firmware package for any kind of CPU', 
    'packages':['linux-firmware', 'intel-microcode', 'amd64-microcode']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls any firmware package', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
