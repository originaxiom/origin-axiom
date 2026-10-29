# W180 — the cusp limits on the integer-λ lines: B1656's frame where a kernel norm grows linearly, by its frozen-norm frame and that frame's limit, against W179's G0 and G2 (the rule, committed before the script)

The SM-derivation seat, 2026-10-29, at the owner's "gogogo" (this seat's recommendation after W179).
Committed and pushed before the script that reads it exists. Nothing here is a result.

## Why

- **W179 left two things open** (NOTE, W179).
  - **G0 failed.** 50 of its 110 finite cusp pairs were not settled by Im τ = 48, all on lines with an integer-λ kernel.
  - **G2 failed as worded.** (1/2, 1/5) and (1/2, 3/10) read D = 10.4075 at Im τ 48, inside the data's 3σ window.
    Post hoc 1 showed D still falling (8.29 at Im τ 128), and a three-term fit put the cusp limit near 7.1.
  - The fit is an extrapolation. W179's closing clause therefore rests on a reading, and main has been asked to rule
    on it (relay §335).
- **This arc replaces the fit with the limit itself,** on every line where a kernel norm grows. It computes the frame's
  exact cusp behaviour on all 49 resolved integer-λ lines: the exponents, the power of Im τ each ratio carries, and,
  where the down and lepton exponents agree, the limit of D.

## The structure (computed data-free for this rule; no mass or ratio was computed)

- **Which lines.** A kernel has an integer λ exactly when 3a ∈ ½ℤ, that is a ∈ {0, 1/6, 1/3, 1/2} among the census
  lines. The same holds in all three sectors, since ū = ±3w. That gives 67 lines; 18 are among W178's zero lines, which
  leaves 49 resolved lines. These are exactly W178's resolved lines with slowest rate 0.
- **Which channels.** The integer channels are s = 1 and 2 where 3a is an integer, and s = 3 and 4 where 3a is a half
  integer. On 20 of the 49 lines, one of the two is a θ-zero channel and only one integer channel remains. Every other
  channel on these lines has λ = ±½.
- **The split of W177's series.** On these lines c_s(y) = c_s^∞ + B_s y + ρ_s(y), where:
  - B_s = 4π²/|1 − W_s Q^{−l₀}|² for an integer λ_s = l₀, and 0 otherwise;
  - W_s Q^{−l₀} has modulus 1, so B_s does not depend on Im τ (checked at Im τ 6 and 9 on every line);
  - c_s^∞ = −2π ln 2π for an integer λ and −2π ln(π/2) for λ = ±½;
  - ρ_s falls as e^{−2π Im τ}.
  - With 2πL = 4.040 (L held at its Im τ = 4 value), the integer channels' weights are g_s² = 2πL + c_s = −7.507 +
    B_s y + ρ_s and the others' are 1.203 + ρ_s.
  - On (1/2, 1/5), B₃ = 103.356 and B₄ = 10.912 in the down and lepton sectors. On (1/2, 3/10) the two are swapped.

## The method (fixed now)

- **The frozen frame F(y, Y).** This is W178's frame at Im τ = y (its residues, κ, DR, L, coupling and readings, no cut,
  and the θ-zero rule), with each norm c_s replaced by c_s^∞ + B_s Y. F(y, y) is the true frame up to the ρ_s.
- **The frozen cusp H(Y) = lim_{y→∞} F(y, Y).** At fixed weights everything else in the frame is a q-series. So:
  - the six are exponential in y, with exponents that do not depend on Y;
  - the double ratio D has a finite limit wherever the down and lepton exponents agree.
  - The weights grow only as √Y, while the corrections fall exponentially in y. So the true D(y) = H(y) up to
    exponentially small terms, and the cusp limit of D is the limit of H(Y) as Y → ∞.
- **The limit frame F_∞.** The six's ratios do not change when every weight is multiplied by one number (the coupling
  is linear in M). So H(Y) depends only on g(Y)/√Y. That tends to ĝ, which is √B_s on the integer channels and 0 on the
  others.
  - F_∞ is W178's frame with weight √B_s on the integer channels and no others.
  - Where F_∞'s exponents for the features in D equal the frozen frame's, H is continuous at ĝ. Then D∞ is F_∞'s
    cusp D, computed directly, without extrapolation.
  - Where they differ, D∞ is not given by F_∞. That pair's D is read at the ladder's top Y and flagged, with the power
    of Y it carries.
- **Hand reasoning, not computed:** the weights enter the leading coefficients polynomially, so a feature's frozen value
  goes as Y^p with p a multiple of ½ as Y → ∞.

## The computation (fixed now)

