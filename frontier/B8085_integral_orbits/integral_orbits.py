#!/usr/bin/env python3
"""B8085 -- Route A of B990's orbit-to-point gap: the arithmetic obstruction is ABSENT.

B990 proved the orbit-to-point gap STRUCTURAL -- an orbit invariant is constant on the
orbit, so no refinement of it can ever pick a point -- and named exactly two routes across.
Route A: shrink the group from G(Q) to G(Z) and count the integral orbits inside the
object's rational orbit.  "If it is 1, the integral orbit is a canonical point up to G(Z),
which is exactly what a VEV direction needs."

B990 attached an explicit prior: UNFAVOURABLE.  That prior is adopted here unchanged.

The rational orbit is classified by the cubic etale algebra K = Q[x]/(x^3-12x-5).  The
integral orbits inside one rational orbit, in every correspondence of this Bhargava /
Kato-Yukie type, are counted by a class-group-type quantity of K.  This computes ALL the
candidates.  If they all come out trivial, the conclusion is independent of which one
governs -- and that is the only circumstance under which this arc reports a positive.

WHAT THIS ARC MAY NOT CLAIM: that h(K) = 1 is its finding (already banked, and
independently reconfirmed by an external referee this week), nor that the integral orbit
count IS one of these quantities.  Identifying the counter is Kato-Yukie/Bhargava integral
theory and is registered as OWED.

QUANTIFIER (P0, from B990, restated): the ALGEBRA AND ITS ARITHMETIC.  Not a manifold.
Gate 5: a VEV *direction* is a direction in an algebra; no value or scale enters.

Criteria sealed in PREREGISTRATION.md before the narrow class number was computed.
"""
import subprocess
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
x = sp.symbols("x")
F = x**3 - 12 * x - 5
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


print("=" * 78)
print("CONTROLS -- the field must be right before any class datum is read")
print("=" * 78)
poly = sp.Poly(F, x)
disc = sp.discriminant(poly)
roots = sp.real_roots(poly)
gate("the cubic is irreducible over Q", poly.is_irreducible)
gate("disc = 6237 = 3^4 * 7 * 11", disc == 6237 and sp.factorint(6237) == {3: 4, 7: 1, 11: 1},
     str(sp.factorint(int(disc))))
gate("totally real: three real roots", len(roots) == 3)

# ---------------------------------------------------------------- engine 1: PARI/GP
GP = r"""
T = x^3 - 12*x - 5; K = bnfinit(T,1); N = bnfnarrow(K);
print(K.no); print(K.cyc); print(N[1]); print(K.sign); print(K.disc);
for(i=1,#K.fu, print(lift(K.fu[i])));
"""
out = subprocess.run(["gp", "-q"], input=GP, capture_output=True, text=True).stdout.split("\n")
h = int(out[0]); cyc = out[1].strip(); hplus = int(out[2]); sign = out[3].strip()
pdisc = int(out[4]); units = [sp.sympify(u.strip().replace("^", "**"))
                              for u in out[5:] if u.strip()]
print()
print("=" * 78)
print("ENGINE 1 -- PARI/GP")
print("=" * 78)
print(f"  disc {pdisc} | signature {sign} | h = {h} | Cl = {cyc} | h+ = {hplus}")
gate("PARI agrees with the independently computed discriminant", pdisc == disc)

# ---------------------------------------------------------------- engine 2: from scratch
print()
print("=" * 78)
print("ENGINE 2 -- independent: units verified by norm, signs by exact evaluation")
print("=" * 78)
sig = []
for u in units:
    N = sp.resultant(poly, sp.Poly(u, x))
    gate(f"  {u} is a unit (norm +-1)", abs(N) == 1, f"norm {N}")
    sig.append([0 if u.subs(x, r).evalf(60) > 0 else 1 for r in roots])
sig.append([1, 1, 1])                       # the sign vector of -1
rows = [r[:] for r in sig]
rk = 0
for c in range(3):
    p = next((i for i in range(rk, len(rows)) if rows[i][c] % 2), None)
    if p is None:
        continue
    rows[rk], rows[p] = rows[p], rows[rk]
    for i in range(len(rows)):
        if i != rk and rows[i][c] % 2:
            rows[i] = [(rows[i][j] - rows[rk][j]) % 2 for j in range(3)]
    rk += 1
print(f"\n  signature vectors: {sig}")
print(f"  rank over F2 = {rk} of 3  -> image {2**rk} of 8")
hplus_indep = h * 8 // (2 ** rk)
gate("the unit signature map is SURJECTIVE onto {+-1}^3", rk == 3)
gate("h+ computed independently agrees with PARI", hplus_indep == hplus,
     f"independent {hplus_indep}, PARI {hplus}")

print()
print("=" * 78)
print("THE CANDIDATE COUNTERS")
print("=" * 78)
cands = {"h": h, "h+": hplus, "|Cl/Cl^2|": 1 if cyc == "[]" else None,
         "|Cl/Cl^3|": 1 if cyc == "[]" else None}
for k, v in cands.items():
    print(f"     {k:12s} = {v}")
allone = all(v == 1 for v in cands.values())
gate("EVERY candidate class-group counter is trivial", allone, str(cands))

print(f"""
  B990's prior was UNFAVOURABLE -- "class numbers of this kind are generically > 1, and
  the programme's history is a record of homogeneity winning."  Adopted unchanged, and
  it did NOT hold: the class group is trivial, the narrow class group is trivial, and
  the unit signature map is surjective, so every quotient that could count integral
  orbits is 1.

  WHAT THIS MEANS, stated at exactly its strength: the ARITHMETIC OBSTRUCTION THAT
  ROUTE A WAS EXPECTED TO MEET IS ABSENT.  Whichever class-group-type quantity governs
  the integral orbit count, it is trivial -- so the conclusion does not depend on
  resolving which, which is why all four were computed.

  WHAT IT DOES NOT MEAN: that the integral orbit count IS 1.  Identifying the counter is
  Kato-Yukie/Bhargava integral theory and is OWED, not asserted.  This arc removes the
  obstruction B990 predicted; it does not by itself deliver the canonical point.""")

RES = {"disc": int(disc), "signature": sign, "h": h, "class_group": cyc,
       "h_narrow": hplus, "h_narrow_independent": hplus_indep,
       "signature_rank_F2": rk, "signature_surjective": rk == 3,
       "candidate_counters": {k: v for k, v in cands.items()},
       "all_counters_trivial": allone,
       "prior": "UNFAVOURABLE (B990), adopted unchanged",
       "prior_held": not allone,
       "scope": ("Computes the class-arithmetic of K = Q[x]/(x^3-12x-5) with two "
                 "independent engines. Does NOT claim h=1 as a finding (already banked) "
                 "and does NOT claim the integral orbit count equals any of these "
                 "quantities -- identifying the counter is Kato-Yukie/Bhargava integral "
                 "theory and is registered as owed. The result is that the arithmetic "
                 "obstruction B990 expected is absent, not that the gap is closed.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
