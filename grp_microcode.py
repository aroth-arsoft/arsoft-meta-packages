#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

microcode = [
    {'name':'generic', 
    'shortdesc':'generic microcode/firmware package', 
    'description':'Installs the microcode/firmware package for any kind of CPU', 
    'packages':['linux-firmware'],
    'replaces':['arsoft-microcode-intel', 'arsoft-microcode-amd'],
    'noconflicts':['amd64-microcode']
    },
    {'name':'intel', 
    'shortdesc':'Installs the microcode package for Intel CPUs', 
    'description':'Installs the only the microcode package for Intel CPUs without any other firmware (e.g. for wireless adapters)', 
    'packages':['intel-microcode']
    },
    {'name':'amd', 
    'shortdesc':'Installs the microcode package for AMD CPUs', 
    'description':'Installs the the microcode package for AMD CPUs and firmware for other devices', 
    'packages':['amd64-microcode']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls any firmware package', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
