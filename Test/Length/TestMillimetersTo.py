# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import millimeters_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the millimeters_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestMillimetersTo(unittest.TestCase):
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
        attometers = millimeters_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e15, 2.0e15, 3.0e15, 4.0e15])

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
        femtometers = millimeters_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e12, 2.0e12, 3.0e12, 4.0e12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST PICOOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = millimeters_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e9, 2.0e9, 3.0e9, 4.0e9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST ANGSTROMS()          ================================
# =============================================================================================
# =============================================================================================

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = millimeters_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e7, 2.0e7, 3.0e7, 4.0e7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST NANOMETERS()          ================================
# =============================================================================================
# =============================================================================================

    def test_nanometers_validate_list(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = millimeters_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e6, 2.0e6, 3.0e6, 4.0e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST NANOMETERS()          ================================
# =============================================================================================
# =============================================================================================

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = millimeters_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e3, 2.0e3, 3.0e3, 4.0e3])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST CENTIMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = millimeters_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.1, 0.2, 0.3, 0.4])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST METERS()           ================================
# =============================================================================================
# =============================================================================================

    def test_meters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        meter = millimeters_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.001, 0.002, 0.003, 0.004])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST KILOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_kilometers_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        kilometer = millimeters_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST INCHES()         ================================
# =============================================================================================
# =============================================================================================

    def test_inches_validate_list(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = millimeters_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0393701, 2*0.0393701, 3*0.0393701, 4*0.0393701])

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
        foot = millimeters_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.00328084, 2*0.00328084, 3*0.00328084, 4*0.00328084])

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
        This is a validation test of feet() for an array variable
        """
        mile = millimeters_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.21371e-7, 2*6.21371e-7, 3*6.21371e-7, 4*6.21371e-7])

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
        au = millimeters_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.68459e-15, 2*6.68459e-15, 3*6.68459e-15, 4*6.68459e-15])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST LIGHT_YEARS()         ================================
# =============================================================================================
# =============================================================================================

    def test_lightyears_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        ly = millimeters_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.057e-19, 2*1.057e-19, 3*1.057e-19, 4*1.057e-19])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST YARDS()            ================================
# =============================================================================================
# =============================================================================================

    def test_yards_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        yard = millimeters_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.00109361, 2*0.00109361, 3*0.00109361, 4*0.00109361])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
