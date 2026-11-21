"""
convergence_study.py
Checks how the error of the ground-state energy changes with the number of grid points N.
Theory says error ~ dx^2, so on a log-log plot the line should have slope 2.

Run from the main project folder:
    python examples/convergence_study.py
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 13

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from solver import solve
from potentials import box

os.makedirs("figures", exist_ok=True)

E_exact = np.pi**2 / 2                  # exact ground-state energy of the box (L = 1)
N_list = [25, 50, 100, 200, 400, 800]
dx_list = []
error_list = []

for N in N_list:
    x, E, psi = solve(box, 0, 1, N, 1)
    dx = 1 / (N + 1)
    error = abs(E[0] - E_exact)
    dx_list.append(dx)
    error_list.append(error)
    print(f"N = {N:4d}   dx = {dx:.5f}   error = {error:.3e}")

slope = np.polyfit(np.log(dx_list), np.log(error_list), 1)[0]    # slope of the straight line
print("slope of log(error) vs log(dx) =", round(slope, 3))

dx_arr = np.array(dx_list)
plt.figure(figsize=(6, 4.5))
plt.loglog(dx_list, error_list, "o-", label=f"numerical error (slope = {slope:.2f})")
plt.loglog(dx_list, error_list[0] * (dx_arr / dx_arr[0])**2, "--", color="gray", label="reference: error ∝ dx²")
plt.xlabel("grid spacing dx")
plt.minorticks_off()
plt.xticks(dx_arr, [f"{d:.4f}" for d in dx_arr], rotation=30)
plt.ylabel("|E_numerical - E_exact|")
plt.title("Convergence of the ground-state energy (box)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/convergence.png", dpi=300)
plt.show()