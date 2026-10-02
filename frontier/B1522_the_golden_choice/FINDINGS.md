# B1522 — THE GOLDEN CHOICE: on the levels M₁…M₁₂ of m004's harmonic family the count-odd mirror breaks, first on M₅, exactly where no golden Galois reflection fixes the twist; no banked chiral configuration lives on a broken vacuum, and M₅'s sit on the two golden sheets, held by the golden rotations

cc (the SM-derivation seat), 2026-10-02. Sealed at `5d4eb5f7` before `census.py` read a flag on any level n ≥ 3
(`PREREGISTRATION.md`, sha-256 `2e3e12ce…`, SEAL_LEDGER). The census took 68 s: two routes that share no code, 167 736
characters on twelve levels. **Verdict: PROVED, outcome B.** All nine predictions came true (P1–P9); the priors expected 7.85 of 9.
Five post-run checks pass (§4). One of them drops the criterion and tests every vacuum of M₁…M₆ directly as a module, against all
16n symmetry words. **Prior work: EXTENDS**: sm:B1512's actions and sm:B1520's level-one test, taken to the levels (Seen
first; §6). **0 of 19 stays 0.**

## 0. What was found

- **Main's L242 (b), answered.** On the levels the count-odd mirror does break, unlike level one (sm:B1520):
  - M₁ to M₄: every vacuum keeps a count-odd symmetry, at every λ.
  - M₅: 20 of 121 twists break it at a λ off the unit circle; none breaks it at |λ| = 1.
  - From M₆ on, twists break it at |λ| = 1 too.
  - The share that breaks it off the circle rises with the level: 0.17, 0.30, 0.53, 0.61, 0.77, 0.80, 0.89 and 0.91 on M₅ to
    M₁₂.
- **Where it breaks is golden** (Lemmas C and G, both routes; X2 without the criterion).
  - Off the unit circle, a vacuum breaks the count-odd mirror exactly when no **golden Galois reflection** fixes its twist. These
    reflections are ±M^{2k}S: the maps that exchange the eigenlines of φ and φ̄ = −1/φ on the torsion.
  - At a split prime, a twist with a component on one golden eigenline (one "sheet") always breaks it (P5, checked directly by X1).
  - On M₅, T₅ = 𝔽₁₁², the breaking twists are exactly the single-sheet ones, 10 on each sheet.
- **The gloss "a broken vacuum chooses a sheet" is exact only on M₅.**
  - On M₇, M₉, M₁₀ and M₁₁, mixed twists break as well, those whose sheet ratio lies outside the reflections' orbit (Lemma F):
    392, 3 888, 9 600 and 34 848 of them.
  - On M₆, M₈ and M₁₂ no prime is split, so there is no sheet over 𝔽_p, and 96, 1 344 and 93 936 twists break all the same.
- **No banked chiral configuration lives on a broken vacuum** (P8).
  - All 196 firing members of levels 1–6 are fixed at their own λ, on both routes and directly (X3). The chiral record through
    level 6 is complete (sm:B1512, sm:B1514).
  - So the mirror breaks only where nothing chiral has been found. This is outcome B.
- **After the run, not sealed** (§6): M₅'s chiral configurations are B1511/B1512's eigenline characters.
  - At each λ ∈ μ₄ they are exactly the 20 vacua of M₅ that no reflection fixes, ten on each golden sheet.
  - At their unitary λ, only the **golden rotations** ±M^{2k+1} hold their count-odd mirror. The rotations keep each sheet.
  - Every other level's members are held by a reflection.
