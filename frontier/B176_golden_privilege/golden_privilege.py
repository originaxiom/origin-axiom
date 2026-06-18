#!/usr/bin/env python3
"""B176 (P3 of the multibody-extraction plan): the golden privilege, done with controls. Tests the
cross-session ('chat2') claim that the woven-chain combination structure 'dresses the most irrational
resonance'. Honest verdict: golden (phi) IS robustly privileged -- but it is golden-STANDS-ALONE, NOT a
monotone irrationality ordering (silver ~ bronze).

  C1 [exact] irrationality ordering: the metallic [m;m,m,...] has Hurwitz constant 1/sqrt(m^2+4); golden
     (m=1, sqrt5) is the EXTREMAL most-irrational, then silver (m=2), bronze (m=3) -- decreasing.
  C2 [num, theta-avg, both models] the GOLDEN satellite ladder dominates BOTH the silver and the bronze
     ladders (ratios > 2), in cosine AND Sturmian -> golden is privileged in the collective combination
     structure. (CONFIRMS chat2's core 'phi is special'.)
  C3 [control: not bare-width] the golden/silver LADDER ratio (~10x) >> the golden/silver PRINCIPAL-gap
     ratio (~1, comparable) -> the privilege is NOT explained by golden having a wider bare gap; it is a
     genuine irrationality effect.
  C4 [num] the ordering BREAKS below golden: silver/bronze ladder ratio ~ 1 (comparable) -> NOT a monotone
     golden>silver>bronze law. (CORRECTS chat2's generalization: golden alone, not a continued-fraction order.)

VERDICT: phi/golden privilege is REAL and robust (C2, not bare-width C3); but it is golden-stands-alone,
not a monotone irrationality ordering (C4). The math (golden = Hurwitz-extremal most-irrational =
KAM-most-robust) is real; the P000-anchor tie is [RHYME] with a real kernel, NOT a derivation; a rigorous
statement is NEEDS-SPECIALIST; the effect is cosine-dominant. FIREWALL: emergent quasicrystal physics
(K007/K010), no scale/Lambda/constant, nothing to CLAIMS.md.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5)/2
A = {'golden': 1/phi, 'silver': 2**0.5 - 1, 'bronze': (13**0.5 - 3)/2}    # decreasing irrationality
def cos_(N, a, th): n = np.arange(1, N+1); return np.cos(2*np.pi*(a*n + th))
def stu_(N, a, th): n = np.arange(1, N+1); return (((n*a + th) % 1.0) >= 1.0 - a).astype(float)

N = 7000
THS = [(0.05, 0.31), (0.20, 0.62), (0.41, 0.13)]                          # phase pairs to average over
def wat(Vfun, a1, a2, lam, t, th1, th2):
    V = lam*Vfun(N, a1, th1) + lam*Vfun(N, a2, th2)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N-1))); d = np.diff(e); ids = np.arange(1, N)/N
    m = np.abs(ids - (t % 1.0)) < 0.003; return d[m].max() if m.any() else 0.0

def ladders(Vfun, aA, aB, lam=1.0):
    As = np.mean([sum(wat(Vfun, aA, aB, lam, (1+k)*aA + k*aB, t1, t2) for k in (1, 2, 3)) for t1, t2 in THS])
    Bs = np.mean([sum(wat(Vfun, aA, aB, lam, k*aA + (1+k)*aB, t1, t2) for k in (1, 2, 3)) for t1, t2 in THS])
    pA = np.mean([wat(Vfun, aA, aB, lam, aA, t1, t2) for t1, t2 in THS])   # bare principal gaps
    pB = np.mean([wat(Vfun, aA, aB, lam, aB, t1, t2) for t1, t2 in THS])
    return As, Bs, pA, pB

print("== C1 [exact]: irrationality ordering golden > silver > bronze (Hurwitz 1/sqrt(m^2+4)) ==")
hur = [(m, 1/(m*m+4)**0.5) for m in (1, 2, 3)]
chk("golden(m=1) is the Hurwitz-extremal most-irrational; constant decreases with m",
    hur[0][1] > hur[1][1] > hur[2][1], x=f"1/sqrt(m^2+4): golden {hur[0][1]:.3f} > silver {hur[1][1]:.3f} > bronze {hur[2][1]:.3f}")

print("\n== C2/C3/C4 [theta-averaged ladder strengths, both models] ==")
res = {}
for Vname, Vfun in [('cosine', cos_), ('Sturmian', stu_)]:
    res[Vname] = {}
    for nA, nB in [('golden', 'silver'), ('golden', 'bronze'), ('silver', 'bronze')]:
        As, Bs, pA, pB = ladders(Vfun, A[nA], A[nB])
        res[Vname][(nA, nB)] = (As, Bs, pA, pB)
        r = As/Bs if Bs > 1e-6 else float('inf')
        print(f"   {Vname:9s} {nA}/{nB}: ladder {As:.3f} vs {Bs:.3f} (ratio {r:.2f}) | principal {pA:.3f}/{pB:.3f}")

gs_c = res['cosine'][('golden', 'silver')]; gb_c = res['cosine'][('golden', 'bronze')]
sb_c = res['cosine'][('silver', 'bronze')]; gs_s = res['Sturmian'][('golden', 'silver')]
gb_s = res['Sturmian'][('golden', 'bronze')]; sb_s = res['Sturmian'][('silver', 'bronze')]

print()
chk("C2: GOLDEN ladder dominates BOTH silver & bronze (ratio>2), in cosine AND Sturmian -> golden privileged",
    gs_c[0]/gs_c[1] > 2 and gb_c[0]/gb_c[1] > 2 and gs_s[0]/gs_s[1] > 2 and gb_s[0]/gb_s[1] > 2,
    x=f"g/s {gs_c[0]/gs_c[1]:.1f}(cos) {gs_s[0]/gs_s[1]:.1f}(stu); g/b {gb_c[0]/gb_c[1]:.1f}(cos) {gb_s[0]/gb_s[1]:.1f}(stu)")
chk("C3 [control]: golden/silver LADDER ratio >> golden/silver PRINCIPAL ratio -> not a bare-width artifact",
    (gs_c[0]/gs_c[1]) > 3*(gs_c[2]/max(gs_c[3], 1e-9)),
    x=f"ladder ratio {gs_c[0]/gs_c[1]:.1f} vs principal ratio {gs_c[2]/max(gs_c[3],1e-9):.2f} (golden NOT wider-principal)")
chk("C4: the ordering BREAKS below golden -- silver/bronze ladders COMPARABLE (0.5<ratio<2), both models",
    0.5 < sb_c[0]/max(sb_c[1], 1e-9) < 2.0 and 0.5 < sb_s[0]/max(sb_s[1], 1e-9) < 2.0,
    x=f"s/b ratio {sb_c[0]/max(sb_c[1],1e-9):.2f}(cos) {sb_s[0]/max(sb_s[1],1e-9):.2f}(stu) -> golden stands alone, NOT monotone")

print("\nVERDICT: phi/golden is GENUINELY privileged in the collective combination structure -- its satellite")
print("ladder dominates BOTH silver's and bronze's, theta-averaged, in both models [C2], and not because golden")
print("has a wider bare gap [C3]. (CONFIRMS chat2's 'phi is special'.) BUT it is golden-STANDS-ALONE: the ordering")
print("does NOT continue golden>silver>bronze -- silver and bronze are comparable [C4]. (CORRECTS chat2's")
print("'most-irrational-in-order' generalization.) The golden=most-irrational=most-robust math is real (Hurwitz/KAM);")
print("the P000-anchor tie is [RHYME] with a real kernel, not a derivation; a rigorous statement is NEEDS-SPECIALIST;")
print("the effect is cosine-dominant. FIREWALL: emergent quasicrystal physics, nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
