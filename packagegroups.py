#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

from grp_graphicsdrivers import graphicsdrivers
from grp_desktop import desktop
from grp_openoffice import openoffice
from grp_libreoffice import libreoffice
from grp_firefox import firefox
from grp_thunderbird import thunderbird
from grp_xfce4 import xfce4
from grp_kde import kde
from grp_gnome import gnome
from grp_mythtv import mythtv
from grp_developer import developer
from grp_abiword import abiword
from grp_networkmanager import networkmanager
from grp_cyrusimapd import cyrusimapd

all_package_groups = [
    ('arsoft-gfx', graphicsdrivers),
    ('arsoft-desktop', desktop),
    ('arsoft-openoffice', openoffice),
    ('arsoft-libreoffice', libreoffice),
    ('arsoft-firefox', firefox),
    ('arsoft-thunderbird', thunderbird),
    ('arsoft-xfce4', xfce4),
    ('arsoft-kde', kde),
    ('arsoft-gnome', gnome),
    ('arsoft-mythtv', mythtv),
    ('arsoft-developer', developer),
    ('arsoft-abiword', abiword),
    ('arsoft-networkmanager', networkmanager),
    ('arsoft-cyrusimapd', cyrusimapd)
]
 
