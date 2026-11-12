#!/usr/bin/env python3
"""SM-R79b: why SM-R79's plant "wrong_half_in_the_weil_matrix" (s = N // 2 in place of (N + 1) // 2 in B567's Weil matrix)
passes the E13 lock.  For odd N, N // 2 = -(N + 1) // 2 mod N, so the plant replaces T by its complex conjugate; this
seat's own code computes the spectrum both ways and compares.  Usage: weil_half_check.py OUT.json"""
import json, sys
import numpy as np


def U_of(N, s):
    z = np.exp(2j * np.pi / N)
    T = np.diag([z ** ((s * x * x) % N) for x in range(N)])
    S = np.array([[z ** ((x * y) % N) for y in range(N)] for x in range(N)]) / np.sqrt(N)
    return T @ (S @ np.linalg.inv(T) @ np.linalg.inv(S))


def spectrum(U, order=20):
    Uk = np.linalg.matrix_power(U, order)
    c = Uk[0, 0]
    assert np.linalg.norm(Uk / c - np.eye(len(U))) < 1e-6
    base = c ** (1.0 / order)
    ev = np.linalg.eigvals(U)
    idx = np.round(np.angle(ev / base) / (2 * np.pi / order)).astype(int) % order
    return sorted(np.bincount(idx, minlength=order)[np.bincount(idx, minlength=order) > 0].tolist(), reverse=True), ev


def same_multiset(a, b, tol=1e-6):
    """every point of a, counted with its neighbours within tol, occurs as often in b, and the sizes agree"""
    near = lambda x, arr: int(np.sum(np.abs(arr - x) < tol))
    return bool(len(a) == len(b) and all(near(x, a) == near(x, b) for x in a))


out = {}
for N in (15, 165):
    s_true, s_plant = (N + 1) // 2, N // 2
    mt, et = spectrum(U_of(N, s_true)); mp_, ep = spectrum(U_of(N, s_plant))
    out[str(N)] = {"s_true": s_true, "s_plant": s_plant, "s_plant_is_minus_s_true_mod_N": (s_plant + s_true) % N == 0,
                   "multiplicities_true": mt, "multiplicities_plant": mp_, "same_multiplicities": mt == mp_,
                   "plant_spectrum_is_the_conjugate": same_multiset(np.conj(et), ep),
                   "plant_spectrum_is_the_original": same_multiset(et, ep)}
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(out, indent=1))
