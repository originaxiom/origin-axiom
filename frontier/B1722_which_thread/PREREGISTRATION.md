# B1722 — PREREGISTRATION: WHICH THREAD? (the completion map's C2, P-285) — does a thread drawn from the record's own measure fit the six charged-fermion ratios better than it fits random hierarchies?

cc (main), 2026-10-22, after B1720. **Sealed before `verification/which_thread.py` runs.** A test of a structure, not a
value derived. 0 of 19.

## Why

B1720 put τ and the line on a thread and found the frame's closest approach. With no continuous number free, the thread
L⁵RLR² puts all six ratios within 1.80. But some thread in the census matches 1.65% of random hierarchies as well, so
which thread remains a choice. The record holds two measures over threads, each fixed without reference to the data:
- **μ_U, the weave's uniform word measure** (B1629). A primitive class of length n carries its n rotations, each of
  weight 2⁻ⁿ.
- **μ_A, the action weight at L154's c = 6.** By B1088, S = −Vol·σ and c = 6σ, so the weight is e^{−c·Vol/6π} = e^{−Vol/π},
  with Vol the hyperbolic volume of the class's once-punctured torus bundle.

GENESIS v1.53 records that a selection may select a measure, tested statistically (FK9). This is that test.

## The model and the statistic (no new mass computation)

- **The rows** are B1720's stored output: 121 classes and 3 249 lines, both horocycles, three up readings. The output's
  sha256 is pinned in the instrument.
- **For a target t** (the six ratios), f_k(t) is class k's best worst factor over its rows.
- **The statistic** is the measure-weighted mean log-misfit of a thread drawn from μ, E_μ(t) = Σ_k μ(k) ln f_k(t). There is
  no threshold: B1720's best factor has been seen, and a threshold such as "within 2" would be tuned to it.

## Cells

| cell | prediction | prior |
|---|---|---|
| **W1, the uniform measure** | at most 1% of 4 000 random hierarchical targets (B1695's prior, seed 1722) have E_{μ_U} ≤ E_{μ_U}(data) | 5% |
| **W2, the action weight** | the same with μ_A | 5% |

Read-outs:
- P_μ(f ≤ F) for F = 1.5, 2 and 3, under each measure;
- the classes that carry most of each measure;
- the best class's volume and its weight under each measure.

**The reading, written before the run.**
- **If W1 or W2 holds,** the record's own measure, with the thread, selects the data's neighbourhood specifically. That is
  the first selection on record that is not a choice. It is graded a READING with its tags (Λ, the unit, H-cov, the
  canonical end, the measure's c = 6 for μ_A), and attacked first by an independent route.
- **If both fail,** the record's measures do not select the data's thread. Both favour short threads, whose apexes sit
  too low for a hierarchy. Then the selection needs a measure not on record, or a principle beyond the measure (P-139).

## Seen first

`VERDICT topic-sweep /measure over threads|uniform measure|action weight|c ?= ?6|root share|which thread|thread weight/ (full text, aliases: the weave's measure): 33 of 1493 arcs on main match (NEGATIVE 5, OPEN 4, PROVED 24)`. Bearing on it:
- B1629, the uniform measure's run statistics;
- B1088 and B1015, L154's c = 6σ;
- the web seat's root-share check, where the weights favour the root;
- B1720, the census and its best class.

**Literature:** none beyond the record.

## Disclosed

- **Known before the seal:** B1720's full read-out, including the best class L⁵RLR², its factor 1.80, the per-class
  bests and the calibration (1.65%).
- **The measures are the record's, not chosen here,** and both are reported. c = 6 is L154's.
- **Expected direction, stated before the run:** both measures put most of their weight on short threads, so they are
  expected to fail. The test is run because the expectation is not a result.
- The instrument was import-tested before the seal; importing computes nothing.
- It reads B1720's committed output, pinned by its full sha256.