- **For the goal.** No vacuum selects a chirality on the levels either.
  - Where the mirror breaks, no chiral configuration has been found.
  - Where chiral configurations live, the mirror holds.
  - Over every firing vacuum both orders live with opposite counts (sm:B1511, sm:B1512; main's L241 and B1438).
  - On M₅ the golden sheet is where chirality lives, not what picks its sign.

## Seen first (the repo sweep and the literature)

**The repo sweep**, before the seal (PREREGISTRATION §0, the PRIOR ART section). Refreshed at banking with `git fetch --all`: main
`8d1c1329`, the audit lane `7b088f50` and the seat lanes `7cda35aa`, `0043be2b`, `5d58b935` and `13d2c5b6` are unchanged since
the seal, and none of them was merged. The heads are in `arc_verdict.json`.
- Main's `topic_sweep.py` on "eigenline | eigencharacter | golden eigen | Psi-eigen | count-odd | stabiliser of a vacuum | L242 |
  unfixed | Galois sheet | 1/q | φ⁴ | w = 7 | strong inversion on a level | deck swap/invert": *12 of 1327 arcs on main match
  (NEGATIVE 1, OPEN 1, PROVED 10)*. None decides a vacuum's count-odd stabiliser on a level.
- The tower's golden record on this branch, read where it bears:
  - **sm:B1279**: the inversions swap Y₉'s golden eigenlines; the glide involutions keep them.
  - **sm:B1303**: H₁(Y_n) = ℤ[φ]/(L_n) or ℤ[φ]/(√5 F_n), and the eigencharacter law.
  - **B1297** (main): P = −1 on the torsion.
  - **sm:B1512**: Lemmas I, E, A and D, the actions on characters and on the family.
  - **sm:B1520** and main's **B1455**: level one.
  - **sm:B1511, B1512, B1514**: the firing members on levels 1–6, and the eigenline orbits of M₅ (§6).
  - **sm:B1521**: P is the swap, and the inversion dualises the family.

**Refreshed at banking** with `scripts/checks/prior_work.py` on "count-odd | L242 | golden eigenline | eigenline | Galois
reflection | golden rotation | stabiliser of a vacuum | unfixed vacua | golden sheet | golden choice". The hits off this branch were
read where they bear.
- **Main's "golden rotation" is a different object**: the order-10 elliptic modular lift of A₁ on the flavor side (B672, B674,
  B584; TERMINOLOGY.md). *Terminology:* in this arc "the golden rotations" are the count-odd elements ±M^{2k+1} on the torsion's
  characters, as named at the seal (Lemma G). They are not main's.
- **Main's outside-bench memo 101** (`outside_bench/memos/GAMMA5_REVERSER.md`, 2026-08-28) is adjacent. At the trivial
  representation, the reverser acts on the golden eigenframe as the ℚ(√5) Galois conjugation, exchanging the unstable and stable
  lines up to the units φ^∓6. The sign on the golden eigenline (its "branch bit") is reached by no banked symmetry.
  - That is the orbit-level face of the exchange this arc's reflections make on the torsion characters.
  - Its object differs: the eigenframe of the monodromy's derivative, not the characters of T_n.
  - On characters, the sign v ↦ −v on one eigenline is reached, by ι (count-even). Nothing here decides memo 101's bit.
- "Galois reflection", "golden sheet" and "golden choice" occur on no head, by `git grep` on all nine, except in this arc's seal
  and its seal surfaces.

**What this arc must not present as new.**
- The golden structure of the torsion, and the inversions' swap of the eigenlines (B1279, B1303).
- The actions on characters and on the family (B1512).
- That M₅'s chiral members are the eigenline characters (B1511 Theorem F; B1512 §1).
- The order over a firing vacuum (B1511, B1512; L241, B1438).

New here:
- the criterion on a level (Lemma C);
- the census of the count-odd stabiliser on M₁…M₁₂;
- Lemma F's closed counts and Lemma SP;
- the firing members' status;
- the reading in §6 that M₅'s members are exactly the twists no reflection fixes, held by the rotations.

**The literature.**
- S. A. Ballas, *Finite volume properly convex deformations of the figure-eight knot*, arXiv:1403.3314v3, p. 17: the family and its
  presentation. The ρ_q are holonomies of properly convex structures and so faithful; C1 uses that in checking α.
- SnapPy (run 2026-10-02, and again at banking): the covers M_n, their homology, and |Isom(M_n)| = 8n for n ≤ 8, every M_n
  amphicheiral.
- The splitting of primes in ℚ(√5), checked by own code for every p < 2000 (C11), not cited.
- Reidemeister–Schreier rewriting is a standard method, implemented by own code in route R and in X2. It is checked against
  SnapPy's homology (C3) and against route F character by character (C8), not cited.

## 1. The question (PREREGISTRATION §1–§2)

Main's L242 (b), registered with B1455: *"The same test on the levels M₃ to M₆ of the harmonic family, where the seats count on
covers and the symmetry group is larger."* Taken to M₁₂.

- **A vacuum** on M_n is V = ν ⊗ ρ_q restricted to π_n = F ⋊ ⟨z = mⁿ⟩.
  - Here q > 0 and q ≠ 1.
  - ν = (ν_F, λ) is a character of H₁(M_n) = ℤz ⊕ T_n, with ν_F a character of T_n = coker(Φⁿ − 1) and λ = ν(z).
- **A count-odd map** is V ↦ (V∘β)* with β dualising (d = 1). It may be followed by conjugation of the twist, which keeps the
  count, since ρ_q is real.
