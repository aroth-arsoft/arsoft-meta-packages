
graphicsdrivers = [ 
    {'name':'ati', 'shortdesc':'Installs the ATI/AMD graphics driver', 'description':'', 
        'packages':['radeontool', 'fglrx', 'v86d'],
        'noconflicts':['nvidia-current']
    },
    {'name':'radeon', 'shortdesc':'Installs the ATI/AMD radeon graphics driver', 'description':'', 
        'packages':['xserver-xorg-video-radeon']
    },
    {'name':'nvidia', 'shortdesc':'Installs the NVIDIA graphics driver', 'description':'', 
        'packages-trusty':[
            ('nvidia-390', 'nvidia-387', 'nvidia-384', 'nvidia-381',
             'nvidia-378', 'nvidia-375', 'nvidia-370',
             'nvidia-367', 'nvidia-364', 'nvidia-361',
             'nvidia-358', 'nvidia-355', 'nvidia-352',
             'nvidia-349', 'nvidia-346', 'nvidia-343', 'nvidia-340',
             'nvidia-337', 'nvidia-334', 'nvidia-331',
             'nvidia-325', 'nvidia-319', 'nvidia-313', 'nvidia-304'),
            ('nvidia-settings')
            ],
        'packages-xenial':[
            ('nvidia-390', 'nvidia-387', 'nvidia-384', 'nvidia-381',
             'nvidia-378', 'nvidia-375', 'nvidia-370',
             'nvidia-367', 'nvidia-364', 'nvidia-361',
             'nvidia-358', 'nvidia-355', 'nvidia-352',
             'nvidia-349', 'nvidia-346', 'nvidia-343', 'nvidia-340',
             'nvidia-337', 'nvidia-334', 'nvidia-331',
             'nvidia-325', 'nvidia-319', 'nvidia-313', 'nvidia-304'),
            ('nvidia-settings')
            ],
        'packages-bionic':[
            ('nvidia-driver-415',
             'nvidia-driver-410',
             'nvidia-driver-396',
             'nvidia-driver-390', 'nvidia-driver-387', 'nvidia-driver-384'),
            ('nvidia-settings')
            ],
        'packages-disco':[
            ('nvidia-driver-435', 'nvidia-driver-430', 'nvidia-driver-418', 'nvidia-driver-415',
             'nvidia-driver-410',
             'nvidia-driver-390'),
            ('nvidia-settings')
            ],
        'packages-eoan':[
            ('nvidia-driver-435', 'nvidia-driver-430', 'nvidia-driver-418', 'nvidia-driver-415',
             'nvidia-driver-410',
             'nvidia-driver-390'),
            ('nvidia-settings')
            ],
        'noconflicts':['fglrx']
    },
    {'name':'nv', 'shortdesc':'Installs the free NVIDIA graphics driver', 'description':'', 'packages':['xserver-xorg-video-nv'] },
    {'name':'nouveau', 'shortdesc':'Installs the Nouveau graphics driver', 'description':'', 'packages':['xserver-xorg-video-nouveau'] },
    {'name':'intel', 'shortdesc':'Installs the Intel graphics driver', 'description':'', 'packages':['xserver-xorg-video-intel'] },
    {'name':'vmware', 'shortdesc':'Installs the VMWare graphics and mouse driver', 'description':'', 'packages':['xserver-xorg-video-vmware'] },
    {'name':'virtualbox', 'shortdesc':'Installs the VirtualBox graphics and mouse driver', 'description':'', 'packages':['virtualbox-guest-x11'] },
    {'name':'none', 'shortdesc':'Uninstalls any graphics drivers', 'description':'', 'packages':[] },
]
