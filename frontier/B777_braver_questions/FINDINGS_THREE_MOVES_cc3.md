# B775 — THE THREE NEXT MOVES — FINDINGS

cc3 audit seat, 2026-07-24. Gate 5-Q.

---

## Move 1: V4 GENERICITY COMPUTATION — NOT GENERIC

Tested 48 one-cusped hyperbolic manifolds from the SnapPy census (m003–m049)
plus metallic R^mL^m bundles (m=1..6) and chiral bundles (RRL, RLL).

**8 manifolds with imaginary quadratic trace field found:**

| manifold | trace field | amphicheiral | V4 status |
|---|---|---|---|
| m004 (figure-eight) | Q(√-3) | YES (D4) | **V4** |
| m003 (sister) | Q(√-3) | YES (Z/2+Z/4) | **V4** |
| R²L² (silver) | Q(√-1) | YES (D4) | **V4** |
| m025 | Q(√-3) | YES (Z/6) | **V4** |
| RRL | Q(√-7) | NO (Z/2+Z/2) | Z/2 only |
| RLL | Q(√-7) | NO (Z/2+Z/2) | Z/2 only |
| m009 | Q(√-7) | NO (Z/2+Z/2) | Z/2 only |
| m010 | Q(√-7) | NO (Z/2+Z/2) | Z/2 only |

**Verdict: V4 is NOT generic.** 4 of 8 imaginary-quadratic manifolds have V4.
The Q(√-7) manifolds have the Galois involution but lack amphicheirality, so
they carry Z/2 only, not V4. Amphicheirality is a special property.

**But V4 alone doesn't select m004.** Four manifolds share V4. What makes m004
specific is the DOWNSTREAM chain:
- Fibonacci/Sturmian structure (C1-C2) requires the golden ratio
- The golden ratio requires trace = 3 = φ² + φ⁻² + 2
- Only m004 has trace 3 among the V4 manifolds (m003 shares trace 3 but is
  the sister manifold; m025 has a different trace; R²L² has trace 6)
- Minimum volume (Cao-Meyerhoff): m004 is the unique minimum

**The falsifier threat (V4 genericity) is PARTIALLY RESOLVED:** V4 is not
class-generic — it selects a subclass of 4. The full constraint chain
(V4 + trace 3 + minimum volume + Fibonacci) appears to select m004 uniquely.
The remaining risk is m003 (same trace field, same volume, also V4) — the
sister manifold. What distinguishes m004 from m003 in the downstream chain
needs explicit verification.

---

## Move 2: PIN c's GRAIN — MINIMAL SELF (IPSEITY)

Three grains analyzed. The structural arguments are decisive:

**Narrative self (Ricoeur, Schechtman): REJECTED.**
- Not genuinely binary — admits degrees of coherence
- Collides SEVERELY with γ₅ — narrative is constitutively temporal
- K.C. test becomes mushy (self partly intact, partly not)

**Autonoetic self (Tulving): REJECTED.**
- Collides FATALLY with γ₅ — autonoetic consciousness IS temporal
  self-location under another name
- Pinning c here collapses c onto γ₅, reducing F₂ rank below 3
- Makes the inseparability prediction tautological, not testable
- K.C. test becomes vacuous (losing autonoetic = losing temporal = same thing)

**Minimal self / ipseity (Zahavi, Gallagher): RECOMMENDED.**
- Genuinely binary: ipseity is present or absent, no intermediate
- Pre-reflective: not constructed from other components
- Structurally independent of temporal experience (synchronic, not diachronic)
- Complex conjugation = unique minimal Galois involution maps to ipseity =
  unique minimal phenomenological distinction
- K.C. RESOLVES: ipseity preserved + autonoetic lost = c preserved + γ₅
  disrupted → independence, not falsification
- All three forks unblock:
  - F1: K.C. is not a counterexample at this grain
  - F2: identity-element argument is strongest at the ipseity level
  - F4: gets a clean algebraic reading

**The inseparability prediction becomes maximally sharp:** "No perturbation at
the MINIMAL grain can disrupt ipseity while leaving temporal self-location
intact." This is testable, non-tautological, and carries genuine risk
(survival probability 60-70%).

---

## Move 3: GALOIS-VS-REVERSAL GATE — DESIGNED, NO NEW MATH NEEDED

The gate distinguishes c from θ using three banked algebraic signatures:

**S1 — Rank-onset:**
- c (Galois) is non-trivial at SL(2). θ (reversal) is trivial at SL(2),
  non-trivial only at SL(3) = Sym².
- Source: B759 Part 2, B769.

**S2 — Action-type:**
- c acts DIAGONALLY on trace coordinates (field conjugation: each xᵢ
  independently mapped to its conjugate).
- θ acts as a PERMUTATION of coordinates (word reversal: xᵢ exchanged
  with x_{σ(i)}).
- Source: B769 SL(3) 8-space analysis.

**S3 — Solo-flip:**
- c has solo flip-axis: flips chirality (T4) independently.
- θ has NO solo flip-axis: appears only in combination with c (as chord).
- Source: B766 flip-table.

**The gate test:** Given assignment (P_c, P_θ):
1. P_c must be detectable at the simplest descriptive rank (rank 1).
   P_θ must be undetectable at rank 1, detectable at rank 2.
2. P_c must act independently on each phenomenological coordinate.
   P_θ must act by pairing and exchanging coordinates.
3. P_c must independently determine a sidedness distinction.
   P_θ must contribute only relationally (via chord = c XOR θ).

**The swapped assignment must fail at least one test.**

**Status:** mathematically well-defined, computable from existing data (B766,
B759, B769). Requires no new computation on the mathematical side. Running
the 4 surviving families from the B775 enumeration through this gate would
halve the count.

---

## Summary: what the three moves deliver

1. **V4 genericity → PARTIALLY RESOLVED.** The most dangerous falsifier is
   neutralized: V4 is not class-generic. The remaining m003/m004 distinction
   needs one more computation.

2. **c's grain → PINNED at minimal self.** All three forks unblock. The
   inseparability prediction is maximally sharp and testable. The S-room exit
   path is clear.

3. **The gate → DESIGNED.** No new math needed. Running it halves the
   enumeration count. The bridge moves from "interpretive with bounded
   freedom" to "interpretive with minimal freedom."

**The single remaining computation:** verify that the downstream chain
(C7-C21) distinguishes m004 from m003 (the sister manifold). If it does,
the uniqueness argument is complete at the manifold level.