- **The question:** for which (n, ν) is V fixed by a count-odd map?
- **The owner's "choice might be golden"** was sealed in its first exact form: the vacua that break the count-odd mirror are
  those whose twist no golden Galois reflection fixes, those that choose between φ and φ̄. P2–P5 test its consequences.

## 2. The run (`census.py` with `route_fibre.py` and `route_rs.py`)

Route F is the fibre model, B1511's basis, with the actions closed under composition. Route R is Reidemeister–Schreier on π_n,
with its own Smith form and no fibre model. They are compared character by character through C8's bijection, and they agree on
all 167 736 characters (P9).

| n | \|T_n\| | invariant factors | primes (in ℚ(√5)) | group on characters | unfixed, λ off the circle | unfixed, \|λ\| = 1 |
|---|---|---|---|---|---|---|
| 1 | 1 | — | — | 4 | 0 | 0 |
| 2 | 5 | 5 | 5 ramified | 8 | 0 | 0 |
| 3 | 16 | 4, 4 | 2 inert | 24 | 0 | 0 |
| 4 | 45 | 3, 15 | 3 inert, 5 ramified | 32 | 0 | 0 |
| 5 | 121 | 11, 11 | 11 split | 40 | 20 | 0 |
| 6 | 320 | 8, 40 | 2 inert, 5 ramified | 48 | 96 | 96 |
| 7 | 841 | 29, 29 | 29 split | 56 | 448 | 392 |
| 8 | 2 205 | 21, 105 | 3, 7 inert, 5 ramified | 64 | 1 344 | 1 344 |
| 9 | 5 776 | 76, 76 | 2 inert, 19 split | 72 | 4 464 | 4 320 |
| 10 | 15 125 | 55, 275 | 5 ramified, 11 split | 80 | 12 100 | 12 080 |
| 11 | 39 601 | 199, 199 | 199 split | 88 | 35 244 | 34 848 |
| 12 | 103 680 | 144, 720 | 2, 3 inert, 5 ramified | 96 | 93 936 | 93 936 |

The orders of the unfixed characters:
- M₅: 11.
- M₆: 40.
- M₇: 29.
- M₈: 21 and 105.
- M₉: 19, 38 and 76 off the circle; only 38 and 76 on it.
- M₁₀: 11, 55 and 275 off the circle; only 55 and 275 on it.
- M₁₂: fifteen orders from 18 to 720.

The read-out is in `census.json` and `census_run.txt`.

## 3. The predictions (`read_out.py` → `read_out.json`)

| | prediction | read | prior | held |
|---|---|---|---|---|
| P1 | levels 1, 2: no unfixed vacuum at any λ | 0, 0 | 99% | yes |
| P2 | n = 5: 20 and 0 (Lemma F) | 20, 0 | 95% | yes |
| P3 | n = 7: 448 and 392 | 448, 392 | 95% | yes |
| P4 | n = 11: 35 244 and 34 848 | 35 244, 34 848 | 95% | yes |
| P5 | a single-eigenline component at a split prime is never fixed off the circle; n = 9 ≥ 576, n = 10 ≥ 2 500 | X1 holds on every level; 4 464, 12 100 | 97% | yes |
| P6 | some level with no split prime has unfixed vacua | M₆ 96, M₈ 1 344, M₁₂ 93 936 | 70% | yes |
| P7 | on M₁₂ more than half unfixed off the circle | 93 936 of 103 680 | 70% | yes |
| P8 | every one of the 196 firing members is fixed at its λ | 196 of 196, and directly (X3) | 65% | yes |
| P9 | the two routes agree on every character | all 167 736 | 99% | yes |

Nine of nine held; 7.85 were expected. Outcome A was impossible by Lemma SP, and it was not read. **Outcome B:** unfixed vacua
exist, and every firing member is fixed.

## 4. Post-run checks (`post_run_check.py` → `post_run_check.json`; written and run after the census, disclosed as such)

Both routes implement Lemma C's criterion, so a flaw in the criterion would pass them both. These checks drop it.

- **X1 (P5 directly).** On every level n ≤ 12, no character that a reflection fixes has a nonzero component on a single golden
  eigenline at a split prime. **Passes.**
