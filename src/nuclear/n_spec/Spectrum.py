# Import modules here
import numpy as np
from scipy.integrate import quad
import sys

from src.nuclear.n_spec import generic_functions as gf
# =============================================================================================
# =============================================================================================
# Date:      March 17, 2018
# Purpose:   This class contains the functions necessary to determining the probability
#            of neutron emission resulting from an incident neutron of a specific
#            energy using the Watt fission spectrum
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


class NeutronSpectrum(object):
    """
    This class is a container for other spectrum classes
    """
    @staticmethod
    def factory(spec_type):
        if spec_type.upper() == 'MAXWELL':
            return MaxwellSpectrum()
        elif spec_type.upper() == 'WATT':
            return WattSpectrum()
        elif spec_type.upper() == 'SPONTANEOUS':
            return SpontaneousSpectrum()
# =============================================================================================
# =============================================================================================


class WattSpectrum(NeutronSpectrum):
    def __init__(self):
        # Public variables
        self.isotopes = ['Th232', 'U233', 'U235', 'U238', 'Pu239']

        # Private variables
        self.__energy = np.array([2.53e-8, 1.0, 14.0])
        self.__Th232_a = np.array([1.0888, 1.1096, 1.1700])
        self.__U233_a = np.array([0.977, 0.977, 1.0036])
        self.__U235_a = np.array([0.988, 0.988, 1.028])
        self.__U238_a = np.array([0.88111, 0.89506, 0.96534])
        self.__Pu239_a = np.array([0.966, 0.966, 1.055])

        self.__Th232_b = np.array([1.6871, 1.6316, 1.4610])
        self.__U233_b = np.array([2.546, 2.546, 2.6377])
        self.__U235_b = np.array([2.249, 2.249, 2.084])
        self.__U238_b = np.array([3.4005, 3.2953, 2.8330])
        self.__Pu239_b = np.array([2.842, 2.842, 2.383])
# =============================================================================================
# =============================================================================================
# =========================             PUBLIC FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def neutron_emission_prob_cont(self, isotope, incident_energy, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar, \
                           list or array value
        :return probability: float
                             The non-normalized probability of neutron emission for a \
                             user specified neutron birth energy.

        This function calculates continuous energy neutron emission spectrum for \
        fission neutrons as a function of energy for a user specified isotope \
        using the Watt method.
        """
        # transform to an array if necessary
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        # calculate value(s)
        if np.size(out_energy) > 1:
            probability = np.array([self.__calculate_probability(isotope,
                                   incident_energy, out_energy[i], 'cont')
                                   for i in range(len(out_energy))],
                                   np.dtype(np.float32))
        else:
            probability = self.__calculate_probability(isotope, incident_energy,
                                                       out_energy, 'cont')
        return probability
# ---------------------------------------------------------------------------------------------

    def neutron_emission_prob_disc(self, isotope, incident_energy, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           list, or array value
        :return probability: float
                             The probability of neutron emission at a user specified \
                             energy.  Can be a scalar or array value.
        """
        # transform to an array if necessary
        if np.size(out_energy) < 2:
            sys.exit("out_energy must have at least 2 data points")
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        probability = np.array([self.__calculate_probability(isotope, incident_energy,
                               [out_energy[i], out_energy[i+1]], 'disc')
                                for i in range(len(out_energy)-1)], np.dtype(np.float32))
        probability = np.append(np.array(0.0), probability)
        return probability
