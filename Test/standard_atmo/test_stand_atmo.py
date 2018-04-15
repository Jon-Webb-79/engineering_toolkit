# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.standard_atmosphere.standard_atmosphere import StandardAtmosphere
# =============================================================================================
# =============================================================================================
# Date:    February 23, 2018
# Purpose: This code tests the functions within the standard atmosphere class
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
        self.alt1 = [-5000.0, -1000.0, 0.0, 3000.0, 7000.0, 11000.0, 19000.0, 27000.0,
                     38000.0, 60572.0, 85638.0, 150000.0, 230000.0, 318000, 460000.0,
                     600000.0, 800000.0, 850000.0, 900000.0, 1000000.0]
        self.alt2 = [86000.0, 100000.0, 130000.0, 160000.0, 200000.0, 230000.0, 270000.0, 310000.0,
                     400000.0, 478000.0, 500000.0, 650000.0, 750000.0, 845000.0, 855000.0,
                     900000.0, 915000.0, 945000.0, 970000.0, 1000000.0]
        self.atmo = StandardAtmosphere()

# =============================================================================================
# =============================================================================================
# =================          TEST geopotential_altitude()      ================================
# =============================================================================================
# =============================================================================================

    def test_geo_alt_scalar(self):
        """
        This is a functional test of geopotential_altitude with a scalar input taken from \
        table II and III of reference 1.  NOTE: There is errata in the source document \
        which mixes u geopotential and geometric altitude
        """
        result = round(self.atmo.geopotential_altitude(3000), 0)
        try:
            self.assertTrue(math.isclose(result, 2999.0, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))

