#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

chromium = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Chromium', 
    'description':'', 
    'packages':['chromium-browser', 'chromium-codecs-ffmpeg'],
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Chromium', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
 
