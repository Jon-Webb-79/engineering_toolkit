# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import hectacres_to
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
        sq_mm = hectacres_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/1.0e-10), 2*(1/1.0e-10), 3*(1/1.0e-10), 4*(1/1.0e-10)])

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
        sq_cm = hectacres_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/1.0e-8), 2*(1/1.0e-8), 3*(1/1.0e-8), 4*(1/1.0e-8)])

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
        sq_meter = hectacres_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/0.0001), 2*(1/0.0001), 3*(1/0.0001), 4*(1/0.0001)])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_kilometers_validate_list(self):
        """
        This is a validation test of square_kilometer() for an array variable
        """
        sq_kilometer = hectacres_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/100), 2*(1/100), 3*(1/100), 4*(1/100)])

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
        sq_inch = hectacres_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/6.4516e-8), 2*(1/6.4516e-8), 3*(1/6.4516e-8), 4*(1/6.4516e-8)])

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
        sq_foot = hectacres_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/9.2903e-6), 2*(1/9.2903e-6), 3*(1/9.2903e-6), 4*(1/9.2903e-6)])

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
        sq_yard = hectacres_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/8.36127e-5), 2*(1/8.36127e-5), 3*(1/8.36127e-5), 4*(1/8.36127e-5)])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_miles_validate_list(self):
        """
        This is a validation test of square_yards() for an array variable
        """
        sq_mile = hectacres_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/258.999), 2*(1/258.999), 3*(1/258.999), 4*(1/258.999)])

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
        sq_acre = hectacres_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1/0.404686), 2*(1/0.404686), 3*(1/0.404686), 4*(1/0.404686)])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_acre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