# ---------------------------------------------------------------------------------------------

    def test_geo_alt_list(self):
        """
        This is a functional test of geopotential_altitude() with a list input taken from \
        table II and III of reference 1.  NOTE: There is errata in the source document \
        which mixes u geopotential and geometric altitude
        """
        comparison = np.array([-5004.0, -1000.0, 0.0, 2999.0, 6992.0, 10981.0, 18943.0,
                               26886.0, 37774.0, 60000.0, 84500.0, 146542.0, 221969.0,
                               302850.0, 428959.0, 548252.0, 710574.0, 749747.0, 788380.0,
                               864071.0])
        result = self.atmo.geopotential_altitude(self.alt1)
        try:
            for i in range(len(comparison)):
                test = round(result[i], 0)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_geoscalar_exception(self):
        """
        This function tests gravity for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.geopotential_altitude(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_geo_array_exception(self):
        """
        This function tests gravity for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.geopotential_altitude(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================           TEST gravity()          ================================
# =============================================================================================
# =============================================================================================

    def test_gravity_scalar(self):
        """
        This is a functional test of gravity() with a scalar input taken from \
        table II and III of reference 1.  NOTE: There is errata in the source document \
        which mixes u geopotential and geometric altitude
        """
        result = round(self.atmo.gravity(3000.0), 4)
        try:
            self.assertTrue(math.isclose(result, 9.7974, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_gravity_list(self):
        """
        This is a functional test of gravity() with a list input taken from \
        table II and III of reference 1.  NOTE: There is errata in the source document \
        which mixes u geopotential and geometric altitude
        """
        comparison = np.array([9.8221, 9.8097, 9.8066, 9.7974, 9.7851, 9.7728, 9.7483,
                               9.7239, 9.6904, 9.6224, 9.5477, 9.3597, 9.1337, 8.8945,
                               8.5278, 8.1880, 7.7368, 7.6298, 7.5250, 7.3218])
        result = self.atmo.gravity(self.alt1)
        try:
            for i in range(len(comparison)):
                test = round(result[i], 4)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_gravity_scalar_exception(self):
        """
        This function tests gravity() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.gravity(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_gravity_array_exception(self):
        """
        This function tests gravity() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.gravity(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ==========================        TEST temperature()        =================================
# =============================================================================================
# =============================================================================================

    def test_temperature_scalar(self):
        """
        This is a functional test of temperature() with a scalar input taken from Table 1 \
        of reference 1
        """
        result = np.round(self.atmo.temperature(3000.0), 3)
        try:
            self.assertTrue(math.isclose(result, 268.659, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_temperature_list(self):
        """
        This is a functional test of temperature() with a list input taken from \
        table I of reference 1
        """
        comparison = np.array([320.676, 294.651, 288.15, 268.659, 242.70, 216.773, 216.65,
                               223.536, 244.818, 245.449, 187.651, 634.392, 915.782, 982.554,
                               998.502, 999.853, 999.994, 999.997, 999.999, 1000.0])
        result = self.atmo.temperature(self.alt1)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 4)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_temperature_scalar_exception(self):
        """
        This function tests temperature() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.temperature(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_temperature_array_exception(self):
        """
        This function tests temperature() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.temperature(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# =======================       TEST diatomic_nitrogen()      =================================
# =============================================================================================
# =============================================================================================

    def test_dian2_scalar(self):
        """
        This is a functional test of diatomic_nitrogen() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.diatomic_nitrogen(86000.0)
        try:
            self.assertTrue(math.isclose(result, 1.130e20, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dian2_list(self):
        """
        This is a functional test of diatomic_nitrogen() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([1.130e20, 9.210e18, 1.326e17, 1.774e16, 2.925e15, 9.600e14, 2.494e14,
                               7.024e13, 4.669e12, 4.885e11, 2.592e11, 4.003e9, 2.741e8, 2.299e7,
                               1.778e7, 5.641e6, 3.859e6, 1.815e6, 9.726e5, 4.626e5])
        result = self.atmo.diatomic_nitrogen(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 4)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dian2_scalar_exception(self):
        """
        This function tests diatomic_nitrogen() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.diatomic_nitrogen(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_dian2_array_exception(self):
        """
        This function tests diatomic_nitrogen() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.diatomic_nitrogen(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# =======================       TEST monoatomic_oxygen()      =================================
# =============================================================================================
# =============================================================================================

    def test_monooxygen_scalar(self):
        """
        This is a functional test of monatomic_oxygen() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.monoatomic_oxygen(86000.0)
        try:
            self.assertTrue(math.isclose(result, 8.600e16, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_monooxygen_list(self):
        """
        This is a functional test of monoatomic_oxygen() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([8.60e16, 4.298e17, 4.625e16, 1.238e16, 4.050e15, 2.081e15, 9.447e14,
                               4.540e14, 9.584e13, 2.628e13, 1.836e13, 1.695e12, 3.666e11, 8.901e10,
                               7.685e10, 3.989e10, 3.212e10, 2.088e10, 1.462e10, 9.562e9])
        result = self.atmo.monoatomic_oxygen(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 4)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_monooxygen_scalar_exception(self):
        """
        This function tests monoatomic_oxygen() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.monoatomic_oxygen(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_monooxygen_array_exception(self):
        """
        This function tests monoatomic_oxygen() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.monoatomic_oxygen(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# =======================        TEST dioatomic_oxygen()      =================================
# =============================================================================================
# =============================================================================================

    def test_dioxygen_scalar(self):
        """
        This is a functional test of diatomic_oxygen() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.diatomic_oxygen(86000.0)
        try:
            self.assertTrue(math.isclose(result, 3.031e19, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dioxygen_list(self):
        """
        This is a functional test of diatomic_oxygen() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([3.031e19, 2.151e18, 1.375e16, 1.460e15, 1.918e14, 5.425e13, 1.171e13,
                               2.763e12, 1.252e11, 9.436e9, 4.607e9, 3.932e7, 1.838e6, 1.084e5,
                               8.081e4, 2.177e4, 1.411e4, 5.962e3, 2.924e3, 1.251e3])
        result = self.atmo.diatomic_oxygen(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 4)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dioxygen_scalar_exception(self):
        """
        This function tests diatomic_oxygen() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.diatomic_oxygen(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_dioxygen_array_exception(self):
        """
        This function tests diatomic_oxygen() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.diatomic_oxygen(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# =======================              TEST argon()           =================================
# =============================================================================================
# =============================================================================================

    def test_argon_scalar(self):
        """
        This is a functional test of argon() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.argon(86000.0)
        try:
            self.assertTrue(math.isclose(result, 1.351e18, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_argon_list(self):
        """
        This is a functional test of argon() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([1.351e18, 9.501e16, 3.458e14, 2.321e13, 1.938e12, 4.075e11, 6.078e10,
                               1.007e10, 2.124e8, 8.432e6, 3.445e6, 9.006e3, 1.967e2, 5.742,
                               3.98, 7.742e-1, 4.506e-1, 1.537e-1, 6.312e-2, 2.188e-2])
        result = self.atmo.argon(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 6)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_argon_scalar_exception(self):
        """
        This function tests argon() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.argon(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_argon_array_exception(self):
        """
        This function tests argon() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.argon(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# =======================             TEST helium()           =================================
# =============================================================================================
# =============================================================================================

    def test_helium_scalar(self):
        """
        This is a functional test of helium() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.helium(86000.0)
        try:
            self.assertTrue(math.isclose(result, 7.582e14, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_helium_list(self):
        """
        This is a functional test of helium() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([7.582e14, 1.133e14, 2.972e13, 1.861e13, 1.310e13, 1.083e13, 8.743e12,
                               7.224e12, 4.868e12, 3.518e12, 3.215e12, 1.771e12, 1.208e12, 8.475e11,
                               8.169e11, 6.933e11, 6.567e11, 5.896e11, 5.393e11, 4.850e11])
        result = self.atmo.helium(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 3)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_helium_scalar_exception(self):
        """
        This function tests helium() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.helium(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_helium_array_exception(self):
        """
        This function tests helium() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.helium(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================            TEST hydrogen()           =================================
# =============================================================================================
# =============================================================================================

    def test_hydrogen_scalar(self):
        """
        This is a functional test of hydrogen() with a scalar input taken from \
        Table VIII of reference 1
        """
        result = self.atmo.hydrogen(86000.0)
        try:
            self.assertTrue(math.isclose(result, 0.0, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hydrogen_list(self):
        """
        This is a functional test of hydrogen() with a list input taken from \
        table VIII of reference 1
        """
        comparison = np.array([0.0, 0.0, 0.0, 2.911e11, 1.630e11, 1.324e11, 1.131e11,
                               1.027e11, 8.960e10, 8.191e10, 8.00e10, 6.883e10, 6.249e10, 5.716e10,
                               5.664e10, 5.434e10, 5.361e10, 5.217e10, 5.101e10, 4.967e10])
        result = self.atmo.hydrogen(self.alt2)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 3)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_hydrogen_scalar_exception(self):
        """
        This function tests hydrogen() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.hydrogen(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_hydrogen_array_exception(self):
        """
        This function tests hydrogen() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.hydrogen(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================           TEST molar_mass()          =================================
# =============================================================================================
# =============================================================================================

    def test_molar_mass_scalar(self):
        """
        This is a functional test of molar_mass() with a scalar input taken from \
        Table II of reference 1
        """
        result = self.atmo.molar_mass(0.0)
        try:
            self.assertTrue(math.isclose(round(result, 3), 28.964, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_molar_mass_list(self):
        """
        This is a functional test of molar_mass) with a list input taken from \
        table II of reference 1
        """
        comparison = np.array([28.964, 28.964, 28.964, 28.964, 28.964, 28.964, 28.964,
                               28.964, 28.964, 28.964, 28.955, 24.103, 19.952, 17.326,
                               15.084, 11.506, 5.543, 4.849, 4.404, 3.94])
        result = self.atmo.molar_mass(self.alt1)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 3)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_molar_mass_scalar_exception(self):
        """
        This function tests molar_mass() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.molar_mass(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_molar_mass_array_exception(self):
        """
        This function tests molar_mass() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.molar_mass(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================            TEST pressure()           =================================
# =============================================================================================
# =============================================================================================

    def test_pressure_scalar(self):
        """
        This is a functional test of pressure() with a scalar input taken from \
        Table II of reference 1
        """
        result = self.atmo.pressure(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 1), 1197.0, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_pressure_list(self):
        """
        This is a functional test of pressure() with a list input taken from \
        table II of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([177762, 113931, 101325.0, 70121.2, 41105.3, 22700.0, 6467.6,
                               1879.94, 377.135, 20.3138, 0.39882, 0.00045423, 3.9278e-5, 6.209e-6,
                               5.52e-7, 8.2e-8, 1.70e-8, 1.30e-8, 1.1e-8, 8.0e-9])
        result = self.atmo.pressure(self.alt1)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 9)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_pressure_scalar_exception(self):
        """
        This function tests pressure() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.pressure(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_pressure_array_exception(self):
        """
        This function tests pressure() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.pressure(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================            TEST density()           =================================
# =============================================================================================
# =============================================================================================

    def test_density_scalar(self):
        """
        This is a functional test of density() with a scalar input taken from \
        Table II of reference 1
        """
        result = self.atmo.density(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 5), 1.8410e-2, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_density_list(self):
        """
        This is a functional test of density() with a list input taken from \
        table II of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([1.9311213, 1.3470148, 1.225, 0.9092539, 0.5900184, 0.3648, 0.1039967,
                               0.0292978, 0.0053665, 0.0002883155, 7.4017e-6, 2.075675e-9,
                               1.02925e-10, 1.3169e-11, 1.002e-12, 1.14e-13, 1.1e-14,
                               8.0e-15, 6.0e-15, 4.0e-15])
        result = self.atmo.density(self.alt1)
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 15)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_density_scalar_exception(self):
        """
        This function tests density() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.density(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_density_array_exception(self):
        """
        This function tests density() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.density(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================         TEST speed_of_sound()        =================================
# =============================================================================================
# =============================================================================================

    def test_speed_of_sound_scalar(self):
        """
        This is a functional test of speed_of_sound() with a scalar input taken from \
        Table III of reference 1
        """
        result = self.atmo.speed_of_sound(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 2), 301.71, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_speed_of_sound_list(self):
        """
        This is a functional test of dynamic_viscosity() with a list input taken from \
        table III of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([358.99, 344.11, 340.29, 328.58, 312.31, 295.15, 295.07,
                               299.72, 313.67, 314.07])
        result = self.atmo.speed_of_sound(self.alt1[0:10])
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 2)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_sos_scalar_exception(self):
        """
        This function tests speed_of_sound() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.speed_of_sound(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_sos_array_exception(self):
        """
        This function tests speed_of_sound() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.speed_of_sound(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================        TEST dynamic_viscosity()      =================================
# =============================================================================================
# =============================================================================================

    def test_dynamic_viscosity_scalar(self):
        """
        This is a functional test of dynamic_viscosity() with a scalar input taken from \
        Table III of reference 1
        """
        result = self.atmo.dynamic_viscosity(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 9), 1.4753e-5, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dynamic_viscosity_list(self):
        """
        This is a functional test of dynamic_viscosity() with a list input taken from \
        table III of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([1.9422e-5, 1.8206e-5, 1.7894e-5, 1.6938e-5, 1.5612e-5,
                               1.4223e-5, 1.4216e-5, 1.4592e-5, 1.5723e-5, 1.5756e-5])
        result = self.atmo.dynamic_viscosity(self.alt1[0:10])
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 9)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_dviscosity_scalar_exception(self):
        """
        This function tests dynamic_viscosity() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.dynamic_viscosity(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_dviscosity_array_exception(self):
        """
        This function tests dynamic_viscosity() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.dynamic_viscosity(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================       TEST kinematic_viscosity()     =================================
# =============================================================================================
# =============================================================================================

    def test_kinematic_viscosity_scalar(self):
        """
        This is a functional test of kinematic_viscosity() with a scalar input taken from \
        Table III of reference 1
        """
        result = self.atmo.kinematic_viscosity(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 8), 8.0135e-4, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kinematic_viscosity_list(self):
        """
        This is a functional test of dynamic_viscosity() with a list input taken from \
        table III of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([1.0058e-5, 1.3516e-5, 1.4607e-5, 1.8628e-5, 2.6461e-5,
                               3.8988e-5, 1.36698e-4, 4.98057e-4, 2.929785e-3, 5.4646972e-2])
        result = self.atmo.kinematic_viscosity(self.alt1[0:10])
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 9)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_kviscosity_scalar_exception(self):
        """
        This function tests kinematic_viscosity() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.kinematic_viscosity(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_kviscosity_array_exception(self):
        """
        This function tests kinematic_viscosity() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.kinematic_viscosity(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================
# ======================      TEST thermal_conductivity()     =================================
# =============================================================================================
# =============================================================================================

    def test_thermal_conductivity_scalar(self):
        """
        This is a functional test of thermal_conductivity() with a scalar input taken from \
        Table III of reference 1
        """
        result = self.atmo.thermal_conductivity(30000.0)
        try:
            self.assertTrue(math.isclose(round(result, 6), 2.0331e-2, rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_thermal_conductivity_list(self):
        """
        This is a functional test of dynamic_viscosity() with a list input taken from \
        table III of reference 1.  Numbers had to be validated against hand calculations \
        due to the rounding that was used in reference 1
        """
        comparison = np.array([2.7842e-2, 2.5835e-2, 2.5326e-2, 2.3779e-2, 2.1672e-2,
                               1.9515e-2, 1.9505e-2, 2.0083e-2, 2.1846e-2, 2.1898e-2])
        result = self.atmo.thermal_conductivity(self.alt1[0:10])
        try:
            for i in range(len(comparison)):
                test = np.round(result[i], 6)
                self.assertTrue(math.isclose(test, comparison[i], rel_tol=1.0e-5))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------

    def test_tconductivity_scalar_exception(self):
        """
        This function tests thermal_conductivity() for its ability to handle exceptions with scalars
        """
        try:
            self.atmo.thermal_conductivity(-30000.0)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# ---------------------------------------------------------------------------------------------

    def test_tconductivity_array_exception(self):
        """
        This function tests thermal_conductivity() for its ability to handle exceptions with scalars
        """
        values = np.linspace(-5000.0, 2000000.0, num=50)
        try:
            self.atmo.thermal_conductivity(values)
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
        except SystemExit:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
# =============================================================================================
# =============================================================================================


if __name__ == '__main__':
    unittest.main()
