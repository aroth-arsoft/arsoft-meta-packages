#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

gnome = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'maintains the latest version of the GNOME desktop environment', 
    'description':'This package installs the latest version of GNOME desktop environment and removes obsolete and old packages of GNOME desktop environment.', 
    'packages':['arsoft-desktop',
                'policykit-1-gnome', 'gksu-polkit',
                "gnome-desktop-data", "gnome-settings-daemon", "gnome-panel-data", 'gdebi', 'language-selector',
                "gnome-menus", "gnome-icon-theme", "gnome-themes-selected", "gnome-mime-data", "apturl", "go-home-applet",
                "gnome-terminal", "gnome-screensaver", "gnome-codec-install", "gnome-search-tool", "update-manager", "update-notifier",
                "ssh-askpass-gnome", "gpointing-device-settings", 'ubuntu-sounds', 'xdg-user-dirs-gtk',
                'gconf-defaults-service', 'gconf-editor',
                'gnome-themes-ubuntu', 'gnome-utils', 'packagekit-gnome', 
                'indicator-applet-session', 'indicator-me', 'indicator-sound', 'indicator-session', 'notify-osd', 'notify-osd-icons',
                'nautilus', 'nautilus-sendto', 'nautilus-sendto-empathy', 'nautilus-share', 'gok',
                "metacity", "metacity-common", "compiz", "compiz-gnome"
                ],
    'packages':['arsoft-desktop']
    },
    {'name':'desktop', 
    'shortdesc':'Installs GNOME desktop', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':["brasero", "brasero-common",  "gnome-media-common", 'gnome-common',
                "totem", "totem-common", "libtotem-plparser17", "rhythmbox", "rhythmbox-plugins", "rhythmbox-plugin-cdrecorder",
                'system-config-printer-gnome', 'gnome-paint', 
                "evolution", "evolution-data-server", "evolution-data-server-common", "evolution-common", "evolution-webcal",
                "gnome-games", "gnome-mahjongg", "gnome-games-common", "gnome-sudoku", "gnotski", "gnomine", "gnibbles", "glines", "aisleriot",
                "file-roller", "gedit", "gnome-mag", "gnome-nettool", "gnome-system-tools", "gnome-system-monitor", "tsclient", "vino",
                'eog', 'eog-plugins', 'xournal', 'gnome-user-guide', 'gnome-accessibility-themes',
                "evince", "gnome-screenshot", 'epiphany-browser'], 
    },
    {'name':'multimedia', 
    'shortdesc':'Installs GNOME multimedia desktop', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['english', 'german'],
    'packages':["brasero", "brasero-common",  "gnome-media-common", "totem", "totem-common", "libtotem-plparser17", "rhythmbox", "rhythmbox-plugins", "rhythmbox-plugin-cdrecorder",
                "file-roller", "gedit", "gnome-mag", "gnome-nettool", "gnome-system-tools", "gnome-system-monitor", "tsclient", "vino"], 
    },
    {'name':'english', 
    'shortdesc':'Installs the english languages files for GNOME', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['desktop', 'multimedia', 'german'],
    'packages':['language-pack-gnome-en']
    },
    {'name':'german', 
    'shortdesc':'Installs the german languages files for GNOME', 
    'description':'', 
    'depends':['common'],
    'side-by-side':['desktop', 'multimedia', 'english'],
    'packages':['language-pack-gnome-en']
    },
    {'name':'none', 
    'shortdesc':'removes all versions of the GNOME desktop environment', 
    'description':'This package removes all versions of GNOME desktop environment.', 
    'packages':[], 
    'noconflicts':['arsoft-desktop', 
                'apturl', 'gnome-icon-theme', 'policykit-1-gnome'
                ]
    },
]
 
