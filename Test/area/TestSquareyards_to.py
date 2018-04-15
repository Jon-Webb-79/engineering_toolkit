# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_yards_to
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


class TestSquareYards(unittest.TestCase):
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
        sq_mm = square_yards_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([836127, 2*836127, 3*836127, 4*836127])

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
        sq_cm = square_yards_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([8361.27, 2*8361.27, 3*8361.27, 4*8361.27])

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
        sq_meter = square_yards_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.836127, 2*0.836127, 3*0.836127, 4*0.836127])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_kilometer_validate_list(self):
        """
        This is a validation test of square_kilometer() for an array variable
        """
        sq_kilometer = square_yards_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([8.36127e-7, 2*8.36127e-7, 3*8.36127e-7, 4*8.36127e-7])

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
        sq_inch = square_yards_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1296, 2*1296, 3*1296, 4*1296])

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
        sq_foot = square_yards_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9, 2*9, 3*9, 4*9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_miles_validate_list(self):
        """
        This is a validation test of square_miles() for an array variable
        """
        sq_mile = square_yards_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.22831e-7, 2*3.22831e-7, 3*3.22831e-7, 4*3.22831e-7])

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
        acre = square_yards_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.06612e-4, 2*2.06612e-4, 3*2.06612e-4, 4*2.06612e-4])

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
        hectacre = square_yards_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([8.36127e-5, 2*8.36127e-5, 3*8.36127e-5, 4*8.36127e-5])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
