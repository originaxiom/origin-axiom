"""PRE-REGISTERED out-of-sample test of the divisor law (written 2026-09-07 BEFORE this solve was run).

In-sample: every coefficient with N(nu) <= 108 (the R=6 window) was inspected while the law was found.
Out-of-sample: an R=10 solve (|mu| <= 10, N(nu) <= 300).  Precision degrades toward the cutoff, so the
test window is 108 < N(nu) <= 200 and the tolerance is the R=10 solve's own precision, MEASURED on the
in-sample band 60 <= N <= 108 (max |obs - S| there, call it eps_in).  PASS iff
   max_{108 < N <= 200} |c(nu)/c0 - S(nu)|  <  max(5e-3, 3 * eps_in)      over ALL even-m2 modes,
including the modes the law predicts to VANISH.  Zero fitted parameters: c0 = c(1) from the same solve.
"""
import json, sys, time, numpy as np
import harmonic_generator as H
import divisor_law as L

R, Y, n = 10.0, 0.45, 3200
tau, chiT, w0, nfound = H.find_cusp_lattice()
lat = H.Lattice(tau, chiT); moves = H.build_moves()
t0 = time.time()
c, modes, info = H.solve(lat, moves, Y, R, n, seed=10)
print("solve:", json.dumps(info), f"{time.time()-t0:.0f}s")
c0 = c[(0, 2)]
print(f"c0 = {c0:.10f}")
out = {"solve": info, "c0": [c0.real, c0.imag],
       "coefficients": {f"{k[0]},{k[1]}": [v.real, v.imag] for k, v in sorted(c.items())}}

def band(lo, hi):
    worst = 0.0; rows = []
    for (m1, m2), v in c.items():
        if m2 % 2: continue
        nu = (m2 // 2, -m1); N = L.norm(nu)
        if not (lo < N <= hi): continue
        s = L.S(nu); d = abs(v / c0 - s); worst = max(worst, d)
        rows.append((N, (m1, m2), nu, s, (v / c0).real, (v / c0).imag, d))
    rows.sort(); return worst, rows

eps_in, rows_in = band(60, 108)
tol = max(5e-3, 3 * eps_in)
worst, rows = band(108, 200)
print(f"in-sample band 60<N<=108: {len(rows_in)} modes, eps_in = {eps_in:.2e}  -> tolerance {tol:.2e}")
print(f"OUT-OF-SAMPLE 108<N<=200: {len(rows)} modes, max |c/c0 - S| = {worst:.2e}")
nz = [r for r in rows if abs(r[3]) > 1e-9]; z = [r for r in rows if abs(r[3]) <= 1e-9]
print(f"   of which predicted nonzero: {len(nz)} (max dev {max(r[6] for r in nz):.2e}), predicted ZERO: {len(z)} (max |obs| {max(r[6] for r in z):.2e})")
print("  N    mode       nu          S(nu)     obs Re     obs Im    |diff|")
for r in rows:
    print(f"{r[0]:4d}  {str(r[1]):10s} {str(r[2]):11s} {r[3]:+9.5f}  {r[4]:+9.5f}  {r[5]:+8.5f}  {r[6]:.1e}" + ("  <-- off" if r[6] > tol else ""))
verdict = "PASS" if worst < tol else "FAIL"
out.update({"eps_in": eps_in, "tol": tol, "worst_out": worst, "n_out": len(rows), "verdict": verdict,
            "rows_out": [[r[0], list(r[1]), list(r[2]), r[3], r[4], r[5], r[6]] for r in rows]})
json.dump(out, open("law_outofsample.json", "w"), indent=1)
print(f"\nPRE-REGISTERED OUT-OF-SAMPLE TEST: {verdict}")
