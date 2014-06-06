#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

# ttf-mscorefonts-installer
#                'gtk2-engines-murrine', 'gtk2-engines-pixbuf', 'gtk2-engines-qtcurve', 'gtk2-engines-aurora', 'gtk2-engines-blueheart', 'gtk2-engines-cleanice',
#                'gtk2-engines-equinox', 'gtk2-engines-magicchicken', 'gtk2-engines-moblin', 'gtk2-engines-mythbuntu', 'gtk2-engines-nodoka', 'gtk2-engines-sapwood'
#                'gtk2-engines-smooth', 'gtk2-engines-wonderland', 'gtk2-engines-xfce'
# All gstreamer packages
# 'gstreamer0.10-ffmpeg', 'gstreamer0.10-alsa', 'gstreamer0.10-gnonlin', 'gstreamer0.10-nice', 'gstreamer0.10-plugins-base-apps', 'gstreamer0.10-tools',
# 'gstreamer0.10-plugins-good', 'gstreamer0.10-plugins-bad', 'gstreamer0.10-plugins-ugly',

desktop = [
    {'name':'common', 
    'mainpackage':True,
    'shortdesc':'Installs the common packages for desktop workstations', 
    'description':'', 
    'packages':['ttf-mscorefonts-installer', 
                'policykit-desktop-privileges',
                'unclutter',
                ],
    'conflicts':[
#                    'ibus-qt4', 'libibus-qt1', 'ibus', 'ibus-gtk', 'libibus1',
                    'scim', 'scim-qtimm', 'scim-modules-socket']
    },
    {'name':'none', 
    'shortdesc':'Uninstalls all common desktop packages', 
    'description':'', 
    'packages':[], 
    'noconflicts':[]
    }
]
