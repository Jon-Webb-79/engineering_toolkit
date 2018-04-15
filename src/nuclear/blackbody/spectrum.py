# Import modules here
import numpy as np
from scipy.integrate import quad
import sys

# =============================================================================================
# =============================================================================================
# Date:      March 20, 2018
# Purpose:   This class contains the functions necessary to determining the probability
#            of photon emission resulting from a black-body emitter for the purposes
#            of developing a spectrum for radiation transport calculations.

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


class BlackBodyRadiation:
    def __init__(self):
        self.plank_constant = 6.62607004e-34  # m2kg/s
        self.speed_of_light = 299792458  # m/s
        self.boltzmanns_constant = 1.38064852e-23  # J/K
# =============================================================================================
# =============================================================================================
# ========================         PUBLIC FUNCTIONS         ===================================
# =============================================================================================
# =============================================================================================

    def blackbody_radiation_cont(self, ev_energy, ev_temperature):
        """

        :param ev_energy: float
                          The emitted photon energy in units of eV.  Can be a \
                          scalar, list, or array variable.
        :param ev_temperature: float
                               The blackbody temperature in units of eV.  Must be \
                               a scalar variable.
        :return intensity: float
                           The intensity of photons emitted at a user defined energy \
                           in normalized units of W/sr/m^2/m.  Can be returned as \
                           a scalar or array variable

        This function determines the blackbody radiation intensity for a continuous \
        energy distribution
        """
        if np.size(ev_temperature) > 1:
            sys.exit("ev_temperature can only be a scalar in blackbody_radiation_cont()")
        # transform list to array
        if isinstance(ev_energy, list):
            ev_energy = self.__list_to_array_float(ev_energy)
        # convert energy to wavelength
        wav = self.__ev_to_wavelength(ev_energy)
        if np.size(wav) > 1:
            minimum = min(wav)
            maximum = max(wav)
            intensity = np.array([self.__plank_radiation(wav[i], ev_temperature)
                                 for i in range(len(wav))], np.dtype(np.float32))
            res, err = quad(self.__plank_radiation, minimum,
                            maximum, args=ev_temperature)
            intensity = intensity / res
        else:
            intensity = self.__plank_radiation(wav, ev_temperature)
        return intensity
# ---------------------------------------------------------------------------------------------

    def blackbody_radiation_disc(self, ev_energy, ev_temperature):
        """

         :param ev_energy: float
                           The emitted photon energy in units of eV.  Can be a \
                           scalar, list, or array variable.
         :param ev_temperature: float
                                The blackbody temperature in units of eV.  Must be \
                                a scalar variable.
         :return intensity: float
                            The intensity of photons emitted at a user defined energy \
                            in normalized units of W/sr/m^2/m over an energy bound.  \
                            Can be returned as a scalar or array variable

         This function determines the blackbody radiation intensity for a discrete \
         energy distribution
         """
        if np.size(ev_temperature) > 1:
            sys.exit("ev_temperature can only be a scalar in blackbody_radiation_disc()")
        if isinstance(ev_energy, list):
            ev_energy = self.__list_to_array_float(ev_energy)
        wav = self.__ev_to_wavelength(ev_energy)
        if np.size(ev_energy) < 2:
            sys.exit("out_energy must have at least 2 data points")
        minimum = min(wav)
        maximum = max(wav)
        intensity = np.array([self.__discrete_calculation([wav[i], wav[i+1]],
                             ev_temperature, minimum, maximum)
                             for i in range(len(ev_energy) - 1)],
                             np.dtype(np.float32))
        intensity = np.append(np.array(0.0), intensity)
        return intensity
# =============================================================================================
# =============================================================================================
# ========================        PRIVATE FUNCTIONS         ===================================
# =============================================================================================
# =============================================================================================

    def __discrete_calculation(self, wav, ev_temperature, minimum, maximum):
        res1, err1 = quad(self.__plank_radiation, wav[0], wav[1],
                          args=ev_temperature)
        res2, err2 = quad(self.__plank_radiation, minimum, maximum, args=ev_temperature)
        return res1 / (res2 * (wav[1] - wav[0]))
# ---------------------------------------------------------------------------------------------

    def __plank_radiation(self, wav, ev_temperature):
        k_temperature = self.__ev_to_kelvins(ev_temperature)
        a = 2.0 * self.plank_constant * self.speed_of_light ** 2
        b = self.plank_constant * self.speed_of_light / \
            (wav * self.boltzmanns_constant * k_temperature)
        intensity = a / ((wav ** 5) * (np.exp(b) - 1.0))
        return intensity
# ---------------------------------------------------------------------------------------------

    def __ev_to_kelvins(self, electron_volts):
        return electron_volts * 11604.505
# ---------------------------------------------------------------------------------------------

    def __ev_to_wavelength(self, ev):
        ej = ev / 6.2415093433e18
        frequency = ej / self.plank_constant
        wav = self.speed_of_light / frequency
        return wav
# ---------------------------------------------------------------------------------------------

    def __wavelength_to_ev(self, wav):
        freq = self.speed_of_light / wav
        ej = self.plank_constant * freq
        ev = ej * 6.2415093433e18
        return ev
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
# ---------------------------------------------------------------------------------------------

    def discrete_plot_format(self, x, y):
        """

        :param x: float
                  List or array of x values (i.e. energy), each representing an energy bound \
                  within which a probability of neutron emission exists
        :param y: float
                  List or array of y values (i.e. probability) corresponding to the \
                  probability of neutron emission between energy bounds.  This array \
                  typically starts with 0.
        :return new_x, new_y: tuple of floats
                              A new list of x and y values corresponding to the vertices \
                              of a discrete energy spectrum

        This function transforms a discrete energy spectrum from an MCNP format where the \
        energy array starts with 0. and the probabilities exists between energy bounds to \
        a format where the probability at an energy bound is returned.
        """
        new_x = []
        for i in range(len(x)):
            new_x.append(x[i])
            new_x.append(x[i])
        new_x = np.array(new_x[:-1], np.dtype(np.float32))
        new_y = []
        for i in range(len(y)):
            new_y.append(y[i])
            new_y.append(y[i])
        new_y = np.array(new_y[1:], np.dtype(np.float32))
        return new_x, new_y
# =============================================================================================
# =============================================================================================
# eof
