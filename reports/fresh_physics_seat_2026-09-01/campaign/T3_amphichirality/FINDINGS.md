# CELL T3 — AMPHICHIRALITY AT THEOREM STRENGTH: PASS (with one honest edge banked as a conjecture, not a claim)

Outside evaluation seat, campaign cell T3, 2026-09-01.
Deliverables in this directory: `THEOREM.md` (Thm A + Cor B at publication care),
`sweep_t3.py` (+ `results.json`), `scan_quarter.py` (+ `scan_quarter_results.json`).
Nothing outside this directory was modified. Gate 5: no measured Standard Model value
appears in any computation below; this cell is pure 3-manifold topology.

## Verdict: PASS

- **Theorem A proved** (THEOREM.md §2): the orientation double cover of any
  non-orientable finite-volume hyperbolic 3-manifold is amphichiral, the mirror
  self-isometry being the deck involution. The orientation-reversal of the deck map is
  proved by descent (an invariant orientation would descend to orient the
  non-orientable base), not asserted; Mostow enters only to make the statement
  metric-independent. This upgrades 02_A6_VERDICT.md item (4) from [argued] to [proved].
- **Corollary B proved** (THEOREM.md §3): any mirror-odd isometry invariant of an
  amphichiral manifold is 2-torsion in its value group — `{0, 1/4}` in `R/(1/2)Z` (CS),
  exactly `0` in torsion-free groups. Matches B1224/B1227; chained a priori to covers.
- **Sweep clean**: 40/40 covers amphichiral (certified full symmetry groups),
  40/40 CS on the 2-torsion set, max deviation **1.19e-64** (tolerance was 1e-9;
  quad-double left ~55 orders of margin).
- **Bite control bites**: 15/15 certified-chiral controls are OFF the set;
  minimum distance **1.346e-2** (m016), median 5.8e-2, i.e. the nearest chiral control
  is **1.3e+7 x tolerance** away. The sweep is informative; not DEGRADED.

## Conventions (E23 discipline — stated, not assumed)

1. **Amphichiral** = admits an orientation-reversing self-isometry; equals the
   self-homeomorphism notion by Mostow (THEOREM.md §1).
2. **CS normalization**: SnapPy `chern_simons()`, real, defined mod 1/2, mirror-odd.
   Anchors re-verified in this run: CS(m004) = -1.2e-65 ≡ 0, CS(m003) = 0.25 exactly.
3. **No sheet chosen**: no orientation of any cover is selected anywhere; every
   reported quantity (distance to the 2-torsion set, membership) is invariant under
   the sheet swap since {0, 1/4} is exactly the negation-fixed 2-torsion subgroup.
4. **Distance metric**: distance mod 1/2 to the nearest element of {0, 1/4}, computed
   as distance to the nearest integer multiple of 1/4; maximum possible = 1/8 = 0.125.
5. **Certification**: amphichiral/chiral labels only from symmetry groups with
   `is_full_group() = True` (all 40 sweep covers and all 15 controls satisfied this;
   orientable-census manifolds with uncertified groups were skipped for the control).
6. **Precision**: CS via `Manifold.high_precision()` (quad-double) throughout.

## Part A — the sweep (first 40 of NonorientableCuspedCensus)

Bases m000…m131 -> covers `m000~`…`m131~` (SnapPy `orientation_cover()`; sanity:
`m000~ ≅ m004` verified by the isometry checker; vol(cover) = 2·vol(base) throughout).

| check | result |
|---|---|
| cover orientable | 40/40 |
| amphichiral (certified full group) | **40/40** |
| CS on {0, 1/4} mod 1/2 within 1e-9 | **40/40** |
| max distance from the set | 1.19e-64 |
| value distribution | **{0: 40, 1/4: 0}** |

## Part B — the bite control (MB12), run as mandated

Criterion falsifiability, both directions, stated before reading results:
(i) a cover with CS off {0, 1/4} ⇒ COUNTEREXAMPLE refuting the seat's refinement;
(ii) chiral controls also clustering on {0, 1/4} ⇒ sweep uninformative ⇒ DEGRADED.

