#!/usr/bin/env python3
"""B1386 S2-S4 -- the open Eisenstein cusp: cube~3.24, the degree-3 cover no. 24 of ocube06_08812 (B1385 S9), itself o10_150725's
degree-3 cover no. 4 -- a degree-9 cover of a member of B1186's family, so a member of m004's commensurability class.

The manifold is stored as its decorated isomorphism signature (cube3_24.isosig: the triangulation with its cusp order and peripheral
curves).  The instruments run on the covering path's own triangulation, asserted to have exactly that signature: a change in SnapPy's
enumeration of covers fails loudly instead of silently analysing another manifold.  (B1369's exact homology, sympy's fraction-free
elimination, exhausts memory on the signature's relabelled copy of the same triangulation; the covering path's labelling runs in
about two minutes.)

S2 (SnapPy): 90 tetrahedra, all positively oriented; volume 45 vol(m004); H_1 = Z/3 + Z/3 + Z/9 + Z^5; four cusps, three hexagonal
    (0, 2, 3) and one of modulus sqrt(3) i (cusp 1); isometry group D3 of order 6, chiral; an order-3 isometry R rotates cusps 0 and 3.
S3 (B1369's instrument through B1385's subclass, on the manifold's own triangulation, which realises all six isometries): the action of
    every isometry on H^1(M; Q) and on the cusps.  V = H^1(M; Q)^R has dimension 3 (the transfer lemma, L2: it lies in ann(P_0) and
    ann(P_3)); the three swaps of cusps 0 and 3 act on V with eigenvalues +1, -1, -1; the classes fixed by every isometry form one
    line <v+>, and it is exactly the cuspidal line (the classes vanishing on every cusp; dimension b_1 - #cusps = 1 by
    half-lives-half-dies).  No isometry negates v+: neither B1369's parity nor L3 applies.
S4 (B1370's instrument, unchanged): every cusp developed from the shapes, every fixer's affine action (linear part and translation part)
    read, the allowed Fourier shells for v+ computed.  R acts on cusps 0 and 3 by an order-3 rotation with three fixed points and on
    cusps 1 and 2 by a translation of order 3.  The leading allowed shells: cusps 0 and 3, the first hexagonal shell (six vectors, one
    rotation orbit, real dimension 2); cusp 1, one direction; cusp 2, the sqrt(3)-shell (three directions, real dimension 3).
    Then L4, the fixed-point congruence, checked on random invariant fields and applied: N(v+) = chi_0 (mod 3), never 0 while the
    first shell leads at cusp 0.
Usage: python3 the_open_cusp.py"""
import cmath
import math
import random
import sys
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
import sympy as sp
import snappy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1385_the_states_together" / "verification"))
import eisenstein_cusps as E                     # B1369's instrument (family_isometries.py) through B1385's thin subclass
import eisenstein_partition as EP                # B1385 S7: the Euler characteristic on the triangulated periodic grid
from eisenstein_candidate import R70             # B1370's instrument (residual_cusp_modes.py): its function definitions, unchanged

ISOSIG = (HERE / "cube3_24.isosig").read_text().strip()


def member():
    return snappy.Manifold(ISOSIG)


def covering_path():
    """o10_150725 (B1186's family) -> covers(3)[4] = ocube06_08812 (B1385 S9) -> covers(3)[24]"""
    return snappy.Manifold("o10_150725").covers(3)[4].covers(3)[24]


def _order3(m):
    a, b, c, d = int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1])
    return a * d - b * c == 1 and a + d == -1


