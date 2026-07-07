# B465 — the "8×4×3 two-generator monodromy" handoff: VERIFIED exactly, then DERIVED link by link

**Status: banked (frontier). Firewalled. Intake + reading rules: `INTAKE.md` (committed
before the exact runs). Verdict: Chat-2's 8-4-3 is REAL and now EXACT (three split primes,
cross-agreeing) — and the entire phenomenon launders through a five-link derivable chain
whose only object-input is one Fricke trace. The SU(3)/SU(4) readings are REFUTED at the
eigenspace level, not merely unmatched. One genuinely new exact fact was found underneath
(the spectrum's field of definition = ℚ(√−3)); two of the handoff's claims are corrected;
three await constructions the other seats have not shared. No H1.**

## Reproduction (C1) — exact, F_p at p ∈ {61, 421, 541} (all ≡ 1 mod 60), cross-agreeing

M(l) = Par·W₁·W₂^l (the reconstruction validated against the handoff's own table).
**M(1): order 60; eigenvalues ζ₆₀^{8,23,38,53} with multiplicities (4,4,3,4); order
multiset {60: 8, 15: 4, 30: 3} — the claimed 8-4-3, exact.** But the parsimonious law the
handoff missed: **M(1)⁴ = ζ₆₀³²·I** — the spectrum is the μ₄-coset ζ₆₀⁸·{1,i,−1,−i}.
There are FOUR eigenvalues, not three multiplets: the "octet" is **4 ⊕ 4 — two eigenspaces
with DIFFERENT eigenvalues** (ζ₆₀²³, ζ₆₀⁵³) that merely share the property of being
primitive 60th roots.

## The mechanism (C2) — every link named, the launder complete

1. **Fricke**: tr(A₁A₂) = tr(A₁)tr(A₂) − tr(A₁A₂⁻¹) = 3·6 − 3 = **15 exactly**
   (A₁ = RL golden, A₂ = R²L² silver, classical).
2. **⇒ tr(−A₁A₂) ≡ 0 (mod 15) ⇒ (−A₁A₂)² = −I (Cayley–Hamilton) ⇒ classical order 4.**
3. **Egorov (banked B376)**: the Weil functor sends classical order to quantum order up to
   scalar ⇒ M(1)⁴ = scalar·I.
4. Weil-representation character arithmetic (Gauss sums) fixes the eigenspace dims
   (4,4,3,4) on ℂ¹⁵ — computed exactly here; standard-shaped (lit anchor: finite Weil rep
   character theory), symbolic certificate = named follow-up.
5. The "periods" 60/15/30 are the dressing arithmetic of the scalar ζ₆₀⁸ on the μ₄-coset
   — which k in {8, 23, 38, 53} is a primitive 60th/30th/15th root.

**The l-sweep is a function of the classical shadow** (verified l = 0..11): classical
(ord, tr) of −A₁A₂^l mod 15 determines the spectral type exactly — (4, 0) → the 8-4-3;
(20, 12) → 15 singletons, order-counts (1,2,4,8) at orders (6,12,30,60); (20, 3) → the
11-fold (2,2,2,2,1⁷). **The handoff's "period 3 in l" is WRONG**: the true structure is
**period 6** — A₂⁶ = 11·I is CENTRAL in SL(2,ℤ/15) — with the reflection l ↔ 5−l. (l=1 ≅
l=4 comes from the reflection, not from a period 3; the seats extrapolated from two
points.) **Bin: LAUNDERS — the Weil functor reading SL(2,ℤ/15) conjugacy-class arithmetic;
the one object-input is Fricke's tr(A₁A₂) = 15.** The numerical coincidence tr(A₁A₂) =
15 = the seam level (both = 3·5 from golden/silver arithmetic) is recorded as a hint
(HINT_LEDGER), not banked: it is exactly why the collapse-to-order-4 happens AT level 15
(tr ≡ 0 only at N | 15).

## C8/C9 — the SU(3)/SU(4)/Pati–Salam readings: REFUTED at the eigenspace level

- The SU(4)→SU(3) adjoint branching (8+3+3̄+1) requires an irreducible 8-dim structure.
  **No 8-dim invariant subspace exists**: the invariant decomposition is eigenspaces
  4⊕4⊕3⊕4 of an order-4-mod-scalar operator. The "8" is the SUM of two distinct
  eigenspaces — an artifact of grouping by primitivity of the eigenvalue.
- "Does the 4 = 3̄+1?" is **ill-posed as stated**: no second commuting observable is
  supplied that could canonically split the quartet eigenspace (the commutant is
  u(4)⊕u(4)⊕u(3)⊕u(4) — any split exists, none is canonical). And even granting one, the
  branching comparison is already dead (previous bullet).
- "15 = SU(4)/SO(6) adjoint": 15 here is dim of the Hilbert space at level N = 15 — the
  seam level (whitelist), not an adjoint of anything constructed. HELD(value-matching)
  stamps per B452's frozen rule; nothing fires.

## The genuinely new exact fact underneath (banked as arithmetic)

**The Galois stabilizer of spec(Par·W₁) is {c ∈ (ℤ/15)*: c ≡ 1 mod 3} = ker(c|3)** — the
ℚ(√−3)-fixing subgroup (exact, two primes). Equivalently: the characteristic polynomial of
the single-generator quantum monodromy has coefficients in ℚ(√−3) (·ℚ(i) from the fixed
ζ₄) — **the figure-eight's trace field appears as the spectrum's field of definition.**
The 8 Galois conjugates form exactly **2 spectral classes, split by c mod 3 — NOT by the
Legendre/QR class**: {1,4,7,13} vs {2,8,11,14}. This simultaneously:
- corrects Chat-1's "all 8 c-values have distinct spectra" (float phase-labeling conflation;
  the exact count is 2 classes), and
- corrects the QR-attribution instinct (the banked B402/B459 QR/NQR splits live on the
  ADDRESS torus; the operator SPECTRUM splits mod 3).
Bin: derived arithmetic (the 3-part of the level-15 Gauss sums) — consistent with the
Inversion Law (K020): the object forces its arithmetic; class structure, not fingerprint.

## The claims that did not survive or await constructions

- **C4 (QR c → 15 modes, NQR c → 9): NOT REPRODUCED — and cannot be true under any pure
  Galois twist** (conjugation preserves multiplicity structure a priori; empirically all
  8 c-twists give 15 distinct eigenvalues). Their "c-operator" must be a different twist
  (address/character twist, not Galois). **Awaiting Chat-2's construction.**
- **C6 (max|tr| = √5 at c=1 vs √15 others)**: under both power-trace readings the result
  is UNIFORM in c (|tr(U^j)| = 15 at central powers; max nonscalar = 5.000 exactly, all
  c). The claim most plausibly lives on the per-address pair traces — which is the banked
  B459 tier-table content (values in subfields; |√5| vs |√−15| magnitudes are
  channel-occupancy-forced, as already adjudicated there). **Awaiting Chat-1's
  construction.**
- **C5 (32 loops, non-abelian monodromy, cycle structure 8×4×3) and C7 (dark points carry
  12.2 vs 8.2 phases)**: floating-point, constructions not shared. Recorded;
  burden-inversion applies on arrival. Note the constraint the exact spectrum already
  imposes on C5: at l=1 there are only 4 distinct eigenvalues, so any "eigenvalue
  permutation" with 8-, 4-, 3-cycles must act on eigenVECTOR labels (a bundle-monodromy
  statement, not a spectrum statement) — the two seats' "same 8-4-3" (Chat-1 cycles vs
  Chat-2 periods) are PRIMA FACIE DIFFERENT objects, and any identification needs the
  loop construction.

## What to send back to the other seats (the report's ask)

1. Chat-2: the exact definition of the c-twisted operator behind "NQR gives 9 modes."
2. Chat-1: the loop family (which torus, which basepoint operator) behind the 32-loop
   monodromy and the per-point family behind the dark-point phase counts + max|tr|.
3. Both: the corrected facts — period 6 (not 3) in l via the central A₂⁶; the μ₄-coset
   scalar law; 8 = 4⊕4; the mod-3 (not QR) spectral split.

## Reproduce
```
python3 exact_engine.py        # ~4 min: all exact claims, three primes, ALL CHECKS PASS
pytest ../../tests/test_b465.py
```
