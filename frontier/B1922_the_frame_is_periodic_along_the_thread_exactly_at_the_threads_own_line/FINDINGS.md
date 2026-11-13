# B1922 — The frame is periodic along a thread's geodesic exactly at the thread's own line, with the invariant end: the extension condition is what makes the read-out as a thread average well defined

**Verdict: PROVED** (numerically, on the golden thread, with B1724's frame and transport rules). cc (main), 2026-11-13
(S306p). Only deviations between the frame at two points are computed and kept; no output of the frame is printed or
compared with anything measured. **0 of 19.**

## 1. The answer first

- **The question** (P-776's question after B1920 and B1921): can the frame be read as an average along a thread instead
  of at a chosen point of the modulus? That needs its outputs to repeat after one period of the thread's geodesic.
- **Written before the run:** the golden thread's monodromy acts on the modulus as γ = TR: τ ↦ (2τ + 1)/(τ + 1). By
  B1724's transport rules it carries a line (a, b) to (a − b, 2b − a) and the end L to L + log∣τ + 1∣, which keeps
  B1921's invariant end L̃ fixed. The frame's line (2/5, 4/5) goes to (3/5, 1/5), the same line up to sign: the
  extension condition (B1867, B1914). So at that line the covariant readings S and S̃ (B1724) should repeat after one
  period; at a line γ does not fix they should not; S*, covariant only under Γ⁰(2), should not either.
- **The run** (`verification/periodic.py`), the maximum over sectors, ends and readings of ∣log∣ of the ratio of outputs
  at τ and γτ:

  | window | Im τ, Im γτ | the own line (2/5, 4/5): S, S̃ | S* | the line (1/5, 3/5): S, S̃ |
  |---|---|---|---|---|
  | symmetric | 0.745, 0.745 | 3.1 × 10⁻¹⁰ | 2.7 | 2.3 |
  | shifted | 0.829, 0.663 | 9.8 × 10⁻¹⁰ | 1.5 | 3.4 |
  | from the top | 1.118, 0.319 | 7.8 × 10⁻⁵ | 2.7 | 2.5 |

  The third window's 7.8 × 10⁻⁵ is the frame code's loss of precision low in the half-plane (B1724 kept its points at
  Im τ ≥ 0.6); in the first two it is at rounding.
- **So, with the invariant end, the frame's covariant readings are periodic along a thread's geodesic exactly at the
  thread's own line, and not at any other line.** The average of the frame over one period is then canonical (it does
  not depend on where the period starts). The extension condition that fixed the line's order and eigenline (B1914) is
  the same condition that makes the read-out as a thread average well defined.

## 2. What this means, and what it does not

- **It makes the thread average a definite candidate** for P-776's read-out, in place of a chosen point of τ: each
  thread, read at its own line, gives frame outputs averaged over its own closed geodesic, with no point of the modulus
  chosen and B1920's arithmetic supplying the channel weights' line part. Whether the read-out on the whole IS such an
  average (and how the threads of the weave are combined) is a condition to be written before anything is computed.
- **It removes no input yet:** the end L̃ is still free, the hand (decision 1) and the weight are still open, and
  only the golden thread was tested. S* is not periodic, so the reading of the Higgs matters (B1724).
- Only deviations were computed. No output of the frame is read out here.

## 1a. Seen first

`VERDICT topic-sweep /periodic along|thread average|own line|extension condition|read.out.{0,10}average/: 11 of 1661 arcs
on main match (PROVED 11); 9 register rows match (DONE 4, QUEUED 5)`. B1724 (the frame's covariance and its transport
rules), B1867 § 4 and B1914 (the extension condition), B1921 (the invariant end), B1920 (the channel weights'
average), P-776, P-717 (an apex read-out, which this does not use). **Literature:** none.

## Files

- `verification/periodic.py` → `periodic.json`, `periodic_run.txt`.
- The lock: `verification/test_b1922_periodic.py`.
