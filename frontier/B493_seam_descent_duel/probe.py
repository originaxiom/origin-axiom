"""B493 (CL-1a) -- the seam descent duel: does CRT locality (P66/P67) + the character
gates (P68) + the universal trace-formula machinery (P64) assemble into a DERIVATION
of the B459/P1 subfield-lattice vanishing law of the seam channels?

Pre-registered in docs/CLOSURE_CAMPAIGN_2026-07.md (outcome enum DERIVED / OBSTRUCTED /
PARTIAL; control mandatory). Exact Q(zeta60) arithmetic throughout (the B358 engine);
zero numerics. Firewalled: statements about the level-15 theta model only.

THE DESCENT CHAIN (per-step status; proofs and the honest tiering in FINDINGS.md):

  (M) the master identity [DERIVED -- pure Fourier/Galois bookkeeping; also machine-
      checked]: for a pair with orders (o1,o2), channel tables ch_i = the (1,sqrt5,
      sqrt-3,sqrt-15)-coordinates of Pi_H t(a,b), and the dual-torus grids
      grid_i(x,y) = sum_{a,b} ch_i(a,b) zeta_{o1}^{ax} zeta_{o2}^{by}:
        grid_i(x,y) * basis_i = (1/16) sum_{c in (Z/60)^x} chi_i(c)
                                 sigma_c( C[c^-1 x mod o1, c^-1 y mod o2] )
      with chi_{p,q,r,s} = 1, chi5, chi_-3, chi5*chi_-3.  The gate roles are derived
      here: chi_-3 is the c3-flip sign (r,s channels), chi5 is the 5-side window
      character (q,s channels).
  (T) the tensor split [BANKED P66/P67; G1 re-verified out-of-sample here]:
      C = C3 * C5 cell-wise at multiplier (2,2), so the master summand factors
      through the two LOCAL tables.
  (S) the support lemma [DERIVED, given the checked period divisibilities]:
      F3(c) := sigma_c(C3[c^-1 x mod d1, c^-1 y mod d2]) factors through c mod 12
      (values in Q(zeta3), indices mod d_i | 12); F5(c) factors through c mod 30.
      Grouping the 16-term master sum by c3 = c mod 3, with
      X(c3) := sum_{c4} F3 and Y_psi(c3) := sum_{c5} psi(c5) F5:
        16 grid_p           = X(1)Y_1(1) + X(2)Y_1(2)
        16 grid_q sqrt5     = X(1)Y_L(1) + X(2)Y_L(2)
        16 grid_r sqrt-3    = X(1)Y_1(1) - X(2)Y_1(2)
        16 grid_s sqrt-15   = X(1)Y_L(1) - X(2)Y_L(2)
      Everything on the right is LOCAL.  Actual scope facts (checked): every 3-side
      order divides 4, every 5-side order lies in {1,6,10}.
  (X0/Xbar) the coset collapse and the conjugation identity [DERIVED, given d_i | 4]:
      X(1) = C3[x,y] + C3[-x,-y] cell-exact, and X(2) = conj3(X(1)) (41 = lift(1,2,1)
      is 1 mod 4 and 1 mod 5, so sigma_41 permutes the c3-cosets without moving the
      indices).  Both also machine-checked at every dual point.
  (R) cross-field rigidity [DERIVED]: X in Q(zeta3), Y in Q(zeta5),
      Q(zeta3) cap Q(zeta5) = Q; with Xbar, any ratio X(1)/X(2) forced rational is
      +-1, and -1 means X purely imaginary.
  (N1) no purely-imaginary X [DERIVED from two finite cell censuses]: every C3 cell
      lies in mu6 union {0} (checked), and QM below; then X = 2u or u + conj3(u),
      neither a nonzero element of Q*sqrt(-3).
  (QM) the 3-side quasi-mirror [VERIFIED cell-wise per pair; mechanism = unitarity +
      Par-trace reversal; its parity rule is a finite checked fact, sub-residue]:
      C3[-j,-l] = C3[j,l] (j = l mod 2) or conj3(C3[j,l]) (else).
  (L5a) no odd windows [VERIFIED per pair, all pairs so far]: no window pair
      (Y_psi(1), Y_psi(2)) is ever odd (Y(2) = -Y(1) != 0).
  (L5b) the window-matching law [VERIFIED on (1,2); PAIR-SPECIFIC -- THE NAMED
      RESIDUE]: tL in {zero, t1}.  It FAILS on the dark pair (1,3) (census mode
      (gen,even)), where its failure produces exactly the observed non-lattice
      single-s-dead tier -- so no universal argument can derive it; it is exactly
      where the (1,2)-specific content of the law lives.
  (CLS) the classifier theorem [DERIVED from Xbar+R+N1+L5a; machine-checked at every
      dual point of every pair]: the 4-bit vanishing pattern at a dual-torus point is
      a function of type-level local data alone -- (reality class of X, c3-flip type
      of Y_1, c3-flip type of Y_L).  Corollaries: the zero stratum is exactly
      (X = 0) or (Y-quadruple = 0); q dead forces s dead, so the Q(sqrt-15) node is
      absent UNIVERSALLY; and on any pair satisfying L5a+L5b the pattern set is
      contained in the subfield lattice of Q(sqrt5,sqrt-3) minus the Q(sqrt-15) node.
      With (1,2)'s checked census {(zero,zero),(even,zero),(even,even),(gen,gen)}
      this yields the full B459/P1 five-pattern law with its tier counts.

  THE P68 GATE ROLES (stage 2b; scope facts found here, all report-only):
      chi_-3 and chi5 enter the derivation as the (M)-characters above.  The
      Eisenstein order-gate (P68 L2) LOCALIZES to the 3-side (cell conj3-real <=>
      chi_-3(det(gamma'-I)) = +1 over det != 0 mod 3) and, at level 15 through the
      tensor identity, extends to EVERY pair (0 violations, incl. (2,5) and (4,7);
      the class-1 domain counts reproduce B396's banked counts).  P68 L1 (root of
      unity) also extends to every pair.  The chi5 order-gate (P68 L3) is
      (1,2)-SPECIFIC: it FAILS on (1,3), (1,4), (2,4), (4,7) both naively-local and
      at level 15 -- like L5b it is pair content, not framework.

PHASES (run in this order; the point of the split is that the (4,7) PREDICTION is
committed before any global (4,7) computation exists anywhere in the repo):
  control -- the mandatory controls + the descent checks on the twelve banked pairs;
  predict -- pair (4,7) (never computed in the repo; absence grep-verified) from
             LOCAL q=3 / q=5 data only -> b493_prediction_47.json;
  verify  -- the global (4,7) table via the banked B367 machinery; compare cell-exact.

Reuse: cyclo_engine + seam_certification (B358), step0_exact_matrices (B367);
local_model is lifted verbatim from B386 tensor_gate.py (that module is a top-level
script -- importing it would re-run its gate).
"""
import argparse
import hashlib
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E                      # noqa: E402
import seam_certification as SC               # noqa: E402
from step0_exact_matrices import (            # noqa: E402
    build_theta_W, matrix_order, pair_smatrix, par_trace)

