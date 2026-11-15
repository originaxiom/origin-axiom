#!/usr/bin/env python3
"""W-A1, part 1: the gauge structure from level 5's Weil representation. Pure algebra; no frame, no data.

    python3 -I -u wa1_weil.py

rho: the Weil representation of SL(2, F_5) on C^5 = functions on F_5, psi(x) = exp(2 pi i x / 5). Candidates are
rho(T) = diag(psi(k x^2)) and rho(S) = c F, F_xy = psi(s x y) / sqrt 5, with k in F_5*, s = +-1 and c in {1, -1, i, -i}.
A candidate is kept when the assignment along the Cayley graph of SL(2, F_5) (generators S = [[0, -1], [1, 0]],
T = [[1, 1], [0, 1]]) is consistent at all 120 elements, so that it is a homomorphism. P = rho(-I).

EXPECTATIONS (card W-A1, committed before this script):
  D1  some candidate is a faithful representation (120 distinct matrices); P = rho(S)^2 is the parity f(x) -> f(-x);
      eigenvalue +1 three times and -1 twice.
  D2  the P-eigenspaces are irreducible (character norm 1 each); the commutant of rho has dimension 2 (spanned by I, P).
  D3  the commutant's traceless element, scaled to 3 on the -1 eigenspace, is (I - 5P)/2: -2 on the 3, 3 on the 2.
  D4  the centraliser of P in su(5) has real dimension 12; exp(2 pi i Y), Y = 6Y / 6, is diag(wbar x3, -1 x2) with
      determinant 1, central in SU(3) x SU(2).
  D5  on Lambda^even(C^5) the (6Y, colour, weak) content is one generation in SIXY's values: Q (1; 3, 2), u (-4; 3bar,
      1), e (6; 1, 1), d (2; 3bar, 1), L (-3; 1, 2), and (0; 1, 1).
  D6  over those 16 states: sum Y = 0, sum Y^3 = 0, SU(3)^2 Y = 0, SU(2)^2 Y = 0.
  D7  Lambda^1's weak doublet has 6Y = 3 (SIXY's H).
  Plant: the same steps with the projector on rho(T)'s 1-dimensional eigenspace in place of P's do not give D5's
  content.
"""
import itertools
from fractions import Fraction as Fr

import numpy as np

p = 5
w5 = np.exp(2j * np.pi / p)
X = np.arange(p)


def say(*a):
    print(*a, flush=True)


def sl2_elements():
    return [(a, b, c, d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a * d - b * c) % p == 1]


def mul(g, h):
    a, b, c, d = g
    e, f, g2, h2 = h
    return ((a * e + b * g2) % p, (a * f + b * h2) % p, (c * e + d * g2) % p, (c * f + d * h2) % p)


GS, GT, I2 = (0, p - 1, 1, 0), (1, 1, 0, 1), (1, 0, 0, 1)


def try_rep(rS, rT):
    rho = {I2: np.eye(p, dtype=complex)}
    todo = [I2]
    while todo:
        g = todo.pop()
        for gen, rg in ((GS, rS), (GT, rT)):
            h = mul(g, gen)
            M = rho[g] @ rg
            if h in rho:
                if np.max(np.abs(rho[h] - M)) > 1e-9:
                    return None
            else:
                rho[h] = M
                todo.append(h)
    return rho if len(rho) == 120 else None


def find_reps():
    out = []
    for k in range(1, p):
        rT = np.diag(w5 ** ((k * X * X) % p))
        for s in (1, -1):
            F = w5 ** ((s * np.outer(X, X)) % p) / np.sqrt(p)
            for c in (1, -1, 1j, -1j):
                rho = try_rep(c * F, rT)
                if rho is not None:
                    out.append(((k, s, c), rho))
    return out


def nullspace(A, tol=1e-9):
    u, sv, vh = np.linalg.svd(A)
    r = int(np.sum(sv > tol))
    return vh[r:].conj().T


def commutant(mats):
    rows = [np.kron(np.eye(p), M.T) - np.kron(M, np.eye(p)) for M in mats]
    return nullspace(np.vstack(rows))


def content(nc, nw, y_c, y_w):
    """the (6Y, colour, weak) multiset of Lambda^even of C^nc + C^nw with 6Y = y_c on the first, y_w on the second"""
    col = {0: "1", 1: "3", 2: "3bar", 3: "1"}
    wk = {0: "1", 1: "2", 2: "1"}
    out = {}
    for k in (0, 2, 4):
        for n3 in range(0, min(k, nc) + 1):
            n2 = k - n3
            if n2 < 0 or n2 > nw:
                continue
            key = (n3 * y_c + n2 * y_w, col.get(n3, "?") if nc == 3 else "n%d" % n3, wk.get(n2, "?") if nw == 2 else "m%d" % n2)
            out[key] = out.get(key, 0) + int(round(np.prod([1])) * _binom(nc, n3) * _binom(nw, n2))
    return out


def _binom(n, k):
    from math import comb
    return comb(n, k)


