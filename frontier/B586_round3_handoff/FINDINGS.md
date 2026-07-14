# B586 — the Round-3 handoff processed: E₆ hears everything too, and the golden voice stays home

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM quantities
(the B580 binding rule); firewall intact. Preregistered (PREREGISTRATION.md) with
the frame corrections registered BEFORE computing. Locks:
`tests/test_b586_round3_handoff.py`.**
Run: `python3 r3a_e6_pairs.py` (pyenv, ~2 min; reuses the banked C3 machinery,
all C3 gates reproduced).

## Verify-don't-trust verdicts on the three proposed cells

### R3-A — computed (after a frame correction). Two blind results.

**The frame correction (registered pre-computation):** the handoff's "decompose
through the six Sym-blocks" mixes two decompositions. The exponents {1,4,5,7,8,11}
grade the ADJOINT via the principal sl₂ (B575/B581, classical side); the E₆₂
STAGE's θ-odd space is graded by the three conjugate primary pairs (27/27̄,
351′/351̄′, 351/351̄) — dimension 3, not 6, and no canonical bijection exists.
Through the principal-sl₂ shadow every rep is self-dual (C = 1), so the antiphase
vanishes identically in that dictionary: **the proposed sign-law/torsion
comparison is not a defined computation.** (The honest unifier remains the L82
mechanism.) Chat-1's per-block sign expectation is additionally unanswerable as
posed because the actual per-pair amplitudes are COMPLEX, not signed reals.

**Blind result 1 — E₆₂ also hears everything:**
> `Z = +1`, `Z_C = −1`, **tr_even = 0 exactly, tr_odd = +1** — the entire E₆₂
> amplitude is θ-odd, exactly as on the golden stage (B584). Two stages, two
> different total values (−1/φ and +1), one pattern: **the figure-eight's whole
> stage amplitude IS its chiral amplitude; the even channel is exactly silent.**
> (Not universal — the SU(3)_k table (B585) has tr_even ≠ 0 at many κ — but it
> holds at both banked "special" stages.)

**Blind result 2 — the golden voice does NOT travel:** the −1/φ check found
NOTHING on E₆₂ — not among the per-pair amplitudes, not among their ratios.
Chat-1's key test is answered: −1/φ is **stage arithmetic** (B585's 5|κ tone on
the SU(3) tower), not an object-universal constant. The object's universal part
is the *pattern* (all-θ-odd), not the *number*.

**The new numbers (the three per-pair chirality amplitudes, blind):**
> ⟨u|ρ(A₁)|u⟩[27-pair] = +0.13151189 + 0.57619122i
> ⟨u|ρ(A₁)|u⟩[351′-pair] = +0.20449548 − 0.25642922i
> ⟨u|ρ(A₁)|u⟩[351-pair] = +0.66399264 − 0.31976200i
> (sum = 1 = C3's banked trace; block order 4 reproduced.)
Convention note recorded: E₆₂ has S² = +C (S₀₀ > 0), vs S² = −C in B238's
SU(3)₂ normalization — the lift identity holds on both with the matching sign.

### R3-B — superseded by B585's naming theorem (chat-1 hadn't seen it); the geometric questions are ill-posed as asked.

The C-twisted mapping torus (the frame in which the antiphase was computed) IS
the (−A₁)-bundle: monodromy trace −3, |tr| > 2 ⇒ **Sol geometry** (Thurston's
torus-bundle trichotomy, cited). Not hyperbolic ⇒ no hyperbolic census name, no
hyperbolic volume, no trace field, no hyperbolic CS. ℚ(√−15) does not arise
here. The handoff's alternative construction (the complement doubled along the
cusp torus) contains an essential torus ⇒ a graph manifold with two hyperbolic
JSJ pieces (cited standard) — also not hyperbolic; its Gromov-norm volume is
additive (2 × 2.029883…) but "its trace field" is not a defined single field.
**The "CS = cosmological constant of the chord" hook dies at the geometry
level.** What stands instead (B585, locked): the chord's carrier in the bundle
frame is the OTHER Sol world −A₁, and chirality is what the two Sol worlds
agree on.

### R3-C — answered structurally; the solo antiphase is zero.

4₁ is invertible (its full symmetry group D4 was computed in-sandbox and banked
in B279) and dual color = knot-orientation reversal (Reshetikhin–Turaev
functoriality, cited-standard) ⇒ **J₂₇(4₁) = J₂₇̄(4₁) identically** — for every
color of every stage, not just level 2. The solo antiphase invariant is zero;
chat-1's cautious branch is confirmed: **chirality lives in the chord (the
coupled construction), never in the solo colored invariant.** The full
U_q(e₆) 6j computation is therefore unnecessary for this question (and remains
out of round-scope for any other; residual registered in L83).

## Reading (firewalled)

Round 3 closes coherently: three deafnesses (vacuum, filling, bare state — now
proven at every color by invertibility), one listener (the antiphase mirror
channel), and on both banked stages that listener hears the WHOLE invariant.
The stage decides the number (−1/φ golden, +1 at E₆₂, the two-tone law across
the SU(3) tower); the object supplies the invariant pattern — total silence of
the symmetric channel. The chord's geometric carrier is not a hyperbolic
manifold hiding new constants; it is the object's own other lift.

## Gates and discipline

All C3 gates reproduced before any new number (|W| = 51840, S unitary/symmetric,
S² = +C, (ST)³ = S², two-word ρ(A₁) agreement, odd-trace 1, order 4). The
identity tr_odd = ½(Z − Z_C) and the lift identity verified on-stage. Blind
protocol followed; the −1/φ absence and the undefined-comparison verdicts are
computed/argued in-sandbox or cited precisely. MB13 sweep in the prereg.

## Anchors

B584/B585 (mechanism + naming + LAW-O), C3/B570 (stage machinery + banked odd
block), B581 (torsions — NOT unified here; see L82), B279 (D4 in-sandbox),
B238 (convention contrast), L82 (mechanism), L83 (new residual).
