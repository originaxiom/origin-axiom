# B1927 — The end fixed by the fibre's own geometry: B1667's canonical end is covariant, so the read-out needs no chosen end, only a convention

**Verdict: PROVED** for the covariance, the periodicity, the positivity and the two conventions' difference, and for the
corner that rules out the maximal horoball under analyticity (§ 3). The choice of the length-2 end rests on that stated
regularity condition. cc (main), 2026-11-14 (S306p). Data-free; B1667's
sealed instrument, used unchanged. Values in the json files only. **0 of 19.**

## 1. The answer first

- **The question** (B1924's correction): B1924 held the end at two chosen constants. Is the end a free continuous
  input?
- **The record already fixes it** (B1667, 2026-10-16). The fibre's own hyperbolic metric gives a canonical end radius
  L = log(1/ε), with ε a radius in the flat coordinate z of ℂ/(ℤ + τℤ), from an intrinsic horocycle. There are two
  conventions: the maximal embedded horoball (L_max) and the horocycle of length 2 (L_2).
- **It is covariant.** Under τ → −1/τ the flat coordinate scales by 1/∣τ∣, so L(−1/τ) = L(τ) + log∣τ∣. That is exactly
  the frame's own covariance (B1724, B1921). So the invariant form L̃(τ) = L(τ) + ½ log Im τ − (γ + log π) is a modular
  function, not a constant: B1921's L̃ is fixed point by point by the geometry.
- **Checked** (`verification/grid.py`; the end on 53 new points of the fundamental domain up to Im τ = 6, where the
  read-out's reduced nodes stay below 5.6 for n ≤ 22):
  - B1667's sealed values reproduced exactly;
  - the mirror symmetry to 2.9 × 10⁻¹³;
  - the covariance L(−1/τ) = L(τ) + log∣τ∣ to 4.0 × 10⁻¹² at 0.25 + 1.5i.
  The first version ran to Im τ = 10 and stalled at 8, where the instrument is slow. It was capped at 6 after measuring
  where the threads go.
- **So the frame read with the canonical end repeats along a thread at its own line with nothing chosen**
  (`verification/canon_readout.py`, E1): on the golden thread the outputs at τ and one period later agree to
  1.3 × 10⁻¹³.
- **Both conventions keep every channel's weight positive** (`verification/positivity.py`). Along the threads of 60
  allowed words at n = 16, 22 767 nodes, no channel with a non-zero residue is cut, for either convention. Positivity
  does not decide.
- **The two conventions give different read-outs.** The paired comparison over the same words gives a median ∣z∣ near
  20, with 92 % of the numbers above 2, at the mark and at the twin.
- **The read-out with the canonical end** (`canon_readout.py`, 60 words at n = 16 and 22, the mark and the twin;
  `canon_compare.py` → `canon_compare_run.txt`; noise gives a median ∣z∣ of 0.67):

  | convention | n = 16 against 22, the mark; the twin | the mark against the twin at n = 22, paired |
  |---|---|---|
  | L_max | 0.93 (12 % above 2); 1.41 (0 %) | 1.01 (0 % above 2) |
  | L_2 | 1.10 (21 % above 2); 1.06 (4 %) | 0.87 (0 % above 2) |

  This is looser than with the constant ends (B1924). The twins are not told apart beyond two errors at n = 22. But the
  medians are near 1, and at the mark the read-out still moves between n = 16 and 22. With the mark's understated
  errors (B1924's addendum) this fits slower settling. Not shown: convergence with the canonical end at n ≥ 28. B1928's
  ergodic integral with the canonical end gives the predicted limit directly.

## 2. What this means

- **The end is not a free continuous input.** B1921's L̃ is a modular function fixed by the fibre's geometry. B1924's
  constants are replaced by it. What remains is **one bit: the convention** (maximal horoball or length-2 horocycle),
  the record's decision 5, and it changes the read-out.
- With B1928, the read-out on the whole then depends on no point of the modulus, no reading point and no end constant.
  It depends on that one bit, and on the principle's own measure. § 3 settles the bit by analyticity: the
  horocycle of length 2.

## 3. Which convention: decided by analyticity (the author's reminder of 2026-11-14)

- **The criterion, written before the runs.** L_max = (2π/λ)(1/min∣c_γ∣ − Im B) is a minimum over group elements, so
  where two elements tie for the minimum it can have a corner. L_2 = π − (2π/λ) Im B involves no minimum. Every other
  part of the frame is real-analytic in τ: the theta functions, the channel norm's Kronecker limit (B1919), the
  residues. An end with corners would make the frame, and the read-out, non-analytic along them.
- **Where no tie occurs, both are smooth.** Along Re τ = 0.25 (Im 1 to 3) and Im τ = 1.3 (Re 0 to 0.5), the two
  smallest ∣c_γ∣ never meet, and neither end's second difference spikes (`smoothness.py`). At the mirror line
  Re τ = ½ both grow like x² (ratio 4.00, `mirror_lines.py`). At Re τ = 0 the instrument's values near the symmetric
  locus are not reliable at this resolution, but the two smallest ∣c_γ∣ do not tie there either (gap 0.22 and 0.72).
- **Along the bottom arc ∣τ∣ = 1 two elements tie exactly.** Just above the arc their gap is about 1.5 × 10⁻³ at a
  distance of 0.002, at every Re τ tested (`arc_gap_run.txt`). The invariant end is symmetric under the inversion across
  the arc (S with the mirror), so it is smooth there only if its radial slope is zero.
- **The decisive run** (`arc_corner.py`, at 80° and 70° on the arc; ratio 4 means the change grows like (r − 1)², a
  smooth end; ratio 2 means it grows like ∣r − 1∣, a corner):

  | convention | ratio, Δr 0.01 to 0.02 | ratio, Δr 0.02 to 0.04 |
  |---|---|---|
  | L_max, the maximal horoball | **1.99** (both angles) | 1.98 |
  | L_2, the horocycle of length 2 | **3.96** (both angles) | 3.92 |

- **So the maximal-horoball end has a corner along the arc ∣τ∣ = 1 and along every image of it under SL(2, ℤ). The
  length-2 end is smooth there.** Requiring the end to be real-analytic in τ, as every other part of the frame is,
  selects the horocycle of length 2.
  - This does not make the choice disappear. It replaces a bare convention by a stated regularity condition, which is a
    weaker and more natural input than a choice of horocycle.
  - The length-2 horocycle is also the one embedded in every cusped hyperbolic surface (Adams), so it is canonical
    without reference to this surface.
- **Not shown:** that L_2 is real-analytic everywhere. It is smooth wherever tested, and its formula contains no
  minimum. Analyticity of the uniformisation's Im B in τ is standard but not re-proved here.

## 1a. Seen first

`VERDICT topic-sweep /canonical end|maximal horoball|length.2 horocycle|end convention|decision 5/: 20 of 1665 arcs on
main match (NEGATIVE 6, PROVED 14); 25 register rows match (DECLINED 1, DONE 22, QUEUED 2)`. The arcs that used the canonical
end (B1656 to B1660, B1692 to B1712, B1795 to B1807) worked at a fixed end, and none decides between the two
conventions. B1816 (the accessory parameter is a Weil–Petersson primitive) supports the length-2 end's analyticity. Read for this arc:
- B1667, the canonical cusp and its two conventions.
- B1724, whose frame used the canonical end point by point along a column.
- B1921, the invariant end.
- B1922 and B1924.

**Literature:** Shimizu's lemma and the maximal cusp; the embedded horocycle of length 2 on a cusped hyperbolic surface
(Adams).

## Files

- `verification/grid.py` → `grid.json`, `grid_run.txt`.
- `verification/canon_readout.py` → `canon_readout.json`, `canon_readout_run.txt`; `canon_compare.py` →
  `canon_compare_run.txt`.
- `verification/positivity.py` → `positivity_run.txt`.
- `verification/smoothness.py` → `smoothness.json`, `smoothness_run.txt`.
- The lock: `verification/test_b1927_canonical_end.py`.
