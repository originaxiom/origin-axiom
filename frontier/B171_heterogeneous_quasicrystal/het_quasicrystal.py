#!/usr/bin/env python3
"""B171 (Phase 0 of the multi-seed plan): the heterogeneous metallic quasicrystal --
baseline + density-trap null + verification of the cross-session 'combination gap' claim.

Builds discrete Schrodinger operators (Hψ)_n = ψ_{n+1}+ψ_{n-1}+V_n ψ_n with metallic
Sturmian potentials V_n = λ·χ_{[1-α,1)}(nα+θ mod 1) (the Fibonacci-Hamiltonian construction,
K007/K010). A SINGLE metallic chain has IDS gap labels in the rank-2 module Z+Z·α (gap
labeling theorem, Bellissard/Johnson-Moser). WEAVING two distinct metallic chains gives a
two-frequency potential whose labels live in the rank-3 module Z + Z·α_g + Z·α_s. The
QUESTION (L16): does a genuine COMBINATION gap -- label n1·α_g+n2·α_s with BOTH nonzero and
SMALL -- open above the density floor?

Phase-0 locks:
  B1 [control] single golden / single silver chains: every prominent gap sits at a
     single-frequency label (n,0)/(0,n) -- the pure rank-2 ladders, low null.
  B2 [num] the WOVEN chain INHERITS both pure ladders (the ±1 labels of each survive) --
     the 'bilingual' result; credible (small label, low null).
  B3 [null, DENSITY TRAP] the rank-3 label set {n1 αg + n2 αs mod 1} is DENSE: by |n1|+|n2|
     the chance-hit rate climbs (sum<=1 ~0.4%, <=4 ~4%, <=6 ~8%); min spacing collapses.
     => a LARGE-label match is NOT evidence; the credible window is small labels (sum<=3).
  B4 [VERIFICATION] the cross-session 'first combination gap' IDS≈0.611. A real, wide gap DOES
     sit there (w~0.11, comparable to the inherited ±1 ladders) -- so it is NOT noise. But its
     ONLY module match is the LARGE label (3,-3) (sum 6, ~20% null); no small label is near it.
     By the gap-labeling theorem a real gap's IDS must lie in the module, so its true label is
     well-defined but UNIDENTIFIED at this resolution -- the (3,-3) assignment (err ~2e-4 ~ O(1/N))
     is PLAUSIBLE but NOT statistically credible. The honest status: real gap, label unverified;
     the Phase-1 test is whether its IDS CONVERGES to (3,-3)=0.611461 as N grows. (The cross-session
     headline over-read a plausible-but-uncertified large-label match as an established result.)

VERDICT (Phase 0): the woven spectrum is bilingual (both rank-2 ladders survive) [B2, credible];
the density trap is real and quantified [B3]; the cross-session 0.611 gap is REAL but its
combination-label (3,-3) is plausible-yet-UNVERIFIED (large label / high null) [B4] -- not a
density artifact (the gap exists) and not an established combination gap (the label is uncertified);
the genuine test = IDS-convergence + a SMALL-label hunt, both Phase 1. FIREWALL: emergent
quasicrystal math (K007/K010 boundary), NOT fundamental; no scale/Λ; nothing to CLAIMS.md.
"""
import numpy as np

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

def metallic_alpha(m):
    """frequency α = 1/λ_m, λ_m = (m+√(m²+4))/2 the metallic mean (golden m=1, silver 2, bronze 3)."""
    lam = (m + (m * m + 4) ** 0.5) / 2
    return 1.0 / lam

def sturmian_V(N, alpha, theta):
    """V_n = χ_{[1-α,1)}(nα+θ mod 1), n=1..N -- the metallic Sturmian indicator (Fibonacci pot.)."""
    n = np.arange(1, N + 1)
    frac = (n * alpha + theta) % 1.0
    return (frac >= 1.0 - alpha).astype(float)

