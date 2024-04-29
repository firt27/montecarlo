"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import montecarlo as mc

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from ..functions import canvas


def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo" in sys.modules

def test_BS_length():
    """Tests if the len returns the correct value of a BitString"""

    bs_list = []
    true_list = []
    test = True

    for i in range(10):
        bs_list.append(mc.BitString(i))
        true_list.append(len(bs_list[i]) == bs_list[i].N)
        test = False if true_list[i] != True else test

    assert test

def test_BS_onoff():
    """Tests the on and off methods of Bitstring"""

    bs = mc.BitString(13)
    bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])

    assert bs.on() == 5 and bs.off() == 8

def test_BS_int():
    """Testing the int method of BitString"""

    bs = mc.BitString(13)
    bs.set_config([0,1,1,0,0,1,0,0,1,0,1,0,0])

    assert bs.int() == 3220

def test_BS_setintconf():
    """Testing the set_int_config method of BitString"""

    bs = mc.BitString(20)
    bs.set_int_config(3221)

    for i in range(1000):
        bs.set_int_config(i)
        assert(bs.int() == i)

def test_BS_eq():
    """Testing the equality operator for BitString"""

    bs1 = mc.BitString(13)
    bs1.set_config([0,1,1,0,0,1,0,1,1,0,1,0,0])
    bs2 = mc.BitString(13)
    bs2.set_int_config(3252)
    
    assert(bs1 == bs2)
    bs2.flip_site(5)
    assert(bs1 != bs2)

def test_IH_cav():
    """Test for the compute_average_values method of IsingHamiltonian"""

    N = 6
    Jval = 2.0
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    G.add_edges_from([(i, (i+1)% G.number_of_nodes() ) for i in range(N)])
    for e in G.edges:
        G.edges[e]['weight'] = Jval

    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    mus = np.zeros(len(G.nodes()))

    conf = mc.BitString(N)
    ham = mc.IsingHamiltonian(J, mus)

    E, M, HC, MS = ham.compute_average_values(1)

    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))



    