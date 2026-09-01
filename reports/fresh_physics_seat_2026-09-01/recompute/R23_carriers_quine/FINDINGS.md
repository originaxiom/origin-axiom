# R23 — B1186: the 2√3i cusp-shape carriers and the quine

**Verdict: MATCH** (all three sub-claims; one convention note, one vacuity note on the
banked *instrument*, neither changing the verdict).

## What I read before computing (blind-first log)

`frontier/B1186_family_is_112/FINDINGS.md` lines 1–60 only. Extracted claims:

1. Family = all members of `snappy.OrientableCuspedCensus` (212,641; any cusp count) whose
   tetrahedron shapes all lie in ℚ(√−3), shape-denominator bound 256. Banked |𝓕| = 112.
2. Exactly six members other than m004 carry cusp shape 2√3i:
   t12840, o9_41001, o9_41009, o10_150684, o10_150685, o10_150693.
3. Quine (exact banked wording): "zero collisions — no member other than m004 is
   simultaneously 1-cusped, at m004's volume, with cusp shape 2√3i. (The two 1-cusped
   carriers o9_41001/o9_41009 sit at 4× volume; t06829 at 3× volume is 2-cusped.)"

I did NOT open `verification/`, `b1186_results.json`, or the addenda until after my own
sweep and carrier/quine scripts had run.

## Own computation

- `r23_sweep.py` — full census sweep (own code, 4 procs, 3m00s): double-precision
  prefilter Re z, Im z/√3 ∈ ℚ with `limit_denominator(256)` and tol 1e-9 on every
  tetrahedron shape. Result: **112 candidates, 0 errors** → `sweep_candidates.json`.
- `r23_carriers.py` — for each candidate: 220-bit shapes re-fitted to ℚ(√−3) at 1e-40
  (**112/112 confirmed**; max denominator 98, only t06829 > 49 — matches the banked
  boundary member); volume ratio to m004 at 220 bits; every cusp's shape
  (`high_precision().cusp_info()['shape']`, i.e. snappy's longitude/meridian modulus)
  **SL(2,ℤ)-reduced** to |Re τ| ≤ ½, |τ| ≥ 1, then compared to 2√3i at 1e-30.
  Output `carriers_quine.json`.

### (i) Family count
My count = **112**, and after unblinding the name set is identical to
`verification/family_census.json: members_B` (symmetric difference ∅).

### (ii) Carriers
Reduced cusp shape 2√3i occurs on exactly **7** members (cusp index in brackets):
m004[0], t12840[1], o9_41001[0], o9_41009[0], o10_150684[1], o10_150685[2], o10_150693[0].
Excluding m004: **six**, name-for-name the banked six. Volumes: t12840, o9_41001,
o9_41009 at 4×Vol(m004); o10_150684/85/93 at 5×. Cusp counts: o9_41001, o9_41009
are 1-cusped; t12840, o10_150684, o10_150693 2-cusped; o10_150685 3-cusped — so in the
multi-cusped carriers only one cusp carries the shape.

**Planted-positive control**: m004's own raw cusp shape is −1.5e−64 + 3.46410161513775i
= 2√3i to 220 bits; it is detected by the same filter. m003 (the other 1-cusped member at
Vol(m004)) has cusp shape ½ + (√3/2)i and is correctly *not* a carrier.

Normalisation note: mirror-reversal τ ↦ −τ̄ fixes 2√3i, and 2√3i is already in the
SL(2,ℤ) fundamental domain, so orbit vs raw make no difference here — indeed for all 112
members every raw snappy cusp shape was already reduced (0 of the cusps moved under
reduction). The banked instrument compares the *raw* `cusp_info` shape (double precision,
tol 1e-6, no reduction); that is a weaker convention than mine but gives the same answer.
Not a discrepancy.

### (iii) Quine
Fingerprint (1-cusped) ∧ (Vol = Vol(m004), 220-bit ratio integer 1) ∧ (a cusp with reduced
shape 2√3i), run over the 112: hits = **['m004'] only** → zero collisions. MATCH.

Non-vacuity of the shape leg: the sub-fingerprint (1-cusped ∧ Vol(m004)) alone returns
{m003, m004} — a collision — so the cusp-shape term is load-bearing.

**Planted-positive control for the zero-collision statement**: a randomised
re-triangulation of m004 injected under the alias `PLANT` (1 cusp, ratio 1.0, reduced
τ = 2√3i) is flagged as a collision by the same fingerprint → the check can fail.

## Diff against the arc's verification (read after)

`verification/family_census.py` lines 87–107: same census, same membership test
(limit_denominator 256), carriers by raw `cusp_info` shape within 1e-6 of 2√3i, quine by
`nc==1 and |vol − 2.029883212819| < 1e-6 and shape match`, `name != 'm004'`.
`family_census.json`: `carriers_2sqrt3i_excl_m004` = the same six; `quine_collisions = []`.
All numbers agree.

Vacuity remark on the banked quine check (does not affect verdict): the arc's quine
filter was run only over the 112 family members, and its own carrier list already shows
the two 1-cusped carriers are at 4× volume, so the loop could only ever return ∅ given the
carrier table — but the claim as worded is *scoped to the family*, and the family-scoped
statement is exactly what I recomputed, with a plant showing the filter itself is live.

Gate 5: no measured SM values used; the one hard-coded constant in the banked script is
Vol(m004) = 2.0298832128… (a mathematical constant), which I replaced by a 220-bit ratio.

## Artifacts (all under this cell dir)
- `r23_sweep.py`, `sweep_candidates.json` (112 names)
- `r23_carriers.py`, `carriers_quine.json` (per-member volume ratio, cusp shapes raw and
  reduced, carrier flags, quine hits)

## ADDENDUM (2026-09-01, later the same day) — claims (i) and (ii) made exact by R29

`../R29_interval_hyperbolicity/` certifies (Krawczyk, 300-bit intervals) the complete hyperbolic structure
on all 112 members and then shows the 1e-40 fits above are **exact**: the ℚ(√−3) candidates satisfy every
gluing equation exactly and lie inside the uniqueness box (distance ≤ 3.9e-58). The cusp moduli of all 183
cusps are then computed exactly over ℚ(√−3) (Neumann–Zagier derivative), agree strictly with snappy's
`cusp_info` shapes, and after exact SL(2,ℤ) reduction equal 2√3i on exactly the seven cusps listed in (ii).
The 220-bit volume ratios in (iii) remain numerical.
