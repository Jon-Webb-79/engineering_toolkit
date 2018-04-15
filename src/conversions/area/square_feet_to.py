# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 22, 2018
# Purpose:   This code contains functions required to convert units of feet^2 to other
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
    :return square_millimeters: float, or double

    This function converts square_feet into square millimeters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 92903
# ----------------------------------------------------------------------------------------------


def square_centimeters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_centimeters: float, or double

    This function converts square_feet into square centimeters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 929.03
# ----------------------------------------------------------------------------------------------


def square_meters(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_meters: float, or double

    This function converts square_feet into square meters
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 0.092903
# ----------------------------------------------------------------------------------------------


def square_kilometers(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_kilometers: float, or double

    This function converts square_feet into square kilometers
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 9.2903e-8
# ----------------------------------------------------------------------------------------------


def square_inches(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_inches: float, or double

    This function converts square_feet into square inches
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 144
# ----------------------------------------------------------------------------------------------


def square_yards(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_yards: float, or double

    This function converts square_feet into square yards
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 0.111111
# ----------------------------------------------------------------------------------------------


def square_miles(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return square_miles: float, or double

    This function converts square_feet into square miles
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 3.58701e-8
# ----------------------------------------------------------------------------------------------


def acres(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return acres: float, or double

    This function converts square_feet into acres
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 2.29568e-5
# ----------------------------------------------------------------------------------------------


def hectacres(area):
    """

    :param area: int, float or double
                     A distance in units of feet
    :return hectacres: float, or double

    This function converts square_feet into hectacres
     """
    if isinstance(area, list):
        area = __first_variable_test(area)
    __second_variable_test(area)
    return area * 9.2903e-6
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
        sys.exit("input into square_feet_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof
