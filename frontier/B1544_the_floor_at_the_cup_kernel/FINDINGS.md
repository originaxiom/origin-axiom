# B1544 — THE FLOOR AT THE CUP KERNEL: SEALED; NO COUNT AT A NON-INTERIOR CLASS OF K0 READ. Where can three live in sm:B1515's frame at the trivial character, and what do the cup map's kernel's strata read on N₄₅ and the four degree-60 covers?

cc (the SM-derivation seat), 2026-10-06. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome of the run.** It states what is proved at design time, what is sealed, what was checked before the run, and how the
run will be read. The verdict, the read-out and the surfaces come at the bank. **Price:** unchanged, 0 of 19.

## 1. What is proved at design time (the seal's §3)

- **Lemma F.** At the trivial character on a finite cover with m cusps, every class c of H¹(N; ρ) has I(W) ≥ k − m − 1, k the
  number of cusps where c is non-zero.
  - So sm:B1543's floor I(W) ≥ −1 holds wherever c is non-zero on every cusp.
  - I(W) = −g needs c to vanish on g − 1 cusps.
  - The proof uses the identity route R checks at every reading, and the four's cohomology on a cusp torus. The torus facts
    are h⁰(T; W*) = 2 for every c, and h¹(T; ρ) = 2.
- **Corollary F′.** With Theorem C (ii), three needs a + rk δ¹_W ≤ n(1) − 2 and k ≤ m − 2.
- **Lemma G″.** The generic classes of the strata K0(S), over the closed supports S, give the least I(W) on all of the cup
  map's kernel K0.
- **Proposition D.** This uses the structure and sm:B1542's banked counts.
  - On d10.13's and d10.36's covers, three can only be at the classes of K0(S) for three supports of four cusps each.
  - On d10.16's and d10.40's covers no class reads I(W) = −3.

## 2. What is sealed

- `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before `run.py` read any
  count at a non-interior class of K0. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The population** (§5 of the seal): every closed support S of K0 on N₄₅ (sixteen) and on the four degree-60 covers (five,
  two, five, two), three generic classes of K0(S) per route, in route F and route R. In all, 30 subspaces, 90 tasks and
  180 readings.
- **Predictions** P1–P6 with priors. P4, the floor on K0, has prior 70%. P6, (−3, −3) at a stratum in both routes, has
  prior 4%.
- **Reading rules.**
  - PROVED if a stratum reads I(W) < −1 in two routes.
  - NEGATIVE if the floor holds on all of K0. With Proposition D, the four degree-60 covers then carry no three at the trivial
    character.

## 3. Checked before the run

Controls K1–K6 hold (`verification/controls.json`):
- structure in two routes, including the closed supports and the deck group's action on the cusps;
- the cochain formula against the long exact sequence;
- the banked interior counts;
- the read-out on synthetic rows;
- the cusps' identity across routes;
- Lemma F's ingredients at a generic and an interior class, with the banked counts.

Disclosed in the seal's §6:
- the first design (generic classes of K0 and its eigen-parts), replaced before any reading when Lemma F showed it could not
  break the floor;
- a module-shadowing slip caught by its first control trial (E12);
- the classes whose banked counts were re-read.

## Seen first

- **The repo sweep** (the seal's §0): twelve terms on every head. The hits that bear are this seat's own: sm:B1543's
  observation of the floor, sm:B1542's and sm:B1541's banked counts, sm:B1535's Theorem C, and sm:B1542's kill entry. The
  other hits are other objects: Massey products as deformation obstructions, triple products as couplings.
- **The literature:**
  - Putman's note on half lives;
  - Menal-Ferrer and Porti on twisted cohomology, whose cusp computations cover the holomorphic Vₙ and not this frame's
    four V₂ ⊗ V̄₂;
  - Garoufalidis and Levine on Massey products in 3-manifolds.
  None states Lemma F or a count of this frame.
