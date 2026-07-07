# B460 — Relation R1: the child's own dynamics — the spectrum table + the per-vacuum CS (the live cell, fired)

**Status: banked (frontier). Firewalled. Prereg: PREREGISTRATION.md (PR #607, before
computation). The live cell produced genuinely new numbers under a two-gate-validated method;
adjudication: forced/laundered pending the Kirk–Klassen lit-gate (named); no H1.**

## Cell 1 — the length spectrum (the table cell, pre-forced, as labeled)

| manifold | shortest geodesics (len, torsion, mult) |
|---|---|
| **4₁(5,1)** (the child) | 0.5780824355 (+2.1324), 0.7215683663 (−1.1512), 0.8894429972 (+2.9419, ×2), 0.9983251885 (−2.9210, ×2), 1.0403151251 (+0.9824) |
| 4₁(7,1) | 0.3566450336 (−0.8044), 0.8578129477 (+2.0059), … |
| Weeks (arithmetic control) | 0.5846036850 (+2.4954, ×3), 0.7941346630 (−2.3049, ×3), … (the ×3 systematics = its symmetry group) |
| m007(3,1) (generic control) | ±torsion pairs (its symmetry); note 1.3169578969 with torsion exactly π |

Class-forced as pre-registered; the table banks as data. Novelty: NOT claimed (blocking
lit-gate — Chinburg-era Meyerhoff literature — pending; the earlier covers lit-gate found no
cover-homology tables but did not sweep geodesic tables).

## Cell 2 — the per-vacuum CS (LIVE; the method and the numbers)

**Method:** Kirk–Klassen path integral I = ∫(l dm − m dl) along the parent's A-polynomial curve
from the complete structure to each solution of the (p,1)-filling equation; CS = Re(I)/2π²
mod 1; **multi-path consistency binding** (5 detour classes must agree).
**GATES BOTH FIRED:** (5,1) geometric → CS = +0.0770380 = the banked ±0.07703818 (B434) with
voldrop 1.04851 = Vol(4₁) − Vol(child) exactly; **(7,1) independent validation → CS =
+0.0606170 = SnapPy's 0.0606168663** with voldrop 0.56611 = the exact volume difference. The
multi-path pass also CAUGHT a genuine branch slip (one SU(2) value corrected −0.107 → −0.34077)
— the discipline earning its keep.

**The child's per-vacuum CS values (the new numbers):**

| vacuum (meridian trace t) | type | CS (mod 1) | voldrop check |
|---|---|---|---|
| t = 1.788105 − 0.401358i | geometric | **+0.0770380** (= banked) | 1.04851 ✓ |
| t = −0.905166 | irreducible **SU(2)** | **−0.4415870** | −Vol(4₁) exactly ✓ |
| t = +0.328956 | irreducible **SU(2)** | **−0.3407670** | −Vol(4₁) exactly ✓ |
| t = −2 (reducible) | abelian branch | +0.3000000 — **flagged, not banked** (the endpoint does not satisfy the odd-filling condition on the abelian branch; needs the classical abelian-CS closed form as its own gate) |
| conjugate/complex non-geometric paths | — | **path-class boundary** (all detours in one homotopy class; the mirror values are ±-forced by the banked B289 sign law, not needed from the integral) |

Control (7,1): its SU(2) vacua give −0.1923890 and −0.2493530 — **different values, slope-
dependent as expected**; the per-vacuum-CS register behaves like every other: real structure,
object(-and-slope)-specific labels.

## Adjudication

The two SU(2) numbers are genuinely new in-repo. **Lit-gate (named, pending): Kirk–Klassen's
own papers computed CS of flat SU(2) connections on figure-eight surgeries — these exact values
may be published; no novelty claimed until swept.** Launder status: the values live on the
banked A-polynomial curve's arithmetic (the quartic's real points); a closed-form F was not
attempted this session (burden-inversion clock starts if anyone reads them as physics).
The Chat-1 premise corrections carried (the mirror pair, the B289 sign law, B443's framing).

## Reproduce
```
python3 length_spectrum.py     # cell 1
python3 pervacuum_cs2.py       # cell 2: gates -> multi-path pass (~10 min)
pytest ../../tests/test_b460.py
```
