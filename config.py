#!/usr/bin/python
# -*- coding: utf-8 -*-
# kate: space-indent on; indent-width 4; mixedindent off; indent-mode python;

all_distributions = {
    'hardy':'8.04',
    'intrepid':'8.10',
    'jaunty':'9.04',
    'lucid':'9.10',
    'karmic':'10.04',
    'maverick':'10.10',
    'natty':'11.04',
    'oneiric':'11.10',
    'precise':'12.04',
    'quantal':'12.10',
    'raring':'13.04',
    'saucy':'13.10',
    'trusty':'14.04',
    'utopic':'14.10',
    'vivid':'15.04',
    'wily':'15.10',
    'xenial':'16.04',
    'yakkety':'16.10',
    'zesty':'17.04',
    'artful':'17.10',
}

default_distributions = ['trusty', 'xenial', 'zesty', 'artful']
source_package_name = 'arsoft-meta-packages'
package_maintainer = 'Andreas Roth <aroth@arsoft-online.com>'
package_homepage = 'https://github.com/aroth-arsoft/arsoft-meta-packages'
package_debhelper = 9
package_standardsversions = '3.9.8'
