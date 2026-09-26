# B1378 — THE M6 DECK TRIPLET: a native order-3 deck orbit on Y₆ gives an exact three-generation-shaped index in all six Standard-Model sectors at once

> **Scope and notation correction (2026-09-26, B1379; E72).** "Y₆" below is the **cusped** 6-fold cyclic cover of m004 — the source's own name, **M₆**, is the right one; B1301's Yₙ are the closed branched covers, and B1278's "six-fold closing" is that closed Y₆, a different manifold. **The triplet does not descend to it**: on the filled meridian z the three members' characters are trivial but ρ(z) = [[1, c], [0, 1]] with c ≠ 0 — the nonsplit class that carries the whole index is exactly what obstructs descent (consistent with B1351: a closed manifold's index vanishes). The (−3)⁶ is a statement about M₆ only. Verified in `frontier/B1379_the_genesis_and_m004_links/verification/descent_check.py`.

**Date:** 2026-09-26 · **Seat:** cc (the SM-derivation branch) · **Occasion:** an uploaded seat-checkpoint archive's audit
package, verified with this branch's own code · **Status:** PROVED (the index computation, two independent methods, three
primes and exact) · CONFIRMED (the semisimplification control) · CORRECTION FOUND in the source's own automorphism check
(does not touch the index) · **Fence:** as B1374/B1375/B1377 — main's index on a non-semisimple background, no physics
reading, index ≠ physical generation count · **Price: unchanged, 0 of 19** · **Numbering:** B1378.

## 0. Seen from above — provenance

The owner uploaded two "seat checkpoint" archives from external ChatGPT web seats (the owner's description; corrected 2026-09-26, B1379 — an earlier draft misnamed their origin) working the wider Origin Axiom project
(`Origin_Axiom_Seat_Full_Checkpoint_2026-09-25.zip`, `Origin_Axiom_Seat_Checkpoint_2026-09-26_FULL_HANDOFF.zip`) and asked
this seat to check whether their work "helps the project." Both are handoff bundles (chronology, claim ledgers,
corrections, recovered artifacts), not git branches; nothing in them is banked by that act alone. One item stood out:
seat "0925"'s `05_SEPTEMBER_COMPUTATIONS/m6_deck_chiral_triplet/` — a self-contained audit (`REPORT.md`,
`verify_m6_triplet.py`, `exact_qz8.py`, `scan_family_tensor.py`, and their JSON outputs) claiming a native order-3 deck
orbit on M6 (their name for the degree-6 cyclic cover of m004) gives three B1374/B1375-shaped backgrounds whose rank-6
direct sum has index (−3)^6 across all six Standard-Model sectors, exactly.

