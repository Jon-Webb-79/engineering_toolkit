# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.length import feet_to
# =============================================================================================
# =============================================================================================
# Date:    January 11, 2018
# Purpose: This code tests the functions within the feet_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestFeetTo(unittest.TestCase):
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
    def test_attormeters_scalar(self):
        """
        This is a functional test of attometers() with a scalar input
        """
        try:
            feet_to.attometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_array(self):
        """
        This is a functional test of attometers() with array input
        """
        try:
            feet_to.attometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_list(self):
        """
        This is a functional test of attometers() with a scalar input
        """
        try:
            feet_to.attometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_scalar(self):
        """
        This is a validation test of attometers() for a calar variable
        """
        attometers = feet_to.attometers(1.0)
        try:
            self.assertTrue(math.isclose(attometers, 3.048e17, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_array(self):
        """
        This is a validation test of attometers() for an array variable
        """
        attometers = feet_to.attometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e17, 6.096e17, 9.144e17, 1.2192e18])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_validate_list(self):
        """
        This is a validation test of attometers() for an array variable
        """
        attometers = feet_to.attometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.048e17, 6.096e17, 9.144e17, 1.2192e18])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(attometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_break1(self):
        """
        This is a break test of attometers() for a string
        """
        try:
            feet_to.attometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_attometers_break2(self):
        """
        This is a break test of attometers() for a string
        """
        try:
            feet_to.attometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST PICOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_picometers_scalaer(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            feet_to.picometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_array(self):
        """
        This is a functional test of picometers() with array input
        """
        try:
            feet_to.picometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_list(self):
        """
        This is a functional test of picometers() with a scalar input
        """
        try:
            feet_to.picometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_scalar(self):
        """
        This is a validation test of picometers() for a calar variable
        """
        picometers = feet_to.picometers(1.0)
        try:
            self.assertTrue(math.isclose(picometers, 3.048e11, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_array(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = feet_to.picometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e11, 6.096e11, 9.144e11, 1.2192e12])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_validate_list(self):
        """
        This is a validation test of picometers() for an array variable
        """
        picometers = feet_to.picometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.float32(np.array([3.048e11, 6.096e11, 9.144e11, 1.2192e12]))
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(picometers[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_break1(self):
        """
        This is a break test of picometers() for a string
        """
        try:
            feet_to.picometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_picometers_break2(self):
        """
        This is a break test of picometers() for a string
        """
        try:
            feet_to.picometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST ANGSTROMS()         ================================
# =============================================================================================
# =============================================================================================

    def test_angstroms_scalar(self):
        """
        This is a functional test of angstroms() with a scalar input
        """
        try:
            feet_to.angstroms(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))

# ---------------------------------------------------------------------------------------------

    def test_angstroms_array(self):
        """
        This is a functional test of angstroms() with array input
        """
        try:
            feet_to.angstroms(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_list(self):
        """
        This is a functional test of angstroms() with a scalar input
        """
        try:
            feet_to.angstroms([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_scalar(self):
        """
        This is a validation test of angstroms() for a calar variable
        """
        angstrom = feet_to.angstroms(1.0)
        try:
            self.assertTrue(math.isclose(angstrom, 3.048e9, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_validate_array(self):
        """
        This is a validation test of angstroms() for an array variable
        """
        angstrom = feet_to.angstroms(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e9, 6.096e9, 9.144e9, 1.2192e10])
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
        angstrom = feet_to.angstroms([1.0, 2.0, 3.0, 4.0])
        comparison = np.float32(np.array([3.048e9, 6.096e9, 9.144e9, 1.2192e10]))
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
            feet_to.angstroms('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_angstroms_break2(self):
        """
        This is a break test of angstroms() for a string
        """
        try:
            feet_to.angstroms(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST NANOMETERS()         ================================
# =============================================================================================
# =============================================================================================

    def test_nanometers_scalar(self):
        """
        This is a functional test of nanometers() with a scalar input
        """
        try:
            feet_to.nanometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_array(self):
        """
        This is a functional test of nanometers() with array input
        """
        try:
            feet_to.nanometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_list(self):
        """
        This is a functional test of nanometers() with a scalar input
        """
        try:
            feet_to.nanometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_scalar(self):
        """
        This is a validation test of nanometers() for a calar variable
        """
        nanometers = feet_to.nanometers(1.0)
        try:
            self.assertTrue(math.isclose(nanometers, 3.048e8, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_array(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = feet_to.nanometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e8, 6.096e8, 9.144e8, 1.2192e9])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(nanometer[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_validate_list(self):
        """
        This is a validation test of nanometers() for an array variable
        """
        nanometer = feet_to.nanometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.048e8, 6.096e8, 9.144e8, 1.2192e9])
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
            feet_to.nanometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_nanometers_break2(self):
        """
        This is a break test of nanometers() for a string
        """
        try:
            feet_to.nanometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST FEMTOMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_femtometers_scalar(self):
        """
        This is a functional test of femotometers() with a scalar input
        """
        try:
            feet_to.femtometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_array(self):
        """
        This is a functional test of femtometers() with array input
        """
        try:
            feet_to.femtometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_list(self):
        """
        This is a functional test of femtometers() with a scalar input
        """
        try:
            feet_to.femtometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_scalar(self):
        """
        This is a validation test of femtometers() for a calar variable
        """
        femtometers = feet_to.femtometers(1.0)
        try:
            self.assertTrue(math.isclose(femtometers, 3.048e14, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_validate_array(self):
        """
        This is a validation test of femtometers() for an array variable
        """
        femtometer = feet_to.femtometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e14, 6.096e14, 9.144e14, 1.2192e15])
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
        femtometer = feet_to.femtometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.048e14, 6.096e14, 9.144e14, 1.2192e15])
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
            feet_to.femtometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_femtometers_break2(self):
        """
        This is a break test of femtometers() for a string
        """
        try:
            feet_to.femtometers(['Test String', 'Test Two'])
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
            feet_to.micrometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_array(self):
        """
        This is a functional test of micrometers() with array input
        """
        try:
            feet_to.micrometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_list(self):
        """
        This is a functional test of micrometers() with a scalar input
        """
        try:
            feet_to.micrometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_scalar(self):
        """
        This is a validation test of micrometers() for a calar variable
        """
        micrometers = feet_to.micrometers(1.0)
        try:
            self.assertTrue(math.isclose(micrometers, 3.048e5, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_validate_array(self):
        """
        This is a validation test of micrometers() for an array variable
        """
        micrometer = feet_to.micrometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e5, 6.096e5, 9.144e5, 1.2192e6])
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
        micrometer = feet_to.micrometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.048e5, 6.096e5, 9.144e5, 1.2192e6])
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
            feet_to.micrometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_micrometers_break2(self):
        """
        This is a break test of micrometers() for a string
        """
        try:
            feet_to.micrometers(['Test String', 'Test Two'])
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
            feet_to.millimeters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_array(self):
        """
        This is a functional test of millimeters() with array input
        """
        try:
            feet_to.millimeters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_list(self):
        """
        This is a functional test of millimeters() with a scalar input
        """
        try:
            feet_to.millimeters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_scalar(self):
        """
        This is a validation test of millimeters() for a calar variable
        """
        millimeter = feet_to.millimeters(1.0)
        try:
            self.assertTrue(math.isclose(millimeter, 304.8, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_validate_array(self):
        """
        This is a validation test of millimeters() for an array variable
        """
        millimeter = np.float32(feet_to.millimeters(np.array([1.0, 2.0, 3.0, 4.0])))
        comparison = np.array([304.8, 609.6, 914.4, 1219.2])
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
        millimeter = np.round(np.float32(feet_to.millimeters([1.0, 2.0, 3.0, 4.0])), 2)
        comparison = np.round(np.float32(np.array([304.8, 609.6, 914.4, 1219.2])), 2)
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
            feet_to.millimeters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_millimeters_break2(self):
        """
        This is a break test of millimeters() for a string
        """
        try:
            feet_to.millimeters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST CENTIMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_centimeters_scalar(self):
        """
        This is a functional test of centimeters() with a scalar input
        """
        try:
            feet_to.centimeters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_array(self):
        """
        This is a functional test of centimeters() with array input
        """
        try:
            feet_to.centimeters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_list(self):
        """
        This is a functional test of centimeters() with a scalar input
        """
        try:
            feet_to.centimeters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_scalar(self):
        """
        This is a validation test of centimeters() for a calar variable
        """
        centimeter = feet_to.centimeters(1.0)
        try:
            self.assertTrue(math.isclose(centimeter, 30.48, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_validate_array(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = feet_to.centimeters(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([30.48, 60.96, 91.44, 121.92])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(centimeter[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_centiimeters_validate_list(self):
        """
        This is a validation test of centimeters() for an array variable
        """
        centimeter = feet_to.centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([30.48, 60.96, 91.44, 121.92])
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
            feet_to.centimeters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_centimeters_break2(self):
        """
        This is a break test of centimeters() for a string
        """
        try:
            feet_to.centimeters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================            TEST METERS()          ================================
# =============================================================================================
# =============================================================================================

    def test_meters_scalar(self):
        """
        This is a functional test of meters() with a scalar input
        """
        try:
            feet_to.meters(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_array(self):
        """
        This is a functional test of meters() with array input
        """
        try:
            feet_to.meters(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_list(self):
        """
        This is a functional test of meters() with a scalar input
        """
        try:
            feet_to.meters([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_scalar(self):
        """
        This is a validation test of meters() for a calar variable
        """
        meter = feet_to.meters(1.0)
        try:
            self.assertTrue(math.isclose(meter, 0.3048, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_meters_validate_array(self):
        """
        This is a validation test of meters() for an array variable
        """
        meter = feet_to.meters(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([0.3048, 0.6096, 0.9144, 1.2192])
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
        meter = feet_to.meters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.3048, 0.6096, 0.9144, 1.2192])
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
            feet_to.meters('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_meters_break2(self):
        """
        This is a break test of meters() for a string
        """
        try:
            feet_to.meters(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================          TEST KILOMETERS()        ================================
# =============================================================================================
# =============================================================================================

    def test_kilometers_scalar(self):
        """
        This is a functional test of kilometers() with a scalar input
        """
        try:
            feet_to.kilometers(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_array(self):
        """
        This is a functional test of kilometers() with array input
        """
        try:
            feet_to.kilometers(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_list(self):
        """
        This is a functional test of kilometers() with a scalar input
        """
        try:
            feet_to.kilometers([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_scalar(self):
        """
        This is a validation test of kilometers() for a calar variable
        """
        kilometer = feet_to.kilometers(1.0)
        try:
            self.assertTrue(math.isclose(kilometer, 3.048e-4, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_validate_array(self):
        """
        This is a validation test of kilometers() for an array variable
        """
        kilometer = feet_to.kilometers(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.048e-4, 6.096e-4, 9.144e-4, 1.2192e-3])
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
        kilometer = feet_to.kilometers([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.048e-4, 6.096e-4, 9.144e-4, 1.2192e-3])
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
            feet_to.kilometers('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_kilometers_break2(self):
        """
        This is a break test of kilometers() for a string
        """
        try:
            feet_to.kilometers(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================             TEST INCHES()         ================================
# =============================================================================================
# =============================================================================================

    def test_inches_scalar(self):
        """
        This is a functional test of inches() with a scalar input
        """
        try:
            feet_to.inches(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_array(self):
        """
        This is a functional test of inches() with array input
        """
        try:
            feet_to.inches(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_list(self):
        """
        This is a functional test of inches() with a scalar input
        """
        try:
            feet_to.inches([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_scalar(self):
        """
        This is a validation test of inches() for a calar variable
        """
        inch = feet_to.inches(1.0)
        try:
            self.assertTrue(math.isclose(inch, 12, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_inches_validate_array(self):
        """
        This is a validation test of inches() for an array variable
        """
        inch = feet_to.inches(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([12.0, 24.0, 36.0, 48.0])
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
        inch = feet_to.inches([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([12.0, 24.0, 36.0, 48.0])
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
            feet_to.inches('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_inches_break2(self):
        """
        This is a break test of inches() for a string
        """
        try:
            feet_to.inches(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================             TEST MILES()          ================================
# =============================================================================================
# =============================================================================================

    def test_miles_scalar(self):
        """
        This is a functional test of miles() with a scalar input
        """
        try:
            feet_to.miles(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_array(self):
        """
        This is a functional test of miles() with array input
        """
        try:
            feet_to.miles(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_list(self):
        """
        This is a functional test of miles() with a scalar input
        """
        try:
            feet_to.miles([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_scalar(self):
        """
        This is a validation test of miles() for a calar variable
        """
        mile = feet_to.miles(1.0)
        try:
            self.assertTrue(math.isclose(mile, 1.89394e-4, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_miles_validate_array(self):
        """
        This is a validation test of miles() for an array variable
        """
        mile = feet_to.miles(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([1.89394e-4, 2*1.89394e-4, 3*1.89394e-4, 4*1.89394e-4])
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
        mile = feet_to.miles([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([1.89394e-4, 2*1.89394e-4, 3*1.89394e-4, 4*1.89394e-4])
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
            feet_to.miles('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_miles_break2(self):
        """
        This is a break test of miles() for a string
        """
        try:
            feet_to.miles(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST ASTRO_UNITS()        ================================
# =============================================================================================
# =============================================================================================

    def test_astrounits_scalar(self):
        """
        This is a functional test of astronomical_units() with a scalar input
        """
        try:
            feet_to.astronomical_units(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_array(self):
        """
        This is a functional test of astronomical_units() with array input
        """
        try:
            feet_to.astronomical_units(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_list(self):
        """
        This is a functional test of astronomical_units() with a scalar input
        """
        try:
            feet_to.astronomical_units([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_scalar(self):
        """
        This is a validation test of astronomical_units() for a calar variable
        """
        astro = feet_to.astronomical_units(1.0)
        try:
            self.assertTrue(math.isclose(astro, 2.03746e-12, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_array(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        astro = feet_to.astronomical_units(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([2.03746e-12, 2*2.03746e-12, 3*2.03746e-12, 4*2.03746e-12])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(astro[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_validate_list(self):
        """
        This is a validation test of astronomical_units() for an array variable
        """
        astro = feet_to.astronomical_units([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([2.03746e-12, 2*2.03746e-12, 3*2.03746e-12, 4*2.03746e-12])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(astro[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_break1(self):
        """
        This is a break test of astronomical_units() for a string
        """
        try:
            feet_to.astronomical_units('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_astrounits_break2(self):
        """
        This is a break test of astronomical_units() for a string
        """
        try:
            feet_to.astronomical_units(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================         TEST LIGHT_YEARS()        ================================
# =============================================================================================
# =============================================================================================

    def test_lightyear_scalar(self):
        """
        This is a functional test of light_year() with a scalar input
        """
        try:
            feet_to.light_year(1.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_array(self):
        """
        This is a functional test of light_year() with array input
        """
        try:
            feet_to.light_year(np.linspace(1.0, 5.0, num=5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_list(self):
        """
        This is a functional test of light_year() with a scalar input
        """
        try:
            feet_to.light_year([1.0, 2.0, 3.0, 4.0, 5.0])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_validate_scalar(self):
        """
        This is a validation test of light_year() for a calar variable
        """
        ly = feet_to.light_year(1.0)
        try:
            self.assertTrue(math.isclose(ly, 3.22174e-17, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_validate_array(self):
        """
        This is a validation test of light_year() for an array variable
        """
        ly = feet_to.light_year(np.array([1.0, 2.0, 3.0, 4.0]))
        comparison = np.array([3.22174e-17, 2*3.22174e-17, 3*3.22174e-17, 4*3.22174e-17])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_validate_list(self):
        """
        This is a validation test of light_year() for an array variable
        """
        ly = feet_to.light_year([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([3.22174e-17, 2*3.22174e-17, 3*3.22174e-17, 4*3.22174e-17])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(ly[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_break1(self):
        """
        This is a break test of alight_year() for a string
        """
        try:
            feet_to.light_year('Test String')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_lightyear_break2(self):
        """
        This is a break test of light_year() for a string
        """
        try:
            feet_to.light_year(['Test String', 'Test Two'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================

    def test_yards_validate_list(self):
        """
        This is a validation test of yards() for an array variable
        """
        yard = feet_to.yards([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([(1.0/3.0), 2*(1.0/3.0), 3*(1.0/3.0), 4*(1.0/3.0)])
        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(yard[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
