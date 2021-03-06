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
                'konsole', 'kate',
                'dolphin', 'kscreen',
                'systemsettings',
                'kubuntu-notification-helper',
                'oxygen-icon-theme', 'kdepim-runtime', 'akonadi-server',
                'bluedevil',
                'ksshaskpass', 'kwalletmanager',
                'ark', 'okular', 'okular-extra-backends', 'ksystemlog', 'krusader', 'krename', 'krdc',
                # temporary remove of krfb because of libkpeople3/libkpeople4 trouble
                # 'krfb',
                'filelight',
                'print-manager',
                ],
    'packages-trusty': ['kde-config-gtk-style', 'user-manager', 'muon-discover', 'muon-notifier', 'about-distro',
                        'kde-workspace', 'kde-baseapps', 'kde-plasma-desktop',
                        'strigi-client', 'strigi-daemon', 'polkit-kde-1', 'khelpcenter4',
                        'gtk2-engines-qtcurve',
                        'kde-style-qtcurve',
                        'virtuoso-minimal',
                        'kde-config-cron',
                        'phonon4qt5-backend-vlc',
                        ],
    'packages-xenial': ['kde-config-gtk-style', 'user-manager', 'plasma-discover',
                       'baloo-kf5', 'polkit-kde-agent-1',
                       'phonon-backend-gstreamer',
                       'phonon4qt5-backend-gstreamer',
                       'ksnapshot'
                    ],
    'packages-artful': ['kde-config-gtk-style', 'user-manager', 'plasma-discover',
                       'baloo-kf5', 'polkit-kde-agent-1',
                       'phonon-backend-gstreamer',
                       'phonon4qt5-backend-gstreamer',
                       'kde-config-plymouth',
                    ],
    'packages-bionic': ['kde-config-gtk-style', 'user-manager', 'plasma-discover',
                       'baloo-kf5', 'polkit-kde-agent-1',
                       'phonon-backend-gstreamer',
                       'phonon4qt5-backend-gstreamer',
                       'kde-config-plymouth',
                    ],
    'conflicts':['phonon-backend-xine', 'kpackagekit'],
    },
    {'name':'desktop', 
    'shortdesc':'Installs KDE for regular desktop PCs', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':[
                # multimedia packages
                'gwenview',
                'kipi-plugins', 'digikam',
                # list some kdegames packages explicit because we want to remove them when arsoft-kde-none is installed
                'bomber', 'bovo', 'kajongg', 'palapeli',
                'kapman', 'katomic', 'kblackbox',
                'kblocks', 'kbounce', 'kbreakout', 'kdiamond', 'kfourinline',
                'kgoldrunner', 'kigo', 'killbots', 'kiriki', 'kjumpingcube',
                'klines', 'kmahjongg', 'kmines', 'knetwalk', 'kolf',
                'kollision', 'konquest', 'kpat', 'kreversi',
                'kshisen', 'ksirk', 'kspaceduel', 'ksquares',
                'ksudoku', 'ktuberling', 'kubrick', 'lskat',
                # problematic game
                #'granatier', 
                # list some kdepim packages explicit because we want to remove them when arsoft-kde-none is installed
                'akregator', 'kaddressbook', 'kalarm', 'kmail', 'knotes', 'konsolekalendar', 'kontact', 'korganizer',
                'kleopatra', 'kgpg',
                'akonadiconsole',
                # chat packages
                'konversation',
                # remove kopete because it brakes the language packages
                # 'kopete',
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
    'packages-xenial': [
                ],
    'packages-bionic': [
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
