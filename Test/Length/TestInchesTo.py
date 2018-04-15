# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import inches_to
# =============================================================================================
# =============================================================================================
# Date:    January 18, 2018
# Purpose: This code tests the functions within the inches_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestInchesTo(unittest.TestCase):
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
        attometers = inches_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e16, 2*2.54e16, 3*2.54e16, 4*2.54e16])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_list(self):
        """
        This is a validation test of attometers() for an array variable
        """
        femtometers = inches_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e13, 2*2.54e13, 3*2.54e13, 4*2.54e13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = inches_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e10, 2*2.54e10, 3*2.54e10, 4*2.54e10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = inches_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e8, 2*2.54e8, 3*2.54e8, 4*2.54e8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        nanometer = inches_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e7, 2*2.54e7, 3*2.54e7, 4*2.54e7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = inches_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e4, 2*2.54e4, 3*2.54e4, 4*2.54e4])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = inches_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([25.4, 2*25.4, 3*25.4, 4*25.4])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = inches_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54, 2*2.54, 3*2.54, 4*2.54])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_list(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = inches_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0254, 2*0.0254, 3*0.0254, 4*0.0254])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = inches_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.54e-5, 2*2.54e-5, 3*2.54e-5, 4*2.54e-5])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_validate_list(self):
        """
        This is a validation test of feet() for an array variable
        """
        foot = inches_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0/12.0, 2*(1.0/12.0), 3*(1.0/12.0), 4*(1.0/12.0)])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(foot[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = inches_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.57828e-5, 2*1.57828e-5, 3*1.57828e-5, 4*1.57828e-5])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = inches_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.69789e-13, 2*1.69789e-13, 3*1.69789e-13, 4*1.69789e-13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_validate_list(self):
        """
        This is a validation test of light_years() for an array variable
        """
        ly = inches_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.68478e-18, 2*2.68478e-18, 3*2.68478e-18, 4*2.68478e-18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = inches_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0277778, 2*0.0277778, 3*0.0277778, 4*0.0277778])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
