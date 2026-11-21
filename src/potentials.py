"""
potentials.py
Potential energy functions V(x) to use with the solver.
Each function takes an array x and returns V at each point.
"""

import numpy as np


def box(x):
    """Infinite square well: V = 0 inside. The walls come from psi = 0 at the ends."""
    return np.zeros(len(x))


def harmonic(x, w=1.0):
    """Harmonic oscillator: V = (1/2) w^2 x^2."""
    return 0.5 * w**2 * x**2


def finite_well(x, V0=50.0, a=1.0):
    """Finite square well: V = 0 for |x| < a, and V = V0 outside."""
    return np.where(abs(x) < a, 0.0, V0)


def double_well(x, V0=10.0, a=1.0):
    """Double well: two dips at x = -a and x = +a, with a bump of height V0 at x = 0."""
    return V0 * (x**2 - a**2)**2 / a**4