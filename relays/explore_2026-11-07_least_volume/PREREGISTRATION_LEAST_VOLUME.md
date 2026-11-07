# THE LEAST-VOLUME DEPARTURE — pre-registration (the explore seat, 2026-11-07)

**For:** the owner's test (2026-11-07, "lets do the test"): is the departure's length forced, with no data and no
choice? On the record (P-717, S305v, P-724), least action among departures invisible to the last finite rung selects the
single run of 6 uniquely, post hoc, under a two-dimensional action: the excess hyperbolic length of the history's closed
geodesic. This check asks whether that selection survives the object's own three-dimensional action.

**Kind:** data-free. SnapPy volumes of once-punctured-torus bundles and SL(2, ℤ) arithmetic mod 5 only: no frame value,
no data, no held-out quantity. The six are not a criterion (P-708).
**Written before** `least_volume_check.py` is run. Its output is committed unread, then read.

## Why volume

- Volume is Mostow-rigid: it is fixed by the topology, so it carries no metric choice. Of the object's invariants, it is
  the one most canonically called its action. Hyperbolic volume is, for instance, the on-shell action of the 3D
  hyperbolic saddle, up to sign and normalisation.
- It discriminates where length cannot. The single run of 6 and the cluster (2, 2, 2) have equal traces at every k: they
  are conjugate by C = I + LR, det 5 (the web seat's least_action_posthoc_rung.py, part 5). So length ties them, and only
  their class mod 5 separates them. They are different 3-manifolds, and volume can separate them.
- Seen first: volume was used only as a weight on a sum over depths (P-476: vol(LᵃR) rises to the Whitehead link's
  3.66386, so e^(−Vol/π) does not suppress deep runs). It was never used as the selector among departures. Swept
  2026-11-07: "excess volume", "least volume", "volume … departure" over main's docs and the web seat's departure relays.

## Definitions (identical to the web seat's; its modules are copied here, pinned at ecda7de70)

- **A defect** S = (r₁, …, r_m) replaces m consecutive golden runs, starting with an L-run at a period boundary. Its
  first and last runs are ≥ 2.
- **The range:** m ≤ 6 with runs ≤ 6; m = 7, 8 with runs ≤ 3 (`least_action_check.space()`).
- **The closed word:** W_{S,k} = L^{r₁} R^{r₂} ⋯ · X · (LR)^k, with X = R for odd m and X = I for even m. Its manifold is
  SnapPy's `b++` + W, the orientable bundle with monodromy +W. Control: `b++LR` is m004.
- **The golden comparison** G_{S,k} has the same number of runs, all golden: (LR)^{k + ⌈m/2⌉}, of volume
  (k + ⌈m/2⌉)·Vol(m004).
- **Excess volume:** ΔV(S) = lim_k [Vol(W_{S,k}) − (k + ⌈m/2⌉)·Vol(m004)]. It is evaluated at k = 10, with k = 8 and
  12 as a convergence check on the reported leaders.
- **Classes mod 5** (`least_action_posthoc_rung.klass`):
  - **rung-invisible:** E = D_S D_g⁻¹ ≡ ±I mod 5 (class 0);
  - **line-invisible (L):** E ≡ ±(LR)^a mod 5, a = 0..4 (any class).

## Controls (each must pass, or the run is reported as failed)

- **C1:** `b++LR` identifies as m004, volume 2.02988321282.
- **C2:** Vol((LR)^k) = k·Vol(m004) for k = 2..6, to 1e-9.
- **C3:** every word's solution is "all tetrahedra positively oriented". Any other is counted, reported and excluded.
- **C4:** the single runs n = 2..16 — ΔV at k = 8, 10, 12 (convergence), and whether ΔV(n) rises with n (reported).
- **C5:** the length tie (6) against (2, 2, 2) reproduced (equal traces), and both volumes' ΔV reported.

## The hypotheses, before computing

- **HV1:** among rung-invisible defects in the range, the least excess volume belongs to the single run of 6,
  uniquely: the next is above it by more than 1e-6.
- **HV2 (a question, no stated expectation):** among line-invisible defects, which has the least excess volume? Compare
  it with the least excess length, (2, 1, 1, 1, 2) (the web seat's least_action_check, H False).
- **HV3 (depth sensitivity):** among rung-invisible single runs n = 6, 11, 16, report the gaps of ΔV. If
  ΔV(11) − ΔV(6) < 0.05·ΔV(6), volume barely distinguishes depth (saturation).

**My prior:** HV1 about even odds.
- For it: volume saturates along a run (P-476), which favours one long run over several syllables.
- Against it: a short cluster may add less volume per syllable than a run of 6 adds over a golden run.

## What follows either way

- **If HV1 holds:** the record's selection of the run of 6 holds under both of the object's canonical actions, the 2D
  length and the 3D volume. The choice of action is not a hidden joint for "one departure". The selection stays
  conditional on two things, the premise that the departure is invisible to the last finite rung and the apex read-out,
  and neither is touched here.
- **If HV1 fails:** the selected departure depends on the action. The action becomes a borrowed joint for "one
  departure", and the test's answer is that the departure's length is not forced by least action alone.

**Reported only, never a criterion:** the highest apex of the least-volume defect's closed approximant at k = 20, with the
web seat's `highest_cf`.

0 of 19.
