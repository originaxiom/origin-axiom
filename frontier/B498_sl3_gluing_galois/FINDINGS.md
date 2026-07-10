# B498 — Gate A class 2d: **SEALED** — the SL(3) gluing class is mirror-organized end to end: a ℚ-rational atlas of three 2-planes, the ψ-swapped filling pair (k = ±3, sum 0; c = 1 = (−1)^{n−1} at 50 digits on BOTH members), Galois-paired point data over {ℚ(√−3), ℚ(√−7)}, and the exact transverse torsion −84 = (−3)·28

**Status: banked (frontier), Closure Campaign Phase 2, class 2d (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum SEALED / COUNTEREXAMPLE /
TOOL-BLOCKED). Verdict: SEALED — at the computable horizon; the class beyond these components
remains open (C-guardrail). Firewalled; nothing to `CLAIMS.md`.**

Gate A (S032-A) asks whether any invariant of the single seed is (1) trace-map-invariant,
(2) discretely multivalued, (3) unsymmetrizable — a forced choice. This probe assembles the
**SL(3) gluing/character-variety invariant class of 4₁ computable in-sandbox** — the component
atlas (B71/P24, reused via importlib), the degree=rank scalars (B106/B108/B153), the Sym²
geometric content (B129/K012), the boundary-unipotent Ptolemy fields (B444), and a
component-level torsion-type invariant (the B98/B495 transverse-Jacobian convention, new at
SL(3)) — and runs the B330 three-condition test. Tier honesty throughout: **exact** (sympy
symbolic, no floats in the claim), **computer-assisted-exact** (50-digit mpmath at exact
rational points — the B71 "exact-grade" convention), **certified-numerical** (double-precision
medians on the fsolve pipeline, controls only).

## 0. Controls (prereg: fail ⇒ INVALID; all PASS)

- **B71/P24 reproduced with a complete exact case split** (tier: exact; B71's probe code loaded
  via importlib, its equations re-derived): four of the eight `Fix(T₁²)` equations are literally
  linear (`x3=x2, x8=x5, x6=x4, x7=x1`); in the four free coordinates the ideal contains
  `(x1−x4)(x2−1)` and `(x1−x4)(x5−1)`, and: case `x1≠x4` ⇒ `x2=x5=1` (all generators vanish
  identically there) = **W2**; case `x1=x4` ⇒ every generator is a rational multiple of
  `(x1−1)(x2−x5)` ⇒ `x2=x5` = **V0** or `x1=x4=1` = **W1**. So `Fix(T₁²) = V0 ∪ W1 ∪ W2`,
  three **linear 2-planes**: exactly **three irreducible components, each dim 2**, irredundant
  (witness points), each parametrization T₁²-fixed. ✓
- **Sym² shadow** (B67→B71 chain): `Sym²` of the SL(2) family lands on V0, max dev 1.1e−14
  (certified-numerical; upgraded to an exact identity in §2). ✓
- **A-variety relations** (B71 scalar-matrix criterion, V46/V47): `[A,B]·μ⁻³` scalar on W1
  (`M³=L`), `[A,B]·μ³` scalar on W2 (`M³L=1`), medians 4.4e−10 / 1.1e−09. ✓

## 1. The inversion involution ψ — the atlas is a mirror system (tier: exact)

ψ: `a↦b, b↦a⁻¹` acts on the 8 fiber trace coordinates as the permutation
`(x2,x4,x6,x5,x1,x8,x3,x7)`. Computed exactly:

- **ψ⁴ = id and ψ² = θ**, the B108 contragredient/opposition involution at character level
  (`x1↔x4, x2↔x5, x3↔x8, x6↔x7`) — the atlas carries a **ℤ/4** whose square is θ.
- **ψ∘T₁²∘ψ⁻¹ = T₁⁻²** (polynomial identity, all 8 coordinates) ⇒ ψ preserves
  `Fix(T₁²) = Fix(T₁⁻²)`; abelianized, `[[0,−1],[1,0]]` conjugates the monodromy `[[2,1],[1,1]]`
  to its **inverse** — monodromy reversal, i.e. the **mirror move** (B318/B348 landing in the
  gluing class).
- **Component action**: ψ(V0(p,q)) = V0(q,p) (fixed, parameters swapped); **ψ(W1(p,q)) =
  W2(q,p)** and ψ(W2) = W1 — the two Dehn-filling-type components are a **mirror pair** (Falbel
  D2/D3 = the ±3 fillings; the mirror swaps the slope sign). θ fixes V0 **pointwise** (V0 is
  exactly the contragredient-fixed 2-plane through the atlas).

## 2. The invariant table (the class, assembled; tiers labeled)