# =============================================================================================
# =============================================================================================
# =========================            PRIVATE FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def __calculate_probability(self, isotope, incident_energy, out_energy, spec_type):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           value
        :param spec_type: str
                          'cont' or 'disc' for type of spectrum
        :return probability: float
                             The non-normalized probability of neutron emission for a \
                             user specified neutron birth energy.
        """
        # verify the user specified isotope is in the library.
        gf.verify_isotopes(isotope, self.isotopes, ' Watt ')
        # determine probability of emission
        if isotope == 'Th232':
            a = gf.interpolate_values(self.__energy, self.__Th232_a, incident_energy)
            b = gf.interpolate_values(self.__energy, self.__Th232_b, incident_energy)
        elif isotope == 'U233':
            a = gf.interpolate_values(self.__energy, self.__U233_a, incident_energy)
            b = gf.interpolate_values(self.__energy, self.__U233_b, incident_energy)
        elif isotope == 'U235':
            a = gf.interpolate_values(self.__energy, self.__U235_a, incident_energy)
            b = gf.interpolate_values(self.__energy, self.__U235_b, incident_energy)
        elif isotope == 'U235':
            a = gf.interpolate_values(self.__energy, self.__U238_a, incident_energy)
            b = gf.interpolate_values(self.__energy, self.__U238_b, incident_energy)
        else:
            a = gf.interpolate_values(self.__energy, self.__Pu239_a, incident_energy)
            b = gf.interpolate_values(self.__energy, self.__Pu239_b, incident_energy)
        if spec_type == 'cont':
            spectrum = self.__watt_spectrum(out_energy, 1, a, b)
            res, err = spectrum / quad(self.__watt_spectrum, 0, 20, args=(1, a, b))
        else:
            res1, err1 = quad(self.__watt_spectrum, out_energy[0], out_energy[1],
                              args=(1, a, b))
            res2, err2 = quad(self.__watt_spectrum, 0, 20, args=(1, a, b))
            res = res1/(res2 * (out_energy[1] - out_energy[0]))
        return res
# ---------------------------------------------------------------------------------------------

    def __watt_spectrum(self, e, c, a, b):
        # extractged from page H-3 of reference 1
        return c * np.exp(-e / a) * np.sinh(np.sqrt(b * e))
# =============================================================================================
# =============================================================================================


class MaxwellSpectrum(NeutronSpectrum):
    def __init__(self):
        # Public variables
        self.isotopes = ['Pa233', 'U234', 'U236', 'U237', 'Np237', 'Pu238',
                         'Pu240', 'Pu241', 'Pu242', 'Am241', 'Pu242m', 'Am243',
                         'Cm242', 'Cm244', 'Cm245', 'Cm246']

        # Private variables
        self.__energy = np.array([2.53e-8, 1.0, 14.0])
        self.__Pa233_a = np.array([1.3294, 1.3294, 1.3294])
        self.__U234_a = np.array([1.2955, 1.3086, 1.4792])
        self.__U236_a = np.array([1.2955, 1.3086, 1.4792])
        self.__U237_a = np.array([1.2996, 1.3162, 1.5063])
        self.__Np237_a = np.array([1.315, 1.315, 1.315])
        self.__Pu238_a = np.array([1.330, 1.330, 1.330])
        self.__Pu240_a = np.array([1.346, 1.3615, 1.547])
        self.__Pu241_a = np.array([1.3597, 1.3752, 1.5323])
        self.__Pu242_a = np.array([1.337, 1.354, 1.552])
        self.__Am241_a = np.array([1.330, 1.330, 1.330])
        self.__Pu242m_a = np.array([1.330, 1.330, 1.330])
        self.__Am243_a = np.array([1.330, 1.330, 1.330])
        self.__Cm242_a = np.array([1.330, 1.330, 1.330])
        self.__Cm244_a = np.array([1.330, 1.330, 1.330])
        self.__Cm245_a = np.array([1.4501, 1.4687, 1.6844])
        self.__Cm246_a = np.array([1.3624, 1.4075, 1.6412])
# =============================================================================================
# =============================================================================================
# =========================             PUBLIC FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def neutron_emission_prob_cont(self, isotope, incident_energy, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           value
        :return probability: float
                             The non-normalized probability of neutron emission for a \
                             user specified neutron birth energy.

        This function calculates continuous energy neutron emission spectrum for \
        fission neutrons as a function of energy for a user specified isotope \
        using the Maxwell method.
        """
        # transform to an array if necessary
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        # calculate value(s)
        if np.size(out_energy) > 1:
            probability = np.array([self.__calculate_probability(isotope,
                                   incident_energy, out_energy[i], 'cont')
                                   for i in range(len(out_energy))],
                                   np.dtype(np.float32))
        else:
            probability = self.__calculate_probability(isotope, incident_energy,
                                                       out_energy, 'cont')
        return probability
