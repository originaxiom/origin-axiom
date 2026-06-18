#!/usr/bin/env python3
"""B175 (collective-spectrum extraction, P1+P2 of the multibody plan): the woven metallic spectrum is
TWO-NUMBER PREDICTABLE -- heights exact at all couplings (gap-labeling), widths by an order-power law at
weak coupling. The disciplined version of the chat2 ridge: ridge real but MODEL-SPECIFIC; the width law
real but WEAK-COUPLING (perturbative, saturates strong). Lead positive, the bound stated once.

  C1 [heights, exact, all couplings] the prominent gaps of the woven cosine chain sit at the gap-labeling
     labels n1*a1+n2*a2 mod 1 (gap-labeling theorem, B173) -- seed-robust (golden+silver & golden+bronze).
  C2 [the width law, weak coupling] width(n1,n2) ~ lambda^(|n1|+|n2|): the log-lambda slope -> the label
     ORDER at weak coupling (decisive at order 2: slope ~ 2), seed-robust. => (lambda1,lambda2) forecast
     every gap WIDTH (perturbatively).
  C3 [the bound, stated once] at STRONG coupling the gaps SATURATE and the order-scaling breaks (slope <<
     order) -- the law is perturbative. Honest scope: predictivity over STRUCTURE (gap position + size),
     NOT over the value of a fundamental constant.
  C4 [model-distinction, reconciles B172/B173] the small-label combination ridge OPENS in the smooth
     cosine (bichromatic) model but is ~closed in the metallic Sturmian-indicator chain -- HEIGHTS are
     potential-independent (the module/theorem), WHICH gaps open + their widths are potential-dependent.
  C5 [null] the order-power scaling is specific to gap-label positions: a random non-label IDS window does
     not host a gap with clean order-scaling.

FIREWALL: emergent quasicrystal physics (K007/K010; bichromatic lattices + quasicrystals are MEASURED
materials); no scale/Lambda/constant; nothing to CLAIMS.md.
"""
import numpy as np
from scipy.linalg import eigvalsh_tridiagonal

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

phi = (1 + 5**0.5) / 2
ag = 1/phi                          # golden  1/phi
as_ = 2**0.5 - 1                    # silver  sqrt2 - 1
ab = (13**0.5 - 3)/2               # bronze  1/((3+sqrt13)/2) = (sqrt13-3)/2

def cos_V(N, a, th):
    n = np.arange(1, N+1); return np.cos(2*np.pi*(a*n + th))
def sturm_V(N, a, th):
    n = np.arange(1, N+1); return (((n*a + th) % 1.0) >= 1.0 - a).astype(float)

def width_at(Vfun, a1, a2, lam, target, N, th1=0.137, th2=0.413):
    V = lam*Vfun(N, a1, th1) + lam*Vfun(N, a2, th2)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N-1)))
    d = np.diff(e); ids = np.arange(1, N)/N
    m = np.abs(ids - target) < 0.003
    return d[m].max() if m.any() else 0.0

def label(a1, a2, n1, n2):
    return (n1*a1 + n2*a2) % 1.0

def order_slope(Vfun, a1, a2, n1, n2, lams, N):
    t = label(a1, a2, n1, n2)
    ws = np.array([width_at(Vfun, a1, a2, lam, t, N) for lam in lams])
    v = ws > 3e-4
    return (np.polyfit(np.log(np.array(lams)[v]), np.log(ws[v]), 1)[0] if v.sum() >= 2 else float('nan')), ws

N = 10000
PAIRS = [("golden+silver", ag, as_), ("golden+bronze", ag, ab)]

print("== C1 [heights, exact]: prominent woven-chain gaps sit at gap-labeling labels (seed-robust) ==")
for name, a1, a2 in PAIRS:
    V = 1.0*cos_V(N, a1, 0.137) + 1.0*cos_V(N, a2, 0.413)
    e = np.sort(eigvalsh_tridiagonal(V, np.ones(N-1))); d = np.diff(e); ids = np.arange(1, N)/N
    top = sorted(((ids[i], d[i]) for i in np.argsort(d)[::-1][:8]))
    def best(t):
        b = None
        for n1 in range(-6, 7):
            for n2 in range(-6, 7):
                if abs(n1)+abs(n2) <= 6:
                    v = label(a1, a2, n1, n2); e2 = min(abs(t-v), 1-abs(t-v))
                    if b is None or e2 < b[2]: b = (n1, n2, e2)
        return b
    errs = [best(t)[2] for t, w in top if w > 0.05]
    chk(f"{name}: every prominent gap matches a gap-label to <2e-3",
        max(errs) < 2e-3, x=f"max label-error {max(errs):.1e} over {len(errs)} gaps")