- **X2 (the criterion bypassed).** For every character of M₁…M₆:
  - V = ν ⊗ ρ_q is built on π_n's Reidemeister–Schreier generators over 𝔽_p, with p = 13, 41, 13, 61, 89 and 241 on levels 1 to 6,
    and q = 2.
  - Every relator, and the rewriting of every image word, are checked.
  - For each of the 16n words ι^a ε^b α^c τ^k (a, b ∈ {0, 1}, c < 4, k < n), which cover the 8n isometries, it tests directly
    whether (V∘β)* is isomorphic to a target module. The test computes the whole space of intertwiners, with a trace filter only
    to skip a solve.
  - λ is a primitive root of 𝔽_p whose square is not an N-th root of unity, the stand-in for a λ that is no root of unity.
  - Three readings:
    - generic: the target is V;
    - real: the targets are V and (−v, λ);
    - unitary: the targets are V and (−v, λ⁻¹).
  - No dualising flag, σ, Lemma C or Lemma Z is used.
  - **Passes:**
    - the fixed counts are 1, 5, 16, 45, 101 and 224 off the circle (the generic and real readings) and 1, 5, 16, 45, 121 and 224
      on it, character by character equal to the census;
    - every fixing word is dualising;
    - every intertwiner space has dimension at most one, so no self-twist of ρ_q mod p intervened.
- **X3 (the firing members directly).** The same module test on all 196 members at their own λ (1, −1, i, −i), with both targets.
  **All 196 are fixed, and only by dualising words.**
- **X4 (a live control: the test can say more).** The same instrument at the hyperbolic point q = 1 on M₅ and M₆, where ρ₁ is
  self-dual and every isometry keeps it. **Passes:**
  - at |λ| = 1 every character is fixed: 121 and 320, against 121 and 224 at q = 2 (Lemma U, now checked directly);
  - off the circle the fixed sets are those of all σ = −1 elements of either d, 101 and 224;
  - non-dualising words now fix, 20 to 816 times per reading.
  - So X2's zero count of non-dualising fixers is a property of q ≠ 1, not of the code.
  - It also shows that off the circle the golden breaking is already present at the hyperbolic point. What the deformation adds
    is the breaking at |λ| = 1, from M₆ on.

- **X5 (Lemma F beyond the sealed range;** `lemma_f_beyond.py` **→** `lemma_f_beyond.json`**).** M₁₃, with L₁₃ = 521, checked by
  code that shares nothing with either route.
  - Φ¹³ = I mod 521, so T₁₃ = 𝔽₅₂₁².
  - The group ±M^j S^e is built mod 521, checked closed under the four lifts and of order 104.
  - All 271 441 characters are counted.
  - **257 920 are unfixed off the circle and 256 880 on it, exactly (p − 1)(p + 1 − 2n) and (p − 1)(p − 1 − 2n).**
  - Every odd-n Lucas number is ±1 mod 5 (n < 200), so Lemma F's hypothesis "L_n a split prime" is just "L_n prime".

**Disclosed design slips, all caught before any outcome was read.**
- Route R first read its Smith form in the column convention while multiplying on the right. Its assertion "z must
  generate the free part" failed; it now uses y = x·V, with the basis the rows of V⁻¹. An E1 instance, logged.
- C5's expectation said 8n at n = 2. T₂ = ℤ/5 has only 8 distinct actions, so the expectation was restated as 4, 8, then 8n, before
  the seal.
- The first draft of X2 used p = 41 on M₆, where every element of 𝔽₄₁* is a 40th root of unity, and λ = i, itself a root of unity,
  so neither stood in for a λ that is no root of unity. Read before it ran. It now uses p = 241 with an asserted g² ∉ μ_N, and the
  unitary reading uses the conjugate target. An E31 instance, logged.
- A dead primitive-root line in that draft would have stopped it at once. Removed before it ran.

## 5. The golden reading, tested

**In its sealed form it holds.** Off the circle a vacuum breaks the count-odd mirror exactly when no golden Galois reflection
±M^{2k}S fixes its twist. This is Lemma C with Lemma G, confirmed on both routes for n ≤ 12 and without the criterion by X2 for
n ≤ 6. The reflections are the maps that exchange φ and φ̄, and a single-sheet twist is never fixed (P5, X1).

**As a description of the breaking vacua, the gloss "they choose a sheet" is exact on M₅ and only there.** The counts are from
`read_out.json`:

| level | unfixed off the circle | with a single-sheet component | mixed only | no split prime |
|---|---|---|---|---|
| M₅ | 20 | 20 (10 + 10) | 0 | |
| M₆ | 96 | | | yes |
| M₇ | 448 | 56 | 392 | |
| M₈ | 1 344 | | | yes |
| M₉ | 4 464 | 576 | 3 888 | |
| M₁₀ | 12 100 | 2 500 | 9 600 | |
| M₁₁ | 35 244 | 396 | 34 848 | |
| M₁₂ | 93 936 | | | yes |