def s2_snappy(M=None):
    """the SnapPy-level facts (seconds)"""
    M = M or member()
    G = M.symmetry_group()
    rot = set()
    for iso in G.isometries():
        for c, img in enumerate(iso.cusp_images()):
            if img == c and _order3(iso.cusp_maps()[c]):
                rot.add(c)
    vol = snappy.ManifoldHP(ISOSIG).volume() / snappy.ManifoldHP("m004").volume()
    shapes = [complex(z) for z in M.cusp_info("shape")]
    return {"tetrahedra": M.num_tetrahedra(), "solution": M.solution_type(), "volume / vol(m004)": float(vol),
            "volume ratio error": float(abs(vol - 45)), "H1": str(M.homology()), "cusps": M.num_cusps(),
            "cusp shapes": [complex(round(z.real, 9), round(z.imag, 9)) for z in shapes],
            "isometries": G.order(), "group": str(G), "amphichiral": G.is_amphicheiral(), "rotation cusps": sorted(rot),
            "isometric to the covering path": M.is_isometric_to(covering_path())}


def _nullspace(rows):
    return sp.Matrix.vstack(*rows).nullspace()


def _primitive(v):
    den = sp.ilcm(*[sp.fraction(x)[1] for x in v])
    w = v * den
    g = sp.igcd(*[int(x) for x in w])
    w = w / g
    first = next(x for x in w if x != 0)
    return w if first > 0 else -w


def s3_classes(FM):
    """the isometries on H^1 and on the cusps; V; the invariant line; the cuspidal line; the swaps on V"""
    b1 = FM.b1
    I = sp.eye(b1)
    auts = []
    for a in FM.auts:
        perm = FM.cusp_permutation(a)
        A = FM.action_on_H1(a)
        orient = "preserving" if FM.aut_sign(a) == {0} else "reversing"
        tor = {c: FM.action_on_torus(a, c) for c in range(FM.num_cusps) if perm[c] == c}
        auts.append(dict(aut=a, perm=tuple(perm[c] for c in range(FM.num_cusps)), A=A, orient=orient, torus=tor))
    rots = [x for x in auts if 0 in x["torus"] and x["torus"][0].det() == 1 and E.order(x["torus"][0]) == 3]
    swaps = [x for x in auts if x["perm"][0] == 3]
    V = _nullspace([x["A"].T - I for x in rots])
    Vm = sp.Matrix.hstack(*V)
    ann = {c: sp.Matrix.hstack(*FM.cusp[c]["ann"]) for c in range(FM.num_cusps)}
    in_ann = {c: sp.Matrix.hstack(ann[c], Vm).rank() == ann[c].rank() for c in range(FM.num_cusps)}
    inv = _nullspace([x["A"].T - I for x in auts])
    cusp_line = _nullspace([FM.cusp[c]["P"].T for c in range(FM.num_cusps)])
    assert len(inv) == 1 and len(cusp_line) == 1
    vp = _primitive(inv[0])
    assert sp.Matrix.hstack(vp, cusp_line[0]).rank() == 1, "the invariant line is the cuspidal line"
    # a swap restricted to V: A^T Vm = Vm S
    eig = []
    for g in swaps:
        S = (Vm.T * Vm).inv() * Vm.T * (g["A"].T * Vm)
        assert g["A"].T * Vm == Vm * S
        eig.append(sorted(int(e) for e, m in S.eigenvals().items() for _ in range(m)))
    negators = [x["perm"] for x in auts if x["A"].T * vp == -vp]
    return {"auts": auts, "rotations": rots, "swaps": swaps, "V": V, "vp": vp,
            "summary": {"isometries (cusp permutation, orientation)": sorted((x["perm"], x["orient"]) for x in auts),
                        "rotations fixing cusp 0 (order 3)": len(rots), "swaps of cusps 0 and 3": len(swaps),
                        "free cusps": [c for c in range(FM.num_cusps) if FM.cusp[c]["free"] > 0],
                        "dim V = dim H^1(M)^R": len(V), "V inside ann(P_c)": in_ann,
                        "dim H^1(M)^Isom": len(inv), "dim of the cuspidal line": len(cusp_line),
                        "v+ (B1369's H-basis)": [int(x) for x in vp], "swap eigenvalues on V": eig,
                        "isometries negating v+": negators,
                        "v+ fixed by every isometry": all(x["A"].T * vp == vp for x in auts)}}


