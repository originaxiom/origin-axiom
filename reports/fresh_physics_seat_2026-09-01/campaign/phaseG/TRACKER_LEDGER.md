# Phase G — the tracker enumerated: every listener/observer/seam definition in the record, classified by what it does under the object's own symmetries

**Date:** 2026-09-02. **Owner's instruction:** "regarding what the tracker does to the world, we need to compute all
possible options and not lean on my intuition or opinion but on math." **Method:** 58 arcs (every arc on any head named
listener / observer / hearing / seam / tracker / closing / witness / measurement) read by cheap sonnet agents into 79
definitions (`results/tracker_sweep.tsv`, `results/DIGEST.md`); the classification below is the seat's, from R54/R54e.

## 1. The mathematics that enumerates all options (R54, R54e)

A tracker is any function T of the object (its word, monodromy, character, cusp, or manifold). The object's own
symmetry group Sym(m004) = D4 (order 8; 4 orientation-reversing elements; the cusp image is (ℤ/2)² = ⟨mirror, flow
reversal⟩) acts on every such function. Representation theory of D4 gives the complete list:

| type | behaviour under the object's symmetries | what it costs |
|---|---|---|
| (even, even) | blind to the mirror and to flow reversal | nothing: object-canonical |
| (mirror-odd, even) | flips sign under the mirror c (= complex conjugation on ℚ(√−3)) | one chosen bit: sheet / embedding / step parity |
| (even, time-odd) | flips under flow reversal A ↦ A⁻¹ (= the √5 Galois flip γ5, φ² ↦ φ⁻²) | one chosen bit: arrow / basepoint (B766: T7 = T3) |
| (odd, odd) | flips under both | two bits |
| doublet | an unordered pair exchanged by the group | one labelling bit |

plus the SL(2)/PSL(2) central lift sign θ (B585, B766), which is a symmetry of the representation, not of the manifold,
and costs a third bit when a tracker sees it. This is exhaustive because the character table of D4 is exhaustive; it
reproduces B766's rank-3 lattice {c, θ, γ5} and B1164's "two discrete bits + one dilaton" (the dilaton is the ℂˣ scale,
B1166 C3). No tracker derives a bit; every odd tracker consumes one.

## 2. The record's trackers, classified

