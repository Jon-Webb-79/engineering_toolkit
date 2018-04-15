# import necessary packages here
import unittest
import numpy as np
import sys
from src.physics.blackbody.plank_rad import PlankRadiation
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
        self.body = PlankRadiation()
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
        spectrum = self.body.blackbody_radiation(1.0e-8, 5000.0)
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
        energy = np.linspace(1.0e-8, 1.0e-7, num=10)
        spectrum = self.body.blackbody_radiation(energy, 5000.0)
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
        energy = [1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8, 5.0e-8,
                  6.0e-8, 7.0e-8, 8.0e-8, 9.0e-8, 1.0e-7]
        spectrum = self.body.blackbody_radiation(energy, 5000.0)
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
        energy = [1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8, 5.0e-8,
                  6.0e-8, 7.0e-8, 8.0e-8, 9.0e-8, 1.0e-7]
        try:
            self.body.blackbody_radiation(energy, [5000.0, 6000.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ====================      TEST blackbody_radiation_disc()    ================================
# =============================================================================================
# =============================================================================================


if __name__ == '__main__':
    unittest.main()
# eof
