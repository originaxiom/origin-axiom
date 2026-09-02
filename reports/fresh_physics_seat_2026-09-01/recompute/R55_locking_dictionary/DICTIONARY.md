# The locking dictionary — what the object predicts once reality has chosen the bits

**Date:** 2026-09-02. **Seat cell R55.** Built at the owner's request ("it's not what I want but what reality chooses" /
"please build it"). Computation: `r55.py` (`r55_output.txt`, `r55_results.json`). Status of every physical number below:
standard textbook/PDG values quoted from memory for the SIGN only; each must be checked against the current PDG before
any use. Nothing here is banked; this is a proposal with its own falsifiers attached.

## 0. The claim being tested

The object m004 cannot choose its odd bits (B1163 theorem; R54). Reality has chosen them. The object's remaining content
is the LOCKING between bits: B766's table says that under the three closing involutions {c, θ, γ5},

    T4 (chirality-side)  flips under c only            (1,0,0)
    T6 (chord-sign)      flips under c and θ           (1,1,0)  = T4 ⊕ θ
    T7 (time-direction)  flips under γ5 only           (0,0,1)
    T3 (basepoint-bit)   flips under γ5 only           (0,0,1)  = T7
    no axis              flips under c and γ5 together (1,·,1)  absent

R55 Part A re-derives the c and γ5 columns from the manifold's symmetry group (R54e) and takes the θ column and the T3
identification from B766 (marked NOT re-derived). The dictionary maps these to measured signs. If reality's signs violate
a locking, the dictionary (and with it the object's claim to describe reality's discrete choices) is refuted.

## 1. Reality's bit space (Part B)

A world carries three discrete choices: h (which chirality the weak current couples), m (which charge sector is
"matter"), t (the arrow). P flips h, C flips m, T flips t. CPT is a theorem, so (h, m, t) ~ (h+1, m+1, t+1): the physical
bit space has rank **2**, and mod CPT there are exactly three nontrivial flips, P ~ CT, C ~ PT, T ~ CP. Any measured
nonzero sign is CPT-even, so its parities satisfy ε_P ε_C ε_T = +1 and it is one of four types:

| type | (ε_P, ε_C, ε_T) | measured examples (sign statements, convention-free) |
|---|---|---|
| EVEN | (+,+,+) | masses, rates |
| **W** handedness | (−,−,+) | Wu 1957: β⁻ electrons from polarised ⁶⁰Co emerge preferentially opposite the nuclear spin; Goldhaber–Grodzins–Sunyar 1958: the neutrino helicity is negative |
| **K** CP/T rate asymmetry | (+,−,−) | K_L semileptonic charge asymmetry δ_L = [Γ(π⁻e⁺ν) − Γ(π⁺e⁻ν̄)]/sum ≈ +3.3×10⁻³ (K_L prefers the positron); CPLEAR A_T ≈ +6.6×10⁻³ (K⁰→K̄⁰ faster than K̄⁰→K⁰); the baryon excess η_B ≈ +6×10⁻¹⁰ taken with the arrow (matter = the sector containing our electrons) |
| **E** EDM-type | (−,+,−) | electron, neutron, atomic EDMs: only upper bounds today; no measured sign |

The object's rank is 3 = {c, γ5} on the manifold + θ on the representation; reality's world-bit rank is 2. The
dictionary therefore maps {c, γ5} onto two of the three physical flips, and θ is left as the third bit (its natural
type-match, the SL(2)/PSL(2) central sign = the sign of a 2π rotation on spinors, is recorded as a type-match only).

## 2. Every dictionary (Part C, exhaustive)

Six assignments of (c, γ5) to distinct flips in {P, C, T}; the object's own axis semantics (T4 is a handedness, so
P-odd; T7 is a time direction, so T-odd) reject three. The survivors:

| dictionary | T4, T6 (chirality row) | T7 = T3 (time row) | the absent (odd,odd) axis | status today |
|---|---|---|---|---|
| **c = P, γ5 = T** | W-type (handedness signs) | K-type (CP/T rate asymmetries) | E-type | both rows populated by measured signs: **testable** |
| c = C, γ5 = T | W-type | E-type (EDM signs) | K-type | time row unmeasured |
| c = P, γ5 = C | E-type | K-type | W-type | chirality row = EDM signs: implausible by the axis's meaning |