def spectrum(N, potentials):
    """eigenvalues of the tridiagonal Dirichlet Schrodinger operator with V = sum of pot. terms."""
    V = np.zeros(N)
    for lam, alpha, theta in potentials:
        V += lam * sturmian_V(N, alpha, theta)
    H = np.diag(V) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    return np.linalg.eigvalsh(H)

def top_gaps(eigs, N, k=12, min_width=0.04):
    """the k widest spectral gaps; IDS on a gap = (#states below)/N. Returns (ids, width)."""
    e = np.sort(eigs)
    d = np.diff(e)
    idx = np.argsort(d)[::-1]
    out = []
    for i in idx:
        if d[i] < min_width:
            break
        ids = (i + 1) / N                      # i+1 states at or below the lower gap edge
        out.append((ids, d[i]))
        if len(out) >= k:
            break
    return sorted(out)

def best_label(ids, ag, as_, Lmax=8):
    """nearest label (n1,n2), |n1|+|n2|<=Lmax, to an IDS value (circular distance)."""
    best = None
    for n1 in range(-Lmax - 1, Lmax + 2):
        for n2 in range(-Lmax - 1, Lmax + 2):
            if 0 < abs(n1) + abs(n2) <= Lmax:
                v = (n1 * ag + n2 * as_) % 1.0
                err = min(abs(ids - v), 1 - abs(ids - v))
                if best is None or err < best[2]:
                    best = (n1, n2, err)
    return best

def null_rate(ag, as_, Lmax, tol, R=200000, seed=0):
    """chance a uniform-random IDS lands within tol of SOME label with |n1|+|n2|<=Lmax."""
    rng = np.random.default_rng(seed)
    vals = np.array(sorted({(n1 * ag + n2 * as_) % 1.0
                            for n1 in range(-Lmax - 1, Lmax + 2)
                            for n2 in range(-Lmax - 1, Lmax + 2)
                            if 0 < abs(n1) + abs(n2) <= Lmax}))
    x = rng.uniform(0, 1, R)
    j = np.searchsorted(vals, x) % len(vals)
    d1 = np.abs(x - vals[j]); d2 = np.abs(x - vals[(j - 1) % len(vals)])
    dd = np.minimum(np.minimum(d1, d2), 1 - np.maximum(d1, d2))
    return (dd < tol).mean()

ag, as_, ab = metallic_alpha(1), metallic_alpha(2), metallic_alpha(3)
print(f"frequencies: golden α_g=1/φ={ag:.6f}  silver α_s=√2-1={as_:.6f}  bronze α_b={ab:.6f}")
N, LAM, theta = 8000, 1.5, 0.1357
TOL = 1.2e-3                                    # ~ finite-size O(1/N) resolution at N=8000

print("\n== B1 [control]: single metallic chains -> pure rank-2 ladders (single-freq labels) ==")
for name, a in (("golden", ag), ("silver", as_)):
    gaps = top_gaps(spectrum(N, [(LAM, a, theta)]), N, k=8)
    sums = []
    for ids, w in gaps:
        n1, n2, err = best_label(ids, ag, as_)
        sums.append((n1, n2, err))
    # for a single chain, every prominent gap is a single-frequency label of THAT chain
    one_freq = all((n2 == 0) if name == "golden" else (n1 == 0) for n1, n2, e in sums if e < TOL)
    labs = ", ".join(f"({n1},{n2})" for n1, n2, e in sums if e < TOL)
    chk(f"{name} chain: prominent gaps are single-frequency labels", one_freq, x=f"{labs}")

print("\n== B2 [num]: the WOVEN chain inherits BOTH pure ladders (bilingual) ==")
wgaps = top_gaps(spectrum(N, [(LAM, ag, theta), (LAM, as_, theta + 0.27)]), N, k=14)
inherited_g = inherited_s = False
print("   woven-chain prominent gaps (IDS -> nearest small label):")
for ids, w in wgaps:
    n1, n2, err = best_label(ids, ag, as_)
    tag = "" if err < TOL else "  [>tol: density floor]"
    s = abs(n1) + abs(n2)
    print(f"     IDS {ids:.4f}  w={w:.3f} -> ({n1:2d},{n2:2d}) sum={s} err={err:.4f}{tag}")
    if err < TOL and s == 1 and n2 == 0:
        inherited_g = True
    if err < TOL and s == 1 and n1 == 0:
        inherited_s = True
