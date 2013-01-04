#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

lightdm = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of LightDM', 
    'description':'', 
    'packages':['lightdm']
    },
    {'name':'gtk', 
    'shortdesc':'Installs GTK+ Greeter for LightDM', 
    'description':'Installs GTK+ Greeter for LightDM.', 
    'depends':['common'],
    'packages':['lightdm-gtk-greeter']
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE Greeter for LightDM', 
    'description':'Installs KDE Greeter for LightDM.', 
    'depends':['common'],
    'packages':['lightdm-kde-greeter']
    },
    {'name':'webkit', 
    'shortdesc':'Installs WebKit Greeter for LightDM', 
    'description':'Installs WebKit Greeter for LightDM.', 
    'depends':['common'],
    'packages':['lightdm-webkit-greeter']
    },
    {'name':'unity', 
    'shortdesc':'Installs Unity Greeter for LightDM', 
    'description':'Installs Unity Greeter for LightDM.', 
    'depends':['common'],
    'packages':['unity-greeter']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of LightDM', 
    'description':'', 
    'packages':[]
    },
]
 
