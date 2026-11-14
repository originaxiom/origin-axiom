# W-F7: of the four faces of three distinctions, only all half-turns admits a hyperbolic history step: every face with a mirror has a corner of non-zero class on the records, and the half-turn face's one corner is the scar. The mixed faces are dead for the tick (one has steps of infinite order, but none hyperbolic)

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free), by hand with a computed check.
This note closes card W-F7 (`relays/cards/CHAT1_W-F7_the_mixed_faces.md`, 9fee774c5).

**How it was checked.** Argued by hand for histories of every length; not independently checked. Computed once, on
this seat's own code, with expectations committed first, for the 2,800 products of at most four moves.
- **The sealed run.** The script (sha256 `d2a3c86e…4d89fc42`, pushed at 9fee774c5) was run once; its output was
  committed (87ef20dda) before it was read. All four expectations were met as coded.
- **Post hoc 1.** It was committed before its run (5553c2300), with output 2340ca390. It is **not blind**: it was
  written after the sealed output was read, to correct a fault found in reading (§ 3). It met all four of its
  expectations.
- **The helpers** are W-F2's, taken by text.

## 1. The faces and the results

A face says, for each letter of W₃ = ⟨a, b, c | a², b², c²⟩, whether it is a mirror (M) or a half-turn (H). A history
step must send mirrors to conjugates of mirrors and half-turns to conjugates of half-turns, and must send the face's
corners to its corners.

| face | corners (rotation elements) | steps among the 2,800 | matrices up to sign | hyperbolic | parabolic | finite order |
|---|---|---|---|---|---|---|
| MMM (control) | ab, bc, ca | 538 | 6 | 0 | 0 | 538 |
| HHH (control) | the puncture abc | 2,800 | 132 | **512** (144 of them det −1) | 1,084 | 1,204 |
| MMH, half-turn a / b / c | pq and qrpr | 329 / 384 / 329 | 4 | 0 | 0 | all |
| MHH, mirror a / b / c | p qrprq | 670 / 538 / 670 | 16 | **0** | 374 / 264 / 374 (all det +1) | 296 / 274 / 296 |

- **The controls.** MMM reproduces W-F2's M2 (538 steps, 6 matrices, all of finite order). HHH reproduces W-F2's M1,
  and its count of 380 under the sealed test.
- **Which run each column comes from.** The table's hyperbolic, parabolic and finite-order columns use post hoc 1's
  corrected classification (§ 3). The sealed run's HHH parabolic count was 1,144.
- **A second computation.** The referee of this note recomputed every count in the table independently, over all
  2,800 products, on its own code: its own conjugacy test, its own H₁ map, and a spectral-radius classification.
- **MHH's infinite-order step.** The half-twist of the two half-turns, {a ↦ a, b ↦ c, c ↦ cbc} ("swap b,c" after
  "c through b"), is a step of MHH(a). Its matrix is R = [[1, 0], [1, 1]].

## 2. By hand, for steps of any length

- **A step's action on a corner.** A step f preserves parity, since each letter goes to a word of odd length. It
  sends each corner's rotation element ρ to gρ′^(±1)g⁻¹, where ρ′ is a corner's rotation element (possibly another
  corner's).
  - On H₁ of the even part ⟨x = ab, y = bc⟩, conjugation by an even element is trivial. Conjugation by an odd element
    is −I, since a(ab)a = ba and a(bc)a = (ab)(ca) give −x and −y.
  - So f₊ sends each corner's class [ρ] to ± a corner's class.
- **The classes.** In the basis x, y:
  - **HHH:** (abc)² = ab·ca·bc has class x − (x + y) + y = **0**. It is a commutator (the scar, aλa = (abc)⁻²), so it
    places no constraint.
  - **MHH, mirror a:** a·bcacb has class x − (x + y) − y = **−2y**. The other labellings give one non-zero class too.
  - **MMH, half-turn c:** ab = x and bcac = y + (x + y) = x + 2y: **two independent classes**.
  - **MMM:** x, y and −(x + y): **three classes**.
- **The consequence.**
  - If a matrix sends a non-zero v to ±v, it has an eigenvalue ±1. At det +1 its trace is then ±2, so it is parabolic
    or ±I; at det −1 its trace is 0, so it has order 2. Either way it is **not hyperbolic**. That covers MHH.
  - If it permutes a finite set of lines spanning the plane, some power fixes each line and is ±I: **finite order**
    (for two lines, the fourth power is I). That covers MMH (two lines) and MMM (three).
  - Only HHH, whose puncture class is 0, leaves room for a hyperbolic step. It has them: the tick itself, realised by
    {a ↦ aca, b ↦ a, c ↦ b} ("swap a,b" ∘ "swap a,c" ∘ "a through b"), which acts on the records as x ↦ xy, y ↦ x.
- **So:** a corner with a non-zero class on the records rules out a hyperbolic step. Among the four faces, only the
  all-half-turn face has no such corner, and it does have hyperbolic steps. The converse is shown for this face only,
  by example. There the corner is the scar.

## 3. A fault found in reading, and its correction (post hoc 1)

- **The fault.** The sealed script called a matrix hyperbolic exactly when |trace| > 2. That test is complete only at
  det +1. At det −1 every matrix with non-zero trace is hyperbolic (the tick [[1, 1], [1, 0]] has trace 1), so the
  test missed det −1 matrices with |trace| 1 and filed those with |trace| 2 as parabolic. W-F2's M3 used the same
  test.
- **The corrected count.** Post hoc 1 classifies correctly, and finds 512 hyperbolic steps on the half-turn face, 144
  of them with det −1. **W-F2's "products with a hyperbolic matrix: 380" undercounts.** Its conclusion is unaffected:
  W-F2's M2 rests on finite order, which is exact.
- **The mixed faces under the corrected test.** No step is hyperbolic. Post hoc 1 finds no hyperbolic MHH step, so no
  sealed "parabolic" MHH step has det −1: the corrected parabolic counts (374, 264, 374) equal the sealed ones. W4
  stands. MMH and MMM rest on finite order and are unaffected.

## 4. What it means for the system (W-C8 part 4's page)

- **Line 2 (their face) moves from "established among move sequences up to length four, the mixed faces open" to
  "derived from line 5" (a hyperbolic act):**
  - by hand, for steps of every length, over all four faces;
  - the two mixed faces are now closed;
  - MHH carries infinite-order steps (the half-twist), so a weaker requirement, "some non-periodic history", would
    not kill it. The tick's hyperbolicity does.
- **The faces and the scar are tied.** A hyperbolic history needs the face's corners to have class zero on the
  records, that is, to lie in their commutator subgroup. Among the four faces that singles out the half-turns, whose one corner is the scar of line 3. So, granted that a
  history step must respect the face (its letter types and corners), line 2 follows from line 5 among the four faces
  of W₃. The reason is line 3's scar, the one corner whose class vanishes.

## 5. Typed

| statement | how checked |
|---|---|
| the census in § 1, products of at most four moves | computed once; expectations committed first (sealed); the corrected classification computed once in post hoc 1 (not blind); recomputed independently by the referee |
| only HHH admits a hyperbolic step, steps of every length | not independently checked (by hand) |
| W-F2's count of 380 undercounts the hyperbolic steps | computed once (post hoc 1) |
| line 2 follows from line 5, granted that steps respect the face | not independently checked (by hand) |

## 6. Files

`relays/chat1_2026-11-14_wf7/`:
- `wf7_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf7_checks_out.txt`, `wf7_checks_err.txt` (empty);
- `wf7_posthoc_1.py` and `wf7_posthoc_1_out.txt`.

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
