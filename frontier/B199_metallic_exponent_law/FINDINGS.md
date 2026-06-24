# B199 — the metallic exponent: no closed-form law; the clean exponent is a *sublocus*; SL(5) exact-symbolic exhausted

**Date:** 2026-06-24. **Status:** the flagship metallic-exponent question is **closed by computation** with three honest results:
(A) **no closed-form `k(o,m)`** survives an adversarial judge panel — only the **sign `s=(−1)ⁿ⁻¹`** does; (B) **verify-don't-trust
correction of B198** — the rigid identity `[A,B]=µ²` holds only on a **~1% rigid sublocus** of the loxodromic component,
not the whole component; (C) the **SL(5) exact-symbolic proof is NEEDS-SPECIALIST** at a sharp, named 25-variable Gröbner
wall, after **maximal** exhaustion of four routes. Standalone character-variety / low-dim-topology math; **no physics, nothing
to `CLAIMS.md`, P1–P16 untouched.** Ledger V192. Produced by a multi-agent **Workflow** (113 agents, ~4.5M tokens, 4h):
adversarial verify → law propose+judge → 4 Goal-B exact routes → deep-research novelty → consolidate (`workflow_result.json`).

## The verified geometric-stratum exponent table

`k` is the integer in `[A,B] = s·µ^k` (`µ=A⁻ᵐt`), read **only on the `order(µ)=∞` (loxodromic/cusped) stratum** (B198/V191).

| m \ o | 3 | 4 | 5 | 8 |
|---|---|---|---|---|
| **1** | 4 (s−) | 3 (s+) | 2 (s+) | 3 (s±) |
| **2** | 4 (s−) | 2 (s+) | — | 2 (s±) |
| **3** | (deg) | 3 (s+) | — | — |

`exps`: o=3,n=4 {1,1,ω,ω²}; o=4,n=3 {1,i,−i}; o=5,n=5 {ζ₅ʲ}; o=8,n=4 {ζ₈^{1,3,5,7}}. Higher-m cells (m≥4 at o=3,4) have
**no loxodromic reps** (irreducibles exist but are all finite-order-µ Dehn-filling, or the cell is `o∣m` degenerate) — the
geometric exponent is a **low-m phenomenon**. Tiers: SL3 cells `[exact]` (Q(ω)/Q(i)); SL5 o5 `[num, high-precision certified
~23 digits]`; the rest `[num, ≥2 seeds]`.

## Result A — NO closed-form law `k(o,m)`; only the sign survives

No single-valued `k(o,m)` (or `k(o,m,gcd)`, or `k(A^m-spectrum)`) reproduces the table. **Three decisive refuters**
(the o=4/o=8 collision and the non-monotonicity were *fully* re-derived by CC this session; the A^m-spectrum *matrix
identity* was re-derived by CC — its `k`-values are from the workflow grid):

1. **The o=4 / o=8 collision.** Both give `k=3` at m=1 on the µ-infinite stratum (my grid: `{3:8}` and `{3:8}`). The
   shared invariant is the **effective/projective order** `eff_o` = order of the eigenvalue-**ratio** group of A
   (`eff_o(o=4)=eff_o(o=8)=4`, verified). This **kills `k=7−o`, every `f(o)`, and all gcd-rules** — and also kills the
   `k=7−eff_o` candidate, which **misses the silver cell** m=2 o=4 (predicts 3, actual 2).
2. **The A^m-spectrum collision.** `A²` (o=4 {1,i,−i}) `= A³` (o=6 {1,ζ₆,ζ₆⁵}) `= diag(1,−1,−1)` **exactly** (verified), yet
   `k=2` vs `k=1`. So **no pure-`A^m`-spectral / `order(A^m)` law** can exist.
3. **Non-monotonicity.** The o=4 column is `k=(3,2,3)` over m=(1,2,3) — defeating every affine / 2-parameter law. A brute-force
   search found **zero** affine integer fits over `{m,o,n,gcd,o/gcd,m/gcd,o−m,o·m,o²,m+o}` at 1–3 features.