First 15 certified-chiral one-cusped manifolds (full symmetry group, no
orientation-reversing element):

| manifold | CS | dist to {0, 1/4} |
|---|---|---|
| m006 | -0.114137 | 0.114137 |
| m007 | -0.135863 | 0.114137 |
| m009 | -0.020833 (= -1/48) | 0.020833 |
| m010 | 0.229167 (= 11/48) | 0.020833 |
| m011 | -0.191837 | 0.058163 |
| m015 | -0.153204 | 0.096796 |
| m016 | -0.236537 | **0.013463 (min)** |
| m017 | 0.096796 | 0.096796 |
| m019 | -0.147781 | 0.102219 |
| m022 | -0.213107 | 0.036893 |
| m023 | 0.036893 | 0.036893 |
| m026 | -0.078093 | 0.078093 |
| m027 | -0.158846 | 0.091154 |
| m029 | 0.212191 | 0.037809 |
| m030 | -0.037809 | 0.037809 |

0/15 on the set at tolerance; min distance 1.346e-2 >> 1e-9. **The control bites.**
(Side observation: m009/m010 have *rational* CS (±1/48 class) yet are chiral —
rationality of CS is not the phenomenon; 2-torsion membership is.)

## The honest edge (new datum, typed): covers never take the value 1/4

The sweep's distribution is degenerate — all 40 covers sit at **0**. An extended
CS-only scan (`scan_quarter.py`; amphichirality guaranteed by Thm A) of the first
**120** orientation double covers found:

> at 0: **120/120** · at 1/4: **0** · off-lattice: 0 · max |CS| = 2.46e-64

The known 1/4-manifolds (m003, m135, m207 per B1224) are amphichiral but did not arise
as orientation covers here; checked directly that the Gieseking's cover is m004
(isometric, verified) and is **not** m003. Consequences, stated carefully:

1. **Not a counterexample** to anything banked: {0} ⊂ {0, 1/4}; Cor B is confirmed.
2. **But** the record should not cite the cover census as evidence that both 2-torsion
   values occur *for covers* — on 120/120 the bound is never tight at 1/4. B1227's
   non-vacuity witnesses (m003 etc.) live in the amphichiral class at large, outside
   the cover subclass, and that distinction is now load-bearing.
3. Banked as **Conjecture C** (THEOREM.md §3.3), not as a claim: orientation double
   covers may satisfy CS = 0 exactly, with the candidate mechanism being the *freeness*
   of the deck involution (extra structure Cor B does not use — mirror-oddness alone
   provably cannot yield more than 2-torsion). Missing datum typed in THEOREM.md §3.3.
   A single cover at 1/4 kills Conjecture C without touching Thm A / Cor B.
4. If Conjecture C is true, it *sharpens* the seat's A6 verdict: "CS(m004) = 0 is what
   the deck involution pins" would be literally right after all — the B1227 correction
   ("only {0, 1/4}") would itself need the refinement that the *free* involution of a
   covering pins the value all the way to 0, while a non-free reversing symmetry only
   pins to {0, 1/4}. Not established here; flagged for a future cell.

## Reproduction

```
python3 sweep_t3.py        # writes results.json (sweep + control + anchors)
python3 scan_quarter.py    # writes scan_quarter_results.json (120-cover scan)
```
snappy census access required. Randomness-free; symmetry groups canonical-cell
certified; CS quad-double.

## MB12 compliance statement

The verdict criterion could fail in both directions (cover off-lattice ⇒
COUNTEREXAMPLE; chiral controls on-lattice ⇒ DEGRADED). The named bite control was
actually run: 15 certified-chiral manifolds, 0/15 on-lattice, min distance 1.346e-2.
Additionally the corollary's own non-vacuity (both branch values inhabited among
amphichiral manifolds) is witnessed by m003/m135/m207 at 1/4 — while honestly noting
those witnesses are not covers (previous section).
