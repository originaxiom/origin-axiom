# B1538 — THE PUNCTURE CHARACTERS: SEALED; NO OUTCOME READ. On the fibre-direction covers M_{D,w} (2 ≤ |D| ≤ 12) of m004, m003, m136 and m135, at the characters non-trivial on a puncture, does the line's interior supply reach two, and where it does, does the four's?

cc (the SM-derivation seat), 2026-10-04. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome.** It states what is sealed, what was checked before the run, and how the run will be read. The verdict, the
read-out and the surfaces come at the bank. **Price:** unchanged, 0 of 19.

## 1. What is sealed

- **The seal.** `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before
  `run.py` read any outcome. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The question** (§1 of the seal). sm:B1535's Theorem C, with Lemmas 2 and W′ (§3), puts room for g ≥ 2 generations on
  M_{D,w} only at a member ν whose ν⁴ is a puncture character with n(ν⁴) ≥ g, and where also capL2 ≥ g.
  - Part L reads the line's supply n at every puncture character of the population.
  - Part F reads the four's supplies at every member over a puncture character with n ≥ 2.
- **The population** (§5).
  - 80 covers: 5 of m004, 9 of m003, 29 of m136 and 37 of m135.
  - 2,406,622 puncture characters of order dividing m(C), in 662,988 Galois orbits.
  - Every root of unity s, found completely by route W.
- **The routes** (§4).
  - Route W: Wang, exact over cyclotomic fields (PARI).
  - Route P: the cover's own Reidemeister–Schreier presentation, over GF(p) at two primes (python-flint).
  - Route T: the transfer, from the integer homology of the cyclic cover ker χ.
  - For Part F: route R (sm:B1536's `route_r`, by path) and route P4.
- **Proposition H, the quaternion line** (§3 of the seal).
  - On every state's (ℤ/2)² cover, the order-2 character ζ_H that cuts out the Q₈ cover has the quaternions ℍ as its
    twisted fibre homology.
  - The monodromy acts there with finite order, so the line's supply sums to 4 over the roots of unity.
  - It is at most 2 at any s where the monodromy moves Q₈, and even where the monodromy fixes it.
  - P9–P11 seal it. P9 is the run's positive control inside its own population.
- **Eleven predictions with priors** (§7). The priors expect 8.23 of 11; P4–P8 were revised before the seal, with the draft's
  values shown. `read_out.py` reads them.
- **The reading rules** (§9).
  - **NEGATIVE** (scoped to the population) if P1–P3 and P9 hold and no member has min(capW, capL2) ≥ 2.
  - **PROVED** (room for two, not a count) if P1–P3 and P9 hold and such a member exists. The class readings are then a
    separately sealed arc.
  - **OPEN** while any route disagrees or P9 fails.
  - **Coverage** (the audit lane's R87): a population-wide prediction is certified only on complete records, checked
    against K11's manifest and Part F's planned readings; missing or empty records give None, never a negative.

## 2. The controls (before the seal)

K0–K12 hold (`verification/controls.json`; §6 of the seal):
- the covers against low_index (K0);
- sm:B1535 Part W's banked rows at |D| = 1 in routes P and W (K1);
- Lemma W′ at every puncture-trivial character of the population, in both routes (K2);
- b₁ = #cusps (K3);
- route T's homology against SnapPy on every cover of degree 2–6 (K4);
- the transfer on controls (K5);
- Part F's routes against sm:B1536's own pulled-back supplies at |D| = 1, with the banked members (K6);
- the Burau/Alexander identity of the figure-eight's 3-braid (K7);
- the Galois enumeration (K8);
- the read-out on synthetic rows, twenty-six cases, with the audit lane's R87 probes (K9);
- Proposition H's characters on the ten (ℤ/2)² covers, located by structure alone (K10);
- the population manifest by formula, equal to the seal's enumerated table (K11);
- Part F's fourth roots against brute force on the 40 covers with |D| ≤ 5 (K12, the audit lane's R89).

**Eight pre-seal slips**, each caught before the seal and logged in ERROR_LEDGER or disclosed in the seal's §6:
- a design-note statement about when puncture characters exist;
- two E12 module-name collisions, one with sm:B1529's `fibre_lib.py` and one with sm:B1535's `read_out.py` and
  `controls.py`;
- a read-out comprehension bug that K9 caught;
- route W read PARI's `polcyclofactors` as single cyclotomic factors; K2's crash caught it, and no root could have been lost
  silently;
- the draft's priors for P4–P6 contradicted Proposition H;
- two record-format errors in the draft verdict;
- the read-out's coverage: no expected manifest, and an empty Part F that certified P7 and P8. The audit lane's R87 found
  both at the pre-seal snapshot `27dd37e2`, and its R89 asked for a fourth-root certificate; all of it is closed.

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` ran first. Then `scripts/checks/prior_work.py` ran over every head with sixteen terms.
  No head reads the line's supply at a character of a cover that is non-trivial on a puncture. The hits that bear on this
  arc:
  - this seat's sm:B1532, sm:B1534, sm:B1535 (Theorem C, Lemma W, C3) and sm:B1536 (sealed and running; pulled-back
    characters only; its records are not read here);
  - B349's census of the figure-eight's covers through index 6;
  - the physics seat's R57, whose three half-periods are the three-puncture orbit of m004's |D| = 4 cover here;
  - the audit lane's RT6, and its R85–R89 after the sweep (R87 and R89 reviewed this arc's read-out; the others do not
    bear).
- **The literature**, read on 2026-10-04:
  - Wikipedia's "Burau representation" and "Figure-eight knot (mathematics)", for K7;
  - Putman–Wieland's Appendix A (through sm:B1536);
  - Hironaka's Theorem 4.1.1 and Leroux's abstract, for §10's question of all orders;
  - Shapiro's lemma as sm:B1532 cites it, and Gaschütz's theorem as sm:B1536's Proposition Q uses it.
- **Standing: EXTENDS.** sm:B1535's Lemma W extends to every fibre-direction cover (Lemma W′), and sm:B1515's frame is read at
  a cover's own puncture characters for the first time.

## 3. Why this document exists before the outcome

The file-drawer lock (B837) and the verdict locks require every sealed, ledgered preregistration to carry a report. A seal
commit ships its arc's findings stub with it (ERROR_LEDGER, E50 instance and recurrence). This document and the OPEN verdict
beside it make the arc's state readable now. Both are replaced at the bank.

**0 of 19 stays 0.**