- A mixed twist a·u + b·uS breaks it when a/b lies outside the reflections' orbit H = ±⟨φ̄²⟩ (Lemma F).
- At |λ| = 1 the golden rotations, which keep each sheet, also act:
  - on M₅, M₇ and M₁₁, where T_n = 𝔽_p², every single-sheet twist is then held, and the breaking twists are exactly the mixed ones
    with a/b ∉ H (0, 392 and 34 848; Lemma F);
  - on M₉ and M₁₀, where T_n has a second primary part, 432 and 2 480 single-sheet twists still break (216 + 216 and 1 240 + 1 240).
- On levels with no split prime, twists break with no sheet to choose over 𝔽_p.
- So the golden reflections are the right symmetry to state the breaking. The sheet choice is a sufficient condition at split
  primes, not the mechanism.

## 6. After the run (not sealed): where M₅'s chiral configurations sit

Seen in `census.json` after the run. These facts decide nothing; `read_out.json` holds them under "after the run (not sealed)".
- **M₅'s case-(b) members are B1511/B1512's eigenline characters** (B1511 Theorem F; B1512 §1 and §5 (d)). That part is theirs.
- **New here:**
  - At each λ ∈ μ₄ (1, −1, i, −i) the 20 members are exactly the 20 vacua of M₅ that no golden Galois reflection fixes, ten on
    each golden sheet (`eigen_type` at p = 11).
  - None of the 80 is fixed by a reflection (E). All 80 are fixed by a golden rotation (A), and they are held only because their λ
    is unitary.
  - Off the circle these same twists would break the count-odd mirror.
- **Every other level's members are held by a reflection:** M₄'s 8 order-3 members, M₆'s 96 order-8 members, the triplets and the
  pullbacks.
- **The reading.**
  - On M₅ each chiral background chooses a golden sheet, and the population holds both sheets equally.
  - The symmetry that keeps the count balanced is a rotation, which keeps the sheet.
  - Both orders live over each of these vacua with opposite counts (B1512 §5 (c): M₅'s double point counts +1 for W₁ and −1 for
    W₂).
  - So the golden sheet is where M₅'s chirality lives, not what selects its sign.
- **A sealed question registered** (OPEN_LEADS sL-10 item 7):
  - On the levels with split primes (M₇: 29, M₉: 19, M₁₀: 11, M₁₁: 199), do case-(b) members exist?
  - Are they single-sheet, and held only by the rotations?
  - Their unitary λ would then be the only thing holding their mirror. To be sealed before computing.

## 7. Scope, and what it does not do

- **Object:** m004's Ballas family on the cyclic covers M₁…M₁₂ (reach: class), with the lemmas proved on every level, and Lemma F
  on every odd n with L_n a split prime.
- **Hypotheses:**
  - H-vac, the bridge's vacua (R44, R54, R76; not re-derived);
  - the uniqueness of the harmonic metric (R47 F13), so a vacuum is fixed exactly when its flat bundle is;
  - main's class index with L1, L2 (B1297, B1512);
  - "all isometries are lifts", from SnapPy for n ≤ 8 and the group closure for n ≤ 12 (C5).
- **Other states.** Lemma U says that at the hyperbolic point every unitary vacuum of every word state is fixed; X4 checks it
  directly on M₅ and M₆. Off the hyperbolic point a family must first exist. The next arc is registered as sL-10 item 6: which word
  states are projectively flexible. It is to be sealed first.
- **Not decided here:**
  - what picks the order (L241's owed question; GENESIS GAP2);
  - the componentwise B130 question (sL-10 item 5).
- **The experiential question.** GENESIS FK12 registers it under Gate 5-Q, and nothing here bears on it. The seal quotes the
  owner's message verbatim as its source. This text, like GENESIS, keeps to "the experiential question" (Q5).
- **No Standard-Model number is touched:** 0 of 19; I-26 stays UNEARNED.
- **creates_law: true** under B1214's rule. Lemma C (the criterion on every level) and Lemma F (the closed counts on every odd level
  with L_n split) are new general propositions proved here. They are rowed as T-GOLDEN-CHOICE in `docs/THEOREM_REGISTRY.md`.

## 8. Reproduce

```
cd frontier/B1522_the_golden_choice
sha256sum -c ARTIFACT_HASHES.txt                         # the sealed files
python3 verification/controls.py                         # C1–C11 (SnapPy for C1, C3, C5)
python3 verification/census.py                           # 68 s; census.json
python3 verification/read_out.py                         # read_out.json
python3 verification/post_run_check.py                   # 64 s; post_run_check.json
python3 verification/lemma_f_beyond.py                   # 4 s; lemma_f_beyond.json (M13)
pytest tests/test_b1522_the_golden_choice.py              # the lock (from the repo root)
```