# ------------------------------------------------------------------------------------------- B1370 on every cusp, for the class v+
def _allowed_basis(ks, fixers):
    """a real basis of the coefficient vectors (Re a_k, Im a_k) allowed by a_{-k} = conj a_k and a_{A^T k} = eps a_k e^{2 pi i k.b}
    (B1370's constraints, the same rows as its allowed_dimension)"""
    idx = {k: i for i, k in enumerate(ks)}
    n = len(ks)
    rows = []
    for k in ks:
        i, j = idx[k], idx[(-k[0], -k[1])]
        r1 = np.zeros(2 * n); r1[2 * j] = 1; r1[2 * i] = -1; rows.append(r1)
        r2 = np.zeros(2 * n); r2[2 * j + 1] = 1; r2[2 * i + 1] = 1; rows.append(r2)
    for (A, b, eps) in fixers:
        for k in ks:
            kA = tuple(int(x) for x in A.T @ np.array(k))
            ph = cmath.exp(2j * math.pi * (k[0] * b[0] + k[1] * b[1]))
            co = {idx[kA]: 1 + 0j}
            co[idx[k]] = co.get(idx[k], 0j) - eps * ph
            re = np.zeros(2 * n); im = np.zeros(2 * n)
            for jj, cv in co.items():
                re[2 * jj] += cv.real; re[2 * jj + 1] -= cv.imag
                im[2 * jj] += cv.imag; im[2 * jj + 1] += cv.real
            rows.append(re); rows.append(im)
    _, s, vt = np.linalg.svd(np.array(rows))
    rank = int((s > 1e-8).sum())
    return vt[rank:]


def s4_cusps(FM, cls, nshells=10):
    vp = cls["vp"]
    R = cls["rotations"][0]["aut"]
    out = {}
    for c in range(FM.num_cusps):
        pos = trans = None
        for mirror in (False, True):
            pos, trans = R70["develop_cusp"](FM, c, mirror)
            if pos is not None:
                break
        assert pos is not None
        b1v, b2v = R70["lattice_basis"](trans)
        tau = R70["reduce_tau"](b2v / b1v)
        fixers = []
        for x in cls["auts"]:
            if x["perm"][c] != c:
                continue
            eps = 1 if x["A"].T * vp == vp else -1
            orient, A, bc, _, _ = R70["affine_action"](FM, c, x["aut"], pos, b1v, b2v)
            fixers.append((A, bc, eps))
        oR, AR, bR, _, _ = R70["affine_action"](FM, c, R, pos, b1v, b2v)
        if np.array_equal(AR, np.eye(2, dtype=int)):
            kind = "translation"
            assert np.allclose(3 * bR, np.round(3 * bR)) and not np.allclose(bR, np.round(bR)), "a translation of order 3"
            fixed = []
        else:
            kind = "rotation"
            assert np.array_equal(np.linalg.matrix_power(AR, 3), np.eye(2, dtype=int)) and round(np.linalg.det(AR)) == 1
            IA = np.eye(2) - AR
            fixed = []
            for m in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2)]:
                p = np.linalg.solve(IA, bR + np.array(m)) % 1.0
                if not any(np.allclose((p - q + 0.5) % 1.0 - 0.5, 0, atol=1e-7) for q in fixed):
                    fixed.append(p)
            assert len(fixed) == 3, "an order-3 rotation of a torus has three fixed points"
        shells = R70["dual_shells"](b1v, b2v, nshells=nshells)
        table, allowed = [], []
        for nrm, ks in shells:
            dim = R70["allowed_dimension"](ks, fixers, None)
            dirs = R70["zero_set_type"](ks)
            table.append((round(nrm / shells[0][0], 6), len(ks), len(dirs), dim))
            if dim > 0:
                basis = _allowed_basis(ks, fixers)
                assert len(basis) == dim
                allowed.append((nrm, ks, basis))
        lin = Counter(tuple(int(x) for x in A.flatten()) for A, _, _ in fixers)
        out[c] = {"tau": complex(round(tau.real, 6), round(tau.imag, 6)), "fixers": len(fixers),
                  "fixers' linear parts (a, b, c, d): count": dict(sorted(lin.items())),
                  "signs on v+": sorted(set(e for _, _, e in fixers)), "R acts by": kind,
                  "R's translation": tuple(round(float(t), 6) for t in bR) if kind == "translation" else None,
                  "R's fixed points": [tuple(round(float(t), 6) for t in p) for p in fixed],
                  "shells (|k|^2 / first, vectors, directions, allowed real dim)": table,
                  "leading allowed shell (|k|^2 / first, vectors, directions, real dim)":
                      next((row for row in table if row[3] > 0), None),
                  "_allowed": allowed, "_fixed": fixed}
    return out


