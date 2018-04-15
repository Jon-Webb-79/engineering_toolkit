# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 22, 2018
# Purpose:   This code contains functions required to convert units of mm^3 to other
#            Imperial and Metric area units

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def cubic_centimeters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return cubic_centimeter: float, or double

    This function converts acres into cubic centimeters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 0.001
# ---------------------------------------------------------------------------------------------
# =============================================================================================
# =============================================================================================
# =====================                                                 =======================
# =====================               PRIVATE-LIKE FUNCTIONS            =======================
# =====================                                                 =======================
# =============================================================================================
# =============================================================================================


def __first_variable_test(area):
    try:
        area = np.float32(area)
    except ValueError as ve:
        sys.exit(ve)
    return area
# ---------------------------------------------------------------------------------------------


def __second_variable_test(area):
    if isinstance(area, str):
        sys.exit("input into cubic_millimeters_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof