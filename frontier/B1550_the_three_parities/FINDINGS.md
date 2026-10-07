# B1550 — THE THREE PARITIES: NEGATIVE as sealed — the root's generation sector is not only its 24 sign members: 24 order-4 members read one generation too; and every one of the 48 carries one of the three non-zero parities, 16 to each, cycled by the golden map

cc (the SM-derivation seat), 2026-10-07. **Verdict: NEGATIVE, by the seal's §9** (P8 fails). Sealed at `db9d9902`.
- **The identity.** It held at 11:34:47–11:36:50Z (`verification/identity.json`).
- **The run.** 11:36:50Z to 12:26:53Z, rc 0, one start and no stop.
- **The record.** It was committed unread at `19cd2833`.
- **The read-out.** `read_out.py` ran once, at 12:27:25Z (`35199ffd`).
- **The price is unchanged:** 0 of 19.

## Seen first

- **The repo sweep at the seal** (the seal's §0): eight terms over every head, fetched 2026-10-07 at 11:20Z, and a search
  on main for Φ₃ mod 2.
  - "three parities", "A4 cover" and "non-zero parit" are absent.
  - Main's B326 has the Φ₃ action of m004's 3-fold cover on its torsion, and B1067's hook has Δ ≡ Φ₃ (mod 2). The parity
    lemma's arithmetic for the root is on the record.
  - B298 bounds Galois multiplicities over ℚ. B1255 has the criterion for a genuine three. Main's B1496 grades three as
    obtained by selection everywhere.
- **The repo sweep after the run.** `git fetch --all` (2026-10-07, 12:28Z; main at `d5b6ca8e`, which seals B1498 on
  o10_150691), then `scripts/checks/prior_work.py` over every head with five terms: "golden triplet", "binary
  tetrahedral", "spin cover", "congruence cover", "generation-shaped".
  - **"spin cover" bears through main's B206** (2026-06-25): the golden monodromy mod 5 is SL(2, F₅) = 2I, the "spin
    shadow" of A₅ = PSL(2, F₅). That is an arithmetic shadow of the act on another prime.
    - Here the act mod 2 gives A₄ through F₂² ⋊ ℤ/3.
    - The holonomy mod √−3 gives PSL(2, F₃) ≅ A₄, and its spin lift SL(2, F₃) is the binary tetrahedral group.
  - **"binary tetrahedral"** leads to this seat's B1356 (A₄ = 2T/±1 on Y₃) and to other objects.
  - **"golden triplet"** leads only to this seat's relay of 2026-10-07 and to unrelated arcs.
  - **"generation-shaped"** leads to this seat's arcs, B1549 among them, and to main's readings of them.
  - No head reads the members of a tetrahedral cover.
- **The literature** (the seal's §0):
  - Altarelli, Feruglio and Lin get A₄ on the four fixed points of T²/ℤ₂, the four 2-torsion points (hep-ph/0610165).
  - Kobayashi, Nilles, Plöger, Raby and Ratz get families as multiplicities of equivalent fixed points (hep-ph/0611020).
  - Hattori, Matsunaga, Matsuoka and Nakanishi take generations at an elliptic curve's torsion points (arXiv:0903.2718).
  - Standing: **EXTENDS** B326, B1067 and AFL. **NEW-AS-SWEPT** for the tetrahedral covers' members, their parity labels
    and counts.

## 1. The question and the design (the seal's §1–§5)

- **The parity lemma (proved at design time).** tr φ is odd exactly when φ permutes the three non-zero parities of the
  two records as a 3-cycle, exactly when Δ ≡ Φ₃ (mod 2). GENESIS's SE1 gives the root an odd trace.
- **The tetrahedral cover N.** The kernel of π₁M → A₄ = F₂² ⋊ ℤ/3, with four ends at the fibre's 2-torsion points.
- **The selection.** The four odd-trace states of word length at most 4: +LR (m004, the root), −LR (m003), +LLLR (m023)
  and −LLLR.
- **The population.** Every member at characters of order dividing 4: 60 members in 9 A₄ orbits, none golden-fixed.
  - 54 are on the root:
    - two free sign orbits of edge characters;
    - four order-4 orbits of size 6, with m_A = 2 and n = 1;
    - two order-4 orbits of size 3, with n = 4.
  - 6 are on −LR, and none on ±LLLR.
- **What is proved at design time.**
  - n(1) = 0 on each cover, so a member carries at most one generation, and generation-shaped means (−1, −1).
  - The orbit law.
  - The golden-triplet law: a member orbit of size 12, 6 or 3 gives three local systems on the third level, carried into
    one another by the golden map.
- **The claim tested (P8, THE THREE).** The root's generation-shaped members are exactly its 24 sign members, eight per
  non-zero parity, and the golden map is a 3-cycle on the labels.

## 2. The read-out (`verification/read_out.json`, `read_out_log.txt`)

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the banked identity: K2–K5 reproduce, every sealed file hashes as sealed | 97% | **holds** |
| P2 | the routes agree at every member: (h¹, r¹, n), the interior dimension, the generic count | 90% | **holds**: 60 of 60 |
| P3 | the orbit law: every member of an A₄ orbit reads alike, in each route | 93% | **holds**: 9 orbits |
| P4 | the theorems at every reading, the structure as the census, every gap clean | 95% | **holds** |
| P5 | the three draws read alike at every task | 92% | **holds** |
| P6 | every sign member of the root reads (−1, −1) | 95% | **holds**: 24 of 24 |
| P7 | no order-4 member of the root is generation-shaped | 70% | **fails**: 24 read (−1, −1) |
| P8 | THE THREE: the root's generation-shaped members exactly its 24 sign members | 65% | **fails** (as P7) |
| P9 | −LR's six sign members are not generation-shaped | 70% | **holds**: they read (0, −3) |

7 of 9 hold, against 7.67 expected. **Verdict: NEGATIVE.** P1–P5 hold on complete records (120 of 120 tasks, three draws
each), and P8 fails.

## 3. The counts

Every member's generic count, alike in route P and route S, and alike across each orbit:

| state | members | (h¹, r¹, n), m_A | count |
|---|---|---|---|
| +LR | 24 sign members, two free orbits (each member an edge) | (1, 0, 1), 0 | **(−1, −1)** |
| +LR | 24 order-4 members, four orbits of size 6 (no puncture value) | (3, 2, 1), 2 | **(−1, −1)** |
| +LR | 6 order-4 members, two orbits of size 3 (−1 on all four puncture loops) | (4, 0, 4), 0 | (1, 0) |
| −LR | 6 sign members, one orbit of size 6 (−1 on all four puncture loops) | (4, 0, 4), 0 | (0, −3) |

- **The root carries 48 generation-shaped members, and no other state of the four carries any.**
- **The generation shape is not confined to sign characters here.**
  - On sm:B1549's three-ended covers no order-4 member was generation-shaped.
  - On the root's tetrahedral cover the 24 order-4 members trivial on two ends (m_A = 2) read one generation each.
  - So "the shape follows the square" (sm:B1549 §4) is a law of the three-ended covers, not of the family's covers.
- **−LR's members read (0, −3):** three on the Λ² side and none on W₁. Their interior has dimension 4.
- **The root's members with n = 4 read (1, 0).**

## 4. After the read-out: every generation is parity-labelled (`verification/post_run_tables.py`)

This table was written after the read-out and is named as such. It seals and predicts nothing.

| generation-shaped members of the root's cover | per label (1, 0) ∣ (0, 1) ∣ (1, 1) | the golden map on the labels |
|---|---|---|
| 24 sign members, labelled by their edge | 8 ∣ 8 ∣ 8 | (1, 0) → (0, 1) → (1, 1) → (1, 0) |
| 24 order-4 members, labelled by the translation that fixes them | 8 ∣ 8 ∣ 8 | the same 3-cycle |
| all 48 | **16 ∣ 16 ∣ 16** | |

- **What it says.**
  - Every generation on the root's tetrahedral cover carries exactly one non-zero parity of the two records, 16 to each.
  - The golden map permutes the three as GENESIS's SE1 forces (the parity lemma).
  - The sealed claim was too narrow. The parity structure it was built on holds for the whole generation sector.
- **Where the order-4 ones live.** Each is fixed by the translation t_p for its label p, so it descends to the double
  cover N/⟨t_p⟩ of the third level, one of the three fibre-direction double covers (the controls' K6 counts eight members
  with n = 1 at order 4 on each). The three double covers are cycled by the golden map.
- **On the third level** (the golden-triplet law) the 48 give 18 local systems, each carrying one generation: six types
  (the two sign orbits and the four order-4 orbits).
  - Each type appears exactly three times, once per non-zero parity.
  - The three copies are carried into one another by the golden map.

## 5. What it means

- **For the owner's goal ("derive three generations from oa principle").** The three is derived: GENESIS's SE1 makes the
  root's act a 3-cycle on the three non-zero parities of its two records (∣F₄^×∣ = 3, π(2) = 3).
  - On the root's own congruence cover of level √−3, the tetrahedral cover, every member that carries a generation
    carries one parity.
  - The golden map moves each to the next.
  - So the generations come in threes, by the principle's arithmetic, and not by a choice of quotient.
  - Whether these threes are the physical three generations is a reading (GENESIS FK14).
- **What it is not.**
  - It is not one module of index three, which main's B1496 asks for. Each member carries one generation, as Theorem C
    allows with n(1) = 0 here.
  - Three in one module needs room. The spin cover (the dossier, and the next arc) has room four.
- **The family.**
  - Members on the tetrahedral cover appear only on the golden pair ±LR, the two arithmetic states of the selection.
  - Generations appear only on the root.
  - +LLLR (m023) and −LLLR have the same 3-cycle and no members at all at these orders.

## 6. What this arc does not decide

- **Characters of other orders** (3, 8, 12, …) and non-interior classes.
- **States beyond word length 4,** and states of even trace.
- **One module of index three.** The spin cover's glued module is the next arc.
- **What the two kinds and the two sign types are** physically.
- **Masses and mixings** (B1391's Schur limit), and **which object and state** the genesis takes (GENESIS FK14, FK9).

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/`:
  - the sealed code: `tetra_lib.py`, `census.py`, `run.py`, `read_out.py`, `controls.py`, `identity.py`;
  - `population.json`, with `census_0.jsonl.gz`, `census_1.jsonl.gz`, `census_2.jsonl.gz` and `census_sha256.txt`;
  - `controls.json`, `identity.json`;
  - `run_notes.md`;
  - the record: `run.jsonl.gz` with `run_sha256.txt`;
  - the read-out: `read_out.json`, `read_out_log.txt`;
  - after the read-out: `post_run_tables.py` → `post_run_tables.json`.
- The derivation note: `docs/dossiers/the_three_parities_2026-10-07/NOTE.md`.
- Lock: `tests/test_b1550_the_three_parities.py`.
