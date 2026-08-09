# B1007 — the instrument already existed, and this arc's first draft was wrong about the cost

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** instruments. Gate 5 untouched.

**Verdict: NEGATIVE.** This arc set out to build an arbitrary-precision Maass solver because
B1006 named *more digits* as the value layer's bottleneck. **It built one that does not work,
claimed a cost overturn that is false, and then found that a working one has been on main since
B922.** All three are recorded here, because the third is the only one worth keeping.

---

## 1. THE HEADLINE, AND IT IS A CORRECTION OF THIS ARC'S OWN FIRST DRAFT

**A working, sealed, arb-based 25-digit solver is already in the repository:**

> **`frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py`** — *"conformant to sealed prereg
> v3 (`169e9042`)"*, **the same seal hash B922 names.** This is the script behind the 58.1-hour
> run. It is on main. It was on main before this arc started.

**This seat wrote a new solver without reading it.** That is the **ninth instance** of the
same failure this session: *grepping claims instead of reading code.* B1006's cell D duplicated
B922 the same way five hours earlier.

## 2. THE COST CLAIM IS WITHDRAWN — B798 STANDS, INCLUDING ITS COST ESTIMATE

The first draft of this file claimed *"B798's cost estimate was priced against arithmetic that is
not what arb does."* **That is false, and B798's own text refutes it in the same sentence it makes
the estimate in:**

> *"…**4–5 orders of magnitude** beyond the certified run, **on a different numerical stack
> (arb/mpmath Bessel, mp linear algebra)**…"* — `B798_falsifier_power_box/FINDINGS.md`

**B798 named arb.** It priced an arb instrument, and included arb's overhead as a factor of 10–100.
And the 58.1-hour run **used flint/arb**: `flint.ctx.prec = int((DIGITS+45)*3.33)+250`,
`K_ir(r,x) = flint.acb(x).bessel_k(i·r)`, an `flint.acb_mat` LU solve, at **n ≈ 1300**.

**Where the error was, precisely.** B798's cost model has two terms and **this seat used only one**:

| B798's term | what it says | what this arc did |
|---|---|---|
| **modes scale ~linearly with precision** | 900 modes → **11 250** at 100 digits | **held the mode count FIXED** at 300–1000 |
| dense solve is **cubic in modes** | **1953×** at 100 digits | measured one **200×200** solve |
| arb overhead 10–100× | — | measured, correctly, as **< 2×** per operation |

**The per-operation timings are correct as measurements and do not support the conclusion drawn
from them.** Precision is cheap *per operation*; **the cost is that higher precision demands more
modes, and the solve is cubic in modes.** Varying `dps` at fixed `M` measures the one term that was
never the problem.

> **B798's law stands. B798's cost estimate stands. Nothing in this arc overturns either.**

## 3. THE SOLVER FAILED, AND THE WORKING SOURCE DOCUMENTS EVERY FIX

The gate: **recover B922's r = 4.9000853730625213014795758 or claim nothing.** It does not —
M=40 gives g ~ **10²⁶**, M=80 is smooth with no sign change. **Five differences from the working
solver, four of them fixed in its source with the reason written in a comment:**

1. **No column equilibration.** The working code divides each column by |Y·K(2π|μ|Y)|, and says
   why: *"the truncation-edge dynamic range (~1e-19 at shakedown, **~1e-32 at the real run**)
   collapses to O(1), **which arb's certified LU requires at n ≳ 1300**."* **The 10²⁶ is exactly
   this, and the fix was already written down.** *(B792's float64 scanner does the same thing —
   `svd(V / cn[None,:])` — and says so in its docstring.)*
2. **No risen-point filter.** The working code keeps a point only `if mv and ts > Y*(1+1e-20)`.
   A point that does not move gives f(z,Y) = f(z,Y) — **an identically zero row.** This seat
   filtered nothing, so the system was singular by construction.
3. **Modes chosen by COUNT, not RADIUS.** The working code takes all μ with |μ| ≤ R_cut where
   R_cut = (πr/2 + margin)/(2πY) — the truncation is set by where K_{ir} dies. Picking "the first
   M by |μ|" is not the same set and has no convergence argument behind it.
4. **Y = 0.28 against the sealed Y = 0.75.**
5. **The wrong indicator for the job — the conceptual error.** The held-out-row residual g(r) is
   what the working code uses, but only for **local refinement inside an already-bracketed root**
   (*"damped bracketed secant"*). **Detection** is done by **σ_min of the column-normalized V(r)**
   in the float64 scanner, which *dips* at an eigenvalue. **This seat used a refinement indicator
   to search**, which is why scanning found no sign change: **g(r) is not built to have one.**

## 4. WHAT ACTUALLY SURVIVES

- **The exact ℤ[ω] geometry port** (91 moves, τ = 2√3 i to ±4.8e-40, exact dual lattice, working
  pullback) is correct — **and redundant**: `branch_cell9_rung1_v2.py` already has `_mpgen`/
  `_mpmoves`/`mp_reduce` doing the same job in mpmath, and already drives arb from it.
- **One genuinely new observation, kept because it is not in the working source:** since
  1/(2√3) ≈ 0.289, ordering Λ\* by |μ| gives **only m ∈ {−1,0,1} even at M = 30**. This is a
  consequence of choosing modes by count, and it is another reason not to.

## Honest standing

**The programme can reproduce λ₂ — it has been able to since B922, with the code on main.** What
this arc contributes is a corrected cost picture (**B798 was right**), a precise diff against the
working instrument for anyone who touches it next, and one more datum on the failure mode that has
now cost this session nine arcs: **read the code before rebuilding it.**

**No number produced by `arb_maass.py` enters any ledger, and the file is kept only as the record
of the failed attempt.**

---

**Verdict: NEGATIVE. The cost overturn is withdrawn; B798 stands; the instrument already existed.**
