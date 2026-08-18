# B1070 — THE LISTENER DERIVATION: u3/u6 are not a convention — they are the unique Galois-fixed vertex pair

**Date:** 2026-08-18 · **Seat:** cc (banking) · Track A of L166 (the crossing door's opening
computations; 3 compute + 3 adversarial-verify agents, 0 errors, every attack failed against
independent re-implementations) · EXPLORATION-GRADE per the dual protocol — the promotion path is
named at the end · Gate 5 untouched: no measured number anywhere.

## A1 — the orbit/stabilizer run (L166's named first computation): EXISTENCE = OUTCOME (b)

(1) Aut(2T×2I) ≅ Aut(2T)×Aut(2I) EXACTLY (≅ S4×S5, orders 24×120; no shear terms — Hom(2I,2T)={0} and the only Hom(2T,2I) landing in Z(2I) is trivial, both exhaustively computed). (2) The 2I-factor's projective image in PU(2) is the full 60-element icosahedral rotation group (= Inn(2I) ≅ A5, cross-validated against (1)); CP¹_odd's orbit structure is exactly 12 (order-5 stabilizer) + 20 (order-3) + 30 (order-2) + everything else size 60 (generic, witnessed). u3, u6 sit EXACTLY on the order-5 axis fixed by R itself (R|_odd is diagonal in the u3,u6 basis, projective order exactly 5) — the size-12 orbit, not 20, not 30, not generic. (3) Gal(Q(ζ60)/Q) (order 16) maps each of the three exceptional orbits bijectively onto itself as a set; WITHIN the 12-point order-5 orbit, u3 and u6 are the UNIQUE pair fixed by every one of the 16 Galois automorphisms (the other 10 points are genuinely permuted, e.g. by k=7). Outer automorphisms of 2I reproduce the Galois √5-flip on the odd-sector character exactly (verified on all 120 elements) — no new symmetry beyond Galois. 2T's factor is always projectively scalar (χ is 1-dimensional) — irrelevant to the PU(2) action. (4) VERDICT (B1040-S3 trichotomy): outcome (b) — a DISTINGUISHED FINITE ORBIT (size 12, order-5/vertex type), with u3/u6 further singled out inside it as the unique Galois-individually-fixed pair. Neither a bare fixed ray nor free/generic action.

**The derivation, stated once:** define Λ = "the directions of ℂP¹_odd lying in an exceptional
orbit of minimal size whose individual points are fixed by all of Gal(ℚ(ζ₆₀)/ℚ)". Then Λ's output
is EXACTLY {u3, u6} — the banked listener convention (B593/B856's GIVEN-not-derived choice) is
DERIVED from field + group data alone: AC1 non-vacuous (excludes all but 2 of the projective line's
points), AC2 field-only (no measured value enters the rule's statement — redaction-stable by
inspection), AC5 orbit-decidable (the trichotomy computed, not asserted). The existence question of
`docs/LISTENER_MAP_SPEC.md` §1.2 closes POSITIVE; the uniqueness question closes as THE PAIR (one
ray per eigenspace of R|_odd, conjugate-swapped by the Galois √5-flip).

## A2 — B641 closed: the odd sector's split into theorem + discriminating channel

B641's ear-independence LAW upgrades to a THEOREM-EXACT over the WHOLE of CP^1_odd (real and complex directions, not just the 6 tested real ears): for every g in <R,L> (all 2880 elements, hence every R^mL^m), M_odd(g) = chi(g)*W(g) EXACTLY, with chi(g) a genuine cube root of unity and W(g) in SU(2) exactly (proved from the generators R,L by a mu3*SU(2) group-closure argument, all arithmetic in Q(zeta_60)); Re(zeta(g)^-1 u^dag M_odd(g) u) = (1/2)tr(W(g)) for EVERY unit u in C^2 follows from 3 lines of SU(2) linear algebra and needs no per-u computation at all. The companion imaginary part -- previously untested and exactly the AC4' discriminating territory the LISTENER_MAP_SPEC names as open -- is ALSO closed form: Im(zeta(g)^-1 u^dag M_odd(g) u) = <n_vec(g), Bloch(u)>, an exact Bloch-sphere pairing whose axis n_vec(g) is computed exactly for m=1..5 and DOES separate points of CP^1_odd at m=1,2,3,4 (two-direction witnesses exhibited exactly); m=5 is the one genuine trivial case (M_odd = -I exactly), independently matching B856 FINDINGS' own "acts as -I on the whole odd plane" claim. Every hypothesis of the candidate theorem was checked to hold (not assumed), and two deliberate near-miss checks confirm the checks are non-vacuous (MB12).

## A3 — the θ-even landscape: where u-dependence actually lives

The even 4-dim sector genuinely varies with the listener u for m=1,2,4 (T_m has exact nonzero eigenvalues +-e_m, e_1=e_4=sin(2pi/5), e_2=sqrt3/2) and is exactly ear-independent for m=3,5 (T_m=0 identically, matching B1011's own 'forced' criterion); the three nontrivial T_m pairwise FAIL to commute exactly, so no canonical simultaneous eigenframe exists across the family; B1011's C6 mirror value is proven (not just observed) to be the u-independent constant (1/4)tr(M_even), and its own code evaluates no u at all.

## What this changes for the crossing cell (design facts, binding on the prereg)

- **The listener is constructed.** The crossing's one unknown is pinned by Λ; nothing about u is
  chosen or fitted downstream.
- **The predicted quantities are the u-dependent functionals at Λ's output**: the odd Bloch
  pairings Im(ζ⁻¹u†M_odd u) = ⟨n(g), Bloch(u3)⟩ (exact axes computed, m = 1..5) and the even
  quadratic forms u†T_m u (nonzero exactly at m = 1, 2, 4; eigenvalues ±sin(2π/5), ±√3/2, ±sin(2π/5)
  — the two ends' flavors; forced-zero at m = 3, 5). **The banked mirror VALUE SET is proven
  u-independent ((1/4)tr)** — so the kind-table's mirror row licenses the SECTOR, and the crossing's
  contact quantity needs its own kind-row adjudication in the prereg (flagged, not assumed).
- **No joint eigenframe exists** (the three nontrivial T_m pairwise fail to commute) — a canonical
  frame cannot be smuggled; any frame choice must be priced under R7.
- **The two-ended flavor split appears in the even eigenvalues** (sin(2π/5) golden at m = 1, 4;
  √3/2 ω-flavored at m = 2) — unprompted, worth the sweep-ledger's eye.

## The promotion path (dual protocol; nothing here is sealed)

1. SEAL a preregistration stating Λ's definition verbatim + the claim Λ(ℂP¹_odd) = {u3, u6} + the
   three theorem inputs (A1's orbit trichotomy; A2's μ₃·SU(2) closure; A3's T_m spectra), each with
   its named fresh-rederivation check;
2. run the sealed re-derivation (independent implementation, the house standard);
3. only then may the crossing prereg cite the derived listener. Prior-art gate at promotion: the
   icosahedral orbit structure on ℂP¹ is classical (Klein); the NEW content is the identification
   of THIS instrument's banked listener pair as the unique Galois-rigid vertex axis, and the exact
   closed forms of both hearing channels.

## Artifacts

- `track_a_results.json` (the three items + the three adversarial verdicts, verbatim).
- The verifiers' scripts lived in the session scratchpad (READ-ONLY discipline; repo untouched by agents).