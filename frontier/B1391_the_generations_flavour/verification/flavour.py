#!/usr/bin/env python3
"""B1391 -- THE GENERATIONS' FLAVOUR (test 4, structural): how the frame's generations transform under the isometries that fix the
Higgs class, and what that forces on the Yukawa couplings at the symmetric point.

(A) THE EQUIVARIANT INDEX.  At an Isom-invariant cut M_T, the frame's count is N = chi(M_T, d+M_T) (B1351 (ii), chi(M_T) = 0).  An
    isometry g fixing the Higgs class preserves d+ and acts on H*(M_T, d+M_T); its Lefschetz number is chi(Fix g, Fix g n d+)
    (Lefschetz for pairs).  So the generations form a virtual representation V of Isom_v(M) with character chi_V(g) = L(g).
(B) CUBE~3.24 (B1386, B1387; Isom = D3, all orientation-preserving, all fixing v+).  From B1390's instrument, per element: the fixed
    arcs and their ends on each cusp torus.  From B1387's partitions: cusps 0 and 3 disc-type (chi(d+) = -1, so d- is ONE disc), cusps
    1 and 2 annular (one d+ annulus, one d- annulus).  Two lemmas place the fixed points exactly:
      - a periodic map of a closed disc onto itself has exactly one fixed point (Brouwer; Kerekjarto: it is conjugate to a rotation), so
        R's three fixed points on cusps 0 and 3 put one in d- and two in d+;
      - an orientation-preserving involution of an annulus onto itself has 0 or 2 fixed points (its Lefschetz number is 1 - (+-1)), so a
        swap's four fixed points on cusps 1 and 2 split 2 / 2 (assuming, as for B1387's partitions, none on the zero curve).
    Then L(e) = 2, L(R) = 3 - 4 = -1, L(swap) = 4 - 4 = 0: the character of E, D3's two-dimensional irreducible representation.
    Cross-check with the zero count (B1388): R fixes the three zeros at its axes' midpoints, Hopf indices +1, -1, +1, so tr R = -1.
(C) THE YUKAWA TEXTURES, exact (sympy).  D3-covariant bilinear forms on E with a Higgs in a one-dimensional representation, and the
    free Z/3's regular representation (the pullback three, B1390) with a Higgs of definite charge.
(D) HOW COMMON THE 2 + 1 IS.  On B1386's 184 members (ocube06_08812 and its covers of degree 2 and 3), the members with an order-3
    isometry that rotates no cusp (so acts freely, B1390) and an isometry inverting it -- the structure under which a pullback three
    would be S3's singlet + doublet.
Usage: python3 flavour.py            (A)-(C)
       python3 flavour.py deck       (D), about a minute"""
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1390_the_eisenstein_axes" / "verification"))

D3_CLASSES = ("e", "R", "swap")                       # sizes 1, 2, 3
D3_SIZES = (1, 2, 3)
D3_IRREPS = {"A1": (1, 1, 1), "A2": (1, 1, -1), "E": (2, -1, 0)}


def decompose(chi):
    """multiplicities of D3's irreducible characters in the class function chi = (chi(e), chi(R), chi(swap))"""
    out = {}
    for name, psi in D3_IRREPS.items():
        s = sum(n * a * b for n, a, b in zip(D3_SIZES, chi, psi))
        assert s % 6 == 0, "not a virtual character"
        out[name] = s // 6
    return out


def cube324():
    import snappy
    return snappy.Manifold("o10_150725").covers(3)[4].covers(3)[24]


# the partitions of v+'s leading modes (B1387): chi(d+) per cusp, and the type of d-
PARTITION = {0: ("disc", -1), 1: ("annular", 0), 2: ("annular", 0), 3: ("disc", -1)}


def fixed_points_in_dplus(k, cusp, n_fixed):
    """how many of g's n_fixed fixed points on cusp's torus lie in d+, by the two lemmas"""
    kind, chi = PARTITION[cusp]
    if kind == "disc":                                  # d- is one disc: exactly one fixed point of the periodic map in it
        return n_fixed - 1
    assert kind == "annular" and k == 2 and n_fixed == 4   # an involution of each annulus: 2 and 2
    return 2