| invariant | value | tier | B330 bin |
|---|---|---|---|
| component count; dims | 3; (2,2,2) | exact | F (canonical integers) |
| component definition fields | ℚ, ℚ, ℚ (rational 2-planes) | exact | F |
| the component pair {W1, W2} | ψ-orbit; V0 intrinsically distinguished (Sym²) | exact | P |
| A-variety exponents k | +3 (W1), −3 (W2) — B106 D4 convention | c-a-exact (50-digit) | P (sum 0, product −9) |
| degree=rank scalars c | **1 and 1** — worst \|c−1\| = 1.8e−50 at 3 exact rational points; **W2 new at this tier** via the ψ-image realization (A′,B′) = (B, A⁻¹) of B71's ℚ(i) W1 realization | computer-assisted-exact | F (= (−1)^{n−1}, B153/B83; θ-fixed since c²=1, B108) |
| geometric pair on V0 | (p,q) = ((1+3√−3)/2, (1−3√−3)/2); q = p̄ | exact | G (σ₃ **= ψ\|V0**; e-syms 1, 7) |
| Ptolemy N=3, class 0 | degree **6**; eliminant `(c−1)(4c²−c+4)` (B444's sage output **reproduced bit-for-bit in-sandbox**, sympy Groebner, saturated); fields **ℚ(√−3) ∪ ℚ(√−7)** | exact | G/F |
| Ptolemy N=3, class 1 | degree **2**; **ℚ(√−3) only** (the PGL(3)-only pair — **new beyond B444**, which solved class 0 only) | exact | G/F |
| τ functions (transverse-Jacobian reg-at-1) | τ_V0 = −4(p−1)(q−1)(pq−4); τ_W = −3(p−q)² — **identical charpoly on W1/W2** (ψ at Jacobian level), θ-invariant | exact | C (continuous, B130 pattern) |
| τ_V0(geometric pair) | **−84 = (−3)·28**, equal at both Galois lifts | exact | F (total Galois collapse) |
| transverse multipliers at the geometric pair | char = (t−1)²·(t²−5t+1)·(t⁴−9t³+44t²−9t+1); u-form: **{5} ∪ roots of u²−9u+42, disc −87** | exact | G (e-syms 9, 42) |

The Sym² leg is made **exact at trace level** (upgrading B71's 1e−14 numerics to an identity):
`tr Sym² = tr²−1` and Fricke `tr(A⁻¹B) = trA·trB − trAB` give, on the SL(2) fixed curve
`y = z = x/(x−1)` (where `w = xy−z = x` exactly), **Sym²(SL(2) fixed curve) = V0(p = x²−1,
q = y²−1)** as an 8-coordinate identity. At the geometric anchor `x²−3x+3 = 0` (B98/B495) the
V0 coordinates are the σ₃-conjugate pair with **sum 1, product 7** — and since ψ|V0 swaps p↔q,
**the object's own mirror move acts on the geometric pair as the Galois conjugation** (the B318
"conjugation IS the amphichiral involution" pattern at SL(3)). The B129/K012 knot-side rep
cross-checks exactly (traces 3, 3, ½−3√3⁄2·i, 9⁄2+5√3⁄2·i all in ℚ(√−3); generated algebra =
M₃, rank 9 — irreducible-but-arithmetically-SL(2), as banked).

The transverse-Jacobian leg **closes B495 §5's named "time-boxed out" item** (the 8-coordinate
symbolic SL(3) trace-map Jacobian): the quadratic block `t²−5t+1` (u = pq−2 = 5) is the Sym²
shadow of the SL(2) multiplier (B98's c(x_geo) = 5; B495's quadratic, disc 21); the quartic is
palindromic with `u²−9u+42` (disc −87 = −3·29) — **the exact form of B99's numerical spectrum
{5, 4.5±4.664i}**; and reg-at-1 factors as −84 = (−3)·N(u−2), with (−3) the banked SL(2)
geometric torsion. The (t−1)-multiplicity is exactly 2 on every component — an independent
exact certificate of the three dim-2 tangents, consistent with B106's banked (1,1,6) signature.
(Decorative, no forcing claimed per the B444 Inversion-Law caution: −84 = −4·3·7 carries the
Eisenstein 3 and the 7 that is both N(p_geo) and the √−7 discriminant prime; ℚ(√−87) is a new
multiplier field but arrives as a symmetrized Galois pair.)

## 3. The three-condition test (the seal)

1. **Trace-map-invariant** ✓ — every value is cut intrinsically from `Fix(T₁²)`: the components
   themselves, their peripheral relations (conjugation-invariant eigenvalue data; the
   meridian↔longitude naming transpose is a convention, B71, and the ψ-swap statement is
   convention-independent), the Sym²/geometric stratum, boundary-unipotency, the Jacobian at
   fixed points.
2. **Discretely multivalued** ✓ — the G/P rows are finite orbits with more than one member:
   k ∈ {+3,−3}, the W-pair, the geometric pair, the Ptolemy root pairs, the multiplier pair.
