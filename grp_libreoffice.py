#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

libreoffice = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs LibreOffice', 
    'description':'', 
    'side-by-side':['german', 'english', 'gnome', 'kde'],
    'packages':['libreoffice', 'libreoffice-calc', 'libreoffice-math', 
        'libreoffice-writer', 'libreoffice-impress', 'libreoffice-draw', 
        'libreoffice-base', 'libreoffice-pdfimport', 'libreoffice-base-core', 
        'libreoffice-core', 
        'libreoffice-officebean',
        'libreoffice-style-hicontrast', 'libreoffice-style-tango',
        'libreoffice-style-crystal', 'libreoffice-style-oxygen',
        'hunspell-dictionary', 'myspell-dictionary', 
        'pstoedit'] 
    },
    {'name':'english', 
    'shortdesc':'Installs english language and help files for LibreOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['german', 'gnome', 'kde'],
    'packages':['aspell-en', 'wamerican-large', 'wbritish-large',
                'libreoffice-help-en-us', 'libreoffice-help-en-gb', 
                'libreoffice-l10n-en-gb'
        ] 
    },
    {'name':'german', 
    'shortdesc':'Installs german language and help files for LibreOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'gnome', 'kde'],
    'packages':['wngerman', 'aspell-de', 
        'libreoffice-help-de', 'libreoffice-l10n-de'
        ] 
    },
    {'name':'gnome', 
    'shortdesc':'Installs GNOME support files for LibreOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['kde', 'english', 'german'],
    'packages':['libreoffice-gnome'], 
    },
    {'name':'kde', 
    'shortdesc':'Installs KDE support files for LibreOffice', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['gnome', 'english', 'german'],
    'packages':['libreoffice-kde'], 
    },
    {'name':'none', 
    'shortdesc':'Uninstalls LibreOffice', 
    'description':'', 
    'packages':[], 
    'noconflicts':['pstoedit', 
                    'hunspell-dictionary', 'myspell-dictionary', 
                    'aspell-en', 'wamerican-large', 'wbritish-large', 
                    'wngerman', 'aspell-de']
    },
]
 
