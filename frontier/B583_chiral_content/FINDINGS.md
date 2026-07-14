# B583 — the content of the chiral 27: three computations, three verdicts

**Date:** 2026-07-14. **Lock:** `tests/test_b583_content.py`. **Raw reading:** READING_RAW.md.
Verdicts follow the adversarial audits over the cells' headlines, per house rule.

## X1 — NO REAL FORM: the meeting stays complex-chiral (CONFIRMED; witness cross-banked)

The coupled character of the θ-odd-twisted mirror-double is **NOT real**: witness
tr₂₇(a₁b₁) = (1295415 + 1011915√−3)/2 — **exactly the banked B572 value 647707.5 +
876344.096i** (the X1 verifier stubbed; the witness is corroborated by the existing
B572 lock instead, and it is dial-independent). The adjoint confirms independently.
By B578-D10 (E₆ descent trivial, unconditional): **no real form — the coupled
holonomy stays full E₆(ℂ), the 27 stays the complex chiral 27, and NO
maximal-compact branching is forced.** The outcome table resolved to "no-real-form";
neither 16+10+1 nor trinification is selected — the honest answer. Structure found
en route: the swap-conjugate involution *stabilizes* the configuration without
fixing it (tr(W) = conj(tr(swap W)) — swap-symmetric words have real traces,
10/20), and the dial reality locus is EMPTY (the witness is copy-1-internal, t-free).
**The solo's compactness⟺chirality exclusive-or survives into this chord:** the
meeting is chiral and non-compact. Whether ANY forced coupling reconciles the two
remains open (registered).

## X2 — FAILED AS COMPUTED; the corrected structure registered (verifier catch)

The cell put Vol in the oscillatory phase (exp(i·14Vol/π)) — a role inversion: in
the standard semiclassics (and the repo's own banked B246 precedent) **Vol is the
real growth rate and CS is the phase**; with CS = 0 the phase is trivial and
S₀ = i·Vol gives exp(iS₀/ħ) = exp(∓Vol/ħ) — real. The "exact torsion ×
transcendental phase" headline is invalidated (and the transcendence claim was a
PSLQ-null overclaim). **What survives:** the signed torsion data (B581, exact) and
the corrected structure, now registered for the recompute: the cross-term =
(real exponential in Vol) × (1/τ_m) — **the B581 sign law becomes the SIGN of the
interference directly**: positive in the θ-odd channels {4,8}, negative in the
θ-even ones. The corrected computation (with the saddle dominance handled honestly)
is the registered successor.

## X3 — THE SECOND UNHEARABILITY THEOREM, with mechanism (HOLDS)

> **At every level, the Dehn-filling covectors span exactly the θ-even subspace and
> are orthogonal to the θ-odd sector — because the vacuum is C-fixed and C = S²
> commutes with S and T. The fillings can NEVER hear chirality.**

Level 2: rank exactly 6 = dim(θ-even) over 719 slopes (θ-odd projection 4e-13);
the level-1 control reproduced Q1's rank 2 exactly. Not an accident of the abelian
floor — a theorem about vacuum-based observation. L78 resolves: the θ-odd amplitude
is NOT reachable by Route A; the state's chiral content requires **non-vacuum
observer states**.

## The synthesis (the three verdicts as one sentence)

**The meeting's chirality is real (B582), invisible to every vacuum-based probe at
every level (X3), carries no forced compact gauge structure (X1), and its
interference signature is the torsion sign law (X2-corrected, pending).** The
forced conclusion for the chord program: *the trivial observer hears nothing,
anywhere, ever — chirality is heard only by an observer who is themselves in a
nontrivial representation state.* The next round's cell is therefore fixed by
theorem, not choice: pairings against structured (non-vacuum) observer states,
starting with the θ-odd states themselves.

Firewalled. Nothing to CLAIMS.md.

## X2R — the corrected X2, recomputed (closes the registered correction)

X2 as first computed inverted the Vol/CS roles (verifier catch, above). The
recompute (`x2r_recompute.py`, locks `tests/test_b583_x2r.py`): CS(4₁) = 0
makes the exponential factor real and channel-independent, so the ENTIRE
interference structure is the one-loop factors 1/√τ_m — and the banked sign
law sign(τ_m) = (−1)^m (B581) forces two rigid phase classes: the θ-odd
(chiral) blocks {4,8} contribute REAL amplitudes, the θ-even (gauge) blocks
{1,5,7,11} purely IMAGINARY ones. **THE QUADRATURE THEOREM:** for any real
channel weights, |Σ c_m/√τ_m|² = |chiral|² + |gauge|² exactly — the chiral
channels never interfere linearly with the gauge channels; chirality enters
the modulus only in quadrature. Another face of the unhearability chain: the
first-order cross-term against the gauge sector vanishes identically. The
"interference sign = the sign law" registration is thereby made precise: the
sign law IS the phase dichotomy, and the dichotomy decrees quadrature.