# ------------------------------------------------------------------------------------------- L4 and the index
def grid_values(terms, n):
    """F(s, t) = sum Re(a_k e^{2 pi i (k0 s + k1 t)}) on the n x n grid of the torus in lattice coordinates"""
    s = np.arange(n) / n
    F = np.zeros((n, n))
    for a, k in terms:
        F += np.real(a * np.exp(2j * np.pi * (k[0] * s[:, None] + k[1] * s[None, :])))
    return F


def chi_grid(pos):
    """chi of the full subcomplex on the vertices where pos holds -- the same triangulated grid as B1385's chi_positive (squares split
    along the (1, 1) diagonal), vectorised"""
    a = np.roll(pos, -1, axis=0)
    b = np.roll(pos, -1, axis=1)
    d = np.roll(a, -1, axis=1)
    V = pos.sum()
    Ecount = (pos & a).sum() + (pos & b).sum() + (pos & d).sum()
    T = (pos & a & d).sum() + (pos & b & d).sum()
    return int(V - Ecount + T)


def value_at(terms, p):
    return sum((a * cmath.exp(2j * math.pi * (k[0] * p[0] + k[1] * p[1]))).real for a, k in terms)


def critical_points(terms, seeds=64, iters=60, extra=()):
    """the critical points of F on the torus: damped Newton from a seeds x seeds grid (and from the points in extra -- the rotation's
    fixed points, which are critical for every invariant field), deduplicated modulo the lattice; returns [(x, F(x), type)] with type
    'max', 'min' or 'saddle' from the Hessian (Sylvester: a congruent form has the same signs)"""
    a = np.array([t[0] for t in terms])
    K = np.array([t[1] for t in terms], dtype=float)
    KK = np.stack([K[:, 0] * K[:, 0], K[:, 0] * K[:, 1], K[:, 1] * K[:, 1]], axis=1)
    g = (np.arange(seeds) + 0.5) / seeds
    X = np.array([(s, t) for s in g for t in g] + [tuple(p) for p in extra])

    def derivatives(X):
        E = a[None, :] * np.exp(2j * np.pi * (X @ K.T))
        return np.real(E.sum(axis=1)), np.real((2j * np.pi) * (E @ K)), -4 * np.pi ** 2 * np.real(E @ KK)

    active = np.arange(len(X))
    for _ in range(iters):                                   # Newton on the seeds not yet converged
        _, grad, h = derivatives(X[active])
        det = h[:, 0] * h[:, 2] - h[:, 1] ** 2
        ok = np.abs(det) > 1e-14
        step = np.zeros((len(active), 2))
        step[ok, 0] = (h[ok, 2] * grad[ok, 0] - h[ok, 1] * grad[ok, 1]) / det[ok]
        step[ok, 1] = (-h[ok, 1] * grad[ok, 0] + h[ok, 0] * grad[ok, 1]) / det[ok]
        norm = np.linalg.norm(step, axis=1)
        big = norm > 0.05
        step[big] *= (0.05 / norm[big])[:, None]
        X[active] = (X[active] - step) % 1.0
        active = active[norm >= 1e-13]
        if not len(active):
            break
    vals, grad, h = derivatives(X)
    scale = max(1.0, float(np.abs(vals).max()))
    conv = np.linalg.norm(grad, axis=1) <= 1e-9 * scale
    X, vals, h = X[conv], vals[conv], h[conv]
    _, first = np.unique(np.round(X * 1e6).astype(np.int64) % 1000000, axis=0, return_index=True)
    X, vals, h = X[first], vals[first], h[first]
    D = np.abs((X[:, None, :] - X[None, :, :] + 0.5) % 1.0 - 0.5).max(axis=2)       # merge a pair split by the rounding
    keep = [i for i in range(len(X)) if not any(D[i, j] < 1e-7 for j in range(i))]
    pts = []
    for i in keep:
        d = h[i, 0] * h[i, 2] - h[i, 1] ** 2
        kind = "saddle" if d < 0 else ("max" if h[i, 0] < 0 else "min")
        pts.append((X[i], float(vals[i]), kind))
    return pts


