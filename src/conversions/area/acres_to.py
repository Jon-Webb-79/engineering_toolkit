# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 22, 2018
# Purpose:   This code contains functions required to convert units of acres to other
#            Imperial and Metric area units

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def square_millimeters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_millimeter: float, or double

    This function converts acres into square millimeters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/2.47105e-10
# ---------------------------------------------------------------------------------------------


def square_centimeters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_centimeter: float, or double

    This function converts acres into square centimeters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/2.47105e-8
# ---------------------------------------------------------------------------------------------


def square_meters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_meter: float, or double

    This function converts acres into square meters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/0.000247105
# ---------------------------------------------------------------------------------------------


def square_kilometers(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_kilometer: float, or double

    This function converts acres into square kilometers
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/247.105
# ---------------------------------------------------------------------------------------------


def square_inches(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_inches: float, or double

    This function converts acres into square inches
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/1.59423e-7
# ---------------------------------------------------------------------------------------------


def square_feet(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_feet: float, or double

    This function converts acres into square feet
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/2.29568e-5
# ---------------------------------------------------------------------------------------------


def square_yards(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_yards: float, or double

    This function converts acres into square yards
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/2.06612e-4
# ---------------------------------------------------------------------------------------------


def square_miles(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_miles: float, or double

    This function converts acres into square miles
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 1/640
# ---------------------------------------------------------------------------------------------


def hectacres(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return hectacres: float, or double

    This function converts acres into hectacres
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 0.404686
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
        sys.exit("input into square_acres_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof