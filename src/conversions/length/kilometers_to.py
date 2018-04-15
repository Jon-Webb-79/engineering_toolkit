# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 20, 2018
# Purpose:   This code contains functions required to convert units of kilometers to other
#            Imperial and Metric length units

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def attometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return attometers: float, or double

    This function converts kilometers into attometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e21
# ---------------------------------------------------------------------------------------------


def femtometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return femtometers: float, or double

    This function converts kilometers into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e18
# ---------------------------------------------------------------------------------------------


def picometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return picometers: float, or double

    This function converts kilometers into picometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e15
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts kilometers into angstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e13
# ---------------------------------------------------------------------------------------------


def nanometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts kilometers into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e12
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return micrometer: float, or double

    This function converts kilometers into micrometer
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e9
# ---------------------------------------------------------------------------------------------


def millimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return millimeter: float, or double

    This function converts kilometers into millimeter
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e6
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeter: float, or double

    This function converts kilometers into centimeter
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e5
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meter: float, or double

    This function converts kilometers into meter
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e3
# ---------------------------------------------------------------------------------------------


def inches(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return inches: float, or double

    This function converts kilometers into inches
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 39370.10
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts kilometers into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3280.84
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return yards: float, or double

    This function converts kilometers into yards
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1093.61
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts kilometers into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.621371
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts kilometers into astronomical units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.68459e-9
# ---------------------------------------------------------------------------------------------


def light_years(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_years: float, or double

    This function converts kilometers into light years
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.057e-13
# =============================================================================================
# =============================================================================================
# =====================                                                 =======================
# =====================               PRIVATE-LIKE FUNCTIONS            =======================
# =====================                                                 =======================
# =============================================================================================
# =============================================================================================


def __first_variable_test(distance):
    try:
        distance = np.float32(distance)
    except ValueError as ve:
        sys.exit(ve)
    return distance
# ---------------------------------------------------------------------------------------------


def __second_variable_test(distance):
    if isinstance(distance, str):
        sys.exit("input into kilometers_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof
