"""The peripheral certificate for lambda = a(bABaaBAb)a^-1 = "abABaaBAbA"
(SL(2) level; seconds). Checks: the relator holds at the geometric parabolic
rep; lambda commutes with the meridian a; exponent sum 0; the image is
-[[1, 2 sqrt3 i],[0,1]] (off-diagonal = the banked cusp shape); the two
words bABaaBAb and abABaaBAbA are group-equal (same image)."""
import numpy as np
from scipy.optimize import least_squares

def rep(c):
    a = np.array([[1, 1], [0, 1]], dtype=complex)
    b = np.array([[1, 0], [c, 1]], dtype=complex)
    return a, b

def word(w, a, b):
    D = {'a': a, 'b': b, 'A': np.linalg.inv(a), 'B': np.linalg.inv(b)}
    M = np.eye(2, dtype=complex)
    for ch in w:
        M = M @ D[ch]
    return M

def F(x):
    a, b = rep(x[0] + 1j * x[1])
    R = word("abABaBAbaB", a, b) - np.eye(2)
    return [R[0, 0].real, R[0, 0].imag, R[0, 1].real, R[0, 1].imag,
            R[1, 0].real, R[1, 0].imag]

r = least_squares(F, (0.5, 0.9), ftol=1e-15, xtol=1e-15, gtol=1e-15)
c = r.x[0] + 1j * r.x[1]
assert np.linalg.norm(r.fun) < 1e-10
a, b = rep(c)
LAM = "abABaaBAbA"
L = word(LAM, a, b)
Lc = word("bABaaBAb", a, b)
assert np.abs(a @ L - L @ a).max() < 1e-9                  # commutes with mu
es = sum(+1 if ch in "ab" else -1 for ch in LAM)
assert es == 0                                             # zero-framed (null-homologous)
assert np.abs(L - Lc).max() < 1e-9                         # group-equal words
assert abs(L[0, 0] + 1) < 1e-9 and abs(L[1, 1] + 1) < 1e-9
assert abs(abs(L[0, 1].imag) - 2 * 3 ** 0.5) < 1e-8        # the banked cusp shape
print(f"peripheral certificate PASS: c = {c:.6f}; lambda image upper = {L[0,1]:.6f}")
