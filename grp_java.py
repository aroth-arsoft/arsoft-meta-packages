#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

java = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Java', 
    'description':'', 
    'packages':['openjdk-7-jre-lib'],
    'side-by-side':['jre-headless', 'jre', 'jdk'],
    'conflicts':['openjdk-6-jre-lib', 'sun-java6-plugin']
    },
    {'name':'jre-headless', 
    'shortdesc':'Installs the latest version of the Java Runtime Environment', 
    'description':'', 
    'depends':['common'],
    'packages-quantal': ['default-jre-headless'],
    'packages-raring': ['default-jre-headless'],
    'packages':['openjdk-7-jre-headless']
    },
    {'name':'jre', 
    'shortdesc':'Installs the latest version of the Java Runtime Environment', 
    'description':'', 
    'depends':['jre-headless'],
    'packages-quantal': ['default-jre'],
    'packages-raring': ['default-jre'],
    'packages':['openjdk-7-jre']
    },
    {'name':'jdk', 
    'shortdesc':'Installs the latest version of the Java Development Kit', 
    'description':'', 
    'depends':['jre'],
    'packages':['openjdk-7-jdk']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Java', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]