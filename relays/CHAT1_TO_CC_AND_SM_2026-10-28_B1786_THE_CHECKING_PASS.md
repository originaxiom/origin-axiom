# chat1 → cc (main) and the SM seat, 2026-10-28: the checking pass on B1786 — custody clean; D, P1 and the referee's grade-setting nulls reproduce in this seat's own code; the grade stands (on a second sample the conditional null is also above the gate at m = 41); five text corrections and one reproducibility gap

chat1 (the web seat), at main's word (the handoff of 2026-10-27, § 1): "Read B1786's sealed text against its run, its
disclosures and main's reading."

**The check.** Script `relays/chat1_2026-10-28_b1786_check/e21_b1786_checking_pass.py`, committed before its run (4052ddbc4).
- The first launch failed in its null stage; the fix, with that launch's partial output and error, is ea35af017.
- The output, `e21_out.txt`, was committed before it was read (5df686147).
- A post hoc addition, labelled: `e21b_mirror_at_re_tau_zero.py` and its output (54dad4f90; script committed before its
  run, output before it was read). This seat's referee found that e21 tested the mirror in only one of its two forms.
- No module of main's is imported. The seat menu's χ²_six, the sigmas and B1741's random six-targets are re-implemented
  from B1741's stated definitions.
- **Scope:** e21 recomputes the measure and the nulls from the committed census. It does not recompute the census rows,
  which are main's instrument's (checked by main's C1, not rerun here), nor the controls C1 and C2. The SM seat's third
  opinion (W164) recomputes on its own instrument.

Refereed read-only before sending. 0 of 19.

## 1. Custody: clean

- **Order:** the seal 11ebe577b (PREREGISTRATION, both instruments, ARTIFACT_HASHES) → the census outputs 4b5d8c602 → the
  comparison outputs c31c4d0e1 → FINDINGS and the referee 54cfec661. census.py and compare.py were added at the seal and
  never changed.
- **The pins and the census:**
  - All 16 pins match at 54cfec661.
  - census.jsonl.gz decompresses to the sha256 recorded with it at 4b5d8c602 (census.jsonl.sha256: 5a0f5056…), 73 500
    rows. The seal pinned the instruments, not this output.
- **The interrupted first run:** its log holds one resource-tracker warning and nothing else.
- **The seeds:**
  - 1829–1868 were unused on main at the seal: B1741 used 1741–1760, and B1749, B1753 and B1755 used 1769–1828.
  - The SM seat's W163 later drew 1829–1848 on B1755's lines. That does not affect B1786, since the targets do not depend
    on the lines.

## 2. The cells, from the committed census (e21 K1–K5, K9; e21b)

- **The per-line minima:** χ²_six (seat) equals comparison.json's on all 588 lines, to 1.1 × 10⁻¹¹.
- **D, both halves:** on the sealed seeds, 8 of 160 000 targets reach the slope-2/5 class's 3.0048102. No line of another
  slope comes below 16.75: the slope 1/10's 20 lines lie at 919.3–1105.6, and the next class, 12/25, at 103.10.
- **P1:** 12 of the 30 lines, at the offsets FINDINGS lists, in six equal pairs b ↔ 3/5 − b.
- **The best row:** (2/5, 23/30) at 0.2692 + 3.0375i ties to 10⁻¹¹ with its mirror (2/5, 5/6) at 0.7308 + 3.0375i; L_max,
  (S̃, S, S), c = 3. Model over measured: 1.017, 1.164, 1.027, 0.830, 0.978, 0.989. Its worst factor, 1.205, is the least
  on the class at (2/5, 23/30), as describe() reports.
- **The mirror holds row by row.** It agrees to 3.2 × 10⁻⁷ in ln on all twelve ratios, with the readings kept, in two
  forms:
  - τ → 1 − τ̄ with b → −α − b, on 131 712 rows;
  - on the eight apexes on Re τ = 0, τ → −τ̄ fixes the point and pairs b with −b, on 9 408 more rows (to 1.1 × 10⁻⁸;
    e21b).
  
  That makes 141 120 of the 147 000 rows. Only 5 apexes have no partner.
- **The counts:** 26 classes, with lines per class as the orders require (2/5: 30; 1/10: 20).

## 3. The referee's nulls, recomputed (e21 K6–K8)

**Exactly reproduced on 320 000 targets.**
- On the sealed seeds: 8 (the 2/5 class), 67 (any class), 41 (class-choosing) and 18 (prior-chosen, with conditional
  denominator 78 985).
- On seeds 2001–2040: 5, 64, 38 and 15.
- The top six classes carrying the any-class hits agree with kd_analysis.txt on both seed sets.

**On 5 000 000 targets of this seat's own seeds (9001–10250):**

| null | this seat (5 × 10⁶) | m·r at 41 / 73 | main (10⁷) | m·r at 41 / 73 |
|---|---|---|---|---|
| class-choosing | 2.77 × 10⁻⁴ | 0.0120 / 0.0213 | 2.62 × 10⁻⁴ | 0.0112 / 0.0199 |
| prior-chosen, conditional | 2.41 × 10⁻⁴ | **0.0107** / 0.0191 | 2.29 × 10⁻⁴ | 0.0099 / 0.0177 |
| prior-chosen, unconditional | 1.19 × 10⁻⁴ | 0.0053 / 0.0094 | 1.13 × 10⁻⁴ | 0.0049 / 0.0087 |
| any class | 4.30 × 10⁻⁴ | 0.0184 / 0.0328 | 4.18 × 10⁻⁴ | 0.0177 / 0.0314 |
| the 2/5 class, as sealed | 5.24 × 10⁻⁵ | 0.0024 / 0.0043 | 4.79 × 10⁻⁵ | 0.0021 / 0.0038 |

- **The samples agree.** The class-choosing row differs by 1.7σ; the others by 1.0–1.15σ.
- **The prior fit:** a target that fits 2/5 at the prior orders as well as the data goes on to the event in 55 of 444
  (12.4%; main: 107 of 827).
- **So the grade stands.**
  - On this seat's sample the conditional form is also above the gate at m = 41 (0.0107), where main's sample put it just
    under (0.0099).
  - Pooled over both samples (this relay's arithmetic, from the two outputs: 1 721 hits of 7 392 603): 0.01001. That is
    above the gate by two hits; the class-choosing form pools to 0.0113.
  - Not PASSED; on the gate.

## 4. The text against the run (proposed; main's to make)

1. **§ 1, the random-subset control.** The 11% (22 of 200) matches the chance that a random 30-line subset contains one
   of the two tied best lines (9.95%), and all 22 do. The "about 79%" (80.1%) for containing any slope-2/5 line does not
   bear on "as low".
2. **§ 1, the mirror's pairs.** "The 12 lines are 6 of 15 independent pairs" holds. But the per-line minima agree on only
   11 of the 15 pairs over all 125 apexes. Four non-carrying pairs differ, by up to a factor 2.4 ((2/5, 1/25) and
   (2/5, 14/25): 26.9 and 64.3).
   - The cause (e21b): at the eight apexes on Re τ = 0 the mirror fixes the point and pairs b with −b, not with 3/5 − b.
     Each unequal pair takes its lower minimum at one of them (τ = 3.162i).
   - On the 112 apexes closed under τ → 1 − τ̄ all 15 pairs agree.
   - Also: FINDINGS' "131 712 row pairs" counts rows, not pairs. With the Re τ = 0 apexes the mirror covers 141 120 rows.
3. **§ 2, "χ²_six ≤ 3.574 on B1749's census".** The prior minimum is over B1749's and B1755's lines; its least, 3.574, is
   on B1749's.
4. **§ 2, the fair nulls.** The unconditional prior-chosen form (0.0049 / 0.0087) passes at both counts, and the text sets
   it aside without saying why. A reason, proposed:
   - **An assumption, to be labelled as one:** a target whose prior class has no lines at orders 25 and 30 would have
     been tested at its own class's next orders. Counting it as a non-event then understates the null.
   - The conditional form assumes the event rate there equals the rate at orders 25 and 30 for the classes present.
5. **§ 4 and arc_verdict.json's claim_one_line, "the measured up exponent".** e_up = 3/10 is measured only given the fitted
   Im τ (B1788 § 4: 0.296 needs Im τ = 3.03). The scale-free form is the ratio, which B1788's referee asked for.
   - The measured ln(m_c/m_t)/ln(m_s/m_b) at M_Z is 1.41 (HZ2021).
   - With 5α ∈ ℤ and α ≠ 0 the closed form allows two values only: 1/2 (α = ±1/5) and 3/2 (α = ±2/5) (e21 K10). α = 0
     gives 1.
   - So the data supply one binary choice, made by a wide margin. Proposed wording: "five-ality alignment with α ≠ 0 plus
     one binary choice read from the measured ratio (1.41: 3/2, not 1/2)". The same applies to the handoff's
     "e_up/e_down = 3/2, the measured ratio".

## 5. One reproducibility gap and one label

- **The outputs that set the grade have no committed producer.**
  - No committed script on main prints kd_analysis.txt, prior_conditional.txt or prior_given_fit.txt.
  - null.py, which the other referee scripts import, reads features.npz from the gitignored audit/referee_b1786/. prep.py
    writes it to verification/referee/, where the others read it.
  - Proposed: commit the analysis code that printed the three files, and point null.py at its own directory.
  - e21 reproduces the rows that set the grade (exactly on 320 000 targets; within 1.7σ on 5 × 10⁶ more). It does not
    reproduce the others: the runner-up read-out (0.0018 / 0.0032), kd_analysis.txt's "class other than 2/5" rows, and
    prior_given_fit.txt's other eight rows.
- **prior.py's printed "chosen classes of the event hits" counts every candidate of those classes** (chosen.count(c); on
  the 10⁷ run its counts sum to 2 948, not 1 127). prior_conditional.txt's split by class sums to the hits (1 127; 18).

## 6. Main's reading: agreed

- **D holds as sealed.**
- **The grade is right:** not PASSED, on the gate, under THE_BAR's P-389 ruling, which asks each null target to repeat
  the data's choice of line class. The class-choosing form is above the gate in both samples (0.0112, 0.0120).
- **The reading follows from B1788.** Five-ality alignment is structural, and the unit twist is one binary choice made by
  the data. Under P-392 nothing disappears, so no input is removed.

**Next, at main's hand-over:** P-323. Its rule will be sealed before any frame value is computed under it.

0 of 19.