| family | definition (from the arcs) | inputs → outputs | parity | chosen bit | status |
|---|---|---|---|---|---|
| Dehn slope (B286, B287, B717#1, B432, B434) | oriented slope (p,q) on the cusp → closed manifold, CS(p,q) | slope → manifold, CS, core length | CS mirror-odd; \|slope\| even | sign of q (the mirror); magnitude 5 forced by exceptional slopes | STANDS |
| Galois sheet / embedding (B713, B717#3, B1163, B8154, B321#2 Im w>0) | choice of ℚ(√−3) ↪ ℂ | free ℤ/2 torsor → a side | the mirror bit itself | yes (this IS the bit) | STANDS (B723's SSB version RETRACTED by B942/B957) |
| Listener direction u (B593, B856, B751, B1070/B1071 Λ) | h(g,u) = u†M_odd(g)u; Λ = Galois-fixed pair {u3,u6} | word g, direction u → complex h | Re h (even, listener-invariant to 2e−16); Im h / arg h doublet-odd (u3 ↔ u6 conjugate) | which of u3/u6 = labelling bit; B1070 derives the PAIR, not the point | STANDS |
| θ-odd projector (B584, B585, B592, B640, B642, B594) | tr_odd = ½(Z − Z_C); M_odd = Cρ(g); ρ image 2I × ℤ/3 | word → odd-block trace/matrix | θ-type: sign flips under the C-twist (B592 sign-flip theorem); closed pairings deaf | the lift/twist sign θ | STANDS |
| Galois-conjugate stage (B642) | √5 ↦ −√5 on the stage | word → tr ρ(RL) = −1/φ or +φ | time-odd (γ5) | which √5 | STANDS |
| Par / seam traces (B358–B363, B408, B431, B536) | tr(Par·P_a·Q_b) H-averaged → √−15 coefficient s; DFT S(x,y) | seed pair, lift → s; parity S(−x,−y) = conj S(x,y) | s-sets symmetric ±; DFT parity-conjugate (odd at value level, B431) | theta-characteristic (L57 open: forced or chosen) | data STAND; laws B359–B362 REFUTED by B367 |
| Class-field / congruence (B334, B1029, B704, B708, B731, B733) | Hilbert class field of ℚ(√−15); principal/non-principal; F₂-space of stage discriminants; observer bit count per congruence door | primes, discriminants → labels, dims | even (Galois-invariant identities); B704's "measurement = choice of origin in V" is the declared bit | origin in V | STANDS (B731 RETRACTED in-file, superseded by B734) |
| Time / modular flow (B723#3, B717#2) | Tomita flow of a chosen state; temporal continuation | state ω → clock | time-odd by construction; tracial ω gives Δ = 1 | the state ω | STANDS |
| Pointer tracking (B783) | parent/child choice at each σ-expansion | position, bit → trajectory | P-type (word reversal swaps parent ↔ child, exact) | PARENT/CHILD = the P bit (B1083) | STANDS except the γ5 typing (F5 in the chirality ledger) |
| Real-form involutions (B1134, B1135) | θ ∈ Aut(Φ(E6)) with signed lift, dressed with the observer's antilinear τ | root data → real form label | τ is the mirror bit by declaration | τ | STANDS (frame choice of which A2 = colour declared) |
| Bloch-class completions (B1155, B1156) | one class ξ ∈ K3(ℚ(√−3)) → Vol (archimedean), torsion (finite), GSWZ (p-adic) | ξ → three invariants | Vol even; the archimedean sign is the mirror bit | embedding | OPEN (seam) |
| Centralizers / walls (B874, B892, B893) | Cent(S) of a subtorus of the charge torus in e6; wall point y* | subtorus → dimension; wall → 14 (not 12) | even (dimensions); the wall is complex at every Galois root (a² < 0) | one √−1 per branch (B893) | STANDS (B950 correction: 14 ≠ SM 12) |
| Born form / weights (B725, B726) | \|ψ\|² = ψ·c(ψ); weights d_a²/D² ∈ ℚ(√5); phase in ℚ(ζ5) | amplitude → norm; label → weight | norm even by construction (c-invariant); phase needs ζ5 | none for the form; the bare faces do not close the phase | STANDS (NEGATIVE overall) |
| Refinement measure (B412, B415) | cyclotomic-orbit splitting summing to the parent; N → ∞ Haar-with-Gauss-phase | level → measure | even | none | STANDS (fails its SM bar) |
| Derivation flow (B540) | return-word induction on the prefix window; 12-node flow, σ a fixed point | system → system | even | none | STANDS (known phenomenon, LIT_GATE) |
| Observer card / cut (B1091) | "the observer IS the cut": forced data read at the boundary; free data have no closed readout | observables → boundary values | even for forced, none for free | the free data | STANDS (assembly) |
| Seam envelope (B408, B1048) | RMS over embeddings of the √−15 coefficient | level → ratio | Galois-invariant (even) after correction; the max-selecting version was embedding-biased | none | B408/B426 headlines RETRACTED, B1048 corrects |

Rows counted: DERIVED_FROM_RULE 45, DECLARED_CHOICE 22, NOT_STATED 8, AMBIGUOUS 4 (reader labels). Seat re-typing: of
the 45 "derived" trackers, every one derives an even quantity or a symmetric pair; none derives a sign. Of the 22 declared
choices, every one is a point in one of the torsors above. The two labels are therefore consistent with §1: the record
derives the torsors and declares the points.

## 3. What this settles for the owner's belief

"Everything is derived from the rule and the mechanism that tracks what happens with it" is true of the even part and of
the torsors, and false of the points. The rule gives: the monodromy, the field, the amphichirality, the alternation of
orientation with each tick, the K4 of equivalent rules, the P-type reading bit, the monoid arrow. The tracker, whatever
its definition, is a function on the object and therefore decomposes under D4 as in §1. There is no definition of a
tracker, in the record or possible in mathematics, that outputs a mirror-odd sign without an input bit, because the
mirror is an automorphism of the object (B1163's theorem, R54 §6). The three bits the record has found (c, γ5, θ) are
the three that exist. The honest sentence is: everything is derived from the rule and the tracker, up to three chosen
bits and one scale, and the record has already priced exactly those (B1164, B1166).
