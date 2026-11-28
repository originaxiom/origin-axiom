"""The decisive script of main's card on the whole's chiral blindness (P-882, the listening line; data-free; 2026-11-28).

On omega's orbit mod N (N = 27, 81), the orbit of (3,3,3) under the moves, the group G the moves generate acts
transitively, and the stabiliser of omega's point is <C> (order 3). For j = 0, 1, 2 the native bundle B_j = Ind_<C>^G psi_j,
psi_j(C) = w^j (sections carrying charge j at omega's fixed point), is built from coset representatives: g acts by
e_v -> psi_j(c) e_{g v} with g t_v = t_{g v} c. On each B_j the six-move sum s = L + R + L^-1 + R^-1 + X + X^-1 is split into
the three eigenspaces of C (charge sectors q). Scaling the one sector whose spectrum is twice the others' by 1/2, the three
sectors share a common core; what each sector holds beyond the core is its exceptional modes.

Decided: at both levels, on every bundle, the two sectors other than the doubled one are identical outside at most four
exceptional modes, and the exceptional modes are the same at mod 27 and mod 81. The whole tells its two charged sectors
apart only through those modes; at mod 81 the ninth-root cosines 2 cos(2 pi k / 9) are in the spectrum, alike in both
charged sectors.

    python3 relays/claims/main_frontier/chiral_blindness.py            (the claim; exit 0)
    python3 relays/claims/main_frontier/chiral_blindness.py --control  (an outside phase theta = 2 pi / 9 between the two walks
                                                                         W+ = L + X + R^-1 and W- = R + L^-1 + X^-1: the charged
                                                                         sectors split in bulk and the claim fails; exit 1)"""
import cmath
import math
import sys
from collections import Counter

import numpy as np

CONTROL = "--control" in sys.argv
W3 = cmath.exp(2j * math.pi / 3)
TOL = 1e-6


def moves(N):
    return dict(
        L=lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N), R=lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N),
        Li=lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]), Ri=lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0]),
        X=lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]), Xi=lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2]),
        C=lambda v: (v[1], v[2], v[0]))


def setup(N):
    m = moves(N)
    x0 = (3, 3, 3)
    seen, todo = {x0}, [x0]
    while todo:
        v = todo.pop()
        for k in ("L", "R", "Li", "Ri"):
            u = m[k](v)
            if u not in seen:
                seen.add(u)
                todo.append(u)
    pts = sorted(seen)
    idx = {v: i for i, v in enumerate(pts)}
    perm = {k: np.array([idx[f(v)] for v in pts]) for k, f in m.items()}   # perm[k][i] = image of point i
    i0 = idx[x0]
    # the group, as permutations (a o b)[i] = a[b[i]], and a representative t_v for each point (t_v[i0] = v)
    ident = np.arange(len(pts))
    reps = {i0: ident}
    frontier = [ident]
    elements = {ident.tobytes()}
    gens = [perm["L"], perm["R"], perm["C"]]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = g[a]                                      # g o a
                key = b.tobytes()
                if key not in elements:
                    elements.add(key)
                    nxt.append(b)
                    reps.setdefault(int(b[i0]), b)
        frontier = nxt
    inv = lambda p: np.argsort(p)
    Cp = perm["C"]
    powers = [ident, Cp, Cp[Cp]]
    return pts, perm, i0, reps, inv, powers, len(elements)


def bundle(perm_g, j, reps, inv, powers, n, i0):
    A = np.zeros((n, n), dtype=complex)
    for v in range(n):
        gv = int(perm_g[v])
        c = inv(reps[gv])[perm_g[reps[v]]]                    # t_gv^-1 o g o t_v, in the stabiliser of omega's point
        assert c[i0] == i0
        k = next(k for k in range(3) if np.array_equal(c, powers[k]))
        A[gv, v] = W3 ** (j * k)
    return A


def sectors(N, j, theta=0.0):
    pts, perm, i0, reps, inv, powers, order = setup(N)
    n = len(pts)
    act = {k: bundle(perm[k], j, reps, inv, powers, n, i0) for k in perm}
    ph = cmath.exp(1j * theta)
    S = ph * (act["L"] + act["X"] + act["Ri"]) + np.conj(ph) * (act["R"] + act["Li"] + act["Xi"])
    Cj = act["C"]
    out = []
    for q in range(3):
        Pi = (np.eye(n) + W3 ** (-q) * Cj + W3 ** (-2 * q) * Cj @ Cj) / 3
        u, sv, _ = np.linalg.svd(Pi)
        basis = u[:, sv > 0.5]
        H = basis.conj().T @ S @ basis
        out.append(np.sort(np.linalg.eigvalsh((H + H.conj().T) / 2)))
    return out, n, order


def counter(vals):
    return Counter(round(float(x), 4) + 0.0 for x in vals)


def analyse(secs):
    """the doubled sector, the common core of the three (the doubled one halved), and each sector's exceptional modes"""
    best = None
    for f in range(3):
        sc = [counter(s / 2 if q == f else s) for q, s in enumerate(secs)]
        core = sc[0] & sc[1] & sc[2]
        extra = [sc[q] - core for q in range(3)]
        size = sum(sum(e.values()) for e in extra)
        if best is None or size < best[0]:
            best = (size, f, core, extra)
    return best


bad = []
found = {}
for N in (27, 81):
    for j in range(3):
        secs, n, order = sectors(N, j, theta=2 * math.pi / 9 if CONTROL else 0.0)
        size, f, core, extra = analyse(secs)
        others = [q for q in range(3) if q != f]
        diff = sum((extra[others[0]] - extra[others[1]]).values()) + sum((extra[others[1]] - extra[others[0]]).values())
        found[(N, j)] = (f, [sorted(e.elements()) for e in extra])
        print("DECISIVE: mod %d (%d points, |G| = %d), bundle j = %d: doubled sector q = %d; the other two differ in %d modes; "
              "exceptional modes by sector %s" % (N, n, order, j, f, diff, [sorted(e.elements()) for e in extra]))
        if diff > 4:
            bad.append("mod %d, j = %d: the charged sectors differ in %d modes" % (N, j, diff))
        if N == 81 and j == 0:
            nine = [2 * math.cos(2 * math.pi * k / 9) for k in (1, 2, 4)]
            ok = all(any(abs(abs(x) - abs(c)) < 1e-3 for x in secs[q]) for c in nine for q in others)
            print("DECISIVE: mod 81, j = 0: the ninth-root cosines 2 cos(2 pi k / 9), k = 1, 2, 4, are in both charged sectors: %s" % ok)
            if not ok:
                bad.append("the ninth-root cosines are not in both charged sectors at mod 81")
for j in range(3):
    if found[(27, j)] != found[(81, j)]:
        bad.append("bundle j = %d: the doubled sector or the exceptional modes differ between mod 27 and mod 81" % j)
if bad:
    print("the claim fails: " + "; ".join(bad))
    sys.exit(1)
print("DECISIVE: on every native bundle at mod 27 and 81 the charge sectors are one doubled and two alike, outside the same "
      "exceptional modes at both levels: the whole tells its charged sectors apart only through them")
