# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import miles_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the miles_to module
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

# =============================================================================================
# =============================================================================================
# ==========================         TEST ATTOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_attometers_validate_list(self):
        """
        This is a validation test of attometers() for an array variable
        """
        attometers = miles_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e21, 2 * 1.609e21, 3 * 1.609e21, 4 * 1.609e21])

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
        femtometers = miles_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e18, 2 * 1.609e18, 3 * 1.609e18, 4 * 1.609e18])

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
        picometers = miles_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e15, 2 * 1.609e15, 3 * 1.609e15, 4 * 1.609e15])

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
        angstroms = miles_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e13, 2 * 1.609e13, 3 * 1.609e13, 4 * 1.609e13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstroms[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = miles_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e12, 2 * 1.609e12, 3 * 1.609e12, 4 * 1.609e12])

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
        micrometer = miles_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e9, 2 * 1.609e9, 3 * 1.609e9, 4 * 1.609e9])

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
        millimeter = miles_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e6, 2 * 1.609e6, 3 * 1.609e6, 4 * 1.609e6])

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
        centimeter = miles_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.609e5, 2 * 1.609e5, 3 * 1.609e5, 4 * 1.609e5])

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
        meter = miles_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1609.34, 2*1609.34, 3*1609.34, 4*1609.34])

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
        kilometer = miles_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.60934, 2*1.60934, 3*1.60934, 4*1.60934])

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
        inch = miles_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([63360, 2*63360, 3*63360, 4*63360])

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
        foot = miles_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([5280, 2*5280, 3*5280, 4*5280])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = miles_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1760, 2*1760, 3*1760, 4*1760])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = miles_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0757e-8, 2*1.0757e-8, 3*1.0757e-8, 4*1.0757e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_alightyears_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        ly = miles_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.70108e-13, 2*1.70108e-13, 3*1.70108e-13, 4*1.70108e-13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))



if __name__ == '__main__':
    unittest.main()
