# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_inches_to
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


class TestSquareInchesTo(unittest.TestCase):
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
        sq_mm = square_inches_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([645.16, 2*645.16, 3*645.16, 4*645.16])

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
        sq_cm = square_inches_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.4516, 2*6.4516, 3*6.4516, 4*6.4516])

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
        sq_meter = square_inches_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.4516e-4, 2*6.4516e-4, 3*6.4516e-4, 4*6.4516e-4])

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
        sq_kilometer = square_inches_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.4516e-10, 2*6.4516e-10, 3*6.4516e-10, 4*6.4516e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_feet_validate_list(self):
        """
        This is a validation test of square_feet() for an array variable
        """
        sq_feet = square_inches_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.00694444, 2*0.00694444, 3*0.00694444, 4*0.00694444])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_feet[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_yards_validate_list(self):
        """
        This is a validation test of square_yards() for an array variable
        """
        sq_yards = square_inches_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.000771605, 2*0.000771605, 3*0.000771605, 4*0.000771605])

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
        sq_mile = square_inches_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.49098e-10, 2*2.49098e-10, 3*2.49098e-10, 4*2.49098e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_acress_validate_list(self):
        """
        This is a validation test of acres() for an array variable
        """
        acres = square_inches_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.59423e-7, 2*1.59423e-7, 3*1.59423e-7, 4*1.59423e-7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(acres[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hectacress_validate_list(self):
        """
        This is a validation test of hectacres() for an array variable
        """
        hectacres = square_inches_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.4516e-8, 2*6.4516e-8, 3*6.4516e-8, 4*6.4516e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacres[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
