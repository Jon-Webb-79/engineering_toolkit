# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import astrounits_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the astrounits_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestAstrounitsTo(unittest.TestCase):
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
        attometers = astrounits_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e29, 2*1.496e29, 3*1.496e29, 4*1.496e29])

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
        femtometers = astrounits_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e26, 2*1.496e26, 3*1.496e26, 4*1.496e26])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = astrounits_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e23, 2*1.496e23, 3*1.496e23, 4*1.496e23])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = astrounits_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e21, 2*1.496e21, 3*1.496e21, 4*1.496e21])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = astrounits_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e20, 2*1.496e20, 3*1.496e20, 4*1.496e20])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = astrounits_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e17, 2*1.496e17, 3*1.496e17, 4*1.496e17])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = astrounits_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e14, 2*1.496e14, 3*1.496e14, 4*1.496e14])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = astrounits_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e13, 2*1.496e13, 3*1.496e13, 4*1.496e13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_list(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = astrounits_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e11, 2*1.496e11, 3*1.496e11, 4*1.496e11])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = astrounits_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.496e8, 2*1.496e8, 3*1.496e8, 4*1.496e8])

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
        inch = astrounits_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([5.89e12, 2*5.89e12, 3*5.89e12, 4*5.89e12])

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
        foot = astrounits_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([4.908e11, 2*4.908e11, 3*4.908e11, 4*4.908e11])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = astrounits_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.296e7, 2*9.296e7, 3*9.296e7, 4*9.296e7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        ly = astrounits_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.58125e-5, 2*1.58125e-5, 3*1.58125e-5, 4*1.58125e-5])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = astrounits_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.636e11, 2*1.636e11, 3*1.636e11, 4*1.636e11])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))



if __name__ == '__main__':
    unittest.main()