3. **Symmetrizable** ✓ — exhaustive bin classification, every symmetrizer computed:
   - **bin F (forced/canonical)**: counts (3; 2,2,2; 6; 2), ℚ-definition fields, c = {1,1}
     (equal, rational, the rank-parity value (−1)^{n−1}), τ_V0(geo) = −84 (rational at both
     lifts), the eliminant polynomials (already in ℚ[x] — the value-level **total Galois
     collapse**, the B495 pattern);
   - **bin G (Galois orbits)**: the geometric pair (σ₃, e-syms 1, 7), the Ptolemy root pairs
     (σ₃, σ₇), the multiplier pair (σ₈₇, e-syms 9, 42) — symmetric functions rational, the
     B330 mechanism verbatim;
   - **bin P (mirror pairs)**: {W1, W2} and k = {+3, −3} (sum 0) — swapped by the object's
     **own** inversion involution ψ; selecting a member = selecting an orientation/slope sign =
     **external label** (the B432/B496 bin-P pattern, now at the component level);
   - **bin C (continuous)**: τ_V0, τ_W as functions — fail clause (2) (B130 pattern), no
     discrete choice.

**No forced choice exists in this class ⇒ SEALED.** The object hands you a rational atlas,
symmetric orbits, and mirror pairs — never a member.

## 4. Honest credit split (what is new here vs banked)

**Corroborated (not new):** the three-components/dim-2 atlas (B71/P24); c = 1 on W1 at
exact-grade (B71 V47); the SL(3) traces sealed in ℚ(√−3) (B129/K012); class-0 Ptolemy fields
{ℚ(√−3), ℚ(√−7)} (B444 via sage, Falbel 2008, HMP). **New in this probe:** (i) the exact
complete case split for the decomposition; (ii) ψ as an exact ℤ/4 symmetry with ψ² = θ,
conjugating T₁² to its inverse and swapping W1↔W2 — the mirror organization of the atlas;
(iii) **c = 1 on W2 at 50 digits** (was ~3e−10, B106) via the ψ-image realization;
(iv) **Sym²→V0 as an exact identity** (was 1e−14 numerics); (v) the **class-1 Ptolemy solve**
(degree 2, Eisenstein only); (vi) B444's sage elimination **reproduced offline in sympy**
(the sage dependency removed for this control); (vii) the **exact SL(3) transverse-Jacobian
torsion class** — τ_V0, τ_W, τ_V0(geo) = −84, and the exact multiplier quartic u²−9u+42
(disc −87) behind B99's numerics — closing B495 §5's named in-sandbox item.

## 5. Honest scope (C-guardrail) — what remains out of reach

- **The exact A-variety of the geometric component V0** (Falbel et al.'s eliminated Groebner
  basis is 141 polynomials): magma/sage-scale elimination — **TOOL-BLOCKED (magma / sage;
  prereg-excluded)**. The Sym²-shadow identity is the geometric-branch check.
- **The Ptolemy → fiber-trace dictionary for the √−7 points** (their exact (p,q) coordinates on
  W1/W2; the sympy radical solve of the 9-variable triangular system did not terminate
  in-budget): **TOOL-BLOCKED (magma / sage / Ptolemy database — no network)**. The *fields* are
  exact above; only the per-point component dictionary rests on B444 (sage-exact, banked) +
  Heusener–Muñoz–Porti / Falbel (lit).
- **Adjoint (Porti-normalized) torsion at the SL(3) reps** (Fox/Wada at Ad SL(3), 8-dim, over
  number fields): cross-reference **B495 §5** — the same named block (number-field Groebner /
  magma / sage); **not repeated here**. The transverse-Jacobian half of that item is now closed
  (§2).
- **Ptolemy N ≥ 4** enumeration; the Ptolemy database cross-check (no network): **TOOL-BLOCKED**.
- The **universal** all-invariants statement stays **open**: this is "sealed at the computable
  horizon; the class beyond these components remains open," not victory-by-exhaustion.

## The fence

`probe.py` (runnable, ~9 s, tiers labeled; B71 probe/peripheral/symbolic_dehn reused via
importlib) → `b498_sl3_gluing.json`; lock `tests/test_b498_sl3_gluing_galois.py` (the exact
decomposition, the ψ identities, the Sym² identity + geometric pair, c = 1 at 40 digits on both
components, the Jacobian torsion values, the class-0 Ptolemy solve from the bundled B444
equations — offline, no snappy needed; snappy behind importorskip for the class-1/obstruction
count checks; JSON + FINDINGS integrity). Cross-refs: **B71/P24** (the control), **B106/B108**
(k, c conventions; θ), **B153** (the rank-stratification; the (−1)^{n−1} sign law), **B129/K012**
(Sym² sealed in ℚ(√−3)), **B444** (the field control; its sage step replaced), **B98/B99/B495**
(the transverse-torsion convention; the closed §5 item; the sibling class-2a seal), **B496**
(the sibling class-2b seal; the bin-P pattern), **B330** (the mechanism), **B318/B348**
(conjugation = the geometric involution), `docs/OPEN_PROBLEMS.md` Gate A. Lit: Heusener–Muñoz–
Porti arXiv:1505.04451 (the SL(3) character variety of 4₁), Falbel–Guilloux–Koseleff–Rouillier–
Thistlethwaite arXiv:1412.4711 (the A-variety relations L³=M, L³M=1), Falbel 2008 (ℚ(√−7) for
the boundary-unipotent reps), Lawton 2007 (SL(3) trace coordinates), Garoufalidis–Thurston–
Zickert (Ptolemy varieties and obstruction classes).

**Nothing to `CLAIMS.md`; firewall untouched.**
