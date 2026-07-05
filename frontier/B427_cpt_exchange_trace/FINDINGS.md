# B427 — the seam as a twisted exchange trace: base identity TRUE, corollary CORRECTED — exchange is Galois (σ₁₇), and it FIXES √−15

**Status: banked. Chat-1's §1 handoff adjudicated: the theorem survives, the corollary needed a
correction, and the correction is itself a structural discovery. Firewalled.**

## Verified (Chat-1's base result — clean)

1. **The identity** tr_V(W₁·Par·W₂) = tr_{V⊗V}(Q·(W₁⊗W₂)), Q=(Par⊗I)P: four-line algebra, true.
2. **Q⁴=I with multiplicities {+1:57, −1:56, +i:56, −i:56}** on ℂ²²⁵: Q is the permutation
   (m,n)→(−n,m) on (ℤ/15)²; one fixed point (0,0), 56 four-cycles, no two-cycles (15 odd). Exact.

## Corrected (the Q³ step fails on the actual matrices)

Chat-1's projector-trace corollary assumed tr(Q³·A)=tr(Q·A) ("reversed seam = seam"). **False:**
on the exact theta-lifted Weil matrices, C = tr(Par·W₂W₁) = ζ₁₅ but C′ = tr(Par·W₁W₂) = ζ₁₅².
The corrected projector traces (T = trW₁·trW₂, S = tr(ParW₁)·tr(ParW₂)):

    tr P₊₁ = (T + S + C + C′)/4        tr P₊ᵢ = (T − S + i(C′−C))/4
    tr P₋₁ = (T + S − C − C′)/4        tr P₋ᵢ = (T − S − i(C′−C))/4

The ±1 sectors see the **symmetrized** seam (C+C′)/2; the ±i sectors see the **antisymmetrized**
(C−C′)/2 — not "only T−S" as claimed. (Chat-1's (T±2C+S)/4 holds only if C′=C.)

## The structural payoff (new): exchange = the Galois element σ₁₇, and it fixes √−15

C′ = σ₁₇(C): the exchange W₁W₂ → W₂W₁ acts on the seam trace by a **Galois element** of ℚ(ζ₆₀)
(the k with 4k≡8 mod 60, gcd(k,60)=1: k ∈ {17,47}). σ₁₇ **fixes i, flips √5 and √−3
individually — hence FIXES √−15 = √5·√−3.** So:
- the seam's physical (√−15) channel is **exchange-symmetric**;
- the exchange asymmetry lives entirely in the √5/√−3 side channels;
- this extends the banked "symmetries ARE Galois" law (P61/B380; B369: rotation = the √5-Galois
  involution; now: **exchange = σ₁₇**).

## Bar note (firewall)

"CPT-twisted" is a label for the inversion x→−x on ℤ/15; nothing here is a physics claim. The
content is finite algebra + Galois bookkeeping; the productive part is the exchange-Galois law
and the symmetric/antisymmetric seam split across the Q-sectors.

**Provenance.** cpt_trace.py → cpt_trace.json; lock tests/test_b427_cpt_trace.py.
Machinery: B367 step0_exact_matrices (theta W's), B358 cyclo_engine (exact ℚ(ζ₆₀)).
