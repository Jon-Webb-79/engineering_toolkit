# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 16, 2018
# Purpose:   This code contains functions required to convert units of nanometers to other
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

    This function converts angstroms into attometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e9
# ---------------------------------------------------------------------------------------------


def femtometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return femtometers: float, or double

    This function converts angstroms into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e6
# ---------------------------------------------------------------------------------------------


def picometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return picometers: float, or double

    This function converts angstroms into picometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1000
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts angstroms into angstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 10
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return micrometers: float, or double

    This function converts angstroms into micrometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.001
# ---------------------------------------------------------------------------------------------


def millimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return millimeters: float, or double

    This function converts angstroms into millimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-6
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeters: float, or double

    This function converts angstroms into centimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-7
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meters: float, or double

    This function converts angstroms into meters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-9
# ---------------------------------------------------------------------------------------------


def kilometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return kilometers: float, or double

    This function converts angstroms into kilometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-12
# ---------------------------------------------------------------------------------------------


def inches(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return inches: float, or double

    This function converts angstroms into inches
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.93701e-8
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts angstroms into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.28084e-9
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return yards: float, or double

    This function converts angstroms into yards
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.09361e-9
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts angstroms into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.21371e-13
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts angstroms into astronomical units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.68459e-21
# ---------------------------------------------------------------------------------------------


def light_years(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_years: float, or double

    This function converts angstroms into light years
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.057e-25
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
        sys.exit("input into nanometers_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof