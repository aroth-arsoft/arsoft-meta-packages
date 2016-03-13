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
                'plasma-desktop',
                'konsole', 'konqueror', 'kdesudo', 'kate',
                'dolphin', 'kscreen',
                'systemsettings',
                'kubuntu-notification-helper',
                'oxygen-icon-theme', 'kde-zeroconf', 'kdepim-runtime', 'akonadi-server',
                'soprano-daemon',
                'update-manager-kde', 'kmix', 'bluedevil',
                'apturl-kde', 'ksshaskpass', 'kwalletmanager',
                'ark', 'okular', 'okular-extra-backends', 'ksnapshot', 'ksystemlog', 'krusader', 'krename', 'krdc',
                # temporary remove of krfb because of libkpeople3/libkpeople4 trouble
                # 'krfb',
                'dragonplayer', 'filelight',
                'rekonq',
                'print-manager',
                ],
    'packages-precise': ['kde-config-gtk', 'phonon-backend-vlc'],
    'packages-trusty': ['kde-config-gtk-style', 'user-manager', 'muon-discover', 'muon-notifier', 'about-distro',
                        'kde-workspace', 'kde-baseapps', 'kde-plasma-desktop',
                        'strigi-client', 'strigi-daemon', 'polkit-kde-1', 'khelpcenter4',
                        'gtk2-engines-qtcurve',
                        'kde-style-qtcurve',
                        'virtuoso-minimal',
                        'kde-config-cron',
                        'phonon4qt5-backend-vlc',
                        ],
    'packages-wily': ['kde-config-gtk-style', 'user-manager', 'plasma-discover-updater', 'plasma-discover', 'about-distro',
                       'baloo-kf5', 'polkit-kde-agent-1',
                       'phonon4qt5-backend-vlc',
                    ],
    'packages-xenial': ['kde-config-gtk-style', 'user-manager', 'plasma-discover-updater', 'plasma-discover', 'about-distro',
                       'baloo-kf5', 'polkit-kde-agent-1',
                       'phonon4qt5-backend-vlc',
                    ],
    'conflicts':['phonon-backend-xine', 'kpackagekit'],
    'conflicts-wily':['phonon-backend-vlc'],
    },
    {'name':'desktop', 
    'shortdesc':'Installs KDE for regular desktop PCs', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # multimedia packages
                'amarok', 'gwenview', 'soundkonverter',
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
                'kdepim',
                # list some kdepim packages explicit because we want to remove them when arsoft-kde-none is installed
                'akregator', 'kaddressbook', 'kalarm', 'kmail', 'knotes', 'konsolekalendar', 'kontact', 'korganizer', 'blogilo',
                'kleopatra', 'kget', 'kgpg',
                'akonadiconsole',
                # chat packages
                'kopete', 'kopete-message-indicator', 'konversation',
                # burning packages
                'k3b',
                # Hex editor
                'okteta',
                # education packages
                'marble', 'speedcrunch',
                ], 
    'packages-trusty': [
                # plasma desktop edition
                'plasma-widgets-workspace', 'kdeplasma-addons',
                ],
    'packages-wily': [
                ],
    'packages-xenial': [
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
