#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

latex = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of latex', 
    'description':'', 
    'packages':['texlive-latex-base', 'tex-common', 'texlive-base', 'texlive-binaries', 'texlive-common' ]
    },
    {'name':'extra', 
    'shortdesc':'Installs the extra Latex packages', 
    'description':'', 
    'packages':['texlive-latex-extra']
    },
    {'name':'recommended', 
    'shortdesc':'Installs the recommended Latex packages', 
    'description':'', 
    'packages':['texlive-latex-recommended', 'texlive-fonts-recommended']
    },
    {'name':'doc', 
    'shortdesc':'Installs the recommended Latex packages', 
    'description':'', 
    'packages':['texlive-fonts-recommended-doc']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of Latex', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    },
]
 
