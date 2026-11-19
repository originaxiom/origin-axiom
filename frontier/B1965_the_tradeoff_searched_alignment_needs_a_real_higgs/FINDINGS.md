# B1965 — In frame C under the charge rule, an adversarial search over every Higgs triplet finds alignment only with a nearly real Higgs and no heavy-pair hierarchy

**Verdict: OPEN.** A conjecture, with a search that supports it at four points. Main, 2026-11-19. Data-free. Register
rows P-847 and P-879. **0 of 19.**

> *Corrected 2026-11-19, the same day: "a value below −2 would be a counterexample" is too loose. A nearly degenerate coupling can score below −2 without alignment, because the logarithm outweighs the penalty. A counterexample needs the smallest diagonal at 0.9 or above and three distinct nonzero masses. No run here came near −2: every one ended on the alignment boundary with m₂/m₃ 0.57 to 0.68. So the result stands. B1967 shows that with free channels the interior has counterexamples near reality 0, so the exclusion found here must come from frame C's own channels.*

## Seen first

- **Swept, in the record's own words:** `VERDICT topic-sweep /nearly null|non-null Higgs|reality of the Higgs|V_ud|hierarchy and (the )?alignment|dichotomy|Standard Model's reading|trade-off/: 31 of 1706 arcs on main match (NEGATIVE 6, OPEN 4, PROVED 21); 19 register rows match (DONE 12, QUEUED 7)`.
- **B1739 (PROVED):** under the Standard Model's reading (this arc's charge rule) a nearly null Higgs misaligns the
  light generation. With the channels off it is exact: the light states are h̄ and h, so |V_ll| = |h·h|/|h|².
- **B1740 (NEGATIVE as sealed, for F₋₂):** a non-null Higgs aligns the light generation and loses the hierarchy.
- **B1742:** two nearly null directions read S in every sector give the hierarchy and alignment, but the mixing is
  too small.
- **B1743** verifies the web seat's R5: in the idealised up channel (u = a₃h₀, no antisymmetric weight), m₁ = 0,
  m₂m₃ = |a₃|²|h·h| and m₂/m₃ ≥ |h·h|/4. So there the Higgs's non-nullity sets the floor of the heavy pair. B1743 calls
  the combination with B1739 "a reading, not a derivation", because the real channels depart from both idealisations.
- **B1963 and B1964** are frame C's form of B1739.
- **The literature:** none bears on frame C's coupling.

## What was run (exploratory)

The question was stated in each script before its run. No expectations were written or hashed: this is exploration,
labelled as such.

- **`verification/scan.py`.** At three fixed points of frame C (height 3 and 6 at (1/5, 2/5), height 3 at (3/7, 1/7)),
  400 constant Higgs triplets h ∈ ℂ³ in place of DR, sampled so that the reality r = |h·h|/|h|² spreads over [0, 1].
  - Under the charge rule (up S̃, down S) the script records |V_ll|, the smallest diagonal |V|, and each sector's
    m₂/m₃ and m₁/m₃.
- **`verification/adversary.py`.** At four points, Nelder–Mead from 12 starts (400 evaluations each) over h, unit norm
  with its global phase fixed.
  - It minimises log₁₀ max(m₂/m₃ up, m₂/m₃ down) + 20·max(0, 0.9 − smallest diagonal).
  - A value below −2 would be a counterexample: aligned to 0.9, with both heavy-pair ratios below 1e-2. That
    threshold is written in the script, before its run.

## The results

**The scan.** At each point, no triplet has an aligned mixing with both sectors' m₂/m₃ ≤ 1e-2.
- Aligned triplets are rare: 2, 1 and 11 of 400. Every one has max m₂/m₃ ≥ 0.68.
- The heavy-pair hierarchy grows with the reality r. The median up m₂/m₃ is 0.07, 0.011 and 0.011 for r < 0.05, and
  about 0.5 for r > 0.8.

**The adversary:**

| point | best objective (a counterexample needs < −2) | smallest diagonal | up m₂/m₃ | down m₂/m₃ | r |
|---|---|---|---|---|---|
| height 3, (1/5, 2/5) | −0.166 | 0.900 | 0.68 | 0.68 | 0.939 |
| height 6, (1/5, 2/5) | −0.174 | 0.900 | 0.67 | 0.67 | 0.977 |
| height 3, (3/7, 1/7) | −0.239 | 0.901 | 0.58 | 0.57 | 0.997 |
| height 6, (2/7, 5/7) | −0.168 | 0.900 | 0.68 | 0.68 | 0.959 |

Every start ended against the alignment constraint, with a nearly real Higgs and the heavy pair nearly degenerate.

## The conjecture (P-879)

It is a consistency condition between two outputs of one coupling, the mixing's alignment and the heavy pair's ratio. It is
not a finite classification, and it selects no Higgs: it says which pairs of outputs no Higgs can give together.

**In frame C, under the charge rule, for every Higgs triplet h at every point where the channels are non-degenerate,
an aligned mixing forces the heavy pair together:** the smallest diagonal |V| ≥ 0.9 implies max m₂/m₃ ≥ c, with c
about 0.5 on this evidence.

- **Its two halves are on record in idealisations:**
  - B1739's exact lemma: |V_ll| = r with the channels off;
  - R5's floor: m₂/m₃ ≥ r/4 in the idealised up channel.
- **What a proof needs:** both halves in the full coupling at once.
  - The coupling is bilinear in the Higgs and the channel quaternions, Y_ab = 2σ_a·Re(C_a QJ S C_b Mwᵀ), with
    σ = (−1, 1, 1).
  - The cross-product channel alone, [h]_×, has singular values (|h|, |h|, 0) for every complex h. So the heavy pair's
    splitting comes only from the other channels.

## What it means for the goal

- **If the conjecture holds, frame C cannot carry an aligned mixing with a hierarchy under the charge rule, whatever
  its Higgs.** The choice of Higgs direction (A:A04) then leaves the mixing's fate unchanged.
- **The record's frames would then hold no value-specific card for the mixing** unless the charge rule is overridden
  by a principle, which P-847 has not found.

## Not established

- **A proof.** A search over five real parameters at four points is evidence only.
- **Points other than these four,** and Higgs fields that vary with τ (here h is constant at each point; a modular
  Higgs is one value of h per point, so it is covered pointwise).
- **Any comparison with data.**

## Files

`verification/scan.py` with `scan_run.txt`, `verification/adversary.py` with `adversary_run.txt`. The lock is
`verification/test_b1965_tradeoff.py`.

0 of 19.
