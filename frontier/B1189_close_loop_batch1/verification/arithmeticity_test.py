#!/usr/bin/env python3
"""GC-1 (3): the commensurability question, own code, no sage.

Criterion used (Maclachlan-Reid, "The Arithmetic of Hyperbolic 3-Manifolds",
Thm 8.3.2 / Thm 3.3.4): a finite-covolume Kleinian group Gamma = pi_1(M) (M
cusped, orientable, hence torsion-free) is ARITHMETIC iff
  (i)  the invariant trace field k(Gamma) is an imaginary quadratic field, and
  (ii) tr(gamma) is an algebraic integer for every gamma in Gamma.
Reid's theorem (noncompact case): the invariant quaternion algebra of any
NONCOMPACT arithmetic Kleinian group is automatically M_2(k) -- so for cusped
arithmetic manifolds COMMENSURABILITY CLASS = INVARIANT TRACE FIELD, no
quaternion-algebra computation needed.

Independent reduction used here (not asserted, computed): every member of
members_B has ALL tetrahedron shapes in Q(sqrt(-3)) by the B1186 definition;
since holonomy matrix entries (via SnapPy's fundamental_group().SL2C, built
from the gluing solution) are algebraic functions of the shapes, the trace
field is CONTAINED in Q(sqrt(-3)); a genuinely hyperbolic (non-elementary)
representation cannot have trace field = Q (traces would then all be real,
forcing every generator to be loxodromic-with-real-trace or parabolic with
trace +-2, impossible for a discrete non-elementary group acting on H^3 with
more than one loxodromic axis direction) -- so trace field = Q(sqrt(-3))
EXACTLY. This script does not re-derive that reduction abstractly; instead it
DIRECTLY VERIFIES, numerically at 50 dps, that sampled traces (i) lie in
Q(sqrt(-3)) to 1e-40, confirming containment/exactness on the sample, and
(ii) are algebraic integers of Z[omega], omega=(1+sqrt(-3))/2 -- criterion (ii)
above, checked member-by-member.

Sample: ALL 35 non-regular members (the open case) + 5 regular members (m004,
m003, s955 if present, t12840, plus one more) as a POSITIVE CONTROL of the
method itself, + 5 non-family manifolds as a NEGATIVE CONTROL (traces should
fail to reconstruct as elements of Q(sqrt(-3)) at all, or fail integrality).
"""
import json
from fractions import Fraction
import snappy
import mpmath as mp

mp.mp.dps = 50
SQ3 = mp.sqrt(3)
MAXDEN = 400  # generous; traces of short words in small hyperbolic groups have small denominators

FAM = "/Users/dri/origin-axiom/frontier/B1186_family_is_112/verification/family_census.json"


def reconstruct_Qsqrtm3(z, maxden=MAXDEN, tol=mp.mpf(10) ** -35):
    """z = a + b*sqrt(-3), a,b rational. Returns (a,b) as Fractions, or None if
    z cannot be matched to a rational pair at this denominator bound/tolerance."""
    a = z.real
    b = z.imag / SQ3
    fa = Fraction(float(a)).limit_denominator(maxden)
    fb = Fraction(float(b)).limit_denominator(maxden)
    # verify at HIGH precision (not just double round-trip)
    are = mp.mpf(fa.numerator) / fa.denominator
    bre = mp.mpf(fb.numerator) / fb.denominator
    if abs(are - a) < tol and abs(bre - b) < tol:
        return fa, fb
    return None


def is_Zomega_integral(fa, fb):
    """x = a + b*sqrt(-3) is in Z[omega] (omega=(1+sqrt-3)/2, ring of integers of
    Q(sqrt-3)) iff writing x = m + n*omega (m,n in Z): n = 2b in Z, m = a-b in Z."""
    n = fa.denominator  # placeholder, real check below
    two_b = 2 * fb
    m = fa - fb
    n_is_int = (two_b.denominator == 1)
    m_is_int = (m.denominator == 1)
    return n_is_int and m_is_int, (m if m_is_int else None), (two_b if n_is_int else None)


