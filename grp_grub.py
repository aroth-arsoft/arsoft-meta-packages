#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

grub = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of grub', 
    'description':'', 
    'packages':['grub2-common' ]
    },
    {'name':'bios', 
    'shortdesc':'Installs the GRUB for systems with BIOS', 
    'description':'', 
    'packages':['grub2']
    },
    {'name':'efi-amd64', 
    'shortdesc':'Installs the GRUB for 64-bit EFI systems', 
    'description':'', 
    'packages':['grub-efi-amd64', 'efibootmgr']
    },
    {'name':'efi-ia32', 
    'shortdesc':'Installs the GRUB for 32-bit EFI systems', 
    'description':'', 
    'packages':['grub-efi-ia32', 'efibootmgr']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of grub (not recommended)', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
