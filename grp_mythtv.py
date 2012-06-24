#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

mythtv = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the MythTV environment', 
    'description':'This package installs the latest version of MythTV environment and removes obsolete and old packages of MythTV.', 
    'packages':['arsoft-desktop', 'mythtv-common', 'arsoft-scripts-mythtv' ],
    'noconflicts':['mythweb']
    },
    {'name':'database', 
    'depends':['common'],
    'side-by-side':['database', 'backend', 'frontend', 'web' ],
    'shortdesc':'Installs the MythTV database', 
    'description':'Installs the files required to set up and maintain the MythTV database.', 
    'packages':['mythtv-database'], 
    },
    {'name':'backend', 
    'depends':['common'],
    'side-by-side':['database', 'backend', 'frontend', 'web' ],
    'shortdesc':'Installs the MythTV backend', 
    'description':'Installs the MythTV backend.', 
    'packages':['mythtv-backend'], 
    },
    {'name':'frontend', 
    'shortdesc':'Installs the MythTV frontend', 
    'description':'Installs the MythTV frontend.', 
    'depends':['common'],
    'side-by-side':['database', 'backend', 'frontend', 'web' ],
    'packages':[ 'ttf-mscorefonts-installer', 
                "mytharchive", "mythbrowser", "mythgallery", "mythgame", "mythmusic", "mythnetvision", "mythnews", "mythweather" ], 
    },
    {'name':'web', 
    'shortdesc':'Installs the MythTV web configuration', 
    'description':'Installs the MythTV web configuration.', 
    'depends':['common', 'frontend' ],
    'side-by-side':['database', 'backend', 'frontend', 'web' ],
    'packages':["mythweb"], 
    },
    {'name':'none', 
    'shortdesc':'removes all MythTV packages', 
    'description':'removes all MythTV packages.', 
    'packages':[], 
    'noconflicts':['arsoft-desktop']
    },
]
 
