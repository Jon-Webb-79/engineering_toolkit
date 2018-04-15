# Import modules here
import sys
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      January 14, 2017
# Purpose:   This code contains functions required to convert units of attometers to other
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

    This function converts attometers into femtometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 0.001
# ---------------------------------------------------------------------------------------------


def feet(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return feet: float, or double

    This function converts attometers into feet
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.28084e-18
# ---------------------------------------------------------------------------------------------


def picometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return picometers: float, or double

    This function converts attometers into picometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-6
# ---------------------------------------------------------------------------------------------


def angstroms(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return angstroms: float, or double

    This function converts attometers into angstroms
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-8
# ---------------------------------------------------------------------------------------------


def nanometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return nanometers: float, or double

    This function converts attometers into nanometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-9
# ---------------------------------------------------------------------------------------------


def micrometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return micrometers: float, or double

    This function converts attometers into micrometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-12
# ---------------------------------------------------------------------------------------------


def millimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return millimeters: float, or double

    This function converts attometers into millimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-15
# ---------------------------------------------------------------------------------------------


def centimeters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return centimeters: float, or double

    This function converts attometers into centimeters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-16
# ---------------------------------------------------------------------------------------------


def meters(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return meters: float, or double

    This function converts attometers into meters
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-18
# ---------------------------------------------------------------------------------------------


def kilometers(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return kilometers: float, or double

    This function converts attometers into kilometers
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.0e-21
# ---------------------------------------------------------------------------------------------


def inches(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return inches: float, or double

    This function converts attometers into inches
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 3.93701e-17
# ---------------------------------------------------------------------------------------------


def yards(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return yards: float, or double

    This function converts attometers into yards
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.09361e-18
# ---------------------------------------------------------------------------------------------


def miles(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return miles: float, or double

    This function converts attometers into miles
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.21371e-22
# ---------------------------------------------------------------------------------------------


def astronomical_units(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return astronomical_units: float, or double

    This function converts attometers into astronomical units
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 6.68459e-30
# ---------------------------------------------------------------------------------------------


def light_year(distance):
    """

    :param distance: int, float or double
                     A distance in units of feet
    :return light_years: float, or double

    This function converts attometers into light_years
     """
    if isinstance(distance, list):
        distance = __first_variable_test(distance)
    __second_variable_test(distance)
    return distance * 1.057e-34
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
        sys.exit("input into attometers_to() cannot be a str")
    return
# =============================================================================================
# =============================================================================================
# eof
