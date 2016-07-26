#!/usr/bin/env python                                                          #
#                                                                              #
# Autor: Michela Negro, University of Torino.                                  #
# On behalf of the Fermi-LAT Collaboration.                                    #
#                                                                              #
# This program is free software; you can redistribute it and/or modify         #
# it under the terms of the GNU GengReral Public License as published by       #
# the Free Software Foundation; either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
#------------------------------------------------------------------------------#


"""Logging utilities, building on top of the python logging module.
"""

import logging
import sys
import time


logger = logging.getLogger('advlab')
logger.setLevel(logging.DEBUG)


""" Configure the main terminal logger.
"""
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleFormatter = logging.Formatter(">>> %(message)s")
consoleHandler.setFormatter(consoleFormatter)
logger.addHandler(consoleHandler)


def abort(message = ''):
    """Abort the execution (via a sys.exit) with a message.
    Use this with care, and opt for custom exceptions whenever possible.
    """
    if message != '':
        message = '%s. Abort.' % message
    else:
        message = 'Abort.'
    sys.exit(message)

def startmsg():
    """Print the start message.
    """
    BUILD_DATE = '1 Feb 2016'
    print('\n    Welcome to GRATools (built on %s).\n' %BUILD_DATE)
    print('    Autor: Michela Negro, University of Torino.')
    print('    On behalf of the Fermi-LAT Collaboration.\n')
    print('    This is a framework created to study gamma-ray')
    print('    anisotropy with Fermi-LAT data. \n\n')

if __name__ == '__main__':
    startmsg()
