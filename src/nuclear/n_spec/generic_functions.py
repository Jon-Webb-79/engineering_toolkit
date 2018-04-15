# Import modules here
import sys
import numpy as np
from scipy import interpolate
# =============================================================================================
# =============================================================================================
# Date:      March 17, 2018
# Purpose:   This module contains all functions necessary to implement the
#            neutron energy spectrum module
# NOTE:      All data is extracted from pages H-1 through H-3 of reference 1
# References
# 1. LA-UR-03-1987, 'MCNP - A General Monte Carlo N-Particle Transport Code, Version 5
#    Volume 1: Overview and Theory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def verify_isotopes(isotope, possible_isotopes, spectrum):
    """

    :param isotope: str
                    The isotope being analyzed (i.e. U235, Pu239, etc...).  Must be a \
                    scalar value
    :param possible_isotopes: list or array
                              A list or array of possible isotopes in an isotope \
                              catalog
    :param spectrum: str
                     The name of the isotope catolog, i.e. Maxwell, Watt, etc... \
                     Must be a scalar value
    :return: NA

    This function compares an input isotope to an array or list of possible \
    isotopes and halts the program execution if the user enters the wrong \
    isotope.
    """
    if isotope not in possible_isotopes:
        message = '{}{}{}{}'.format(isotope, ' not part of the ',
                                    spectrum, 'fission spectra isotope catolog')
        sys.exit(message)
    return
# ---------------------------------------------------------------------------------------------


def list_to_array_float(nd_list):
    """

    :param nd_list: float
                 A list of float or integer variables that will be transformed into \
                 an array
    :return nd_array: float
                     The numpy array created from the input list
    """
    if not isinstance(nd_list, list):
        sys.exit("Input to 'list_to_array()' is not a list")
    try:
        nd_array = np.float32(nd_list)
    except ValueError as ve:
        sys.exit(ve)
    return nd_array
# ---------------------------------------------------------------------------------------------


def interpolate_values(x, y, new_x):
    """

    :param x: float
              The x position for interpolation.  Can be a list or array variable.
    :param y: float
              The y position for interpolation.  Can be a list or array variable. \
              If an array variable it must be the same length as the x variable
    :param new_x: float
                  The new_x position for which a new_y position must be determined. \
                  Can be a scalar or an array variable.
    :return new_y: float
    """
    if isinstance(x, list):
        x = list_to_array_float(x)
    if isinstance(y, list):
        y = list_to_array_float(y)
    if isinstance(new_x, list):
        new_x = list_to_array_float(new_x)
    f = interpolate.interp1d(x, y)
    return f(new_x)
# eof
