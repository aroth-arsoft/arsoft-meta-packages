#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

developer = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the the basic set of development tools', 
    'description':'basic development tools', 
    'packages':[ 'libc6-dev', 'manpages-dev',
                'gcc', 'g++', 'make',
                'cmake', 'cmake-curses-gui', 
                'dpkg-dev', 'devscripts', 'cdbs', 'debhelper', 'quilt',
                'git', 'ack',
                ],
    },
    {'name':'qt',
    'shortdesc':'Installs Qt development tools',
    'description':'Installs the Qt development tools.',
    'depends':['common'],
    'side-by-side':['gnome', 'kde', 'kdevelop'],
    'packages':[
                'cmake-qt-gui',
                'qttools5-dev-tools',
                ]
    },
    {'name':'kde',
    'shortdesc':'Installs KDE development tools',
    'description':'Installs the KDE development tools.',
    'depends':['qt'],
    'side-by-side':['gnome', 'qt', 'kdevelop'],
    'packages':[
                'kcachegrind-converters',
                ]
    },
    {'name':'kdevelop',
    'shortdesc':'installs KDevelop',
    'description':'include KDevelop and the following plugins: python, php',
    'depends':['kde'],
    'side-by-side':['gnome', 'kde', 'qt'],
    'packages':[ 'kdevelop', 'kdevelop-l10n',
                 'kdevelop-python', 'kdevelop-python-l10n',
                 'kdevelop-php', 'kdevelop-php-l10n'],
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME development tools', 
    'description':'Installs the GNOME development tools.', 
    'depends':['common'],
    'side-by-side':['kde', 'qt', 'kdevelop'],
    'packages':[], 
    },
    {'name':'none', 
    'shortdesc':'removes all development tools.', 
    'description':'This package removes all development tools.', 
    'packages':[],
    'noconflicts':['gcc', 'make','libc6-dev', 'subversion', 'git', 'git-svn', 'debhelper', 'quilt', 'ack']
    },
]
