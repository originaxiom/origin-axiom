# B198 — the B157 metallic-exponent wall, breached by computation (Sage in-env + gauge-fix)

**Date:** 2026-06-23. **Status:** the B157 "NEEDS-SPECIALIST / needs a real CAS" mark is **corrected**.
The m=1 metallic exponent is now computed at the previously-unreachable **SL(5) o=5** cell:
**`[A,B] = +µ²`, k=2, certified to ~23 digits.** Standalone low-dimensional-topology / character-variety
result; **no Origin-core claim, no physics**; proven core P1–P16 untouched; nothing promotes to
`../../CLAIMS.md`. Ledger V190. Reproducers in this folder.

**Provenance.** A direct test of the standing "we compute before deferring to a specialist" directive and
the new `GOVERNANCE.md` §6.1 **(C)** guardrail (don't upgrade "our probes can't reach it" into
"it's unreachable"). The wall-breach was our own representation-variety computation, not an adopted
cross-chat insight. Every load-bearing value re-derived two independent ways (verify-don't-trust); a first
high-precision certificate **failed** (a seed-selection bug in the certificate script), was caught, fixed,
and now converges cleanly — the failure and its fix are part of the record.

## What the wall was, and why it wasn't one

B157 marked the SL(5)/o≥5 cells NEEDS-SPECIALIST on two findings, **both tooling/diagnosis, not math**:

1. *"needs a real CAS (Singular / Macaulay2 / Sage)."* — **Sage is installed in-environment**
   (`command -v sage`). The mark was written without checking. (Cheap to verify; it was the whole premise.)
2. *"Newton fails at SL(4)/SL(5)."* — The failure was **gauge-induced Jacobian rank-deficiency**: the
   diagonal torus that commutes with `A=diag` gives a whole *orbit* of solutions, not an isolated point,
   so the solver's Jacobian is rank-deficient by the gauge dimension and it wanders/diverges. **Gauge-fixing**
   (pin the superdiagonal `t[i,i+1]=1`) removes the null space and Newton converges. For m=1 only `t` is
   unknown (`B = A⁻²tAt⁻¹`), so the SL(5) system is 25 variables, not 50.

## Result — SL(5) o=5, m=1: `k = 2` (certified)

`[A,B] = +µ²` (`mu = A⁻¹t`; sign `s=+1`, scalar `c=1`). **Three independent confirmations:**

- **gauge-fixed single-`t` Newton:** 9 irreducible reps (Burnside dim 25 = full), 3 RNG seeds, all `(s,k)=(1,2)`.
- **gauge-fixed `(B,t)` Newton** (different code path, 50 vars): 3 irreducible reps, all `(1,2)`.
- **mpmath certificate (dps=60):** as the relation residual falls `4.6e-14 → 1e-47`, `‖[A,B]−µ²‖` falls in
  **lockstep** `1.7e-7 → 1.5e-23` (this *tracking* is what proves `[A,B]=µ²` is an **exact consequence on the
  component**, not a float64 coincidence). `[A,B]·µ⁻² = I` to 23 digits, `c=+1`; neighbours excluded
  (`‖[A,B]−µ¹‖=3.9`, `‖[A,B]−µ³‖=8.2`); `‖µ−t‖=2.19` throughout (non-degenerate, `A^m≠I`, no component jump).

`k = 2 = 7−o = 4−m(o−3)` at m=1: this **extends the figure-eight (m=1) row to o=5**, previously unreachable.
Note `k=2 ≠ rank 5` — **reinforces** B157's "order-determined, not degree=rank" (it is *not* a counterexample).

**TIER: `[num, high-precision certified]`** — effectively certain (12 reps, 2 independent solvers, 23-digit
certificate). The **exact symbolic proof** over `ℚ(ζ₅)` (primary decomposition, 25 vars) is **not** done — see
the residual. This is not `[proved]`.

## Validation — the method reproduces every known cell

- **Sage/Singular EXACT** (ideal membership over `ℚ(ζ_o)`, read on the geometric component):
  **SL3 o3 → k=4**, **SL3 o4 → k=3** — the Gröbner computation sympy could **not** finish in B157.
  Reducible components correctly yield no finite `k`. `[exact]`
- **gauge-Newton:** SL3 o3→4 (1194 reps), SL3 o4→3 (1200 reps), SL3 m=2 o4→2, SL3 m=2 o3→4 — all match
  B157/B89/B71.

## New — the existence-boundary refines the *refuted* formula

B157 refuted `k = 4 − m(o−3)` (the bronze m=3 row breaks it). The SL(5) data **sharpens** the picture for
m∈{1,2}:

| m | o=3 | o=4 | o=5 |
|---|---|---|---|
| **m=1** | 4 | 3 | **2 (NEW)** |  → `k = 7−o`, confirmed to o=5 |
| **m=2** | 4 | 2 | **none (NEW)** | → `k = 10−2o`; at o=5 formula gives `k=0` (trivial longitude) and indeed **no irreducible rep exists** |

At o≤5 this *looked* like `k=4−m(o−3)` governing m∈{1,2} in value and existence-boundary. **That reading was an
over-reach on too small an `o` range — CORRECTED below (the grid follow-up).** What is solid: the m=1 row
`(o=3,4,5)→(4,3,2)`, the m=2 row `(o=3,4)→(4,2)`, m=3 o=4→3 (re-verified, certified method), and m=2 o=5 has no
irreducible rep — all on the geometric component.

## Grid follow-up + CORRECTION (2026-06-23) — the meridian-order refinement; no simple closed form

Extending the grid to o=8 and re-checking with the **meridian order** (`order(µ)`, `µ=A⁻ᵐt`) **refutes the two
secondary claims above** (verify-don't-trust + the (K) guardrail, applied to this frontier's own first draft):

1. **The exponent must be read on the geometric / cusped component — where `µ` has INFINITE order (loxodromic).**
   The bundle variety *also* contains **finite-order-`µ` (Dehn-filling / orbifold) reps**, where `[A,B]=µ^k` holds
   only **mod `order(µ)`** and which are **not** the canonical cusp. Example: SL(4) o=8 m=1 has a genuine
   irreducible branch with `order(µ)=20` (µ-eigenvalues are 20th roots of unity) giving a spurious "k=8"; the
   **geometric** branch there (µ infinite order) gives **k=3**. Including the finite-order-µ reps produced the
   illusory "component-dependent / multi-exponent" readings. *(The shipped certified SL(5) o=5 rep is confirmed on
   the geometric component: `µ` loxodromic, `|eig|=2.09,1.0,1.62,0.62,0.48`, infinite order — so the **k=2 headline
   stands, strengthened**. `meridian_order.py`, and the test now checks it.)*
2. **No simple single-valued `k(o,m)` law — even on the geometric component.** On the µ-infinite component,
   **o=4 m=1 and o=8 m=1 BOTH give k=3** (8/8 reps each). So `k=7−o` / `k=4−m(o−3)` and the **`gcd(m,o)` lead are
   REFUTED** (o=8 m=1: the formula predicts `k=−1` and *no* rep, but a geometric rep exists with `k=3`). The
   existence-boundary claim falls with it.

**Net:** the headline (the wall breach + SL(5) o=5 m=1 → k=2, geometric) is unchanged and strengthened; the
order-determined values on the geometric component are solid for the clean cells; but **the closed-form exponent
law does not reduce to a simple `k(o,m)`** — the right invariant is subtler (the variety stratifies by `order(µ)`,
and even the geometric stratum gives `o=4,8 → 3`). The closed form stays genuinely **NEEDS-SPECIALIST** — now with
the correct object identified (read `k` on the `order(µ)=∞` stratum). `meridian_order.py --grid` reproduces this.

## Grid sparsity

SL3 o5 `{1,ζ₅,ζ₅⁴}` and SL3 o6 `{1,ζ₆,ζ₆⁵}`: the bundle ideal is **nonempty** (Sage ideal dimension **3** —
reducible reps exist, e.g. direct sums) but contains **no irreducible reps** (gauge-Newton, many seeds × 3 RNG
yield 0; Burnside never reaches `n²`). So it is the *irreducible* locus that is empty, not the whole variety —
confirms B95/B157 order↔rank (o=5 needs n=5). `[ideal nonempty: exact (Sage dim=3); no-irreducible: num — a
rigorous proof needs the full decomposition showing every component reducible]`

## The residual — the wall MOVED, it did not vanish

The **exact symbolic `k` at SL(5)** — primary decomposition over `ℚ(ζ₅)` at 25 vars, or per-cell hand-reduction
for the o=5 spectrum — remains open. Sage primary decomposition stalls at **SL(4)** (16 vars) and the SL(5)
ideal-dimension is itself heavy. So we converted *"needs any CAS at all"* into *"needs exact decomposition at
≥16 vars / specialist algebra"* — genuine progress, not a solve. The **general closed form across all m** (the
`gcd(m,o)` anomaly) is the deeper open problem; **NEEDS-SPECIALIST for the proof, now on maximal computed
evidence.**

## Firewall

Standalone character-variety / low-dimensional-topology mathematics. No physics; nothing to `CLAIMS.md`;
P1–P16 untouched. The figure-eight A-polynomial connection (B67) is to a published knot invariant
(Cooper–Long), not a physical claim.

## Reproduction

- `gauge_newton.py` (**pyenv** `python`): the gauge-fixed Newton, validation cells + the SL(5) cells + sparsity.
- `sage_groebner.py` (**sage-python**): the EXACT SL(3) cells (ideal membership on the geometric component) +
  `dim` mode for rigorous existence/emptiness.
- `mp_certificate.py` (**pyenv** `python`, mpmath): the SL(5) o=5 high-precision certificate (the lockstep table).
- `meridian_order.py` (**pyenv**): the meridian-order refinement — the certified rep is loxodromic/infinite-order
  (geometric); `--grid` shows o=4,8 both → k=3 on the µ-infinite stratum (the CORRECTION to the secondary claims).
- `cert_sl5o5_rep.json`: a certified SL(5) o=5 rep (≈40-digit entries) loaded by `tests/test_b198_*`.
