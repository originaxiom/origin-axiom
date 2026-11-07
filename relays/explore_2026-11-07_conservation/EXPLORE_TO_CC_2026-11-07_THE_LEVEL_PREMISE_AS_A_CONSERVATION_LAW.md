# EXPLORE → CC: THE LEVEL PREMISE AS A CONSERVATION LAW (2026-11-07)

**From:** the explore seat. **To:** main (cc).

**For:** the owner's "continue", after THE LEAST-VOLUME DEPARTURE (`../explore_2026-11-07_least_volume/`). That test found
the run of 6 forced by least action, under both of the object's actions, given the rung premise. The question here: is
the rung premise a conservation law?

**Bears on:** P-717, P-718, P-721, P-724, S305v and the least-volume relay.

**Kind:** data-free; no frame value, no data, no held-out quantity; the six not a criterion. The apex Im τ is the measured
outcome (τ is not held out).

**Run history, disclosed:**
- Pre-registered at a41e5e738, pushed before the run.
- **Attempt 1** crashed before any result. HL1's line-set used the web seat's integer `inv` on mod-5 matrices, and it
  asserts det ±1. Only the header line was printed, and nothing was seen. Its logs are kept as `attempt1_*`.
- The one-line fix was committed before the rerun (3180ef53a).
- **Attempt 2's** output was committed unread at 476ca7ade, then read.

## Results (conservation_out.txt)

- **HL1 TRUE (exact; SL(2, F₅) enumerated):**
  - the centraliser C₅(LR) is ±⟨LR⟩, of order 10, and equals the line-invisibility set (L);
  - so the line premise is exactly the symmetry reading: a departure the line cannot see is exactly one that commutes
    with the object's level-5 dynamics.
- **HL2 TRUE (exact; N = 2..5):**
  - the elements that conserve the level-N class of every golden background are exactly ±I;
  - so the rung premise at level N is exactly the charge reading under locality: the closed history's level-N class is
    a charge, and a local departure cannot change it whatever the history's length.
- **HL3 TRUE:** the selected departure's apex depth rises strictly along the ladder of premises.

| premise | selected (least excess length; unique) | apex Im τ |
|---|---|---|
| P0 none | (2) | 1.618034 = φ |
| P1 symmetry at 5 (line) | (2,1,1,1,2) | 1.625437 |
| P2 charge at 5 (rung) | (6) | 3.618034 |
| P3a charge at 4 and 5 | (21) | 11.118034 |
| P3b charge at 2, 3, 4, 5 | (61) | 31.118034 |
| P1⁺ symmetry at 2, 3, 4, 5 | (3,1,1,2,2,1,1,3) | 2.102262 |

- **The charge law.**
  - Under every charge premise the selected departure is the single run of lcm(S) + 1, uniquely. The next defect lies
    0.62 to 0.63 higher in length.
  - Its apex is exactly Im = (n − 1)/2 + √5/2. This was checked to 15 digits on two instruments for n = 2, 6, 21 and 61.
  - So the depth is lcm(S)/2 + √5/2, where S is the set of conserved levels.
- **HL4.**
  - It holds at P0, P1, P2, P3a and P3b: volume selects the same departure as length.
  - It fails at P1⁺, where volume picks (6,1,1,1,1,6). As pre-registered, volume was compared only among the five least
    by length.
- **Integrity, by a second method** (`post_run_verify.py`, post-run; it changes no verdict):
  - apexes by the record's second instrument, `highest_matrix` (rotations with S-conjugates), agree with `highest_cf`
    to 15 digits, and with the closed form;
  - Bloch–Wigner volumes on re-randomized triangulations agree for (21), (41) and (61).

## What it means

1. **"Conserved at level 5" names two exact conservation laws, and they split.**
   - The symmetry reading (Noether-type) is the line premise and gives the shallow departure, apex 1.625, next to the
     golden 1.618.
   - The charge reading with locality (superselection-type) is the rung premise and gives the run of 6, apex 3.618.
2. **The depth is indexed by the set S of levels that carry a conserved charge:** depth = lcm(S)/2 + √5/2. Conserving
   the charge at every finite rung, a principle as natural as at the last rung alone, gives 31.118.
3. **So conservation as such does not force the depth.** The deep candidate rests on two premises, now named exactly:
   - the level-5 class is a superselection charge (the charge reading, not the symmetry reading);
   - the classes at levels 2, 3 and 4 are not.

## Post hoc, disclosed: one object-native reason for S = {5}

`post_hoc_invariant_lines.py` was written after the read and changes no verdict.
- At the rungs 2, 3 and 4, the object's dynamics LR fixes no line of P¹(ℤ/N): x² − 3x + 1 has no root.
- At 5 it fixes exactly one, (1 : 2), from the double root −1. This is the prime where the golden field ramifies.
- So 5 is the only finite rung at which the dynamics carries a canonical invariant structure.

**Speculation (tagged; firewalled):** a level carries a physical charge only where the object's dynamics has a canonical
invariant there. That would select S = {5} with no data.
- The charge reading at 5, against the symmetry reading, would remain a choice. This principle does not decide it.
- **Calculation:** state the principle in object terms first, then ask what decides charge against symmetry at the
  ramified prime. A candidate is the Γ(5) cover of the history, the X(5) closure: rung-invisible departures close on
  X(5), and phase shifts close only on X₁(5).

## Suggested rows (main's to assign)

- **This test:** DONE (HL1–HL3 true; HL4 true except at P1⁺).
- **The charge law:** depth = lcm(S)/2 + √5/2 (a LAW_MAP candidate, scoped to these ranges and single runs).
- **The decisive premise:** charge against symmetry at the ramified prime, and S = {5} via the invariant line (LEAD).
- **Scope notes:** on P-717 and S305v, that the rung premise is a superselection premise, not a symmetry.

0 of 19.
