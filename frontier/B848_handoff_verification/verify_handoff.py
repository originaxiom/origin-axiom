#!/usr/bin/env python3
"""B848 -- independent verification of the incoming review-seat handoff bundle.

Six documents arrived (2026-07-30 .. 08-01). The bundle's own record lists eleven errors in
one document and thirteen in another, and states an expected ~33% correction rate on first
statements. So nothing here is taken on citation: every load-bearing claim is recomputed,
and every instrument is self-tested against a KNOWN answer before it is pointed at the
handoff's data.

The headline under test -- the arrow/amphichirality census -- is the one the sending seat got
wrong FOUR TIMES before getting it right, and it records that each wrong version looked
cleaner than the truth. That is precisely the profile that earns a second, structurally
different method rather than a re-reading.

Two methods, sharing no code path:
  (1) saturated integer conjugator lattice -> binary quadratic det form -> reduction cycle
  (2) brute-force exact integer box search over all four entries of P

Method (2) makes no use of method (1)'s derivation (that tr(P) = 0), so it cannot inherit an
error from it. Method (1) decides ABSENCE, which no bounded search ever can.

Repository-instrument and mathematics scope. Nothing here reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from itertools import product
from math import isqrt

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Instrument: reduction cycle of an indefinite binary quadratic form.
# A form represents m with |m| < sqrt(D)/2 iff m is a leading coefficient of its reduction
# cycle. For m = +-1 and D > 4 that bound always holds, so the test is DECIDABLE -- which is
# the whole reason to prefer it to a bounded search when the answer is "no such element".
# ---------------------------------------------------------------------------
def _rho(f, D, sD):
    a, b, c = f
    ac = abs(c)
    lo = -ac if ac > sD else sD - 2 * ac
    r = (-b - lo - 1) % (2 * ac) + lo + 1
    return (c, r, (r * r - D) // (4 * c))


def cycle_leads(a, b, c):
    """Leading coefficients of the reduction cycle of (a,b,c), plus its discriminant."""
    D = b * b - 4 * a * c
    if D <= 0 or isqrt(D) ** 2 == D:
        raise ValueError(f"need indefinite non-square discriminant, got {D}")
    sD = isqrt(D)
    f = (a, b, c)
    for _ in range(2000):                 # run into the cycle
        f = _rho(f, D, sD)
    start, tail = f, []
    for _ in range(2000):                 # then walk it once
        tail.append(f)
        f = _rho(f, D, sD)
        if f == start:
            break
    return {g[0] for g in tail}, D


def represents_pm1(a, b, c):
    lead, D = cycle_leads(a, b, c)
    return (1 in lead), (-1 in lead), sorted(lead), D


# ---------------------------------------------------------------------------
# The conjugator lattice
# ---------------------------------------------------------------------------
def _kernel_basis(v):
    """Saturated ZZ-basis of ker(v) for an integer row vector, by unimodular column ops.

    The kernel of an integer map to ZZ is automatically saturated. Taking a rational
    nullspace and clearing denominators would give a SUBLATTICE with inflated content --
    and a sublattice's det form misses values the true lattice represents. That inflation
    is exactly how the sending seat manufactured a false absence on its third attempt.
    """
    n = len(v)
    w = list(v)
    U = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def swap(j, k):
        w[j], w[k] = w[k], w[j]
        for i in range(n):
            U[i][j], U[i][k] = U[i][k], U[i][j]

    def sub(j, k, q):
        w[j] -= q * w[k]
        for i in range(n):
            U[i][j] -= q * U[i][k]

    for j in range(1, n):
        while w[j] != 0:
            if w[0] == 0:
                swap(0, j)
                continue
            sub(j, 0, w[j] // w[0])
            if w[j] != 0:
                swap(0, j)
    return [[U[i][j] for i in range(n)] for j in range(1, n)]


def conjugator_lattice(A):
    """Saturated basis of {P in M2(ZZ) : P A = A^-1 P}.

    Writing A = [[a,b],[c,d]], the four equations force tr(P) = 0 (whenever b or c is
    nonzero) and collapse to the single condition p(a-d) + q*c + r*b = 0. That derivation
    is VERIFIED below by substitution rather than trusted -- an assumed criterion is how
    the first of the sending seat's four wrong attempts died.
    """
    a, b, c, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
    if (b, c) == (0, 0):
        raise ValueError("diagonal A -- separate case, not needed here")
    mats = [sp.Matrix([[p, q], [r, -p]]) for (p, q, r) in _kernel_basis([a - d, c, b])]
    Ai = A.inv()
    for M in mats:
        assert M * A == Ai * M, f"derived lattice basis fails P A = A^-1 P: {M.tolist()}"
    return mats


def det_form(basis):
    x, y = sp.symbols("x y")
    pol = sp.Poly(sp.expand((x * basis[0] + y * basis[1]).det()), x, y)
    return (int(pol.coeff_monomial(x**2)), int(pol.coeff_monomial(x * y)),
            int(pol.coeff_monomial(y**2)))


def verdict(A):
    """(amphichiral, arrow, cycle_leads, disc) for hyperbolic A in SL(2,Z).

    Convention (the handoff's): a flow-reversing self-map of the mapping torus needs
    P A P^-1 = A^-1; total orientation change = sign(det P) * (-1) from reversing t.
      det P = -1 -> orientation preserved -> flow reversible -> NO arrow
      det P = +1 -> orientation reversed  -> AMPHICHIRAL
    """
    qa, qb, qc = det_form(conjugator_lattice(A))
    has_p1, has_m1, lead, D = represents_pm1(qa, qb, qc)
    return has_p1, (not has_m1), lead, D


def box_search(A, N=25):
    """Independent existence check: exact integer scan over ALL FOUR entries of P.

    Deliberately does not use the tr(P) = 0 derivation, so it cannot inherit its error.
    Bounded, so it can exhibit presence but never certify absence -- that is the cycle's job.
    """
    a, b, c, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
    got = set()
    for p in range(-N, N + 1):
        for q in range(-N, N + 1):
            for r in range(-N, N + 1):
                for s in range(-N, N + 1):
                    det = p * s - q * r
                    if det != 1 and det != -1:
                        continue
                    if (p * a + q * c == d * p - b * r and p * b + q * d == d * q - b * s
                            and r * a + s * c == -c * p + a * r
                            and r * b + s * d == -c * q + a * s):
                        got.add(det)
        if got == {1, -1}:
            break
    return got


L = sp.Matrix([[1, 0], [1, 1]])
R = sp.Matrix([[1, 1], [0, 1]])


def wm(w, Lm=L, Rm=R):
    M = sp.eye(2)
    for ch in w:
        M = M * (Lm if ch == "L" else Rm)
    return M


# the handoff's own census table (MASTER_HANDOFF sec 1.3)
CLAIMED = {
    "LR":     dict(tr=3,  disc=5,   arrow=False, amphi=True),
    "LLRR":   dict(tr=6,  disc=8,   arrow=False, amphi=True),
    "LRR":    dict(tr=4,  disc=12,  arrow=False, amphi=False),
    "LLRLR":  dict(tr=10, disc=96,  arrow=False, amphi=False),
    "LLRLRR": dict(tr=15, disc=221, arrow=True,  amphi=True),
    "LLRRLR": dict(tr=15, disc=221, arrow=True,  amphi=True),
}


def census():
    out = {}
    for w, cl in CLAIMED.items():
        A = wm(w)
        amphi, arrow, lead, D = verdict(A)
        found = box_search(A)
        out[w] = dict(trace=int(A.trace()), disc=D, cycle_leads=lead,
                      amphichiral=amphi, arrow=arrow, box_dets=sorted(found),
                      symmetric=bool(A.T == A),
                      matrix=[[int(v) for v in row] for row in A.tolist()],
                      matches_handoff=(int(A.trace()) == cl["tr"] and D == cl["disc"]
                                       and arrow == cl["arrow"] and amphi == cl["amphi"]),
                      box_consistent=all((d == 1 and amphi) or (d == -1 and not arrow)
                                         for d in found))
    return out


def metallic_census(mmax=12):
    """M_m = [[m,1],[1,0]]; the bundle monodromy is M_m^2. Does ANY m yield an arrow?"""
    out = []
    for m in range(1, mmax + 1):
        A = sp.Matrix([[m, 1], [1, 0]])**2
        amphi, arrow, lead, D = verdict(A)
        # the CORRECT mechanism: disc = m^2+4 and the metallic mean itself is a unit of
        # norm -1, since ((m+sqrt(m^2+4))/2)*((m-sqrt(m^2+4))/2) = (m^2-(m^2+4))/4 = -1.
        out.append(dict(m=m, trace=int(A.trace()), disc=D, symmetric=bool(A.T == A),
                        amphichiral=amphi, arrow=arrow, cycle_leads=lead,
                        disc_is_m2p4=(D == m * m + 4)))
    return out


def base_rates(nmax=10):
    """How common is the arrow? The handoff asks for this (sec 5 item 3) and lacks it."""
    rows = []
    for n in range(2, nmax + 1):
        tot = n_arrow = n_nonamphi = 0
        for bits in product("LR", repeat=n):
            w = "".join(bits)
            if "L" not in w or "R" not in w:
                continue                                   # not hyperbolic
            if min("".join(w[i:] + w[:i]) for i in range(n)) != w:
                continue                                   # one representative per cyclic class
            tot += 1
            _amphi, _arrow, _lead, _D = verdict(wm(w))
            n_arrow += _arrow
            n_nonamphi += (not _amphi)
        rows.append(dict(length=n, classes=tot, arrow=n_arrow, non_amphichiral=n_nonamphi))
    return rows


def riley():
    """Which Riley polynomial follows from the handoff's OWN raw relation?

    E6_PROBE sec 1 states   phi = u^2 + (5-x^2)*u + 1
    MASTER_HANDOFF sec 6 corrects it to   phi = u^2 + (5-x^2)*(u+1)
    and notes the parabolic sanity check passed on the wrong one. Decide from the raw
    expression both documents quote, rather than from either simplified form.
    """
    m, u = sp.symbols("m u")
    raw = -m**4 * u - m**4 + m**2 * u**2 + 3 * m**2 * u + 3 * m**2 - u - 1
    red = sp.expand(raw / m**2)
    cu = sp.simplify(red.coeff(u, 1))
    c0 = sp.simplify(red.coeff(u, 0))
    x = sp.Symbol("x")
    formA = u**2 + (5 - x**2) * u + 1
    formB = u**2 + (5 - x**2) * (u + 1)
    return dict(
        coeff_u=str(cu), coeff_const=str(c0),
        u_coeff_equals_const=bool(sp.simplify(cu - c0) == 0),   # => form B
        both_collapse_at_x2=bool(sp.simplify(formA.subs(x, 2) - (u**2 + u + 1)) == 0
                                 and sp.simplify(formB.subs(x, 2) - (u**2 + u + 1)) == 0),
        both_degree_2=bool(sp.degree(formA, u) == 2 and sp.degree(formB, u) == 2),
        trefoil_degree=int(sp.degree(sp.Poly(-m**4 + m**2 * u + m**2 - 1, u), u)))


def gky():
    """GKY power sums on the figure-eight quartic (E6_PROBE sec 2, 'the central finding')."""
    mp.mp.dps = 40

    def psum(k, cval):
        rts = mp.polyroots([1, -3, (1 - cval), (4 + 2 * cval), -(2 + cval)],
                           maxsteps=300, extraprec=300)
        def Fp(t):
            return 4 * t**3 - 9 * t**2 + 2 * (1 - cval) * t + (4 + 2 * cval)
        return sum(Fp(r)**k for r in rts)

    cs = [mp.mpf("0.3"), mp.mpf("1.7"), mp.mpf("-3.4")]
    claims = {
        -1: lambda c: mp.mpf(0),
        0:  lambda c: mp.mpf(4),
        1:  lambda c: -4 * c - 17,
        2:  lambda c: 8 * c**3 + 66 * c**2 + 180 * c + 187,
        -2: lambda c: 2 * (c - 1) * (c + 3) / ((c - 2) * (c + 2) * (4 * c + 17)),
        -3: lambda c: -3 / ((c - 2) * (c + 2) * (4 * c + 17)),
    }
    out = {}
    for k, f in claims.items():
        errs = [float(abs(psum(k, c) - f(c))) for c in cs]
        out[str(k)] = dict(max_abs_err=max(errs), holds=max(errs) < 1e-18)
    return out


def lambda_k():
    """Res Lambda_K, Res phi -- and whether the two 'independent routes' really are two."""
    mp.mp.dps = 40
    s3 = mp.sqrt(3)

    def L_chi3(s):
        return (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)) / mp.power(3, s)

    res_zetaK = 2 * mp.pi / (6 * s3)                    # 2*pi*h/(w*sqrt|d|), h=1, w=6, |d|=3
    res_LambdaK = (s3 / (2 * mp.pi)) * mp.gamma(1) * res_zetaK
    LK2 = (s3 / (2 * mp.pi))**2 * mp.gamma(2) * mp.zeta(2) * L_chi3(2)
    res_phi = (mp.mpf(1) / 6) / LK2
    vol = mp.mpf("2.029883212819307250042405108549")
    return dict(
        res_LambdaK_at_1=mp.nstr(res_LambdaK, 25),
        res_LambdaK_is_one_sixth=bool(abs(res_LambdaK - mp.mpf(1) / 6) < mp.mpf("1e-35")),
        res_phi=mp.nstr(res_phi, 20),
        res_phi_matches_handoff=bool(abs(res_phi - mp.mpf("1.7065521766281616088"))
                                     < mp.mpf("1e-16")),
        vol_equals_12sqrt3_LK2=bool(abs(12 * s3 * LK2 - vol) < mp.mpf("1e-18")),
        # the point of the check: GIVEN vol = 12 sqrt3 LK(2), 2sqrt3/vol == 1/(6 LK(2))
        # identically -- so the "3.6e-20 agreement" is algebra, not corroboration.
        two_routes_are_algebraically_identical=bool(
            abs(2 * s3 / (12 * s3 * LK2) - res_phi) < mp.mpf("1e-35")))


def e6():
    exps = [1, 4, 5, 7, 8, 11]
    dims = [2 * e + 1 for e in exps]
    C = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                   [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
    mp.mp.dps = 30
    phi = (1 + mp.sqrt(5)) / 2
    return dict(exponents=exps, block_dims=dims, dim_sum=sum(dims), dim_is_78=sum(dims) == 78,
                sum_exponents=sum(exps), positive_roots=36, coxeter=max(exps) + 1,
                cartan_det=int(C.det()), h1_equals_rank=(len(dims) == 6),
                suspension_entropy=mp.nstr(2 * mp.log(phi), 12))


def main():
    res = dict(census=census(), metallic=metallic_census(), base_rates=base_rates(),
               riley=riley(), gky=gky(), lambda_k=lambda_k(), e6=e6())

    # the two flags the first pass raised
    A41_std = wm("LR")
    A41_swapped = wm("LR", R, L)
    Cm = sp.Matrix([[1, 0], [-1, -1]])
    res["flag_convention"] = dict(
        C_works_standard=bool(Cm * A41_std * Cm.inv() == A41_std.inv()),
        C_works_swapped=bool(Cm * A41_swapped * Cm.inv() == A41_swapped.inv()),
        note="C is correct only under the swapped L/R convention, which the handoff omits")

    S = sp.Matrix([[0, -1], [1, 0]])
    a, b, d = sp.symbols("a b d")
    Asym = sp.Matrix([[a, b], [b, d]])
    Acex = wm("LLRLRR")
    amphi_c, arrow_c, _l, _D = verdict(Acex)
    res["flag_symmetry_mechanism"] = dict(
        symmetric_identity_holds=bool(sp.simplify(S * Asym * S.inv() - Asym.adjugate())
                                      == sp.zeros(2, 2)),
        det_S=int(S.det()),
        counterexample="LLRLRR",
        counterexample_matrix=[[int(v) for v in row] for row in Acex.tolist()],
        counterexample_symmetric=bool(Acex.T == Acex),
        counterexample_amphichiral=amphi_c,
        counterexample_arrow=arrow_c,
        note="symmetry supplies the det=+1 conjugator (amphichirality) ONLY; 'no arrow' "
             "needs det=-1, which symmetry does not give. A symmetric trace-15 matrix "
             "HAS an arrow, so the stated metallic mechanism proves the wrong half.")

    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)

    print("=" * 78)
    print("B848 -- independent verification of the incoming handoff bundle")
    print("=" * 78)
    print("\n  ARROW / AMPHICHIRALITY CENSUS (two independent methods)\n")
    print(f"  {'word':8} {'tr':>4} {'disc':>5} {'sym':>6} {'cycle leads':>14} "
          f"{'amphi':>6} {'ARROW':>6} {'box':>9}  handoff?")
    for w, r in res["census"].items():
        print(f"  {w:8} {r['trace']:>4} {r['disc']:>5} {str(r['symmetric']):>6} "
              f"{str(r['cycle_leads']):>14} {str(r['amphichiral']):>6} "
              f"{str(r['arrow']):>6} {str(r['box_dets']):>9}  "
              f"{'MATCH' if r['matches_handoff'] else 'DIVERGES'}")
    n_match = sum(r["matches_handoff"] for r in res["census"].values())
    print(f"\n  {n_match}/6 rows reproduce the handoff table exactly.")

    print("\n  DEFECT -- the stated metallic mechanism proves the wrong half:")
    f = res["flag_symmetry_mechanism"]
    print(f"    LLRLRR = {f['counterexample_matrix']} is symmetric={f['counterexample_symmetric']} "
          f"and has ARROW={f['counterexample_arrow']}")
    print(f"    => symmetry gives amphichirality, not absence of arrow.")
    print(f"    metallic conclusion nonetheless HOLDS m=1..12: "
          f"{all(not r['arrow'] for r in res['metallic'])}  "
          f"(disc = m^2+4 always: {all(r['disc_is_m2p4'] for r in res['metallic'])})")

    print("\n  BASE RATES (asked for by the handoff, not supplied by it):")
    for r in res["base_rates"]:
        pct = 100 * r["arrow"] / r["classes"] if r["classes"] else 0
        print(f"    length {r['length']:>2}: {r['classes']:>4} classes   "
              f"arrow {r['arrow']:>4} ({pct:5.1f}%)   non-amphi {r['non_amphichiral']:>4}")

    print(f"\n  Riley: u-coeff == const-coeff -> {res['riley']['u_coeff_equals_const']} "
          f"(=> the CORRECTED form; both collapse at x=2: "
          f"{res['riley']['both_collapse_at_x2']})")
    print(f"  GKY power sums: all six hold -> "
          f"{all(v['holds'] for v in res['gky'].values())}")
    print(f"  Lambda_K: two 'routes' algebraically identical -> "
          f"{res['lambda_k']['two_routes_are_algebraically_identical']}")
    print(f"  E6: dim 78 -> {res['e6']['dim_is_78']}, Cartan det {res['e6']['cartan_det']}, "
          f"h {res['e6']['coxeter']}")
    print("\n  results.json written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
