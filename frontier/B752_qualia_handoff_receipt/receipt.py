"""B752 -- the qualia-handoff receipt (prereg ecb2fab7).  Cells per the seal.
Deterministic (seed 7 for the surrogate null); sympy + stdlib; Gate 5 absolute."""
import math
import random

import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
PHI = float(sp.N(phi, 30))

print("=" * 92)
print("CELL 1 -- Op-1: the handoff's requested family scan (sealed family/targets/windows)")
print("=" * 92)
cands = {}
for c_lab, c in (("1", 1.0), ("1/2", 0.5), ("1/3", 1 / 3), ("2", 2.0), ("3", 3.0)):
    for n in range(1, 11):
        cands[f"{c_lab}*phi^-{n}"] = c * PHI**-n
assert len(set(round(v, 12) for v in cands.values())) == 50, "family must be 50 distinct values"
targets = {  # PDG 2024 central values -- adjudication targets only (B655/B743 precedent)
    "sin2_th12_PMNS": 0.307, "sin2_th13_PMNS": 0.0220, "sin2_th23_PMNS": 0.546,
    "sin_thC": 0.2250, "Vus": 0.2243, "Vcb": 0.0408, "Vub": 0.00382,
    "CKM_A": 0.826, "CKM_rhobar": 0.1591, "CKM_etabar": 0.3523,
    "alpha_em_0": 1 / 137.035999, "alpha_em_MZ": 1 / 127.95, "alpha_s_MZ": 0.1180,
    "s2W_MZ": 0.2312, "mW/mZ": 80.369 / 91.1876, "mH/mt": 125.2 / 172.6,
    "m_e/m_mu": 0.5110 / 105.658, "m_mu/m_tau": 105.658 / 1776.86,
    "m_e/m_tau": 0.5110 / 1776.86, "m_c/m_b": 1.27 / 4.18, "m_s/m_b": 0.093 / 4.18,
    "m_b/m_t": 4.18 / 172.6, "m_u/m_d": 0.47, "Koide_Q": 2 / 3, "m_d/m_s": 4.70 / 93.5,
}
assert len(targets) == 25
for wlab, w in (("0.1% (the handoff's rule)", 0.001), ("1% (B751's rule)", 0.01)):
    hits = [(cl, tl, cv, tv) for cl, cv in cands.items() for tl, tv in targets.items()
            if abs(cv / tv - 1) < w]
    print(f"window {wlab}: HITS = {len(hits)}")
    for cl, tl, cv, tv in hits:
        print(f"    {cl} = {cv:.5f} ~ {tl} = {tv:.5f} (off {abs(cv/tv-1)*100:.2f}%)")
# empirical null: 2000 surrogate target sets, log-uniform over the observed target span
rng = random.Random(7)
lo, hi = math.log(min(targets.values())), math.log(max(targets.values()))
vals = sorted(cands.values())
for wlab, w, k_obs in (("0.1%", 0.001, None), ("1%", 0.01, None)):
    counts = []
    for _ in range(2000):
        surr = [math.exp(rng.uniform(lo, hi)) for _ in range(25)]
        counts.append(sum(1 for cv in vals for tv in surr if abs(cv / tv - 1) < w))
    k = sum(1 for cl, cv in cands.items() for tl, tv in targets.items() if abs(cv/tv-1) < w)
    p = sum(1 for c in counts if c >= k) / len(counts)
    print(f"surrogate null @{wlab}: mean hits = {sum(counts)/len(counts):.2f}, "
          f"observed = {k}, empirical P(>= observed) = {p:.3f}")
print("CELL 1 NOTE: at the handoff's OWN 0.1% window the sin2_th12 hit (0.7% off) vanishes --")
print("the claimed two-hit 1/(2phi^n) pattern self-reduces to one hit under its own rule.")

print("=" * 92)
print("CELL 2 -- Op-3a: the scalar collapse is UNIVERSAL (Cayley-Hamilton), proved symbolically")
print("=" * 92)
a, b, c, d = sp.symbols("a b c d")
A = sp.Matrix([[a, b], [c, d]])
Ainv_scaled = sp.Matrix([[d, -b], [-c, a]])          # A^-1 * det(A)
expr = sp.simplify(A + Ainv_scaled - (a + d) * sp.eye(2))   # A + adj(A) == tr(A) I, always
print("CHECK: A + adj(A) == tr(A)*I for a GENERIC 2x2 matrix:", expr == sp.zeros(2, 2))
print("=> with det A = 1: A + A^-1 = tr(A)*I, so Delta(A) = (3 - tr A)*I for EVERY SL(2) matrix.")
print("CELL 2 VERDICT: UNIVERSAL -- the collapse carries zero object content.")

print("=" * 92)
print("CELL 3 -- Op-3b: the input audit (trace 1 is NOT the holonomy)")
print("=" * 92)
R_a = sp.Matrix([[1, 1], [0, 1]])                    # B285 banked Riley holonomy meridian
print("CHECK: banked geometric meridian (B285) trace =", sp.trace(R_a), "(parabolic) -- not 1")
t = sp.symbols("t")
print("CHECK: trace-1 SL(2) charpoly =", sp.factor(t**2 - t + 1), "= Phi_6 (order-6 elliptic;")
print("       B155's PHASE factor -- not the geometric representation)")
print("Delta at the CORRECT holonomy: (3 - 2)*I = I -> scalar 1")
print("CELL 3 VERDICT: the 1/2 result does NOT survive the corrected input; the true")
print("Delta-self-image of the geometric holonomy is I (the trivial tone), immediately fixed.")

print("=" * 92)
print("CELL 4 -- Op-3c: stability (sealed expectation: 1/2 repelling, 1 superattracting)")
print("=" * 92)
x = sp.symbols("x")
f = 3 - x - 1 / x
fps = sp.solve(sp.Eq(f, x), x)
fp_derivs = {str(p): sp.diff(f, x).subs(x, p) for p in fps}
print("fixed points:", fps, "| f' at each:", fp_derivs)
def it(x0, n=40):
    xv = x0
    for _ in range(n):
        if xv == 0 or abs(xv) > 1e6:
            return "diverged"
        xv = 3 - xv - 1 / xv
    return round(xv, 6)
print("orbit from the handoff's seed 2:", [round(v,4) for v in [2, 3-2-0.5]], "-> lands EXACTLY on 1/2 (repelling)")
print("perturbed seed 0.5001 ->", it(0.5001), "| generic panel: 0.7 ->", it(0.7),
      "; 2.0001 ->", it(2.0001), "; 3.1 ->", it(3.1), "; -0.33 ->", it(-0.33))
print("CELL 4 VERDICT: f'(1/2) = 3 REPELLING, f'(1) = 0 SUPERATTRACTING -- 'the object sees")
print("half' is a measure-zero landing on an unstable point from a mislabeled seed; generic")
print("self-inspection sees ONE. Both 1/2 and 1 are tones (roots of (2x-1)(x-1)) -- tone-")
print("membership does not discriminate.")

print("=" * 92)
print("CELL 5 -- citation audit: the handoff cites 'B620' for 1/(2phi); the banked source is")
print("B593 (complex word-level matrix element). B620 = the conductor mechanism (no 1/(2phi)).")
print("=" * 92)
print("RECEIPT COMPLETE")
