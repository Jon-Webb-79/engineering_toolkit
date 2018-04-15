# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 11, 2018
# Purpose:   This code contains functions required to convert units of inches to other
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

    This function converts feet into attometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e16
# ---------------------------------------------------------------------------------------------


def femtometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return femtometers: float, or double

    This function converts feet into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e13
# ---------------------------------------------------------------------------------------------


def picometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return picometers: float, or double

    This function converts feet into picometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e10
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts feet into pangstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e8
# ---------------------------------------------------------------------------------------------


def nanometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts feet into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e7
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return micrometers: float, or double

    This function converts feet into micrometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e4
# ---------------------------------------------------------------------------------------------


def millimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return millimeters: float, or double

    This function converts feet into millimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 25.4
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeters: float, or double

    This function converts feet into centimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meters: float, or double

    This function converts feet into meters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.0254
# ---------------------------------------------------------------------------------------------


def kilometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return kilometers: float, or double

    This function converts feet into kilometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.54e-5
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts feet into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * (1.0/12.0)
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts feet into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.0277778
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts feet into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.57828e-5
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts feet into astronomical units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.69789e-13
# ---------------------------------------------------------------------------------------------


def light_years(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_years: float, or double

    This function converts feet into astronomical light years
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 2.68478e-18
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
        sys.exit("input into inches_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof
