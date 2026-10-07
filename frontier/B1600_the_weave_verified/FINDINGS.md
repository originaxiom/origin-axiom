# B1600 — THE WEAVE VERIFIED: the SM seat's W1–W4 read by main's own code — the moves on the three parities of the two records, the parity lemma on 988 signed words, the quaternion point as the one common fixed point, 2T on every odd-trace word to length six, the A₄ triplet by representation theory — and the weave adopted on main

**Verdict: PROVED** (a harvest-verification of the SM seat's stated claims; a WEAVE result). cc (main), 2026-10-07, at the
owner's word: "we should focus on the weave program relayed by SM, comprehend it first." Not sealed: the claims verified
are the seat's, stated before main's code ran; main's instrument (`verification/weave_verify.py`) was written and run
the same night, its outcomes fixed in advance by the seat's W1–W4. No physical quantity. **0 of 19.**

**Credit.** The SM seat for the name, the test and W1–W4 (its `docs/THE_WEAVE.md` and `docs/dossiers/the_weave_2026-10-07/`);
the owner for the rule, stated daily for a year and named this day; B141/B148 for the quaternion point on main.

## 0. Seen first, and literature

`VERDICT topic-sweep /weave|thread result|parity|quaternion point|binary tetrahedral|2T|A4 triplet/` — read at the level of
the record: B141 (the metallic map's unique irreducible fixed point), B148 (on the Markov surface), B1275 (E₈'s family
triplet), B1291, B1491–B1499 (thread results, labelled so today). **Literature:** the Fricke trace maps; the McKay
correspondence 2T ↔ Ê₆; the A₄ flavour triplet (Ma–Rajasekaran 2001; Altarelli–Feruglio 2005) as the seat cites — cited,
not built on.

## 1. The words (adopted on main: `docs/THE_WEAVE.md`, `WORKING_RULES.md`, `TERMINOLOGY.md`, GENESIS v1.24)

A **thread** is one object the principle allows — one closed path of the moves through the shared fibre, the two
records. **The weave** is the joint action of every allowed move on the records and everything it forces. **The test
before any arc: weave or thread?** — all threads under a stated rule, none hand-picked; defined by the joint action;
claimed about all threads at once. A thread result is labelled so and never presented as the answer to a weave
question. Every arc from B1491 on carries the field `weave_or_thread` in its verdict file.

## 2. W1–W4 on main (`verification/weave_verify.json`)

| | the seat's claim | main's verification |
|---|---|---|
| **W1** | each move fixes a different non-zero parity; any two cycle all three | L fixes (1, 0), R fixes (0, 1), the swap fixes (1, 1), the sign fixes all three; (L, R), (L, P), (R, P) each generate S₃ on the three — **HOLDS** |
| parity lemma | tr φ odd ⟺ φ is a 3-cycle on the parities | all 988 signed words to length eight (448 odd) — **HOLDS** |
| **W2** | the quaternion point is the one point every move fixes (puncture parabolic) | on x² + y² + z² − xyz − 2 = −2 the only common fixed point of the Fricke maps of L and R is (0, 0, 0); on all levels, (0, 0, 0) and (2, 2, 2) (the trivial representation) — **HOLDS** |
| **W3** | every odd-trace thread receives 2T with A₄ below | for all 54 odd-trace words to length six a τ ∈ 2T (two signs) conjugates (i, j) to the act's images and ⟨i, j, τ⟩ has order 24; for the 60 even-trace words, 24 have τ ∈ Q₈ (image 8) and 36 have no τ in 2T — **HOLDS** |
| **W4** | the three parity lines form one irreducible A₄ triplet on odd-trace threads, split on even | h¹(F; χ_ε) = 1 for each non-zero parity (the punctured torus's twisted cohomology, as in B1494's theorem); A₄ = (ℤ/2)² ⋊ ℤ/3 acts by the three non-trivial characters permuted by the 3-cycle: the standard three-dimensional irreducible representation (character (3, −1, 0, 0), norm one); for an involution it splits — **HOLDS by representation theory** |

## 3. What it says

The weave's three is the three non-zero parities of two records — a number forced by the records themselves
(2² − 1) and cycled by every odd-trace thread, m004, m003 and +LLLR among them, with no thread chosen: it meets the
owner's rule exactly, and it is the orbifold standard of the physics (three sectors under an order-3 action) realised
on the shared fibre rather than on any one thread. Everything main landed today on L8a15, o10_150691 and N₄₅ is thread
work and is now labelled so; its theorems (T-COMPANION-NO-ROOM, T-ROOM-NEEDS-GENUS) are about every thread's covers.
What decides whether the triplet is three generations is W6 — what each parity line carries — and that needs a weave
instrument, defined by the joint action and read on all threads at once; every frame on record is a thread
instrument built on one thread's holonomy.

**Main's ruling on the seat's asks (relayed):** the name and the test adopted; the moves L and R in, the sign and the
swap OPEN (GM5b/c, FK4) — W1–W4 hold either way and the weave's group on the triplet is read in both forms, 24 and 48;
W1–W4 verified here; **main opens the weave program, W6 first**, the seat's draft instrument reviewed before any seal.

## 4. Disclosed

Run before any seal (a verification of stated claims). The moves are taken as the free-group automorphisms
L: b ↦ ab, R: a ↦ ab (a right action on words); the seat's conventions may differ by inverses, which does not change
W1–W4. The 2T image is computed with exact rational quaternion matrices after a first attempt with √2 entries failed
the equality test (the error was the instrument's, caught by an impossible group order and corrected before anything
was read off). W4 is argued, not computed.

## 5. Files

`verification/weave_verify.py` → `weave_verify.json`; `docs/THE_WEAVE.md`; the visual page for the owner (The Weave,
Drawn). Test: `tests/test_b1600_the_weave_verified.py`.
