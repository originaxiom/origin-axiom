# B1297 — THE SPECTRAL-COVER INDEX: derived, pre-registered, evaluated — and the descent's twists are inverted by the figure-eight's own period-2 symmetry, so every (2+1)-reducible spectral-cover configuration on the cyclic tower is vector-like

*MASTERPLAN v3 Phase 3 = Door D2. The 3-manifold spectral-cover index was written as a formula with a
stated domain and sealed (`PREREG.md`, sha256 `75e55a88…`, 2026-09-07) BEFORE evaluation; Part II
(`PREREG_C4.md`, `16918308…`) was sealed before its evaluation on 2026-09-08. Every number is this bench's:
exact arithmetic over ℚ(ζ₁₂) (an own field class, own Reidemeister–Schreier, own Fox calculus, own Smith
form), floating-point SVD as the second method on every rank, and SnapPy 3.3.2 only for the cover census,
isometry-group orders and the base presentation. Nothing is taken from a seat. Dates 2026-09-07/08.*

## The sentence

**On a one-cusped 3-manifold the net chirality of a local system `V` is `I(V) = t₀ − r₁`: the number of
cusp-invariant vectors minus the rank of the boundary map — the failure of "half lives, half dies" for a
non-self-dual `V` with cusp invariants. For the E₆ spectral covers of PW §3.1 on the ℤ/3 descent of m004 the
index reduces by Shapiro to `I(C; Sym²ρ_geo ⊗ ψ)` over the descent's torsion characters ψ, and it is
IDENTICALLY ZERO — on all 16 characters of the 3-fold cover and all 45 of the 4-fold cover — for two
independent reasons, both proved: (i) GALOIS SELF-DUALITY, the coefficient field's automorphism that fixes
ℚ(√−3) and inverts ψ carries `V` to `V*` (every ψ of order prime to 3); (ii) THE PERIOD-2 SYMMETRY of the
figure-eight acts as −1 on its Alexander module (`a ↦ a⁻¹` on the module's generator, one line), hence
inverts every torsion character of every cyclic cover, and being orientation-preserving forces
`J(ψ) = J(ψ⁻¹) = −J(ψ)`. The masterplan's head sentence — "3 comes only from the ℤ/3 descent and the descent is
vector-like" — is now a THEOREM for the whole cyclic tower's (2+1)-reducible configurations, with the
mechanism named: the object's own symmetry is charge conjugation on the descent's twists.**

## 0. What the pre-registration got wrong, and how it is reported (MB12)

Part I registered a PASS/FAIL on the 3-fold cover before computing (§1). The table came out all zero (§4),
matching the symmetry census computed first (§4.2). But the Galois argument (§5.1), found only AFTER the
table while reading the live-manifold scan, shows the Part I test **could never have passed**: the 3-fold
cover's torsion is `(ℤ/4)²`, its characters have order dividing 4, and ℚ(i) ∩ ℚ(√−3) = ℚ. That is the
B1267 shape (a rigid "0 = 0") caught inside the same arc rather than four arcs later (E65). It is reported
here as a **forced zero**, not a passed test. Part II then registered the first sector where the Galois
argument is unavailable — the 3-torsion of the 4-fold cover — and its census, computed before its table,
killed it too (§4.3): the period-2 lift inverts the order-3 characters as well. So **the pre-registered test
was non-vacuous in no sector of the tower examined**, and the honest verdict is not "FAIL" but "FORCED": a
theorem (§5.2) makes the whole family vector-like. The door's remaining live sectors are named in §6 and
registered as L202.



## 1. What was pre-registered (sealed hashes in `PREREG.sha256`)

`PREREG.md` §1–§5: PW's 3d BPS configurations = reductive flat E₆(ℂ) connections; spectral cover =
`ρ = Ind_{π₁C}^{π₁M} ρ₁` with the trinification block structure `27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)`; the index
formula with its domain D and conventions (§2 below); the (2+1)-reducible family
`ρ₁ = (ρ_geo|_C ⊗ κ) ⊕ κ⁻²` and its reduction to `Sym²ρ_geo ⊗ ψ`, `ψ = κ/κ^τ`; PASS = some ψ with `I ≠ 0`,
FAIL = all zero; the symmetry census to be computed before the cohomology; six controls (a)–(f).
`PREREG_C4.md`: the same on the 4-fold cover's order-3 characters, with the explicit clause that a
census-forced zero is reported as forced, not as a fail.

## 2. The index (derived; every identity below is CHECKED on every sector computed)

`M` one-cusped, `T` the cusp torus, `V` a local system, `a_k = h^k(M;V)`, `t_k = h^k(T;V)`,
`r₁ = rank(H¹(M;V) → H¹(T;V))`, starred for `V*`. From the pair sequence, Lefschetz–Poincaré duality,
`χ(M;V) = χ(T;V) = 0` and the annihilator property `r₁ + r*₁ = t₁`:

    n(V) := dim im(H¹(M,T;V) → H¹(M;V)) = a₁ − r₁            (interior = L² classes, Zucker)
    I(V) := n(V) − n(V*) = (a₀ − a*₀) + t*₀ − r₁                 (exact, always)
    F(V) := a₁ − a*₁ = (a₀ − a*₀) + r₁ − t₀ ;   Cc(V) := c₁ − c*₁ = I + (t₀ − t*₀) − (a₀ − a*₀)

**Domain D:** ρ reductive (`a₀ = a*₀`) and cusp holonomy in a one-parameter unipotent group times
finite-order scalars (`t₀ = t*₀`). In D: **`I = t₀ − r₁ = r*₁ − t₀`, `F = −I`, `Cc = I`** — one integer,
convention-free up to the 27-vs-27̄ naming. Theorems inside D, each reproduced by the code: (T1)
`I(V*) = −I(V)` (universal, not only in D); (T2) closed M ⇒ 0 (B1260 §1, irreducible → semisimple); (T3)
self-dual V ⇒ `r₁ = t₀` ⇒ 0 (covers E65 and every θ-symmetric configuration); (T4) characters ⇒ 0
(reciprocity, B1260 §2); (T5) `t₀ = 0 ⇒ I = 0` (only cusp-invariant local systems can be chiral); (T6)
`I(f*V) = I(V)` for every homeomorphism f of the pair, and with complex conjugation `J(ψ∘σ) = −J(ψ)` for
orientation-reversing σ. The physics of the formula: **the whole chirality lives in the boundary map** — the
cohomological form of fc R69's "the cusp keeps the endpoints; every closing removes them".

## 3. The configuration (THE IDENTIFICATION RULE: the map exhibited, then shown to act)

- **The E₆ block structure** (`verification/step6_e6_blocks.py`, exact over ℚ): E₆ built in the SL(3)³ frame
  (72 roots = 18 + 27 + 27, closed under reflections, Cartan matrix of E₆, det 3); the 27 = three 9-blocks,
  minuscule, one W-orbit; the cyclic permutation σ of the three factors preserves the roots, maps 27 → 27
  (not 27̄), cycles B1 → B2 → B3 → B1, and **is the Weyl element `s₁s₅s₃s₂s₄s₅`** (length 6, fixed 2-plane in
  the Cartan) — inner, as the block structure requires.
- **Shapiro:** `ρ|_{π₁C} = (ρ₁, ρ₁^τ, ρ₁^{τ²})`, `27_ρ ≅ Ind(ρ₁ ⊗ (ρ₁^τ)*)`, and since C is one-cusped the
  induction commutes with the cusp restriction: **`I(M; 27_ρ) = I(C; ρ₁ ⊗ (ρ₁^τ)*)`**.
- **The E₆ cubic forces SL(3), not GL(3):** scalar twists must be cube roots of unity. The 3-fold cover has no
  3-torsion, so its family characters enter only through the (2+1)-reducible configurations
  `ρ₁ = (ρ_geo|_C ⊗ κ) ⊕ κ⁻²` (det 1; non-extending iff `κ^τ ≠ κ`, the deck action `Φ₃` being fixed-point-free
  — B326). The bifundamental decomposes as `Sym²ρ_geo ⊗ ψ ⊕ ψ ⊕ ρ_geo ⊗ κκ^{2τ} ⊕ ρ_geo ⊗ κ⁻²κ^{−τ} ⊕ κ^{2τ}κ⁻²`;
  characters give 0 (T4), the rank-2 summands have `t₀ = 0` (the lifted longitude has trace −2 in every
  SL(2)-lift and is null-homologous in C: computed, `[l_C] = 0`) so give 0 (T5). **Deciding table:**
  `I(C; Sym²ρ_geo ⊗ ψ)` over all family characters, `ψ = κ∘(1−τ)` ranging over all of them (`1−τ` invertible
  on the torsion, det Φ₃(1) = 3).
- **The bench:** the exact geometric representation in Fricke normal form,
  `ρ(a) = [[1−ω, 1],[−1, 0]]`, `ρ(b) = [[0, −1],[1, −2ω]]` (ℤ[ω], relator = +I, `tr ρ(ab) = 2`, `tr ρ(ℓ) = −2`;
  the second lift `(−A,−B)` has `tr ρ(ab) = −2`; the longitude has trace −2 in both — Sym² is lift-independent,
  checked). Own Reidemeister–Schreier for the kernels of `a ↦ 0, b ↦ 1 (mod n)`.

## 4. Results

### 4.1 Controls first (PREREG §5, all PASS)
Untwisted `Sym^k` on m004: `h¹ = 1,0,1,0,1,0,1` for k = 0..6 — B1256/B1267's table reproduced, with
`r₁ = t₀ = 1` on every even k (half lives, half dies) and every identity of §2 holding; H₁(C₃) = ℤ⊕(ℤ/4)²
reproduces B326, the deck action on the torsion is `[[2,3],[3,1]]` with characteristic polynomial Φ₃;
`[m_{C₃}] = [z]` = the deck-invariant free generator with ZERO torsion part and `[l_{C₃}] = 0` — so **all 16
family characters are cusp-trivial** (every sector has `t₀ = 1`; the index is live for all 15 non-trivial ψ);
`h¹(C₃;ℂ) = 1 = r₁ = t₀`.

### 4.2 The symmetry census (computed BEFORE the table, as registered)
All 24 isometries of C₃ realised as automorphisms of π₁(m004) found through the faithful PSL rep (exact
SL(2) sign-twist triples; Mostow makes every such endomorphism an automorphism), 12 orientation-preserving
+ 12 reversing (m004 amphichiral), acting **faithfully** on Tors H₁(C₃). **The period-2 symmetry
`P: a ↦ a⁻¹, b ↦ a³b` (orientation-preserving, +1 on the free part) acts as −1 on the torsion** — verified
twice: by Reidemeister–Schreier (`step4_census.py`) and, with no RS at all, by Fox calculus over ℤ[ℤ/3]
with the semilinear coefficient action and a chain-map check (`step4b_period2_check.py`; the strong
inversion, which inverts the ℤ/3, is the case that catches a missing coefficient action — both routes agree
on every invariant). Prediction recorded: `ψ∘P = ψ⁻¹` for all 16 ⇒ with T1 and T6, **J ≡ 0 on all 16**.

### 4.3 The tables
**C₃ (`step5_table.py`):** all 16 sectors `a = (0,1,1) = a*`, `t = (1,2,1)`, `r₁ = r*₁ = 1`, **I = F = Cc = 0**;
every identity true; exact and SVD ranks agree; the other SL(2)-lift gives the same table. Controls: k = 0
(`h¹(C₃;ψ) = 1` for every ψ), k = 1 (both lifts: everything 0, `t₀ = 0`), free-part twists ψ(z) ∈ {i,−1,−i}
(`t₀ = 0 ⇒ 0`), k = 4 (`I = 0`, `r₁ = t₀`).
**C₄ (`step10_c4.py`, Part II):** H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/15 (|Tors| = |Δ(i)|²·|Δ(−1)| = 45; SnapPy agrees), all 45
torsion characters cusp-trivial, `|Isom| = 32` realised (8 classes × 4 deck lifts). **Census first:** P
maps `(1,0) ↦ (2,0)`, `(0,5) ↦ (0,10)` — inversion on the order-3 characters too — so all 8 Galois-unprotected
sectors are forced to 0, as are the order-5 and order-15 ones. **Table:** 45 sectors, all `I = 0`,
`a = (0,1,1)`, `r₁ = r*₁ = 1`; the 8 order-3 sectors exact over ℚ(ζ₁₂) (ω-valued) and numeric agree.

## 5. The two theorems

### 5.1 T-GALOIS-SELF-DUALITY (checked on the table: `step9_galois.py`)
Let `V = W ⊗ χ` with W defined over a number field k and χ a character of finite order n, and suppose
`k(ζ_n)` has an automorphism τ with `τ|_k = id`, `τ(ζ_n) = ζ_n⁻¹` (⟺ `k ∩ ℚ(ζ_n)` is real). Then
`V^τ ≅ W ⊗ χ̄`, every rank of the Fox complex and the boundary map is τ-invariant, and if `W ≅ W*` then
`I(V) = I(V^τ) = I(V*) = −I(V) = 0`. For the object k = ℚ(√−3) = ℚ(ζ₃): **every twist of order prime to 3
is vector-like by arithmetic alone**, on every cover, with no reference to symmetry. The live scan
(`step8_live_manifold_scan.py`, 60 one-cusped census manifolds with torsion ≥ 3, 12 non-self-dual
`Sym²⊗χ` sectors, all `I = 0` with `r₁ = t₀ = 1`) is consistent with it. (This also shows the index vanishes
for every UNITARY local system: `V* ≅ V̄` and conjugation preserves ranks.)

### 5.2 T-PERIOD-2-INVERTS-THE-ALEXANDER-MODULE (proved symbolically: `step11_alexander_module.py`)
With `a ↦ 1, b ↦ t`, the Fox complex of `⟨a,b | aaabABBAb⟩` has `∂r/∂b = 0`, `∂r/∂a = −t⁻¹Δ(t)`,
`Δ = t² − 3t + 1`, so `H₁(X̃) = ℤ[t^±]·e_a/(Δ)` is cyclic on the lift of `a`; the period-2 automorphism
`P: a ↦ a⁻¹, b ↦ a³b` commutes with the deck action (`P(b) ↦ t`) and acts on `e_a` by `∂(a⁻¹)/∂a = −a⁻¹ ↦ −1`.
**Hence P = −1 on the Alexander module, and on the torsion of every cyclic cover `C_n`** (|Tors| =
|Res(Δ, (tⁿ−1)/(t−1))| = 5, 16, 45, 121, 320 for n = 2..6; verified directly for n = 3 and n = 4 by two
routes). **Corollary (T-CYCLIC-TOWER-VECTOR-LIKE):** for every n, every `j`, every torsion character ψ of
`C_n` trivial on the cusp, `I(C_n; Sym^{2j}ρ_geo ⊗ ψ) = 0` — P lifts to an orientation-preserving isometry
of `C_n` fixing the cusp, `ρ_geo∘P ≅ ±ρ_geo` (Mostow), `ψ∘P = ψ⁻¹`, so `J(ψ) = J(ψ⁻¹) = −J(ψ)`. With §3, every
(2+1)-reducible E₆ spectral cover on the cyclic tower is vector-like: **the object's own period-2 symmetry
is charge conjugation on the descent's twists.**

## 6. What is NOT closed (scope, said plainly; registered as L202)
(a) **Irreducible non-extending SL(3) representations of π₁(C_n)** — the corpus's W1/W2 (B102/B1267) extend
to m004 and are rigid; a chiral configuration would need a component of `X_{SL(3)}(C_n)` on which
`ρ₁∘P ≇ ρ₁*` (the period-2 argument needs `P` to act as duality; nothing forces it there). (b) **Non-cyclic
covers** of m004 (B1295's tower of 87 to degree 10): P need not preserve a non-normal subgroup, and the
Galois argument needs the twist's order prime to 3 — 3-torsion in a non-cyclic cover's H₁ is the first
Galois-unprotected, symmetry-unprotected place to look. (c) **Whether `I ≠ 0` occurs at all** on a
one-cusped hyperbolic manifold in domain D: no example found (§5.1 scan); a general vanishing theorem is
NOT proved, and if one exists the index is not an instrument — that question is part of L202 and gates
any further use of the formula as a discriminator. (d) The θ-odd non-abelian direction of B1296's fence is
untouched: `Ind ρ₁` is block-permuting, not a Cartan direction; its abelian limit `κ → 1` is the self-dual
sector (T3), consistent with the lock.

## 7. Controls and non-vacuity (MB12: operation non-trivial, criterion can pass AND fail)
(a) E₆ blocks exhibited (§3); (b) B326 reproduced; (c) rep exact, `Sym^k` table = B1256/B1267, `h¹(C;ℂ) = 1`;
(d) every identity on every one of 61 sectors + controls; (e) **algebraic non-vacuity:** the same code on
random 2-generator presentations with random "peripheral" pairs and random local systems returns `I ≠ 0`
in 26 of 31 trials and violates the 3-manifold identities in the same 26 — the identities are theorems of
the manifold, not tautologies of the code, and the criterion is reachable by the operation; **live
non-vacuity NOT established** (§6c); (f) exact ℚ(ζ₁₂) and float SVD agree on every rank.

## 8. Against the corpus and the seats
- B1260 §1 (closed wall) generalised to semisimple; B1260 §4 / B1267's "0 = 0" on rigid W1/W2 is now
  explained (T3 and Galois both apply to them); B1290's `net chirality = χ(M,∂⁺M)` is the untwisted,
  coefficient-free face of the same boundary-map statement — the twisted version is `I = t₀ − r₁`; B1086's
  `h¹ = 2` on the θ-odd double is a full count, not an index. fc R69 ("the cusp keeps the endpoints") is
  confirmed in cohomological form; fc R70's scope gap ("non-abelian configurations not examined") is now
  examined for the (2+1) family and closed. The SM-derivation seat's B1280 ("W1/W2 vector-like on every
  cusped cover") is a parallel result on the seat's branch — CITED, not verified here; it enters the
  harvest queue (sm:B1280–B1283), never by trust.
- I-26 (`h¹` ↔ 4d chiral generations) is the conditional every count here rests on and stays UNEARNED;
  this arc adds NO identification row (its only "X is Y" is the E₆ block structure, a theorem in E₆).
- The masterplan head: **"the descent is vector-like" is a theorem for the cyclic tower's (2+1)
  configurations, by the object's own symmetry.** The chirality bit, if it exists, needs a configuration
  the period-2 symmetry does not dualise (§6a–b) — a sharper door than "PW §3.1 spectral covers".

**Credit, read after the arc was written (2026-09-08).** The SM-derivation seat's **sm:B1280** (2026-09-06, one day before this
arc's Part I) proved that B71's elliptic SL(3) components W1, W2 are vector-like on every cusped cyclic cover, and its mechanism
is the same isometry: over each point of the trace coordinates the second sheet is **the dual representation pulled back by the
period-2 isometry** (the hyperelliptic involution of the fibre, `a ↦ a⁻¹, b ↦ b⁻¹` on the punctured torus). This arc found the
period-2 isometry acting as −1 on the Alexander module, i.e. the same duality on the descent's *twists*; the seat had it for the
*irreducible components* first. Neither is verified on the other's bench yet: sm:B1280 enters the harvest queue at the top (its
Theorem 1, if it reproduces here, closes L202(a) for every component that extends from m004, leaving only non-extending ones).
The Galois wall is this bench's alone. Cited, not verified; nothing here rests on it.

## 9. Firewall and fences
The Galois theorem is a statement about coefficient fields, not about physics; "charge conjugation" names
the action `ψ ↦ ψ⁻¹` on twists, and nothing about CP in 4d is claimed. No number here is a generation
count. The 1 : 3 of B1296 is not touched. The "period-2 symmetry" is the figure-eight's rotational period-2
symmetry (axis disjoint from the knot, preserving the meridian direction) realised as `a ↦ a⁻¹, b ↦ a³b` in
SnapPy's presentation; absence sweeps: `spectral cover index` ABSENT on all 40 heads; "Galois self-duality"
on no head but this arc's; "Alexander module" present (B326, the deck action, cited) with no row on P's action.

## 10. Reproduction
`verification/`: `d2lib.py` (field ℚ(ζ₁₂), matrices, Fox, RS, Smith), then in order `step3_controls.py`
(writes `cover_presentation.json`), `step4_census.py`, `step4b_period2_check.py`, `step5_table.py`,
`step6_e6_blocks.py`, `step7_nonvacuity_random.py`, `step8_live_manifold_scan.py [cap]`, `step9_galois.py`,
`step10_c4.py`, `step11_alexander_module.py`; each ends in a PASS line or a `nonzero = 0` line pinned by
`tests/test_b1297_the_spectral_cover_index.py`, which RUNS them in a scratch cwd. Runtime ≈ 2 min (scan capped).
