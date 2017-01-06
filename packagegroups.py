#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

from grp_graphicsdrivers import graphicsdrivers
from grp_desktop import desktop
from grp_libreoffice import libreoffice
from grp_firefox import firefox
from grp_thunderbird import thunderbird
from grp_chromium import chromium
from grp_chrome import chrome
from grp_xfce4 import xfce4
from grp_kde import kde
from grp_gnome import gnome
from grp_mythtv import mythtv
from grp_developer import developer
from grp_abiword import abiword
from grp_networkmanager import networkmanager
from grp_cyrusimapd import cyrusimapd
from grp_mono import mono
from grp_java import java
from grp_latex import latex
from grp_googleearth import googleearth
from grp_googlemusicmanager import googlemusicmanager
from grp_lightdm import lightdm
from grp_sddm import sddm
from grp_nagios import nagios
from grp_icinga import icinga
from grp_microcode import microcode
from grp_grub import grub
from grp_unity import unity
from grp_vim import vim
from grp_check_mk import check_mk
from grp_dovecot import dovecot
from grp_roundcube import roundcube
from grp_trac import trac
from grp_cups import cups
from grp_clamav import clamav
from grp_sssd import sssd

all_package_groups = [
    ('arsoft-gfx', graphicsdrivers, {} ),
    ('arsoft-desktop', desktop, {} ),
    ('arsoft-libreoffice', libreoffice, {} ),
    ('arsoft-firefox', firefox, {} ),
    ('arsoft-thunderbird', thunderbird, {} ),
    ('arsoft-chromium', chromium, {} ),
    ('arsoft-chrome', chrome, {} ),
    ('arsoft-xfce4', xfce4, {} ),
    ('arsoft-kde', kde, {} ),
    ('arsoft-gnome', gnome, {} ),
    ('arsoft-mythtv', mythtv, {} ),
    ('arsoft-developer', developer, {} ),
    ('arsoft-abiword', abiword, {} ),
    ('arsoft-networkmanager', networkmanager, {} ),
    ('arsoft-cyrusimapd', cyrusimapd, {} ),
    ('arsoft-mono', mono, {} ),
    ('arsoft-java', java, {} ),
    ('arsoft-latex', latex, {} ),
    ('arsoft-googleearth', googleearth, {} ),
    ('arsoft-googlemusicmanager', googlemusicmanager, {} ),
    ('arsoft-lightdm', lightdm, {} ),
    ('arsoft-sddm', sddm, {} ),
    ('arsoft-nagios', nagios, {} ),
    ('arsoft-icinga', icinga, {} ),
    ('arsoft-microcode', microcode, {} ),
    ('arsoft-grub', grub, {} ),
    ('arsoft-unity', unity, {} ),
    ('arsoft-vim', vim, {} ),
    ('arsoft-check-mk', check_mk, {} ),
    ('arsoft-dovecot', dovecot, {} ),
    ('arsoft-roundcube', roundcube, {} ),
    ('arsoft-trac', trac, {} ),
    ('arsoft-cups', cups, {} ),
    ('arsoft-clamav', clamav, {} ),
    ('arsoft-sssd', sssd, {} ),
]
