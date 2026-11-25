# B1978 — The act's eight orbits of twelve at order 30: the monodromy carries the 96 points into themselves, changes their rates, and keeps alignment and both quark hierarchies at every point; the slow 2–3 mixing lives on four of the eight orbits

**Verdict: PROVED (a reading of B1977's committed rates under the act's monodromy, no new frame computation).** Main,
2026-11-24. Data-free. Register row P-845. **0 of 19.**

*Dated caveat (2026-11-24, after landing, main's own reading).* The act acts on the modulus and the point together: it
carries E_τ to E_{Mτ}. This arc moves the point by M and holds τ fixed. So "not invariant under the object's own act" is
true at a fixed τ only. If the frame is covariant under the joint action, moving the point by M at fixed τ matches moving
τ by M⁻¹ at a fixed point, which leaves the cusp i∞ for the cusp M⁻¹(∞). The orbits, the counts and the alignment and
hierarchy at every point stand as computed. The reading "the menu is the act's orbits" needs the joint covariance checked
first: frame C's SL(2,ℤ) covariance is known for τ → τ + 1 (B1940) and is obstructed at level 5 for flat unitary
connections (agy-002's M34).

*Dated note (2026-11-25, B1979).* B1977's classes converge to 12, not 17. The act keeps the converged class at 8 of 96, as
here, and its orbits fall into two families of four, each carrying six classes.

## Seen first

- **Swept:** `VERDICT topic-sweep /orbit of the act|monodromy orbit|M-orbit|orbits of twelve|act's orbit/: 0 of 1719 arcs on main match (none); 0 register rows match (none)`.
- **The record:**
  - B1943: the act fixes the order-5 line, its only invariant line mod 5;
  - B1976 and B1977: order 30 on the act's line;
  - B1944: the average over the surface washes out the hierarchy;
  - P-845: which level the object picks.
- **The literature:** the action of a hyperbolic element of SL(2,ℤ) on torsion points (standard).

## The results (`verification/orbits.py`, `orbits_run.txt`)

- **The act moves the 6-part.** M = [[2,1],[1,1]] carries the 96 points into themselves. It keeps a point's rate class at only 8 of the 96, so the frame's readings at order 30 are not invariant under the object's own act.
- **The orbits.** M acts on the 96 points with **8 orbits, each of 12 points**. It has order 12 on them: order 3 mod 2 and order 4 mod 3, while it fixes the order-5 line.
- **Every point of every orbit is aligned** (least diagonal at least 0.9) **and hierarchical in both quark sectors**, 96 of 96.
- **The slow 2–3 mixing** (rate within 3e-3 of 1/30) **lives on 4 of the 8 orbits.** Along each orbit the least mixing rate cycles through a few rationals: 1/30, 1/10, 1/5, 0.234, 3/10, 0.368, 0.433.

## What it means

- **Alignment and hierarchy are properties of the act's orbits.** At order 30 on the act's line they hold at every point the act can reach, so they are not accidents of a chosen point.
- **The size of the mixing is not invariant under the act.** Along an orbit it changes.
- **If the object's reading is the act's orbit,** as its own symmetry suggests, the menu is the 8 orbits, not the 17 classes of B1977.
- **What stays open is how an orbit is read.** The aggregation of its 12 points has to come from the object, not be chosen: a coherent or Gramian sum, or the orbit's Hecke-like operator. B1944 warns that a naive average washes out the hierarchy.

## What is open

- **The principled reading of an orbit,** and what it gives for the masses and the mixing.
- **Whether the 4 slow orbits are singled out** by anything the object carries.
- **Level 30 itself** (P-845).
