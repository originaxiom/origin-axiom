# B495 — Gate A class 2a: **SEALED** — the adjoint-torsion class is a *total* Galois collapse: multiset {±3, ±5}, sum 0, product 15⁴, sign killed by amphichirality

**Status: banked (frontier), Closure Campaign Phase 2, class 2a (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum SEALED / COUNTEREXAMPLE /
TOOL-BLOCKED). Verdict: SEALED — at the computable horizon; the class beyond these components
remains open (C-guardrail). Firewalled; nothing to `CLAIMS.md`.**

Gate A (S032-A) asks whether any invariant of the single seed is (1) trace-map-invariant,
(2) discretely multivalued, (3) unsymmetrizable — a forced choice. This probe computes the
**adjoint Reidemeister torsion across the entire SL(2,ℂ) character variety of 4₁** — both
components, every canonical finite stratum reachable in-sandbox — with the banked methods
(B425 Fox/Wada pipeline; B98 trace-map Jacobian), assembles the value multiset, and runs the
B330 Galois-orbit test. Every claim below is **tier: exact** (sympy quadratic-field arithmetic;
no floats in any claim; cypari `algdep` was never needed — nothing is merely certified-numerical).

## 0. Controls (prereg: fail ⇒ INVALID; both PASS)

- **Geometric adjoint torsion** (B425 / V30 / V31 / B98): Fox/Wada at ρ_geo (relator forces
  v²−v+1=0, u=−v=ω, ℚ(√−3)) gives `W(t)=(t−1)(t²−5t+1)/t³`, reg-at-1 = **−3** — at *both*
  Galois lifts. ✓
- **Dynamical zeta** (B423/B425): `charpoly Sym²([[2,1],[1,1]]) = (t−1)(t²−7t+1)`, reduced
  value at t=1 = **−5** = 2−L₄. ✓
- PSL collapse: `Sym²(−M) ≡ Sym²(M)` (symbolic identity) — sign-lifts (m→−m) can never add
  values; the SL(2) lift multiplicity is invisible to the adjoint class. ✓

## 1. The atlas: X(4₁) has TWO components; the canonical strata and their values

Derived from the relator (no literature constants): Riley form `(v−1)(s²+s⁻²) + v²−3v+3 = 0`;
in character coordinates (m = tr μ, z = tr ab): **Φ(m,z) = z² − (m²+1)z + 2m² − 1**,
irreducible over ℚ, and irreducible over ℂ (double cover of the m-line with squarefree branch
divisor `disc_z Φ = (m²−1)(m²−5)` — a simple branch point forces connectivity). So
X(4₁) = [abelian line] ∪ [ONE nonabelian curve]: **all components enumerated.**

Per-point table (Wada = the B425 pipeline `det Φ(∂r/∂b)/det(Sym²ρ(a)t−I)`, reg-at-1;
Jacobian = the B98 transverse pair `τ_B(x) = 2−c(x) = −(2x²−3x+3)/(x−1)` on the pointwise-
T₁²-fixed curve V0; **the two methods agree at every stratum**):

| stratum | locus | point field | image / structure | adjoint W(t) quad (disc) | **τ** | μ-framing | tier |
|---|---|---|---|---|---|---|---|
| PC-1 geometric pair | m=±2; z²−5z+7 | ℚ(√−3) | discrete faithful (Mostow pair) | t²−5t+1 (21) | **−3** | regular (∂Φ/∂z≠0) | exact |
| PC-2 metabelian pair | m=0; z²−z−1 (z=φ) | ℚ(√5) | binary dihedral **Dic₅**, order 20 (ζ₅ on the fiber) | t²+3t+1 (**5**) | **+5** | regular | exact |
| PC-3 bifurcation pair | m=±√5; z=3 | ℚ(√5) | reducible non-semisimple (X_red∩X_irr, Burde–de Rham: Δ(s²)=0) | t²−7t+1 (45) — **the dynamical zeta polynomial** | **−5** | critical (∂Φ/∂z=0, exact) | exact |
| PC-4 branch/2T pair | m=±1; z=1 | ℚ (char); rep over ℚ(√−3) | **binary tetrahedral 2T**, order 24 — the McKay-E₆ group | t²+t+1 = Φ₃ (**−3**) | **+3** | critical (exact) | exact |

Certificates at every point: relator ρ(r)=I exact; Fox rank 2 ⇒ dim H¹ = 1; finite images by
exact closure enumeration (20, 24); x_μ-regularity by ∂Φ/∂z (nonzero at PC-1/PC-2 — the honest
Porti-normalized values; zero at PC-3/PC-4 — there the Wada number coincides, as it does
everywhere, with the transverse-Jacobian normalization). The **abelian component** carries the
continuous Δ-governed function `V_ab(s) = Δ(s²)²/(s(s²−1))²` with the classical simple
(t−1)-pole — **fails clause (2)** (B130 pattern), contributes no discrete value, and vanishes
exactly at PC-3 (the two sides of the bifurcation match).

