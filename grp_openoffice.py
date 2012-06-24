#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

openoffice = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs OpenOffice', 
    'description':'', 
    'side-by-side':['english', 'german', 'gnome', 'kde'],
    'packages':['openoffice.org', 'openoffice.org-calc', 'openoffice.org-math', 
        'openoffice.org-writer', 'openoffice.org-impress', 'openoffice.org-draw', 
        'openoffice.org-base', 'openoffice.org-pdfimport', 'openoffice.org-base-core', 
        'openoffice.org-core', 'openoffice.org-hyphenation',
        'hunspell-dictionary', 'myspell-dictionary', 
        'pstoedit'] 
    },
    {'name':'english', 
    'shortdesc':'Installs english language files for OpenOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['german', 'gnome', 'kde'],
    'packages':['aspell-en', 'wamerican-large', 'wbritish-large',
                'openoffice.org-hyphenation-en-us', 'openoffice.org-thesaurus-en-us', 'openoffice.org-thesaurus-en-au'
        ] 
    },
    {'name':'german', 
    'shortdesc':'Installs german language files for OpenOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'gnome', 'kde'],
    'packages':['wngerman', 'aspell-de', 
        'openoffice.org-l10n-de', 'openoffice.org-hyphenation-de', 'openoffice.org-thesaurus-de'
        ] 
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME support files for OpenOffice', 
    'description':'', 
    'depends':['common', 'english', 'german'],
    'side-by-side':['english', 'german', 'kde'],
    'packages':['openoffice.org-gnome', 'openoffice.org-evolution'], 
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE support files for OpenOffice', 
    'description':'', 
    'depends':['common', 'english', 'german'],
    'side-by-side':['english', 'german', 'gnome'],
    'packages':['openoffice.org-kde', 'openoffice.org-style-oxygen'], 
    },
    {'name':'none', 
    'shortdesc':'Uninstalls OpenOffice', 
    'description':'', 
    'packages':[], 
    'noconflicts':['pstoedit', 
                    'hunspell-dictionary', 'myspell-dictionary', 
                    'aspell-en', 'wamerican-large', 'wbritish-large', 
                    'wngerman', 'aspell-de']
    },
]
 
