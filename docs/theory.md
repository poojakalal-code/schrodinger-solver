# Theory and Numerical Method

## 1. The Schrödinger equation

The 1D time-independent Schrödinger equation is

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)$$

To keep the numbers simple we use units where ħ = 1 and m = 1:

$$-\frac{1}{2}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)$$

- V(x) is the potential energy.
- E is the energy of the particle.
- ψ(x) is the wavefunction. |ψ(x)|² is the probability density.

Only certain values of E give a wavefunction that goes to zero far away.
These are the allowed energy levels.

## 2. Finite-difference approximation

We divide the region from x_min to x_max into N points with equal spacing dx:

$$x_i = x_{min} + i\,dx, \qquad i = 1, 2, \dots, N$$

From the Taylor series of ψ(x + dx) and ψ(x − dx), the second derivative is

$$\frac{d^2\psi}{dx^2} \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{dx^2}$$

The error of this formula is proportional to dx².
So if we use twice as many points, the error becomes about four times smaller.

## 3. Matrix form

Putting the formula into the Schrödinger equation gives, for each point i:

$$-\frac{1}{2dx^2}\psi_{i-1} + \left(\frac{1}{dx^2} + V_i\right)\psi_i - \frac{1}{2dx^2}\psi_{i+1} = E\psi_i$$

Writing this for all N points gives a matrix equation

$$H\psi = E\psi$$

H is an N × N tridiagonal matrix:

- main diagonal: 1/dx² + V_i
- the two diagonals next to it: −1/(2dx²)
- all other entries: 0

H is real and symmetric, so all its eigenvalues are real (as energies must be).
We use `numpy.linalg.eigh`, which is made for symmetric matrices.

- Eigenvalues of H = energy levels E
- Eigenvectors of H = wavefunctions ψ at the grid points

## 4. Boundary conditions

We set ψ = 0 at x_min and x_max. This is the same as putting infinite walls
at both ends. For the box this is exact. For the other potentials we choose
x_min and x_max far enough away that the wavefunction is already almost zero there.

## 5. Normalization

The total probability must be 1:

$$\int |\psi(x)|^2 dx = 1$$

numpy gives eigenvectors with sum of |ψ_i|² = 1, so we divide by √dx
to make the integral (sum × dx) equal to 1.

## 6. Potentials and exact answers

| Potential | V(x) | Exact energies |
|---|---|---|
| Infinite square well (0 < x < L) | 0 inside | E_n = n²π² / (2L²), n = 1, 2, 3, ... |
| Harmonic oscillator | ½ ω² x² | E_n = (n + ½) ω, n = 0, 1, 2, ... |
| Finite square well | 0 for \|x\| < a, V0 outside | no simple formula |
| Double well | V0 (x² − a²)² / a⁴ | no simple formula |

The first two are used to check the code. The last two show physics that
needs a numerical method: leaking into the walls and tunneling splitting.

## 7. How to add a new potential

Write a function that takes an array x and returns V at each point, then pass it to `solve`:

    def my_potential(x):
        return 0.1 * x**4

    x, E, psi = solve(my_potential, -6, 6, N=1000, n_states=4)