def equivariant_index():
    import eisenstein_axes as EA
    M = cube324()
    FS, rows, agree = EA.analyse("cube~3.24", M)
    assert agree and len(FS.auts) == 6
    chi_d_plus = sum(PARTITION[c][1] for c in PARTITION)
    table = []
    for (k, o, r) in rows:
        assert o == 1                                  # D3: all orientation-preserving
        if k == 1:
            L = 0 - chi_d_plus                         # chi(M_T) - chi(d+M_T)
            table.append(("e", k, L, "chi(M_T) = 0, chi(d+) = %d" % chi_d_plus))
            continue
        assert r["closed"] == 0 and not r["anomalies"]
        in_plus = sum(fixed_points_in_dplus(k, c, n) for c, n in r["ends"].items())
        L = r["arcs"] - in_plus
        cls = "R" if k == 3 else "swap"
        table.append((cls, k, L, "%d arcs, ends %s, %d of them in d+" % (r["arcs"], dict(sorted(r["ends"].items())), in_plus)))
    chi = []
    for cls in D3_CLASSES:
        vals = {t[2] for t in table if t[0] == cls}
        assert len(vals) == 1, (cls, vals)             # a class function
        chi.append(vals.pop())
    return table, tuple(chi), decompose(tuple(chi))


def yukawa_E():
    """D3-covariant bilinear forms B on E x E with values in a one-dimensional rep of the Higgs.
    Basis e+ (R-charge w), e- (R-charge w^2); the swap exchanges them.  B(Rx, Ry) = B(x, y) (the Higgs is R-neutral: a 1-dim rep of D3
    is trivial on R), B(sx, sy) = eps B(x, y), eps = +1 (A1) or -1 (A2)."""
    w = sp.exp(2 * sp.pi * sp.I / 3)
    Rm = sp.diag(w, w ** 2)
    Sm = sp.Matrix([[0, 1], [1, 0]])
    b = sp.symbols("b0:4")
    B = sp.Matrix(2, 2, b)
    out = {}
    for name, eps in (("A1", 1), ("A2", -1)):
        eqs = list(Rm.T * B * Rm - B) + list(Sm.T * B * Sm - eps * B)
        sol = sp.solve([sp.nsimplify(sp.simplify(e)) for e in eqs], b, dict=True)
        Bs = sp.simplify(B.subs(sol[0]))
        sv = sorted(set(sp.simplify(sp.sqrt(v)) for v in (Bs.H * Bs).eigenvals()))
        sym = sp.simplify(Bs - Bs.T) == sp.zeros(2, 2)
        out[name] = (Bs, sv, sym)
    return out


def yukawa_regular():
    """the free Z/3's regular representation (charges 0, 1, 2) with a Higgs of charge q: covariant 3 x 3 matrices Y_ij != 0 only if
    i + j + q = 0 (mod 3).  Symmetric (the 10 10 5_H coupling): the singular values, exactly.  General (10 5bar 5bar_H): a permutation
    pattern with three independent entries."""
    res = {}
    for q in range(3):
        a = sp.symbols("y0:9")
        Y = sp.Matrix(3, 3, lambda i, j: a[3 * i + j] if (i + j + q) % 3 == 0 else 0)
        Ysym = Y.subs({a[3 * j + i]: a[3 * i + j] for i in range(3) for j in range(3) if i < j})
        free_sym = sorted({s for s in Ysym.free_symbols}, key=str)
        # singular values of the symmetric texture: eigenvalues of Ysym^dagger Ysym for positive real entries
        vals = [sp.Symbol("p%d" % i, positive=True) for i in range(len(free_sym))]
        Yp = Ysym.subs(dict(zip(free_sym, vals)))
        ev = (Yp.T * Yp).eigenvals()
        res[q] = (Ysym, ev, len({s for s in Y.free_symbols}))
    return res


