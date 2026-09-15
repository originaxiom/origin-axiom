#!/usr/bin/env python3
"""B511/D3.3 — wild-register accessibility under the stationary measure.
Wild fields (S4..S11) live at irreducible kappa!=2; classical kappa=2 is the abelian torsion factory.
The measure's mass near kappa!=2 = how often a typical history can birth wild arithmetic.

NUMERICAL NOTE (2026-09-09).  The walk lives in SU(2): haar() draws SU(2) and every step is a
product of SU(2) elements, so A and B are unitary for the whole run in exact arithmetic.  In
floating point they are not.  The step (A, B) -> (AB, A) grows word length like Fibonacci and the
squaring branches double it, so a rounding perturbation of size eps is carried by a word of
length L and a generic SL(2,C) perturbation of a unitary is LOXODROMIC -- its norm grows like
exp(c*L).  Rescaling by sqrt(|det|) every 20 steps, as this file used to do, does not help: a
loxodromic element already has det 1.  The run therefore overflowed to NaN around step 70 and
accessibility() returned classical = 0.0 -- a pure arithmetic failure, with no bearing on the
claim.  The fix is to project back onto SU(2) after every step (read off the quaternion part and
normalise -- exact for a true SU(2) matrix, so it changes nothing but the rounding error).
Control: against the old code the two agree to 5e-13 at 20 steps, and diverge to 1.5e-8 at 40 and
4.4e-4 at 60 -- the old error doubling with each squaring, exactly as predicted."""
import numpy as np


def to_su2(M):
    """project a nearly-SU(2) matrix back onto SU(2): take the quaternion part
    (a + ib, c + id; -c + id, a - ib) and normalise.  A no-op, to rounding, on a
    true SU(2) matrix; it removes the drift that otherwise compounds."""
    a = (M[:, 0, 0].real + M[:, 1, 1].real) / 2
    b = (M[:, 0, 0].imag - M[:, 1, 1].imag) / 2
    c = (M[:, 0, 1].real - M[:, 1, 0].real) / 2
    d = (M[:, 0, 1].imag + M[:, 1, 0].imag) / 2
    q = np.stack([a, b, c, d], 1)
    q /= np.linalg.norm(q, axis=1, keepdims=True)
    a, b, c, d = q.T
    out = np.empty_like(M)
    out[:, 0, 0] = a + 1j*b; out[:, 0, 1] = c + 1j*d
    out[:, 1, 0] = -c + 1j*d; out[:, 1, 1] = a - 1j*b
    return out


def haar(n, rng):
    q = rng.normal(size=(n, 4)); q /= np.linalg.norm(q, axis=1, keepdims=True)
    a, b, c, d = q.T
    M = np.zeros((n, 2, 2), complex)
    M[:, 0, 0] = a + 1j*b; M[:, 0, 1] = c + 1j*d; M[:, 1, 0] = -c + 1j*d; M[:, 1, 1] = a - 1j*b
    return M


def run(seed, n, steps, mix):
    rng = np.random.default_rng(seed); A, B = haar(n, rng), haar(n, rng)
    for t in range(steps):
        r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
        AB = A @ B
        Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A))
        An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
        A, B = to_su2(A), to_su2(B)      # every step: see the numerical note
    x = np.real(np.trace(A, axis1=1, axis2=2)); y = np.real(np.trace(B, axis1=1, axis2=2))
    z = np.real(np.trace(A @ B, axis1=1, axis2=2))
    return x*x + y*y + z*z - x*y*z - 2


def accessibility(seed=11, n=4000, steps=3000, mix=(0.10, 0.10)):
    k = run(seed, n, steps, mix)
    classical = float(np.mean(np.abs(k - 2) < 0.05))
    wild = float(np.mean((np.abs(k - 2) > 0.5) & (k >= -2) & (k <= 2)))
    return classical, wild


if __name__ == "__main__":
    for mix, name in [((0.10, 0.10), "M10/D10/F80"), ((0.20, 0.0), "M20/F80"), ((0.0, 0.20), "D20/F80")]:
        c, w = accessibility(mix=mix)
        print("%-14s classical=%.3f wild-accessible=%.3f" % (name, c, w))