- **Pairs:** the 49 resolved integer-λ lines (W178's register: slowest rate 0, no zero channel) at Re τ 1/8 and 3/8,
  98 pairs. The 18 zero lines are left out, as in W178 and W179.
- **Heights:** y ∈ {48, 64}, at W178's two precisions (doubled once where a feature is unresolved), with W178's status
  rule per feature.
- **The ladder:** F(y, Y) at Y ∈ {48, 64, 96, 128, 256, 1024, 4096} and both heights, 14 points per pair.
- **The limit frame:** F_∞ at both heights, 2 points per pair. 1568 points in all, on four workers.
- **The quantities.**
  - The frozen exponent e(Y) = −[f(64, Y) − f(48, Y)]/(2π · 16) per feature.
  - ln r₂, ln r₁ and ln D from the six, as in W179.
  - D∞ is F_∞'s D at Im τ 64.
  - A pair's exponents agree when the down and lepton exponents of both features agree within 10⁻⁶ at Y = 1024.
- **The data,** read once: D = 10.58 ± 0.11 (P-094's received file, as in W179).

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| H0 | **The tie.** F(48, 48) agrees with W178's stored six at Im τ 48 within 10⁻⁶ in ln, on every feature resolved in both, on all 98 pairs | 97% |
| H1 | **The frozen exponents converge.** On every pair, every feature resolved at all 14 ladder points has the same e(Y) at all seven Y within 10⁻⁶ | 80% |
| H2 | **The frozen exponents are simple.** Every exponent in H1 lies within 10⁻⁶ of a fraction with denominator at most 60 | 85% |
| H3 | **The interchange.** On (1/2, 1/5) and (1/2, 3/10) at Re τ 1/8, ln D of F(64, Y) at Y = 64, 96 and 128 equals post hoc 1's ln D at Im τ 64, 96 and 128 within 10⁻⁶ | 90% |
| H4 | **The limit frame is continuous.** On every pair whose exponents agree: F_∞'s exponents for the four features in D equal the frozen ones within 10⁻⁶; F_∞'s ln D agrees between heights 48 and 64 within 10⁻⁶; and \|ln D(64, Y) − ln D∞\| does not increase along Y = 128, 256, 1024, 4096 (10⁻¹² allowed for exact ties) | 75% |
| H5 | **No exact cusp D near the data.** No pair's D∞ lies within 3σ of 10.58, that is in [10.25, 10.91] | 85% |
| H6 | **The two G2 lines.** D∞ on (1/2, 1/5) and (1/2, 3/10) lies in [6.5, 7.7] at both Re τ | 75% |
| H7 | **W179's classification.** The pairs whose exponents agree are exactly W179's 62 finite pairs on integer-λ lines | 70% |
| R | **Read-outs** (no predictions): per pair, the frozen exponents and their nearest fractions; each feature's power p of Y, from Y = 1024 to 4096 at Im τ 64, and its nearest multiple of ½; on agreeing pairs, r₂∞, r₁∞ and D∞, and D at each Y; the distinct D∞ to 10⁻⁶ and the ten nearest to the data's D; W178's e(32, 48) on these lines minus the frozen exponent, beside −p ln(3/2)/(2π · 16) | — |

## What the outcomes mean (fixed now)

- **H0 or H3 fails:** the split of the norm or the interchange of limits does not hold as computed. The D∞ of the
  pairs named are withheld, and the failure is recorded.
- **H1 or H2 fails:** the frozen cusp is not reached by Im τ 48–64 on the pairs named. Their values are flagged.
- **H4 fails on a pair:** the limit frame does not give that pair's limit. Its D is read at Y = 4096 and flagged, with
  its power of Y.
- **H5 and H6 hold:**
  - W179's G2 hit is a height crossing, now settled exactly.
  - With W179's settled ties, B1656's frame gives no cusp D within 3σ of the data on any line.
  - W179's G2 held as worded at τ = i. So W179's closing clause is met, read with this arc.
  - Then the record's forced routes give no down–lepton factor near the data's. The factor is a candidate entry for
    GENESIS's dictionary data (FK11), and main is asked to rule. It is not a derivation.
- **H5 fails** (a pair's exact cusp D within 3σ):
  - It is the record's first forced cusp D near the data, and the line is a thread choice (W140).
  - Its specificity is read from how many distinct D∞ the census produces.
  - It becomes a sealed target for the next arc, and nothing is banked from it here.
- **H6 fails but H5 holds:** post hoc 1's fit was wrong about the limit. The exact value is recorded.
- **H7 fails:** W179's 0.005 classification misfiled the pairs named. They are corrected here, and W179 gets a dated
  correction note.

## Weave or thread

- **neither (a frame census over every census line with an integer-λ kernel, at the cusp).** The frame is B1656's.
  The lines are the frame's whole class (a ∈ {0, 1/6, 1/3, 1/2}), none picked. The weave's own answer on the split
  stays W140's, D ≡ 1.

## What stays out

- The other 163 resolved lines, settled in W178 and W179.
- Finite heights and τ = i (W179's Part B).
- Other frames, readings and horocycles; the up sector's factor; the CKM.

## Looks

- One look at the data, counted: H5 and the read-outs read D once. No line is selected for a later fit.

## Seen before the rule (disclosed)

- **W179's output and post hoc 1, read in recording W179:**
  - every count and read-out list;
  - the two G2 lines' D at Im τ 6–128 and the fit's A = 7.12;
  - the G0 list of unsettled pairs.
- **The structure above,** computed data-free for this rule with W177's functions. It covers the integer-λ lines,
  their channels, B_s and its independence of Im τ, c_s^∞ and 2πL. No six, ratio or D was computed.
- **Hand reasoning while designing:**
  - the split of the norm and the interchange argument;
  - the limit frame and its continuity condition;
  - the half-integer powers;
  - (1/2, 1/5) and (1/2, 3/10) differ only by swapping channels 3 and 4, which is why their ladders agree.
- **Not computed:** no frozen-frame or limit-frame value at any line, height or Y.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