def morse_chi(terms, fixed=()):
    """chi(d+) by the Morse count, chi({F > 0}) = #max - #saddle + #min over the critical points with F > 0 (the handle count of the
    sublevel set of -F).  The search is refined (64, 128, 256 seeds per side) until it is complete in the checkable sense: the fixed
    points are among the critical points found and #max - #saddle + #min = chi(T^2) = 0.  Returns (chi, complete, gap, points), gap
    the smallest |critical value| relative to max |F| -- the distance from a degenerate partition"""
    for seeds in (64, 128, 256):
        pts = critical_points(terms, seeds=seeds, extra=fixed)
        sign = {"max": 1, "min": 1, "saddle": -1}
        total = sum(sign[k] for _, _, k in pts)
        found_fixed = all(any(np.allclose((x - np.array(p) + 0.5) % 1.0 - 0.5, 0, atol=1e-6) for x, _, _ in pts) for p in fixed)
        if total == 0 and found_fixed:
            break
    chi = sum(sign[k] for _, v, k in pts if v > 0)
    top = max(abs(v) for _, v, _ in pts)
    gap = min(abs(v) for _, v, _ in pts) / top
    return chi, total == 0 and found_fixed, gap, pts


HEX_ROT = np.array([[0, -1], [1, -1]])                        # an order-3 rotation of the hexagonal lattice, basis (1, omega)
HEX_FIX = [(0.0, 0.0), (2 / 3, 1 / 3), (1 / 3, 2 / 3)]        # its three fixed points on the torus


DEGENERATE = 1e-6      # a critical value within this fraction of max|F| of zero: the partition is not regular -- excluded, and counted
RESOLVED = 1e-2        # every critical value at least this far from zero: the grid must agree with the Morse count


def judge(terms, fixed, n=150):
    """one invariant field: chi(d+) by the Morse count (primary; for a one-direction field, whose critical set is not isolated, by the
    grid, where B1370's annulus gives 0), the number of fixed points in d+, and the grid's chi where every critical value is at least
    RESOLVED from zero (the cross-check)"""
    K = np.array([k for _, k in terms], dtype=float)
    nfix = sum(1 for p in fixed if value_at(terms, p) > 0)
    if np.linalg.matrix_rank(K) == 1:
        chi = chi_grid(grid_values(terms, n) > 0)
        return dict(chi=chi, complete=True, degenerate=False, nfix=nfix, grid=None, one_direction=True)
    chi, complete, gap, pts = morse_chi(terms, fixed)
    grid = chi_grid(grid_values(terms, n) > 0) if gap > RESOLVED else None
    return dict(chi=chi, complete=complete, degenerate=gap < DEGENERATE, nfix=nfix, grid=grid, one_direction=False)


