# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_feet_to
# =============================================================================================
# =============================================================================================
# Date:    January 22, 2018
# Purpose: This code tests the functions within the square_feet_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestSquareFeetTo(unittest.TestCase):
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
        sq_mm = square_feet_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([92903, 2*92903, 3*92903, 4*92903])

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
        sq_cm = square_feet_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([929.03, 2*929.03, 3*929.03, 4*929.03])

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
        sq_meter = square_feet_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.092903, 2*0.092903, 3*0.092903, 4*0.092903])

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
        sq_kilometer = square_feet_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.2903e-8, 2*9.2903e-8, 3*9.2903e-8, 4*9.2903e-8])

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
        sq_inches = square_feet_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([144, 2*144, 3*144, 4*144])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_inches[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_yards_validate_list(self):
        """
        This is a validation test of square_yards() for an array variable
        """
        sq_yards = square_feet_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.111111, 2*0.111111, 3*0.111111, 4*0.111111])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_yards[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_miles_validate_list(self):
        """
        This is a validation test of square_miles() for an array variable
        """
        sq_mile = square_feet_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.58701e-8, 2*3.58701e-8, 3*3.58701e-8, 4*3.58701e-8])

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
        acre = square_feet_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.29568e-5, 2*2.29568e-5, 3*2.29568e-5, 4*2.29568e-5])

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
        hectacre = square_feet_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([9.2903e-6, 2*9.2903e-6, 3*9.2903e-6, 4*9.2903e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
