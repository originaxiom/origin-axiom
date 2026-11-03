# W182 — the down–lepton factor on the centre lines (main's P-567, Q1): B1656's frame's own double ratios at the cusp and at τ = i on the 90 lines (2/5 + j/3, k/30), against the Georgi–Jarlskog shape and the data (the rule, committed before the script)

The SM-derivation seat, 2026-11-03, at the owner's "continue". The question is main's P-567, Q1 (S289, B1827, FL-08).
Committed and pushed before the script that reads it exists. Nothing here is a result.

## Why

- **Main's framing ledger (S289, B1827, FL-08)** read the frame's lines as centre Wilson lines.
  - On order-5 lines the frame is minimal SU(5) exactly: Y_u is symmetric and Y_e = Y_dᵀ. So the lepton factor c = 3
    used in B1825 is the Georgi–Jarlskog Clebsch, put in by hand.
  - The Z₅ × Z₃ lines, of orders 15 and 30, lie outside the sealed reach (orders 1–12).
  - P-567, Q1 asks for the lepton/down factor on the (2/5 + j/3, k/30) lines at c = 1, data-free. Does any centre line
    give 3, or does the Clebsch need a non-abelian Higgs component? The blind reader (A5) expects none gives 3.
- **This seat's frame has no c**, so it reads the question at c = 1 as asked. W178–W181 settled the factor at the cusp
  and at τ = i on all 266 census lines. The 80 new centre lines are outside that census.
- **This seat takes Q1 as W182** (relay §341), so that main need not duplicate it. Main's own run, if any, stays
  independent.

## The structure (computed data-free for this rule; no six, ratio or D computed)

- **The lines.** (a, b) = (2/5 + j/3 mod 1, k/30) for j ∈ {0, 1, 2} and k ∈ {0, …, 29}: 90 distinct lines, a ∈ {2/5,
  11/15, 1/15}.
  - 10 are census lines, the (2/5, m/10): five of order 5 and five of order 10.
  - The other 80 are new: 40 of order 15 and 40 of order 30.
  - No line has a θ-zero channel in any sector.
- **No integer-λ kernel.** 3a ≡ 1/5 (mod 1) on every line. So W177's norms converge exponentially at the cusp, with no
  linear part (W178's regime; W181's shift is not needed).
- **Where down and leptons differ.** Both sectors have ū = 3w. Their residues differ only through (q_L − q_R)w, which
  is −w for the down quarks and −9w for the leptons.
  - The lepton's is congruent to ± the down's modulo the lattice exactly when 8w or 10w lies in it. Among the 90 lines
    that holds on the 10 census lines only.
  - On the 80 new lines the Z₃ part of the line enters the down sector's −w but not the lepton's −9w, since 9 ≡ 0
    mod 3. These are lines where the frame separates down quarks from leptons through the colour centre.
- **Hand expectation, not computed.** On the 80 new lines the lepton's (q_L − q_R)w has imaginary fraction 2/5, and
  the down's has 14/15 or 4/15. So the leading cusp exponents of the two sectors may differ, and the cusp double ratios
  may run rather than converge.

## The computation (fixed now)

- **The frame is W178's,** unchanged: B1656's frame as W162's point computes it, W177's norms in working precision, no
  residue cut, and the θ-zero rule. W178's two precisions and its status rule apply per feature.
- **The quantities.** These are W179's: ln r₂ = f₃ − f₅, ln r₁ = f₄ − f₆ and ln D = ln r₁ − ln r₂, from the six f₁…f₆ =
  ln of (m_c/m_t, m_u/m_t, m_s/m_b, m_d/m_b, m_μ/m_τ, m_e/m_τ). The Georgi–Jarlskog shape is (r₂, r₁) = (1/3, 3), with
  D = 9.
- **Part A, the cusp.**
  - W178's point function runs on all 90 lines at Re τ 1/8 and 3/8 and Im τ 6, 8, 12, 16, 24, 32 and 48 (W178's
    ladder).
  - Where the down and lepton exponents e_i(32, 48) agree within 0.005 for both i, the double ratios have a finite
    cusp limit, read at Im τ 48. The change from 32 to 48 is the check, as in W179.
  - Elsewhere they run, with no forced value.
  - A line and Re τ with a zero or unresolved feature at any height, or a failed point, is excluded, as in W179.
- **Part B, τ = i.**
  - W178's point function runs on all 90 lines at τ = i. A line whose four features in D are not all resolved there
    is excluded, as in W179.
  - For a read-out, the absolute singular values of the down and lepton Yukawas are also taken at τ = i, at the two
    precisions, giving σ_g(e)/σ_g(d) for g = 3, 2, 1, heaviest first. Each sector's κ belongs to the frame.
