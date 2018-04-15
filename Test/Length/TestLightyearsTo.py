# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import light_years_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the light_years_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestLightYears(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
# =============================================================================================
# =============================================================================================
# ==========================         TEST ATTOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_attometers_validate_list(self):
        """
        This is a validation test of attometers() for an array variable
        """
        attometers = light_years_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e33, 2*9.461e33, 3*9.461e33, 4*9.461e33])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometers = light_years_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e30, 2*9.461e30, 3*9.461e30, 4*9.461e30])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        picometers = light_years_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e27, 2*9.461e27, 3*9.461e27, 4*9.461e27])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstrom() for an array variable
        """
        angstrom = light_years_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e25, 2*9.461e25, 3*9.461e25, 4*9.461e25])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of nanometer() for an array variable
        """
        nanometer = light_years_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e24, 2*9.461e24, 3*9.461e24, 4*9.461e24])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometer() for an array variable
        """
        micrometer = light_years_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e21, 2*9.461e21, 3*9.461e21, 4*9.461e21])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeter() for an array variable
        """
        millimeter = light_years_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e18, 2*9.461e18, 3*9.461e18, 4*9.461e18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeter() for an array variable
        """
        centimeter = light_years_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e17, 2*9.461e17, 3*9.461e17, 4*9.461e17])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_list(self):
        """
        This is a validation test of meter() for an array variable
        """
        meter = light_years_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e15, 2*9.461e15, 3*9.461e15, 4*9.461e15])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometer() for an array variable
        """
        kilometer = light_years_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.461e12, 2*9.461e12, 3*9.461e12, 4*9.461e12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_list(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = light_years_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.725e17, 2*3.725e17, 3*3.725e17, 4*3.725e17])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_validate_list(self):
        """
        This is a validation test of feet() for an array variable
        """
        foot = light_years_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.104e16, 2*3.104e16, 3*3.104e16, 4*3.104e16])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_yard_validate_list(self):
        """
        This is a validation test of feet() for an array variable
        """
        yard = light_years_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.035e16, 2*1.035e16, 3*1.035e16, 4*1.035e16])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = light_years_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([5.879e12, 2*5.879e12, 3*5.879e12, 4*5.879e12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = light_years_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([63241.10, 2*63241.10, 3*63241.10, 4*63241.10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