G60 = [c for c in range(60) if gcd(c, 60) == 1]
MU6 = [E.zeta(10 * k) for k in range(6)]      # the sixth roots of unity in the engine


def chi5(c):
    r = c % 5
    return 0 if r == 0 else (1 if r in (1, 4) else -1)


def chim3(c):
    r = c % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def conj3(x):
    """Galois conjugation nontrivial exactly on the zeta3-part (c = 41: (1,2,1) mod (4,3,5))."""
    return SC.sigma(x, 41)


def conj5(x):
    """zeta5 -> zeta5^4 (c = 49: (1,1,4)); on Q(zeta5)-values, fixed field = Q(sqrt5)."""
    return SC.sigma(x, 49)


def lift(c4, c3, c5):
    """The element of (Z/60)^x with the given CRT components."""
    for c in G60:
        if c % 4 == c4 and c % 3 == c3 and c % 5 == c5:
            return c
    raise RuntimeError((c4, c3, c5))


# ---------------- the local theta models (B386 conventions, u = 2) ----------------
def zq(q, k):
    return E.zeta((60 // q) * (k % q))


def local_model(q, u, m):
    """Lifted verbatim from B386 tensor_gate.py."""
    N = q

    def diagm(f):
        return [[f(j) if i == j else E.ZERO for j in range(N)] for i in range(N)]

    D = diagm(lambda j: zq(q, u * (j * (j - 1) // 2)))
    Di = diagm(lambda j: zq(q, -u * (j * (j - 1) // 2)))
    F = [[zq(q, u * i * j) for j in range(N)] for i in range(N)]
    Fi = [[E.scal(Fr(1, q), zq(q, -u * i * j)) for j in range(N)] for i in range(N)]
    WR = E.mmul(E.mmul(F, Di), Fi)
    W = [[E.ONE if i == j else E.ZERO for j in range(N)] for i in range(N)]
    for _ in range(m):
        W = E.mmul(W, WR)
    Dm = diagm(lambda j: zq(q, m * u * (j * (j - 1) // 2)))
    return E.mmul(W, Dm)


def local_order(W, q, cap=64):
    ident = [[E.ONE if i == j else E.ZERO for j in range(q)] for i in range(q)]
    P = W
    for k in range(1, cap + 1):
        if P == ident:
            return k
        P = E.mmul(P, W)
    raise RuntimeError("order cap exceeded")


def local_powers(W, q, n):
    P = [[E.ONE if i == j else E.ZERO for j in range(q)] for i in range(q)]
    out = [P]
    for _ in range(n - 1):
        out.append(E.mmul(out[-1], W))
    return out


def local_par_trace(A, B, q):
    t = E.ZERO
    M = E.mmul(A, B)
    for x in range(q):
        t = E.add(t, M[(-x) % q][x])
    return t


def build_locals(m1, m2):
    """The two local Par-trace tables on their own period grids."""
    W3a, W3b = local_model(3, 2, m1), local_model(3, 2, m2)
    W5a, W5b = local_model(5, 2, m1), local_model(5, 2, m2)
    d1, d2 = local_order(W3a, 3), local_order(W3b, 3)
    e1, e2 = local_order(W5a, 5), local_order(W5b, 5)
    p3a, p3b = local_powers(W3a, 3, d1), local_powers(W3b, 3, d2)
    p5a, p5b = local_powers(W5a, 5, e1), local_powers(W5b, 5, e2)
    C3 = {(j, l): local_par_trace(p3a[j], p3b[l], 3) for j in range(d1) for l in range(d2)}
    C5 = {(j, l): local_par_trace(p5a[j], p5b[l], 5) for j in range(e1) for l in range(e2)}
    return (d1, d2, C3), (e1, e2, C5)


# ---------------- the convolution closed form (stage 1a) ----------------
def closed_form_ttable(loc3, loc5):
    """t(a,b) = sum over CRT-split frequencies of chat3 * chat5 -- LOCAL data only.

    chat_q = the DFT of the local table on its own period grid; a frequency a mod o1
    receives exactly the (alpha, gamma) with (o1/d1)alpha + (o1/e1)gamma = a mod o1.
    """
    d1, d2, C3 = loc3
    e1, e2, C5 = loc5
    o1 = d1 * e1 // gcd(d1, e1)
    o2 = d2 * e2 // gcd(d2, e2)

    def dft(table, n1, n2):
        out = {}
        for a in range(n1):
            for b in range(n2):
                acc = E.ZERO
                for j in range(n1):
                    za = E.zeta((-(60 // n1) * j * a) % 60)
                    for l in range(n2):
                        acc = E.add(acc, E.mul(E.mul(za, E.zeta((-(60 // n2) * l * b) % 60)),
                                               table[(j, l)]))
                out[(a, b)] = E.scal(Fr(1, n1 * n2), acc)
        return out

    c3h = dft(C3, d1, d2)
    c5h = dft(C5, e1, e2)
    splits1 = {a: [] for a in range(o1)}
    for al in range(d1):
        for ga in range(e1):
            splits1[((o1 // d1) * al + (o1 // e1) * ga) % o1].append((al, ga))
    splits2 = {b: [] for b in range(o2)}
    for be in range(d2):
        for de in range(e2):
            splits2[((o2 // d2) * be + (o2 // e2) * de) % o2].append((be, de))
    T = {}
    for a in range(o1):
        for b in range(o2):
            acc = E.ZERO
            for (al, ga) in splits1[a]:
                for (be, de) in splits2[b]:
                    acc = E.add(acc, E.mul(c3h[(al, be)], c5h[(ga, de)]))
            T[(a, b)] = acc
    return T, o1, o2


def channel_tables(T, o1, o2):
    """{(a,b): (p,q,r,s)} over raw-nonzero t -- EXACTLY the banked pair_smatrix convention."""
    out = {}
    for (a, b), t in sorted(T.items()):
        if t == E.ZERO:
            continue
        sol = SC.solve_H(SC.H_avg(t))
        assert sol is not None, (a, b)
        out[(a, b)] = sol
    return out


# ---------------- the descent machinery (stages 1b + 2) ----------------
def xy_data(loc3, loc5, o1, o2, x, y):
    """u, v, X(c3), Y_psi(c3) at the dual-torus point (x,y) -- all from LOCAL tables."""
    d1, d2, C3 = loc3
    e1, e2, C5 = loc5
    u = C3[(x % d1, y % d2)]
    v = C3[((-x) % d1, (-y) % d2)]
    X = {}
    for c3 in (1, 2):
        acc = E.ZERO
        for c4 in (1, 3):
            c = lift(c4, c3, 1)
            ci = pow(c, -1, 60)
            acc = E.add(acc, SC.sigma(C3[((ci * x) % d1, (ci * y) % d2)], lift(1, c3, 1)))
        X[c3] = acc
    Y = {}
    for c3 in (1, 2):
        for nm, ps in (("1", lambda cc: 1), ("L", chi5)):
            acc = E.ZERO
            for c5 in (1, 2, 3, 4):
                c = lift(1, c3, c5)
                ci = pow(c, -1, 60)
                cell = C5[((ci * x) % e1, (ci * y) % e2)]
                acc = E.add(acc, E.scal(Fr(ps(c5)), SC.sigma(cell, lift(1, 1, c5))))
            Y[(nm, c3)] = acc
    return u, v, X, Y


def xy_combos(X, Y):
    """(16 grid_p, 16 grid_q sqrt5, 16 grid_r sqrt-3, 16 grid_s sqrt-15)."""
    return (
        E.add(E.mul(X[1], Y[("1", 1)]), E.mul(X[2], Y[("1", 2)])),
        E.add(E.mul(X[1], Y[("L", 1)]), E.mul(X[2], Y[("L", 2)])),
        E.sub(E.mul(X[1], Y[("1", 1)]), E.mul(X[2], Y[("1", 2)])),
        E.sub(E.mul(X[1], Y[("L", 1)]), E.mul(X[2], Y[("L", 2)])),
    )


def ft_grids(ch, o1, o2):
    """FT of the four rational channel tables to the native dual torus Z_o1 x Z_o2
    (the B459 convention: + sign)."""
    grids = {}
    for i in range(4):
        g = {}
        for x in range(o1):
            for y in range(o2):
                acc = E.ZERO
                for (a, b), vv in ch.items():
                    if vv[i] != 0:
                        acc = E.add(acc, E.scal(Fr(vv[i]),
                                                E.zeta(((60 // o1) * a * x + (60 // o2) * b * y) % 60)))
                g[(x, y)] = acc
        grids[i] = g
    return grids


def pattern_of(grids, x, y):
    return tuple(1 if grids[i][(x, y)] == E.ZERO else 0 for i in range(4))


def window_type(Y, nm):
    """The c3-flip type of a window pair: zero / even / odd / gen."""
    a, b = Y[(nm, 1)], Y[(nm, 2)]
    if a == E.ZERO and b == E.ZERO:
        return "zero"
    if b == a:
        return "even"
    if b == E.scal(Fr(-1), a):
        return "odd"
    return "gen"


def reality_type(z, conj):
    if z == E.ZERO:
        return "0"
    zc = conj(z)
    if zc == z:
        return "real"
    if zc == E.scal(Fr(-1), z):
        return "imag"
    return "gen"


LATTICE = {(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 1)}


def classify_point(Xcls, t1, tL):
    """The stage-2 derivation as an executable case table.

    Inputs: the conj3-reality class of X(1) and the c3-flip types of the two window
    pairs.  Output: the predicted 4-bit vanishing pattern, or None when the point
    falls outside the derivation's premises (an odd window = L5a violation, or a
    purely imaginary X = N1 violation) -- expected never.
    Proof obligations discharged in FINDINGS.md: given Xbar + R + N1 + L5a,
      p dead <=> t1 = zero;  r dead <=> t1 = zero or (t1 = even and X real);
      q dead <=> tL = zero;  s dead <=> tL = zero or (tL = even and X real);
    and X = 0 or (t1 = tL = zero) kills everything.
    """
    if t1 == "odd" or tL == "odd" or Xcls == "imag":
        return None
    if Xcls == "0" or (t1 == "zero" and tL == "zero"):
        return (1, 1, 1, 1)
    real = (Xcls == "real")
    if t1 == "zero":
        p, r = 1, 1
    elif t1 == "even":
        p, r = 0, (1 if real else 0)
    else:
        p, r = 0, 0
    if tL == "zero":
        q, s = 1, 1
    elif tL == "even":
        q, s = 0, (1 if real else 0)
    else:
        q, s = 0, 0
    return (p, q, r, s)


def descent_analysis(m1, m2, ch=None, check_master_against=None):
    """Run the full descent machinery for a pair from LOCAL data (+ optional checks).

    ch: a banked/global channel table {(a,b): (p,q,r,s)} to check the XY formula
        against (grids from ch must equal the XY combos). If None, grids are BUILT
        from the local closed form (pure prediction mode).
    check_master_against: a global C-table {(j,l): elt} to verify the master identity.
    """
    loc3, loc5 = build_locals(m1, m2)
    d1, d2, C3 = loc3
    e1, e2, C5 = loc5
    assert 12 % d1 == 0 and 12 % d2 == 0, ("3-side period outside scope", d1, d2)
    assert 30 % e1 == 0 and 30 % e2 == 0, ("5-side period outside scope", e1, e2)
    T, o1, o2 = closed_form_ttable(loc3, loc5)
    ch_local = channel_tables(T, o1, o2)
    if ch is None:
        ch = ch_local
    grids = ft_grids(ch, o1, o2)

    rep = {"pair": [m1, m2], "orders": [o1, o2], "periods3": [d1, d2], "periods5": [e1, e2],
           "d_divides_4": (4 % d1 == 0 and 4 % d2 == 0)}

    # cell censuses: the N1 premise (mu6-valued 3-side) + the 5-side value kinds
    rep["C3_cells_mu6_or_zero"] = all(v == E.ZERO or v in MU6 for v in C3.values())
    kinds = Counter()
    for v in C5.values():
        if v == E.ZERO:
            kinds["zero"] += 1
        elif any(v == E.zeta(k) for k in range(60)):
            kinds["root_of_unity"] += 1
        else:
            kinds["other"] += 1
    rep["C5_cell_kinds"] = dict(kinds)

    # (M) the master identity against a global C-table, when supplied
    BAS = [E.ONE, E.SQRT5, E.SQRTm3, E.SQRTm15]
    if check_master_against is not None:
        CH = [lambda c: 1, chi5, chim3, lambda c: chi5(c) * chim3(c)]
        bad = 0
        for x in range(o1):
            for y in range(o2):
                for i in range(4):
                    acc = E.ZERO
                    for c in G60:
                        ci = pow(c, -1, 60)
                        acc = E.add(acc, E.scal(Fr(CH[i](c)),
                                                SC.sigma(check_master_against[((ci * x) % o1, (ci * y) % o2)], c)))
                    if E.mul(grids[i][(x, y)], BAS[i]) != E.scal(Fr(1, 16), acc):
                        bad += 1
        rep["master_identity_mismatches"] = bad
        rep["master_identity_checks"] = 4 * o1 * o2

    # the pointwise sweep: (S) XY formula, (X0/Xbar), (N1), the window censuses,
    # (L5a/L5b), the zero stratum, the s-law, and the (CLS) classifier
    xy_bad = 0
    x0_bad, xconj_bad = 0, 0
    n1_viol = 0
    l5a_viol, l5b_viol = 0, 0
    w_census = Counter()
    r_census = Counter()
    zero_equiv_bad = 0
    s_law_bad = 0
    cls_bad, cls_skip = 0, 0
    patterns = {}
    for x in range(o1):
        for y in range(o2):
            u, v, X, Y = xy_data(loc3, loc5, o1, o2, x, y)
            combos = xy_combos(X, Y)
            for i in range(4):
                if E.mul(grids[i][(x, y)], BAS[i]) != E.scal(Fr(1, 16), combos[i]):
                    xy_bad += 1
            # (X0) the coset collapse X(1) = u + v; (Xbar) X(2) = conj3(X(1))
            if X[1] != E.add(u, v):
                x0_bad += 1
            if X[2] != conj3(X[1]):
                xconj_bad += 1
            pat = pattern_of(grids, x, y)
            patterns[(x, y)] = pat
            # (N1): X purely imaginary nonzero?
            Xcls = reality_type(X[1], conj3)
            if Xcls == "imag":
                n1_viol += 1
            # window censuses + L5a/L5b
            t1, tL = window_type(Y, "1"), window_type(Y, "L")
            w_census[(t1, tL)] += 1
            r_census[(reality_type(Y[("1", 1)], conj5), reality_type(Y[("L", 1)], conj5))] += 1
            if t1 == "odd" or tL == "odd":
                l5a_viol += 1
            if tL not in ("zero", t1):
                l5b_viol += 1
            # zero-stratum equivalence: all-dead <=> X = 0 or Y-quadruple = 0
            x_dead = (X[1] == E.ZERO)
            y_dead = all(Y[k] == E.ZERO for k in Y)
            if (pat == (1, 1, 1, 1)) != (x_dead or y_dead):
                zero_equiv_bad += 1
            # the s-law: s alive => all four alive
            if pat[3] == 0 and pat != (0, 0, 0, 0):
                s_law_bad += 1
            # (CLS): the type-level classifier must reproduce the observed pattern
            pred = classify_point(Xcls, t1, tL)
            if pred is None:
                cls_skip += 1
            elif pred != pat:
                cls_bad += 1
    rep["xy_formula_mismatches"] = xy_bad
    rep["xy_formula_checks"] = 4 * o1 * o2
    rep["X0_collapse_violations"] = x0_bad
    rep["Xbar_conj_violations"] = xconj_bad
    rep["N1_violations"] = n1_viol
    rep["window_census"] = {f"{k[0]},{k[1]}": n for k, n in sorted(w_census.items())}
    rep["window_reality_census"] = {f"{k[0]},{k[1]}": n for k, n in sorted(r_census.items())}
    rep["L5a_odd_violations"] = l5a_viol
    rep["L5b_matching_violations"] = l5b_viol
    rep["zero_stratum_equivalence_failures"] = zero_equiv_bad
    rep["s_law_failures"] = s_law_bad
    rep["classifier_mismatches"] = cls_bad
    rep["classifier_skips"] = cls_skip

    # (QM) at table level
    qm_eq, qm_conj, qm_fail = 0, 0, 0
    for j in range(d1):
        for l in range(d2):
            uu = C3[(j, l)]
            vv = C3[((-j) % d1, (-l) % d2)]
            if (j - l) % 2 == 0:
                qm_eq += (vv == uu)
                qm_fail += (vv != uu)
            else:
                qm_conj += (vv == conj3(uu))
                qm_fail += (vv != conj3(uu))
    rep["QM_equal_branch"] = qm_eq
    rep["QM_conj_branch"] = qm_conj
    rep["QM_failures"] = qm_fail

    # the P68 gates: localized versions + the level-15 gates through the tensor
    # identity (the character-gate roles of stage 2b; all report-only censuses)
    def Amat(m, q):
        return [[(1 + m * m) % q, m % q], [m % q, 1 % q]]

    def mm2(a, b, q):
        return [[(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % q,
                 (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % q],
                [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % q,
                 (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % q]]

    def det_gI(m1_, m2_, j, l, q):
        g = [[1 % q, 0], [0, 1 % q]]
        for _ in range(j):
            g = mm2(g, Amat(m1_, q), q)
        for _ in range(l):
            g = mm2(g, Amat(m2_, q), q)
        return ((-g[0][0] - 1) * (-g[1][1] - 1) - g[0][1] * g[1][0]) % q

    gate3_bad, gate3_dom = 0, 0
    for j in range(d1):
        for l in range(d2):
            d3 = det_gI(m1, m2, j, l, 3)
            if d3 == 0:
                continue
            gate3_dom += 1
            cell = C3[(j, l)]
            is_real = (conj3(cell) == cell)
            if (chim3(d3) == 1) != is_real:
                gate3_bad += 1
    rep["gate3_local_domain"] = gate3_dom
    rep["gate3_local_violations"] = gate3_bad
    # the NAIVE 5-side localization of P68 L3 (kept as a census: it has genuine
    # counterexamples on (1,3), (1,4), (2,4), (4,7) -- see FINDINGS)
    gate5_bad, gate5_dom = 0, 0
    for j in range(e1):
        for l in range(e2):
            d5 = det_gI(m1, m2, j, l, 5)
            if d5 == 0:
                continue
            gate5_dom += 1
            cell = C5[(j, l)]
            in_Qsqrt5 = (conj5(cell) == cell)   # fixed by zeta5 -> zeta5^4 <=> in Q(sqrt5)
            if chi5(d5) == -1 and in_Qsqrt5 and cell != E.ZERO:
                gate5_bad += 1
    rep["gate5_local_naive_domain"] = gate5_dom
    rep["gate5_local_naive_violations"] = gate5_bad
    # the level-15 gates (B404/P68 verbatim domain: det(gamma'-I) in (Z/15)^x),
    # with the cell built from the LOCAL tables via the tensor identity
    g15_dom = g15_nonroot = g15_l2 = g15_l3 = 0
    ZK60 = [E.zeta(k) for k in range(60)]
    for j in range(o1):
        for l in range(o2):
            d15 = det_gI(m1, m2, j, l, 15)
            if gcd(d15, 15) != 1:
                continue
            g15_dom += 1
            cell = E.mul(C3[(j % d1, l % d2)], C5[(j % e1, l % e2)])
            k = next((kk for kk in range(60) if cell == ZK60[kk]), None)
            if k is None:
                g15_nonroot += 1
                continue
            order = 60 // gcd(k, 60)
            if (chim3(d15) == 1) == (order % 3 == 0):    # L2: 3|ord <=> chi_-3 = -1
                g15_l2 += 1
            if chi5(d15) == -1 and order % 5 != 0:       # L3: chi5 = -1 forces 5|ord
                g15_l3 += 1
    rep["gate15_domain"] = g15_dom
    rep["gate15_nonroot"] = g15_nonroot
    rep["gate15_L2_violations"] = g15_l2
    rep["gate15_L3_violations"] = g15_l3

    # pattern tiers
    cnt = Counter(patterns.values())
    rep["tier_counts"] = {"".join(map(str, k)): n for k, n in sorted(cnt.items())}
    rep["lattice_only"] = set(cnt) <= LATTICE
    rep["node_Q_sqrt_minus15_absent"] = all(
        not (k[1] == 1 and k[2] == 1 and k[3] == 0) for k in cnt)
    return rep, ch_local, patterns


# the lemmas the stage-2 derivation CONSUMES -- these must be violation-free on
# every pair for the duel to stand; the gates are report-only observations
UNIVERSAL_KEYS = ("xy_formula_mismatches", "X0_collapse_violations", "Xbar_conj_violations",
                  "N1_violations", "L5a_odd_violations", "zero_stratum_equivalence_failures",
                  "classifier_mismatches", "classifier_skips", "QM_failures")


# ---------------- serialization ----------------
def canon_channels(ch):
    return {f"{a},{b}": [str(x) for x in v] for (a, b), v in sorted(ch.items())}


def table_hash(ch):
    return hashlib.sha256(json.dumps(canon_channels(ch), sort_keys=True).encode()).hexdigest()


def s_summary(ch):
    scells = {k: v[3] for k, v in ch.items() if v[3] != 0}
    return {
        "bright": bool(scells),
        "n_s_cells": len(scells),
        "s_value_set": sorted({str(x) for x in scells.values()}),
        "sum_s_squared": str(sum((x * x for x in scells.values()), Fr(0))),
    }


# ---------------- phases ----------------
def phase_control():
    t0 = time.time()
    out = {"phase": "control", "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    # C1: the six banked pair tables, cell-exact, from LOCAL data only (closed form)
    banked = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))
    pair_ok = {}
    ch_cache = {}
    for key, tab in sorted(banked.items()):
        m1, m2 = map(int, key.split(","))
        loc3, loc5 = build_locals(m1, m2)
        T, o1, o2 = closed_form_ttable(loc3, loc5)
        ch = channel_tables(T, o1, o2)
        ch_cache[(m1, m2)] = ch
        want = {tuple(map(int, k.split(","))): tuple(Fr(x) for x in v) for k, v in tab.items()}
        pair_ok[key] = (ch == want)
        print(f"  control C1: pair ({m1},{m2}) closed-form == banked table: {ch == want} "
              f"({len(ch)} nonzero cells)", flush=True)
    out["banked_pairs_cell_exact"] = pair_ok
    out["banked_pairs_all_ok"] = all(pair_ok.values())

    # C2: bright/dark 12/12 (the twelve banked pairs, P67) + the (2,5) out-of-sample
    # precedent = 13/13, from LOCAL data only, against the banked verdicts; the s-cell
    # counts must also match the banked global counts.
    crit = json.load(open(os.path.join(HERE, "..", "B390_criterion_tensor", "criterion.json")))
    oos = json.load(open(os.path.join(HERE, "..", "B390_criterion_tensor", "out_of_sample_25.json")))
    verdicts = {k: (v["status"], v["n_s_cells"]) for k, v in crit.items()}
    verdicts["2,5"] = (oos["verdict"], len(oos["s_cells"]))
    bd_ok = {}
    for key, (status, n_s) in sorted(verdicts.items()):
        m1, m2 = map(int, key.split(","))
        if (m1, m2) not in ch_cache:
            loc3, loc5 = build_locals(m1, m2)
            T, o1, o2 = closed_form_ttable(loc3, loc5)
            ch_cache[(m1, m2)] = channel_tables(T, o1, o2)
        ss = s_summary(ch_cache[(m1, m2)])
        pred = "bright" if ss["bright"] else "dark"
        bd_ok[key] = (pred == status and ss["n_s_cells"] == n_s)
        print(f"  control C2: pair ({m1},{m2}) local closed-form says {pred} "
              f"({ss['n_s_cells']} s-cells); banked {status} ({n_s}): "
              f"{'OK' if bd_ok[key] else 'MISS'}", flush=True)
    out["brightdark_matches"] = bd_ok
    n12 = sum(bd_ok[k] for k in bd_ok if k != "2,5")
    out["brightdark_tally_banked12"] = f"{n12}/12"
    out["brightdark_tally_with_oos"] = f"{sum(bd_ok.values())}/{len(bd_ok)}"

    # C3: the flagship t(0,4) of (golden, silver) = (1,2), two routes
    flag_banked = SC.double_one("C_theta.json", 0, 4)
    flag_local = ch_cache[(1, 2)].get((0, 4))
    out["flagship_banked_route"] = [str(x) for x in flag_banked]
    out["flagship_local_route"] = [str(x) for x in flag_local]
    out["flagship_ok"] = (tuple(flag_banked) == SC.FLAGSHIP == tuple(flag_local))
    print(f"  control C3: flagship t(0,4) = {out['flagship_local_route']} "
          f"(= -1/48 - (1/80)sqrt5 - (1/48)sqrt-3 + (1/48)sqrt-15) ok={out['flagship_ok']}",
          flush=True)

    # D: the descent chain on all twelve banked pairs; (1,2) additionally gets the
    # master-identity check against the banked global C-table (C_theta.json)
    data = json.load(open(os.path.join(HERE, "..", "B358_seam_certification", "C_theta.json")))
    Cglob = {(j, l): [Fr(s) for s in data["C"][j][l]] for j in range(20) for l in range(12)}
    reps = {}
    for key in sorted(verdicts):
        if key == "2,5":
            continue
        m1, m2 = map(int, key.split(","))
        kw = {"ch": ch_cache[(m1, m2)]}
        if (m1, m2) == (1, 2):
            kw["check_master_against"] = Cglob
        rep, _, _ = descent_analysis(m1, m2, **kw)
        reps[key] = rep
        extra = (f"master {rep['master_identity_mismatches']}/{rep['master_identity_checks']} bad; "
                 if "master_identity_mismatches" in rep else "")
        print(f"  descent ({m1},{m2}): {extra}xy {rep['xy_formula_mismatches']}/"
              f"{rep['xy_formula_checks']} bad; X0 {rep['X0_collapse_violations']}; "
              f"Xbar {rep['Xbar_conj_violations']}; N1 {rep['N1_violations']}; "
              f"QM fail {rep['QM_failures']}; L5a {rep['L5a_odd_violations']}; "
              f"L5b {rep['L5b_matching_violations']}; cls {rep['classifier_mismatches']}"
              f"+{rep['classifier_skips']}skip; tiers {rep['tier_counts']}", flush=True)
    out["descent_reports"] = reps

    # the scoreboard: the CONSUMED universal lemmas must be violation-free on every
    # pair; L5b is allowed to fail (it is the pair-specific residue) and its
    # per-pair status is recorded; the P68 gates are report-only observations.
    out["universal_lemmas_clean"] = all(
        all(rep.get(k, 0) == 0 for k in UNIVERSAL_KEYS) and rep["C3_cells_mu6_or_zero"]
        for rep in reps.values())
    out["L5b_by_pair"] = {k: reps[k]["L5b_matching_violations"] for k in reps}
    out["lattice_only_by_pair"] = {k: reps[k]["lattice_only"] for k in reps}
    out["node_absent_all_pairs"] = all(rep["node_Q_sqrt_minus15_absent"] for rep in reps.values())
    out["gate3_local_clean_all_pairs"] = all(rep["gate3_local_violations"] == 0
                                             for rep in reps.values())
    out["gate15_L1_L2_clean_all_pairs"] = all(
        rep["gate15_nonroot"] == 0 and rep["gate15_L2_violations"] == 0 for rep in reps.values())
    out["gate15_L3_by_pair"] = {k: reps[k]["gate15_L3_violations"] for k in reps}
    out["gate5_local_naive_by_pair"] = {k: reps[k]["gate5_local_naive_violations"] for k in reps}
    print(f"  scoreboard: consumed universal lemmas clean on 12/12: "
          f"{out['universal_lemmas_clean']}; L5b violations by pair: {out['L5b_by_pair']}; "
          f"Q(sqrt-15) node absent on all pairs: {out['node_absent_all_pairs']}", flush=True)
    print(f"  gates: 3-side local Eisenstein clean 12/12: {out['gate3_local_clean_all_pairs']}; "
          f"level-15 L1+L2 clean 12/12: {out['gate15_L1_L2_clean_all_pairs']}; "
          f"level-15 chi5-gate (L3) violations by pair: {out['gate15_L3_by_pair']} "
          f"(P68 L3 is (1,2)-specific); naive 5-side localization violations: "
          f"{out['gate5_local_naive_by_pair']}", flush=True)

    # the B459/P1 lattice law on (1,2)
    rep12 = reps["1,2"]
    out["p1_law_ok"] = (rep12["lattice_only"] and rep12["node_Q_sqrt_minus15_absent"]
                        and rep12["tier_counts"] == {"0000": 120, "0011": 20, "0101": 20,
                                                     "0111": 10, "1111": 70})
    print(f"  the B459/P1 law on (1,2): tiers {rep12['tier_counts']} "
          f"lattice-only={rep12['lattice_only']} node-absent="
          f"{rep12['node_Q_sqrt_minus15_absent']} -> p1_law_ok={out['p1_law_ok']}", flush=True)

    out["control_pass"] = (out["banked_pairs_all_ok"] and n12 == 12
                           and all(bd_ok.values()) and out["flagship_ok"]
                           and out["universal_lemmas_clean"] and out["p1_law_ok"])
    out["elapsed_s"] = round(time.time() - t0, 1)
    json.dump(out, open(os.path.join(HERE, "b493_control.json"), "w"), indent=1)
    print(f"control {'PASS' if out['control_pass'] else 'FAIL -- DUEL INVALID'} "
          f"in {out['elapsed_s']}s -> b493_control.json", flush=True)
    if not out["control_pass"]:
        raise SystemExit("CONTROL FAILED -- the duel is invalid per the prereg")
    return out


def phase_predict():
    """Pair (4,7) -- LOCAL data only. No global (4,7) object is built here."""
    t0 = time.time()
    out = {"phase": "predict", "pair": [4, 7],
           "committed_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "note": "computed from the q=3 and q=5 local theta models ALONE, before any "
                   "global (4,7) computation exists in the repo (absence grep-verified: "
                   "the banked pairs with seed 7 are (1,7),(2,7),(3,7) only)."}
    rep, ch_local, patterns = descent_analysis(4, 7, ch=None)
    out["descent_4_7_local"] = rep
    out["prediction"] = {
        "channels": canon_channels(ch_local),
        "table_sha256": table_hash(ch_local),
        "s": s_summary(ch_local),
        "tier_counts": rep["tier_counts"],
        "lattice_only": rep["lattice_only"],
        "node_absent": rep["node_Q_sqrt_minus15_absent"],
    }
    s = out["prediction"]["s"]
    print(f"  PREDICTION for (4,7): {'BRIGHT' if s['bright'] else 'DARK'}; "
          f"n_s_cells={s['n_s_cells']}; sum s^2 = {s['sum_s_squared']}; "
          f"values {s['s_value_set']}", flush=True)
    print(f"  PREDICTION tier table: {out['prediction']['tier_counts']}; "
          f"lattice-only={out['prediction']['lattice_only']}; "
          f"Q(sqrt-15) node absent={out['prediction']['node_absent']}", flush=True)
    print(f"  table sha256 = {out['prediction']['table_sha256']}", flush=True)
    out["elapsed_s"] = round(time.time() - t0, 1)
    json.dump(out, open(os.path.join(HERE, "b493_prediction_47.json"), "w"), indent=1)
    print(f"predict done in {out['elapsed_s']}s -> b493_prediction_47.json", flush=True)
    return out


def phase_verify():
    """The global (4,7) table via the banked B367 machinery; compare with the prediction."""
    t0 = time.time()
    pred = json.load(open(os.path.join(HERE, "b493_prediction_47.json")))
    out = {"phase": "verify", "pair": [4, 7],
           "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "prediction_committed_utc": pred["committed_utc"]}

    W1 = build_theta_W(4)
    W2 = build_theta_W(7)
    o1, p1 = matrix_order(W1)
    o2, p2 = matrix_order(W2)
    out["global_orders"] = [o1, o2]
    print(f"  global W4, W7 built; orders ({o1},{o2}) [{time.time()-t0:.0f}s]", flush=True)

    # G1: the tensor identity on all global cells (P66/P67 extended out-of-sample)
    loc3, loc5 = build_locals(4, 7)
    d1, d2, C3 = loc3
    e1, e2, C5 = loc5
    g1_bad = 0
    Cglob = {}
    for j in range(o1):
        for l in range(o2):
            cell = par_trace(p1[j], p2[l])
            Cglob[(j, l)] = cell
            if cell != E.mul(C3[(j % d1, l % d2)], C5[(j % e1, l % e2)]):
                g1_bad += 1
    out["G1_tensor_mismatches"] = g1_bad
    print(f"  G1 tensor identity on (4,7): {g1_bad}/{o1*o2} mismatches [{time.time()-t0:.0f}s]",
          flush=True)

    # the global t-table (banked route: pair_smatrix)
    ch_glob = pair_smatrix(p1, p2)
    out["global_table_sha256"] = table_hash(ch_glob)
    out["global_s"] = s_summary(ch_glob)
    print(f"  global table: {'BRIGHT' if out['global_s']['bright'] else 'DARK'}; "
          f"n_s_cells={out['global_s']['n_s_cells']}; sum s^2={out['global_s']['sum_s_squared']} "
          f"[{time.time()-t0:.0f}s]", flush=True)

    # the full descent machinery against the GLOBAL table + the master identity
    # against the fresh global C -- the strongest out-of-sample form of (M)+(T)+(S)
    rep, _, _ = descent_analysis(4, 7, ch=ch_glob, check_master_against=Cglob)
    out["descent_4_7_global"] = rep
    print(f"  descent (4,7) vs global: master {rep['master_identity_mismatches']}/"
          f"{rep['master_identity_checks']} bad; xy {rep['xy_formula_mismatches']}/"
          f"{rep['xy_formula_checks']} bad; cls {rep['classifier_mismatches']} "
          f"[{time.time()-t0:.0f}s]", flush=True)

    # the comparison
    p = pred["prediction"]
    out["match_table_hash"] = (out["global_table_sha256"] == p["table_sha256"])
    out["match_table_cells"] = (canon_channels(ch_glob) == p["channels"])
    out["match_brightdark"] = (out["global_s"]["bright"] == p["s"]["bright"])
    out["match_s_summary"] = (out["global_s"] == p["s"])
    out["match_tiers"] = (rep["tier_counts"] == p["tier_counts"])
    out["all_match"] = (all(out[k] for k in
                            ("match_table_hash", "match_table_cells", "match_brightdark",
                             "match_s_summary", "match_tiers"))
                        and g1_bad == 0 and rep["master_identity_mismatches"] == 0
                        and rep["xy_formula_mismatches"] == 0)
    print(f"  MATCH: table hash {out['match_table_hash']}; cells {out['match_table_cells']}; "
          f"bright/dark {out['match_brightdark']}; s-summary {out['match_s_summary']}; "
          f"tiers {out['match_tiers']}; G1 {g1_bad == 0}", flush=True)
    print(f"  OUT-OF-SAMPLE VERDICT: {'HIT' if out['all_match'] else 'MISS'}", flush=True)

    out["elapsed_s"] = round(time.time() - t0, 1)
    json.dump(out, open(os.path.join(HERE, "b493_verify_47.json"), "w"), indent=1)
    print(f"verify done in {out['elapsed_s']}s -> b493_verify_47.json", flush=True)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["control", "predict", "verify", "all"])
    args = ap.parse_args()
    if args.phase in ("control", "all"):
        phase_control()
    if args.phase in ("predict", "all"):
        phase_predict()
    if args.phase in ("verify", "all"):
        phase_verify()
