# B1296 — THE CHARGE-LOCUS PARITY LOCK: dropping θ-equivariance buys count 2 at the price of three closer's choices — and θ-evenness is NOT vector-likeness: the F₄ chamber is vector-like or SU(3)-anomalous, face by face

*MASTERPLAN v3 Phase 2 = Door D1. Pre-registered in `DESIGN` (T1–T5) before any computation; two of
the pre-registered expectations were wrong and the computation, not the expectation, is banked (§0).
Every number below is this bench's: the swap and level-curve tests run on B1295's own harmonic
generator (508 group moves, cutoff R = 10), the Lie-theoretic half on a standard rational
realisation of E₆ in ℝ⁸ (72 roots, 27 = W·ω₁) built here — not on the physics seat's icosian
basis. Nothing is taken from a seat by trust; fc R69/R70 are cited where they are confirmed and
corrected where they are not (§6). Date 2026-09-07.*

## The sentence

**Under θ-equivariance, a charge locus on Fix(θ) forces the Higgs direction into the θ-even Cartan
= the Cartan of F₄ = E₆^θ, and on that four-dimensional chamber every one of the 15 faces is either
vector-like or SU(3)-cubic-anomalous — never chiral and anomaly-free. The anomaly-free chiral
direction (SO(10)×U(1), two 16's, count 2) exists only on the θ-ODD walls, which parity forbids as a
charge locus; reaching it means dropping equivariance and paying three closer's choices (the locus,
the sign pair, the direction), priced here as I-27 UNEARNED. The count is 2 on every road; the
masterplan's head sentence stands, and the wall's name changes from "θ-equivariance" to "the charge
locus is unsupplied".**

## 0. What the pre-registration got wrong (and why the correction is the result)