def tally(records):
    """L4 over the regular samples: chi(d+) = nfix (mod 3) -- nfix = 0 where R translates"""
    out = Counter()
    for r in records:
        if not r["complete"]:
            out["search incomplete (excluded)"] += 1
            continue
        if r["degenerate"]:
            out["degenerate (excluded)"] += 1
            continue
        out["congruence holds" if (r["chi"] - r["nfix"]) % 3 == 0 else "congruence FAILS"] += 1
        if r["grid"] is not None:
            out["grid agrees" if r["grid"] == r["chi"] else "grid DISAGREES"] += 1
        if r["one_direction"]:
            out["one direction (annular)"] += 1
    return dict(sorted(out.items()))


def l4_synthetic(trials=60, n=150, seed=1, box=2):
    """L4 on the model torus, independent of any manifold: a random trigonometric polynomial G (frequencies in a box, random complex
    coefficients) averaged over the rotation, F = G + G o A + G o A^2, or over the translation by (1/3, 1/3); then chi(d+) against the
    number of fixed points in d+ (mod 3), and chi(d+) = 0 (mod 3) for the free action"""
    rng = random.Random(seed)
    ks = [(m, k) for m in range(-box, box + 1) for k in range(-box, box + 1) if (m, k) != (0, 0)]
    A1 = HEX_ROT.T
    A2 = (HEX_ROT @ HEX_ROT).T
    rot, trans, pairs = [], [], Counter()
    for _ in range(trials):
        g = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) / (1 + abs(m) + abs(k)) for (m, k) in ks]
        terms = []
        for gk, k in zip(g, ks):                                # G o A has the coefficient of k at A^T k
            terms += [(gk, k), (gk, tuple(int(x) for x in A1 @ np.array(k))), (gk, tuple(int(x) for x in A2 @ np.array(k)))]
        r = judge(terms, HEX_FIX, n)
        rot.append(r)
        if r["complete"] and not r["degenerate"]:
            pairs[(r["chi"], r["nfix"])] += 1
        tt = [(3 * gk, k) for gk, k in zip(g, ks) if (k[0] + k[1]) % 3 == 0]    # G averaged over x -> x + (1/3, 1/3)
        trans.append(judge(tt, (), n))
    out = {"rotation-averaged": tally(rot), "translation-averaged": tally(trans),
           "rotation-averaged (chi(d+), fixed points in d+)": dict(sorted(pairs.items())),
           "translation-averaged chi(d+)": dict(sorted(Counter(r["chi"] for r in trans if r["complete"] and not r["degenerate"]).items()))}
    for key in ("rotation-averaged", "translation-averaged"):
        assert "congruence FAILS" not in out[key] and "grid DISAGREES" not in out[key], out[key]
    return out


def random_field(rng, allowed, shells=1, decay=0.6, skip_first=False):
    """a random field from the allowed shells: the leading one alone, or several with geometrically decaying weights"""
    use = allowed[1:] if skip_first else allowed
    terms = []
    for depth, (nrm, ks, basis) in enumerate(use[:shells]):
        coef = sum(rng.gauss(0, 1) * v for v in basis) * (decay ** depth)
        terms += [(complex(coef[2 * i], coef[2 * i + 1]), k) for i, k in enumerate(ks)]
    return terms


def s4_l4(cusps, trials=120, n=150, seed=5):
    """L4 on the member's own invariant fields, at every cusp: random allowed coefficients on the leading shell, on four allowed shells,
    and on three allowed shells after the first; chi(d+) = #(Fix R in d+) (mod 3) where R rotates, 0 (mod 3) where R translates"""
    rng = random.Random(seed)
    checks, ranges = {}, {}
    kinds = (("leading shell", 1, False), ("four shells", 4, False), ("three shells after the first", 3, True))
    for c, row in cusps.items():
        allowed, fixed = row["_allowed"], row["_fixed"]
        recs = {label: [] for label, _, _ in kinds}
        for trial in range(trials):
            for label, shells, skip in kinds:
                recs[label].append(judge(random_field(rng, allowed, shells, skip_first=skip), fixed, n))
        checks[c] = {label: tally(r) for label, r in recs.items()}
        good = {label: [r for r in rr if r["complete"] and not r["degenerate"]] for label, rr in recs.items()}
        ranges[c] = {"chi(d+), leading shell": dict(sorted(Counter(r["chi"] for r in good["leading shell"]).items())),
                     "fixed points in d+, leading shell": dict(sorted(Counter(r["nfix"] for r in good["leading shell"]).items()))
                     if fixed else None,
                     "fixed points in d+, three shells after the first":
                         dict(sorted(Counter(r["nfix"] for r in good["three shells after the first"]).items())) if fixed else None}
    return checks, ranges


