# THE LEVEL PREMISE AS A CONSERVATION LAW — pre-registration (the explore seat, 2026-11-07)

**For:** the owner's "continue" (2026-11-07), after THE LEAST-VOLUME DEPARTURE (`../explore_2026-11-07_least_volume/`).

That test found the following:
- least action selects the single run of 6 under both of the object's actions, the 2D excess length and the 3D excess
  volume;
- it does so given the rung premise, that the departure is invisible to the last finite rung, E ≡ ±I mod 5;
- under the weaker line premise, E ≡ ±(LR)^a mod 5, it selects the shallow (2,1,1,1,2).

**The question here:** is the rung premise a conservation law, the history's class at level 5 conserved like a discrete
charge? And how does the departure's depth depend on which conservation law is imposed?

**Kind:** data-free; SL(2, ℤ/N) arithmetic, geodesic lengths, SnapPy volumes and continued-fraction apexes only; no frame
value, no data, no held-out quantity; the six not a criterion (P-708). The apex depth Im τ is the measured outcome. τ is
not a held-out target.
**Written before** `conservation_check.py` is run. Its output is committed unread, then read.

## Seen first (swept 2026-11-07 over main's docs and the web seat's departure relays)

**On record:**
- (2,1,1,1,2) is a level-5 golden phase shift, E = LR (HARVEST_LEDGER row 1587);
- "the stabiliser of ±v is ⟨±LR⟩ mod 5" (the web seat's post hoc rung script);
- level 5 is the object's own (P-721, P-718);
- Γ(5) = ⟨⟨T⁵⟩⟩, the last finite rung (P-717).

**Not found:**
- line-invisibility as commuting with the object's level-5 dynamics;
- rung-invisibility as a conserved level-5 charge under locality;
- the ladder of conservation premises across the rungs 2–5 with the depth each selects.

## Definitions

- **Defects, closed words, E, and the two actions (ΔS, ΔV)** are the web seat's and the least-volume test's, with the
  modules pinned at ecda7de70. E = D_S D_g⁻¹. The actions are evaluated in the k → ∞ limit at k = 20 (length) and k = 10
  (volume), so a defect's cost is a local quantity, independent of the background's length.
- **The rungs:** N = 2, 3, 4, 5. PSL(2, ℤ)/⟨⟨T^N⟩⟩ is S₃, A₄, S₄, A₅, and N = 5 is the last for which ⟨⟨T^N⟩⟩ = Γ(N)
  has finite index.
- **The symmetry reading at level N:** E mod N commutes with LR mod N (E ∈ C_N(LR)).
- **The charge reading at level N, with locality:**
  - the closed history's level-N class is the conjugacy class of its monodromy in SL(2, ℤ/N), up to sign;
  - a local departure conserves it if, for every golden background W = (LR)^j (every length), E·W lies in the class
    of ±W.
- **The premises compared** (each restricts which defects count as invisible):
  - **P0** none;
  - **P1** symmetry at 5;
  - **P1⁺** symmetry at 2, 3, 4, 5;
  - **P2** charge at 5;
  - **P3a** charge at 4 and 5;
  - **P3b** charge at 2, 3, 4, 5.
- **Ranges:**
  - R1 is the web seat's;
  - R2 extends it: m ≤ 3 with runs ≤ 64, m = 4 with runs ≤ 24, m = 5 with runs ≤ 10, first and last runs ≥ 2.
- **Per premise:**
  - the defect of least excess length in R1 ∪ R2, and whether it is unique;
  - the excess volume of the five least by length, and whether volume selects the same one;
  - the selected defect's highest apex Im τ on its closed approximant (k = 20, the web seat's `highest_cf`).

## Hypotheses, before computing

- **HL1 (exact):** C₅(LR) = ±⟨LR⟩ mod 5, of order 10. It equals the line-invisibility set (L), so the line premise is
  exactly the symmetry reading at level 5.
- **HL2 (exact):** for N = 2, 3, 4, 5, the elements of SL(2, ℤ/N) that conserve the level-N class of every golden
  background are exactly ±I. So the rung premise at level N is exactly the charge reading with locality.
  - Expected by the background W ≡ I alone, so this is a consistency check.
- **HL3:** the selected departure's apex depth rises strictly along P0 → P1 → P2 → P3a → P3b under length, and P2 selects
  (6).
- **HL4:** at every premise, excess volume selects the same departure as excess length, among the five least by length.

**Priors:** HL1 and HL2 are near certain, being algebra. HL3 is likely, since stronger invisibility admits fewer and
longer departures. HL4 is likely, after the least-volume test.

## What follows either way

- **If HL1–HL3 hold,** "conservation at level 5" names two different laws:
  - the symmetry (Noether-type) reading gives the line premise and the shallow departure;
  - the charge (superselection-type) reading with locality gives the rung premise and the run of 6.
  - Conserving the charge at every finite rung, which is as natural, gives a deeper departure still.
  - So the depth is not forced by conservation as such. It is indexed by which level structure is conserved. The deep
    candidate rests on one precise premise: the level-5 charge, and only it, is a superselection label.
- **If HL3 fails,** the departure is reported where the depth stops rising.
- **Any result** is a statement about premises, never about the 19.

0 of 19.