The design expected (i) *no θ-odd ray with a q↔−q symmetric spectrum* and (ii) *θ-even ⇒ vector-like*
(fc R70's reading: "θ-even Cartan directions all give 2(R⊕R̄)"). Both failed on the screen:

- (i) **24 of the 168 odd rays are symmetric** — exactly the six *root lines* of the restricted A₂
  (§4.3), where the centraliser is D₄ ⊕ u(1)² and the 27 decomposes into self-conjugate D₄ pieces.
- (ii) **θ-even does NOT imply vector-like.** The four F₄ fundamental coweights split 2 : 2 —
  `ω₂^∨` (A₅) and `ω₁^∨+ω₆^∨` (D₄) are vector-like, `ω₄^∨` (A₂×A₁×A₂) and `ω₃^∨+ω₅^∨` (A₁×A₂×A₁) are
  **chiral** (dim 54 in the 78, 36 in the 27). What θ-evenness gives is `dim 27_q = dim 27_{−q}`
  (44/44 rays) — a **dimension** symmetry, which fc R70 read as vector-likeness. The two coincide
  only when θ acts on the centraliser by an inner automorphism (§4.2).

The first failure is bookkeeping; the second is the finding. It forced §4 — the full classification of
the F₄ chamber and the anomaly computation that turns "chiral" into "anomalous" on every chiral face.

## 1. T1 — the swap theorem: the object's equivariant smooth vacuum is θ-ODD and χ(∂⁺M) = 0 coefficient-free

**Statement.** Let σ be a strong inversion of m004 (B1294: an orientation-preserving involution whose
fixed set is two arcs; on the cusp torus `z ↦ −z`) and ω the harmonic generator of H¹(m004;ℝ)
(B1295's collocation solution, `c₍0,2₎ = −4.260982635 i`). Then `σ*ω = −ω` (B1294: Lefschetz
`L(σ) = 2 = 1 − s_μ ⇒ s_μ = −1`), hence the radial cusp component `g(z,t) = ω(∂_t)` satisfies
`g(−z, t) = −g(z, t)`, hence σ maps `∂⁺M = {g > 0}` onto `∂⁻M = {g < 0}`; when 0 is a regular value of
g on a horotorus, `χ(∂⁺M) = χ(∂⁻M)` and `χ(∂⁺M) + χ(∂⁻M) = χ(T²) = 0`, so **`χ(∂⁺M) = 0` and the
smooth-frame net chirality (B1290) vanishes without any coefficient** — B1295's `c₍±2,0₎ ≠ 0` is now
needed only for regularity (it decides that the zero set is two circles, not what the count is).

**Computation** (`swap_and_level.py`, T1). The eight elements of the cusp isometry group D₄
(identity; `z ↦ z + τ/2`; two glides; the two strong inversions σ₁, σ₂; two rotatory reflections of
order 4) all satisfy `g(m z, t) = α(m) g(z, t)` with α = the meridian sign, to relative deviation
≤ 6.8 × 10⁻¹³ on B1295's 538 half-modes; on a 60×60 grid at t = 1, `sign g(−z) = −sign g(z)` at all
3592 points off the zero set. **The object's own equivariant smooth vacuum φ = ω ⊗ u is θ-odd**
(`θ_G u = −u`) — the opposite parity from fc's singular-frame conclusion, and the first hint that the
two frames pull in opposite directions (§3 makes it a theorem).

## 2. T2 — the level-curve lemma; T4/T4b — the arcs are distinguished, not related

**Lemma.** A σ-odd 1-form annihilates `T Fix(σ)` (at p ∈ Fix(σ), `dσ_p = +1` along the arc and `−1` on
the normal plane; `ω_p ∘ dσ_p = −ω_p` kills the tangential component). So the arcs are **level curves**
of the local potential of ω and the normal components are unconstrained.

**Computation** (T2). At the eight arc endpoints (the fixed points of σ₁ and σ₂ on the cusp torus:
`0, ½, τ/2, ½+τ/2` and their τ/4-translates), at three heights: `max |g| = 1.6 × 10⁻¹³` (tangential
component vanishes, as the lemma says) while the normal components do not: `ω(∂_x) = 1.280438` on the
orbit `{0, τ/2, ½+τ/4, ½+3τ/4}` and `0.724301` on `{½, ½+τ/2, τ/4, 3τ/4}`, `ω(∂_y) = ±1.62185 /
±1.45683`. **Fix(θ) is not a zero locus of the object's Higgs, Morse–Bott or otherwise** — the
object's own field runs *across* the arcs at unit-order strength.

**T4 / T4b.** Stabilisers of the eight endpoints under the eight actions: `{2: 8}` — each endpoint is
fixed by the identity and its own strong inversion only, so no second symmetry fixes an arc pointwise.
The endpoint orbits have sizes `[4, 4]`; each arc's two endpoints lie in one orbit, **but the two arcs
of σ₁ lie in different orbits** — and the object distinguishes them numerically (`ω(∂_x) = 1.28` on
one, `0.72` on the other). Consequence: **no symmetry of the object relates the two arcs' signs; the
sign pair (ε₁, ε₂) is the closer's** — fc R69 §4's observation, now proved from the symmetry group
rather than observed from the bookkeeping. With opposite signs every net vanishes (T3, last line).

## 3. THE CHARGE-LOCUS PARITY LOCK (topological half; a theorem about involutions, not about E₆)

Let σ be an orientation-preserving involution of an oriented 3-manifold with `Fix(σ) = Δ` a union of
arcs/circles, and let the abelian Higgs be `φ = ω ⊗ u` (ω a real closed 1-form, u a Cartan direction
of the gauge algebra; the frame of B1290/fc R69). Equivariance under `θ = (σ, θ_G)` means
`σ*ω ⊗ θ_G u = ω ⊗ u`, i.e. **either `(σ*ω, θ_G u) = (+ω, +u)` or `(−ω, −u)`**.

At p ∈ Δ the differential is `dσ_p = diag(+1 | −1, −1)` (tangent | normal; orientation-preserving with a
1-dimensional fixed set forces exactly this). Hence:

- a σ-**even** covector at p is purely **tangential**; a σ-**odd** covector is purely **normal** (§2);
- a **Morse–Bott zero locus along Δ**, `ω = H_ij x_i dx_j + …` in normal coordinates (x ↦ −x, dx ↦ −dx),
  is σ-**even**; a σ-odd closed form `ω = df` with f odd (`f∘σ = −f`) has vanishing normal Hessian
  along Δ, so it admits **no** non-degenerate zero locus there, and no Morse zero on Δ either: the
  odd germ `s·(ax + by)` has Hessian rank 2 < 3 (checked symbolically, `Hessian ranks [2]`);
- a **vortex/singular locus** `q dϑ` (ϑ the angle in the normal plane, σ: ϑ ↦ ϑ + π) is σ-**even**.

**Therefore every charge locus supported on Fix(σ) is σ-even, and equivariance forces `θ_G u = +u`:
the Higgs direction lies in the θ-even Cartan, which for `θ_G` = the E₆ diagram flip is the Cartan of
`F₄ = E₆^θ`.** Conversely the object's own harmonic ω is σ-odd (§1) with non-vanishing normal
components (§2): **the object supplies no charge locus on Fix(θ) at all** — the arcs are where its
field is purely normal and non-zero. The lock has two jaws: the object's field is odd and misses the
arcs; a charge locus on the arcs must be even and lands on F₄'s Cartan. §4 computes what F₄'s Cartan
contains.

*Name.* "Parity lock" was already in the corpus in a different sense (B1149's *clock-depth-parity
lock*, `frontier/B1148_*/carrier.py`); this one is **the charge-locus parity lock**,
`T-CHARGE-LOCUS-PARITY-LOCK`.

## 4. The spectral half — THE F₄ CHAMBER: vector-like or SU(3)-anomalous, never chiral and clean

Set-up (`e6_theta_spectra.py`). E₆ realised in ℝ⁸ over ℚ (72 roots; 27 = W·ω₁, 27 weights; θ = the
diagram flip 1↔6, 3↔5, an involution of the root system with 24 fixed roots, fixed Cartan dim 4, odd
dim 2, `θ(27) = 27̄`). For a Cartan direction u the centraliser is `C = C_ss ⊕ u(1)^k`; the left-handed
content under fc R69's bookkeeping with equal arc signs (the (+,+) rule, |net| = 2 per sector) is
`2 × 78_{q>0}` for the adjoint (78 self-conjugate) and `2 × (27_{q>0} ⊕ 27_{q<0}^*)` for the 27.
**Vector-like** ⟺ the signed C_ss-weight multiset of the left-handed content is closed under negation;
`chiral dim = Σ_w max(N(w) − N(−w), 0)`. All of this is exact (Fractions).

### 4.1 The four F₄ fundamental coweights (T6)

| u | θ | C_ss | 78 | 27 |
|---|---|---|---|---|
| `ω₂^∨` | even | A₅ | VECTOR-LIKE (20 = Λ³6 self-conjugate) | VECTOR-LIKE (6̄_{±1}) |
| `ω₄^∨` | even | A₂×A₁×A₂ | **CHIRAL dim 54** | **CHIRAL dim 36** |
| `ω₁^∨+ω₆^∨` | even | D₄ | VECTOR-LIKE (8_v, 8_s, 8_c real) | VECTOR-LIKE |
| `ω₃^∨+ω₅^∨` | even | A₁×A₂×A₁ | **CHIRAL dim 54** | **CHIRAL dim 36** |
| `ω₁^∨` (mixed, θ → ω₆^∨) | — | D₅ | CHIRAL dim 32 = 2×16̄ | CHIRAL dim 32 |
| `ω₁^∨−ω₆^∨`, `ω₃^∨−ω₅^∨` (odd walls) | odd | D₅ | CHIRAL dim 32 | CHIRAL dim 32 |
| odd root lines, odd generic | odd | D₄ | VECTOR-LIKE | VECTOR-LIKE |

Rep content of the chiral even faces (`css_content.py`, Dynkin labels per factor, (A₂, A₁, A₂) order):
`ω₄^∨`: 78 → q=1 (3̄,2,3) [18], q=2 (3,1,3̄) [9], q=3 (1,2,1) [2]; 27 → (3,2,1)₁ ⊕ (1,2,3)₋₁ ⊕ (1,1,3)₂ ⊕
(3,1,1)₋₂ ⊕ (3̄,1,3̄)₀ — **trinification** with the third SU(3) broken to SU(2)×U(1)_u (compare B1098's
*trinification remnant*, where the object's holonomy eats one SU(3) instead). `ω₃^∨+ω₅^∨`: 78 → q=1
(1,3̄,2)+(2,3̄,1), q=2 (2,3,2), q=3 (2,1,1)+(1,1,2), q=4 (1,3̄,1). In both, the charged sectors at
charges q and q′ carry the SU(3) fundamental and anti-fundamental with *different* partners, so the
left-handed multiset is not closed under conjugation.

### 4.2 Why θ-even ≠ vector-like (the mechanism)

θ fixes u, so it preserves C and maps the C-module `27_q` to `27̄_q = (27_{−q})^*` **twisted by
θ|_C**. When θ|_C is inner on C_ss (A₅ and A₃: θ acts as the diagram flip = complex conjugation of
SU(n), and the pieces that occur are self-conjugate; D₄, A₁: all reps self-conjugate) this gives
`27_q ≅ 27_{−q}^*` — vector-like. When θ **swaps two factors** (the two A₂'s of `ω₄^∨`, roots {1,3} ↔
{5,6}) or fixes an A₂ **pointwise** (the {2,4} A₂ of `ω₃^∨+ω₅^∨`, on which θ is the identity, not
conjugation), the twist is outer and `27_q ≇ 27_{−q}^*`. fc R70 tested the A₅/trivial directions,
where the two notions coincide, and generalised.

### 4.3 The full chamber (T7): 15 faces, two coefficient draws each, coefficient-independent

The θ-even coweights are spanned by `ω₂^∨, ω₄^∨, ω₁^∨+ω₆^∨, ω₃^∨+ω₅^∨` — the fundamental coweights of
F₄ under the folding. A face = a non-empty subset S; its generic point has the same C_ss, chirality
and anomaly for every positive coefficient draw (asserted).

| face S | C_ss | 78 | SU(3) cubic anomaly (left-handed content) |
|---|---|---|---|
| w2 | A₅ | vector-like | 0 |
| **w4** | A₂×A₁×A₂ | **chiral 54** | **≠ 0 (both A₂)** |
| w1+w6 | D₄ | vector-like | — (no cubic invariant) |
| **w3+w5** | A₁×A₂×A₁ | **chiral 54** | **≠ 0** |
| **w2+w4** | A₂×A₂ | **chiral 18** | **≠ 0 (both A₂)** |
| w2+w1+w6 | A₃ | vector-like | 0 |
| w2+w3+w5, w4+w1+w6, w4+w3+w5 | A₁³ | vector-like | — ; Witten SU(2) parity 0 |
| **w1+w6+w3+w5** | A₂ | **chiral 6** | **≠ 0** |
| w2+w4+w1+w6, w2+w4+w3+w5 | A₁² | vector-like | — ; Witten 0 |
| w2+w1+w6+w3+w5, w4+w1+w6+w3+w5 | A₁ | vector-like | — ; Witten 0 |
| all four (interior) | abelian | vector-like | — |

**`chiral faces = cubic-anomalous faces = {w4, w3+w5, w2+w4, w1+w6+w3+w5}`** — exactly the faces whose
C_ss contains an A₂ that θ does not reverse (a swapped pair or the pointwise-fixed {2,4}); the eleven
others are vector-like and anomaly-free, with the Witten SU(2) parity 0 on every A₁ everywhere. For
contrast, the mixed `ω₁^∨` and the odd wall `ω₁^∨−ω₆^∨` (both D₅, both unreachable equivariantly by §3)
are **chiral dim 32 and cubic-anomaly-free** (D₅ has no cubic invariant): the one clean chiral
direction sits where the lock forbids the charge locus. `U(1)_u` itself is anomalous on every chiral
face (`Σq³`, `Σq` ≠ 0; the arcs end on the cusp, where such anomalies flow — "every closing removes the
arcs", fc R69), so the statement is about the non-abelian gauge factors, which is where it bites.

### 4.4 The sector table (T8): normalised anomalies, and a 1 : 3 that is recorded, not spent

Per face, per A₂ factor, the cubic anomaly of each sector normalised to the fundamental (exact and
x-independent by uniqueness of the SU(3) cubic invariant):

| face | A₂ factor | A₃(78-sector) | A₃(27-sector) | multiplicities (n₇₈ : n₂₇) cancelling all cubic anomalies |
|---|---|---|---|---|
| w4, w2+w4 | first | −3 | +1 | **1 : 3** (the only primitive solution) |
| w4, w2+w4 | second | +3 | −1 | (same) |
| w3+w5, w1+w6+w3+w5 | the {2,4} A₂ | −1 | −2 | **none** (same sign) |
| w2, w2+w1+w6 (A₅, A₃) | — | 0 | 0 | unconstrained |

On the trinification faces the 78-sector's SU(3)² anomaly is **minus three times** the 27-sector's —
the 78 ⊃ (3,3,3̄) is tri-fundamental, the 27 bi-fundamental, and the 3 is the dimension of the third
SU(3)'s fundamental. **FIREWALL.** The two sectors belong to two frames (PW's 7d adjoint vs the
heterotic-type matter 27); no frame on main contains both with free multiplicities, and the two parent
adjoints that do contain both give the wrong ratio: E₇ (133 = 78+1+27+27̄) has 27-sector multiplicity
2 (anomaly −1 ≠ 0) and E₈ (248 = (78,1)+(1,8)+(27,3)+(27̄,3̄)) multiplicity 6 (anomaly +3 ≠ 0), because
the 27̄-sector's left-handed weights coincide with the 27-sector's (checked). This is an exact
representation-theoretic fact about E₆ ⊃ SU(3)²×SU(2)×U(1) and **not** a generation count; it is
registered as a hint (H-B1296-RATIO) and nothing is built on it.

### 4.5 The θ-odd plane is the restricted A₂ of (E₆, F₄) — EIV, Helgason's table

On the odd plane `a(ω₁^∨−ω₆^∨) + b(ω₃^∨−ω₅^∨)` (168 primitive rays in [−6,6]²): the 72 roots restrict
to **6 distinct restricted roots of multiplicity 8**, cosines {±1, ±½} — the A₂ of the symmetric pair
(E₆, F₄) = the real form E₆(−26) = EIV (rank 2, restricted root system A₂, m = 8, M = Spin(8)), the
form the corpus already names as the object's spacetime form (T-SIMUL-CLOSING). Generic ray:
centraliser 30 = D₄ ⊕ u(1)² (108 rays); **walls** (kernels of the restricted roots): centraliser 46 =
D₅ ⊕ u(1), 36 rays, chiral type; **root lines**: 24 rays, D₄ ⊕ u(1)², spectrum symmetric. Weyl
conjugacy: `ω₃^∨−ω₅^∨ ∈ W·ω₁^∨` and `ω₁^∨−ω₆^∨ ∈ W·ω₆^∨` (both true; the cross pairs false) — **the
chiral SO(10) direction IS reachable inside the θ-odd plane**, on its walls, by a Weyl conjugate of the
minuscule coweight. It is reachable by the object's odd field and forbidden as a charge locus by the
lock; the even chamber is allowed as a charge locus and has no clean chiral face. That is the crux of
c vs θ (memory: *two chiralities*) stated in coweights.

## 5. T3 — the toggle: count 2, priced as I-27

With equivariance dropped, Δ = Fix(θ) signed (+,+), u = ω₁^∨: 27 → `1_{4/3} + 16_{1/3} + 10_{−2/3}` with
nets (−2, −2, +2); 78 → `(45+1)_0 + 16_{+1} + 16̄_{−1}` with nets (−2, +2): **two chiral 16's of SO(10)
from the 78 alone, two more 16's from a 27 if present — COUNT 2 either way**, matching B1086
(`h¹ = 2` on the θ-odd double) and fc R70's own computation. The odd walls give the same spectrum
with the sign of the 27 charges flipped (Weyl conjugates). With signs (+,−) every net is 0.

**I-27 — the chiral vacuum ≡ (a Higgs with charge locus Fix(θ), equal arc signs, direction ω₁^∨):
UNEARNED.** The three inputs are the closer's: the **locus** (the object's field is odd and non-zero
on the arcs, §2–§3), the **sign pair** (the arcs lie in different symmetry orbits, T4b), the
**direction** (odd wall/minuscule, B1174/B576: the object is θ-symmetric, chirality is the θ-odd
motion). Earning condition: a Higgs on the object that vanishes or is vortex-singular exactly on
Fix(θ) with equal signs *and* a θ-odd direction — which §3 shows cannot be θ-equivariant, so the
earning must come from a frame that breaks θ on the object's side (the D2 spectral covers are the one
such frame on the table).

