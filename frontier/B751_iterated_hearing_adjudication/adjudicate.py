"""B751 -- adjudication of the incoming 1/(2*phi^3) = alpha_s claim (prereg cd550335).

Cells per the sealed prereg.  SM values appear ONLY as adjudication targets
(B655/B743 precedent); Gate 5 absolute.  Deterministic, sympy + stdlib.
"""
import math

import sympy as sp

phi = (1 + sp.sqrt(5)) / 2

print("=" * 90)
print("CELL 1 -- arithmetic (the forced part)")
print("=" * 90)
cand = 1 / (2 * phi**3)
print(f"CHECK: 1/(2*phi^3) = {sp.N(cand, 10)}  (phi^3 == 2+sqrt5: {sp.simplify(phi**3 - 2 - sp.sqrt(5)) == 0})")
# b-density: right Perron eigenvector of the substitution matrix [[1,1],[1,0]]
M = sp.Matrix([[1, 1], [1, 0]])
vec = M.eigenvects()
dom = max(vec, key=lambda t: t[0])
v = dom[2][0]
b_density = sp.simplify(v[1] / (v[0] + v[1]))
print(f"CHECK: Fibonacci-word b-density (Perron eigenvector) = {sp.simplify(b_density)}"
      f" == 1/phi^2: {sp.simplify(b_density - 1/phi**2) == 0}")
print(f"CHECK: (1/phi^2)*(1/(2*phi)) == 1/(2*phi^3): {sp.simplify((1/phi**2)*(1/(2*phi)) - cand) == 0}")
print("CELL 1 VERDICT: TRUE -- the identity is exact; the b-density limit is forced.")

print("=" * 90)
print("CELL 2 -- the assignment audit (derived or inserted?)")
print("=" * 90)
amp = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)
print(f"the BANKED amplitude (B593, word-level, golden word RL): u3' M_odd u3 = {sp.N(amp, 9)}")
print(f"CHECK: |amplitude| = {sp.N(sp.Abs(amp), 9)}  vs the claim's Re-only 1/(2*phi) = {sp.N(1/(2*phi), 9)}")
print(f"CHECK: the imaginary part dropped by the claim = {sp.N(sp.im(amp), 9)}  (NOT small)")
print("grep-audit result (run 2026-07-22, recorded): NO banked per-LETTER hearing weight exists;")
print("the banked 1/(2*phi) is the real part of a COMPLEX WORD-level matrix element at g = RL.")
print("CELL 2 VERDICT: CONSTRUCTED -- word-level Re x letter-density is a free composition:")
print("  insertion 1: per-letter attribution of a word-level quantity (no banked derivation);")
print("  insertion 2: silent Re projection discarding i*sin(2pi/5)/sqrt5 = 0.4253 (|amp| = 0.5257);")
print("  the 'sigma applied to its own data' phrase covers the DENSITY limit only (cell 1).")

print("=" * 90)
print("CELL 3 -- the target audit (is alpha_s a fixed target?)")
print("=" * 90)
# one-loop running, n_f = 5: alpha_s(mu) = alpha_s(MZ) / (1 + b0*alpha_s(MZ)*ln(mu^2/MZ^2))
# b0 = (33 - 2*nf)/(12*pi); anchor: world average alpha_s(MZ) = 0.1180 (PDG 2024, cited)
aMZ, MZ = 0.1180, 91.1876
b0 = (33 - 2 * 5) / (12 * math.pi)
for mu in (10.0, 91.1876, 1000.0):
    a = aMZ / (1 + b0 * aMZ * math.log(mu**2 / MZ**2))
    print(f"  alpha_s({mu:7.1f} GeV) = {a:.4f}")