def sample_traces(name, words=("a", "b", "aB", "ab", "aab")):
    """Return list of (word^2 label, tr(gamma^2)-as-mpc) for a manifold's holonomy
    rep, high precision. USES SQUARED WORDS (gamma^2 = word+word), per
    Maclachlan-Reid Thm 8.3.2's precise arithmeticity criterion: the criterion is
    stated for tr(gamma^2), NOT tr(gamma) -- squaring removes the SL(2,C)-vs-
    PSL(2,C) lift-sign ambiguity, which otherwise pushes tr(gamma) itself into a
    (generically) DEGREE-2 EXTENSION of the invariant trace field kGamma. This was
    caught in-cell: an earlier version of this script tested tr(gamma) directly and
    wrongly flagged known family members (e.g. o9_41001) as NOT_IN_Qsqrtm3; tr(a^2)
    for o9_41001 lands exactly on -sqrt(-3) (denominator 1), resolving it."""
    M = snappy.Manifold(name).high_precision()
    G = M.fundamental_group()
    gens = set(G.generators())
    out = []
    for w in words:
        if not all(c.lower() in gens for c in w):
            continue
        try:
            mat = G.SL2C(w + w)  # gamma^2
        except Exception:
            continue
        tr = mat[0][0] + mat[1][1]
        re = mp.mpf(str(tr.real).replace(" ", ""))
        im = mp.mpf(str(tr.imag).replace(" ", ""))
        out.append((w + "^2", mp.mpc(re, im)))
    return out


def analyze_manifold(name):
    rows = []
    for w, tr in sample_traces(name):
        rec = reconstruct_Qsqrtm3(tr)
        if rec is None:
            rows.append({"word": w, "trace": mp.nstr(tr, 12), "in_Qsqrtm3": False})
            continue
        fa, fb = rec
        integral, m, n = is_Zomega_integral(fa, fb)
        rows.append({"word": w, "trace": mp.nstr(tr, 12),
                     "in_Qsqrtm3": True, "a": str(fa), "b": str(fb),
                     "integral_Z_omega": integral,
                     "m_plus_n_omega": (f"{m} + {n}*omega" if integral else None)})
    return rows


def verdict_for(name):
    rows = analyze_manifold(name)
    if not rows:
        return "NO_DATA", rows
    all_in_field = all(r["in_Qsqrtm3"] for r in rows)
    if not all_in_field:
        return "NOT_IN_Qsqrtm3", rows
    all_integral = all(r["integral_Z_omega"] for r in rows)
    return ("ARITHMETIC_CONSISTENT" if all_integral else "IN_FIELD_BUT_NON_INTEGRAL_SAMPLE"), rows


def main():
    fam = json.load(open(FAM))
    members_A = set(fam["members_A"])
    members_B = set(fam["members_B"])
    non_regular = sorted(members_B - members_A)

    print(f"testing ALL {len(non_regular)} non-regular members (open case)")
    results = {}
    for name in non_regular:
        v, rows = verdict_for(name)
        results[name] = {"verdict": v, "rows": rows}
        print(f"  {name:>14s}: {v}  (n_traces_sampled={len(rows)})")

    n_ok = sum(1 for r in results.values() if r["verdict"] == "ARITHMETIC_CONSISTENT")
    print(f"\n{n_ok}/{len(non_regular)} non-regular members: ARITHMETIC_CONSISTENT "
          f"(invariant-trace-field sample in Q(sqrt-3), traces integral in Z[omega])")

    print("\n--- POSITIVE CONTROL (regular / already-classical members) ---")
    pos_names = ["m004", "m003", "t12840", "o9_41001", "o10_150684"]
    pos_results = {}
    for name in pos_names:
        v, rows = verdict_for(name)
        pos_results[name] = v
        print(f"  {name:>14s}: {v}")

    print("\n--- NEGATIVE CONTROL (non-family manifolds; shapes NOT in Q(sqrt-3)) ---")
    neg_names = ["m015", "m006", "m007", "m009", "m010"]
    neg_results = {}
    for name in neg_names:
        v, rows = verdict_for(name)
        neg_results[name] = v
        print(f"  {name:>14s}: {v}")

    out = {"non_regular_results": {k: v["verdict"] for k, v in results.items()},
           "non_regular_full": results,
           "positive_control": pos_results,
           "negative_control": neg_results,
           "n_arithmetic_consistent_of_non_regular": n_ok,
           "n_non_regular": len(non_regular)}
    json.dump(out, open("arithmeticity_test_output.json", "w"), indent=1)
    print("\nDONE")


if __name__ == "__main__":
    main()