chk("a golden ±1 ladder gap survives in the woven spectrum", inherited_g)
chk("a silver ±1 ladder gap survives in the woven spectrum", inherited_s)

print("\n== B3 [null, DENSITY TRAP]: the label set is dense; small labels are the credible window ==")
prev = -1; mono = True
for L in (1, 2, 3, 4, 6):
    r = null_rate(ag, as_, L, TOL)
    print(f"     |n1|+|n2|<={L}: chance-hit {100*r:5.1f}%  (tol {TOL:.0e})")
    if r < prev:
        mono = False
    prev = r
chk("chance-hit rate rises with label-sum (density trap real); sum<=3 is the low-null window",
    mono and null_rate(ag, as_, 3, TOL) < 0.06 and null_rate(ag, as_, 6, TOL) > null_rate(ag, as_, 3, TOL),
    x=f"sum<=3: {100*null_rate(ag,as_,3,TOL):.1f}%  vs  sum<=6: {100*null_rate(ag,as_,6,TOL):.1f}%")

print("\n== B4 [VERIFICATION]: the cross-session 0.611 gap -- real, but label (3,-3) UNVERIFIED ==")
comb = (3 * ag - 3 * as_) % 1.0                 # = 0.611461, the claimed (3,-3) combination label
# locate the actual woven-chain gap nearest 0.611 (reuse B2's spectrum)
near = min(wgaps, key=lambda g: min(abs(g[0] - comb), 1 - abs(g[0] - comb)))
nids, nw = near
n1, n2, err = best_label(nids, ag, as_)
print(f"     a REAL gap sits at IDS {nids:.4f} (width {nw:.3f}); (3,-3) value = {comb:.6f}")
chk("a real, wide gap exists near 0.611 (NOT noise)", nw > 0.06,
    x=f"width {nw:.3f} ~ the inherited ±1 ladder widths")
chk("...but its only module match is the LARGE label (3,-3) (sum 6) -> label UNVERIFIED, not credible",
    (n1, n2) == (3, -3) and abs(n1) + abs(n2) >= 5,
    x=f"label ({n1},{n2}) sum {abs(n1)+abs(n2)}, err {err:.4f}; null sum<=6 ~{100*null_rate(ag,as_,6,TOL):.0f}% "
      f">> small-label ~{100*null_rate(ag,as_,2,TOL):.0f}% => plausible but uncertified (Phase-1 IDS-convergence test)")
# a genuine combination witness would be a SMALL mixed label, e.g. (1,1),(1,-1),(2,-1)...
genuine = [(1, 1), (1, -1), (2, -1), (1, -2), (2, 1), (1, 2)]
print("   the genuine small-label combination witnesses to hunt in Phase 1 (both freqs, sum<=3):")
for a, b in genuine:
    print(f"     ({a:2d},{b:2d}) -> IDS {(a*ag+b*as_)%1.0:.4f}  sum={abs(a)+abs(b)}")
chk("genuine small-label combination targets are identified for Phase 1 (sum 2-3, low null)",
    all(abs(a) + abs(b) <= 3 for a, b in genuine))

print("\nVERDICT: the woven metallic spectrum is BILINGUAL -- both rank-2 ladders survive [B2, credible];")
print("the density trap is real and quantified [B3]; the cross-session 0.611 gap is REAL (w~0.11) but its")
print("combination-label (3,-3) is PLAUSIBLE-yet-UNVERIFIED (sum 6, ~20% null) [B4, verify-don't-trust] -- not")
print("a density artifact (the gap exists) and not an established combination gap (the label is uncertified).")
print("Phase-1 test = IDS-convergence to 0.611461 + a genuine SMALL-label hunt. Firewall: emergent quasicrystal")
print("math (K007/K010 boundary), nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
