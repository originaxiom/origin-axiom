# B1051 — B0–B99 closed: the fixed line is Dickson, and two siblings the instrument could not see

**Status: banked (frontier). The other ten rows of the band B1050 opened. Consolidation only; every
statement is a banked arc's, re-verified symbolically before restoring. Firewalled; nothing to
`CLAIMS.md`; Gate 5 untouched; zero anchors.**

---

## The sharpest result is not a restoration

> ### Two of the ten rows are the **same law** as rows already on `LAW_MAP`, and `law-siblings` could see neither.

**B27 is B1038's tower law at SL(3).** Its stated Jacobian characteristic polynomial

    (t−1)(t+1)(t²−4t−1)(t²−3t+1)(t²+t−1)

**is**, verified **symbolically — polynomial against polynomial, not root-by-root numerics — the
characteristic polynomial of `Sym³ ⊕ Sym² ⊕ trivial` of the half-step eigenvalues `{φ, −1/φ}`.**
And `t²−3t+1`, the golden charpoly of `A = LR`, is a factor. **B33 — already cited on that row —
states exactly this.** Cited on the tower row; not restored as anything new.

**B83 is B77's signed law in A-polynomial language.** B77's `[A,B] = (−1)^{n−1}µⁿ` is already on the
metallic exponent row; B83's `L = (−1)^{n−1}Mⁿ` is, in **its own words**, *"the peripheral eigenvalue
shadow"* of it — same sign, same exponent, **a plane curve instead of a matrix identity** — and it
contributes the **SL(4) member `L = −M⁴`, new**. Cited there with its **HIGH-PRECISION NUMERICAL**
tier stated.

### A third miss mode, and the fix overshot before it landed

The registry recorded two modes. **B485** was *one law in two vocabularies* (missed). **B876** was
*two laws in one vocabulary* (falsely matched). **These are one law at a different OBJECT** — a
fingerprint is authored in the *restored* arc's words, so a sibling stating the same law about a
plane curve rather than a matrix identity, or at SL(3) rather than as `Sym` bands, walks straight
past it.

> **The first widening overshot, and it is recorded rather than quietly corrected.** Adding bare
> `A-polynomial|Dehn-filling` took the sweep from 3 candidates to **12, nine untriaged, six of them
> false** — that vocabulary is **ambient** in this corpus, not this law's signature. Narrowed to the
> law's **shape** and **tested in both directions**: both true positives survive, all six false ones
> drop, and both directions are locked.
>
> **Narrowing after seeing results is how `E38` begins, so the distinction is stated:** `E38` is
> narrowing to make a *failing* check pass. This removes *false positives* while holding the true
> positives fixed as the test.

---

## The three restorations

### THE METALLIC FIXED LINE IS DICKSON, EXACTLY, OVER ℤ[m] — B55 · B57 · B63

The fixed-line spectra factor over `ℤ[m]` into **Dickson** pieces — characteristic polynomials of
powers of the seed `M = [[m,1],[1,0]]` — and **the shape of that factorisation does not depend on `m`
at all; only the coefficients move.**

- **B55, at `c = 1`, for all `m`:** the **symmetric** sector is **mod 4** — `Φ₆` at `m ≡ 1,3`, `Φ₄`
  at `m ≡ 2`, and a **parabolic `(t−1)³(t+1)` degeneration at `m ≡ 0`** — while the **antisymmetric**
  sector is universally `(t−1)(t+1)(t²−mt−1)`. **⚠ B55's own correction travels: *"odd → Φ₆, even →
  Φ₄"* is WRONG.**
- **B63, at SL(4), symbolically in `m`:** `char(M⁻¹)·char(M)·char(M²)·char(M³)·char(M⁴)·char(−M²)·(t−1)²(t+1)`,
  **total degree 15 = dim 𝔰𝔩(4)** (checked), `L_k(m) = tr(Mᵏ)`, and the M-power set, sign sector and
  parity block all **`m`-independent**.
- **B57 makes splitting decidable:** the antisymmetric quartic splits over ℤ **iff `D = A²−4(C+2)` is
  a perfect square with `A+√D` even**; `c = 1` and `c = 3` split for **every** `m`.

