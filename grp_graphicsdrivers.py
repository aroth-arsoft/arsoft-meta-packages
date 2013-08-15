
graphicsdrivers = [ 
    {'name':'ati', 'shortdesc':'Installs the ATI/AMD graphics driver', 'description':'', 
        'packages':['radeontool', 'fglrx', 'fglrx-modaliases', 'v86d'],
        'noconflicts':['nvidia-current']
    },
    {'name':'nvidia', 'shortdesc':'Installs the NVIDIA graphics driver', 'description':'', 
        'packages':[ 
            ('nvidia-304','nvidia-313','nvidia-319','nvidia-325'), 
            ('nvidia-settings-304','nvidia-settings-313','nvidia-settings-319','nvidia-settings-325'), 
            'v86d', 'vdpau-va-driver'],
        'noconflicts':['fglrx']
    },
    {'name':'nv', 'shortdesc':'Installs the free NVIDIA graphics driver', 'description':'', 'packages':['xserver-xorg-video-nv'] },
    {'name':'nouveau', 'shortdesc':'Installs the Nouveau graphics driver', 'description':'', 'packages':['xserver-xorg-video-nouveau'] },
    {'name':'intel', 'shortdesc':'Installs the Intel graphics driver', 'description':'', 'packages':['xserver-xorg-video-intel'] },
    {'name':'vmware', 'shortdesc':'Installs the VMWare graphics and mouse driver', 'description':'', 'packages':['xserver-xorg-video-vmware'] },
    {'name':'virtualbox', 'shortdesc':'Installs the VirtualBox graphics and mouse driver', 'description':'', 'packages':['virtualbox-guest-x11'] },
    {'name':'none', 'shortdesc':'Uninstalls any graphics drivers', 'description':'', 'packages':[] },
]
 
