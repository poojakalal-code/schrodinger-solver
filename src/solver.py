"""
solver.py
Solves the 1D Schrodinger equation:  -(1/2) psi'' + V psi = E psi
Units: hbar = m = 1
"""

import numpy as np


def make_grid(x_min, x_max, N):
    """Make N points between x_min and x_max (the two ends are not included)."""
    x = np.linspace(x_min, x_max, N + 2)   # points including both ends
    x = x[1:-1]                            # remove the ends (psi = 0 there)
    dx = x[1] - x[0]                       # spacing between points
    return x, dx


def make_hamiltonian(x, dx, V):
    """Build the matrix H using the finite-difference formula."""
    N = len(x)
    H = np.zeros((N, N))
    for i in range(N):
        H[i, i] = 1 / dx**2 + V[i]             # main diagonal
        if i > 0:
            H[i, i - 1] = -1 / (2 * dx**2)     # left neighbour
        if i < N - 1:
            H[i, i + 1] = -1 / (2 * dx**2)     # right neighbour
    return H


def solve(V_func, x_min, x_max, N=1000, n_states=5):
    """Return the grid x, the lowest energies E, and the wavefunctions psi.
    psi[:, k] is the wavefunction of state k (k = 0 is the ground state)."""
    x, dx = make_grid(x_min, x_max, N)
    V = V_func(x)
    H = make_hamiltonian(x, dx, V)
    E, psi = np.linalg.eigh(H)     # eigenvalues = energies, eigenvectors = wavefunctions
    E = E[:n_states]               # keep only the lowest few
    psi = psi[:, :n_states]
    psi = psi / np.sqrt(dx)        # normalize: sum of |psi|^2 * dx = 1
    return x, E, psi