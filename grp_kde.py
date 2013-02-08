#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

# suggested packages from ark
# rar md5deep cfv arj lha unace

kde = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the latest version of KDE', 
    'description':'', 
    'packages':['arsoft-desktop',
                'polkit-kde-1', 'jockey-kde',
                'gtk2-engines-qtcurve',
                'konsole', 'konqueror', 'kdesudo', 'kate', 'gdebi-kde', 'kdelibs5-data',
                'dolphin', 'kdebase-workspace', 
                'khelpcenter4', 'systemsettings', 'language-selector-kde', 'userconfig',
                'oxygen-icon-theme', 'kde-zeroconf', 'kdepim-runtime', 'akonadi-server',
                'kde-style-skulpture', 'muon',
                'soprano-daemon',
                'strigi-client', 'strigi-daemon',
                'kubuntu-konqueror-shortcuts', 
                'update-manager-kde', 'kmix',
                'apturl-kde', 'ksshaskpass', 'kwalletmanager', 'kwalletcli', 
                'kde-style-qtcurve', 'kwin-style-qtcurve', 'kde-config-gtk',
                'ark', 'okular', 'okular-extra-backends', 'ksnapshot', 'ksystemlog', 'krusader', 'krename', 'krdc', 'krfb',
                'dragonplayer', 'filelight',
                'system-config-printer-kde', 'printer-applet',
                'phonon-backend-vlc', 'phonon-backend-gstreamer',
                'rekonq',
                'kde-config-cron',
                'virtuoso-minimal'
                ],
    'conflicts':['phonon-backend-xine', 'kpackagekit']
    },
    {'name':'netbook', 
    'shortdesc':'Installs KDE optimized for netbooks', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # plasma netbook edition
                'plasma-netbook',
                # multimedia packages
                'amarok', 'gwenview', 'kdegraphics-strigi-plugins', 
                # kdepim packages
                'kdepim', 'kdepim-strigi-plugins', 'kdepim-kresources',
                # list some kdepim explicit because we want to remove them when arsoft-kde-none is installed
                'akregator', 'kaddressbook', 'kalarm', 'kmail', 'knode', 'knotes', 'konsolekalendar', 'kontact', 'korganizer', 'ktimetracker', 'kjots', 'blogilo',
                'kleopatra', 
                'akonadiconsole'
                ], 
    },
    {'name':'tablet', 
    'shortdesc':'Installs KDE optimized for tablets', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # plasma netbook edition
                'plasma-netbook',
                # multimedia packages
                'amarok', 'gwenview', 'kdegraphics-strigi-plugins', 
                ], 
    },
    {'name':'desktop', 
    'shortdesc':'Installs KDE for regular desktop PCs', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # plasma desktop edition
                'kde-plasma-desktop', 'kdeplasma-addons',
                # multimedia packages
                'amarok', 'gwenview', 'kdegraphics-strigi-plugins', 'soundkonverter',
                # temp disable digikam
                # 'kipi-plugins', 'digikam', 'digikam-data', 
                # list some kdegames packages explicit because we want to remove them when arsoft-kde-none is installed
                'bomber', 'bovo', 'kajongg', 'palapeli',
                'kapman', 'katomic', 'kbattleship', 'kblackbox',
                'kblocks', 'kbounce', 'kbreakout', 'kdiamond', 'kfourinline',
                'kgoldrunner', 'kigo', 'killbots', 'kiriki', 'kjumpingcube',
                'klines', 'kmahjongg', 'kmines', 'knetwalk', 'kolf',
                'kollision', 'konquest', 'kpat', 'kreversi',
                'ksame', 'kshisen', 'ksirk', 'kspaceduel', 'ksquares',
                'ksudoku', 'ktron', 'ktuberling', 'kubrick', 'lskat',
                'kmahjongg-data', 'kdegames-card-data', 'kdegames-card-data-extra',
                # problematic game
                #'granatier', 
                # kdepim packages
                'kdepim', 'kdepim-strigi-plugins', 'kdepim-kresources',
                # list some kdepim packages explicit because we want to remove them when arsoft-kde-none is installed
                'akregator', 'kaddressbook', 'kalarm', 'kmail', 'knode', 'knotes', 'konsolekalendar', 'kontact', 'korganizer', 'ktimetracker', 'kjots', 'blogilo',
                'kleopatra', 'kget', 'kgpg',
                'akonadiconsole', 'akonadi-kde-resource-googledata',
                # chat packages
                'kopete', 'kopete-message-indicator', 'konversation', 'konversation-data',
                # burning packages
                'k3b', 'k3b-data', 'libk3b6-extracodecs',
                # Hex editor
                'okteta',
                # education packages
                'marble', 'speedcrunch',
                ], 
    },
    {'name':'multimedia', 
    'shortdesc':'Installs KDE for multimedia PCs', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # plasma desktop edition
                'kde-plasma-desktop',
                # multimedia packages
                'amarok', 'gwenview', 'kipi-plugins', 'digikam', 'digikam-data', 'kdegraphics-strigi-plugins', 
                ], 
    },
    {'name':'english', 
    'shortdesc':'Installs the english languages files for KDE', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['netbook', 'tablet', 'desktop', 'multimedia', 'german'],
    'packages':['language-pack-kde-en']
    },
    {'name':'german', 
    'shortdesc':'Installs the german languages files for KDE', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['netbook', 'tablet', 'desktop', 'multimedia', 'english'],
    'packages':['language-pack-kde-de']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of KDE', 
    'description':'', 
    'packages':[], 
    'noconflicts':['arsoft-desktop']
    },
]
 
