# B796 WAVE-1 PREREGISTRATION (Cells 1, 2, 3) — sealed before compute

cc3 audit seat, 2026-07-29. Owner greenlight ("execute it"), chat1
final-handoff §5 structure (Cells 1–7 + 8A standalone). Branch-side
seal; cc remains the merge gate. Gate 5-Q. Rung discipline: every
comparison below is rung 1–3 or instrument work; no rung-4 use except
labelled calibration. Conventions per the E21/E23 rules: all quotient
groups named with their orders; the coset group is SL(2,Z[ω]/4)/{±I},
order 1920 (true PSL = 960).

## CELL 1 — GH LADDER (live range r ∈ (10, 13.5))

COMPUTATION: extend the verified hejhal_m004.py scan from r = 10 to
13.5 (dr = 0.002, Y = 0.75, margin 21); two-system refinement of every
dip (Y = 0.75/0.62); eigenspace projection test (S-invariance over the
full nullspace, the B797-addendum instrument) for old/new; parity
census (z → −z̄ and the semidirect-2 generator) on every S-invariant
form found, starting from the banked parent ground state 51.0132434.

PRE-STATED (predictions, never controls — the 51.014-arc rule):
SOME parent (S-invariant) eigenvalues appear near r ≈ 11.0086,
12.5016, 13.2960 (transcription-grade; 122.19 uncorroborated; the GH
table is per-symmetry-type, so NO completeness claim between rungs;
completeness statements come only from the Weyl budget, used as a
±2σ screen per main's B791 caveat).

FALSIFIERS: (a) no S-invariant eigenvalue anywhere near any predicted
rung → indicts the GH transcription or the solver — either is banked;
(b) an S-invariant eigenvalue found FAR from every rung → GH
completeness indicted; (c) projection-test controls (below-ground-
state eigenspaces parent-free; 7.072 reads parent) must pass or the
instrument is indicted, not the mathematics.

## CELL 2 — DOUBLET SURGERY (Hecke discriminator; VALIDATION GATE FIRST)

STAGE 0 (the gate, abort condition): build Hecke coefficient relations
at level (4) from the certified eigenvectors' Fourier coefficients
c(μ). Primes: split π = 3+ω (N = 7), π̄ = 2−ω... (conjugate, N = 7),
and a second split prime over 13 (π₁₃ = 4+ω, N(4+ω) = 16−4+1 = 13);
2 (inert, divides the level) and √−3 (ramified) EXCLUDED. On the
mult-1 certified newforms (r = 4.90008537, 5.91291788, 7.40661560,
7.68767117, 9.02742152, 9.08064862) test, with c normalized by the
smallest-norm nonzero coefficient: multiplicativity
c(π)c(π̄) ≐ c(ππ̄) + (norm-factor per the chosen normalization —
BOTH standard normalizations tested and NAMED), and the Hecke-bound
sanity |λ_π| ≤ 2·N(π)^{1/2} (trivial bound; Ramanujan-grade bound
reported, not enforced). GATE: if the relations fail on the mult-1
forms under BOTH normalizations, the level-(4) normalization is
wrong → ABORT, banked as a normalization fact; NO Hecke claim runs.

STAGE 1 (only if gate passes): diagonalize T_π inside each certified
mult-2 eigenspace (r = 3.93891686, 5.67072003, 6.63280230,
7.34952664, 7.85778326, 8.30822480, 8.86340536, 9.04778823,
9.64012103, 9.83711622). PRE-REGISTERED FORK: equal Hecke eigenvalues
on both basis vectors ⇒ GEOMETRIC degeneracy (symmetry-forced);
distinct ⇒ ARITHMETIC (Steil-type) doubling. Either outcome banks;
it also decides B791's "generic multiplicity" scoping.

## CELL 3 — SPIN FORK (exact arithmetic; two-outcome by construction)

SETUP: H¹(m004; Z/2) = Z/2 → exactly two spin structures = the two
SL(2,C) lifts of the holonomy: ρ₁ = (A, B) (the banked Riley lift)
and ρ₂ = (−A, −B) (the nontrivial character sends both meridional
generators to −1; the relator w = ab⁻¹a⁻¹b has even signed length so
both are genuine SL(2,C) lifts — verified in-cell).

COMPUTATION (sympy-exact): traces of the lifted PERIPHERAL generators
for both lifts — meridian a and the longitude word bABaaBAb (the
banked parabolic with translation τ = 2√−3). Each trace is exactly
±2; the sign pattern (ε_m, ε_l) per lift determines the induced spin
structure on the cusp torus.

CONVENTION (named, per E23 discipline): for a parabolic peripheral γ,
tr ρ̃(γ) = −2 ⟺ the spin structure is TRIVIAL (periodic) along γ;
the LIE spin structure on T² = trivial along BOTH generators. Bär's
dichotomy: essential spectrum of the Dirac operator = ℝ iff the cusp
spin structure is the Lie one; otherwise the Dirac spectrum is
DISCRETE. Both convention orientations are reported; the FORK is
convention-independent if the two lifts land in different classes.

PRE-REGISTERED FORK: (i) if some extending spin structure induces the
Lie structure on the cusp → the conventional fermionic spectral-action
family CLOSES for that structure (banked negative); (ii) if an
extending structure induces a non-Lie cusp structure → the Dirac
spectrum is discrete for it and the Dirac–Hejhal follow-up is
AUTHORIZED. No third outcome. Cross-check: P52 ("τ fixes both spin
structures") must be consistent with the computed pattern.

## SEAL

Algorithm: SHA-256 of this file's bytes; digest recorded in
docs/SEAL_LEDGER.md (never in this file).
