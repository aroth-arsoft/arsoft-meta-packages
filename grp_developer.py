#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

developer = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the the basic set of development tools', 
    'description':'basic development tools', 
    'packages':[ 'libc6-dev', 'glibc-doc', 'manpages-dev',
                'gcc', 'g++', 'make', 'ack-grep',
                'cmake', 'cmake-curses-gui', 
                'dpkg-dev', 'devscripts', 'cdbs', 'debhelper', 'quilt',
                'git', 'git-svn', 'subversion',
                ],
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE development tools', 
    'description':'Installs the KDE development tools.', 
    'depends':['common'],
    'side-by-side':['gnome'],
    'packages':[
                'cmake-qt-gui', 'kdelibs5-dev',
                'kdevelop', 'kdevelop-data', 'valkyrie', 'c-cpp-reference', 'qt4-dev-tools', 'qt4-doc', 'qt4-designer', 'umbrello', 'kompare',
                'kcachegrind', 'kdesdk-strigi-plugins', 'kdesdk-dolphin-plugins', 'kdesvn', 'kdesvn-kio-plugins'
                # do not install 'kdesdk-kio-plugins' because they replace kdesvn-kio-plugins
                ]
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME development tools', 
    'description':'Installs the GNOME development tools.', 
    'depends':['common'],
    'side-by-side':['kde'],
    'packages':[], 
    },
    {'name':'none', 
    'shortdesc':'removes all development tools.', 
    'description':'This package removes all development tools.', 
    'packages':[], 
    'noconflicts':['gcc','make','libc6-dev','subversion']
    },
]
 
