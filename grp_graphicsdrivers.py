
graphicsdrivers = [ 
    {'name':'ati', 'shortdesc':'Installs the ATI/AMD graphics driver', 'description':'', 'packages':['radeontool', 'fglrx', 'fglrx-modaliases', 'v86d'] },
    {'name':'nvidia', 'shortdesc':'Installs the NVIDIA graphics driver', 'description':'', 
        'packages':['nvidia-current-updates', 'nvidia-settings-updates', 'v86d', 'vdpau-va-driver'] 
    },
    {'name':'nv', 'shortdesc':'Installs the free NVIDIA graphics driver', 'description':'', 'packages':['xserver-xorg-video-nv'] },
    {'name':'nouveau', 'shortdesc':'Installs the Nouveau graphics driver', 'description':'', 'packages':['xserver-xorg-video-nouveau'] },
    {'name':'intel', 'shortdesc':'Installs the Intel graphics driver', 'description':'', 'packages':['xserver-xorg-video-intel'] },
    {'name':'vmware', 'shortdesc':'Installs the VMWare graphics and mouse driver', 'description':'', 'packages':['xserver-xorg-video-vmware'] },
    {'name':'virtualbox', 'shortdesc':'Installs the VirtualBox graphics and mouse driver', 'description':'', 'packages':['virtualbox-guest-x11'] },
    {'name':'none', 'shortdesc':'Uninstalls any graphics drivers', 'description':'', 'packages':[] },
]
 