def deck_inverted():
    """(D): members of B1386's family with a free order-3 isometry R and an isometry s with s R s^-1 = R^-1"""
    import snappy
    base = snappy.Manifold("o10_150725").covers(3)[4]
    cands = [("ocube06_08812", base)] + [("cube~%d.%d" % (d, i), C) for d in (2, 3) for i, C in enumerate(base.covers(d))]
    hits, free_any = [], 0
    for name, M in cands:
        G = M.symmetry_group()
        n = G.order()
        if n % 3:
            continue
        isos = G.isometries()
        e = next(i for i in range(n) if all(G.multiply_elements(i, j) == j for j in range(n)))
        inv = {g: next(h for h in range(n) if G.multiply_elements(g, h) == e) for g in range(n)}
        o3 = [g for g in range(n) if g != e and G.multiply_elements(G.multiply_elements(g, g), g) == e]
        found, has_free = None, False
        for g in o3:
            imgs, maps = isos[g].cusp_images(), isos[g].cusp_maps()
            if any(im == c and int(maps[c][0, 0]) + int(maps[c][1, 1]) == -1 for c, im in enumerate(imgs)):
                continue                                          # rotates a cusp
            has_free = True
            for s_ in range(n):
                if G.multiply_elements(G.multiply_elements(s_, g), inv[s_]) == inv[g]:
                    found = (name, M.num_cusps(), n)
                    break
            if found:
                break
        free_any += has_free
        if found:
            hits.append(found)
    return len(cands), free_any, hits


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "deck":
    total, free_any, hits = deck_inverted()
    print("=== (D) B1386's %d members: a free order-3 isometry on %d; one inverted by another isometry on %d ===" % (total, free_any,
                                                                                                           len(hits)))
    print("  e.g. %s" % hits[:6])
    print("  -> the S3 structure of a 2 + 1 is common; the binding condition for a pullback three is |N| = 1 on the quotient.")
    print("DONE")
    sys.exit(0)

if __name__ == "__main__":
    print("=== (A)-(B) the equivariant index on cube~3.24 (Lefschetz numbers of the pair (M_T, d+M_T) at an invariant cut) ===")
    table, chi, dec = equivariant_index()
    for cls, k, L, why in table:
        print("  %-5s order %d: L = %+d   (%s)" % (cls, k, L, why))
    print("  character (e, R, swap) = %s; D3 decomposition %s" % (chi, dec))
    assert chi == (2, -1, 0) and dec == {"A1": 0, "A2": 0, "E": 1}
    print("  -> the two generations are D3's doublet E: R gives them the charges w and w^2, the swaps exchange them.")
    print("  cross-check (B1388's zeros): R fixes the three axis-midpoint zeros, Hopf indices +1, -1, +1; tr R = -(+1) = -1.")
    print("\n=== (C) the Yukawa textures at the symmetric point ===")
    for name, (Bs, sv, sym) in yukawa_E().items():
        print("  Higgs in %s: the covariant form on E x E is %s; symmetric: %s; singular values %s" % (name, Bs.tolist(), sym, sv))
    E = yukawa_E()
    assert len(E["A1"][1]) == 1 and len(E["A2"][1]) == 1                       # one singular value, twice: degenerate
    assert E["A1"][2] and not E["A2"][2]                                         # the up-type (symmetric) coupling needs A1
    print("  -> with one Higgs doublet of each type (a one-dimensional representation), both generations have the SAME mass in every"
          " sector; the symmetric 10 10 5_H coupling vanishes if its Higgs is in A2.  A Higgs in E (a doublet of doublets) splits them"
          " only through a D3-breaking vacuum: the swap forces |h+| = |h-| and R forces h+ = h- = 0.")
    for q, (Ysym, ev, nfree) in yukawa_regular().items():
        mult = sorted(ev.values())
        print("  free Z/3, Higgs charge %d: symmetric texture %s, eigenvalues of Y^T Y with multiplicities %s; general texture %d"
              " independent entries" % (q, Ysym.tolist(), mult, nfree))
        assert 2 in mult and nfree == 3
    print("  -> the pullback three (B1390): a symmetric coupling with a Higgs of definite charge always has a degenerate pair --"
          " B1362's circulant degeneracy, for every charge; the 10 5bar coupling is a permutation texture, not degenerate.")
    print("DONE")
