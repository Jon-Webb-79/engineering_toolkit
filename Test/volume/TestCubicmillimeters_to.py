# import necessary packages here
import unittest
import numpy as np
import sys
import math
from src.conversions.volume import cubic_mm_to
# =============================================================================================
# =============================================================================================
# Date:    January 22, 2018
# Purpose: This code tests the functions within the square_yards_to module
# NOTE:    file is run with >> python3 -m unittest Test.TestReader from the engineering_toolkit
#          directory

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================


class TestCubicMillimeters(unittest.TestCase):
    def setUp(self):
        self.accepted_error = 1e-6
        self.passed = '.......................... OK'
        self.failed = '.......................... FAILED'
        self.padding = ' ' + '.' * 40
# =============================================================================================

    def test_cubic_cm_validate_list(self):
        """
        This is a validation test of cubic_centimeter() for an array variable
        """
        sq_mm = cubic_mm_to.cubic_centimeters([1.0, 2.0, 3.0, 4.0])
        comparison = np.array([0.001, 2*0.001, 3*0.001, 4*0.001])

        try:
            for i in range(len(comparison)):
                self.assertTrue(math.isclose(sq_mm[i], comparison[i], rel_tol=self.accepted_error))
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.passed))
        except AssertionError:
            print('{:.40s}{}'.format(sys._getframe().f_code.co_name + self.padding, self.failed))
# ---------------------------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()
