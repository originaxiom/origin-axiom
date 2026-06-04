# B58 Phase A — exact (n²−1) fixed-line Jacobian via ε-series over F_p

**Date:** 2026-06-03. **Status:** exploratory. Proven core P1–P16 untouched. `m=1` throughout
(`σ:(X,Y)→(X+Y,X)`). Engine + n=4 pass committed (`efda953`); this update supersedes the §(c)
causal framing below.

---

## UPDATE (2026-06-03) — the n=5 gap is the pinv-limit CONSTRUCTION, not the field/metric

A follow-up brief hypothesized the n=5 `char(M²)` shortfall was an **F_p non-canonicity**
artifact (finite fields have no positive-definite form → the least-squares metric is
non-canonical → ambiguous at a degenerate eigenspace) and proposed an exact-ℚ + `S=I` fix
(the analog of B66's real SVD-pinv) that should restore `a₂=2`. **The allowed cross-checks
refute that diagnosis.** Three independent computations of the pinv-limit all return **`a₂=1`**
at n=5 — across both fields and both metrics, including a genuinely positive-definite char-0 one:

| computation | field | metric | char(M²) | leftover |
|---|---|---|---|---|
| this engine (committed) | F_p exact | random symmetric `S` | **1** | untagged deg-3 |
| this engine, `S=I` | F_p exact, **prime-stable** (= ℚ mod p) | `S=I` (canonical) | **1** | untagged deg-3 |
| B66 `fixed_line_spectrum` | ℝ (mpmath, dps 60) | MP-pinv (**positive-definite**) | **1** | `{−0.734, −0.734, 2.695}` |

The `S=I` exact-F_p run is **prime-stable over 3 primes**, so for those primes `Dx·Dxᵀ` is
non-singular and the result **equals the ℚ `S=I` result mod p** — the canonical-metric exact
characteristic-zero answer is `a₂=1`. B66's real MP-pinv (literally the positive-definite char-0
construction the fix invokes) also returns `a₂=1`. So **neither the field (F_p vs ℚ) nor the
metric (random `S` vs `S=I`) is the cause** — the proposed exact-ℚ fix would reproduce `a₂=1`,
not `a₂=2`. (A direct exact-ℚ engine, `_q_engine.py`, was written and **validated at n=3** — it reproduces
`char(M⁻¹)·char(M²)·char(M³)·(t−1)(t+1)` exactly (~10 s) — confirming the construction is correct;
but via sympy+`Fraction` it is impractically slow at n≥4 (n=4 did not finish in minutes vs the
F_p engine's ~3 s, the anticipated rational blowup) without python-flint. It is also **not needed**:
exact F_p with `S=I` already *is* the ℚ object mod p, prime-stably.)

**The real cause: the pinv-limit is non-canonical at the n=5 degenerate even-k sector.** The
leftover is a **non-Dickson** degree-3 block — B66's real eigenvalues there are
`{−0.734, −0.734, 2.695}` (a *repeated* root, hinting at a defective/Jordan structure), nowhere
near `char(M²)·(t+1)`'s roots `{2.618, 0.382, −1}`. At n=5 the even-k sector carries the *repeated*
factors `char(M²)²` and `(t+1)²`; the `ε→0` least-squares limit at colliding eigenvalues is not a
canonical operation, and **every** field/metric realization produces this defective cubic instead
of the clean doubled Dickson factors. The clean `a₂=2` is recovered only by **B62's structural
opposition-involution (θ=−w₀) argument**, which *does not go through the pinv-limit*. So the two
characterizations **disagree exactly at the degenerate even-k block** — the pinv-limit / "ambient
Jacobian" construction (B59–B66, any field/metric) underflows it; B62's structural split fills it.

**This is the brief's anticipated outcome 3** ("the pinv-limit CONSTRUCTION, not the field,
disagrees with B66/B62"). Per its binding rule: **STOP, do NOT patch** — the exact-ℚ field-swap
is not the fix (the construction, not the arithmetic, is what underflows the degenerate sector),
and the resolution (a degeneracy-aware canonical limit, or anchoring the multiplicities on B62's
structural split rather than the pinv-limit at colliding eigenvalues) is a **joint decision, not a
solo patch**. `a₂=2` is not in doubt (B62 structural); what is established is that **no pinv-limit
realization recovers it at the collision** — the precise, corrected localization.

---

## What this is

The one surviving route to the `a_d` multiplicity formula is the `(n²−1)`-dim fixed-line
Jacobian of the metallic trace map, whose `char(J)` factors over the Dickson catalog
`{char(±M^k)}`. B63/B65 built it by rep-perturbation numerics + rational interpolation; B66 by
rep-perturbation + **mpmath SVD-pinv**, which ceilings out at n=6 (the "gauge degeneracy" =
ill-conditioned float pinv). Phase A computes the **same object via the same pinv-limit but
EXACTLY over F_p**, to remove the float conditioning.

### The engine (`jacobian_closure.py`)

- **The limit is a least-squares pinv-limit, not an exact solve.** `ρ(ε)=(exp εP, exp εQ)` is
  *not* a fixed point of `φ` for `ε≠0`, so `DT·Dx = DX` is **inconsistent**; and the trace map is
  first-order degenerate at the identity (`Dx(0)=0`), so `DT_0 = lim_{ε→0} DX(ε)·pinv(Dx(ε))` is a
  genuine `0/0` least-squares limit (this is *why* B66 needs a pinv). A first wrong attempt
  (exact solve of `DT·Dx=DX`) was correctly rejected as inconsistent.
- **Exact F_p realization.** Work in `F_p[ε]/(ε^{L+1}) ⊗ F_p[h]/(h²)`: reps `A=(I+h g)exp(εP)`
  are exactly in `SL(n)` to all tracked ε-orders. The `h¹` part of `tr(word)` is the gradient row
  `Dx(ε)=Σ_{l≥1} Dx_l ε^l` (the `ε¹` part alone is the **rank-3 Fricke block** — all words share
  the same 2nd-order trace form — so the `n²−1` coordinates only separate across orders `1..L`).
- **The least-squares solution satisfies the normal equations exactly**, so we solve the
  consistent power series `DT(ε)·G(ε)=R(ε)` with `G=Dx S Dxᵀ`, `R=DX S Dxᵀ` (random metric `S`),
  order-by-order for the constant term `DT_0`. The solve **decouples by row**, keeping each step
  small and exact over F_p. (Only the complete orders `≤L+1` are used.)
- **The n×n matrix arithmetic auto-enforces Cayley–Hamilton / the exterior-power closure** (a
  concrete matrix satisfies its own char poly), so `e_2..e_{n-1}` need **no hand-built multi-block
  trace identities** — the gap B64 localized and B65 sidestepped is handled implicitly.
- **Word basis:** the `n²−1` coordinate words are picked by B66's proven near-fixed-line QR-pivot
  (`b66_select`). This is a **basis choice only**; the Jacobian is then computed exactly and
  validated prime-stable + against B65, so the selection method does not affect rigor. (A
  generic-rep / unipotent F_p selection was tried and *fails*: power traces `tr(A),tr(A²),…` are
  independent at a generic point but Newton-dependent at the fixed line, so a generic-point
  coordinate set need not be a valid **fixed-line** coordinate system — confirmed empirically.)

Prime-stable over 3 primes `{2000003, 2000029, 2000039}`. Computer-assisted modular **evidence**,
not a symbolic proof.

## (a) Does n=4 reproduce B65's `(1,1,1,1)`?  — **YES (POC GATE PASS).**

Exact, prime-stable over 3 primes:
```
char(M^-1)·char(M)·char(M^2)·char(M^3)·char(M^4)·char(-M^2)·(t-1)^2(t+1)
a_d = (1,1,1,1),  b_2 = 1.
```
Identical to B65's independently-reconstructed `Z[m]` factorization. n=3 (sanity) also exact:
`char(M^-1)·char(M^2)·char(M^3)·(t-1)(t+1)`, `a_d=(·,1,1)`. **The machinery is validated through
n=4.**

## (b) Does n=5 reproduce `(2,2,1,1,1)`?  — **NO. The n=5 gate FAILS, localized.**

Converged (identical at **L=12,16,20**) and prime-stable, the engine returns
```
char(M^-1):1  char(M^1):2  char(M^2):1  char(M^3):1  char(M^4):1  char(M^5):1
char(-M^2):1  char(-M^3):1  (t-1):2  (t+1):1  +  degree-3 UNTAGGED remainder
```
vs the established `a_d=(2,2,1,1,1)`, `b_d=[d≤3]`. **The single localized discrepancy is the
`char(M²)` block: multiplicity 1 instead of 2**, with the `(t+1)` parity also 1 instead of 2; the
"missing" `char(M²)·(t+1)` (degree 3) appears instead as an untagged degree-3 factor.

**This is the binding-rule outcome: STOP, report which block.** Per the Phase A brief
("If the gate FAILS: STOP, do NOT spawn diagnostics, report exactly which `char(M^k)` block the
closure gets wrong"), no further diagnostics were run and **Phase B (n=6,7) was NOT entered.**

### (c) The localized failure — `char(M²)` = the even-k / `e₂=tr(Λ²A)` sector

The failing block is precisely the **doubly-degenerate even-k sector**, and the diagnostic
detail is sharp:
- the **fundamental** `char(M¹)` multiplicity-2 **resolves correctly** (`a_1=2` ✓);
- only the `char(M²)` multiplicity-2 **fails** (`a_2`: 1 not 2).

`char(M²)` is the even-k factor tied to `e₂=tr(Λ²A)` (B64's parity mechanism: even-k ↔
P-symmetric sector; B64/B65 localized the genuinely-new multi-block to `e₂=tr(Λ²A)`). So the
exact-modular LS-limit closes everything **except the second copy of the `Λ²/e₂` even-k factor**.

### Method-limitation, not a refutation (honest caveat)

`a_2=2` is **correct** — B66's high-precision SVD-pinv resolves `char(M²)=2` with the *same* word
basis (and B61/B62 established the full `(2,2,1,1,1)` row). So this is a **localized gap in the
exact F_p least-squares pinv-limit at the doubly-degenerate `Λ²/e₂` block**, not a property of the
underlying closure: the char-0 SVD-pinv resolves the degenerate eigenspace there; the exact
F_p normal-equation limit, as implemented, resolves only one of the two copies. The precise
input for the next step is therefore: **strengthen the exact pinv-limit's handling of the
doubly-degenerate even-k (`e₂=tr(Λ²A)`) eigenspace** — the fundamental-sector degeneracy
(`char(M¹)` mult-2) already works, so the gap is specifically the multi-block Λ² multiplicity.

## Files

- `jacobian_closure.py` — the engine (ε-series dual numbers over F_p; LS normal-equation
  pinv-limit; B66 word basis; Dickson tagging reused from B58 Stage 1).
- `phaseA_results.json` — per-n towers, `a_d`/`b_d`, prime-stability, gate verdicts, word bases.

## Reproduce

```bash
python frontier/B58_phaseA/jacobian_closure.py     # n=3 sanity, n=4 POC gate, n=5 gate (~40s)
```

## Disposition

- n=4 POC: **PASS** (machinery validated, exact, matches B65).
- n=5 gate: **FAIL**, converged + prime-stable, localized to the `char(M²)` / `e₂=tr(Λ²A)`
  even-k multiplicity-2 block.
- **Phase B (n=6,7) not entered** (binding stopping rule). No claim promoted; proven core
  untouched. Uncommitted pending review.
