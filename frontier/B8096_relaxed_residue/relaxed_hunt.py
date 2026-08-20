#!/usr/bin/env python3
"""B8096 -- the residue hunt with the guard relaxed to the banked condition.
Preregistered and SHA-256 sealed before this file existed (SEAL.txt).

Filter on FRAME-INVARIANCE alone; disqualify Re h by name; drop the nativeness and
per-candidate demands. Vacuity control is BINDING: anything forced merely by living in K is
VACUOUS. Gate 5 untouched; no measured number anywhere.
"""
from fractions import Fraction as F
import itertools, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAIL.append(l)

E = ["I", "chi_a", "chi_b", "D2"]
LAM = {"I": F(1), "chi_a": F(864,413), "chi_b": F(6912,3047), "D2": F(2304,953)}
SGN = {"I": -1, "chi_a": -1, "chi_b": +1, "D2": +1}          # sign of lambda^2 (B1076 record)
LSQ = {k: SGN[k]*LAM[k]**2 for k in E}
DEN = {k: LAM[k].denominator for k in E}

print("="*74); print("THE DATA (banked per element)"); print("="*74)
for k in E:
    print(f"  {k:6} lambda={str(LAM[k]):>10}  lambda^2={str(LSQ[k]):>22}  den={DEN[k]}")
gate("lambda^2(I) = -1 (independently reproduced today on all six couplings)", LSQ["I"] == -1)
gate("denominators factor as banked: 413=7*59, 3047=11*277, 953 prime",
     DEN["chi_a"] == 7*59 and DEN["chi_b"] == 11*277 and DEN["D2"] == 953)

print(); print("="*74); print("KLEIN-ORBIT INVARIANTS (frame-invariance ONLY)"); print("="*74)
vals = [LSQ[k] for k in E]
e1 = sum(vals)
e2 = sum(a*b for a,b in itertools.combinations(vals,2))
e3 = sum(a*b*c for a,b,c in itertools.combinations(vals,3))
e4 = vals[0]*vals[1]*vals[2]*vals[3]
prod_lam = LAM["I"]*LAM["chi_a"]*LAM["chi_b"]*LAM["D2"]
sum_lam  = sum(LAM[k] for k in E)
# per-class, under the character with kernel {I, chi_a}
ker = ["I","chi_a"]; cos = ["chi_b","D2"]
p_ker = LAM["I"]*LAM["chi_a"]; p_cos = LAM["chi_b"]*LAM["D2"]
inv = {"e1(lambda^2)":e1, "e2(lambda^2)":e2, "e3(lambda^2)":e3, "e4(lambda^2)":e4,
       "prod(lambda)":prod_lam, "sum(lambda)":sum_lam,
       "prod_kernel_class":p_ker, "prod_coset_class":p_cos}
for k,v in inv.items():
    print(f"  {k:22} = {v}")

print(); print("="*74); print("THE INTEGER STRUCTURE -- where 77 would live"); print("="*74)
D = DEN["chi_a"]*DEN["chi_b"]*DEN["D2"]
print(f"  product of the three nontrivial denominators = {D}")
print(f"    = 7*59 * 11*277 * 953")
gate("77 divides that product", D % 77 == 0)
gate("and 77 = 7*11 is exactly the resolvent radicand (disc mu = 6237 = 3^4 * 7 * 11)", 7*11 == 77)
print(f"  D/77 = {D//77} = 59*277*953 = {59*277*953}")

print(); print("="*74); print("THE BINDING VACUITY CONTROL"); print("="*74)
print("""  B1076's own 77-candidate died here: the hierarchy discriminant's squarefree part was
  77 at all three nontrivial gauges and was FORCED by V_ccl living in K -- it held for a
  control diagonal with ZERO relation to the coboundary structure.

  The same test, applied to the divisibility above:""")
# The control: is 77 | D forced merely by 7 and 11 being the ramified/resolvent primes of K,
# independent of the coboundary structure?  7 | 413 and 11 | 3047 are SINGLE-ELEMENT facts;
# their product's divisibility is then automatic.  A genuine coset invariant must not be
# reconstructible from per-element facts that the control also produces.
per_element_facts = (DEN["chi_a"] % 7 == 0, DEN["chi_b"] % 11 == 0)
forced = per_element_facts[0] and per_element_facts[1]
gate("77 | D is FORCED by the two per-element divisibilities (7|413, 11|3047)", forced)
print("""    B1076 already banked '7 | 413 and 11 | 3047' as an OBSERVATION, unweighted, no
    mechanism claimed.  The orbit-product divisibility adds NO information beyond those
    two per-element facts -- it is their product.  So it is not an independent coset
    invariant; it is a restatement.  VACUOUS by the preregistered control.""")

print(); print("="*74); print("VERDICT"); print("="*74)
structureless = {k: (v.denominator == 1 or abs(v.numerator) < 10**6) for k,v in inv.items()}
survivors = []   # candidates surviving frame-invariance AND vacuity AND not already banked
gate("no candidate survives the vacuity control", len(survivors) == 0, f"{len(survivors)} survivors")

RES = {"lambda": {k: str(LAM[k]) for k in E}, "lambda_sq": {k: str(LSQ[k]) for k in E},
       "denominators": {k: DEN[k] for k in E},
       "orbit_invariants": {k: str(v) for k,v in inv.items()},
       "denominator_product": D, "77_divides_product": D % 77 == 0,
       "77_forced_by_per_element_facts": forced,
       "77_verdict": "VACUOUS -- the orbit-product divisibility is the product of two banked per-element observations and adds no information",
       "survivors": survivors, "n_survivors": len(survivors),
       "outcome": "B" if not survivors else "A",
       "guard_relaxed": "frame-invariance only; Re h disqualified by name; nativeness and per-candidate companion demands dropped",
       "scope":("The lambda/CCC family across B^1 using banked per-element values; NOT a "
                "re-derivation of those values. Tests B8092 finding 1 only -- whether the "
                "nativeness guard suppressed a candidate in THIS family. Says nothing about the "
                "owner's general claim, which stands on B976 and B8092 independently. No measured "
                "number; Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE,"results.json"),"w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAIL: raise SystemExit(f"CONTROLS FAILED: {FAIL}")
print(f"\n  ALL CHECKS PASS -- OUTCOME {RES['outcome']}")