- **Points:** 90 × 2 × 7 at the cusp plus 90 at τ = i, 1350 in all, on four workers.
- **The data,** read once (no new look): D = 10.58 ± 0.11 (P-094), with r₂ = 0.318 and r₁ = 3.365, as in W179.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| C0 | **The tie to the record.** On the 10 census lines, the six at every ladder height (both Re τ) and at τ = i equal W178's stored six and W179's τ = i six within 10⁻⁶ in ln, on every feature resolved in both | 97% |
| C1 | **The tie law.** On the five order-5 lines \|ln D\| ≤ 10⁻⁸ at every height, both Re τ, and at τ = i; on each of the 80 new lines \|ln D\| > 10⁻⁸ at τ = i | 85% |
| C2 | **The cusp runs on the new lines.** On every one of the 80 new lines, at both Re τ, the down and lepton exponents differ (by more than 0.005 for some i): no finite cusp limit | 70% |
| C3 | **No Georgi–Jarlskog shape.** No line, at a finite cusp limit or at τ = i, has both r₂ and r₁ within a factor 1.25 of (1/3, 3) | 85% |
| C4 | **No match to the data.** No line's finite cusp D and no line's D at τ = i lies in [10.25, 10.91] | 85% |
| R | **Read-outs** (no predictions): per line and point, ln r₂, ln r₁ and ln D with their status; the exponent differences at the cusp; at τ = i, σ_g(e)/σ_g(d) for each generation; the lines where one factor (r₂ or r₁, or one σ_g(e)/σ_g(d)) lies within a factor 1.1 of 3 or 1/3; the distinct values; the ten nearest to (1/3, 3) and to the data's (r₂, r₁) and D | — |

## What the outcomes mean (fixed now)

- **C0 fails:** the frame on these lines is not W178's as computed. The arc's values are withheld and the failure
  recorded.
- **C1 fails:** the tie law as stated is wrong on the lines named. That is recorded with the lines.
- **C2 fails:** some new lines have a finite cusp limit. Their values are read under C3 and C4.
- **C3 holds** (with C0): in B1656's frame no centre line gives the Georgi–Jarlskog shape at the points the principle
  marks. This answers P-567, Q1 in this frame. The 3 is not supplied by the lines; a Clebsch would need more structure
  (main's "non-abelian Higgs component"), as A5 expected. Single factors near 3 are read-outs, not a shape.
- **C3 fails** (a line within 1.25 of (1/3, 3)):
  - It is the record's first Georgi–Jarlskog-like split from a line alone, without c. The line is a thread choice
    (W140).
  - Its specificity is read from how many of the 90 lines come near.
  - It becomes a sealed target for the next arc, with main. Nothing is banked here.
- **C4 fails:** a line's D lies within 3σ of the data. It is read as in W179's G2: the record's first such value on a
  centre line, a sealed target, nothing banked.

## Weave or thread

- **neither (a frame census over the centre lines P-567 names, at the points the principle marks).** The frame is
  B1656's. The lines are P-567's whole set (every j and every k), none picked. The weave's own answer on the split
  stays W140's, D ≡ 1.

## What stays out

- The census's other 256 lines, settled in W178–W181.
- Other τ: finite heights other than the ladder, and τ = ω, which lies below B1667's column (as in W179).
- A singlet or non-abelian Higgs component (P-566); other readings; c ≠ 1; the up sector and the CKM.

## Looks

- One look at the data, counted: C4 and the read-outs read D and (r₂, r₁) once. No line is selected for a later fit.

## Seen before the rule (disclosed)

- **Main's S286–S290, read in full by their commit messages:**
  - FL-08 and P-567;
  - main's order-5 check, which on (2/5, 0) and (1/5, 3/5) gives σ(e)/σ(d) = 1 and Y_e = Y_dᵀ, and on (2/5, 1/10) and
    an order-7 line gives spectra differing at two finite τ;
  - S290's 45-like singlet note.
- **W179's and W181's outputs, read in recording them,** including the values on the 10 census lines here: at the cusp
  they tie (D = 1), and at τ = i the order-5 lines tie.
- **The structure above,** computed for this rule: the line list, orders and census membership; the θ-zero channels;
  3a mod 1; and the tie law's lattice condition.
- **Not computed:** no six, ratio, D or singular value on any new line, at any point.

## Discipline

- This rule is committed and pushed before the script exists in the tree.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
