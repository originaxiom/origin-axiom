# B1845 — the object's own line, and the excursion read out (P-717, P-718, P-455; data-free exploration)

*Main, 2026-11-06, toward the owner's goal ("Find a process in the object that places τ, the line and an energy scale, so
we stop choosing them"). Exploration tier, labelled. Every number below is computed by a script in `verification/`, with
its committed output. No measured number is read by any script. 0 of 19.*

## 1. Level 5 is the object's own

- LR = [[1,1],[1,2]] has trace 3 and discriminant 3² − 4 = 5.
- Mod 5, LR ≡ −(unipotent): (LR + I)² ≡ 0, and LR^k ≡ ±I mod 5 iff 5 ∣ k, so LR has order 5 in A₅ = PSL(2, 𝔽₅).
- The ladder's end (Γ/⟨⟨T⁵⟩⟩ ≅ A₅, GENESIS v1.57) and the monodromy's ramified prime are the same 5.

## 2. The line is the object's own level-5 eigenline (P-718)

- **What RL fixes.** By B1733's rule, the Smith invariants of RL − I and RL + I are 1 and 5 (`own_lines_run.txt`). So RL
  fixes exactly the order-5 lines (1/5, 2/5) and (2/5, 4/5) up to sign: the two points of its unique eigenline in
  (ℤ/5)². LR fixes (1/5, 3/5) and (2/5, 1/5).
- **The line classes are X₁(5)'s cusps.** The 12 order-5 lines form 4 T-classes, of sizes 1, 1, 5 and 5, which are
  X₁(5)'s cusp widths.
- **The diamond ⟨2⟩, which swaps an eigenline's two points, is not a frame symmetry at fixed τ.** The sealed features at
  the two points differ by 2 to 6 in ln ratio, under every sector permutation and reading swap (`diamond_run.txt`).
- **So at a placed τ, the 266 lines become 4:** the eigenline's two points, times the orientation RL or LR (the record's
  chirality bit).
- **POST HOC:** B1841's best line, (2/5, 4/5), is RL's own fixed line. The thread rule predates B1841 (B1733, B1734).

## 3. The excursion (P-717, a firewalled candidate)

- **The apexes converge.** The closed threads L⁵R(LR)^k have highest apexes converging to Im 2 + √5/2: the gap shrinks by
  φ⁻⁴ per golden period, and Re τ = ½ exactly at every k (`approximants_run.txt`). Two methods agree to 10⁻¹²: the
  matrix orbit with S-conjugates, and the continued-fraction Lagrange formula.
- **The line is inherited.** In apex coordinates, L⁵R(LR)^k fixes RL's eigenline iff k ≡ 0 mod 5, and is then ≡ ±RL
  mod 5 (`compat_run.txt`). The family L⁵R(LR)^{5m} carries RL's own (Re τ, line) pair, lifted toward
  τ* = ½ + (2 + √5/2)i.

## 4. The read-out: the period average washes out the hierarchy (P-455)

- **What was computed.** Along one period of the k = 5 thread's axis (translation length 13.600), each of 41 points was
  reduced to the fundamental domain by T and S with the line carried. The frame's per-sector ratios were computed at E4
  (`period_average.py`, `period_N41.json`).

| sector, reading | ln ratios at the apex | arclength mean of the ln ratios |
|---|---|---|
| up, S | −5.11, −5.52 | −1.01, −2.96 |
| up, S̃ | −5.99, −12.55 | −1.40, −3.90 |
| down, S (= lepton, S) | −4.35, −7.36 | −1.14, −3.10 |
| down, S̃ (= lepton, S̃) | −4.41, −10.95 | −1.29, −3.61 |

- Only 14.9 % of the period's arclength lies above Im τ = 2: exactly 2·acosh(h/2)/ℓ, with h the apex height. The loop average sits near the golden loop's mild values. [Review 76, corrected: the 41-point sample read 7/41 = 17 %; the exact fraction is 14.9 %. The conclusion is unchanged.]
- **So the hierarchy exists only when the frame is read at a point near the apex.** P-717's apex read-out is
  load-bearing.
- Deriving it — for example the zero modes' localization along the circle — needs a kinetic structure on the circle.
  The record has none (FL-05; B6: the lift is a choice).

## Reading

- **The line is placed by the object, up to the hand and one binary choice.** That is a reduction from 266 to 4, and its
  ground is B1733's theorem applied to the object's own monodromy at its own prime.
- **τ is not placed.** The candidate excursion gives an exact point, but only with two choices still borrowed: one
  excursion, and the read-out at its apex. The natural loop read-out gives no hierarchy.
- **The scale:** see P-719 (a dimensionless ratio not excluded; a level principle missing).

## Seen first

- **Swept:** `VERDICT topic-sweep /golden geodesic|axis of LR|monodromy axis|Teichm.ller geodesic|√5/2|Hurwitz|Markov|lowest geodesic/ (full text): 85 of 1589 arcs on main match`; `VERDICT topic-sweep /homoclinic|single departure|excursion into the cusp|run of five|departure/ (full text)`; `VERDICT topic-sweep /X_?1\(5\)|Gamma_?1\(5\)|X\(5\)|LR mod 5|Rogers.Ramanujan/ (full text): 3 of 1589 arcs`; the register for P-465, P-455, P-373, P-597.
- **Read:**
  - B1733 and B1734, the thread rule and the thread's own lines;
  - P-465, the golden ground path;
  - B1629, which shows nothing the principle forces visits the cusp;
  - B1749's referee, which withdrew the apex rule as a selector;
  - P-455;
  - B1696, B1702 and B1791 (Im τ's closed routes).
- **The literature:**
  - the cusps of Γ₁(N) as ±T-orbits on primitive N-torsion (classical: Shimura; Diamond–Shurman);
  - Γ(N) as the normal closure of T^N for N ≤ 5 (classical);
  - the Lagrange-spectrum apex formula (Cusick–Flahive);
  - Lévy's constant (Lévy 1936) for the Farey clock.

## Disclosed

- **The 5 was first noticed in the data** (P-373's firewalled lead).
- **Main compared τ* with the six's strip while reasoning.** Main also printed the frame's ratios at τ* while timing
  § 4's instrument; both are logged in LOOK_LEDGER. So the six cannot validate P-717.
- **The first approximant control omitted the S-conjugates** and returned the golden apex. The second method caught it
  (E52).
- **§ 4 uses B1842's draft instrument, which is unrun on any held-out quantity.** It computes no held-out quantity here:
  only within-sector ratios.
