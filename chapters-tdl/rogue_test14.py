#!/usr/bin/env python3
# coding: utf-8
#
# $Id: rogue_test14.py 2 $
# SPDX-License-Identifier: BSD-2-Clause
#

""" test multiple ways of import 

https://stackoverflow.com/questions/20226347/importing-python-libraries-and-gracefully-handling-if-they-are-not-availalble/20228312#20228312

https://stackoverflow.com/questions/3131217/error-handling-when-importing-modules

"""

import pkg_resources


try:
    # installed package
    import pyRogue.roguecolors.py as roguecolors
except ImportError:
    # for dev mode
    import roguecolors

# try:
    # pkg_resources.get_distribution('roguecolors.py')
# except pkg_resources.DistributionNotFound:

# TODO: show import PATH

print(roguecolors.darkest_grey)

