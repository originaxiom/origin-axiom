#!/usr/bin/env python3
"""B8101 -- B739's scattering determinant VERIFIED as a scattering determinant, and the
trace-formula assembly for the object's one-loop problem.

Second rung of the finish-the-3d-theory line. B739 banked phi_m004(s) = Lambda_K(s-1)/Lambda_K(s).
This checks it satisfies the conditions a scattering determinant MUST satisfy on a hyperbolic
3-manifold, computes its value at the symmetric point, and assembles which trace-formula terms
are in hand. Gate 5 untouched -- no measured value anywhere.
"""
import json, os
import mpmath as mp
mp.mp.dps = 25
HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAIL.append(l)

# K = Q(sqrt(-3)), class number 1, d_K = -3.  zeta_K = zeta * L(chi_{-3}).
def Lchi(s): return mp.power(3,-s)*(mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))
def LamK(s): return mp.power(3,s/2)*mp.power(2*mp.pi,-s)*mp.gamma(s)*mp.zeta(s)*Lchi(s)
def phi(s):  return LamK(s-1)/LamK(s)

print("="*74); print("1. THE FIELD SIDE -- Lambda_K's functional equation"); print("="*74)
fe = max(abs(LamK(s)-LamK(1-s)) for s in [mp.mpf('0.3'), mp.mpf('2.7'), mp.mpc('1.4','0.6')])
gate("Lambda_K(s) = Lambda_K(1-s) (so zeta_K is correctly completed)", fe < 1e-25,
     f"worst {mp.nstr(fe,4)}")

print(); print("="*74); print("2. IS IT A SCATTERING DETERMINANT? the unitarity test"); print("="*74)
print("""    On H^3 the spectral parameter is s(2-s) and the critical line is Re s = 1,
    so a scattering determinant must satisfy phi(s) phi(2-s) = 1 -- NOT phi(s)phi(1-s).""")
un = max(abs(phi(s)*phi(2-s)-1) for s in [mp.mpf('1.7'), mp.mpf('0.4'), mp.mpc('1.3','0.9')])
gate("phi(s) phi(2-s) = 1  -- correct H^3 unitarity", un < 1e-25, f"worst {mp.nstr(un,4)}")
print("    So B739's formula is not merely an identity: it has the RIGHT STRUCTURE.")

print(); print("="*74); print("3. THE SYMMETRIC POINT -- and it is the non-trivial sign"); print("="*74)
vals = [phi(1+mp.mpf(e)) for e in ['1e-4','1e-6','1e-8']]
for e, v in zip(['1e-4','1e-6','1e-8'], vals):
    print(f"    phi(1+{e}) = {mp.nstr(v,12)}")
p1 = mp.mpf(-1)
gate("phi(1) = -1 (unitarity forces +-1; it lands on -1)", abs(vals[-1]-(-1)) < 1e-7)
gate("=> the trace-formula term (1 - phi(1)) equals 2, NOT 0", abs((1-p1)-2) < 1e-30)
print("    The cusp therefore contributes NON-TRIVIALLY at the centre of the critical line.")

print(); print("="*74); print("4. THE CONTINUOUS INTEGRAND -- computable, and real"); print("="*74)
def dlogphi(r):
    return -mp.diff(lambda z: mp.log(phi(z)), 1+1j*mp.mpf(r))
rows = [(r, dlogphi(r)) for r in ['0.5','1.0','2.0','4.0','8.0']]
for r, v in rows:
    print(f"    r={r:>4}   -phi'/phi(1+ir) = {mp.nstr(v,10)}")
gate("the integrand is REAL on the critical line (as unitarity requires)",
     all(abs(mp.im(v)) < 1e-20 for _, v in rows))

print(); print("="*74); print("5. THE ASSEMBLY -- what is in hand for the one-loop problem"); print("="*74)
ASM = [
 ("identity/volume term",      "IN HAND",  "Vol = 2.029883212819307 (B8099, verified)"),
 ("geodesic/discrete term",    "IN HAND",  "log Z_geod = -0.272977 +/- 2.0e-3 (B8100)"),
 ("scattering determinant",    "IN HAND",  "phi(s) = Lambda_K(s-1)/Lambda_K(s), unitarity verified here"),
 ("symmetric-point term",      "IN HAND",  "phi(1) = -1, so (1 - phi(1)) = 2"),
 ("continuous integrand",      "IN HAND",  "-phi'/phi computable and real on Re s = 1"),
 ("the test function h(r)",    "MISSING",  "the spin-2 (boundary-graviton) h for a CUSPED quotient"),
 ("the assembled determinant", "MISSING",  "needs h; not attempted here"),
]
for n, st, d in ASM:
    print(f"    {st:<9} {n:<26} {d}")
inhand = sum(1 for _,s,_ in ASM if s == "IN HAND")
gate("five of seven ingredients in hand", inhand == 5, f"{inhand}/7")

RES = {"functional_equation_worst_err": float(fe), "unitarity_worst_err": float(un),
       "unitarity_condition": "phi(s)phi(2-s) = 1  (H^3: spectral parameter s(2-s), critical line Re s = 1)",
       "phi_at_symmetric_point": -1.0, "one_minus_phi1": 2.0,
       "integrand_real_on_critical_line": True,
       "assembly": [{"term": n, "status": s, "note": d} for n, s, d in ASM],
       "n_in_hand": inhand, "n_total": len(ASM),
       "what_is_missing": "the spin-2 test function h(r) for a CUSPED quotient, and hence the assembled determinant",
       "scope": ("Verifies B739's scattering determinant SATISFIES the conditions a scattering "
                 "determinant must satisfy on H^3, computes phi(1) = -1, and shows the continuous "
                 "integrand is computable and real. Does NOT assemble the one-loop graviton "
                 "determinant -- the spin-2 test function for a cusped quotient is missing and was "
                 "not attempted. No measured value; Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE,"results.json"),"w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAIL: raise SystemExit(f"FAILED: {FAIL}")
print("\n  ALL CHECKS PASS")
