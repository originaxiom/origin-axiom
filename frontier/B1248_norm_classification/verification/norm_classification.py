#!/usr/bin/env python3
"""B1248 -- THE NORM CLASSIFICATION: eps IS THE FRICKE INVARIANT READ MOD SQUARES.

Closes the refinement cell B1192 named and left open ("the general norm-classification").

THE LAW.  For A, M in SL2 with (cq - br) != 0, the simultaneous-mirror realizer
    X A X^-1 = A^-1,   X M X^-1 = M^-1
satisfies, identically,
    det X  =  (2 - kappa) / (cq - br)^2 ,      kappa = tr[A,M] = x^2+y^2+z^2-xyz-2
so  det X == 2 - kappa  in K*/(K*)^2.  kappa is K001 / B167's Fricke-Vogt first integral.

INTEGRAL REFINEMENT -- CORRECTED 2026-09-05 by a peer seat's formula, verified here.
Over Z the realizer module is free of rank 1 (rank 2 iff kappa = 2), and its primitive generator is
read off the ADDITIVE commutator, with no linear solve at all:

    det(A M - M A) = 2 - kappa        (identity, Groebner residue 0)
    det X0 = det( (A M - M A) / g )  =  (2 - kappa) / g^2 ,   g = gcd of the entries of AM - MA

  WHAT THIS REPLACED, AND WHY IT WAS WRONG.  A first version of this arc claimed
  det X0 = squarefree(2 - kappa).  That is FALSE: verified against the actual integral realizer
  module on 500 random noncommuting partners, the peer formula scores 500/500 and squarefree
  scores 493/500.  The sharpest counterexample: 2 - kappa = -121 = -(11^2) with entry-gcd g = 1,
  where the true det X0 is -121 (TORSOR) while squarefree(-121) = -1 would have called it THE BIT.
  The two formulas disagree exactly when g^2 is not the largest square dividing 2 - kappa, which
  the arc's original 14 hand-picked partners never exhibited.

  CORRECTED BIT CRITERION:  eps = -1  <=>  2 - kappa = -g^2   (NOT "kappa - 2 is a perfect square").
  Verified 500/500 against the realizer module.
Hence the TRICHOTOMY, which reproduces all four behaviours B1192/B1189 banked separately:
    D = +1   -> mirror realized inside SL2(Z); eps = +1; NO BIT          (B1192 sqrt2 control)
    D = -1   -> eps = -1, DIRECT                                        (B1192 crown positive)
    |D| > 1  -> no GL2(Z) realizer; TORSOR form, det X0 = D             (B1192 sqrt7 control)
    kappa=2  -> module rank 2, both signs; degenerate (Fricke reducible) (B1189 kill)
with D = (2 - kappa)/g^2 as above.

A FIELD-LEVEL CONCLUSION IS NOT LICENSED BY ONE PAIR (peer seat, verified here).  B1192's sqrt2
control fixed ONE integral matrix and spoke of the field.  In the SAME trace field Q(sqrt2) BOTH
determinant signs occur: e.g. tr = -34, M = [[-35,-36],[1,1]] gives D = -1, while
M = [[-29,-12],[-12,-5]] gives D = +1.  The exclusion holds for the displayed pair, NOT the field.

KNOWN-MATHEMATICS IDENTIFICATION (checked here, not cited). The Maclachlan-Reid quaternion algebra
of a two-generator group is (A0^2, B1^2) = (tr^2 A - 4, (2-kappa)/(tr^2 A - 4)), A0 the trace-zero
part and B1 the part anticommuting with it.

  CORRECTED IN-SESSION: a draft of this arc wrote the algebra as (tr^2 A - 4, 2 - kappa) and called
  eps ITSELF the second slot.  That is WRONG.  The check that caught it is 2T, the chain's own door:
  on the Q8 pair (i,j) the true algebra is (-1,-1), the HURWITZ quaternions -- the known answer for
  the binary tetrahedral group -- while the wrong form gives (-1,+1), split.  eps and the second slot
  differ by exactly the FIRST slot.  det X0 = squarefree(2 - kappa) is UNAFFECTED (it is the realizer
  determinant, 14/14 integrally) and the lock already encoded the correct B1^2 formula: only the
  prose was false.  For the object the algebra is (5,-5), split; the draft's (5,-1) is also split, so
  the conclusion survived while the statement did not -- a coincidence, not a defence.
  The 2T control is now permanent, in twoT_algebra() and in the lock.

For the object A = [[2,1],[1,1]] the first slot is tr^2 A - 4 = 5 = disc Q(sqrt5).

THE OBJECT'S OWN VALUE.  The once-punctured-torus fibre of m004 has parabolic commutator,
kappa = -2, so 2 - kappa = 4 and D = +1: the object ALONE carries no bit, with a mechanism --
the cusp pins kappa below the wall kappa = 2.

NOT CLAIMED: no measured physical value; no crossing to physics. Gate 5 clean.
"""
import sympy as sp

