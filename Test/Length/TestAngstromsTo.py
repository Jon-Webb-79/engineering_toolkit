# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import angstroms_to
# =============================================================================================
# =============================================================================================
# Date:    January 11, 2018
# Purpose: This code tests the functions within the angstroms_to module
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
    def test_attometers_scalar(self):
        """
        This is a functional test of attometers() with a scalar input
        """
        try:
            angstroms_to.attometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_array(self):
        """
        This is a functional test of attometers() with array input
        """
        try:
            angstroms_to.attometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_list(self):
        """
        This is a functional test of attometers() with a scalar input
        """
        try:
            angstroms_to.attometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_scalar(self):
        """
        This is a validation test of attometers() for a calar variable
        """
        angstrom = angstroms_to.attometers(1.0)
        try:
            self.assertTrue(math.isclose(angstrom, 1.0e8, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_array(self):
        """
        This is a validation test of attometers() for an array variable
        """
        angstrom = angstroms_to.attometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e8, 2.0e8, 3.0e8, 4.0e8])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_list(self):
        """
        This is a validation test of attometers() for an array variable
        """
        angstrom = angstroms_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e8, 2.0e8, 3.0e8, 4.0e8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_break1(self):
        """
        This is a break test of attometers() for a string
        """
        try:
            angstroms_to.attometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_break2(self):
        """
        This is a break test of attometers() for a string
        """
        try:
            angstroms_to.attometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST FEMTOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_femtometers_scalar(self):
        """
        This is a functional test of femtometers() with a scalar input
        """
        try:
            angstroms_to.femtometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_array(self):
        """
        This is a functional test of femtometers() with array input
        """
        try:
            angstroms_to.femtometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_list(self):
        """
        This is a functional test of femtometers() with a scalar input
        """
        try:
            angstroms_to.femtometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_scalar(self):
        """
        This is a validation test of attometers() for a calar variable
        """
        femtometer = angstroms_to.femtometers(1.0)
        try:
            self.assertTrue(math.isclose(femtometer, 1.0e5, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_array(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometer = angstroms_to.femtometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e5, 2.0e5, 3.0e5, 4.0e5])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometer = angstroms_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e5, 2.0e5, 3.0e5, 4.0e5])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_break1(self):
        """
        This is a break test of femtometers() for a string
        """
        try:
            angstroms_to.femtometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_break2(self):
        """
        This is a break test of femtometers() for a string
        """
        try:
            angstroms_to.femtometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST PICOOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_picometers_scalar(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            angstroms_to.picometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_array(self):
        """
        This is a functional test of picometers() with array input
        """
        try:
            angstroms_to.picometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_list(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            angstroms_to.picometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_scalar(self):
        """
        This is a validation test of picometers() for a calar variable
        """
        picometer = angstroms_to.picometers(1.0)
        try:
            self.assertTrue(math.isclose(picometer, 100, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_array(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometer = angstroms_to.picometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([100, 200, 300, 400])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometer = angstroms_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([100, 200, 300, 400])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_break1(self):
        """
        This is a break test of picometers() for a string
        """
        try:
            angstroms_to.picometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_break2(self):
        """
        This is a break test of picometers() for a string
        """
        try:
            angstroms_to.picometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST NANOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_nanometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable. FROM THIS \
        POINT ON IT WAS DECIDED TO DO THE SINGLE MOST STRESSING TEST AND NO \
        OTHERS
        """
        nanometer = angstroms_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.1, 0.2, 0.3, 0.4])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MICROMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable.
        """
        micrometer = angstroms_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.0001, 0.0002, 0.0003, 0.0004])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MICROMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable.
        """
        millimeter = angstroms_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-7, 2.0e-7, 3.0e-7, 4.0e-7])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST CENTIMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_centimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable.
        """
        centimeter = angstroms_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST METERS()           ================================
# =============================================================================================
# =============================================================================================

    def test_meters_validate_list(self):
        """
        This is a validation test of meters() for an array variable.
        """
        meter = angstroms_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-10, 2.0e-10, 3.0e-10, 4.0e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST KILOMETERS()           ================================
# =============================================================================================
# =============================================================================================

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometers() for an array variable.
        """
        kilometer = angstroms_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-13, 2.0e-13, 3.0e-13, 4.0e-13])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST INCHES()           ================================
# =============================================================================================
# =============================================================================================

    def test_inches_validate_list(self):
        """
        This is a validation test of inches() for an array variable.
        """
        inch = angstroms_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.93701e-9, 2*3.93701e-9, 3*3.93701e-9, 4*3.93701e-9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST FEET()            ================================
# =============================================================================================
# =============================================================================================

    def test_feet_validate_list(self):
        """
        This is a validation test of feet() for an array variable.
        """
        feet = angstroms_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.28084e-10, 2*3.28084e-10, 3*3.28084e-10, 4*3.28084e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(feet[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST MILES()            ================================
# =============================================================================================
# =============================================================================================

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable.
        """
        mile = angstroms_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.2137e-14, 2*6.2137e-14, 3*6.2137e-14, 4*6.2137e-14])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST ASTRONOMICAL_UNITS()     ================================
# =============================================================================================
# =============================================================================================

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable.
        """
        au = angstroms_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.68459e-22, 2*6.68459e-22, 3*6.68459e-22, 4*6.68459e-22])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST LIGHT_YEARS()        ================================
# =============================================================================================
# =============================================================================================

    def test_ly_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable.
        """
        ly = angstroms_to.light_years([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.057e-26, 2*1.057e-26, 3*1.057e-26, 4*1.057e-26])

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
        yards = angstroms_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.09361e-10, 2*1.09361e-10, 3*1.09361e-10, 4*1.09361e-10])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yards[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))



if __name__ == '__main__':
    unittest.main()
