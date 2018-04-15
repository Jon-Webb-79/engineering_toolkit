# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_miles_to
# =============================================================================================
# =============================================================================================
# Date:    January 22, 2018
# Purpose: This code tests the functions within the square_yards_to module
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

    def test_sq_mm_validate_list(self):
        """
        This is a validation test of square_millimeter() for an array variable
        """
        sq_mm = square_miles_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.59e12, 2 * 2.59e12, 3 * 2.59e12, 4 * 2.59e12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_cm_validate_list(self):
        """
        This is a validation test of square_centimeter() for an array variable
        """
        sq_cm = square_miles_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.59e10, 2 * 2.59e10, 3 * 2.59e10, 4 * 2.59e10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_cm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_meter_validate_list(self):
        """
        This is a validation test of square_meter() for an array variable
        """
        sq_meter = square_miles_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.59e6, 2 * 2.59e6, 3 * 2.59e6, 4 * 2.59e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_kilometer_validate_list(self):
        """
        This is a validation test of square_meter() for an array variable
        """
        sq_kilometer = square_miles_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.58999, 2 * 2.58999, 3 * 2.58999, 4 * 2.58999])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_inches_validate_list(self):
        """
        This is a validation test of square_inches() for an array variable
        """
        sq_inch = square_miles_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([4.014e9, 2 * 4.014e9, 3 * 4.014e9, 4 * 4.014e9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_feet_validate_list(self):
        """
        This is a validation test of square_feet() for an array variable
        """
        sq_foot = square_miles_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.788e7, 2 * 2.788e7, 3 * 2.788e7, 4 * 2.788e7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_yards_validate_list(self):
        """
        This is a validation test of square_yards() for an array variable
        """
        sq_yard = square_miles_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.098e6, 2 * 3.098e6, 3 * 3.098e6, 4 * 3.098e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_acres_validate_list(self):
        """
        This is a validation test of acres() for an array variable
        """
        acre = square_miles_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([640, 2 * 640, 3 * 640, 4 * 640])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(acre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hectacres_validate_list(self):
        """
        This is a validation test of hectacres() for an array variable
        """
        hectacre = square_miles_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([258.999, 2 * 258.999, 3 * 258.999, 4 * 258.999])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
