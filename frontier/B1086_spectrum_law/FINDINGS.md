# B1086 — THE SPECTRUM LAW: the corpus's 5 and 2 are one law, and no closed double is chiral in counts (L79 CLOSED at its headline)

**Date:** 2026-08-19 · **Verdict: PROVED (with one named residual)**
**Provenance:** the outside bench's VII.0–VII.4 (certificate twisted_double.py). **Three
evidence layers on this bench:** (1) the certificate re-run green here END-TO-END (3003
Chevalley brackets, the full MV table, both gluings); (2) corpus corroboration at both
endpoints; (3) a commissioned independent own-code spot-check (fresh Fox/MV pipeline,
exact ℚ(√−3) via restriction-of-scalars + multi-prime modular ranks).

## 1. The law (all rows reproduced on this bench; identity AND Galois-mirror gluings agree)

h¹(D_t; 27) for the double of the figure-eight complement with edge twist by the dial:

| dial | t = 0 | t ∈ {1, 2, ω} |
|---|---|---|
| none | **5** (3+2) | — |
| θ-odd (hv8 or hv16, the slots {4,8}) | 5 | **2** (1+1) |
| θ-even (hv14) | 5 | **5** (3+2) |

- **The untwisted 5 = B1036's banked two-route number, blockwise (2+2+1)** — and the
  independent own-code rebuild here confirms it exactly (h¹(M;27) = 3 = 1+1+1 solo; the
  Riley quadratic and the longitude λ = w·w*, trace −2, re-derived from scratch).
- **The twisted 2 = B634's erratum prediction — and its "full-E₆ bends m = 4, 8" are
  exactly the θ-odd slots {4,8}.** The corpus predicted this law's second point two
  months early, in the bent-amalgam language.
- **Only the θ-odd dial changes the interface spectrum** — the same slots {4,8} that
  carry the arrow, the torsion signs, and the E₆-closure.

## 2. The independence finding (the residual, stated at its exact size)

The commissioned spot-check established that **the 2 is dial-SPECIFIC, not generic**: an
inner (monodromy) twist is absorbable and returns 5; a naive grading involution is not
even chain-map-compatible (produces impossible negative ranks — ill-defined, diagnosed
explicitly). The switch therefore requires precisely what the dial is — nontrivial,
meridian-commuting (peripheral-compatible), and NOT inner. **The named residual: an
own-code rebuild of the dial matrices themselves** (the e-centralizing highest vectors
hv8/hv16); until then the twisted rows rest on the verified certificate + the B634
corroboration. (Methodology catch preserved: sympy nsimplify silently corrupted an exact
rational at k=16 in the fresh pipeline — caught by functoriality gates; exact pairs
(P,Q) with s²=−3 and multi-prime modular ranks are the robust pattern.)

## 3. The chirality verdict at count level: ZERO, structurally

h¹(D_t; 27) = h¹(D_t; 27̄) in EVERY cell (both slots, both gluings, all t — the 27̄ rows
identical on this bench), exactly as Poincaré duality forces for any closed double: the
pairing lands in the trivial charge, pairing q with −q. **The θ-odd twist buys full-E₆
closure (the genericity sweep: bracket closure dim 78 at all six (slot, t) cells — L79
sub-item i CLOSED, B582 extends to the special values) at the price of matter
multiplicity (5 → 2), and what survives is vector-like in count. B582's "CHIRAL" was a
closure statement, never a spectrum statement — its own firewall said so; now it is a
computation.** No closed double can be chiral in counts; chirality needs a cut (B1085)
or an isolated conical point (B1084's hatch). PD-pairing = AW non-isolation =
completion-kernel: one theorem, three languages.

## 4. L79 disposition

The "either answer banks" cell has its answer: **chirality-capable (group level),
chirality-empty (count level)** — headline CLOSED. Sub-item i (genericity at t ∈ {2,ω})
CLOSED. Sub-item ii (geometric realization) informed: the θ-odd twist is E₆-native, not
induced from any SL(2) structure — realization must be sought at bundle level. Sub-item
iii (torsion-sign ↔ dial-switch one-loop identity) FED by the law's parity structure.
The residual opening: the graded pieces h¹_q (PD balances totals only) → B1087.

**Locks:** tests/test_b1086_spectrum_law.py (the own-code untwisted pipeline: h¹(M;27)=3,
h¹(D;27)=5 blockwise — the independently-rebuilt rows). The mirror=Galois identity that
rides this arc (gal(ρ(λ)) = ρ(λ)⁻¹ exactly, meridian fixed) was independently verified
with fresh field arithmetic + 50-digit numerics — B570's c-chirality line is now a
computed peripheral fact.