This arc **independently reproduces the claim's numerical core with this branch's own code** (not by running their
script): a Reidemeister-Schreier presentation of π₁(Y₆) built from scratch here (`rs_presentation.py`, following B1368's
⟨a,b|R⟩ conventions for m004 rather than their script's), fed into this branch's own `index_lib.py`/`exact_lib.py`
(B1374). Y₆ is identified with M6 by matching invariants: H₁ = ℤ/8 ⊕ ℤ/40 ⊕ ℤ both ways (confirmed here against
SnapPy's own `covers(6,'cyclic')`, which B1375 already uses), and the same seed data and six-sector, three-member, exact
index pattern reported in `REPORT.md`. **One genuine error was found in the source's own account** (Sec. 3) — disclosed
and corrected, and shown not to affect the index claim, which never depended on it.

## 1. Computed

`verification/rs_presentation.py` (the presentation, two structural cross-checks, run log `rs_presentation_run.txt`);
`verification/deck_triplet.py` (the index computation and the genuineness argument, run log `deck_triplet_run.txt`).

| item | result |
|---|---|
| H₁(Y₆) via Reidemeister-Schreier (own rewriting code, from m004's ⟨a,b\|awb⁻¹w⁻¹⟩) | ℤ/8 ⊕ ℤ/40 ⊕ ℤ, matching SnapPy's `covers(6,'cyclic')` (B1375) exactly |
| classical cross-check (no presentation): m004 fibers over S¹, monodromy M = RL = [[2,1],[1,1]]; H₁(Yₙ) = coker(Mⁿ−I) ⊕ ℤ | coker(M⁶−I) invariant factors [8, 40]; order of M on it is exactly 6 |
| the deck square's order on H₁(Y₆) (own Reidemeister-Schreier word map, exact lattice-membership test) | exactly 3, matching M² |
| six-sector index of each of the 3 deck-orbit members, seed χ = (0,0,15,45,0,75,105) mod 120, three primes (601, 1201, 1321) | (−1,−1,−1,−1,−1,−1) on every member, every prime |
| six-sector index of the rank-6 block-diagonal orbit sum, three primes | (−3,−3,−3,−3,−3,−3) |
| the same, exactly over ℚ(ζ₈) (the seed data are all multiples of 15 mod 120 = 8th roots of unity) | (−3)^6 exactly; cohomology dims (a₀,a₁,t₀,r₁) = (0,6,3,6) for V, (0,3,3,0) for V\* — matching `REPORT.md` exactly |
| semisimplification control (own re-check): the cocycle set to 0 at the seed member | index 0 on all six sectors (the non-split extension class carries the entire index) |
| the genuineness argument's inputs: h¹(π; χ²) = 1 at all three members; `deck()`'s character rotation equals the direct word-pullback by the order-6 deck generator TAU on every character used here | both confirmed |

## 2. The construction

Y₆'s Reidemeister-Schreier presentation (own code, `rewrite()`, standard coset rewriting for the index-6 subgroup
⟨aᵏba⁻ᵏ⟩ᵏ, a⁶⟩ of π₁(m004) = ⟨a,b | R⟩): seven generators z(=a⁶), x₀,…,x₅, six relators (one per coset), meridian
μ = z, longitude λ = the rewritten w·w\* at coset 0. The order-6 deck generator TAU (conjugation by a) acts z → z,
x_k → x_{k+1} (k<5), x₅ → z x₀ z⁻¹; `deck()`, the source's character-rotation map (own-verified: it is the exact
pullback χ → χ∘TAU on every character used here, all of which vanish on z — see the caveat in §4), generates a 3-orbit
from the seed (χ, ψ_Y, ψ_γ) = ((0,0,15,45,0,75,105), (0,…,0), (0,30,15,15,30,75,75)) mod 120 by two steps of TAU at a
time (i.e. by TAU², the order-3 square). Each orbit member gives a rank-2 non-split extension V = ρ_χ ⊗ ψ (ψ built from
ψ_Y, ψ_γ by the same six linear combinations as every SM-sector background in B1374/B1375: (Q,u^c,e^c,d^c,L,ν^c) with
(s_Y,s_γ) = (1,3),(−4,3),(6,3),(2,1),(−3,1),(0,−5)). Cohomology of a direct sum is the direct sum of cohomologies, so
the rank-6 sum of the three members' index is trivially the sum of their individual indices — three separate (−1)⁶
backgrounds combine to an exact (−3)⁶, with no tension against B1377's |I| ≤ 2 bound (which applies to a single
non-split extension of two rank-one pieces, not to a direct sum of three independent such extensions).

## 3. A correction found in the source (does not touch the index)

`REPORT.md` reports the order-3 deck square as a word map (its `TAU2`), used only for an "intertwiner" check that the
three members are literally one automorphism orbit (not merely three characters with matching index). Hand-rederiving
this word map independently here (twice, by two different routes — see `rs_presentation.py`'s `TAU2` comment for both)
found the source's specific formula wrong on two wraparound terms; a corrected formula gives the right order (exactly
3) **on H₁(Y₆)**, cross-validated against the classical, presentation-free monodromy computation (M has order 6, so
M² has order 3) — but neither the source's formula nor either of this seat's own corrected attempts was confirmed at
the full, non-abelian representation level (substituting the word into each of the six relators and evaluating in a
genuine rank-2 representation of π₁(Y₆) does not give the identity on every relator for any of the three candidates
tried). **This is disclosed as an instrument limit, not resolved by further guessing.** It does not affect the index
computation, which never uses this word map — only the separate, simpler, independently-confirmed `deck()` character
rotation. In its place, §3 of `deck_triplet.py` gives a clean, word-map-free argument for genuineness: TAU² is a deck
transformation of an honest covering space, hence a topological automorphism of π₁(Y₆); `deck()` is confirmed to be its
exact action on the characters used; squaring commutes trivially with pullback; and since H¹(π;χ²) is 1-dimensional at
every member (verified), the pulled-back cocycle is forced to be a scalar multiple of the next member's own — an
isomorphism of representations. The three members are a genuine TAU-orbit by this argument, without trusting any
word-level formula for TAU or TAU².

