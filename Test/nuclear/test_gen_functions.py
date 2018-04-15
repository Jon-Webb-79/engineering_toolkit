# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.nuclear.n_spec import generic_functions
# =============================================================================================
# =============================================================================================
# Date:    January 11, 2018
# Purpose: This code tests the functions within the generic_functions module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestGenFunc(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
# =============================================================================================
# =============================================================================================
# ==========================       TEST verify_isotopes()      ================================
# =============================================================================================
# =============================================================================================

    def test_verify_isotopes(self):
        """
        This is a functional test of verify_isotopes() to ensure that the code \
        correctly determines if an isotope is in a given list
        """
        try:
            generic_functions.verify_isotopes('Pa233', ['Pa233', 'U233', 'Pu239'], 'Maxwell')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_verify_isotopes_exception(self):
        """
        This is a functional test of verify_isotopes() to ensure that the code \
        correctly throws an exception if an isotope is not in an input list
        """
        try:
            generic_functions.verify_isotopes('Pa234', ['Pa233', 'U233', 'Pu239'], 'Maxwell')
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST list_to_array_float()    ================================
# =============================================================================================
# =============================================================================================

    def test_list_to_array(self):
        """
        This is a functional test of list_to_array() to determine if the list is \
        correctly transformed from a list to an array
        """
        transform = generic_functions.list_to_array_float([32.1, 14.687, 32.189, 54.])
        try:
            self.assertTrue(isinstance(transform, np.ndarray))
            self.assertTrue(np.size(transform) == 4)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_list_to_array_exc1(self):
        """
        This is a functional test of list_to_array() to determine if the code will \
        properly throw an exception if one of the inputs is a character string
        """
        try:
            generic_functions.list_to_array_float([32.1, 14.687, 32.189, 'test'])
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_list_to_array_exc2(self):
        """
        This is a functional test of list_to_array() to determine if the code will \
        properly throw an exception if th einput is not a list
        """
        try:
            generic_functions.list_to_array_float(np.array([32.1, 14.687, 32.189, 44.5]))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================     TEST interpolate_values()     ================================
# =============================================================================================
# =============================================================================================

    def test_interpolate_values_list(self):
        """
        This is a functional test of interpolate_values() to determine if the code \
        correctly interpolates between a set of lists
        """
        value = generic_functions.interpolate_values([1.0, 2.0], [1.0, 2.0], 1.5)
        try:
            self.assertTrue(math.isclose(value, 1.50, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_interpolate_values_array(self):
        """
        This is a functional test of interpolate_values() to determine if the code \
        correctly interpolates between a set of arrays
        """
        value = generic_functions.interpolate_values(np.array([1.0, 2.0]),
                                                     np.array([1.0, 2.0]), 1.5)
        try:
            self.assertTrue(math.isclose(value, 1.50, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_interpolate_values_output(self):
        """
        This is a functional test of interpolate_values() to determine if the code \
        correctly interpolates between a set of arrays
        """
        value = generic_functions.interpolate_values(np.array([1.0, 2.0]),
                                                     np.array([1.0, 2.0]),
                                                     np.array([1.5, 1.8]))
        comparison = np.array([1.50, 1.80])
        try:
            for i in range(len(value)):
                self.assertTrue(math.isclose(value[i], comparison[i],
                                             rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))


if __name__ == '__main__':
    unittest.main()