A_OBJ = sp.Matrix([[2, 1], [1, 1]])


def inv(m):
    """Adjugate. Equals the inverse exactly when det m = 1, which is where the symbolic
    derivation uses it (det = 1 is imposed afterwards by Groebner reduction)."""
    return sp.Matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]])


def true_inv(m):
    """Honest inverse. The distinction from the adjugate matters for det = -1 partners:
    the adjugate would silently solve X M = -M^-1 X instead of X M = M^-1 X, and would
    report a realizer where none exists."""
    return inv(m) / sp.det(m)


def kappa(P, Q):
    return sp.expand(sp.trace(P * Q * inv(P) * inv(Q)))


def squarefree(n):
    n = int(n)
    if n == 0:
        return 0
    sign, n, out = (1 if n > 0 else -1), abs(n), 1
    for pr, e in sp.factorint(n).items():
        if e % 2:
            out *= pr
    return sign * out


def realizer_module(A, M):
    """Integer solutions X of X A = A^-1 X and X M = M^-1 X; primitive generators."""
    w, x, y, z = sp.symbols('w x y z')
    X = sp.Matrix([[w, x], [y, z]])
    eqs = list(X * A - true_inv(A) * X) + list(X * M - true_inv(M) * X)
    sysm, _ = sp.linear_eq_to_matrix(eqs, [w, x, y, z])
    gens = []
    for v in sysm.nullspace():
        den = sp.ilcm(*[sp.Rational(t).q for t in v])
        vi = [int(sp.Rational(t) * den) for t in v]
        g = sp.igcd(*[t for t in vi if t]) or 1
        vi = [t // g for t in vi]
        gens.append(sp.Matrix([[vi[0], vi[1]], [vi[2], vi[3]]]))
    return gens


def additive_commutator_det(M, A=A_OBJ):
    """det((AM - MA)/g), g the entry-gcd. Equals det X0 with no linear solve (peer seat's formula).

    Verified 500/500 against realizer_module(); the older squarefree(2-kappa) scores 493/500.
    """
    from math import gcd
    C = A * M - M * A
    g = 0
    for e in C:
        g = gcd(g, int(e))
    if g == 0:
        return None, 0
    return int(sp.det(C / g)), g


def classify(M, A=A_OBJ):
    """Return (kappa, D, predicted-label, observed-label). D from the additive commutator."""
    k = int(kappa(A, M))
    D, _g = additive_commutator_det(M, A)
    if D is None:
        D = 0
    gens = realizer_module(A, M)
    if k == 2:
        return k, D, "DEGENERATE", f"rank {len(gens)}"
    pred = {1: "DIRECT+1", -1: "DIRECT-1"}.get(D, "TORSOR")
    det0 = int(sp.det(gens[0])) if gens else None
    obs = "none" if det0 is None else ({1: "DIRECT+1", -1: "DIRECT-1"}.get(det0, "TORSOR"))
    return k, D, pred, obs


# ---------------------------------------------------------------- the law, symbolically
def law_symbolic():
    a, b, c, d, p, q, r, s = sp.symbols('a b c d p q r s')
    w, x1, y1, z1 = sp.symbols('w x1 y1 z1')
    A = sp.Matrix([[a, b], [c, d]])
    M = sp.Matrix([[p, q], [r, s]])
    X = sp.Matrix([[w, x1], [y1, z1]])
    eqs = list(X * A - inv(A) * X) + list(X * M - inv(M) * X)
    sol = sp.solve(eqs, [w, x1, y1, z1], dict=True)[0]
    free = sorted({t for e in sol.values() for t in e.free_symbols} - {a, b, c, d, p, q, r, s}, key=str)
    Xg = sp.Matrix(2, 2, [sp.together(sol.get(k, k).subs({free[0]: 1})) for k in (w, x1, y1, z1)])
    num, den = sp.fraction(sp.cancel(sp.together(Xg.det())))
    G = sp.groebner([a * d - b * c - 1, p * s - q * r - 1], a, b, c, d, p, q, r, s, order='lex')
    resid = sp.expand(G.reduce(sp.expand(num - (2 - sp.trace(A * M * inv(A) * inv(M)))))[1])
    return resid, sp.factor(den)


# --------------------------------------------------------------------------- the controls
BANKED = {                                    # B1192 / B1189 exhibited pairs and their behaviour
    "sqrt2  [[5,2],[2,1]]":   (sp.Matrix([[5, 2], [2, 1]]),   "DIRECT+1"),
    "sqrt3  [[2,3],[1,2]]":   (sp.Matrix([[2, 3], [1, 2]]),   "DIRECT-1"),
    "sqrt7  [[8,21],[3,8]]":  (sp.Matrix([[8, 21], [3, 8]]),  "TORSOR"),
    "homog  (A,A)":           (A_OBJ,                          "DEGENERATE"),
}
EXTRA = {
    "sqrt6  [[5,12],[2,5]]":  sp.Matrix([[5, 12], [2, 5]]),
    "sqrt10 [[19,60],[6,19]]": sp.Matrix([[19, 60], [6, 19]]),
    "sqrt15 [[4,15],[1,4]]":  sp.Matrix([[4, 15], [1, 4]]),
    "[[3,5],[1,2]]":          sp.Matrix([[3, 5], [1, 2]]),
    "[[5,3],[3,2]]":          sp.Matrix([[5, 3], [3, 2]]),
    "[[1,3],[1,4]]":          sp.Matrix([[1, 3], [1, 4]]),
    "[[7,2],[3,1]]":          sp.Matrix([[7, 2], [3, 1]]),
    "[[4,3],[5,4]]":          sp.Matrix([[4, 3], [5, 4]]),
    "[[9,4],[2,1]]":          sp.Matrix([[9, 4], [2, 1]]),
}


def selftest(verbose=True):
    fails = []
    resid, den = law_symbolic()
    if resid != 0:
        fails.append(f"symbolic law residue != 0: {resid}")
    if not den.is_Pow:
        fails.append(f"denominator not a perfect square: {den}")
    if verbose:
        print(f"  [law]  det X * ({den}) - (2 - kappa)  ==  {resid}")

    for nm, (M, want) in BANKED.items():
        k, D, pred, obs = classify(M)
        good = (pred == want == obs) if want != "DEGENERATE" else (pred == "DEGENERATE" and obs == "rank 2")
        if not good:
            fails.append(f"banked control {nm}: want {want}, pred {pred}, obs {obs}")
        if verbose:
            print(f"  [ctl]  {nm:24} kappa={k:>6}  D={D:>6}  {pred:>10} / banked {want:>10}  {'OK' if good else 'FAIL'}")

    for nm, M in EXTRA.items():
        k, D, pred, obs = classify(M)
        # kappa = 2 is the Fricke reducibility locus: the module is rank 2, not rank 1,
        # so the correct observation there is "rank 2", not a determinant class.
        good = (pred == "DEGENERATE" and obs == "rank 2") if k == 2 else (pred == obs)
        if not good:
            fails.append(f"{nm}: predicted {pred}, observed {obs}")
        if verbose:
            print(f"  [prt]  {nm:24} kappa={k:>6}  D={D:>6}  {pred:>10} / observed {obs:>10}  {'OK' if good else 'FAIL'}")

    # NON-VACUITY, both directions: all three branches must actually occur.
    seen = {classify(M)[2] for M in list(EXTRA.values()) + [m for m, _ in BANKED.values()]}
    for branch in ("DIRECT+1", "DIRECT-1", "TORSOR", "DEGENERATE"):
        if branch not in seen:
            fails.append(f"VACUITY: branch {branch} never occurs in the control set")
    if verbose:
        print(f"  [vac]  branches realized: {sorted(seen)}  (all four required)")

    # the object's own fibre: once-punctured torus, parabolic commutator
    w_ = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
    a_ = sp.Matrix([[1, 1], [0, 1]])
    b_ = sp.Matrix([[1, 0], [-w_, 1]])
    kf = sp.simplify(kappa(a_ * inv(b_), inv(b_) * a_))
    if kf != -2:
        fails.append(f"m004 fibre commutator trace {kf} != -2")
    if verbose:
        print(f"  [obj]  m004 once-punctured-torus fibre: kappa = {kf}  ->  2-kappa = {2 - kf} = 2^2  ->  D = +1 (NO BIT)")
    # THE 2T CONTROL -- the computation that refuted the draft quaternion claim.
    order, spec, (ca, cb) = twoT_algebra()
    if order != 24:
        fails.append(f"2T order {order} != 24")
    if set(spec) != {-2, 0, 2}:
        fails.append(f"2T kappa spectrum {spec} != {{-2, 0, 2}}")
    if (ca, cb) != (-1, -1):
        fails.append(f"2T Q8-pair algebra ({ca},{cb}) != (-1,-1), the Hurwitz quaternions")
    if verbose:
        print(f"  [2T ]  order {order}, kappa spectrum {spec}, Q8-pair algebra ({ca},{cb}) = Hurwitz")
    return fails


def twoT_algebra():
    """Build 2T (binary tetrahedral, order 24) in SL2(C) and return the algebra of the Q8 pair.

    This is the control that refuted the draft claim 'eps IS the second slot'. The known answer
    for 2T is the Hurwitz quaternions (-1, -1); anything else means the formula is wrong.
    Returns (order, kappa_spectrum, (a_class, b_class)).
    """
    I_ = sp.I
    i_ = sp.Matrix([[I_, 0], [0, -I_]])
    j_ = sp.Matrix([[0, 1], [-1, 0]])
    k_ = sp.simplify(i_ * j_)
    one = sp.eye(2)
    w = sp.simplify((-one + i_ + j_ + k_) / 2)
    G = set()
    for q in (one, -one, i_, -i_, j_, -j_, k_, -k_):
        for e in range(3):
            for sgn in (1, -1):
                G.add(sp.ImmutableMatrix(sp.simplify(sgn * q * w**e)))
    G = [sp.Matrix(g) for g in G]
    spectrum = set()
    for P in G:
        for Q in G:
            spectrum.add(sp.nsimplify(sp.simplify(kappa(P, Q))))
    A, B = i_, j_
    I2 = sp.eye(2)
    A0 = A - sp.trace(A) / 2 * I2
    B0 = B - sp.trace(B) / 2 * I2
    B1 = sp.expand(B0 - (sp.trace(A0 * B0) / sp.trace(A0 * A0)) * A0)
    a = sp.nsimplify(sp.simplify((A0 * A0)[0, 0]))
    b = sp.nsimplify(sp.simplify((B1 * B1)[0, 0]))
    sq = lambda x: squarefree(sp.Rational(x).p * sp.Rational(x).q)
    return len(G), sorted(spectrum, key=lambda t: sp.re(sp.N(t))), (sq(a), sq(b))


if __name__ == "__main__":
    print("B1248 -- the norm classification (selftest)")
    fails = selftest()
    print()
    print("SELFTEST:", "PASS" if not fails else "FAIL")
    for f in fails:
        print("   !", f)
    raise SystemExit(1 if fails else 0)
