# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import attometers_to
# =============================================================================================
# =============================================================================================
# Date:    January 14, 2018
# Purpose: This code tests the functions within the attometers_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================

class TestAttometersTo(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40

# =============================================================================================
# =============================================================================================
# ==========================         TEST FEMTOMETERS()        ================================
# =============================================================================================
# =============================================================================================
    def test_femtometers_scalar(self):
        """
        This is a functional test of femtometers() with a scalar input
        """
        try:
            attometers_to.femtometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_array(self):
        """
        This is a functional test of femtometers() with array input
        """
        try:
            attometers_to.femtometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_list(self):
        """
        This is a functional test of femtometers() with a scalar input
        """
        try:
            attometers_to.femtometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_scalar(self):
        """
        This is a validation test of femtometers() for a calar variable
        """
        femtometers = attometers_to.femtometers(1.0)
        try:
            self.assertTrue(math.isclose(femtometers, 0.001, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_array(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometers = attometers_to.femtometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([0.001, 0.002, 0.003, 0.004])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_list(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometers = attometers_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.001, 0.002, 0.003, 0.004])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(femtometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_break1(self):
        """
        This is a break test of femtometers() for a string
        """
        try:
            attometers_to.femtometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_break2(self):
        """
        This is a break test of attometers() for a string
        """
        try:
            attometers_to.femtometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================             TEST FOOT()           ================================
# =============================================================================================
# =============================================================================================

    def test_feet_scalar(self):
        """
        This is a functional test of feet() with a scalar input
        """
        try:
            attometers_to.feet(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_array(self):
        """
        This is a functional test of feet() with array input
        """
        try:
            attometers_to.feet(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_list(self):
        """
        This is a functional test of feet() with a scalar input
        """
        try:
            attometers_to.feet([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_validate_scalar(self):
        """
        This is a validation test of feet() for a calar variable
        """
        feet = attometers_to.feet(1.0)
        try:
            self.assertTrue(math.isclose(feet, 3.28084e-18, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_validate_array(self):
        """
        This is a validation test of feet() for an array variable
        """
        feet = attometers_to.feet(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.28084e-18, 2*3.28084e-18, 3*3.28084e-18, 4*3.28084e-18])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(feet[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feeet_validate_list(self):
        """
        This is a validation test of feet() for an array variable
        """
        feet = attometers_to.feet([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.28084e-18, 2*3.28084e-18, 3*3.28084e-18, 4*3.28084e-18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(feet[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_feet_break1(self):
        """
        This is a break test of feet() for a string
        """
        try:
            attometers_to.feet('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_feet_break2(self):
        """
        This is a break test of feet() for a string
        """
        try:
            attometers_to.feet(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST PICOMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_picometers_scalar(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            attometers_to.picometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_array(self):
        """
        This is a functional test of picometers() with array input
        """
        try:
            attometers_to.picometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_list(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            attometers_to.picometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_scalar(self):
        """
        This is a validation test of feet() for a calar variable
        """
        picometer = attometers_to.picometers(1.0)
        try:
            self.assertTrue(math.isclose(picometer, 1.0e-6, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_array(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometer = attometers_to.picometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])
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
        picometer = attometers_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-6, 2.0e-6, 3.0e-6, 4.0e-6])

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
            attometers_to.picometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_break2(self):
        """
        This is a break test of picometers() for a string
        """
        try:
            attometers_to.picometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST ANGSTROMS()        ================================
# =============================================================================================
# =============================================================================================

    def test_angstroms_scalar(self):
        """
        This is a functional test of angstroms() with a scalar input
        """
        try:
            attometers_to.angstroms(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_array(self):
        """
        This is a functional test of angstroms() with array input
        """
        try:
            attometers_to.angstroms(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_list(self):
        """
        This is a functional test of angstroms() with a scalar input
        """
        try:
            attometers_to.angstroms([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_scalar(self):
        """
        This is a validation test of feet() for a calar variable
        """
        angstrom = attometers_to.angstroms(1.0)
        try:
            self.assertTrue(math.isclose(angstrom, 1.0e-8, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_array(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = attometers_to.angstroms(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_list(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = attometers_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-8, 2.0e-8, 3.0e-8, 4.0e-8])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(angstrom[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_break1(self):
        """
        This is a break test of angstroms() for a string
        """
        try:
            attometers_to.angstroms('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_break2(self):
        """
        This is a break test of angstroms() for a string
        """
        try:
            attometers_to.angstroms(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST NANOMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_nanometers_scalar(self):
        """
        This is a functional test of nanometers() with a scalar input
        """
        try:
            attometers_to.nanometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_array(self):
        """
        This is a functional test of nanometers() with array input
        """
        try:
            attometers_to.nanometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_list(self):
        """
        This is a functional test of nanometers() with a scalar input
        """
        try:
            attometers_to.nanometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_scalar(self):
        """
        This is a validation test of nanometers() for a scalar variable
        """
        nanometer = attometers_to.nanometers(1.0)
        try:
            self.assertTrue(math.isclose(nanometer, 1.0e-9, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_array(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = attometers_to.nanometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-9, 2.0e-9, 3.0e-9, 4.0e-9])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        nanometer = attometers_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-9, 2.0e-9, 3.0e-9, 4.0e-9])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_break1(self):
        """
        This is a break test of nanometers() for a string
        """
        try:
            attometers_to.nanometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_break2(self):
        """
        This is a break test of nanometers() for a string
        """
        try:
            attometers_to.nanometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MICROMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_micrometers_scalar(self):
        """
        This is a functional test of micrometers() with a scalar input
        """
        try:
            attometers_to.micrometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_array(self):
        """
        This is a functional test of micrometers() with array input
        """
        try:
            attometers_to.micrometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_list(self):
        """
        This is a functional test of micrometers() with a scalar input
        """
        try:
            attometers_to.micrometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_scalar(self):
        """
        This is a validation test of micrometers() for a scalar variable
        """
        micrometer = attometers_to.micrometers(1.0)
        try:
            self.assertTrue(math.isclose(micrometer, 1.0e-12, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_array(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = attometers_to.micrometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-12, 2.0e-12, 3.0e-12, 4.0e-12])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_list(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = attometers_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-12, 2.0e-12, 3.0e-12, 4.0e-12])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(micrometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_break1(self):
        """
        This is a break test of micrometers() for a string
        """
        try:
            attometers_to.micrometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_break2(self):
        """
        This is a break test of micrometers() for a string
        """
        try:
            attometers_to.micrometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MILLIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_millimeters_scalar(self):
        """
        This is a functional test of millimeters() with a scalar input
        """
        try:
            attometers_to.millimeters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_array(self):
        """
        This is a functional test of millimeters() with array input
        """
        try:
            attometers_to.millimeters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_list(self):
        """
        This is a functional test of millimeters() with a scalar input
        """
        try:
            attometers_to.millimeters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_scalar(self):
        """
        This is a validation test of millimeters() for a scalar variable
        """
        micrometer = attometers_to.millimeters(1.0)
        try:
            self.assertTrue(math.isclose(micrometer, 1.0e-15, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_array(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = attometers_to.millimeters(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-15, 2.0e-15, 3.0e-15, 4.0e-15])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = attometers_to.millimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-15, 2.0e-15, 3.0e-15, 4.0e-15])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(millimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_break1(self):
        """
        This is a break test of millimeters() for a string
        """
        try:
            attometers_to.millimeters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_break2(self):
        """
        This is a break test of millimeters() for a string
        """
        try:
            attometers_to.millimeters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST MILLIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_centimeters_scalar(self):
        """
        This is a functional test of centimeters() with a scalar input
        """
        try:
            attometers_to.centimeters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_array(self):
        """
        This is a functional test of centimeters() with array input
        """
        try:
            attometers_to.centimeters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_list(self):
        """
        This is a functional test of centimeters() with a scalar input
        """
        try:
            attometers_to.centimeters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_scalar(self):
        """
        This is a validation test of millimeters() for a scalar variable
        """
        centimeter = attometers_to.centimeters(1.0)
        try:
            self.assertTrue(math.isclose(centimeter, 1.0e-16, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_array(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        centimeter = attometers_to.centimeters(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-16, 2.0e-16, 3.0e-16, 4.0e-16])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_list(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        centimeter = attometers_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-16, 2.0e-16, 3.0e-16, 4.0e-16])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_break1(self):
        """
        This is a break test of centimeters() for a string
        """
        try:
            attometers_to.centimeters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_break2(self):
        """
        This is a break test of centimeters() for a string
        """
        try:
            attometers_to.centimeters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST METERS()           ================================
# =============================================================================================
# =============================================================================================

    def test_meters_scalar(self):
        """
        This is a functional test of meters() with a scalar input
        """
        try:
            attometers_to.meters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_array(self):
        """
        This is a functional test of meters() with array input
        """
        try:
            attometers_to.meters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_list(self):
        """
        This is a functional test of meters() with a scalar input
        """
        try:
            attometers_to.meters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_scalar(self):
        """
        This is a validation test of meters() for a scalar variable
        """
        meter = attometers_to.meters(1.0)
        try:
            self.assertTrue(math.isclose(meter, 1.0e-18, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_array(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = attometers_to.meters(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-18, 2.0e-18, 3.0e-18, 4.0e-18])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_list(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = attometers_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-18, 2.0e-18, 3.0e-18, 4.0e-18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(meter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_break1(self):
        """
        This is a break test of meters() for a string
        """
        try:
            attometers_to.meters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_meters_break2(self):
        """
        This is a break test of meters() for a string
        """
        try:
            attometers_to.meters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST KILOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_kilometers_scalar(self):
        """
        This is a functional test of kilometers() with a scalar input
        """
        try:
            attometers_to.kilometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_array(self):
        """
        This is a functional test of kilometers() with array input
        """
        try:
            attometers_to.kilometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_list(self):
        """
        This is a functional test of kilometers() with a scalar input
        """
        try:
            attometers_to.kilometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_scalar(self):
        """
        This is a validation test of kilometers() for a scalar variable
        """
        meter = attometers_to.kilometers(1.0)
        try:
            self.assertTrue(math.isclose(meter, 1.0e-21, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_array(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = attometers_to.kilometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.0e-21, 2.0e-21, 3.0e-21, 4.0e-21])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_list(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = attometers_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.0e-21, 2.0e-21, 3.0e-21, 4.0e-21])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(kilometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_break1(self):
        """
        This is a break test of kilometers() for a string
        """
        try:
            attometers_to.kilometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_break2(self):
        """
        This is a break test of kilometers() for a string
        """
        try:
            attometers_to.kilometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST INCHES()           ================================
# =============================================================================================
# =============================================================================================

    def test_inches_scalar(self):
        """
        This is a functional test of inches() with a scalar input
        """
        try:
            attometers_to.inches(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_array(self):
        """
        This is a functional test of inches() with array input
        """
        try:
            attometers_to.inches(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_list(self):
        """
        This is a functional test of inches() with a scalar input
        """
        try:
            attometers_to.inches([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_scalar(self):
        """
        This is a validation test of inches() for a scalar variable
        """
        inch = attometers_to.inches(1.0)
        try:
            self.assertTrue(math.isclose(inch, 3.93701e-17, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_array(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = attometers_to.inches(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.93701e-17, 2*3.93701e-17, 3*3.93701e-17, 4*3.93701e-17])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_list(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = attometers_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.93701e-17, 2*3.93701e-17, 3*3.93701e-17, 4*3.93701e-17])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(inch[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_break1(self):
        """
        This is a break test of inches() for a string
        """
        try:
            attometers_to.inches('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_inches_break2(self):
        """
        This is a break test of inches() for a string
        """
        try:
            attometers_to.inches(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST MILES()           ================================
# =============================================================================================
# =============================================================================================

    def test_miles_scalar(self):
        """
        This is a functional test of miles() with a scalar input
        """
        try:
            attometers_to.miles(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_array(self):
        """
        This is a functional test of miles() with array input
        """
        try:
            attometers_to.miles(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_list(self):
        """
        This is a functional test of miles() with a scalar input
        """
        try:
            attometers_to.miles([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_scalar(self):
        """
        This is a validation test of miles() for a scalar variable
        """
        mile = attometers_to.miles(1.0)
        try:
            self.assertTrue(math.isclose(mile, 6.21371e-22, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_array(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = attometers_to.miles(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([6.21371e-22, 2*6.21371e-22, 3*6.21371e-22, 4*6.21371e-22])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_list(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = attometers_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.21371e-22, 2*6.21371e-22, 3*6.21371e-22, 4*6.21371e-22])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(mile[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_break1(self):
        """
        This is a break test of miles() for a string
        """
        try:
            attometers_to.miles('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_miles_break2(self):
        """
        This is a break test of miles() for a string
        """
        try:
            attometers_to.miles(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST ASTRONOMICAL_UNITS()     ================================
# =============================================================================================
# =============================================================================================

    def test_astrounits_scalar(self):
        """
        This is a functional test of astronomical_units() with a scalar input
        """
        try:
            attometers_to.astronomical_units(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_array(self):
        """
        This is a functional test of astronomical_units() with array input
        """
        try:
            attometers_to.astronomical_units(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_list(self):
        """
        This is a functional test of astronomical_units() with a scalar input
        """
        try:
            attometers_to.astronomical_units([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_scalar(self):
        """
        This is a validation test of astronomical_units() for a scalar variable
        """
        au = attometers_to.astronomical_units(1.0)
        try:
            self.assertTrue(math.isclose(au, 6.68459e-30, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_array(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = attometers_to.astronomical_units(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([6.68459e-30, 2*6.68459e-30, 3*6.68459e-30, 4*6.68459e-30])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        au = attometers_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([6.68459e-30, 2*6.68459e-30, 3*6.68459e-30, 4*6.68459e-30])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(au[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_break1(self):
        """
        This is a break test of astronomical_units() for a string
        """
        try:
            attometers_to.astronomical_units('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_break2(self):
        """
        This is a break test of astronomical_units() for a string
        """
        try:
            attometers_to.astronomical_units(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST ASTRONOMICAL_UNITS()     ================================
# =============================================================================================
# =============================================================================================

    def test_lightyears_scalar(self):
        """
        This is a functional test of alight_years() with a scalar input
        """
        try:
            attometers_to.light_year(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_array(self):
        """
        This is a functional test of light_years() with array input
        """
        try:
            attometers_to.light_year(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_list(self):
        """
        This is a functional test of light_year() with a scalar input
        """
        try:
            attometers_to.light_year([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_validate_scalar(self):
        """
        This is a validation test of light_year() for a scalar variable
        """
        ly = attometers_to.light_year(1.0)
        try:
            self.assertTrue(math.isclose(ly, 1.057e-34, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_validate_array(self):
        """
        This is a validation test of light_year() for an array variable
        """
        ly = attometers_to.light_year(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.057e-34, 2*1.057e-34, 3*1.057e-34, 4*1.057e-34])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyears_validate_list(self):
        """
        This is a validation test of light_year() for an array variable
        """
        ly = attometers_to.light_year([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.057e-34, 2*1.057e-34, 3*1.057e-34, 4*1.057e-34])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_break1(self):
        """
        This is a break test of light_year() for a string
        """
        try:
            attometers_to.light_year('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_break2(self):
        """
        This is a break test of light_year() for a string
        """
        try:
            attometers_to.light_year(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_yards_validate_list(self):
        """
        This is a validation test of light_year() for an array variable
        """
        yard = attometers_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.09361e-18, 2*1.09361e-18, 3*1.09361e-18, 4*1.09361e-18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))



if __name__ == '__main__':
    unittest.main()
