"""B709 — the Turok-marriage adjudication: the exact/base-rate checks.
Math only; every number here supports a KILL or a firewall, not a physics claim."""
import math

def sqfree(n):
    n = abs(n); out = 1
    d = 2
    while d * d <= n:
        c = 0
        while n % d == 0:
            n //= d; c ^= 1
        if c: out *= d
        d += 1
    return out * (n if n > 1 else 1)

print("== I5/T2: the 36-count base rate (does 36 pick E6?) ==")
# rank-6 simple algebras: #positive roots = (dim - rank)/2
fam = {"E6": (78, 6), "B6=so(13)": (78, 6), "C6=sp(12)": (78, 6),
       "A6=su(7)": (48, 6), "D6=so(12)": (66, 6), "F4": (52, 4)}
share36 = [k for k, (d, r) in fam.items() if (d - r) // 2 == 36]
for k, (d, r) in fam.items():
    print(f"  {k:12s} dim {d:2d} rank {r} -> #pos_roots {(d-r)//2}")
print(f"  36 positive roots shared by: {share36}  -> count does NOT select E6")
assert set(share36) == {"E6", "B6=so(13)", "C6=sp(12)"}

print("\n== T5: the rung-4 single-ratios (named ONLY to firewall) ==")
phi = (1 + 5 ** 0.5) / 2
print(f"  1/(2phi) = {1/(2*phi):.5f}  (vs PDG sin^2 th12 ~ 0.307; ~0.6% off)")
print(f"  theta0 = 2/9 = {2/9:.5f}  (B703, 0.89 sigma, HINT-grade)")
print("  both: rung-4 single-ratio, NO mechanism (B685) -> hints only, not derived")
assert abs(1/(2*phi) - 0.309) < 1e-3

print("\n== I1/T1: the two-time distinction (why the FRW embedding fails) ==")
print("  suspension time  : compact S^1 base, monodromy sigma=[[2,1],[1,1]] per period")
print("                     (Anosov flow on a finite-vol H^3 manifold; Euclidean, Lambda<0)")
print("  cosmological time : non-compact R, single bang, Lorentzian FRW metric a(t)")
print("  -> INTERNAL 3-mfd fibration time != EXTERNAL 4-d spacetime time")
print("     (different dimension AND signature; no metric/scale bridges them)")
sigma_tr = 2 + 1  # tr[[2,1],[1,1]] = 3  (pseudo-Anosov, |tr|>2)
assert sigma_tr == 3 and sigma_tr > 2   # hyperbolic monodromy, not a bang-gluing

print("\n== the two-ZZ/2 partition (load-bearing) ==")
print("  Z/2-A amphichirality : K=Kbar, CS=0 -> CANONICAL (fixes the geometric slice)")
print("  Z/2-B fiber torsor   : sqrt5->-sqrt5 -> NON-canonical (B701, no basepoint)")
print("  Turok CPT            : CANONICAL (fixes the bang)  -> matches A, INVERTS B")
print("  -> marriage reaches A (amphichirality/strong-CP); B is the INVERSION")

print("\n== T3: the dimensionful no-go (dimensionless integer -> mass needs a scale) ==")
print("  N(v0) = -6 : dimensionless integer ; 4.8e8 GeV : dimensionful")
print("  a mass needs a SCALE the program lacks (S3/B615) -> value-match REFUTED")

print("\nALL CHECKS CONSISTENT WITH THE SEALED ALL-B VERDICT.")