def main():
    reps = find_reps()
    say("D1: candidates that are representations of SL(2, F_5): %d (parameters (k, s, c)): %s" % (len(reps), [r[0] for r in reps]))
    if not reps:
        say("D1 fails")
        return
    (k, s, c), rho = reps[0]
    mats = list(rho.values())
    faithful = len({tuple(np.round(M, 8).ravel()) for M in mats}) == 120
    P = rho[(p - 1, 0, 0, p - 1)]
    par = np.zeros((p, p))
    for x in range(p):
        par[(-x) % p, x] = 1
    ev = np.round(np.linalg.eigvals(P).real, 9)
    d1 = faithful and np.max(np.abs(P - par)) < 1e-9 and np.max(np.abs(rho[GS] @ rho[GS] - P)) < 1e-9 and \
        sorted(ev.tolist()) == [-1, -1, 1, 1, 1]
    say("D1 holds:", d1, "| using (k, s, c) =", (k, s, c), "| faithful:", faithful, "| P eigenvalues:", sorted(ev.tolist()))

    Ep, Em = nullspace(P - np.eye(p)), nullspace(P + np.eye(p))
    def cnorm(V):
        Q = V.conj().T
        return sum(abs(np.trace(Q @ M @ V)) ** 2 for M in mats) / 120
    C = commutant([rho[GS], rho[GT]])
    in_span = all(np.linalg.matrix_rank(np.column_stack([np.eye(p).ravel(), P.ravel(), C[:, j]]), tol=1e-8) == 2 for j in range(C.shape[1]))
    d2 = abs(cnorm(Ep) - 1) < 1e-9 and abs(cnorm(Em) - 1) < 1e-9 and C.shape[1] == 2 and in_span
    say("D2 holds:", d2, "| character norms %.6f, %.6f | commutant dimension %d, spanned by I and P: %s" % (
        cnorm(Ep), cnorm(Em), C.shape[1], in_span))

    Y6 = (np.eye(p) - 5 * P) / 2
    yev = sorted(np.round(np.linalg.eigvals(Y6).real, 9).tolist())
    d3 = abs(np.trace(Y6)) < 1e-12 and yev == [-2, -2, -2, 3, 3] and all(np.max(np.abs(Y6 @ M - M @ Y6)) < 1e-9 for M in mats)
    say("D3 holds:", d3, "| 6Y = (I - 5P)/2 eigenvalues", yev)

    basis = []
    for i in range(p):
        for j in range(p):
            for herm in (True, False):
                A = np.zeros((p, p), dtype=complex)
                if i == j:
                    if not herm:
                        continue
                    A[i, i] = 1j
                elif i < j:
                    if herm:
                        A[i, j], A[j, i] = 1, -1
                    else:
                        A[i, j], A[j, i] = 1j, 1j
                else:
                    continue
                basis.append(A)
    B = np.array([b.ravel() for b in basis]).T
    comm = np.array([(b @ P - P @ b).ravel() for b in basis]).T
    trace_row = np.array([[np.trace(b) for b in basis]])
    Mreal = np.vstack([np.real(comm), np.imag(comm), np.real(trace_row), np.imag(trace_row)])
    dim = Mreal.shape[1] - np.linalg.matrix_rank(Mreal, tol=1e-9)
    from scipy.linalg import expm
    g0 = expm(2j * np.pi * Y6 / 6)
    w = np.exp(2j * np.pi / 3)
    target = Ep @ Ep.conj().T * np.conj(w) + Em @ Em.conj().T * (-1)
    d4 = dim == 12 and np.max(np.abs(g0 - target)) < 1e-9 and abs(np.linalg.det(g0) - 1) < 1e-9
    say("D4 holds:", d4, "| centraliser of P in su(5): real dimension %d | exp(2 pi i Y) = diag(wbar x3, -1 x2): %s | det %.6f" % (
        dim, np.max(np.abs(g0 - target)) < 1e-9, abs(np.linalg.det(g0))))

    ct = content(3, 2, -2, 3)
    want = {(1, "3", "2"): 6, (-4, "3bar", "1"): 3, (6, "1", "1"): 1, (2, "3bar", "1"): 3, (-3, "1", "2"): 2, (0, "1", "1"): 1}
    d5 = ct == want
    say("D5 holds:", d5, "| Lambda^even content (6Y, colour, weak): multiplicity:", ct)

    st = []
    for (y6, col, wk), m in ct.items():
        st += [(Fr(y6, 6), col, wk)] * m
    sY = sum(y for y, _, _ in st)
    sY3 = sum(y ** 3 for y, _, _ in st)
    dims = {"1": 1, "3": 3, "3bar": 3, "2": 2}
    su3 = sum(Fr(1, 2) * Fr(1, dims[col]) * y for y, col, wk in st if col in ("3", "3bar"))
    su2 = sum(Fr(1, 2) * Fr(1, dims[wk]) * y for y, col, wk in st if wk == "2")
    d6 = sY == 0 and sY3 == 0 and su3 == 0 and su2 == 0
    say("D6 holds:", d6, "| sum Y %s, sum Y^3 %s, SU(3)^2 Y %s, SU(2)^2 Y %s (per state, index / dimension)" % (sY, sY3, su3, su2))

    yw = np.real(np.linalg.eigvals(Em.conj().T @ Y6 @ Em))
    yc = np.real(np.linalg.eigvals(Ep.conj().T @ Y6 @ Ep))
    SIXY_H = 3
    d7 = np.allclose(yw, SIXY_H) and np.allclose(yc, -2)
    say("D7 holds:", d7, "| Lambda^1: 6Y on the weak doublet", np.round(yw, 9).tolist(), "(SIXY's H: 3), on the colour triplet",
        np.round(yc, 9).tolist())

    rT = rho[GT]
    evT = np.linalg.eigvals(rT)
    one = np.isclose(evT, 1)
    plant_ct = content(1, 4, -4, 1) if one.sum() == 1 else None
    plant = plant_ct is not None and plant_ct != want
    say("plant (rho(T)'s 1-dimensional eigenspace in place of P's 3 + 2): content differs from D5:", plant, "| content:", plant_ct)


if __name__ == "__main__":
    main()