## 6. Correction to fc R70 (sharpening; HOLD, not sent)

R70's "θ-even Cartan directions all give 2(R⊕R̄), vector-like" is true on the directions R70 tested
(A₅-type and the trivial ones) and **false on 4 of the 15 F₄ faces** (§4.3). R70's conclusion —
*no anomaly-free chiral spectrum under θ-equivariance* — **survives, strengthened**: the chiral even
faces are all SU(3)-anomalous. R70's mechanism ("even ⇒ dimension-symmetric") is correct and is not
vector-likeness (§4.2). R69 §4 (the sign pair is the closer's) is confirmed by symmetry (T4b). fc's
own singular-frame count of 2 is reproduced exactly on an independent E₆ realisation (T3). Relay
status: **HOLD** (owner rule: all sends hold); the correction lives here and in the ledgers.

## 7. What moves on the map

- **MASTERPLAN v3:** D1 DONE with the corrected verdict (first chiral spectrum exhibited — SO(10)×U(1),
  two 16's — as a **priced** choice, not a derivation; count 2). The assumption list of B1294 is now
  **zero assumptions and one identification**: θ-equivariance is no longer an assumption but a theorem
  about where the charge locus can be (§3), and its removal is I-27. The wall is renamed **"the charge
  locus is unsupplied"**. Next door **D2 = B1297+** (PW §3.1 spectral covers via B298's 3-fold cyclic
  cover): the one frame on the table that can break θ on the object's side — and, by §4.3, the D2
  derivation must land off the F₄ chamber or on a non-abelian configuration to be both chiral and
  clean; that is a **pre-registrable fail condition** for D2.
- **Registry:** `T-CHARGE-LOCUS-PARITY-LOCK` (§3 + §4.3), PROVED, lock test below.
- **Identification ledger:** I-27 UNEARNED (§5).
- **Kill graph:** "θ-equivariant, anomaly-free chirality from the charge locus Fix(θ) in the abelian
  frame" — NEGATIVE; hatches: D2 (non-abelian spectral covers) and "a closing that absorbs the SU(3)
  cubic anomaly of the ω₄^∨ face" (OPEN-lead candidate; `already_banked` run: no settled arc).
- **Hint ledger:** H-B1296-F4 (chiral ⟺ anomalous on the chamber), H-B1296-A2 (restricted A₂ = EIV),
  H-B1296-ORBITS (the two arcs are distinguished, 1.28 vs 0.72), H-B1296-WEYL (the odd wall is a Weyl
  conjugate of ω₁^∨), H-B1296-TRIN (the ω₄^∨ face is trinification broken by U(1)_u vs B1098's
  remnant), H-B1296-RATIO (the 1 : 3, firewalled).
- **B1295 sharpened:** its coefficient is no longer load-bearing for the smooth-frame count (T1).

## Verification

```
cd frontier/B1296_the_charge_locus_parity_lock/verification
OA_ROOT=$(git rev-parse --show-toplevel) python3 swap_and_level.py swap_and_level.json   # ~20 s; needs B1295's harmonic_generator.json
python3 e6_theta_spectra.py e6_theta_spectra.json                                        # ~40 s, exact arithmetic
python3 css_content.py                                                                   # rep names, ~10 s
python3 -m pytest tests/test_b1296_the_charge_locus_parity_lock.py -q                   # the lock
```
Outputs are banked as `*_out.txt`; both scripts end in `SELFTEST: PASS`. Deterministic (seed 1296 for
the random rays and coefficient draws; every random-draw conclusion is asserted draw-independent).

## 10. Credit and scope, read after the arc (2026-09-08)

**Credit and scope, read after the arc (2026-09-08).** The physics seat's **fc R71** (2026-09-06, one day before this arc) scanned 928 θ-even directions and found *"every chiral case has an A₂ factor and a nonzero SU(3) cubic anomaly; no direction is chiral and anomaly-free"* — the same dichotomy this arc proves face by face on the F₄ chamber; R71 corrected R70 §2 at source before B1294's relay reached it. Credited here; verification of R71's scripts on this bench is scheduled (B1298). **Scope clause:** the spectral half of T-CHARGE-LOCUS-PARITY-LOCK is computed under the OUTER lift θ_D of the involution to E₆ (the diagram automorphism composed with an inner element, fixing F₄). fc R72 (2026-09-06) shows B353's own item (B): a second, INNER lift Ad(exp πiρ^∨) exists (fixing A₅ ⊕ A₁, the whole Cartan), under which every U(1) direction is even and the singular count is 2 × (16 ⊕ 10 ⊕ 1), anomaly-free, without dropping equivariance. This arc did not engage the inner lift; whether the object's geometric germ selects the outer lift (the SM-derivation seat's sm:B1280 Thm 2 says it does: six signs) is B1298's question, and the lift itself is the identification row fc asks for (I-28, registered there). Until then the lock reads "under the outer lift", and I-27's "direction" price may become a "lift" price.