**The only surviving closed form is the sign:** `s=(−1)ⁿ⁻¹` (exact on every committed cell: n=3→+1, n=4→−1, n=5→+1) — but
**not robust off-grid** (it splits +1/−1 at m=1 o=8 n=4). The exponent itself is the **structural invariant**
`k = min{ j≥1 : [A,B]·µ⁻ʲ is scalar on the order(µ)=∞ component }` = the integer slope of the **metallic A-polynomial**
(`L=s·Mᵏ`, the B67/Cooper–Long cusp slope generalized to `φ_m`). **order-not-rank survives; degree=rank (`k=n`) is REFUTED
at SL5 o5 (`k=2≠5`).** A closed-form derivation is `[NEEDS-SPECIALIST]` — the law question is answered *negatively* on
maximal computed evidence (the (C) guardrail: this is "no closed form found by exhaustive search + proven collisions," and the
collisions are *proofs* that no `k(o,m)`/`k(A^m-spec)` exists, not merely "none found").

## Result B — the clean exponent is a SUBLOCUS, not the full component (corrects B198)

**Verify-don't-trust correction, confirmed two independent ways.** At SL(5) o=5 the rigid matrix identity `[A,B]=µ²` holds
only on a **dim-2 sublocus** of the dim-4 loxodromic component — **~1% of irreducible loxodromic reps** (this session's grid:
**8/887 = 0.9%**; the workflow's independent run: **24/3486 = 0.7%**). B198/V190's "305/305 unanimous `k=2` on the geometric
component" was an **`err<1e-6` filter-selection artifact** — the filter *selects* the sublocus. `µ` and `[A,B]` always commute
(peripheral), but `eig(L)=eig(µ)^k` is a **fixed integer only on the distinguished rigid sublocus** (which contains the complete
cusped rep), **not** on generic loxodromic reps (the other ~99% satisfy no fixed exponent). At SL(3) the identity *does* hold
on the whole component (o=4: 200/200=100%; o=3: 84.7%); **the sublocus phenomenon emerges with rank** (SL3 ~100% → SL5 ~1%).
Honest restatement: *"the SL(5) o=5 m=1 exponent is `k=2` at the complete cusped rep / on the rigid sublocus,"* not "on the
geometric component." This aligns with Falbel's n=3 **component-inversion** (the tidy `L³=M` lives on the Dehn-filling
components; the geometric component carries a 141-term non-tidy relation). **B198 FINDINGS corrected in place; the `k=2`
*value* stands (where the identity holds), only the *scope* is down-tiered.**

**The sublocus is GENUINE, not a numerical artifact (CC re-verification, prompted by an owner "U sure?").** Among **60**
loxodromic irreducible reps lying *exactly* on the variety (median relresid **2.2e-13**), **59 are NOT clean** — their
best-`k` exponent error is **O(1)** (min 1.2e-6, **median 7.67**, max 7910), while only **1** is clean (k=2). The ratio
`err / (relresid·cond(t))` has median **8.8×10¹¹ ≫ 1**, so the O(1) error is *real structure* — generic loxodromic reps
satisfy **no** integer exponent — not an `err`-threshold filtering numerically-under-resolved-but-genuine reps. So the clean
exponent is a real **codim-2 rigid sublocus**, confirming the correction. (`sublocus_genuine.py`.)

## Result C — Goal B: SL(5) exact-symbolic EXHAUSTED (4 routes) → a sharp NEEDS-SPECIALIST boundary

No route completed an exact proof; the value `[A,B]=+µ²` (k=2, c=+1) stands at `[num, high-precision certified]`. **The wall is
now named precisely** (per the owner directive: compute to exhaustion, then mark the exact boundary):

