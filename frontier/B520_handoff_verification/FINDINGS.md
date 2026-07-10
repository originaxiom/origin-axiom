# B520 — verification of the β-function/bootstrap-ceiling/BTZ handoff: two REJECTED, one corrected, one banked
**Verify-don't-trust on the exploration-seat handoff (2026-07-12). Two headline claims do NOT reproduce
(including a wrong correction to CC's own B506/B507); one is overclaimed vs B516; one formula is correct.
Lock `tests/test_b520.py`.**

## §1/§2 — the β-function "correction" (g(0)≈−0.31, zero at transcendental κ*≈0.764): REJECTED
The handoff claimed the β-function zero is at κ*≈0.764 (a transcendental "Feigenbaum analog / first
emergent value"), correcting B506/B507's zero-at-the-pointer-κ=0. **It does not reproduce.** Computed by
TWO independent correct methods:
- **Goldman-ergodic** (iterating the golden trace map T_F on each κ-leaf — the true F-invariant measure);
- **Haar-conditional-on-κ** (8M samples, narrow bin).

Both AGREE to 3 digits: **g(0) = +0.001 (se 0.0002), g(0.764) = +0.266** — the zero is at κ≈0 (the
pointer leaf), NOT at 0.764 (where g is solidly positive). **B507 REPRODUCES; the handoff's g(0)≈−0.31
is a biased-MC artifact.** No correction to B506/B507. There is no transcendental κ*; the "first emergent
value" claim collapses with the error it rests on.

## §3 — the bootstrap "ceiling" (dim 3 is the maximum): OVERCLAIMED; corrected
Verified kernel: the SELF-DOUBLE ladder terminates at Level 1 — the 8×8 self-double [[M∗,C],[D,M∗]] has
**0 canonical Pisot couplings** (confirms the handoff's search; M∗'s complex eigenvalue pair breaks
Pisot under self-coupling). BUT "**dim 3 is the max / self-reference produces exactly 3" is FALSE**: B516
already found golden-field Pisot at **dim 5** (degree-6, three Fibonacci copies — a different coupling,
not the self-double). Honest statement: **the self-double recursion terminates at Level 1; other
couplings reach dim 5.** Three is the minimal-new golden dimension (B517), not the unique one (B516).

## §4 — BTZ entropy S = arccosh(x/2): formula CORRECT, banked; the 3·7 hook firewalled
Standard 3d gravity (BTZ = AdS₃/loxodromic). At the golden loxodromic x=5 (the 40a1 2-torsion point):
**S = arccosh(5/2) = log((5+√21)/2) ≈ 1.5668** (verified). √21 = √(3·7). The 3·7 reading (Eisenstein
prime × Niven-excluded prime) is a HOOK → speculations/, firewalled; no 4d/Hawking/information claim.

## Verdict + meta-lesson
Two REJECTED (the β-function correction + the transcendental κ*), one corrected (the ceiling), one banked
(the BTZ formula). The handoff's headline — "the β-function's zero is a transcendental first emergent
value, and 3 is the only dimension" — is WRONG on both counts. Verify-don't-trust caught a wrong
correction to CC's own banked work (the right response to "your result is wrong" is to recompute, not to
concede). Cross-seat handoffs are not uniformly reliable: chat3's Stein form (B517 refinement) was solid
and verified; this one was not. Firewalled; nothing to CLAIMS.md.