# ---------------------------------------------------------------------------------------------

    def neutron_emission_prob_disc(self, isotope, incident_energy, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           list, or array value
        :return probability: float
                             The probability of neutron emission at a user specified \
                             energy.  Can be a scalar or array value.
        """
        # transform to an array if necessary
        if np.size(out_energy) < 2:
            sys.exit("out_energy must have at least 2 data points")
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        probability = np.array([self.__calculate_probability(isotope, incident_energy,
                               [out_energy[i], out_energy[i+1]], 'disc')
                       for i in range(len(out_energy)-1)], np.dtype(np.float32))
        probability = np.append(np.array(0.0), probability)
        return probability
# =============================================================================================
# =============================================================================================
# =========================            PRIVATE FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def __calculate_probability(self, isotope, incident_energy, out_energy, spec_type):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param incident_energy: float
                                The incident neutron energy in units of MeV.  Must \
                                be a scalar value
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           value
        :param spec_type: str
                          'cont' or 'disc' for type of spectrum
        :return probability: float
                             The non-normalized probability of neutron emission for a \
                             user specified neutron birth energy.
        """
        # verify the user specified isotope is in the library.
        gf.verify_isotopes(isotope, self.isotopes, 'Maxwell ')
        # determine probability of emission
        if isotope == 'Pa233':
            a = gf.interpolate_values(self.__energy, self.__Pa233_a, incident_energy)
        elif isotope == 'U234':
            a = gf.interpolate_values(self.__energy, self.__U234_a, incident_energy)
        elif isotope == 'U236':
            a = gf.interpolate_values(self.__energy, self.__U236_a, incident_energy)
        elif isotope == 'U237':
            a = gf.interpolate_values(self.__energy, self.__U237_a, incident_energy)
        elif isotope == 'Np237':
            a = gf.interpolate_values(self.__energy, self.__Np237_a, incident_energy)
        elif isotope == 'Pu238':
            a = gf.interpolate_values(self.__energy, self.__Pu238_a, incident_energy)
        elif isotope == 'Pu240':
            a = gf.interpolate_values(self.__energy, self.__Pu240_a, incident_energy)
        elif isotope == 'Pu241':
            a = gf.interpolate_values(self.__energy, self.__Pu241_a, incident_energy)
        elif isotope == 'Pu242':
            a = gf.interpolate_values(self.__energy, self.__Pu242_a, incident_energy)
        elif isotope == 'Am241':
            a = gf.interpolate_values(self.__energy, self.__Am241_a, incident_energy)
        elif isotope == 'Pu242m':
            a = gf.interpolate_values(self.__energy, self.__Pu242m_a, incident_energy)
        elif isotope == 'Am243':
            a = gf.interpolate_values(self.__energy, self.__Am243_a, incident_energy)
        elif isotope == 'Cm242':
            a = gf.interpolate_values(self.__energy, self.__Cm242_a, incident_energy)
        elif isotope == 'Cm244':
            a = gf.interpolate_values(self.__energy, self.__Cm244_a, incident_energy)
        elif isotope == 'Cm245':
            a = gf.interpolate_values(self.__energy, self.__Cm245_a, incident_energy)
        else:
            a = gf.interpolate_values(self.__energy, self.__Cm246_a, incident_energy)
        if spec_type == 'cont':
            spectrum = self.__maxwell_spectrum(out_energy, 1, a)
            res, err = spectrum / quad(self.__maxwell_spectrum, 1, 20, args=(1, a))
        else:
            res1, err1 = quad(self.__maxwell_spectrum, out_energy[0], out_energy[1],
                              args=(1, a))
            res2, err2 = quad(self.__maxwell_spectrum, 0, 20, args=(1, a))
            res = res1 / (res2 * (out_energy[1] - out_energy[0]))
        return res
# ---------------------------------------------------------------------------------------------

    def __maxwell_spectrum(self, e, c, a):
        # extracted from page H-1 of reference 1
        return c * e**0.5 * np.exp(-e / a)
# =============================================================================================
# =============================================================================================


class SpontaneousSpectrum(NeutronSpectrum):
    def __init__(self):
        # Public variables
        self.isotopes = ['Th232', 'U232', 'U233', 'U234', 'U235', 'U236', 'U238',
                         'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242',
                         'Am241', 'Cm242', 'Cm244', 'Bk249', 'Cf252']

        # Private variables
        self.__Th232_a = 0.8
        self.__U232_a = 0.892204
        self.__U233_a = 0.854803
        self.__U234_a = 0.771241
        self.__U235_a = 0.774713
        self.__U236_a = 0.735166
        self.__U238_a = 0.648318
        self.__Np237_a = 0.833438
        self.__Np238_a = 0.847833
        self.__Pu238_a = 0.847833
        self.__Pu239_a = 0.885247
        self.__Pu240_a = 0.794930
        self.__Pu241_a = 0.842472
        self.__Pu242_a = 0.819150
        self.__Am241_a = 0.933020
        self.__Cm242_a = 0.887353
        self.__Cm244_a = 0.902523
        self.__Bk249_a = 3.79405
        self.__Cf252_a = 1.18

        self.__Th232_b = 4.0
        self.__U232_b = 3.72278
        self.__U233_b = 4.03210
        self.__U234_b = 4.92449
        self.__U235_b = 4.85231
        self.__U236_b = 5.35746
        self.__U238_b = 6.81057
        self.__Np237_b = 4.24147
        self.__Np238_b = 4.16933
        self.__Pu238_b = 4.16933
        self.__Pu239_b = 3.80269
        self.__Pu240_b = 4.68927
        self.__Pu241_b = 4.15150
        self.__Pu242_b = 4.36668
        self.__Am241_b = 3.46195
        self.__Cm242_b = 3.89176
        self.__Cm244_b = 3.72033
        self.__Bk249_b = 3.79405
        self.__Cf252_b = 1.03419
# =============================================================================================
# =============================================================================================
# =========================             PUBLIC FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def neutron_emission_prob_cont(self, isotope, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           value
        :return probability: float
                             The continuous normalized probability of neutron emission for a \
                             user specified neutron birth energy.

        This function calculates continuous energy neutron emission spectrum for \
        spontaneous fission neutrons as a function of energy for a user specified isotope \
        using the Watt method.
        """
        # transform to an array if necessary
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        # calculate value(s)
        if np.size(out_energy) > 1:
            probability = np.array([self.__calculate_probability(isotope,
                                   out_energy[i], 'cont')
                                   for i in range(len(out_energy))],
                                   np.dtype(np.float32))
        else:
            probability = self.__calculate_probability(isotope, out_energy, 'cont')
        return probability
# ---------------------------------------------------------------------------------------------

    def neutron_emission_prob_disc(self, isotope, out_energy):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           list, or array value
        :return probability: float
                             The probability of neutron emission at a user specified \
                             energy.  Can be a scalar or array value.
        """
        # transform to an array if necessary
        if np.size(out_energy) < 2:
            sys.exit("out_energy must have at least 2 data points")
        if isinstance(out_energy, list):
            out_energy = gf.list_to_array_float(out_energy)
        probability = np.array([self.__calculate_probability(isotope,
                               [out_energy[i], out_energy[i+1]], 'disc')
                       for i in range(len(out_energy)-1)], np.dtype(np.float32))
        probability = np.append(np.array(0.0), probability)
        return probability
# =============================================================================================
# =============================================================================================
# =========================            PRIVATE FUNCTIONS           ============================
# =============================================================================================
# =============================================================================================

    def __calculate_probability(self, isotope, out_energy, spec_type):
        """

        :param isotope: str
                        The isotope being analyzed for spectrum, must be a scaler value.
        :param out_energy: float
                           The neutron birth energy for which a probability of \
                           emission is desired in units of MeV.  Must be a scalar \
                           value
        :param spec_type: str
                          'cont' or 'disc' for type of spectrum
        :return probability: float
                             The non-normalized probability of neutron emission for a \
                             user specified neutron birth energy.
        """
        # verify the user specified isotope is in the library.
        gf.verify_isotopes(isotope, self.isotopes, 'Spontaneous ')
        # determine probability of emission
        if isotope == 'Th232':
            a = self.__Th232_a
            b = self.__Th232_b
        elif isotope == 'U232':
            a = self.__U232_a
            b = self.__U232_b
        elif isotope == 'U233':
            a = self.__U233_a
            b = self.__U233_b
        elif isotope == 'U234':
            a = self.__U234_a
            b = self.__U234_b
        elif isotope == 'U235':
            a = self.__U235_a
            b = self.__U235_b
        elif isotope == 'U236':
            a = self.__U236_a
            b = self.__U236_b
        elif isotope == 'U238':
            a = self.__U238_a
            b = self.__U238_b
        elif isotope == 'Np237':
            a = self.__Np237_a
            b = self.__Np237_b
        elif isotope == 'Pu238':
            a = self.__Pu238_a
            b = self.__Pu238_b
        elif isotope == 'Pu239':
            a = self.__Pu239_a
            b = self.__Pu239_b
        elif isotope == 'Pu240':
            a = self.__Pu240_a
            b = self.__Pu240_b
        elif isotope == 'Pu241':
            a = self.__Pu241_a
            b = self.__Pu241_b
        elif isotope == 'Pu242':
            a = self.__Pu242_a
            b = self.__Pu242_b
        elif isotope == 'Am241':
            a = self.__Pu241_a
            b = self.__Pu241_b
        elif isotope == 'Cm242':
            a = self.__Cm242_a
            b = self.__Cm242_b
        elif isotope == 'Cm244':
            a = self.__Cm244_a
            b = self.__Cm244_b
        elif isotope == 'Bk249':
            a = self.__Bk249_a
            b = self.__Bk249_b
        else:
            a = self.__Cf252_a
            b = self.__Cf252_b
        if spec_type == 'cont':
            spectrum = self.__watt_spectrum(out_energy, 1, a, b)
            res, err = spectrum / quad(self.__watt_spectrum, 0, 20, args=(1, a, b))
        else:
            res1, err1 = quad(self.__watt_spectrum, out_energy[0], out_energy[1],
                              args=(1, a, b))
            res2, err2 = quad(self.__watt_spectrum, 0, 20, args=(1, a, b))
            res = res1 / (res2 * (out_energy[1] - out_energy[0]))
        return res
# ---------------------------------------------------------------------------------------------

    def __watt_spectrum(self, e, c, a, b):
        # extractged from page H-3 of reference 1
        return c * np.exp(-e / a) * np.sinh(np.sqrt(b * e))
# =============================================================================================
# =============================================================================================


# support function
def discrete_plot_format(x, y):
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
# eof
