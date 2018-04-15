# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.area import square_cm_to
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
# =============================================================================================
# ==========================         TEST ATTOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_sq_mm_validate_list(self):
        """
        This is a validation test of square_millimeter() for an array variable
        """
        sq_mm = square_cm_to.square_millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([100, 200, 300, 400])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_m_validate_list(self):
        """
        This is a validation test of square_meter() for an array variable
        """
        sq_meter = square_cm_to.square_meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0001, 0.0002, 0.0003, 0.0004])

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
        sq_inch = square_cm_to.square_inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.155, 2*0.155, 3*0.155, 4*0.155])

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
        sq_foot = square_cm_to.square_feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.00107639, 2*0.00107639, 3*0.00107639, 4*0.00107639])

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
        sq_yard = square_cm_to.square_yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.000119599, 2*0.000119599, 3*0.000119599, 4*0.000119599])

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
        sq_mile = square_cm_to.square_miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.86102e-11, 2*3.86102e-11, 3*3.86102e-11, 4*3.86102e-11])

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
        acre = square_cm_to.acres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.47105e-8, 2*2.47105e-8, 3*2.47105e-8, 4*2.47105e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(acre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hectacres_validate_list(self):
        """
        This is a validation test of acres() for an array variable
        """
        hectacre = square_cm_to.hectacres([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(hectacre[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sq_kilometers_validate_list(self):
        """
        This is a validation test of square_kilometers() for an array variable
        """
        sq_km = square_cm_to.square_kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-10, 2.0e-10, 3.0e-10, 4.0e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_km[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
