#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

dovecot = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of the Dovecot mail server',
    'description':'', 
    'packages':['dovecot-core', 'dovecot-antispam', 'dovecot-imapd', 'dovecot-pop3d',
                'dovecot-gssapi', 'dovecot-lmtpd', 'dovecot-managesieved', 'dovecot-solr', 'dovecot-lucene' ]
    },
    {'name':'mysql',
    'shortdesc':'Installs the latest version of the Dovecot mail server with MySQL support',
    'description':'',
    'depends':['common'],
    'packages':['dovecot-mysql'],
    },
    {'name':'pgsql',
    'shortdesc':'Installs the latest version of the Dovecot mail server with PostgreSQL support',
    'description':'',
    'depends':['common'],
    'packages':['dovecot-pgsql'],
    },
    {'name':'sqlite',
    'shortdesc':'Installs the latest version of the Dovecot mail server with SQLite support',
    'description':'',
    'depends':['common'],
    'packages':['dovecot-sqlite'],
    },
    {'name':'none',
    'shortdesc':'Uninstalls all versions of the Dovecot mail server',
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
