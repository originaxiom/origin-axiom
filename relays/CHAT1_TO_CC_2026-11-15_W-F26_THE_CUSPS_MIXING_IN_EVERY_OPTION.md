# W-F26: high in the cusp, frame C's mixing tends to a permutation in all eight options (at the twin it is still settling at height 8). It is the identity exactly when the up and down sectors take the same reading, and a cyclic permutation when they take different ones, as both of the record's Higgs worlds do. So M33's structural failure holds in both declared worlds; the same-reading options give mixing near the identity with exponents of their own

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It answers M33's structural point and
closes card W-F26 (`relays/cards/CHAT1_W-F26_the_cusps_mixing_in_every_option.md`, 90cd9b1c1).

**Under the author's ruling of 2026-11-15** (outputs printed; no data, no comparison). **Not blind:** main's finding
(M33; B1945 § 3b) was known.

**How it was checked.** Computed once; expectations committed first. The script `wf26_run.py` was sealed at 90cd9b1c1 and
run once. Its output was committed (a8a44d3e5) before it was read.
- **The frame:** W-F24's, this seat's transcription.
- **The mixing:** the full 3 × 3 matrix |V| = |U_u† U_d|, with each left-singular basis ordered as B1724's frame orders
  it.
- **Where:** at heights 3, 4, 6 and 8, at Re τ = 0 and 1/4, with the canonical end.
- **The options:** the point (the mark or the twin) × the up sector's reading (S or S̃) × the down sector's reading.

## 1. Results

| point | up, down readings | permutation at heights 6 and 8 | largest deviation from it at height 8 |
|---|---|---|---|
| mark | S, S | **identity** | 2.2e-4 |
| mark | S̃, S̃ | **identity** | 1.1e-4 |
| mark | S, S̃ | cyclic (2 0 1) | 8.7e-4 |
| mark | S̃, S | cyclic (1 2 0) | 6.4e-4 |
| twin | S, S | identity | 6.3e-2 (still settling) |
| twin | S̃, S̃ | identity | 1.2e-1 (still settling) |
| twin | S, S̃ | cyclic (1 2 0) | 1.9e-1 (still settling) |
| twin | S̃, S | cyclic (2 0 1) | 9.6e-2 (still settling) |

- The permutation is the same at Re τ = 0 and 1/4, and at heights 6 and 8, in every option.
- **Z1** (within 0.05 of a permutation in every option, at heights 6 and 8) is not met as written. The twin's four options
  are still settling at height 8 (6e-2 to 1.9e-1). The mark's four are within 1e-3.
- **Z2** (at least one non-identity permutation) holds: 4 of 8.
- **Where |V| is the identity** (the mark, S and S), its off-diagonal moduli fall as ε^F, F = −(1/π) d log|V| / d Im τ,
  between heights 6 and 8. The 1-2 and 2-1 entries give 0.600; 2-3 gives 0.301 (0.302 at Re τ = 1/4); 1-3 gives 1.10; 3-1
  gives 0.900.
- **The same at the mark, S̃ and S̃:** 0.70 (0.69 at Re τ = 1/4), 0.30 and 1.00 for 1-2, 2-3 and 1-3, between heights 6
  and 8 (the 3-1 entry falls below the script's 1e-12 floor at height 8).
- **The twin's same-reading options** (still settling): in S and S, 0.90, 0.10 and 1.00 for 1-2, 2-3 and 1-3; in S̃ and S̃,
  0.61, 0.09 and 1.10, between heights 6 and 8.
- **From the referee's read.**
  - The referee ran main's extended-precision frame code (B1940's `frame_mp`, its per-line step, with the record's end) at
    the mark and the twin, at heights 6, 8 and 12 and Re τ = 0 and 1/4.
  - It gives the same permutation in all eight options. At height 8 its |V| equals the script's to the printed digits.
  - At height 12 the deviations are 5e-6 to 2e-5 at the mark and 1.8e-2 to 5.5e-2 at the twin.
  - Between heights 8 and 12 the mark's exponents are 0.600, 0.300 and 1.100 (3-1: 0.900) in S and S, and 0.70, 0.30 and
    1.00 in S̃ and S̃.

## 2. What it means

- **M33's structural failure holds for the record's Higgs worlds.**
  - Both declared worlds read the up and down sectors differently (B1932's four declared options are the world W− (up in S̃, down in S) and its mirror W+ (up in S, down in
    S̃), each under two measures).
  - In both, at the mark and the twin, the cusp's mixing is a cyclic permutation: the heaviest up state aligns with a
    lighter down state (the lightest or the middle one, depending on the world and the point). The other 22 lines of
    order 5 are not run here.
  - So in those worlds the exponent read-out fails on structure, before anything is compared, as M33 says.
