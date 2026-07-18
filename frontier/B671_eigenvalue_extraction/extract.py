"""B671 — the 351-candidate eigenvalue extraction (the web seat's
priority call, adopted): state the exact numbers, the ratios, the
cubics, and DECIDE the scalarization-gauge question via the
scale-invariant coefficient combinations. Plus the D1 sum-rule
coefficients (read from the cc2 seat's completed D1, provisional
pending their loop-4 packet). All exact over Q(sqrt-3)."""
import json
import os

import sympy as sp

_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
lam = sp.symbols("lambda")
r3 = sp.sqrt(3) * sp.I   # sqrt(-3)

d = json.load(open(os.path.join(_REPO, "frontier/B666_leads_campaign/cellA2/a2_results.json")))
ca = d["candidate_analysis"]

polys = {}
for key, v in ca.items():
    cp = sp.sympify(v["charpoly"].replace("lambda", "lam"), locals={"lam": lam, "I": sp.I})
    p = sp.Poly(cp, lam)
    c3, c2, c1, c0 = [sp.simplify(x) for x in p.all_coeffs()]
    assert c3 == 1
    e1, e2, e3 = -c2, c1, -c0            # elementary symmetric functions
    polys[key] = (e1, e2, e3)
    print(f"== {key} ==", flush=True)
    print(f"  e1 = {sp.nsimplify(e1)}", flush=True)
    print(f"  charpoly: lambda^3 - (e1) lambda^2 + (e2) lambda - (e3), exact in Q(sqrt-3)", flush=True)
    import mpmath as mp
    mp.mp.dps = 120
    def _tompc(z):
        zz = sp.expand(z)
        re = sp.N(sp.re(zz), 130); im = sp.N(sp.im(zz), 130)
        return mp.mpc(mp.mpf(str(re)), mp.mpf(str(im)))
    cs = [mp.mpc(1, 0), _tompc(-e1), _tompc(e2), _tompc(-e3)]
    roots = mp.polyroots(cs, maxsteps=200, extraprec=200)
    print("  eigenvalues (40 digits):", flush=True)
    for r_ in roots:
        print(f"    {mp.nstr(r_, 40)}", flush=True)
    print("  pairwise ratios (40 digits):", flush=True)
    rs = list(roots)
    for i in range(3):
        for j in range(i+1, 3):
            print(f"    l{i+1}/l{j+1} = {mp.nstr(rs[i]/rs[j], 30)}", flush=True)

print("\n== THE GAUGE QUESTION (decisive): scale-invariant combinations ==", flush=True)
inv = {}
for key, (e1, e2, e3) in polys.items():
    I1 = sp.simplify(e1**3 / e3)
    I2 = sp.simplify(e1 * e2 / e3)
    inv[key] = (I1, I2)
k1, k2 = list(polys)
same = (sp.simplify(inv[k1][0] - inv[k2][0]) == 0 and
        sp.simplify(inv[k1][1] - inv[k2][1]) == 0)
print(f"  e1^3/e3 and e1*e2/e3 equal across the two scalarizations: {same}", flush=True)
print("  => the eigenvalue RATIOS are " +
      ("GAUGE-INVARIANT (the same spectrum up to overall scale)" if same
       else "SCALARIZATION-DEPENDENT (the ratios are not invariant as computed)"), flush=True)
if not same:
    for key, (I1, I2) in inv.items():
        print(f"  {key}: e1^3/e3 = {sp.N(I1, 25)}; e1*e2/e3 = {sp.N(I2, 25)}", flush=True)

print("\n== THE D1 SUM-RULE COEFFICIENTS (cc2 seat, provisional pending packet) ==", flush=True)
try:
    _d1_path = os.environ.get(
        "OA_CC2_D1_RESULTS",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "d1_results.json"))
    d1 = json.load(open(_d1_path))
    hits = {k: d1[k] for k in d1 if "relation" in k.lower() or "coeff" in k.lower() or "solo" in k.lower()}
    print("  d1 keys:", list(d1)[:12], flush=True)
    print("  relation-bearing entries:", json.dumps(hits)[:800], flush=True)
except Exception as e:
    print(f"  unavailable: {e}", flush=True)
print("\nB671 EXTRACTION DONE", flush=True)