print("CHECK: the target moves 0.18 -> 0.087 across 10 GeV..1 TeV; the match holds ONLY at mu ~ MZ.")
print("free knobs: renormalization scale (chosen: M_Z), scheme (MS-bar), value source (world avg).")
print("object-side scale-pinning offered by the claim: NONE (no banked structure selects M_Z).")
print("contrast: the sin^2(theta12) comparison went through the B648 calibration machinery ONE-SHOT")
print("and was graded LOW evidential weight (FP ~ 32%, neighbors unseparated); its license is SPENT.")
print("CELL 3 VERDICT: KNOB-DEPENDENT -- the 0.04 sigma framing has no meaning under a free scale dial.")

print("=" * 90)
print("CELL 4 -- base-rate (the owner's requested check; family and table sealed in the prereg)")
print("=" * 90)
PHI = float(sp.N(phi, 30))
cands = {}
for n in range(1, 7):
    cands[f"1/(2*phi^{n})"] = 1 / (2 * PHI**n)
    cands[f"phi^-{n}"] = PHI**-n
# NOTE (instrument fix, logged): the first run also listed phi^-n/2, which is IDENTICAL to
# 1/(2*phi^n) -- double-counting every hit.  Deduplicated to distinct values only.
assert len(set(round(v, 12) for v in cands.values())) == len(cands)
# PDG 2024 central values (cited in prereg; adjudication targets only -- Gate 5)
targets = {
    "sin2_th12_PMNS": 0.307, "sin2_th13_PMNS": 0.0220, "sin2_th23_PMNS": 0.546,
    "sin_thC": 0.2250, "Vcb": 0.0408, "Vub": 0.00382,
    "alpha_em_0": 1 / 137.035999, "alpha_em_MZ": 1 / 127.95, "alpha_s_MZ": 0.1180,
    "s2W_MZ": 0.2312, "m_mu/m_tau": 105.658 / 1776.86, "m_e/m_mu": 0.511 / 105.658,
    "m_c/m_b": 1.27 / 4.18, "m_s/m_b": 0.093 / 4.18, "m_b/m_t": 4.18 / 172.6,
    "Koide_Q": 2 / 3,
}
hits = [(c, t, cv, tv) for c, cv in cands.items() for t, tv in targets.items()
        if abs(cv / tv - 1) < 0.01]
n_pairs = len(cands) * len(targets)
# log-uniform null: P(a random candidate lands within 1% of a given target) ~ 0.02/ln(range)
# integrated over the candidate span [3e-3, 0.5] and 16 targets:
span = math.log(0.5 / 0.003)
p_hit = 0.02 / span
expected = n_pairs * p_hit
print(f"pairs tested = {n_pairs} (distinct candidate values only); matching rule |ratio-1| < 1% (sealed)")
print(f"HITS = {len(hits)}:")
for c, t, cv, tv in hits:
    print(f"  {c} = {cv:.5f}  ~  {t} = {tv:.5f}  (ratio-1 = {cv/tv-1:+.4f})")
print(f"expected hits under the log-uniform null ~ {expected:.2f}")
k = len(hits)
p_ge_k = 1 - sum(math.exp(-expected) * expected**i / math.factorial(i) for i in range(k))
print(f"Poisson P(>= {k} hits | lambda = {expected:.2f}) = {p_ge_k:.2f}")
print(f"CHECK: the n=2 gap -- 1/(2*phi^2) = {1/(2*PHI**2):.4f}; nearest target: "
      f"{min(targets.items(), key=lambda kv: abs(1/(2*PHI**2)/kv[1]-1))[0]}"
      f" (off by {min(abs(1/(2*PHI**2)/tv-1) for tv in targets.values())*100:.0f}%)")
print("CELL 4 VERDICT: the observed hit count is consistent with the null; the claimed pattern")
print("1/(2*phi^n) skips n=2 entirely -- the signature of target-shopping, not of a law.")

print("=" * 90)
print("CELL 5 -- the Fox fixed point: NEEDS-DEFINITION (no well-posed iteration received;")
print("cc3's pre-assessment: dimension doubles per step). Uncounted, per the sealed prereg.")
print("=" * 90)
print("ADJUDICATION COMPLETE")
