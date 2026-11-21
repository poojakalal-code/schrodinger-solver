"""
plotting.py
Functions to draw the results of the solver.
"""

import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 13


def plot_states(x, V, E, psi, title, filename=None, walls=False, n_start=0):
    """Draw the potential V(x) and each wavefunction, shifted up to its energy level.
    walls=True draws hard walls at both ends (for the box).
    n_start is the number of the first state (0 for most potentials, 1 for the box)."""
    scale = 0.4 * (E[-1] - E[0]) / len(E)        # height of each wavefunction drawing
    plt.figure(figsize=(7, 4.5))
    plt.plot(x, V, color="black", linewidth=2, label="V(x)")
    if walls:
        plt.axvline(x[0], color="black", linewidth=2)     # left wall
        plt.axvline(x[-1], color="black", linewidth=2)    # right wall
    for k in range(len(E)):
        plt.axhline(E[k], color="gray", linestyle="--", linewidth=0.8)
        wave = psi[:, k] / max(abs(psi[:, k]))     # make the peak height = 1
        plt.plot(x, E[k] + scale * wave, label=f"E{k + n_start} = {E[k]:.3f}")
    plt.ylim(min(V) - 0.1 * E[-1], 1.3 * E[-1])
    plt.xlabel("x")
    plt.ylabel("Energy")
    plt.title(title)
    plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))   # legend outside, on the right
    plt.tight_layout()                                       # make room for the legend
    if filename:
        plt.savefig(filename, dpi=300)           # save a high-quality picture
    plt.show()