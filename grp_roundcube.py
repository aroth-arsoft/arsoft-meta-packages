#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

roundcube = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of roundcube', 
    'description':'', 
    'packages':['roundcube-plugins', 'roundcube-plugins-extra', 'roundcube-amacube']
    },
    {'name':'mysql', 
    'shortdesc':'Installs roundcube using MySQL database', 
    'description':'', 
    'depends':['common'],
    'packages':['roundcube-mysql']
    },
    {'name':'pgsql', 
    'shortdesc':'Installs roundcube using PostgreSQL database', 
    'description':'', 
    'depends':['common'],
    'packages':['roundcube-pgsql']
    },
    {'name':'sqlite3', 
    'shortdesc':'Installs roundcube using SQLite3 database', 
    'description':'', 
    'depends':['common'],
    'packages':['roundcube-sqlite3']
    },
    
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of roundcube', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
