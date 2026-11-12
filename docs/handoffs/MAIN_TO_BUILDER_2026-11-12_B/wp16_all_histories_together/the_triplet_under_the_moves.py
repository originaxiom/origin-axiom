#!/usr/bin/env python3
"""WP-1.6: where the record's own triplet stands in the law of the rates.

The record's triplet T is a three-dimensional module on which the two moves act by the matrices of B1610 (as B1866 reads
them: a group of order 96, scalars of order 4, S_T^4 = -1, so a module of the double cover and not of SL(2, Z)).  The law
of the_weaves_zeta.py is proved for sectors of SL(2, Z).  T is not one, so nothing is assumed: the averaged move
(T_L + T_R) / 2 is diagonalised as it stands.  Also computed: the same for the three theta constants in their classical
transformation (theta_2, theta_3, theta_4 under tau -> tau + 1 and tau -> -1/tau), with R the conjugate of L^-1 by S;
and for T with the inverse moves added.
What is NOT done: no value of the modulus is read, nothing is compared with a measured number, and no meaning is given
to the rate."""
import cmath, importlib.util, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location("hands", ROOT / "frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py")
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
TB = H.PIECES["T"]; TL, TR = TB.conj().T @ H.W.ML @ TB, TB.conj().T @ H.W.MR @ TB
I3 = np.eye(3)
out = {}
def show(name, L, R):
    assert np.allclose(L.conj().T @ L, I3, atol=1e-9) and np.allclose(R.conj().T @ R, I3, atol=1e-9), "not unitary"
    ev = np.linalg.eigvals((L + R) / 2); ev4 = np.linalg.eigvals((L + R + np.linalg.inv(L) + np.linalg.inv(R)) / 4)
    S = L @ np.linalg.inv(R) @ L
    row = {"eigenvalues of the averaged move": sorted(([round(x.real, 9), round(x.imag, 9)] for x in ev), key=lambda z: -abs(complex(*z))),
           "their moduli": sorted((round(abs(x), 9) for x in ev), reverse=True), "rate": round(float(max(abs(ev))), 9),
           "with the inverse moves": sorted((round(float(x.real), 9) for x in ev4), key=abs, reverse=True),
           "braid relation holds": bool(np.allclose(S, np.linalg.inv(R) @ L @ np.linalg.inv(R), atol=1e-9)),
           "S^2, S^4": [("scalar %s" % np.round(np.linalg.matrix_power(S, k)[0, 0], 6)) if np.allclose(np.linalg.matrix_power(S, k), np.linalg.matrix_power(S, k)[0, 0] * I3, atol=1e-9) else "not a scalar" for k in (2, 4)]}
    out[name] = row
    print("%-44s moduli %s   eigenvalues %s" % (name, row["their moduli"], row["eigenvalues of the averaged move"]))
    print("%-44s with the inverse moves: %s; braid relation: %s; S^2, S^4: %s" % ("", row["with the inverse moves"], row["braid relation holds"], row["S^2, S^4"]))
show("the record's triplet T (B1610's matrices)", TL, TR)
z = cmath.exp(1j * math.pi / 4)
thL = np.array([[z, 0, 0], [0, 0, 1], [0, 1, 0]]); thS = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex)
thR = thS @ np.linalg.inv(thL) @ np.linalg.inv(thS)
show("the three theta constants, classical", thL, thR)
show("the same with the other lift of R (-R)", thL, -thR)
show("the record's triplet with -R", TL, -TR)
print("1/sqrt 2 = %.9f; 1/2; sqrt 3 / 2 = %.9f" % (1 / math.sqrt(2), math.sqrt(3) / 2))
json.dump(out, open(HERE / "the_triplet_under_the_moves.json", "w"), indent=1)