print("\n== C2 [the width law, weak coupling]: log-lambda slope -> label ORDER (decisive at order 2) ==")
WEAK = [0.10, 0.15, 0.22, 0.32]
for name, a1, a2 in PAIRS:
    s2, _ = order_slope(cos_V, a1, a2, 1, 1, WEAK, N)      # order 2 -- the clean diagnostic
    chk(f"{name}: order-2 (1,1) gap width slope ~ 2 (the width law, weak coupling)",
        abs(s2 - 2.0) < 0.4, x=f"slope = {s2:.2f}")
s3, _ = order_slope(cos_V, ag, as_, 2, 1, WEAK, N)         # order 3 -- trends to 3
chk("golden+silver: order-3 (2,1) slope trends toward 3 (> the order-2 slope)",
    s3 > 2.3, x=f"slope = {s3:.2f} (-> 3; not fully asymptotic at these lambda)")

print("\n== C3 [the bound, stated once]: STRONG coupling saturates -- the law is perturbative ==")
STRONG = [0.7, 1.0, 1.5]
s2_strong, _ = order_slope(cos_V, ag, as_, 1, 1, STRONG, N)
chk("at strong coupling the order-2 slope collapses (gaps saturate; the width law is weak-coupling only)",
    s2_strong < 1.0, x=f"strong-coupling slope = {s2_strong:.2f} << 2 -- predictivity over structure, NOT constants")

print("\n== C4 [model-distinction]: the ridge is cosine-specific; heights are universal (B172/B173) ==")
t21 = label(ag, as_, 2, 1)
w_cos = width_at(cos_V, ag, as_, 1.5, t21, N)
w_stu = width_at(sturm_V, ag, as_, 1.5, t21, N)
chk("the (2,1) combination gap OPENS in the cosine model but is ~closed in the metallic Sturmian chain",
    w_cos > 0.05 and w_stu < 0.03,
    x=f"cosine width {w_cos:.3f} vs Sturmian {w_stu:.3f} -- WHICH gaps open is potential-dependent; heights are not")

print("\n== C5 [null]: order-scaling is specific to gap-label positions ==")
rng = np.random.default_rng(0)
# a random non-label IDS target: pick one far (>0.02) from every small label
def far_target():
    for _ in range(200):
        t = rng.uniform(0.05, 0.95)
        if all(min(abs(t-label(ag, as_, n1, n2)), 1-abs(t-label(ag, as_, n1, n2))) > 0.02
               for n1 in range(-6, 7) for n2 in range(-6, 7) if abs(n1)+abs(n2) <= 6):
            return t
    return 0.5
tn = far_target()
ws_null = np.array([width_at(cos_V, ag, as_, lam, tn, N) for lam in WEAK])
tiny = ws_null.max() < 0.005                                   # ~100x below the real combination gaps (0.01-0.2)
flat = ws_null.max() / max(ws_null.min(), 1e-9) < 3.0          # no clean lambda-scaling (vs a real order law)
chk("a random non-label IDS window hosts no real, lambda-scaling gap (structure is label-specific)",
    tiny and flat, x=f"non-label widths {np.round(ws_null,4)} -- tiny (<0.005) AND flat (no order-scaling)")

print("\nVERDICT: the woven metallic spectrum is TWO-NUMBER PREDICTABLE -- (a1,a2) fix every gap HEIGHT exactly")
print("at all couplings [C1, gap-labeling theorem], and (lambda1,lambda2) fix every gap WIDTH via the order-power")
print("law width ~ lambda^(|n1|+|n2|) at weak coupling [C2, order-2 slope ~ 2], seed-robust. The bound, once: the")
print("width law is PERTURBATIVE -- it saturates at strong coupling [C3]; this is predictivity over STRUCTURE")
print("(gap position + size), not over a fundamental constant. The combination ridge is cosine-model-specific")
print("[C4] -- heights universal (theorem), openings potential-dependent. Firewall: emergent quasicrystal physics,")
print("nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
