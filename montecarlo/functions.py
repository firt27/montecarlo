"""Provide the primary functions."""

import networkx as nx
import matplotlib.pyplot as plt
import random

from .BitString import *



def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def energy(bs: BitString, J):
    """Compute energy of configuration, `bs`

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """

    # translating 0 and 1 to -1 and 1
    def z1_to_n1(bit1, bit2):
        if bit1 == bit2:
            return 1
        else:
            return -1
            
    # array_J = nx.adjacency_matrix(G).todense()
    nrg = 0
    for i in range(len(J)):
        for j in range(i,len(J[i])):
            nrg += J[i][j][-1] * z1_to_n1(bs.config[i], bs.config[j])

    return nrg


def compute_average_values(bs:BitString, J, T: float):
    """
    Compute the average value of Energy, Magnetization, 
    Heat Capacity, and Magnetic Susceptibility 

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    T    : float
        temperature of the system
    Returns
    -------
    energy  : float
    magnetization  : float
    heat capacity  : float
    magnetic susceptibility  : float
    """

    # k = 1.38064852 * math.pow(10,-23)
    k = 1
    beta = 1/(k * T)
    
    ''' Probability of any bs '''
    def prob(bs):
        return math.exp(-beta * energy(bs, J))
    
    Z = 0
    E = 0
    M = 0
    E2 = 0
    M2 = 0

    ''' Defining magnetism: M(bs) = N_up(bs - N_down(bs)'''
    def mag(bs):
        x = 0
        for i in bs.config:
            x += 2*i - 1
        return x
    
    for i in range(2 ** bs.N):
        bs.set_int_config(i)
        Z += math.exp(-beta * energy(bs, J))
        E += prob(bs) * energy(bs, J)
        M += prob(bs) * mag(bs)
        E2 += prob(bs) * energy(bs, J) ** 2
        M2 += prob(bs) * mag(bs)**2

    E /= Z
    M /= Z
    E2 /= Z
    M2 /= Z

    HC = (E2-E**2) / (T**2)
    MS = (M2-M**2) / T

    return E, M, HC, MS




if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
