# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_mm_to
# =============================================================================================
# =============================================================================================
# Date:    January 22, 2018
# Purpose: This code tests the functions within the square_mm_to module
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

    def test_sq_cm_validate_list(self):
        """
        This is a validation test of square_centimeter() for an array variable
        """
        sq_cm = square_mm_to.square_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.01, 0.02, 0.03, 0.04])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_cm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_m_validate_list(self):
        """
        This is a validation test of square_meter() for an array variable
        """
        sq_meter = square_mm_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_km_validate_list(self):
        """
        This is a validation test of square_kilometer() for an array variable
        """
        sq_kilometer = square_mm_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-12, 2.0e-12, 3.0e-12, 4.0e-12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_inch_validate_list(self):
        """
        This is a validation test of square_kilometer() for an array variable
        """
        sq_inch = square_mm_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.001155, 2*0.001155, 3*0.001155, 4*0.001155])

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
        sq_foot = square_mm_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.07639e-5, 2*1.07639e-5, 3*1.07639e-5, 4*1.07639e-5])

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
        sq_yards = square_mm_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.19599e-6, 2*1.19599e-6, 3*1.19599e-6, 4*1.19599e-6])

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
        sq_mile = square_mm_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.86102e-13, 2*3.86102e-13, 3*3.86102e-13, 4*3.86102e-13])

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
        acre = square_mm_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.47105e-10, 2*2.47105e-10, 3*2.47105e-10, 4*2.47105e-10])

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
        hectacre = square_mm_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-10, 2.0e-10, 3.0e-10, 4.0e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()

# eof
