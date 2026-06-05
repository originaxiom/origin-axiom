# B89-T — the metallic tower's cohomological route closed; the explicit Sym reduction (Task T)

**Status:** route-closure (rigorous) + a STRUCTURAL advance (explicit closed-form, symbolic-m) +
CONJECTURE (the module-iso derivation). Standalone Lie/invariant theory; **no Origin-core claim**; proven
core P1–P16 untouched. Script `probe.py`; test `tests/test_b89t_tower_route.py`.

## Task T's goal and the honest outcome
Task T set out to prove the tower `char(J(m)) = ∏ char(±Mᵏ)` for **all n** via the cohomological /
root-height route (the handoff's premise: `J(m)` = the once-punctured-torus monodromy `M_m` acting on
`H¹(F₂; ad ρ)`, graded by root height). **That route is foreclosed** — but pushing on the genuine gap
(B85's Procesi assembly) produced a concrete advance.

## (1) The cohomological route fails (C1) — a third dead shortcut
The metallic trace-map fixed line is "all traces = n", i.e. the **trivial representation** (first-order
degenerate: `d·tr(W)=0` for every word — B58's obstruction). There
`H¹(F₂; ad triv) = Hom(F₂^{ab}, sl(n)) = sl(n)⊕sl(n)` and `φ_m` acts as `M_m ⊗ id_{sl(n)}`, so its char
poly is **`char(M)^{n²−1}`** — all `char(M)`, no higher powers — verified ≠ tower for n=3,4,5. The
tower-carrying object is the **trace-coordinate (Procesi) Jacobian**, not a representation linearization.
The two cohomological repairs are already refuted: principal-SL(2)/Kostant `sl(n)=⊕Sym^{2k}` is
**even-powers-only** (misses `char(M),char(M³)`), and the `H¹(F₂)=ℂ²` coupling was killed from the
multiplicity side (B58 Stage 1 = V27 kill #25). So the cohomological route joins **B84** (numerics) and
**B85** (`Λ²V`) as a closed shortcut.

## (2) The explicit Sym-module reduction (the advance)
Each `Sym^d(M)` factors over the Dickson catalog in **both** parities (`Sym³=char(M⁻¹)char(M³)`,
`Sym⁴=(t−1)char(−M²)char(M⁴)`, …). The all-n tower equals the explicit two-sequence product
```
   char(J(m))  =  ∏_{d=2}^{n} char(Sym^d M_m)  ·  ∏_{d=0}^{n-3} char(Sym^d M_m)           (T)
```
verified here **symbolically in m** to equal the **proved** tower (B80/B65) at n=3,4 and the
**structural** tower (B62) at n=5 — B58 had checked only `m=1` (the Fibonacci `det=−1` case). Degrees
`(3+…+(n+1)) + (0+…+(n−2)) = n²−1`. This converts B85's "assemble the symbolic trace map σ" into one
clean **module-isomorphism conjecture**:
```
   J(m)  ≅  M_m acting on  [ ⊕_{d=2}^{n} Sym^d ℂ² ]  ⊕  [ ⊕_{d=0}^{n-3} Sym^d ℂ² ]          (M)
```
over the mapping-class `SL(2)` (`M_m` on `H₁(F₂)=ℂ²`). **(M) is PROVED for n≤4** (it equals B80's tower
symbolically in m) and matches B62 at n=5; the **derivation** of (M) for all n — *why* `J(m)` is this Sym
module — is the lone open item (the Procesi structure, B58 Gate 1).

## (3) The n=6 discriminator
(T) predicts `char(M³)` multiplicity `a₃(n=6) = 2` — **agreeing** with the independent
opposition-involution θ-split (B62) and **contradicting only** B66's pinv `a₃=1`, which B84 showed is
**gauge-corrupted** at exactly this doubly-degenerate sector. So the open n=6 row is now corroborated
**2-of-3 toward `a₃=2`**, the lone dissent being the known-bad numerics.

## Labels (honest)
- (1) route-closure: **rigorous** (decisive symbolic computation).
- (T) at n≤4: **PROVED-consistent** (equals B80's proved tower, symbolic m); at n=5: matches structural.
- (M) for all n: **CONJECTURED** (the module-iso derivation is open — the Procesi problem).
- (3) `a₃(n=6)=2`: **CANDIDATE**, corroborated by two independent constructions (Sym, θ).

## Net for the program
The tower's all-n proof is sharpened from B85's "assemble σ" to a **single explicit module-isomorphism**
(M) with an explicit closed-form (T) — and three independent routes (numerics B84, `Λ²V` B85, cohomology
here) are now known dead. The decisive next test is the n=6 row (`a₃`), which still needs the symbolic σ.

```bash
python frontier/B89T_tower_route/probe.py
python -m pytest tests/test_b89t_tower_route.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
