# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import nanometers_to
# =============================================================================================
# =============================================================================================
# Date:    January 11, 2018
# Purpose: This code tests the functions within the nanometers_to module
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
        attometers = nanometers_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e9, 2.0e9, 3.0e9, 4.0e9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST FEMTOETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_femtometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometers = nanometers_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e6, 2.0e6, 3.0e6, 4.0e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST PICOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = nanometers_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1000, 2000, 3000, 4000])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST ANGSTROMS()         ================================
# =============================================================================================
# =============================================================================================

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = nanometers_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([10, 20, 30, 40])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MICROMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = nanometers_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.001, 0.002, 0.003, 0.004])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MILLIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = nanometers_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST CENTIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = nanometers_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-7, 2.0e-7, 3.0e-7, 4.0e-7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST METERS()          ================================
# =============================================================================================
# =============================================================================================

    def test_meters_validate_list(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = nanometers_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-9, 2.0e-9, 3.0e-9, 4.0e-9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST KILOMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = nanometers_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-12, 2.0e-12, 3.0e-12, 4.0e-12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST INCHES()          ================================
# =============================================================================================
# =============================================================================================

    def test_inches_validate_list(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = nanometers_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.93701e-8, 2*3.93701e-8, 3*3.93701e-8, 4*3.93701e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================             TEST FEET()           ================================
# =============================================================================================
# =============================================================================================

    def test_feet_validate_list(self):
        """
        This is a validation test of feet() for an array variable
        """
        feet = nanometers_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.28084e-9, 2*3.28084e-9, 3*3.28084e-9, 4*3.28084e-9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(feet[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST MILES()           ================================
# =============================================================================================
# =============================================================================================

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = nanometers_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.21371e-13, 2*6.21371e-13, 3*6.21371e-13, 4*6.21371e-13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================      TEST ASTRONOMICAL_UNITS()    ================================
# =============================================================================================
# =============================================================================================

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = nanometers_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.68459e-21, 2*6.68459e-21, 3*6.68459e-21, 4*6.68459e-21])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST LIGHT_YEARS()       ================================
# =============================================================================================
# =============================================================================================

    def test_ly_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        ly = nanometers_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.057e-25, 2*1.057e-25, 3*1.057e-25, 4*1.057e-25])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================             TEST YARDS()          ================================
# =============================================================================================
# =============================================================================================

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = nanometers_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.09361e-9, 2*1.09361e-9, 3*1.09361e-9, 4*1.09361e-9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))



if __name__ == '__main__':
    unittest.main()