- **It is not a property of the cusp as such.**
  - When both quark sectors take the same reading, the cusp's mixing is near the identity.
  - Its off-diagonal moduli then fall with their own exponents. At the mark in S these are 3/5 for 1-2, about 3/10 for
    2-3, and about 11/10 for 1-3. They are not compared with anything measured.
  - So the frame at its cusp does carry a hierarchical mixing pattern, but only in an option the record does not declare.
- **Why the readings disagree (the pattern checked in the referee's read; the cause a hypothesis).**
  - With this frame's units, S̃ = ε conj(S) εᵀ = conj(c₁) Q_I + conj(c₂) Q_J + conj(c₃) Q_K. Each component stays on its
    own unit, and only its phase changes.
  - At the cusp two of the triplet's components have equal modulus, and the third is far smaller.
  - At the mark (heights 8 and 12), both sectors in both readings have the same three singular directions: the second
    block alone, and the two equal-weight combinations of the first and third blocks, with relative phase ±i.
  - S̃ lists them in an order cyclically shifted from S's. So the mixed worlds misalign the generations at the cusp by
    construction.
  - A hypothesis: the shift comes from the conjugation reversing the relative phase of the two equal components. Whether
    it is the frame's S₃ (B1935) acting on the generation index is not checked.
- **The fork this leaves for main.**
  - Either the H and H̃ assignment (different readings for up and down) stays, and frame C's cusp read-out fails in
    structure.
  - Or the frame's conjugate reading is not the H̃ of the Standard Model's up coupling. Then a same-reading world would
    need a reason of its own: the parity argument of B1936 gives W− (up in S̃, down in S), a mixed world.
  - Neither branch is decided here. This note is a counterexample to "the cusp's mixing is a permutation at every point"
    taken as a failure in every option. It is not a fix.

## 3. Typed

| statement | how checked |
|---|---|
| the cusp's mixing is a permutation in every option; identity exactly for same readings, cyclic for mixed (at the mark) | computed once; expectations committed first (Z1 not met at the twin, still settling; the identity-versus-cyclic pattern itself was not among them); recomputed independently by the referee with main's extended-precision frame code at heights 6, 8 and 12 |
| the same at the twin | computed once; not settled at height 8 |
| the off-diagonal exponents in the mark's S and S option | computed once (one step, heights 6 to 8); recomputed independently by the referee in extended precision (heights 8 to 12, the same to three digits) |
| the off-diagonal exponents in the mark's S̃ and S̃ option, and the twin's | computed once (heights 6 to 8); the mark's recomputed independently by the referee (heights 8 to 12); the twin's not settled |
| M33's failure holds in both declared worlds | a reading of § 1 |
| at the mark, S̃ orders the same three cusp directions cyclically shifted from S | computed once, in the referee's read (no expectations committed) |
| its cause (the conjugation reverses the relative phase of two equal components); the link to B1935's S₃ | a hypothesis |

## 4. Files

`relays/chat1_2026-11-15_wf26/`: `wf26_run.py` (sealed), `SCRIPT_SHA256.txt`, `wf26_run_out.txt`, `wf26_run_err.txt`
(empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
