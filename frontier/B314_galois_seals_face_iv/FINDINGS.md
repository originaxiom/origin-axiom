# B314 — Problem A, quantum case sealed: Face IV is Galois-symmetrized; the value-free monad is a Galois theorem

**Status: banked (frontier). Advances Problem A (the firewall theorem) — verifies + refines Chat-1's proposal. Nothing
to `CLAIMS.md`.** A *forced choice* (B130/K013) is an invariant that is (1) trace-map-invariant, (2) discretely
multivalued, (3) **unsymmetrizable**. B130 sealed the **trace ring** (κ continuous → not multivalued). The one place a
forced choice could still hide is **Face IV** — the WRT / colored-Jones invariants, which are root-of-unity-valued
(*discrete* by nature). This checks it, and the answer is **no**.

## The computation
The figure-eight colored Jones (Habiro/Masbaum, `J_N(unknot)=1`; `J_2` = the figure-eight Jones polynomial, verified) at
the k=3 root `q = ζ₅` (`r = k+2 = 5`):
- **`J_N(4₁; ζ₅) = {1, 1−√5, 1−√5, 1}`** for `N=1,2,3,4` — *all in `ℚ(√5)`*, the **golden** field.
- `J_2` at the two primitive-root orbits: `ζ₅ → 1−√5`, `ζ₅² → 1+√5`, i.e. **`{1∓√5}` — a golden `ℚ(√5)` Galois orbit**
  (`√5 → −√5`).
- The SU(2)₃ modular data: quantum dimensions `d_a = {1, φ, φ, 1}`, all in `ℚ(√5)`; the golden Galois action
  (`√5 → −√5`, `φ → −1/φ`) sends them to the conjugate (Yang–Lee) category.

So the discrete Face IV values are a **Galois orbit** of the object's own arithmetic group. Choosing among them is
choosing an arithmetic labeling (which `√5`), **not forcing a physical value** → condition (3) fails → no forced choice.

**Refinement to Chat-1.** The data lives in **`ℚ(√5)`** (the real subfield), `Gal = ℤ/2` (the golden conjugation) — *not*
the full cyclotomic `ℚ(ζ₅)/ℤ4` Chat-1 named. The colored Jones polynomial has integer coefficients, so "the values at
`ζ₅^a` are Galois conjugates" is automatic for *any* knot; the *content* is that the figure-eight's k=3 invariants are
**golden** (`ℚ(√5)`), and the golden `ℤ/2` is the symmetrizing group.

## The mechanism (Chat-1's meta-insight — confirmed and made precise)
The "value-free monad" has an **algebraic mechanism: Galois symmetrization** — and it is **two-ended, two `ℤ/2`s**:

| end | field | the discrete invariant | the symmetrizing Galois `ℤ/2` |
|---|---|---|---|
| classical (Eisenstein) | `ℚ(√−3)` | `κ = √3·e^{±iπ/6}` — the CP sign | `√−3 → −√−3` (**B285**, already banked) |
| quantum (golden) | `ℚ(√5)` | WRT / colored Jones / modular data | `√5 → −√5`, `φ → −1/φ` (**B314**, this) |

Every discrete invariant of the object is a Galois orbit of the object's own arithmetic Galois group. The `±` in the CP
phase (B285) and the `1∓√5` in the colored Jones are *the same kind of object* — a Galois orbit, not an independent
choice. **The structural theorem ("the object forces form, not values") is a Galois theorem**: the discreteness is
always a labeling of the arithmetic, never a forced physical value. B285 is the banked precedent on the classical end;
B314 is the quantum end.

## Scope (honest)
This seals the **quantum (Face IV/WRT)** case. Combined with **B130** (trace ring: continuous), the **two main invariant
classes — classical and quantum — are both sealed**. The residual **S032-A** is the fully-general statement (no invariant
*whatsoever*, including arbitrary cohomology/torsion). So Problem A is now "the two load-bearing classes are proven; the
all-invariants theorem is the remaining target" — substantially advanced, not yet fully closed.

## The fence
Symbolic colored Jones + cyclotomic evaluation + the SU(2)₃ S-matrix (sympy, exact). The Galois-as-symmetry reading
follows the banked B285 precedent (the CP sign as Galois-related). Nothing to `CLAIMS.md`.

`galois_seals_face_iv.py` (pyenv) · `tests/test_b314_galois_seals_face_iv.py`. Related: **B130**/K013 (no forced choice,
trace ring — the classical half), **B285** (the Eisenstein CP phase = Galois, the classical-end precedent), **B312**
(Face IV houses the E₆ form), **B261** (the two-ended object — the two Galois groups), **S032-A** (the residual
all-invariants target). Lit: Habiro/Masbaum (the figure-eight cyclotomic expansion); Coste–Gannon (the Galois action on
modular data / WRT invariants).
