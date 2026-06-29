# B292 — Which 2-manifold supplies the multiplicity? It tripartites; only the fiber is a surface

**Status: banked (frontier). A consolidating result — the computable facts are verified; the chiral 4d SM stays a
stop-gate. Nothing to `CLAIMS.md`.** Phase IV of the seam arc (wall #4). The owner's thesis names **multiplicity** as
a third source (besides the object and its interaction with the nothing). B277 fixed wall #4 (a canonical N=2 lift
exists; a chiral 4d SM is blocked by two named inputs). B292 asks, through the multiplicity lens: **which** candidate
"2-manifold / family" supplies the multiplicity?

## The three candidates and their character
| candidate | what it is | character | role |
|---|---|---|---|
| **fiber `Σ_{1,1}`** | once-punctured torus, `χ=−1`, monodromy `φ=RL` (trace 3, pseudo-Anosov) | a literal **2-(real)-manifold** (a surface) | the **class-S Riemann surface** (`class-S(A₁,Σ_{1,1}) = N=2* SU(2)`); shared by every tower member; supplies the **N=2** lift (B277) |
| **metallic tower `RᵐLᵐ`** | `m=1,2,3,…` bundles, traces `m²+2`, volumes `2.03, 3.66, 4.81, 5.57, …` | a **discrete sequence of distinct 3-manifolds**; arithmetic only `m=1` (ℚ(√−3)), `m=2` (ℚ(i)) (B125) | the **arithmetic family** |
| **filling family `(1,n)`** | closed 3-manifolds, scale ladder `2π/n` (B290) | a **discrete sequence of 3-manifolds** | the **scale family** |

## The verdict (consolidating NEGATIVE)
**Only the fiber `Σ_{1,1}` is a 2-manifold.** The tower and the fillings are families of **3-manifolds** (indexed by
a discrete integer parameter), supplying multiplicity in the **arithmetic** and **scale** senses respectively — but
**neither is a surface**, and **none supplies the `N=2 → N=1` chiral datum**. So:
- the literal "2-manifold the chiral 4d lift needs" is the **fiber `Σ_{1,1}`** (exactly B277);
- the multiplicity the owner names is **realized and tripartite** (surface / arithmetic / scale), each a different
  axis (and the *same* axes B287/B288/B290/B291 found for selection: dynamical / arithmetic / scale);
- the **chiral 4d SM stays blocked** for B277's two named reasons (it is N=2, needs an N=2→N=1 datum = wall #3; and
  the type is free = the CRUX).

## Stop-gate (surfaced, not ground)
The **chiral 4d-SM construction** itself — an exceptional/chiral 3d-3d or a 6d (1,0) / half-BPS twist on the fiber —
is **tool-gated / NEEDS-SPECIALIST** (B277/B281). B292 **consolidates the obstruction**; it does not attempt the lift.

## Where this lands
Wall #4 is unchanged in substance (B277) but **clarified through multiplicity**: the three "families" the program
carries are genuinely distinct (a surface and two 3-manifold sequences), they line up with the three selection axes,
and none is the chiral datum. The seam reframe is consistent: the structure (the surface, the families) is in the
object; the chiral *actualization* is not supplied.

## The fence
Geometry/structure, not a physics claim. The chiral 4d SM is a stop-gate. Nothing to `CLAIMS.md`.

`multiplicity_2manifold.py` (sage-python: tower distinctness + fiber-common + χ) · `verdict.py` (pyenv) ·
`tests/test_b292_multiplicity_2manifold.py`. Related: `B277` (the N=2 lift + obstruction), `B125` (tower
arithmeticity), `B290`/`B291` (the scale family), `B287` (the fiber/Sol closing), `B281` (the CRUX).