> **The cross-link this arc found, and it is why these are one row rather than three:** B57's
> universal `c = 3` splitting is **`(t²+mt−1)(t²−L₃(m)t−1)` with `L₃(m) = m³+3m = tr(M³)`** —
> *B63's Dickson trace*. The splitting classification and the factorisation law are **the same
> polynomials**.

### THE TWO-BLOCK OBSTRUCTION IS RANK-1 — B70

The barrier that stopped **every** single-index route to the `a_d` trace-ring proof is **one bilinear
coupling**: the non-separable content of `tr(AᵃBAᵇB)` on the traceless `𝔰𝔩(n)` tangent is the single
term **`a·b·tr(X²)`**, pinned exactly to the **`e₂ = tr(Λ²A)`** coordinate. That is *why* the
cotangent, `Sym²ᵏ`, pinv-limit and nilpotent-gate routes all stalled in the same place — none can
produce even one `a·b` term. **The consequence is a bound, not a defeat:** closure needs **one**
two-index generator, not an unbounded multi-block algebra.

**Re-run end-to-end against the live tree before restoring** — exact `sympy`, **14m09s** — and all three cases returned **RANK-1** with the `e₂`-Hessian identity confirmed. Not carried by citation.

**⚠ The rider B70 wrote against itself travels: the bidegree-(3,3) bound rests on the UNIPOTENT
fixed-line object, not the generic `ε`-series** — on the generic tangent the content **grows
unbounded** with `ε`-order. *A reader who drops that has a false theorem.*

### THE CUSP k-SET IS THE QUANTUM-GROUP LEVEL SET — B76

B69's cusp-torsion law puts the metallic-`m` cusps at `x = 2cos(π/k)`, `k ∈ {3,…,m+2}`,
`k ≡ m (mod 2)` — **exactly the SU(2) quantum-group level set**, since `2cos(π/k) = [2]_q` at the
primitive `2k`-th root `q = e^{iπ/k}`, the `SU(2)_{k−2}` special value. The family's cusps **walk up
the WZW levels in steps of two**.

**Two fences travel.** The categorical *"anyonic TQFT"* reading is **`SPECULATIVE-ANALOGY`** and is
**not** restored — only the number/level correspondence is. And an **`E1` collision is declared
rather than left to bite: this `k` is the CUSP index, not the peripheral exponent `k` in
`[A,B] = ±µᵏ`.** Two rows on `LAW_MAP` use `k` for two things; both now say so.

---

## The declines, and the correction that had to survive one

**B59 · B60 · B61 — DECLINE.** B59 is superseded in substance by B63's symbolic form; **B61's own
words are *"high-precision numerics, not a proof"***, with 2 of 24 modes unresolved.

> **But B61 shows B60's *"SL(5) conditioning wall"* was never a wall.** The 24-word forward-only set
> is **rank 23** — one genuine null direction — and double precision read it as a small-but-nonzero
> singular value, reporting `cond ~ 1e11`. ***"The barrier was a coordinate-system defect, not a
> precision limit."*** **Declining B60 silently would have left a phantom wall on the record**, so
> the correction is written into the ledger row explicitly.

## Registered, not fixed

**B55 and B57 have `probe.py` and no test lock at all** — two arcs with `PRODUCES-PROOF-MODULE`
content and zero lock coverage. Noted here; not added to L165, whose subject is *absent* reproducers,
and these are present.

---

## The band, closed

**16 rows = 6 restored as the wall (B1050) + 5 restored here + 2 retired as siblings + 3 declined.**

**Campaign step 6 is satisfied for B0–B99** — the second band to reach it, and the first whose
closure was measured against the bodies from the start rather than from a keyword map. Measured with
**B1050 and later excluded** (E37).

**Provenance.** `verify.py` (57 checks) · `tests/test_b1051_band_closed.py` (9 locks) ·
bodies read: B27 B55 B57 B59 B60 B61 B63 B70 B76 B83 · `DEBT_LEDGER` §B0–B99 · three new `LAW_MAP`
rows and two sibling citations · `LAW_SIBLINGS.md` (three triaged, the third miss mode recorded) ·
`scripts/checks/law_siblings.py` (two fingerprints widened, then narrowed).
