#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

java = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of Java', 
    'description':'', 
    'packages-precise':['openjdk-7-jre-lib'],
    'packages-trusty':[],
    'packages-utopic':[],
    'side-by-side':['jre-headless', 'jre', 'jdk'],
    'conflicts':['openjdk-6-jre-lib', 'sun-java6-plugin']
    },
    {'name':'jre-headless', 
    'shortdesc':'Installs the latest version of the Java Runtime Environment', 
    'description':'', 
    'depends':['common'],
    'packages-precise':['openjdk-7-jre-headless'],
    'packages-trusty':['openjdk-8-jre-headless'],
    'packages-utopic':['openjdk-8-jre-headless'],
    },
    {'name':'jre', 
    'shortdesc':'Installs the latest version of the Java Runtime Environment', 
    'description':'', 
    'depends':['jre-headless'],
    'packages-precise':['openjdk-7-jre'],
    'packages-trusty':['openjdk-8-jre'],
    'packages-utopic':['openjdk-8-jre'],
    },
    {'name':'jdk', 
    'shortdesc':'Installs the latest version of the Java Development Kit', 
    'description':'', 
    'depends':['jre'],
    'packages-precise':['openjdk-7-jdk'],
    'packages-trusty':['openjdk-8-jdk'],
    'packages-utopic':['openjdk-8-jdk'],
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Java', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
