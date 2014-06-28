#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

developer = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the the basic set of development tools', 
    'description':'basic development tools', 
    'packages':[ 'libc6-dev', 'manpages-dev',
                'gcc', 'g++', 'make', 'ack-grep',
                'cmake', 'cmake-curses-gui', 
                'dpkg-dev', 'devscripts', 'cdbs', 'debhelper', 'quilt',
                'git', 'git-svn', 'subversion',
                ],
    },
    {'name':'qt',
    'shortdesc':'Installs Qt development tools',
    'description':'Installs the Qt development tools.',
    'depends':['common'],
    'side-by-side':['gnome', 'kde', 'kdevelop'],
    'packages':[
                'cmake-qt-gui', 'valkyrie', 'qt4-dev-tools', 'qt4-doc', 'qt4-doc-html', 'qt4-designer', 'qt4-linguist-tools'
                ]
    },
    {'name':'kde',
    'shortdesc':'Installs KDE development tools',
    'description':'Installs the KDE development tools.',
    'depends':['qt'],
    'side-by-side':['gnome', 'qt', 'kdevelop'],
    'packages':[
                'kdelibs5-dev', 'kdesdk', 'kcachegrind-converters',
                ]
    },
    {'name':'kdevelop',
    'shortdesc':'installs KDevelop',
    'description':'include KDevelop and the following plugins: python, php',
    'depends':['kde'],
    'side-by-side':['gnome', 'kde', 'qt'],
    'packages':[ 'kdevelop', 'kdevelop-dbg', 'kdevelop-l10n',
                'kdev-python',
                'kdevelop-php', 'kdevelop-php-l10n',
                'c-cpp-reference'],
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
    'noconflicts':['gcc', 'make','libc6-dev','subversion', 'git', 'git-svn']
    },
]