def s4_index(cusps, trials=200, n=150, seed=9):
    """N(v+) = -(chi_0 + chi_1 + chi_2 + chi_3) with chi_3 = chi_0 (the swap: orientation-preserving, fixing v+, cusp 0 -> cusp 3), the
    leading shells sampled independently at cusps 0, 1, 2"""
    rng = random.Random(seed)
    vals = Counter()
    congruent = True
    excluded = 0
    for _ in range(trials):
        rs = {c: judge(random_field(rng, cusps[c]["_allowed"], 1), cusps[c]["_fixed"], n) for c in (0, 1, 2)}
        if any(not r["complete"] or r["degenerate"] for r in rs.values()):
            excluded += 1
            continue
        N = -(2 * rs[0]["chi"] + rs[1]["chi"] + rs[2]["chi"])
        vals[N] += 1
        congruent &= (N - rs[0]["chi"]) % 3 == 0
    return dict(sorted(vals.items())), congruent, excluded


def cross_check_grid(cusps, seed=3):
    """the vectorised chi agrees with B1385's chi_positive"""
    rng = random.Random(seed)
    for c in (0, 2):
        terms = random_field(rng, cusps[c]["_allowed"], 2)
        F = lambda s, t: sum((a * cmath.exp(2j * math.pi * (k[0] * s + k[1] * t))).real for a, k in terms)
        assert EP.chi_positive(F, 90) == chi_grid(grid_values(terms, 90) > 0)
    return True


def analyse():
    M = covering_path()
    assert M.triangulation_isosig(decorated=True) == ISOSIG, "the covering path must give the stored triangulation"
    FM = E.StateMember(M, "cube~3.24", canonical=False)
    assert len(FM.auts) == M.symmetry_group().order() == 6, "the own triangulation realises the whole isometry group"
    cls = s3_classes(FM)
    cusps = s4_cusps(FM, cls)
    return FM, cls, cusps


if __name__ == "__main__":
    print("L4 on the model torus:", l4_synthetic(), flush=True)
    s2 = s2_snappy()
    print("S2 the member (SnapPy):", s2, flush=True)
    FM, cls, cusps = analyse()
    print("S3 B1369's instrument: b1 %d; H1 basis size %d" % (FM.b1, len(FM.H)))
    for k, v in cls["summary"].items():
        print("   ", k, ":", v)
    print("S4 B1370's instrument, for v+:")
    for c, row in cusps.items():
        print("  cusp %d:" % c, {k: v for k, v in row.items() if not k.startswith("_")}, flush=True)
    print("  grid cross-check with B1385's chi_positive:", cross_check_grid(cusps))
    checks, ranges = s4_l4(cusps)
    print("S4 L4 on the member's random invariant fields (Morse count primary, grid cross-check where resolved):")
    for c, v in checks.items():
        print("  cusp %d:" % c, v)
    print("S4 leading-shell ranges:", ranges)
    vals, congruent, excluded = s4_index(cusps)
    print("S4 the index of v+ from the leading shells, N = -(2 chi_0 + chi_1 + chi_2):", vals, "; N = chi_0 (mod 3) throughout:",
          congruent, "; degenerate samples excluded:", excluded)
    print("DONE")
