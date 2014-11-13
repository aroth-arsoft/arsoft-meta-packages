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
                'kde-workspace',
                'kde-baseapps',
                'polkit-kde-1',
                'gtk2-engines-qtcurve',
                'konsole', 'konqueror', 'kdesudo', 'kate', 'gdebi-kde', 'kdelibs5-data',
                'dolphin', 'kscreen',
                'khelpcenter4', 'systemsettings',
                'kubuntu-notification-helper',
                'oxygen-icon-theme', 'kde-zeroconf', 'kdepim-runtime', 'akonadi-server',
                'muon',
                'soprano-daemon',
                'strigi-client', 'strigi-daemon',
                'update-manager-kde', 'kmix', 'bluedevil',
                'apturl-kde', 'ksshaskpass', 'kwalletmanager', 'kwalletcli',
                'kde-style-qtcurve', 
                'ark', 'okular', 'okular-extra-backends', 'ksnapshot', 'ksystemlog', 'krusader', 'krename', 'krdc',
                # temporary remove of krfb because of libkpeople3/libkpeople4 trouble
                # 'krfb',
                'dragonplayer', 'filelight',
                'phonon-backend-vlc',
                'rekonq',
                'kde-config-cron',
                'print-manager',
                'virtuoso-minimal'
                ],
    'packages-precise': ['kde-config-gtk'],
    'packages-trusty': ['kde-config-gtk-style', 'user-manager', 'muon-discover', 'about-distro'],
    'packages-utopic': ['kde-config-gtk-style', 'user-manager', 'muon-discover', 'about-distro'],
    'conflicts':['phonon-backend-xine', 'kpackagekit'],
    'conflicts-utopic':['kde-plasma-desktop', 'plasma-desktop'],
    },
    {'name':'desktop', 
    'shortdesc':'Installs KDE for regular desktop PCs', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # plasma desktop edition
                'plasma-widgets-workspace', 'kdeplasma-addons',
                # multimedia packages
                'amarok', 'gwenview', 'kdegraphics-strigi-plugins', 'soundkonverter',
                'kipi-plugins', 'digikam',
                # list some kdegames packages explicit because we want to remove them when arsoft-kde-none is installed
                'bomber', 'bovo', 'kajongg', 'palapeli',
                'kapman', 'katomic', 'kbattleship', 'kblackbox',
                'kblocks', 'kbounce', 'kbreakout', 'kdiamond', 'kfourinline',
                'kgoldrunner', 'kigo', 'killbots', 'kiriki', 'kjumpingcube',
                'klines', 'kmahjongg', 'kmines', 'knetwalk', 'kolf',
                'kollision', 'konquest', 'kpat', 'kreversi',
                'kshisen', 'ksirk', 'kspaceduel', 'ksquares',
                'ksudoku', 'ktuberling', 'kubrick', 'lskat',
                # problematic game
                #'granatier', 
                # kdepim packages
                'kdepim', 'kdepim-kresources',
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
    {'name':'english', 
    'shortdesc':'Installs the english languages files for KDE', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['desktop', 'german'],
    'packages':['language-pack-kde-en', 'language-pack-gnome-en']
    },
    {'name':'german', 
    'shortdesc':'Installs the german languages files for KDE', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['desktop', 'english'],
    'packages':['language-pack-kde-de', 'language-pack-gnome-de']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all versions of KDE', 
    'description':'', 
    'packages':[], 
    'noconflicts':['arsoft-desktop', 'language-pack-gnome-en', 'language-pack-gnome-de']
    },
]
