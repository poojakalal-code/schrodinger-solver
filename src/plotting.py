"""
plotting.py
Functions to draw the results of the solver.
"""

import matplotlib.pyplot as plt


def plot_states(x, V, E, psi, title, filename=None):
    """Draw the potential V(x) and each wavefunction, shifted up to its energy level."""
    scale = 0.4 * (E[-1] - E[0]) / len(E)        # height of each wavefunction drawing
    plt.figure(figsize=(7, 5))
    plt.plot(x, V, color="black", linewidth=2, label="V(x)")
    for k in range(len(E)):
        plt.axhline(E[k], color="gray", linestyle="--", linewidth=0.8)
        wave = psi[:, k] / max(abs(psi[:, k]))     # make the peak height = 1
        plt.plot(x, E[k] + scale * wave, label=f"E{k} = {E[k]:.3f}")
    plt.ylim(min(V) - 0.1 * E[-1], 1.3 * E[-1])
    plt.xlabel("x")
    plt.ylabel("Energy")
    plt.title(title)
    plt.legend()
    if filename:
        plt.savefig(filename, dpi=300)           # save a high-quality picture
    plt.show()