# EXPLORE → CC: THE LEAST-VOLUME DEPARTURE (2026-11-07)

**From:** the explore seat. **To:** main (cc).

**For:** the owner's test (2026-11-07, "lets do the test"): is the departure's length forced, with no data and no choice?

**Bears on:** P-717, S305v, P-724, P-476, P-714 and P-729.

**Kind:** data-free; no frame value, no data, no held-out quantity; the six not a criterion (P-708).
- Pre-registered at f18de4351, pushed before the run.
- Output committed unread at 7a6b56843, then read.
- The web seat's modules were reused unchanged, pinned at ecda7de70.

## The question

Least action among departures invisible to the last finite rung selects the single run of 6 (S305v; post hoc). That
was under a two-dimensional action, the excess geodesic length.

Does the selection survive the object's own three-dimensional action, the Mostow-rigid excess volume of each departure's
mapping torus?

Seen first: volume was used only as a weight on depth sums (P-476), never as the selector.

## Results (least_volume_out.txt)

- **Controls pass (C1–C5):**
  - `b++LR` is m004, with volume 2.029883212819;
  - the cyclic covers carry k·Vol(m004);
  - 42 768 defects, 643 of them rung-invisible;
  - no non-geometric solution;
  - convergence |ΔV(k = 12) − ΔV(k = 10)| ≤ 3.3e-8;
  - ΔV(n) rises with n on 2..16.
- **HV1 TRUE.** Among the 643 rung-invisible defects, the least excess volume belongs to the single run of 6, uniquely.
  - ΔV(6) = 1.5714462325.
  - Next come (5,1,1,1,1,2) and its mirror (2,1,1,1,1,5), at 2.1955011599.
  - The gap is 0.6241, which is 40% of ΔV(6). Under length the same pair's gap is 0.4450, which is 19%.
  - So volume selects (6) more decisively than length does.
- **HV2.** Among the line-invisible defects the least excess volume is (2,1,1,1,2), the same defect as the least excess
  length.
- **HV3: not saturated at the 5% screen.**
  - ΔV(11) − ΔV(6) is 11.7% of ΔV(6), and ΔV(16) − ΔV(11) is 3.3% of it.
  - Excess length grows by 45% over the same step.
- **C5.** The length tie of (6) with (2,2,2) is broken by volume: 1.5714 against 2.3592. The two have equal traces at
  every k, being conjugate by I + LR, of det 5.
- **Reported only:** the apex of (6)'s closed approximant has Im 3.618033989 and Re 0, which is i√5·φ, P-717's reading
  (ii).
- **Integrity: a second method.** `post_run_verify.py` was written after the read and changes no verdict.
  - Method: a re-randomized triangulation, with the volume summed independently as the Bloch–Wigner dilogarithm in
    mpmath at 60 digits.
  - It agrees with the run to ≤ 4.4e-15 for m004, (6), (5,1,1,1,1,2) and (2,2,2).
  - The gap by this method is 0.62405492744.

## What it changes

**The action is not a hidden joint for "one departure".** The object's two canonical actions, the 2D excess length and
the 3D excess volume, select the same departure in both classes: (6) among the rung-invisible defects and (2,1,1,1,2)
among the line-invisible ones.

## What it does not change: the depth's remaining choices

1. **The class premise.** Rung-invisible (E ≡ ±I mod 5) against line-invisible (E ≡ ±(LR)^a) decides deep against
   shallow: apex Im 3.618 against about 1.63 (the record's figure for (2,1,1,1,2)). It is now the single most
   consequential choice for the depth.
2. **Minimization against a sum.**
   - ΔV on the rung-invisible single runs n ≡ 1 mod 5 rises but stays bounded. The bound is P-476's Whitehead limit.
   - So Σ e^(−ΔV/ħ) over those runs diverges for every ħ > 0.
   - The least-volume departure is therefore a minimizer, never the dominant term of a volume-weighted sum. This agrees
     with P-476, and with P-724 under length (B).
3. **The rest, untouched:** the read-out at the apex, the premise that the history departs at all, and the hand (P-717,
   B1846, P-720).

**The test's answer:** the departure's length is not forced yet. Least action forces it, robustly across the object's two
actions, given the rung premise and minimization.

## Speculation (tagged; firewalled)

Is the rung premise a level-5 superselection rule? That is: is the history's class in PSL(2, F₅) = A₅ conserved like a
discrete charge, so that a departure must be invisible to it?

**Calculation:**
1. State the conservation in object terms: a ℤ/5 or A₅ holonomy of the mapping torus, through its Γ(5) cover.
2. Check whether it forbids the line-invisible phase shifts E ≡ ±(LR)^a with a ≠ 0.

The check is data-free and is stated here before any value.

## Suggested rows (numbers main's to assign)

- **The least-volume test:** DONE; HV1 true; the action is not a joint.
- **The rung premise's derivation:** LEAD, as the depth's decisive choice.
- **Dated notes:** the sum's divergence under volume, on P-724 and P-476.

0 of 19.
