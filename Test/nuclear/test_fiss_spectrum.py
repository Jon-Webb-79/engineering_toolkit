# import necessary packages here
import unittest
import numpy as np
import sys
from src.nuclear.n_spec.Spectrum import NeutronSpectrum
from src.nuclear.n_spec.Spectrum import discrete_plot_format
# =============================================================================================
# =============================================================================================
# Date:    January 11, 2018
# Purpose: This code tests the functions within the angstroms_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
        self.watt = NeutronSpectrum.factory('Watt')
        self.maxwell = NeutronSpectrum.factory('Maxwell')
        self.spontaneous = NeutronSpectrum.factory('Spontaneous')
# =============================================================================================
# =============================================================================================
# ====================    TEST Watt.neutron_emission_prob()    ================================
# =============================================================================================
# =============================================================================================

    def test_calculate_watt_prob1(self):
        """
        This is a functional test of Watt.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope exists
        """
        isotopes = ['Th232', 'U233', 'U235', 'U238', 'Pu239']
        try:
            for i in range(len(isotopes)):
                self.watt.neutron_emission_prob_cont(isotopes[i], 2.0, 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_watt_prob_excep1(self):
        """
        This is a functional test of Watt.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope does not exists
        """
        isotopes = ['Th232', 'U233', 'U235', 'U238', 'Pu255']
        try:
            for i in range(len(isotopes)):
                self.watt.neutron_emission_prob_cont(isotopes[i], 2.0, 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_watt_prob2(self):
        """
        This is a functional test of Watt.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0.0001, 10, num=500)
        prob = self.watt.neutron_emission_prob_cont('U235', 2.0, energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 500)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_watt_prob3(self):
        """
        This is a functional test of Watt.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0, 1, num=20)
        prob = self.watt.neutron_emission_prob_disc('U235', 2.0, energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 20)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==================    TEST maxwell.neutron_emission_prob()   ================================
# =============================================================================================
# =============================================================================================

    def test_calculate_maxwell_prob1(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope exists
        """
        isotopes = ['Pa233', 'U234', 'U236', 'U237', 'Np237', 'Pu238',
                    'Pu240', 'Pu241', 'Pu242', 'Am241', 'Pu242m', 'Am243',
                    'Cm242', 'Cm244', 'Cm245', 'Cm246']
        try:
            for i in range(len(isotopes)):
                self.maxwell.neutron_emission_prob_cont(isotopes[i], 2.0, 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_maxwell_excep1(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope does not exists
        """
        isotopes = ['Pa233', 'U234', 'U236', 'U237', 'Np237', 'Pu238',
                    'Pu240', 'Pu241', 'Pu242', 'Am241', 'Pu242m', 'Am243',
                    'Cm242', 'Cm244', 'Cm245', 'Cm248']
        try:
            for i in range(len(isotopes)):
                self.maxwell.neutron_emission_prob_cont(isotopes[i], 2.0, 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_maxwell_prob2(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0.0001, 10, num=500)
        prob = self.maxwell.neutron_emission_prob_cont('Pa233', 2.0, energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 500)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_maxwell_prob3(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0, 1, num=20)
        prob = self.maxwell.neutron_emission_prob_disc('Pu240', 2.0, energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 20)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==================     TEST spont.neutron_emission_prob()    ================================
# =============================================================================================
# =============================================================================================

    def test_calculate_spont_prob1(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope exists
        """
        isotopes = ['Th232', 'U232', 'U233', 'U234', 'U235', 'U236', 'U238',
                    'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242',
                    'Am241', 'Cm242', 'Cm244', 'Bk249', 'Cf252']
        try:
            for i in range(len(isotopes)):
                self.spontaneous.neutron_emission_prob_cont(isotopes[i], 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_spont_excep1(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        determines if the input isotope does not exists
        """
        isotopes = ['Th232', 'U232', 'U233', 'U234', 'U235', 'U236', 'U238',
                    'Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242',
                    'Am241', 'Cm242', 'Cm244', 'Bk249', 'Cf253']
        try:
            for i in range(len(isotopes)):
                self.spontaneous.neutron_emission_prob_cont(isotopes[i], 1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_spont_prob2(self):
        """
        This is a functional test of Maxwell.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0.0001, 10, num=500)
        prob = self.spontaneous.neutron_emission_prob_cont('U233', energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 500)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_calculate_spont_prob3(self):
        """
        This is a functional test of Spontaneous.neutron_emission_prob() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0, 1, num=20)
        prob = self.spontaneous.neutron_emission_prob_disc('U235', energy)
        try:
            self.assertTrue(isinstance(prob, np.ndarray))
            self.assertTrue(np.size(prob) == 20)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==================     TEST spont.neutron_emission_prob()    ================================
# =============================================================================================
# =============================================================================================

    def test_discrete_plot_format(self):
        """
        This is a functional test of discrete_plot_format() to ensure it correctly \
        calculates an array of values
        """
        energy = np.linspace(0, 1, num=20)
        prob = self.watt.neutron_emission_prob_disc('U235', 2.0, energy)
        new_x, new_y = discrete_plot_format(energy, prob)
        try:
            self.assertTrue(len(new_x) == len(new_y))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
