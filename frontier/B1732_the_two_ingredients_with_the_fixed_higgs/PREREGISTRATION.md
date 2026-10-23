# B1732 — PREREGISTRATION: THE TWO INGREDIENTS WITH THE HIGGS PF1-W FIXES (P-307) — with F₆ = η⁻³(θ₂⁶, θ₄⁶, iθ₃⁶) in place of ∂R, on B1726's 23 940 points, do the six charged-fermion ratios still come out specifically?

cc (main), 2026-10-23, after B1730 and B1731. **Sealed before `verification/census.py` and `verification/compare.py`
run.** A test of a structure with two ingredients put in by hand and a Higgs fixed by a reading of a principle, not a
value derived. 0 of 19.

## Why

B1726 replicated the two-ingredient result on fresh points: with the Georgi–Jarlskog factor 3 on the leptons and the
covariant readings, the six ratios are specific (0.12% of random hierarchies as good under the seat's menu, 0.41% under
every covariant reading assignment). Its Higgs was ∂R, which no principle on record selects (H-cov, P-115). B1730
showed that under PF1-W read on the Higgs no untwisted Higgs, ∂R included, is zero-free; every zero-free Higgs is a theta
power F_a. B1731 showed that exactly one of them, F₆, also has a zero-free invariant, the Higgs's factor of det Y in
B1656's frame. So PF1-W read on both the Higgs and the determinant fixes the Higgs to F₆ (a necessary condition; whether
the record adopts that reading is the owner's call, P-303). **The question: does the two-ingredient result survive
when the Higgs is the one this reading fixes, instead of the one chosen by hand?**

## The model (no data)

- **The frame,** exactly as B1726: B1656's four-channel coupling, B1667's canonical end at both horocycles with L read
  at Im τ from its Re τ = ¼ column; B1713's 266 lines of order 1–12 up to sign.
- **The Higgs:** S = v_iQ_I + v_jQ_J + v_kQ_K with v the direction of F₆ at τ, (θ₂⁶, θ₄⁶, iθ₃⁶). F₆'s scalar η⁻³ and
  its twist χ_η¹² (SL(2, ℤ)'s sign character) multiply the coupling by a scalar and a global phase, which change no
  ratio, ∣V∣ or J.
- **The rows:** B1726's points, Re τ ∈ {0.05, 0.2, 0.35, 0.55, 0.7, 0.85} × Im τ ∈ {2.05, …, 3.45}: 23 940 points,
  47 880 rows. No F₆ row has been compared with data.
- **The readings:** S and S̃ (B1724); every sector in both, and the CKM for each (up, down) pair.
- **The menus, as B1726:** seat {(S̃, S, S), (S̃, S̃, S̃)} × c ∈ {1, 3}; cov (all 8 assignments) × c ∈ {1, 3}; free (the
  seat's two rules, c continuous).
- **The measure and the calibration:** main's (B1695's random hierarchies, B1713's random mixings). Each cell is the
  mean over 20 fresh seeds, 1732–1751, 4 000 targets each.

## Cells

| cell | prediction | prior |
|---|---|---|
| **R1** | under the seat's menu, the best row puts all six ratios within a factor 2 | 35% |
| **R2, specific** | under the seat's menu, the mean fraction of random hierarchies as good is at most 1% | 20% |
| **R3, specific** | under the covariant menu, at most 1% | 12% |
| **R4, specific** | with the lepton factor free, at most 1% | 15% |
| **R5, specific** | the nine (six and ∣V_us∣, ∣V_cb∣, ∣V_ub∣) under the seat's menu: at most 1% | 8% |
| **R6, unfitted** | at the best nine-row (seat's menu), ∣J∣ within a factor 3 of PDG's 3.08 × 10⁻⁵ | 5% |
| **R7, unfitted** | at the best six-row (seat's menu), P-094's D within 3σ of 10.58 ± 0.11 | 2% |
| **C1, control** | (i) the instrument with the Higgs switched to ∂R reproduces B1725's verified census at its best point on every shared key to 10⁻⁹ in log; (ii) T-covariance with F₆, both readings, at 0.35 + 2.75i on two lines, to 10⁻⁶; (iii) the instrument's F₆ obeys v·v = −3(θ₂θ₃θ₄)⁴ to 10⁻¹⁰ | 95% |

Read-outs: the best six and nine rows under each menu (line, τ, horocycle, readings, factor, D, J); the per-seed
fractions.

**The reading, written before the run.**
- **R2 holds** (and R3): the two-ingredient result survives with the Higgs PF1-W fixes in both readings. The frame then
  has one hand choice fewer, H-cov's direction replaced by a reading of a principle (conditional on P-303). The factor
  (P-294) and the reading (P-295) remain.
- **R1 holds, R2 fails:** F₆ fits but not specifically; the specificity was ∂R's.
- **R1 fails:** F₆ does not carry the hierarchy in B1656's frame. Then PF1-W in both readings and the frame's fit are
  incompatible, and one of them must change: the reading of PF1-W, the frame, or the Higgs's end data.
- **R5–R7:** as in B1726.
- **C1 failing** stops the reading.

## Seen first

`VERDICT topic-sweep /F_?6|F₆|theta.?6|θ₂⁶|zero-free Higgs|PF1-W|invariant has no zero|Higgs PF1|fixed Higgs|two.ingredient/ (full text): 56 of 1503 arcs on main match (NEGATIVE 8, OPEN 2, PROVED 46)`;
most matches use "two-ingredient" or "F6" in other senses.

Bearing on it:
- B1726 (the design, and the ∂R rows at these very points);
- B1730 (the zero-free lines);
- B1731 (F₆'s selection);
- B1724 (the readings' covariance);
- B1700 (∂R; members not dominated by the v₊ line carry no hierarchy in the older frame's census formula);
- B1727 (a flavour-blind Higgs gives none);
- B1695 and B1713 (the priors).

None puts F₆ in the frame against data. **Literature:** Georgi and Jarlskog (1979); Antusch, Hinze and Saad (P-094);
theta functions; standard.

## Disclosed

- **Known before the seal:**
  - B1726 in full, on the same points with ∂R;
  - B1730 and B1731;
  - two data-free audit-room looks, neither comparing any F₆ value with data:
    - the R-Higgs (F₂) against ∂R. A 400-point run crashed before writing any output; four seeded points were then
      printed (m₂/m₃ tracked ∂R's, m₁ ≡ 0).
    - B1731's count of non-zero first generations with F₆ (43 of 48 seeded sectors; only the count was read).
- **The web seat's zero-free census** (HARVEST_LEDGER row 1317; its scripts at d6c6021d2, 0b2dca3a8) puts the ten
  one-unit lines, F₆ among them, in main's B1720 frame against the data. Its results are not recorded on its branch at
  the seal and have not been read; main will not read them before this test's outputs are committed.
- **Expected direction, stated before the run:** below B1726's. F₆ is dominated at the cusp by the N eigenline (line
  orders (1, −1, −5)), while ∂R is dominated by v₊ (orders (1, −1, 3)).
- **The trial count:** this is the twenty-third sealed test of this frame against data.
- **The run's size:** as B1726's (about 3 h 15 min on 8 workers, checkpointed), the calibration about 20 minutes.
- The instruments were import-tested before the seal; importing them computes nothing.

## Instruments

- `verification/census.py` (no data) → `census.jsonl`, `control.json`.
- `verification/compare.py` → `comparison.json`.
- The hashes are in `ARTIFACT_HASHES.txt`: the two instruments relative to this arc, and the files they read in place
  relative to the root (as B1726's).
