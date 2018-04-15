# Import modules here
import sys
import os
import pandas as pd
import numpy as np
# =============================================================================================
# =============================================================================================
# Date:      March 17, 2018
# Purpose:   This module contains all functions necessary to implement discretized
#            energy spectrum for the HERMESIII Gamma Ray Simulator

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2017, Jon Webb Inc."
__version__ = "1.0"
# =============================================================================================
# =============================================================================================


def discretized_spectrum(spec_name):
    """

    :param spec_name: str
                      A string representing the measured spectrum to be propduced. \
                      Options are 'Ballard', 'Adapo', or 'RHSC'.
    :return en, pd: float tuple
                    The energy bounds (en) in units of MeV and the probability of photon \
                    emission within those bounds.

    This function reproduces the photon energy spectrums produced by the HERMESIII \
    machine as measured by 'Ballard', or 'Adapo', or the 'RHSC' experiment.
    """
    file_name = 'data/nuclear/spectra/HermesIII.csv'
    verify_file(file_name)
    if spec_name.upper() == 'BALLARD':
        energy = 'Ballard Energy (MeV)'
        prob = 'Ballard P(E)'
    elif spec_name.upper() == 'ADAPO':
        energy = 'Adapo Energy (MeV)'
        prob = 'Adapo P(E)'
    elif spec_name.upper() == 'RHSC':
        energy = 'RHSC Energy (MeV)'
        prob = 'RHSC P(E)'
    else:
        sys.exit("User did not enter 'spec_name' correctly")
    data = pd.read_csv(file_name, usecols=[energy, prob], na_values=[''])
    data = data.dropna(axis=0, how='any')
    en = np.array(data[energy], np.float32)
    pb = np.array(data[prob], np.float32)
    return en, pb
# ---------------------------------------------------------------------------------------------


def verify_file(file_name):
    """
    :param file_name : char string
                       the pathlink to a file
    :return:

    This function tests a file-directory-path to ensure that
    the file actually exists
    """
    if os.path.isfile(file_name):
        return
    sys.exit('{}{}{}'.format('FATAL ERROR: ', file_name, ' does not exist'))
# ---------------------------------------------------------------------------------------------


def discrete_plot_format(x, y):
    """

    :param x: float
              List or array of x values (i.e. energy), each representing an energy bound \
              within which a probability of neutron emission exists
    :param y: float
              List or array of y values (i.e. probability) corresponding to the \
              probability of neutron emission between energy bounds.  This array \
              typically starts with 0.
    :return new_x, new_y: tuple of floats
                          A new list of x and y values corresponding to the vertices \
                          of a discrete energy spectrum

    This function transforms a discrete energy spectrum from an MCNP format where the \
    energy array starts with 0. and the probabilities exists between energy bounds to \
    a format where the probability at an energy bound is returned.
    """
    new_x = []
    for i in range(len(x)):
        new_x.append(x[i])
        new_x.append(x[i])
    new_x = np.array(new_x[:-1], np.dtype(np.float32))
    new_y = []
    for i in range(len(y)):
        new_y.append(y[i])
        new_y.append(y[i])
    new_y = np.array(new_y[1:], np.dtype(np.float32))
    return new_x, new_y
# ---------------------------------------------------------------------------------------------
# eof