## 2. The two banked "ends" MEET on the variety (the probe's one new structural fact)

B425 banked "two torsions = two ends": geometric −3 (Eisenstein) vs dynamical −5 (golden).
This probe finds the dynamical end **inside the character variety**: the adjoint Wada output at
the Burde–de Rham bifurcation rep (the reducible limit of the nonabelian curve, m=±√5) is
literally `(t−1)(t²−7t+1)/t³` — **the dynamical zeta polynomial, value −5**, i.e. the trivial-
fiber-character end x=2 of the single function τ_B on V0. One rational function carries all four
strata values: {x_geo: −3, x_meta: +5, x=0 (2T): +3, x=2 (trivial): −5}, and its **zero locus is
the seam quadratic** 2x²−3x+3 (disc **−15**). The κ_V0=∓2 strata factor as
`x²(x²−3x+3)` and `(x−2)²(x²+x−1)` — Eisenstein side and golden side, exactly.

## 3. The three-condition test (the seal)

Multiset over the canonical strata (PSL points): **{−3, −3, +3, +3, +5, +5, −5, −5}**.

1. **Trace-map-invariant** ✓ — every stratum lies on the pointwise-T₁²-fixed curve V0 and is
   cut by intrinsic conditions (meridian-parabolic; traceless meridian; component intersection;
   branch locus). Presentation gauge: `W_∂a/W_∂b = −1`, *constant* across all strata (computed),
   and the sign-symmetric multiset is invariant under it.
2. **Discretely multivalued** ✓ — four distinct values {−5, −3, +3, +5}, finite.
3. **Symmetrizable** ✓ — **total Galois collapse**: every value is already RATIONAL (in the
   fixed field — stronger than the B314/B318 pair-symmetrization, where an irrational orbit
   still had to be symmetrized). σ₃: √−3→−√−3 swaps the PC-1 members (and the PC-4 rep lifts) —
   values fixed; σ₅: √5→−√5 swaps the PC-2 members and the PC-3 members — values fixed; complex
   conjugation = the amphichiral involution (SnapPy: symmetry group D4, amphicheiral True; B318/
   B348) — all values real. Symmetric functions: **sum = 0** (the orientation-sign content comes
   in ± pairs — B348's "amphichirality kills the sign" landing in the torsion class),
   **product = 15⁴** (the seam 15 = 3·5; μ-framed sub-multiset product 15²).

**No forced choice exists in this class ⇒ SEALED.** The object hands you a sign-symmetric,
seam-normed, rational multiset — never a member.

## 4. Ptolemy cross-check (N=2, exact, offline)

SnapPy's two obstruction-class Ptolemy varieties for 4₁ at N=2, solved exactly (sympy Groebner
with nonzero-coordinate saturation, no magma/sage/network): class 0 **EMPTY**; class 1 cut by
**c²−c+1 = 0** — the Eisenstein quadratic = the geometric pair, nothing else. No unreached
boundary-unipotent points hide at N=2.

## 5. Honest scope (C-guardrail) — what remains out of reach

- **SL(n≥3)/E₆ adjoint & Ptolemy N≥3 values:** B99's transverse spectrum at Sym²ρ_geo is
  numerical `{5, 4.5±4.664i}`; the exact tier needs the 8-coordinate symbolic SL(3) Jacobian
  (in-sandbox-feasible in principle, time-boxed out of this probe). Exact *enumeration* of
  Ptolemy N≥3 solution sets: **TOOL-BLOCKED (magma/sage, or the Ptolemy database — no network)**.
- **CS/η beyond CS=0** — phase 2b, not this probe. **Extended-Bloch/K₃^ind** — phase 2e.
- The **universal** all-invariants statement stays **open**: this is "sealed at the computable
  horizon; the class beyond these components remains open," not victory-by-exhaustion.

## The fence

`probe.py` (runnable, ~7s, tiers labeled) → `b495_adjoint_torsion.json`;
lock `tests/test_b495_adjoint_torsion_galois.py` (controls −3/−5, the multiset and its Galois
closure, curve anchors, method agreement; SnapPy behind importorskip). All sympy-exact; SnapPy
used only for the Ptolemy equations + amphichirality (optional). Cross-refs: **B425** (method +
the two-torsions correction), **B98/B99** (τ₁=−3 at ρ_geo; the Jacobian formula), **B330**
(the mechanism), **B348** (the sign-kill pattern), **B318** (amphichiral firewall), **V30/V31**
(Porti −3), **OPEN_PROBLEMS.md** Gate A. Lit: Riley (parabolic reps of 2-bridge knots), Burde /
de Rham (bifurcation at Δ roots), Wada (twisted Alexander invariants), Porti (torsion de
Reidemeister pour les variétés hyperboliques), Dubois–Yamaguchi (adjoint twisted Alexander),
Daly arXiv:2411.04431 (monodromy tangent action, cited).

**Nothing to `CLAIMS.md`; firewall untouched.**