## 3. The predictions of the testable dictionary (c = P, γ5 = T)

**P1 (row locking, time row).** T7 = T3: the arrow-relative matter excess and the K_L charge asymmetry are one bit. Their
relative sign is fixed. With one universe this is one data point (η_B > 0 with δ_L > 0 in our sector labelling) and
cannot be falsified alone; it becomes a test only across independent K-type signs. In the SM all CP asymmetries descend
from one CKM phase, so their relative signs are already fixed; the object adds nothing testable here unless a K-type
sign outside the CKM sector (a lepton-sector CP asymmetry, e.g. the sign of δ_CP in neutrino oscillations) is measured:
**the dictionary predicts its sign is not an independent bit.** That is measurable this decade (DUNE, Hyper-K).

**P2 (row locking, chirality row).** T6 = T4 ⊕ θ: the chord sign is a second W-type sign locked to the weak handedness
up to the lift sign. The record has no physical reading of the chord (TERMINOLOGY: "the mirror-coupled double"). Until
one is named, P2 is a slot, not a prediction. Candidate readings must be P-odd, C-odd, T-even signs distinct from the
weak handedness itself: e.g. the sign of the parity-violating asymmetry in a neutral-current process (atomic PV, Møller
scattering) relative to the charged-current handedness. In the SM these are locked by the gauge structure (one θ_W);
in generic new physics they need not be. **The dictionary predicts: all W-type signs are one bit up to θ.**

**P3 (the absent axis).** The object has no (c-odd, γ5-odd) axis, so E-type signs are not closing bits: **every EDM sign
is the product of the handedness bit and the CP bit.** Consequence: the relative signs of the electron, neutron and
atomic EDMs are predicted fixed. In the SM (one phase) they are; in generic new physics they are independent. **Two
measured EDMs decide it.** This is the sharpest falsifier the object offers, and it is remote (no EDM has a measured
sign yet).

**P4 (exclusions, already decidable).** No K-type sign may sit in the chirality row and no W-type sign in the time row.
If any arc reads the chord sign as a CP asymmetry or the basepoint as a handedness, that reading is refuted by CPT plus
the object's own table. The sweep found no such reading in the record (Phase G); the exclusion stands as a rule for
future arcs.

## 4. What is NOT predicted, stated plainly

- Which sign reality chose, for any bit. The object cannot (B1163).
- That the object's mirror IS physical parity. The dictionary is an assignment tested by its consequences; c = P is the
  survivor that is testable today, not a derivation. Phase E's identification-by-type warning applies to every row.
- Any magnitude. All statements are sign relations.

## 5. Protocol (what reality does next)

1. Freeze the dictionary c = P, γ5 = T with the four axis readings above; record it as a declared input (E1 discipline).
2. P1 test: when the leptonic CP phase δ_CP has a measured sign at ≥ 3σ, its sign must equal the sign predicted from the
   K_L / baryon bit through the same locking; write the predicted sign down BEFORE the measurement, from the θ and
   convention analysis, or declare that the dictionary fixes only the relative sign and cannot predict it (then P1 is
   empty for this observable and must be said so).
3. P2 slot: name a physical reading of the chord sign or leave the row open. Do not fill it by type-match.
4. P3 test: when two EDMs have measured signs, compare with the product rule.
5. If any test fails, the dictionary fails, and with it the reading of the object's closing lattice as reality's bit
   space. If all pass, the object has said something true about reality's choices that it did not put in by hand.

## 6. The honest summary

Reality has already chosen three bits; the object is symmetric under all of them. The object's whole remaining claim
about those choices is the locking table, and the locking table says: handedness signs are one bit, CP/T signs are one
bit, EDM signs are their product. That is a real, falsifiable structure, and in the Standard Model it happens to be true
for a different reason (one gauge structure, one CKM phase). The test that separates "the object knows this" from "the
SM knows this" is a sign outside the SM's single-phase sector: a leptonic CP phase or a second EDM. Those are the
measurements to wait for, and the predicted relations should be written down before they arrive.
