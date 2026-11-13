#!/usr/bin/env python3
"""The paired current pole on main, step 1 of the plan (P-749 (e)): the constant 7/(2 l^2), from the operator's form.

WHAT IS TAKEN FROM THE LANE (read through the binding-minimum mask; statements, no code):
  the vector operator is P_v = 2 k^dagger k with k = (Dbar_A, ad q, ad r)   [its proof on the charged vectors, eq. (3)];
  q = E_+/(2 l), r = E_-/(2 l), E_+ and E_- the raising operators of two commuting sl2 with H = H_+ + H_-, and the
  grade mu = m + n is the eigenvalue of H/2                                  [its single-mode proof, section 2];
  the charged vectors' coefficient is V(3/2) x V(3/2) under the two sl2      [the paired-pole proof, section 2].
WHAT MAIN COMPUTES, exactly (fractions), with matrices of its own for V(3/2):
  the potential 2 (ad q^dagger ad q + ad r^dagger ad r) = (1/(2 l^2)) (F_+ E_+ + F_- E_-) on every weight vector;
  that the grade -2 plane is an eigenspace with the value 7/(2 l^2) (so a profile with Dbar z = 0 there is an
  eigenvector of P_v with that value);
  that the other form, (1/(2 l^2)) (E_+ F_+ + E_- F_-), which is what compact conjugation carries the first to, has the
  same value at the opposite weights, vector by vector: so the two charges' spectra match term by term;
  that the two forms differ by (1/(2 l^2)) (H_+ + H_-) = mu / l^2, the curvature's term.
HOW IT COULD FAIL: the plane not an eigenspace; the value not 7/2; the planted case with V(1/2) x V(1/2)."""
import itertools, json, pathlib
from fractions import Fraction as Fr
import sympy as sp
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:220]) if detail else ""))
def sl2(j2):
    """E, F, H on V(j), j = j2/2, basis m = j, j-1, ..., -j; unitary: F = E^dagger"""
    j = sp.Rational(j2, 2); ms = [j - k for k in range(j2 + 1)]; n = len(ms)
    E = sp.zeros(n); F = sp.zeros(n); H = sp.diag(*[2 * m for m in ms])
    for a, m in enumerate(ms):
        if a + 1 < n:                                   # F |m> = sqrt(j(j+1) - m(m-1)) |m-1>
            c = sp.sqrt(j * (j + 1) - m * (m - 1)); F[a + 1, a] = c; E[a, a + 1] = c
    return E, F, H, ms
def table(j2):
    E, F, H, ms = sl2(j2)
    assert sp.simplify(E * F - F * E - H) == sp.zeros(len(ms)) and E.T == F
    FE = sp.simplify(F * E); EF = sp.simplify(E * F)
    assert FE.is_diagonal() and EF.is_diagonal()
    fe = {m: FE[a, a] for a, m in enumerate(ms)}; ef = {m: EF[a, a] for a, m in enumerate(ms)}
    return ms, fe, ef
ms, fe, ef = table(3)
pot = {(m, n): (fe[m] + fe[n]) / 2 for m in ms for n in ms}      # in units of 1/l^2: (1/2)(FE + FE)
pot2 = {(m, n): (ef[m] + ef[n]) / 2 for m in ms for n in ms}
by_grade = {}
for (m, n), v in pot.items(): by_grade.setdefault(m + n, []).append(v)
for mu in sorted(by_grade): print("  grade %+d: %s" % (mu, sorted(by_grade[mu])))
plane = [(m, n) for (m, n) in pot if m + n == -2]
check("the grade -2 plane of V(3/2) x V(3/2) is two-dimensional: (-3/2, -1/2) and (-1/2, -3/2)", sorted(plane) == sorted([(sp.Rational(-3, 2), sp.Rational(-1, 2)), (sp.Rational(-1, 2), sp.Rational(-3, 2))]))
check("on it the potential is the one number 7/2, in units of 1/l^2: the lane's 7/(2 l^2)", all(pot[p] == sp.Rational(7, 2) for p in plane), [pot[p] for p in plane])
check("it is no other grade's whole value: only the grade -2 plane is an eigenspace with 7/2 among the grades of dimension two or more", [mu for mu, v in by_grade.items() if len(v) >= 2 and set(v) == {sp.Rational(7, 2)}] == [-2], {str(mu): [str(x) for x in sorted(v)] for mu, v in by_grade.items()})
check("the conjugate form (E F in place of F E) has the same value at the opposite weights, vector by vector, on all 16", all(pot2[(-m, -n)] == pot[(m, n)] for (m, n) in pot))
check("the two forms differ by the grade: (E F - F E)/2 summed is mu, on all 16 (the curvature's term mu / l^2)", all(pot2[(m, n)] - pot[(m, n)] == m + n for (m, n) in pot))
check("so on the grade +2 plane the conjugate form gives 7/2 as well", all(pot2[(-m, -n)] == sp.Rational(7, 2) for (m, n) in plane))
# planted: the same computation on V(1/2) x V(1/2) must not give 7/2 anywhere
ms1, fe1, ef1 = table(1)
check("planted: on V(1/2) x V(1/2) no weight has the value 7/2", all((fe1[m] + fe1[n]) / 2 != sp.Rational(7, 2) for m in ms1 for n in ms1), sorted({str((fe1[m] + fe1[n]) / 2) for m in ms1 for n in ms1}))
if __name__ == "__main__":                              # the write only when run, never when a lock loads it
    json.dump({"potential in units of 1/l^2, by (m, n)": {"%s,%s" % k: str(v) for k, v in pot.items()}, "checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]},
              open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
    print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
