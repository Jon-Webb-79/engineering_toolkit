# import necessary packages here
import unittest
import numpy as np
import sys
from src.nuclear.blackbody.spectrum import BlackBodyRadiation
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


class BlkbdySpectrum(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
        self.body = BlackBodyRadiation()
# =============================================================================================
# =============================================================================================
# ====================      TEST blackbody_radiation_cont()    ================================
# =============================================================================================
# =============================================================================================

    def test_blackbody_radiation_cont_scalar(self):
        """
        This is a functional test of blackbody_radiation_cont() to ensure it correctly \
        processes scalar inputs
        """
        spectrum = self.body.blackbody_radiation_cont(0.1, 15.0)
        try:
            self.assertTrue(np.size(spectrum) == 1)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_array(self):
        """
        This is a functional test of blackbody_radiation_cont() to ensure it correctly \
        handles array energy inputs
        """
        energy = np.linspace(0.01, 0.1, num=10)
        spectrum = self.body.blackbody_radiation_cont(energy, 15.0)
        try:
            self.assertTrue(np.size(spectrum) == 10)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_list(self):
        """
        This is a functional test of blackbody_radiation_cont() to ensure it correctly \
        handles list energy inputs
        """
        energy = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
        spectrum = self.body.blackbody_radiation_cont(energy, 15.0)
        try:
            self.assertTrue(np.size(spectrum) == 10)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_cont_exception2(self):
        """
        This is a functional test of blackbody_radiation_cont() to ensure it correctly \
        handles an exception caused by entering temperature with size greater than \
        1
        """
        energy = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
        try:
            self.body.blackbody_radiation_cont(energy, [15.0, 20.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ====================      TEST blackbody_radiation_disc()    ================================
# =============================================================================================
# =============================================================================================

    def test_blackbody_radiation_disk_exception(self):
        """
        This is a functional test of blackbody_radiation_disc() to ensure it correctly \
        handles an exception caused by an energy input of size less than 2
        """
        try:
            self.body.blackbody_radiation_disc(0.1, 15.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_disk_array(self):
        """
        This is a functional test of blackbody_radiation_disc() to ensure it correctly \
        correctly handles an array input
        """
        energy = np.linspace(0.01, 0.1, num=10)
        result = self.body.blackbody_radiation_disc(energy, 15.0)
        try:
            self.assertTrue(np.size(result) == 10)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_disk_list(self):
        """
        This is a functional test of blackbody_radiation_disc() to ensure it correctly \
        correctly handles an list input
        """
        energy = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
        result = self.body.blackbody_radiation_disc(energy, 15.0)
        try:
            self.assertTrue(np.size(result) == 10)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_blackbody_radiation_disc_exception2(self):
        """
        This is a functional test of blackbody_radiation_cont() to ensure it correctly \
        handles an exception caused by entering temperature with size greater than \
        1
        """
        energy = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
        try:
            self.body.blackbody_radiation_disc(energy, [15.0, 20.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))


if __name__ == '__main__':
    unittest.main()
# eof
