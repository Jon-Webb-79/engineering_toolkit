# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_kilometers_to
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
        sq_mm = square_kilometers_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e12, 2.0e12, 3.0e12, 4.0e12])

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
        sq_cm = square_kilometers_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e10, 2.0e10, 3.0e10, 4.0e10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_cm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_meters_validate_list(self):
        """
        This is a validation test of square_meter() for an array variable
        """
        sq_meter = square_kilometers_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e6, 2.0e6, 3.0e6, 4.0e6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_inches_validate_list(self):
        """
        This is a validation test of square_inches() for an array variable
        """
        sq_inch = square_kilometers_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.55e9, 2*1.55e9, 3*1.55e9, 4*1.55e9])

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
        sq_foot = square_kilometers_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.076e7, 2*1.076e7, 3*1.076e7, 4*1.076e7])

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
        sq_yard = square_kilometers_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.196e6, 2*1.196e6, 3*1.196e6, 4*1.196e6])

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
        sq_mile = square_kilometers_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.386102, 2*0.386102, 3*0.386102, 4*0.386102])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_acres_validate_list(self):
        """
        This is a validation test of square_acres() for an array variable
        """
        acre = square_kilometers_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([247.105, 2*247.105, 3*247.105, 4*247.105])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(acre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hectacres_validate_list(self):
        """
        This is a validation test of square_acres() for an array variable
        """
        hectacre = square_kilometers_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([100, 200, 300, 400])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