## 4. What it means

1. **The first exact three-generation-shaped index from an internally generated three-cycle**, rather than from
   inserting three arbitrary copies by hand: on Y₆, a single seed background's own order-3 deck symmetry supplies
   the multiplicity, and the result is exact — (−3)^6, not merely "three backgrounds that happen to be chosen."
2. **No tension with B1377.** B1377's bound (|I| ≤ 2 on a single doublet sector with rank-one h¹ ≤ 1) is about ONE
   non-split extension; this arc's (−3) is a DIRECT SUM of three such extensions, where cohomology is additive by
   the most elementary property of direct sums. Three (−1)'s sum to −3 with no bound violated anywhere.
3. **The mechanism is identified and is not physical yet.** The entire index lives in the non-split extension class
   (§1's semisimplification control: turn it off, the index is 0 on all six sectors). B1374/B1375's fence stands
   unchanged: this is main's B1297 class index on a **non-semisimple** (non-reductive) background; by Corlette–Donaldson
   a flat bundle admits a harmonic metric only if its monodromy is reductive, so this extension cannot simply be
   inserted into the standard harmonic-flat physical dictionary without further work (a T-brane/source/nonabelian-Higgs
   completion, per the source's own physics-gate list, itself not attempted here). **Index ≠ physical generation
   count** — this is the sharpest instance of that fence this branch has produced, precisely because the algebra is
   for once exactly three-shaped, which makes the fence matter more, not less.
4. **A negative reported by the source, not independently re-run here.** Its `scan_family_tensor.py` reports an
   exhaustive scan of all 67 200 of B1375's generation-shaped Y₆ backgrounds (115 deck-orbit representatives, weighted
   back by orbit size) under the existing, already-banked "E₆ × SU(3)_family" tensor mechanism, finding **zero**
   complete three-generation triplets that way (42 partial patterns, none complete) — i.e., this deck-orbit mechanism
   is a genuinely different route to a three-shaped count than the repo's own existing factorized construction. This
   specific negative is **taken on the source's own report**, not re-run in full here (115 representatives × six
   sectors is substantial compute); what was independently spot-checked is the much smaller, structurally central
   claim of §1 (the seed member and its orbit sum), which is the arc's load-bearing content.
5. **The error class.** Finding and disclosing an error in an external source's own derivation, at the point where
   independent re-derivation was attempted, is exactly the discipline this branch's "also check other seats' work"
   standing instruction calls for — verify, don't trust, and say so when a check fails rather than silently adopting
   or silently dropping the claim.

## 5. Caveats

1. The index computation (§1's main content) is independently confirmed two ways (three prime fields; exactly over
   ℚ(ζ₈)) and is not in question.
2. The "genuine orbit" claim rests on the word-map-free cohomological argument of §3, not on an explicit intertwiner;
   this is a complete argument (not a gap) but a reader wanting the intertwiner matrices themselves will not find them
   here — the word-level formula needed to compute them was not successfully pinned down.
3. §4 item 4 (the factorization-mechanism negative) is cited, not re-derived; it is the one substantive claim in the
   source's report taken without independent re-computation, and is flagged as such rather than silently absorbed.
4. As always: this is main's B1297 index on a reducible non-split module of a one-cusped cover of m004, in the
   Standard-Model frame set up by B1364/B1368/B1374; no physical admissibility is claimed or implied.

## Verification

`verification/rs_presentation.py` (structural: H₁, the classical cross-check, TAU²'s order); `verification/deck_triplet.py`
(the index, three primes and exact; the genuineness argument's inputs; the semisimplification control). Lock:
`tests/test_b1378_the_m6_deck_triplet.py`.

**Sources.** An uploaded seat-checkpoint archive, `Origin_Axiom_Seat_Full_Checkpoint_2026-09-25` (seat "0925"),
`05_SEPTEMBER_COMPUTATIONS/m6_deck_chiral_triplet/REPORT.md` and its scripts (the construction, the seed data, the
family-tensor negative) — read and cited, not merged; this record's B1374 (`index_lib.py`, `exact_lib.py`, the SM-sector
conventions), B1375 (the tower, T5, the presentation-independence discipline, `covers(6,'cyclic')`'s H₁), B1377 (the
rank-one bound and its scope), B1368 (the ⟨a,b|R⟩ presentation and its meridian/longitude words).
