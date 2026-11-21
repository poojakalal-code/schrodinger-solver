"""
test_validation.py
Validation tests: compare the numerical results with exact answers.

Run from the main project folder:
    python -m pytest -v
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from solver import solve
from potentials import box, harmonic


def test_box_energies():
    """Test 1: particle in a box, exact E_n = n^2 pi^2 / 2."""
    x, E, psi = solve(box, 0, 1, 1000, 4)
    n = np.arange(1, 5)
    E_exact = n**2 * np.pi**2 / 2
    assert np.allclose(E, E_exact, rtol=1e-4)


def test_harmonic_energies():
    """Test 2: harmonic oscillator, exact E_n = n + 1/2."""
    x, E, psi = solve(harmonic, -10, 10, 1000, 4)
    E_exact = np.arange(0, 4) + 0.5
    assert np.allclose(E, E_exact, rtol=1e-3)


def test_normalization():
    """Test 3: each wavefunction has total probability = 1."""
    x, E, psi = solve(harmonic, -10, 10, 1000, 4)
    dx = x[1] - x[0]
    for k in range(4):
        total = np.sum(psi[:, k]**2) * dx
        assert abs(total - 1) < 1e-6


def test_convergence():
    """Test 4: using more grid points gives a smaller error."""
    E_exact = np.pi**2 / 2
    x, E_coarse, psi = solve(box, 0, 1, 100, 1)
    x, E_fine, psi = solve(box, 0, 1, 1000, 1)
    error_coarse = abs(E_coarse[0] - E_exact)
    error_fine = abs(E_fine[0] - E_exact)
    assert error_fine < error_coarse