- **R2 (cleanest boundary):** the **first degrevlex Gröbner basis at 25 variables** (the SL5 o5 bundle ideal, 26 generators)
  **does not terminate within 600s, over ℚ(ζ₅) *or* F_p** (cyclotomic ~14× costlier). Dimension / saturation /
  `minimal_associated_primes` / `variety(QQbar)` all presuppose this GB → all unreached. *(Operational: `signal.SIGALRM` does
  not interrupt Singular's C kernel — only an OS-level process kill enforces a deadline.)*
- **R3 (F_p slice, p=101, 21 gauge-fixed vars):** linear elimination cheaply removes 21→11 vars (<1s), but the residual
  quadratic+det GB walls across **six** formulations (direct, saturation, two eliminations, slimgb, generic-slice-membership)
  all at the 600s cap.
- **R1 (rank-stratification, 10-var residual):** decomposition of the dim-4 geometric component stalls (dimension over ℚ(ζ₅)
  >300s; `minimal_associated_primes` over F₁₀₁ killed at 400s); F_p Newton has an **empty basin** (0 hits in 1500–4000 seeds) →
  no exact F_p point could be produced.
- **R4 (hand-reduction, B89 template):** **two** independent walls — (a) **non-rationality**: the k=2 locus is a codim-2
  subvariety that is **not rationally parametrizable** (high-precision monodromy returns to a different sheet, return-distance
  3.5e-2…7e-2), so no B89-style explicit rational family exists; (b) a GB wall on the k2-locus ideal (55 gens) >420s.
- **METHOD VALIDATED `[exact-mod-p]`:** the same F_p / ℚ(ζ) engines correctly reproduce **every** SL(3) cell (o=3→k=4 at
  p=31,43; o=4→k=3,c=1 at p=41,101) and prove **SL(4) o=4 EMPTY** (dim=−1), confirming B157 — so the SL(5) outcome is a
  **genuine combinatorial compute wall, not a bug.** NEEDS-SPECIALIST routes: a dedicated FGLM/F4 (Magma / msolve), the
  *unsaturated* ideal decomposition (avoid the saturation blow-up), or the from-first-principles metallic A-polynomial
  (the B67→B89 program generalized to `φ_m`, n=5). This is the standing open prize.

## Novelty (deep-research, 19 primary sources; adversarial)

- **R1** (the SL(n) figure-eight A-poly family `L=(−1)ⁿ⁻¹Mⁿ` + the metallic m≥2 generalization): **PARTIALLY-KNOWN.** n=2
  classical (Cooper–Long); n=3 fully known (Falbel–Guilloux–Koseleff–Rouillier–Thistlethwaite 1412.4711; Heusener–Muñoz–Porti
  1505.04451). **No source gives a uniform higher-n (n≥4) family or any metallic generalization** → APPEARS-NOVEL there.
  Unchecked: Zickert 1405.0025 (SL(n) A-variety, non-unipotent) — the key un-examined source.
- **R2** (the `order(µ)=∞` cusped-stratum reading): **PARTIALLY-KNOWN.** The valuation / boundary-slope (Newton-polygon)
  picture is standard (CCGLS 1994; Bénard–Florens–Rodau 2103.14151) but **rank-2 only**; the *meridian-eigenvalue-order*
  framing is distinct (residual: is it genuinely distinct or a re-description of the ideal-point picture?).
- **R3** (order-determined slope, no closed `k(o,m)`): **APPEARS-NOVEL.** Tunnel-number-one rank-2 prior art is solid
  (Baker–Petersen 1211.4479) but rank-2 only; metallic `m≥2` is **not** tunnel-number-one (figure-eight is the unique overlap),
  so it sits outside that theory. Caveat: "no contradicting prior art found," not "proven novel."
- **Component-inversion wrinkle** (specialist must confirm): a specialist should check whether `[A,B]=s·µ^k` with clean
  integer `k` holds on the **geometric** component for n≥3, vs only on orbifold/Dehn-filling strata — Result B already shows it
  is sublocus-only at n=5.

## Reproduction

- `python geom_grid.py` (pyenv) — the P1 geometric-stratum engine; smoke test reproduces o=4→k=3, o=3→k=4 (`ALL CHECKS PASS`).
- `python grid_driver.py out.json` (pyenv) — the full admissible-cell grid (slow: SL5 cells ~1h; the data is in `grid_summary.json`).
- `python ../B198_metallic_exponent_CAS/meridian_order.py --grid` — the o=4/o=8 collision (both `{3:8}` on the µ-∞ stratum).
- `sage-python ../B198_metallic_exponent_CAS/sage_groebner.py` — the EXACT SL(3) cells (o=3→4 over Q(ω); o=4→3 over Q(i)).
- `workflow_result.json` — the full multi-agent record (verify verdicts, law candidates+judges, Goal-B boundaries, novelty).
- `grid_summary.json` — the per-cell table incl. the **clean-fraction** (the sublocus evidence: m1_o5_n5 0.9% vs m1_o4_n3 100%).
- Fast lock: `tests/test_b199_metallic_exponent_law.py` (the deterministic refuters + the sublocus summary).
