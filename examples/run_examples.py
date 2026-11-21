"""
run_examples.py
Solves the Schrodinger equation for four potentials,
prints the energies, and saves the figures in the 'figures' folder.

Run from the main project folder:
    python examples/run_examples.py
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from solver import solve
from potentials import box, harmonic, finite_well, double_well
from plotting import plot_states

os.makedirs("figures", exist_ok=True)


# 1. Particle in a box (from x = 0 to x = 1)
x, E, psi = solve(box, 0, 1, 1000, 4)
n = np.arange(1, 5)
E_exact = n**2 * np.pi**2 / 2
print("Particle in a box")
print("  numerical:", E)
print("  exact:    ", E_exact)
plot_states(x, box(x), E, psi, "Particle in a box", "figures/box.png", walls=True, n_start=1)


# 2. Harmonic oscillator
x, E, psi = solve(harmonic, -5, 5, 1000, 4)
n = np.arange(0, 4)
E_exact = n + 0.5
print("Harmonic oscillator")
print("  numerical:", E)
print("  exact:    ", E_exact)
plot_states(x, harmonic(x), E, psi, "Harmonic oscillator", "figures/harmonic.png")


# 3. Finite square well (no simple exact formula)
x, E, psi = solve(finite_well, -3, 3, 1000, 4)
print("Finite square well")
print("  numerical:", E)
plot_states(x, finite_well(x), E, psi, "Finite square well", "figures/finite_well.png")


# 4. Double well (shows tunneling splitting)
x, E, psi = solve(double_well, -2.5, 2.5, 1000, 4)
print("Double well")
print("  numerical:", E)
print("  splitting E1 - E0 =", E[1] - E[0])
plot_states(x, double_well(x), E, psi, "Double well", "figures/double_well.png")