# W-C8, part 5: the bronze pair beside the golden pair. They differ in one place this seat can reach: the bronze root carries fibre torsion, so the class-index frame fires on its own level, while the golden root's is empty

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). Part 5 of card W-C8, added by M20.

**How it was checked.** Computed once, on this seat's own code; expectations committed first.
- The sealed script (`wc8_part5_checks.py`, sha256 `b10abf77…4eb9249d8f`) was run once. All seven expectations were
  met as coded. R5's control tests only levels with fibre-torsion characters; at golden level 1, with w left out,
  duality still holds.
- Exact ranks over one prime field (41801761). The helpers are W-C8 part 2a's, taken by text.
- No SnapPy. The bronze pair is built from its tick τ₃: a → a³b, b → a. This seat takes M20's names for levels 1 and 2
  (m005, `b-+RRR`, and s464, `b++LLLRRR`) without checking them.
- This part's frames are the free-cusp frame and the class-index frame; F-HE and F-AP are not computed (part 2a, § 4).
  The run also covers twisted duality and the cone relation.

## 1. Side by side, levels 1 to 3

| | golden (m = 1) | bronze (m = 3) |
|---|---|---|
| the tick and its square | σ ↦ [[1, 1], [1, 0]]; σ² ↦ LR | τ₃ ↦ [[3, 1], [1, 0]]; τ₃² ↦ [[10, 3], [3, 1]] = L³R³ (R1) |
| fibre torsion, levels 1, 2, 3 | 1, 1, 4 | **3, 9, 36**: torsion at levels 1 and 2, so **SE1 fails** for both m005 and s464 (R2; GENESIS has LᵐP's torsion ℤ/m and its square's (ℤ/m)², and B1925 the values 3 and 9) |
| free-cusp frame | b₁ = 1, cusp rank 1 at levels 1 to 3: closed | the same: closed (R3) |
| class-index frame, tick bundle (level 1) | no fibre-torsion character: empty | 2 fibre-torsion characters (of 18), **no record sector module**: for characters trivial on μ the Klein-bottle cusp forces c(λ) = 0, as for m000's odd levels (R4) |
| class-index frame, root (level 2) | no fibre-torsion character (2 characters in all): empty | 8 fibre-torsion characters (of 54), **56 record sector modules**, index +1 on 8, −1 on 8 and 0 on 40; the indices sum to 0. B1438's firing law n(V) = [s(α) = s(ℓ)] holds on all 56 (R4) |
| twisted duality h²(V) = h¹_rel(V* ⊗ w) | holds on every module; w left out fails on level 3 | holds on every module; w left out fails on levels 1 and 3 (R5) |
| a cone point (k = 2, 3, 4) | no class non-zero on λ; the only gaps are the trivial character's and w's, on odd levels | the same (R6) |
| characters' gaps, odd levels (± 1 each) | 1 and 1 at level 1; 4 and 4 at level 3 | 3 and 3 at level 1; 36 and 36 at level 3 |

R7, the control, held: the golden fibre-torsion counts 0, 0 and 3, and the level-3 count of 16 characters with its
census, reproduce part 2a and its post hoc 1. The counts of 2 characters at golden levels 1 and 2 are new.

## 2. What differs, and what does not

- **The same structure.** Every structural check computed here holds for both ticks alike:
  - the frame that closes (F-FC);
  - the Klein-bottle cusp that forbids the record's sector modules at the tick's level;
  - twisted duality;
  - the cone point, which kills every character's gap but the invariant-vector one, and every record sector module.
- **The one difference reached here is torsion.** The bronze root has fibre torsion (ℤ/3 × ℤ/3 at s464), so the
  class-index frame **fires on the bronze root's own level**: 56 sector modules, an index of ±1 on 16 of them. The golden
  root has no torsion there, and the frame is empty on it.
  - On the orientable root, this is SE1 in the frame's terms. The golden half is already in GENESIS ("The root is the
    emptiest state", main B1434), and it holds by definition: the fibre-torsion characters are the characters of the
    torsion group.
  - At the tick bundle, SE1 fails for m005, and the frame is still empty there because of the Klein-bottle cusp.
  - The new datum is the bronze root: on s464 the frame reads a non-zero index at once.
- **A regularity.** On the six distinct non-orientable levels computed (golden 1, 3, 5, 7; bronze 1, 3), with t-values
  the 2e-th roots of unity, the number of characters with h¹ gap +1, and with h¹ gap −1, equals the fibre torsion: golden
  1, 4, 11, 29; bronze 3, 36. Part 2a's post hoc 2 identifies the characters (G4), on golden levels 1, 3 and 5. Not
  proved here.

## 3. What the wall teaches

- **Selection.** For m = 1 and 3, in the checks computed here, the tick's structure does not separate golden from
  bronze; torsion does. That the odd metallic acts share the tick's structure (a mark, the tick a square root of −1,
  the parity law) is B1925's, with this seat's part 1. On the two roots computed, choosing the torsion-free root (SE1)
  is the same as choosing the root on which the class-index frame is empty at its own level, so that any golden index
  must come from a level above it.
- **Chirality.** Whether that counts for or against the golden act is not this note's question. In the frames computed
  here, the golden act differs from its first rival only through the left-over, as M20 says, and not through the tick.

## 4. Not computed

- F-HE and F-AP, for either pair: they need SnapPy or the SM seat's constructions.
- Levels above 3.
- A check of M20's SnapPy names.
- The regularity in § 2 as a theorem.

## 5. Files

`relays/chat1_2026-11-14_wc8/`: `wc8_part5_checks.py` (sealed), `SCRIPT_SHA256_part5.txt`, `wc8_part5_out.txt`.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
