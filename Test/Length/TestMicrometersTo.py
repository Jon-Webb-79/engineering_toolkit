# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import micrometers_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the micometers_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================



class TestMicrometersTo(unittest.TestCase):
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
        attometers = micrometers_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e12, 2.0e12, 3.0e12, 4.0e12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST FEMTOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_femtometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometer = micrometers_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e9, 2.0e9, 3.0e9, 4.0e9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometer[i], comparison[i], rel_tol=self.accepted_error))
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
        picometer = micrometers_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e6, 2.0e6, 3.0e6, 4.0e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST ANGSTROMS()          ================================
# =============================================================================================
# =============================================================================================

    def test_angstrom_validate_list(self):
        """
        This is a validation test of angstrom() for an array variable
        """
        angstrom = micrometers_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e4, 2.0e4, 3.0e4, 4.0e4])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST NANOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_nanometer_validate_list(self):
        """
        This is a validation test of nanometer() for an array variable
        """
        nanometer = micrometers_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e3, 2.0e3, 3.0e3, 4.0e3])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MILLIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_millimeter_validate_list(self):
        """
        This is a validation test of millimeter() for an array variable
        """
        millimeter = micrometers_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-3, 2.0e-3, 3.0e-3, 4.0e-3])

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

    def test_centimeter_validate_list(self):
        """
        This is a validation test of centimeter() for an array variable
        """
        centimeter = micrometers_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-4, 2.0e-4, 3.0e-4, 4.0e-4])

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

    def test_meter_validate_list(self):
        """
        This is a validation test of meter() for an array variable
        """
        meter = micrometers_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

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

    def test_kilometer_validate_list(self):
        """
        This is a validation test of kilometer() for an array variable
        """
        kilometer = micrometers_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-9, 2.0e-9, 3.0e-9, 4.0e-9])

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
        inch = micrometers_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.93701e-5, 2*3.93701e-5, 3*3.93701e-5, 4*3.93701e-5])

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
        foot = micrometers_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.28084e-6, 2*3.28084e-6, 3*3.28084e-6, 4*3.28084e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(foot[i], comparison[i], rel_tol=self.accepted_error))
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
        mile = micrometers_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.2137e-10, 2*6.2137e-10, 3*6.2137e-10, 4*6.2137e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST ASTRONOMICAL_UNITS()     ================================
# =============================================================================================
# =============================================================================================

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = micrometers_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.685459e-18, 2*6.685459e-18, 3*6.685459e-18, 4*6.685459e-18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST LIGHT_YEARS()        ================================
# =============================================================================================
# =============================================================================================

    def test_light_years_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        ly = micrometers_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.057e-22, 2*1.057e-22, 3*1.057e-22, 4*1.057e-22])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST LIGHT_YEARS()        ================================
# =============================================================================================
# =============================================================================================

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = micrometers_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.09361e-6, 2*1.09361e-6, 3*1.09361e-6, 4*1.09361e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
