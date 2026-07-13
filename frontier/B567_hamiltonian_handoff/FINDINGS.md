# B567 — the Hamiltonian handoff (seat-1): core spectrum REFUTED; the honest salvage

Seat-1 proposed reading the object as a QFT via H = −i·log ρ(A₁) on ℂ¹⁵, reporting six
π/3-spaced energy levels with degeneracies (3,2,2,3,3,2), an exact zero mode in H₃, an
87.7% interaction fraction, coupling ratio 0.553, and 28/27 multiplicities at level 165.
Processed verify-don't-trust (`tests/test_b567_hamiltonian.py`).

## The refutation (construction-independent at its core)

**An order argument, before any computation:** six eigenvalues equally spaced by π/3
force ρ(A₁)⁶ ∝ I — projective order dividing 6. But A₁ = [[2,1],[1,1]] has order 20 in
SL(2,ℤ/15) (A₁² = −I mod 3; A₁⁵ = −I mod 5), so in ANY projective representation of
SL(2,ℤ/15) — or of its metaplectic double cover (order ≤ 40) — ρ(A₁)'s projective order
divides 40 and is forced to 20 for a faithful rep. **6 divides neither.** The claimed
spectrum is impossible for anything that deserves the name "the monodromy at level 15."

**The computation (standard Weil rep, T→chirp, S→DFT, A₁ = T·(S T⁻¹ S⁻¹)):**
- Level 15: **11 distinct eigenvalues**, degeneracies {1,2}, angles on the 2π/20 lattice,
  **projective order = 20** exactly. Not 6, not (3,2,2,3,3,2), not π/3-spaced.
- Level 165: **21 distinct eigenvalues**, multiplicities 12,12,12,12,11,11,10,… ,
  **projective order = 20** (= lcm(4,10,5)). Not 6, not 28/27 — the "28 = dim SO(8),
  27 = dim h₃(𝕆)" reading dissolves with the spectrum (the Markoff-lesson species).

All downstream claims (the massless H₃ mode, the 87.7% interaction fraction, the 0.553
coupling ratio, "low-energy color singlets") inherit the broken spectrum; the seat's own
caveats (branch dependence, basis dependence of the free/interaction split, no null model)
already flagged the framework's softness.

## The honest salvage (two real kernels)

1. **The "2 vs 3 primes" transition is confounded with the prime 2.** Level 30 = 2·3·5
   contains p = 2 — the genuinely special metaplectic case — while at odd composite levels
   the Weil rep factors by CRT (with quadratic-multiplier twists; a naive un-twisted tensor
   comparison shows spurious "non-factorization"). The correct question is not "how many
   primes" but "does the level contain 2, and are the CRT twists carried correctly."
2. **The framing "ask the object's quantum dynamics, not its numbers" is legitimate** —
   but its invariant content at level N is exactly the eigenvalue distribution of the Weil
   monodromy: Gauss-sum data on the order-20 lattice. That object is real, canonical, and
   connects to the banked measurement-face structure (B534/B566-S1); it does not contain
   an SM-like level structure at N = 15 or 165.

## Verdict

**REFUTED (core), with salvage.** The fifteenth SM-comparison campaign ends like the
fourteen before it — but faster, by an order argument. Consistent with the program's
standing results: the object's dynamics is its own (order-20 monodromy spectrum, the
recursive dark law, the KMS clock), not the Standard Model's.
