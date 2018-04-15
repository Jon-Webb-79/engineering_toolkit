# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_meters_to
# =============================================================================================
# =============================================================================================
# Date:    January 22, 2018
# Purpose: This code tests the functions within the square_cm_to module
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
        sq_mm = square_meters_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e6, 2.0e6, 3.0e6, 4.0e6])

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
        sq_cm = square_meters_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([10000, 20000, 30000, 40000])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_cm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_km_validate_list(self):
        """
        This is a validation test of square_kilometer() for an array variable
        """
        sq_km = square_meters_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_km[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_inches_validate_list(self):
        """
        This is a validation test of square_inches() for an array variable
        """
        sq_inch = square_meters_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1550, 2*1550, 3*1550, 4*1550])

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
        sq_foot = square_meters_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([10.7639, 2*10.7639, 3*10.7639, 4*10.7639])

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
        sq_yard = square_meters_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.19599, 2*1.19599, 3*1.19599, 4*1.19599])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_miles_validate_list(self):
        """
        This is a validation test of square_miles() for an array variable
        """
        sq_mile = square_meters_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.86102e-7, 2*3.86102e-7, 3*3.86102e-7, 4*3.86102e-7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_acres_validate_list(self):
        """
        This is a validation test of acres() for an array variable
        """
        sq_acre = square_meters_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.000247105, 2*0.000247105, 3*0.000247105, 4*0.000247105])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_acre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hectacres_validate_list(self):
        """
        This is a validation test of hectacres() for an array variable
        """
        sq_hectacre = square_meters_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0001, 0.0002, 0.0003, 0.0004])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
