# B1403 — L208's SECOND HALF, CLOSED: B1002's gcd and `gcd(m,15)` have DISJOINT DOMAINS

**L208 asked** whether B1002's other gcd — `gcd(cusp-order conductor, shadow modulus)`, which is
`1` for golden (isomorphism) and `2` for silver (ramified) — relates to B1349's `gcd(m,15)`.

> ### It cannot. The two are defined on disjoint parts of the family, and disjoint **exactly where it matters**.

## 1. The conductor is a Kronecker–Weber object, so it needs an ABELIAN cusp field

B1002's gcd is built from B675's **cusp-order conductor**. A conductor exists only for an **abelian**
field. B675 banks the law as **two instances** and reports where it stops:

> *"The bronze cusp shape's `u = y²` satisfies an IRREDUCIBLE quartic with Galois group **S₄** —
> NON-ABELIAN — so `[ℚ(τ):ℚ] = 8` embeds in **NO** cyclotomic Coxeter-plane field
> (Kronecker–Weber): H-CUSP predicts no stage family at any rank hears the bronze."* — **a DEAF
> object.**

## 2. Verified independently here: the family leaves the quadratic world exactly at bronze

`verification/b1403_cusp_field_quadratic.py`, on the punctured-torus bundles `b++ RᵐLᵐ`, at SnapPy's
high precision. No LLL needed — if `τ² + bτ + c = 0` with `b, c ∈ ℚ` then the imaginary part forces
`b = −Im(τ²)/Im(τ)` and the real part forces `c`, so both are **determined** and the only question is
whether they are rational (tested by PSLQ at full precision).

| m | manifold | cusp shape `τ` | quadratic? | minimal polynomial | field |
|---|---|---|---|---|---|
| **1** golden | `b++RL` | `1 + 0.2886751…i` | **YES** | `τ² − 2τ + 13/12` | disc `−1/3` ⟹ **ℚ(√−3)** |
| **2** silver | `b++RRLL` | `0.5i` | **YES** | `τ² + 1/4` | disc `−1` ⟹ **ℚ(i)** |
| 3 bronze | `b++RRRLLL` | `0.6018385…i` | **NO** | — | — |
| 4 – 8 | — | — | **NO** | — | — |

**B675's two banked fields are reproduced from the cusp shapes independently** — `ℚ(√−3)` for golden,
`ℚ(i)` for silver — and the family is **not quadratic from m = 3 onward**, which is exactly where
B675 found `S₄`.

*(Scope, stated precisely: quadratic ⟹ abelian, so m = 1, 2 certainly admit a conductor. Non-quadratic
does **not** by itself prove non-abelian — abelian fields of higher degree exist. For **bronze** the
non-abelianness is B675's `S₄` computation, **cited, not re-derived here**; for m = 4..8 this arc
establishes only "not quadratic".)*

## 3. THE ANSWER — disjoint domains, and disjoint at the decisive place

| | where it is defined | which branch |
|---|---|---|
| **B1002's gcd** | `m = 1` and `m = 2` only | `gcd(1,15) = gcd(2,15) = 1` ⟹ **both are UNITS of ℤ/15 ⟹ both on BRANCH B** |
| **`gcd(m,15)`'s content** | `m ∈ {3,5,6,9,10,12,15}` | **BRANCH A** — where the conductor fails to exist at the very first member |

> **B1002's gcd lives entirely on the dead branch. `gcd(m,15)` discriminates only on the live one.
> There is no `m` at which both are informative, so no relation between them can be stated —
> not "unknown", but *unaskable* as posed.**

**And the failure is structural, not incidental.** The conductor needs an abelian cusp field; the
metallic family is abelian only at its two smallest members. B675 called it a *"two-instance law"*
in its own words — this arc supplies the reason that it can never be more than two: **the family
leaves the abelian world at bronze and does not return within the computed range.**

## 4. What this does and does not settle

**Closes** L208's second half — with a reason, not a shrug. Together with B1402 (`gcd(m,15)`
decomposes into B996's cut plus a silent 5-part), **L208 is now fully answered**: two of the three
cuts are one structure, and the third quantity cannot be compared to them at all.

**Does not** touch B675 or B1002, both of which are correct as stated; this only maps their domain.
**Does not** reach `CLAIMS.md`, F2 or Gate 5, and no value is compared to any measurement.

**Leaves open** (not investigated, not guessed): whether the cusp field is abelian for any `m ≥ 4` —
this arc shows only *not quadratic*. If some higher `m` were abelian, B1002's gcd would be defined
there and the question could be reopened **at that m**; nothing here suggests it is.

## 5. THREE BUGS OF MINE IN ONE COMPUTATION, all the same class

Recorded because the pattern is now unmistakable — **every one was a float used where exactness was
required**, and only the last was caught by a control:

1. `Fraction(float(x)).limit_denominator(...)` compared at `1e-30` — `float()` truncates at `1e-16`,
   so **no rational with a non-dyadic denominator could ever pass**. The m = 1 answer `13/12` is
   exactly such a rational.
2. **The controls missed it**, because they used only `0, 1, 4, −1` — all exactly representable in
   binary. **A control that does not vary the thing which can break is not a control** (E67's shape).
   Fixed by adding `1 + √−3/6`, whose `c = 13/12` is non-dyadic — and it failed immediately.
3. The cusp shapes were read through Python `complex()` — **double precision** — and then tested at
   `1e-40`, which PSLQ can never satisfy. Fixed with SnapPy's `high_precision()`.

4. And a **fourth**, in the test written to lock all this: the control value `13/12` was built at the
   **ambient** precision before being handed to the full-precision routine, so **the control failed
   for exactly the reason it exists to catch**. Fixed by constructing the control values inside the
   precision block.
5. A fifth, adjacent: `mp.pslq` computes `tol = to_fixed(tol, prec)` and then asserts it is non-zero,
   so a low *ambient* `mp.mp.dps` silently turns a `1e-40` tolerance into `0` and the call dies. The
   script worked and the test did not, for no reason visible in either. **Global numeric state is not
   a contract** — the precision is now set explicitly with `mp.workdps` at every entry point.

**That is the third, fourth and fifth float-before-exact-test failure this session** (after E75's two
mechanisms in B1401 addendum 2). The rule, restated: *when a high-precision test returns "no
relation", suspect the precision of the **input** before believing the answer* — and build the
control's own values at the same precision as the thing under test, or the control tests nothing.
