# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 15, 2017
# Purpose:   This code contains functions required to convert units of picometers to other
#            Imperial and Metric length units

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def femtometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return femtometers: float, or double

    This function converts picometers into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1000
# ---------------------------------------------------------------------------------------------


def attometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return attometers: float, or double

    This function converts picometers into attometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1000000
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts picometers into angstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.01
# ---------------------------------------------------------------------------------------------


def nanometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts picometers into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.001
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return micrometers: float, or double

    This function converts picometers into micrometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-6
# ---------------------------------------------------------------------------------------------


def millimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return millimeters: float, or double

    This function converts picometers into millimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-9
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeters: float, or double

    This function converts picometers into centimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-10
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meters: float, or double

    This function converts picometers into meters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-12
# ---------------------------------------------------------------------------------------------


def kilometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return kilometers: float, or double

    This function converts picometers into kilometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-15
# ---------------------------------------------------------------------------------------------


def inches(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return inches: float, or double

    This function converts picometers into inches
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.93701e-11
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts picometers into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.28084e-12
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return yards: float, or double

    This function converts picometers into yards
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.09361e-12
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts picometers into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.21371e-16
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts picometers into astronomical_units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.68459e-24
# ---------------------------------------------------------------------------------------------


def light_year(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_year: float, or double

    This function converts picometers into light year
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.057e-28
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
        sys.exit("input into picometers_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof
