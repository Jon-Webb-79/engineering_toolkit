# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 19, 2018
# Purpose:   This code contains functions required to convert units of millimeters to other
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

    This function converts millimeters into attometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e15
# ---------------------------------------------------------------------------------------------


def femtometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return femtometers: float, or double

    This function converts millimeters into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e12
# ---------------------------------------------------------------------------------------------


def picometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return picometers: float, or double

    This function converts millimeters into picometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e9
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts millimeters into angstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e7
# ---------------------------------------------------------------------------------------------


def nanometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts millimeters into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e6
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts millimeters into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e3
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeters: float, or double

    This function converts millimeters into centimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.1
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meters: float, or double

    This function converts millimeters into meters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.001
# ---------------------------------------------------------------------------------------------


def kilometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return kilometers: float, or double

    This function converts millimeters into kilometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-6
# ---------------------------------------------------------------------------------------------


def inches(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return inches: float, or double

    This function converts millimeters into inches
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.0393701
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts millimeters into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.00328084
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return yards: float, or double

    This function converts millimeters into yards
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.00109361
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts millimeters into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.21371e-7
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts millimeters into astronomical_units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.68459e-15
# ---------------------------------------------------------------------------------------------


def light_years(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_years: float, or double

    This function converts millimeters into light_years
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.057e-19
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
        sys.exit("input into millimeters_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof