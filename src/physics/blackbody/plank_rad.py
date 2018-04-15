# Import modules here
import numpy as np
from scipy.integrate import quad
import sys

from src.nuclear.n_spec import generic_functions as gf
# =============================================================================================
# =============================================================================================
# Date:      March 17, 2018
# Purpose:   This class contains the functions necessary to determining the probability
#            of photon emission resulting from a blackbody emitter

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


class PlankRadiation(object):
    def __init__(self):
        self.plank_constant = 6.62607004e-34  # m2kg/s
        self.speed_of_light = 299792458  # m/s
        self.boltzmanns_constant = 1.38064852e-23  # J/K
# =============================================================================================
# =============================================================================================
# ========================         PUBLIC FUNCTIONS         ===================================
# =============================================================================================
# =============================================================================================

    def blackbody_radiation(self, wavelength, temperature):
        """

        :param wavelength: float
                          The emitted photon wavelength in units of meters.  Can be a \
                          scalar, list, or array variable.
        :param temperature: float
                               The blackbody temperature in units of Kelvins.  Must be \
                               a scalar variable.
        :return intensity: float
                           The intensity of photons emitted at a user defined energy \
                           in normalized units of W/sr/m^2/m.  Can be returned as \
                           a scalar or array variable

        This function determines the black-body radiation intensity for a continuous \
        energy distribution
        """
        if np.size(temperature) > 1:
            sys.exit("ev_temperature can only be a scalar in blackbody_radiation_cont()")
        # transform list to array
        if isinstance(wavelength, list):
            wavelength = self.__list_to_array_float(wavelength)
        if np.size(wavelength) > 1:
            intensity = np.array([self.__plank_radiation(wavelength[i], temperature)
                                 for i in range(len(wavelength))], np.dtype(np.float32))
        else:
            intensity = self.__plank_radiation(wavelength, temperature)
        return intensity

# =============================================================================================
# =============================================================================================
# ========================        PRIVATE FUNCTIONS         ===================================
# =============================================================================================
# =============================================================================================

    def __plank_radiation(self, wavelength, temperature):
        a = 2.0 * self.plank_constant * self.speed_of_light ** 2
        b = self.plank_constant * self.speed_of_light / \
            (wavelength * self.boltzmanns_constant * temperature)
        intensity = a / ((wavelength ** 5) * (np.exp(b) - 1.0))
        return intensity
# ---------------------------------------------------------------------------------------------

    def __list_to_array_float(self, nd_list):
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
# eof
