#!/usr/bin/env python3
"""W5 (main): the frames' own module at the common point.  The four is H -> g H g^* on Hermitian 2 x 2 matrices in the
basis (1, i, j, k) = (I, sigma_z-type, ...) -- B1492's f4 with the basis (E11, E22, (E12 + E21), i(E12 - E21)) rotated to
(I, sigma_3, sigma_1, sigma_2); at the quaternion point g = i, j (the unit quaternions as SU(2) matrices) it is
diagonal: Ad(i) = (1, +1, -1, -1), Ad(j) = (1, -1, +1, -1), Ad(-1) = the identity.  So the four = the trivial line (+)
the three parity lines, the A4 triplet of W4 on the last three.  Exact (sympy).  Writes w5.json."""
import json, pathlib
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
I2 = sp.eye(2); s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
qi = sp.I * s3; qj = sp.I * s2; qk = sp.I * s1            # i, j, k as SU(2) matrices (i^2 = j^2 = k^2 = -1, ij = k)
assert qi * qj == qk and qi**2 == -I2 and qj**2 == -I2 and qk**2 == -I2
basis = [I2, s3, s2, s1]                                   # the Hermitian basis (1, i, j, k) up to the factor i: i = i s3, j = i s2, k = i s1
def four(g):
    cols = []
    for H in basis:
        Hp = g * H * g.H
        cols.append([sp.simplify((Hp * B).trace() / 2) for B in basis])   # coordinates in the orthonormal basis (tr(B B)/2 = 1)
    return sp.Matrix(cols).T
out = {}
for name, g in (("i", qi), ("j", qj), ("k", qk), ("-1", -I2)):
    M = four(g); out[name] = [[int(e) for e in M.row(r)] for r in range(4)]
    assert M.is_diagonal(), (name, M)
out["trivial_line_plus_triplet"] = (out["i"][0][0] == 1 and out["j"][0][0] == 1 and
                                    [out["i"][r][r] for r in range(1, 4)] == [1, -1, -1] and [out["j"][r][r] for r in range(1, 4)] == [-1, 1, -1])
out["note"] = "Ad(i) = diag(1, +1, -1, -1), Ad(j) = diag(1, -1, +1, -1) on (1, i, j, k): the trivial line and the three sign characters of V4 = the parity lines; the 3-cycle of any odd-trace thread permutes the last three (W4's triplet)."
json.dump(out, open(HERE / "w5.json", "w"), indent=1); print(json.dumps(out))
