#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

cyrusimapd = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'installs the cyrus imap server', 
    'description':'common cyrus imap server', 
    'packages':['arsoft-scripts-cyrusimapd' ],
    },
    {'name':'2.2', 
    'shortdesc':'Installs version 2.2.x of cyrus-imapd', 
    'description':'Installs version 2.2.x of cyrus-imapd.', 
    'depends':['common'],
    'side-by-side':['2.2', '2.4', '2.4-clients'],
    'packages':['cyrus-common-2.2', 'cyrus-admin-2.2', 'cyrus-clients-2.2', 'cyrus-imapd-2.2', 
                'cyrus-pop3d-2.2', 'cyrus-nntpd-2.2', 'cyrus-murder-2.2', 'cyrus-replication-2.2']
    },
    {'name':'2.4', 
    'shortdesc':'Installs version 2.4.x of cyrus-imapd', 
    'description':'Installs version 2.4.x of cyrus-imapd.', 
    'depends':['common'],
    'side-by-side':['2.2', '2.4', '2.4-clients'],
    'packages':['cyrus-common-2.4', 'cyrus-admin-2.4', 'cyrus-clients-2.4', 'cyrus-imapd-2.4', 
                'cyrus-pop3d-2.4', 'cyrus-nntpd-2.4', 'cyrus-murder-2.4', 'cyrus-replication-2.4']
    },
    {'name':'2.4-clients', 
    'shortdesc':'Installs version 2.4.x of cyrus-imapd', 
    'description':'Installs version 2.4.x of cyrus-imapd.', 
    'depends':[],
    'side-by-side':['2.2', '2.4', '2.4-clients'],
    'packages':['cyrus-clients-2.4']
    },
    {'name':'none', 
    'shortdesc':'removes the network manager completely.', 
    'description':'removes the network manager completely.', 
    'packages':[], 
    'noconflicts':[]
    },
]
