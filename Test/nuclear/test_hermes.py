
# import necessary packages here
import unittest
import numpy as np
import sys
import matplotlib
from matplotlib import rcParams, pyplot as plt
from src.nuclear.photon_spec.hermes import discretized_spectrum
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


class HermesSpecTest(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
# =============================================================================================
# =============================================================================================
# ====================       TEST discretized_spectrum()       ================================
# =============================================================================================
# =============================================================================================

    def test_discretized_spectrum_adapo(self):
        """
        This is a functional test of discretized_spectrum() to ensure it returns the \
        correct number of entries for the Adapo spectrum
        """
        adape, adapp = discretized_spectrum('Adapo')
        try:
            self.assertTrue(len(adape) == 43)
            self.assertTrue(len(adapp) == 43)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_discretized_spectrum_ballard(self):
        """
        This is a functional test of discretized_spectrum() to ensure it returns the \
        correct number of entries for the Ballard spectrum
        """
        bale, balp = discretized_spectrum('Ballard')
        try:
            self.assertTrue(len(bale) == 43)
            self.assertTrue(len(balp) == 43)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_discretized_spectrum_rhsc(self):
        """
        This is a functional test of discretized_spectrum() to ensure it returns the \
        correct number of entries for the RHSC spectrum
        """
        bale, balp = discretized_spectrum('RHSC')
        try:
            self.assertTrue(len(bale) == 61)
            self.assertTrue(len(balp) == 61)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_discretized_spectrum_exception(self):
        """
        This is a functional test of discretized_spectrum() to ensure it returns the \
        correctly handles an ecxeption caused by improperly entering the spectrum \
        name
        """
        try:
            discretized_spectrum('RHSC3')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))


if __name__ == '__main__':
    unittest.main()
