# MEMO 183 — **THE QUANTUM A-POLYNOMIAL PRINTED FOR `m(5₂)` DOES NOT ANNIHILATE THE SERIES IT IS PRINTED TO ANNIHILATE**

**Date** 2026-09-08 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/park_ahat_erratum.py` · **Output** `outputs/park_ahat_erratum_out.txt`
**Gate 5** exact integer / `Fraction` arithmetic throughout. No measured value enters. Every
published series appears **only** as a comparison target for something computed first.

**Already-banked check (memo 153).** Terms searched: `quantum`, `a-polynomial`, `park`, `(32)`,
`m(5_2)`, `erratum`, `ahat`, `annihilate`, `f_3`, `defect`, `sigma(2,3,11)`. 108 corpus hits,
**0 settled arcs** matching ≥ 6 of 12. The claim is admissible as new.

---

## 0. The one-line statement

> ### `[Â_{m(5₂)} F⁺_{m(5₂)}]_{x^{7/2}} = q^{13}·f_0(q) ≠ 0`,
>
> with `Â` the quantum A-polynomial printed in Park, *"Large color R-matrix for knot complements
> and strange identities"*, arXiv:2004.02087v2, **eq (32), page 17**, and `f_0` **that same
> paper's** page-15 block. Checked on 23 nonzero coefficients out to `q^270`, exactly, in integer
> arithmetic. The paper's sentence immediately above eq (32) — *"one can numerically check that
> it is annihilated by the (unreduced) quantum A-polynomial given by (32)"* — is therefore
> **not satisfied by the polynomial as printed**.
>
> **And the erratum is not one dropped monomial.** Exactly five single-monomial repairs are
> consistent with the `x^{7/2}` equation; **all five are refuted** at `q^17` against
> `Ẑ(Σ(2,3,11))`, generated here independently of Park.

The three statements Park makes about `m(5₂)` — the closed forms for `f_0, f_1`; the
`ℚ(q)`-formulas for `f_2, f_3`; and eq (32) — **are mutually inconsistent**. The first two agree
with each other and with his printed series. Eq (32) is the one that disagrees.

---

## 1. Why this bench was looking

Memo 177 established, for the figure-eight, that `sup_{|p/r| < 4} c_eff = 1`, and addendum 4
gave the mechanism: `c_edge(K) = c_eff(1/Φ_K)` with `Φ_K` the colored-Jones tail — explicitly
**knot-by-knot**, so the ceiling of 1 has *"no support beyond this one knot"*. The named next
step was a second hyperbolic knot. `m(5₂)` is the cheapest one: non-amphichiral, `c = −1/16`
(memo 182), and Park prints both its `F⁺` blocks and its `Â`, so `F_K` is reachable by recursion
rather than by re-deriving the large-color R-matrix.

The recursion is what broke.

---

## 2. The controls, all fired

| | control | result |
|---|---|---|
| **C1** | Park's page-15 closed forms for `f_0, f_1` reproduce his printed `f_0, f_1` | PASSED (`f_0` to `O(q^35)`, `f_1` to `O(q^9)`, every coefficient including the zeros) |
| **C2** | Park's page-17 `ℚ(q)`-formulas for `f_2, f_3` reproduce his printed `f_2, f_3` | PASSED (`f_2` `q^{−1}..q^{10}`, `f_3` `q^{−1}..q^{11}`, exactly) |
| **C3** | the operator convention is **forced**, not chosen | PASSED — see §3 |
| **C4** | GM Thm 1.2 at `p/r = −1` reproduces **GM eq (12)** for `−Σ(2,3,7)` from `4₁`'s blocks | PASSED, `ε = −1`, all 12 printed coefficients |
| **C5** | the false theta reconstructed from Park's Table 3 reproduces all seven printed exponents **with signs** and his `O(q^61)` | PASSED, including the sign of the `q^61` term he only bounds |

C4 and C5 matter more than the rest: they are what make the refutation in §5 an argument about
Park's `Â` rather than about this bench's assembler.

**The transcription is not the problem.** Eq (32) was extracted from the source PDF twice by
independent routes (raw text stream and `pypdf` layout mode) and the two agree monomial for
monomial; the transcription in the certificate is that agreed text. `arxiv.org` is egress-blocked
from this lane, so the LaTeX source was not obtainable — recorded as a limit, not a hedge, since
two extractions of the same typeset page already agree.

---

## 3. The convention is forced, not chosen  `[C3]`

`Â = Σ_{i=0}^{4} a_i(x,q) ŷ^i` acting on `F⁺ = x^{1/2} Σ_j f_j x^j`. Five readings were tested;
the coefficient of `x^{n+1/2}` in each is `Σ_i Σ_d a_{i,d} q^{w(i,n,d)} f_{n−d}`:

| | `w(i,n,d)` | `n=0` | `n=1` | `n=2` |
|---|---|---|---|---|
| **A** | `i(n−d+½)`  (`ŷ` right, `ŷ:F(x)↦F(qx)`) | **row vanishes** | **row vanishes** | **δ = 0** |
| B | `i(n+½)`   (`ŷ` left) | row vanishes | δ ≠ 0 | δ ≠ 0 |
| C | `−i(n−d+½)` | δ ≠ 0 | δ ≠ 0 | δ ≠ 0 |
| D | `−i(n+½)` | δ ≠ 0 | δ ≠ 0 | δ ≠ 0 |
| E | `i(n−d)`  (no half-shift) | δ ≠ 0 | δ ≠ 0 | δ ≠ 0 |

Convention **A** alone does the two things Park's own text requires: the `x^{1/2}` and `x^{3/2}`
equations **vanish identically as operators** — which is exactly why `f_0` and `f_1` are free and
everything else is determined, his footnote 13 — and the `x^{5/2}` equation is then satisfied
**exactly** by his `f_2`. No other reading gets even the first of those. So the defect below
cannot be relocated by re-reading the operator ordering.

---

## 4. The defect, exactly

Under convention A, with `f_0, f_1, f_2, f_3` all taken from Park himself:

```
   [Ahat_printed F+]_{x^{1/2}}  = 0   (identically, as an operator)
   [Ahat_printed F+]_{x^{3/2}}  = 0   (identically, as an operator)
   [Ahat_printed F+]_{x^{5/2}}  = 0   (exactly, on the series)
   [Ahat_printed F+]_{x^{7/2}}  = q^13 * f_0(q)          <-- NOT ZERO
                                = -q^12 +q^13 -q^15 +q^18 -q^22 +q^27 -q^33 +q^40 - ...
```

Equivalently, **the recursion that eq (32) defines does not produce Park's own `f_3`**. Solving
the `x^{7/2}` equation for `f_3` gives

```
   f_3^{(recursion)} - f_3^{(Park, printed and rational-formula)}
       =  q^3 - q^4 + q^5 + q^6 + q^8 + q^9 + ...     ( = -q^13 f_0 / row_3(3) )
```

so the two first disagree at `q^3`, well inside the twelve coefficients Park prints. The
disagreement is with **both** of his statements of `f_3` at once, which agree with each other.

---

## 5. Exhaustive: it is not one dropped monomial

Adding a monomial `κ·q^{β} x^d` to `a_i` changes the `x^{n+1/2}` equation by
`κ q^{β + i(n−d+½)} f_{n−d}`. Hence:

* `d ≤ 2` perturbs the `x^{5/2}` equation, which is already **exact** — it would break `f_2`.
* `d ≥ 4` leaves the `x^{7/2}` equation untouched — it leaves the defect standing.

So `d = 3` exactly, and the `x^{7/2}` equation then **forces** `κ q^{β+i/2} = −q^{13}`, i.e.
`κ = −1`, `β = 13 − i/2`. **Five candidates, `i = 0…4`, and no others.** Each was run to fourteen
blocks and assembled into `Ẑ(S³_{−1}(m(5₂))) = Ẑ(Σ(2,3,11))` through GM Thm 1.2:

| repair | `f_3` | assembled vs `Ẑ(Σ(2,3,11))` on `q^{−1}..q^{180}` |
|---|---|---|
| `a_0 += −q^{13}x^3` | OK | **first mismatch `q^{17}`** (gives 2, truth 0) |
| `a_1 += −q^{25/2}x^3` | OK | **first mismatch `q^{17}`** (gives 1, truth 0) |
| `a_2 += −q^{12}x^3` | OK | **first mismatch `q^{17}`** (gives 1, truth 0) |
| `a_3 += −q^{23/2}x^3` | OK | **first mismatch `q^{17}`** (gives 1, truth 0) |
| `a_4 += −q^{11}x^3` | OK | **first mismatch `q^{17}`** (gives 1, truth 0) |

The horizon is `q^{180}`, and only blocks `f_0..f_4` can reach `q^{17}` at all (`f_5` first
appears at `q^{25 + lo(f_5)} = q^{22}`), so the mismatch is not a truncation artefact.

**Conclusion: eq (32) needs at least two corrections, and this bench has not determined them.**
That is stated as an open item in §7, not glossed.

---

## 6. The two instruments this produced, which stand on their own

**(a) GM Thm 1.2 at `p/r = −1`, controlled.** Writing `F_K = Σ_{k≥1} f_{k−1}(q) x^{k−1/2}` minus
its `x ↦ 1/x` mirror, the transform `L^{(a)}_{p/r}: x^u ↦ q^{−u²r/p}` applied to
`(x^{1/2r} − x^{−1/2r})F_K` collapses at `p = −1, r = 1` to

```
   Zhat = eps q^d [ -f_0 + sum_{m>=1} (f_{m-1} - f_m) q^{m^2} ] .
```

Fed the figure-eight's `Ξ_k`, this returns **GM eq (12)**, `Ẑ_0(−Σ(2,3,7))`, in all twelve
printed coefficients with `ε = −1`. The bench had previously validated the same placement only
at `p/r = −1/2` (against eq (13)); `p/r = −1` is a second, independent slope, and it is the
slope this memo's refutation runs on.

**(b) `Ẑ(Σ(2,3,11))` to arbitrary order.** Park's Table 3 prints seven coefficients. Reading them
as a false theta gives, uniquely,

```
   support  n in +-{5, 17, 49, 61} mod 132,   chi odd mod 132,   exponent (n^2 - 25)/264
```

which reproduces **all seven exponents with their signs**, and predicts `−q^{61}` where Park
writes `−O(q^61)` — sign included, from a rule fitted only to the earlier terms. That is a
one-parameter-free extension of a published truncation to as many terms as wanted, and it is what
makes §5 exhaustive rather than suggestive. `4P = 264 = 4·2·3·11` is the Brieskorn modulus, as it
must be.

---

## 7. What this costs, stated plainly

* **The `5₂` `c_eff` numbers computed earlier today are VOID.** Values of `0.726, 0.499, 0.399,
  0.339` for `p/r = −1, −1/2, −1/3, −1/4` were obtained from the defective recursion and are
  withdrawn in full, before banking. They were never banked; this memo is the record that they
  existed and why they are not reported.
* **Memo 177's ceiling remains untested on a second knot.** The route through Park's `Â` is
  blocked until eq (32) is repaired. The cheaper route survives untouched: addendum 4's mechanism
  predicts the ceiling from the **colored Jones tail** `Φ_{5₂}`, which needs no `F_K` at all and
  which this bench can compute with the memo-179 calculator. That is the next move.
* **What would unblock the `F_K` route:** any one of (i) the arXiv LaTeX source of eq (32),
  (ii) Garoufalidis–Koutschan's non-commutative A-polynomial of the twist knot `K_2`
  (Park cites [GK13] as its source), or (iii) `f_4^{m(5₂)}` from any independent computation —
  a single further coefficient beyond `q^0` would discriminate. Added to
  `fetch/FETCH_REQUEST_CEFF.md`.

---

## 8. Fences

* This is a statement about **the polynomial as printed in v2 of the arXiv posting**, obtained by
  two independent extractions of that PDF. It is **not** a claim that the paper's method is
  wrong, that `F⁺_{m(5₂)}` is wrong, or that no `Â` exists — Park's `f_0..f_3` are internally
  consistent and survive every test here, and his `ℚ(q)`-formulas for `f_2, f_3` are what expose
  the defect in the first place.
* `Ẑ(Σ(2,3,11))` as extended in §6(b) is a **reconstruction from seven printed coefficients**,
  not an independent derivation from the plumbing. It is controlled by the sign of the eighth
  term, which Park does not print, and by the modulus being the arithmetically forced
  `4·2·3·11`. A plumbing computation would be stronger and has not been done here.
* Convention A is forced **among the five readings tested**. A sixth reading nobody has thought of
  is not excluded by anything above.
* Nothing in this memo touches the origin-axiom programme's own claims. It is an instrument
  finding on a borrowed input, filed because the input was about to carry a number.

---

## 9. Reproduce

```
python3 certificates/park_ahat_erratum.py 300     # ~4 min; all six controls must fire
```

---

# ADDENDUM 1 (2026-09-08, same day) — **PARK'S BLOCKS ARE RIGHT. THE DEFECT IS IN eq (32) AND NOWHERE ELSE**, and the false theta is confirmed by a second instrument

**Certificate** `certificates/park_large_color.py` · **Output** `outputs/park_large_color_out.txt`

## 1. The one way memo 183 could still have been wrong

The memo shows Park's three statements about `m(5₂)` are mutually inconsistent and concludes
that eq (32) is the odd one out. That conclusion rested on his `f_2, f_3` being right, which was
argued from their two forms — printed series and `ℚ(q)`-formula — agreeing. But **both of those
could have come out of the same eq (32) computation**, in which case the agreement would prove
nothing and the defect could have been in the blocks.

It is now settled the other way, by computing the blocks from an instrument that shares nothing
with eq (32).

## 2. Park's own method, implemented from the paper

His §3–4, transcribed and run:

* **eq (17)** the `Ř`-matrix on the **lowest weight Verma module** `V^l_∞`;
* **eq (18)** `Ř^{-1} = P Ř|_{x→1/x, q→1/q} P`;
* **eq (25)–(26)** the reduced stratified quantum trace,
  `Tr'_{q,η} β = x^{−(N−1)/2} q^{(N−1)/2} Σ_{w≥0} Tr β'(w) q^w η^w`, `η → 1`,
  summed in his stated order — by total weight `w`, the leftmost strand left open;
* **eq (31)** `(x^{1/2} − x^{−1/2}) Tr'_q β = F⁺_{m(5₂)}`, on **his** braid
  `β = σ₂^{−3}σ₁^{−1}σ₂σ₁^{−1}`.

Exact integer arithmetic in `u = q^{1/2}`, `s = x^{1/2}`. No A-polynomial anywhere.

## 3. Result

| block | from the R-matrix | vs Park's printed series | stable coefficients |
|---|---|---|---|
| `f_0` | `−q^{−1}+1−q^2+q^5−q^9+…` | **MATCH** | 78 |
| `f_1` | `−q^{−1}+1+q−q^2−q^3−q^4+…` | **MATCH** | 55 |
| `f_2` | `−q^{−1}+2+q−q^2−2q^3−2q^4+…` | **MATCH** | 35 |
| `f_3` | `2+q−2q^2−2q^3−3q^4+0q^5+2q^6+4q^7+4q^8+2q^9+0q^{10}−3q^{11}` | **MATCH** | 17 |
| `f_4` | `q^{−2} + 2 − 3q^2 + …`  (`[1,0,2,0,−3]` from `q^{−2}`) | *not printed by Park* | 5 |

> ### Every block Park prints is reproduced. **The defect memo 183 localises is in eq (32) alone.**

## 4. And the false theta is confirmed by a second, independent instrument

Memo 183 §5's exhaustive refutation of the five single-monomial repairs runs against
`Ẑ(Σ(2,3,11))`, reconstructed there from seven printed coefficients. That reconstruction implies
a specific `f_4` on a window — `[1, 0, 2, 0, −3, −3, −3, 1]` from `q^{−2}` — obtained with **no**
`R`-matrix and **no** `Â`. The large-color computation, which knows nothing of Σ(2,3,11), returns

```
   f_4  =  1*q^-2 + 0*q^-1 + 2*q^0 + 0*q^1 - 3*q^2 + ...
```

**The two agree on every coefficient the R-matrix has converged (all five).** In particular both
give `f_4` starting at `q^{−2}` — two steps below `f_3`'s `q^0`, which is the feature the five
candidate repairs of eq (32) all get wrong, and which no single-monomial repair reproduces.

Park's own `m(7₃)` blocks show the same downward drift (`q^{−2}, q^{−2}, q^{−3}, q^{−3}, q^{−5}`
for `f_1..f_5`), so it is a property of these series, not an artefact.

## 5. An error of mine, recorded at the point of occurrence

The first version of this computation carried an `x`-degree truncation window derived by hand
from the braid word. It was **too tight by five units in `x`**, and it produced an `f_3` that was
**stable in `w` across eight consecutive strata and wrong** — `2, 1, −1, −1, −1, …` instead of
Park's `2, 1, −2, −2, −3, …`. A convergence check on the summation index could not see it; only
widening the window did. That is exactly memo 164's rule, and the certificate now carries
**C2**, which recomputes at margin `M+5` and requires the same blocks, alongside the convergence
check **C3**.

I do not have a proof of the correct margin; C2 is an empirical saturation test (`M` and `M+5`
agree, and `M+5` and `M+10` agreed when checked by hand). **Stated as a fence, not hidden.**

## 6. What is now unblocked, and what is not

* **Unblocked:** `f_j` for `m(5₂)` to any `j`, at a `q`-order that grows with the weight cutoff.
  This is the route to `c_eff` for a second hyperbolic knot that memo 183 §7 said was blocked.
* **Not yet:** `c_eff` needs `f_j` to thousands of `q`-coefficients, and the stratified trace
  costs too much for that directly. The practical route is still to **repair eq (32)** — now
  with true blocks in hand to fit against — and then run the repaired recursion. `f_4` to about
  ten converged coefficients is expected to determine the repair; five are in hand.
* **No `c_eff` number for `5₂` is claimed here.** Memo 182 addendum 2 §4's withdrawal stands.

---

# ADDENDUM 2 (2026-09-08, same day) — **THE REPAIR IS DETERMINATE. THREE OF ITS TERMS ARE RECONSTRUCTED, AND `a_1` IS THE UNIQUE SINGLE-INDEX PLACEMENT**

**Certificate** `certificates/park_ahat_repair.py` · **Output** `outputs/park_ahat_repair_out.txt`
Blocks from `certificates/park_large_color.py`.

## 1. From a search to a solve

Memo 183 §5 could only *exclude*: five single-monomial repairs, all refuted. With the true blocks
in hand (addendum 1) the repair stops being a search. Writing `c_d(Q)` for the Laurent polynomial
to be **added to the `x^d` coefficient of `a_1`** (`q = Q²`), the equation at `x^{n+1/2}` reads

```
   delta_n  =  - sum_d c_d Q^{2(n-d)+1} f_{n-d} ,
```

so `δ_3` gives `c_3`, then `δ_4` gives `c_4`, then `δ_5` gives `c_5` — each as an **exact quotient
by `f_0`**, nothing fitted:

```
   c_3 = -q^{25/2}          c_4 = q^{25/2}(1 + q - q^3)          c_5 = q^{33/2}(1 + q)
```

## 2. `a_1` is forced, not preferred

Two quantities are determined **exactly**. Writing `U_3(t) = Σ_i c_{i,3} Q^{(2t+1)i}` for the
`x^3` correction spread over all five `a_i`:

* `U_3(0) = −Q^{26}`, from `δ_3`, exact to `Q^{612}`;
* `U_3(1) = −Q^{28}`, from `δ_4`. Since `f_0` and `f_1` are **not rationally related**, the pair
  `(U_3(1), U_4(0))` solving `δ_4 = −U_3(1) f_1 − U_4(0) f_0` is **unique** — and the linear solve
  returns it with **zero free parameters**, on `δ_4` known exactly to `Q^{96}`.

| placement | `U_3(1)` it implies | |
|---|---|---|
| `i = 0` | `−Q^{26}` | excluded |
| **`i = 1`** | **`−Q^{28}`** | **consistent** |
| `i = 2` | `−Q^{30}` | excluded |
| `i = 3` | `−Q^{32}` | excluded |
| `i = 4` | `−Q^{34}` | excluded |

For pairs `{i,j}` the 2×2 system has a unique solution: every pair containing `i = 1` collapses to
`c_1 = −Q^{25}` with the other zero; `{0,2}, {0,3}, {0,4}, {2,4}` force **non-Laurent**
coefficients and are excluded outright; only `{2,3}` and `{3,4}` survive as genuine alternatives.

> **`a_1` is the unique single-index placement.** Splits over three or more `a_i` are not excluded
> by these two equations, and `{2,3}` and `{3,4}` were not tested further.

A second, independent test agrees: placing the `x^4` correction in each `a_i` in turn and
assembling `Ẑ(Σ(2,3,11))` gives first mismatches at `q^{24}, **q^{28}**, q^{25}, q^{25}, q^{25}`
for `i = 0,1,2,3,4`.

## 3. The controls, and why they are not circular

Each correction is solved from one instrument and then tested against **two**:

| corrections applied | blocks reproduced | `Ẑ(Σ(2,3,11))` agrees to |
|---|---|---|
| `c_3` | `f_2` 282/282, `f_3` 293/293, `f_4` 8/28, `f_5` 2/11 | `q^{16}` |
| `c_3 + c_4` | `f_4` **28/28**, `f_5` 5/11 | `q^{27}` |
| `c_3 + c_4 + c_5` | `f_5` **11/11** | `q^{33}` |

(`f_2, f_3` against Park's own `ℚ(q)` formulas; `f_4, f_5` against the large color `R`-matrix's
converged output. `f_0, f_1` are the recursion's seeds, not predictions.)

> Seeded with nothing but Park's closed-form `f_0` and `f_1`, the repaired recursion reproduces
> **all 614 coefficients** of `f_2, f_3, f_4, f_5` that either instrument has produced.
>
> **Each correction extends the agreement exactly as far as the next block's converged range
> reaches, and no further** — which is what a correct reconstruction does. An overfit buys
> agreement on what it was fitted to and stops; `c_4` is solved from `δ_4` alone and then
> correctly predicts three further coefficients of `f_5` and eleven further coefficients of
> `Ẑ(Σ(2,3,11))`, neither of which entered the solve.
>
> And every block comes out an **integral Laurent polynomial in `q`** — no denominators, no
> half-integer powers — which the recursion does not enforce and a wrong correction destroys.

## 4. What is NOT claimed — including one thing that cuts against the reconstruction

* **The repair is incomplete.** A further correction at `x^6` is needed: the assembled series
  first fails at `q^{34}`. Determining it needs `f_6` to about ten converged coefficients — at the
  weight cutoff reached here `f_6` has none. Corrections at `x^7 … x^{11}` may follow.
* **These are almost certainly not Park's own missing terms, and here is the reason.** `a_1` is
  printed as `q^{11/2}x²(qx+1)(q³x+1)(q⁷x−1)·I(x)` with `I` an explicit polynomial whose largest
  `q`-power is `q^9`. Dividing the reconstructed correction by `q^{11/2}x²(qx+1)(q³x+1)(q⁷x−1)`
  gives a would-be correction to `I` whose coefficients are `q^7`, then
  `q^7(q+1)(q^6−q^5+q^4−q^3+q^2−q−1)`, then terms reaching `q^{13}` and `q^{16}` — far outside
  `I`'s printed range. **So the missing terms do not sit inside `I`.** Either the misprint is
  structural (a wrong or dropped factor, which a monomial-by-monomial repair reproduces only as
  an equivalent sum), or the split runs over three or more `a_i`. This is recorded because it is
  evidence against the reconstruction being the paper's object, and it was found while writing
  the addendum rather than reported by a control.
* **What the reconstruction *is*:** the unique way to make eq (32) annihilate the series it is
  printed to annihilate, to the order tested, **given** that the missing terms sit in `a_1`.
* **No `c_eff` for `5₂` follows yet.** That needs the recursion right at *all* orders, which §4's
  first bullet says it is not.

## 5. An improvement to addendum 1 §5's fence

Addendum 1 §5 recorded the `x`-degree truncation margin as empirical, with *"I do not have a proof
of the correct margin."* It is now **measured**: at weight cutoff 11 the blocks are wrong at
margin 2, correct at margin 3, and **identical at margins 3, 4 and 5** — saturation at 3. The
certificate uses 5. So `f_5` (margin 4) and `f_6` (margin 3), as used in memo 184 §5, are both
inside the saturated regime. Still an empirical saturation, not a proof.

---

# ADDENDUM 3 (2026-09-08, same day) — **THE REPAIRED BLOCKS REPRODUCE PARK'S TABLE 3 AT `p = −2` AND `p = −3`**, and `c_6` is determined

**Certificate** `certificates/park_table3_repaired.py` · **Output** `outputs/park_table3_repaired_out.txt`

## 1. Why another test was needed

Addendum 2 tested `c_3, c_4, c_5` against the large color `R`-matrix blocks and against
`Ẑ(Σ(2,3,11))`. **Both live at `p/r = −1`.** Park's Table 3 also prints `Ẑ` for `p = −2` and
`p = −3`, where GM Thm 1.2's transform places block `k` at `u²/|p|` instead of `u²`, and the
residue condition `ru − a ∈ pℤ` selects a *different subset of blocks for each `spin^c` label*.
**Nothing in the repair ever looked there.**

## 2. `c_6`, and why it is bookkeeping

With `f_0 … f_5` exact, the surgery identity leaves `g_6 = f_5 − f_6` readable on
`[36 + lo(g_6), 49 + lo(g_7))`, and `δ_6` then gives

```
   c_6 = -q^{27/2} - q^{29/2} - q^{35/2} - 2 q^{37/2} + q^{41/2}
```

which extends the `Ẑ(Σ(2,3,11))` agreement from `q^{33}` to `q^{45}`. **`c_6` was solved from
that target, so the extension is not evidence for it** — stated here so it is not mistaken for a
test. The independent test is §3, and §3 deliberately uses **only `f_0 … f_5`**, the blocks
addendum 2 confirmed coefficient by coefficient against Park's own `R`-matrix.

## 3. The independent test

| | lowest | verified to | Park's printed terms covered | zeros reproduced | |
|---|---|---|---|---|---|
| `p = −1, a = 0` | `q^{−1}` | `q^{33}` | **6 of 7** | 27 | MATCH |
| `p = −2, a = 0` | `q^{−1}` | `q^{15}` | 2 of 6 | 13 | MATCH |
| `p = −2, a = 1` | `q^{3/2}` | `q^{18}` | **4 of 5** | 14 | MATCH |
| `p = −3, a = 0` | `q^{−1}` | `q^{9}` | 3 of 6 | 6 | MATCH |
| `p = −3, a = 1` | `q^{4/3}` | `q^{10}` | 2 of 4 | 8 | MATCH |

> **One overall factor, `1/2`, for all five series** — which is GM's own
> `F_K = ½(Ξ(x) − Ξ(1/x))`, not a fitted scale. It comes out the same on five series with three
> different `p`, two different `spin^c` sectors and four different lowest exponents.

The **zeros** are the strong part. Park's `p = −2, a = 0` row reads `1 − q` and then *eighteen
zeros* before `q^{18}`; thirteen of them are inside the horizon and every one is reproduced. A
wrong block would have to vanish there by accident.

**C2, a structural control the assembly does not enforce:** at `p = −3` the labels `a = 1` and
`a = 2` come out **identical** — `spin^c` conjugation. Park prints two series for `p = −3`, not
three, which is the same statement.

**C3:** the `p = −1` row survives even under the harsh bound `lo(f_j) ≥ −(j−3)²` on the blocks
not used, verified to `q^{28}` with six printed terms. That row does not lean on the repair
beyond `f_5` at all.

## 4. The fence on §3, stated because it is real

At `p = −2` and `p = −3` the horizon is finite **only if** the blocks' lowest `q`-powers fall
more slowly than the placements `u²/|p|` grow. That is GM's own applicability condition (177),
`4c + r/p > 0`. The horizons in §3 use the repaired recursion's computed `lo(f_j)` through
`j = 18` and `−(2j+1)²/40` beyond — the slope the measured blocks show. **Under the much harsher
`−(j−3)²` those two sums do not converge at all and those rows say nothing.** So what §3 verifies
at `p = −2, −3` is *conditional* on `5₂`'s block edge falling at roughly the measured rate.

**A consequence worth flagging, not claimed.** The measured `lo(f_j)` correspond to
`|c| ≈ 1/40`, and GM's condition then gives a slope window `|p/r| < 1/(4|c|) ≈ 10` for `5₂` —
not the `4` memo 182 §3 inferred from the table that addendum 3 there withdrew. Park printing
`Ẑ` for `p = −1, −2, −3` is consistent with a window wider than 4. **No value of `c` is claimed**
(memo 182 addendum 3), so no window is claimed either; this is recorded as the direction the
evidence points.

## 5. Where the repair stands

`c_3 … c_6` determined; `Ẑ(Σ(2,3,11))` reproduced to `q^{45}`; every converged coefficient of
`f_2 … f_5` from two instruments reproduced; Park's Table 3 reproduced at three surgery
coefficients and two `spin^c` sectors. **Still incomplete** — `a_1` has `x`-degree 11 and only
`x^3 … x^6` are pinned, so `c_7 … c_{11}` remain, each needing the next block. And addendum 2 §4's
warning stands: the reconstruction's shape argues these are an equivalent sum rather than Park's
own missing terms. **No `c_eff` for `5₂` is claimed.**

---

# ADDENDUM 4 (2026-09-08, same day) — **THE SINGLE-INDEX RECONSTRUCTION CANNOT CLOSE.** Addendum 2 §4's argument becomes a demonstration, and the ask sharpens

**Certificate** `certificates/park_repair_cannot_close.py` · **Output** `outputs/park_repair_cannot_close_out.txt`

## 1. What I tried, and what it does

Addendum 2's method extends: at each `x`-degree `d`, read `f_d` off the `p = −1` surgery identity
and solve `δ_d` for the correction. Carried to `d = 7, 8, 9, 10, 11` it yields short integral
Laurent polynomials every time, and the `Ẑ(Σ(2,3,11))` agreement climbs
`q^{45} → q^{59} → q^{75} → q^{95} → q^{116} → q^{140}`. It looks like a reconstruction closing.

**It is not, and the certificate is the proof.**

## 2. The demonstration

`a_1` has `x`-degree **11**, so `c_3 … c_11` exhausts it. Only `a_0` and `a_2` reach `x`-degree
**12**, which is the maximum anywhere in eq (32). `δ_12` gives `U_{12}(0) = Q^{50} + Q^{52}` —
even exponents, as the parity of the equation requires. Placing it in either:

| | first mismatch | horizon |
|---|---|---|
| `c_3 … c_11` all in `a_1` | `q^{141}` | `q^{769}` (5.5×) |
| `+ c_12` in `a_0` | `q^{164}` | `q^{778}` (4.7×) |
| `+ c_12` in `a_2` | `q^{165}` | `q^{780}` (4.7×) |

> ### Every `x`-degree eq (32) has is used, every stage is an integral Laurent series, and it still fails — far inside its own horizon.

## 3. Why, exactly

`δ_d` determines `U_d(0) = Σ_i c_{i,d} Q^i` **exactly and uniquely**. It does **not** determine
the five `c_{i,d}` separately. Those are fixed by `U_d(1) … U_d(4)` — a Vandermonde system in
`Q^{2i}` — and those live in `δ_{d+1} … δ_{d+4}`.

So a sequential single-index fit **absorbs each wrong split into the next correction** and pushes
the error one degree up, degree after degree, until the degrees run out. The climbing agreement in
§1 is that push, not convergence. **This is the failure mode the numbers looked most like success
in**, and it is recorded because I ran five more degrees before the structure made it visible.

## 4. What this costs, and what it does not

* **Addendum 2's `c_3` and its placement stand.** That argument uses `U_3(0)` *and* `U_3(1)` —
  two exact quantities, so the split at `d = 3` **is** determined, and only `a_1` satisfies both.
* **Addendum 3 stands untouched.** Its Table 3 test uses `f_0 … f_5`, and `f_4` and `f_5` were
  confirmed coefficient by coefficient against the large color `R`-matrix — they are right
  *however the corrections are distributed*.
* **`c_6 … c_12` are NOT determinations and are not banked as such.** Addendum 3 §2 already
  flagged `c_6` as bookkeeping; this extends that to everything above it.
* **Addendum 2 §4's structural warning is now a demonstrated fact** rather than an inference from
  the shape of the coefficients.

## 5. The ask, sharpened

`fetch/FETCH_REQUEST_CEFF.md §B''` asked for `f_4` to ten coefficients. That is no longer the
binding constraint — `f_4` is in hand to 28. The real requirement is now precise:

> **To close degree `d` one needs `U_d(0) … U_d(4)`, hence `δ_d … δ_{d+4}`, hence `f_0 … f_{d+4}`.
> Closing every degree up to 12 needs blocks to about `f_16`. This bench has `f_5`.**

Two routes, both stated so they can be priced:

1. **More blocks** — the large color `R`-matrix reaches `f_5` at weight cutoff 17; `f_16` is far
   beyond what the stratified trace costs here. A better algorithm, not a bigger machine.
2. **The source** — eq (32)'s LaTeX, or Garoufalidis–Koutschan's non-commutative A-polynomial of
   the twist knot `K_2`, which Park cites as its origin. **One document ends this.**

`§B''` is updated accordingly.

---

# ADDENDUM 5 (2026-09-08, same day) — a reproducibility defect in my own certificates, found by a container restart

**Not a mathematical correction.** Every result in memo 183, its addenda, and memo 184 stands
unchanged; this records a defect in how they were made runnable, and the fix.

## 1. What was wrong

The container this lane runs in was restarted. Nothing scientific was lost — everything was
committed and pushed as it was produced — but it exposed that three certificates could not be
re-run from a clean checkout:

* `park_ahat_repair.py` read the `F⁺_{m(5₂)}` blocks from a **scratch file under `/tmp`**;
* `park_large_color.py` **wrote** them there;
* `gm_thm13.py`, `park_ahat_erratum.py` and `tail_52.py` carried **absolute paths**
  (`/tmp/k52`, `<seat>/...`), one of them dead and merely misleading, two of them real
  dependencies on sibling certificates.

A certificate that only reproduces on the machine that made it is not a certificate. The lane's
own rule — *reproduce* is a section in every memo — was being satisfied by accident of the
filesystem.

## 2. The fix

* The converged blocks are now **vendored into the repo** at
  `data/park_f52_blocks_w16.json`, carrying their own provenance: which certificate produced
  them, at which weight cutoff and `x`-degree margin, that its controls C1–C3 fired, and that
  **only the prefix of each block identical at cutoffs `w = 15` and `w = 16` is stored** —
  nothing unconverged is kept. `f_0 … f_5` at 16, 105, 69, 49, 28, 11 coefficients.
* `park_large_color.py` writes there instead of `/tmp`.
* `park_ahat_repair.py` reads there, by a path relative to its own location.
* Every absolute path in the session's certificates is now relative to the certificate file.

**All seven certificates re-run and all their controls fire:** `park_ahat_erratum`,
`park_large_color`, `park_ahat_repair`, `park_table3_repaired`, `park_repair_cannot_close`,
`tail_52`, `gm_thm13`.

## 3. Recorded as a bench error

It is the same shape as the two errors already filed today — memo 182 addendum 2's truncation
window and addendum 1 §5's margin. All three are cases where *the computation was right and the
apparatus around it was not*, and in all three the apparatus was only tested by something going
wrong. The `/tmp` dependency would have been invisible until someone else tried to run it.

---

# ADDENDUM 6 (2026-09-09) — **A CONVENTION MISMATCH IS EXCLUDED**, and the arrival path for the primary source is built and self-tested

**Certificate** `certificates/ahat_ingest.py` · **Output** `outputs/ahat_ingest_out.txt`

## 1. A loophole the memo did not close

Memo 183's **C3** forced the **operator-ordering** convention — how `ŷ` acts on `F⁺` — by showing
that of five readings, exactly one makes the `x^{1/2}` and `x^{3/2}` equations vanish identically.
That is not the same as fixing the **presentation** of the operator itself. A reader could still
have said: *eq (32) is right, but written in a different convention from the one you assumed* —
`q → 1/q`, `x → 1/x`, the `ŷ`-degree reversed, or a combination. Those give a genuinely different
operator that is still "the" quantum A-polynomial of the same knot, and the memo did not test them.

**They are now tested, and none of them rescues it.**

| presentation | `x^{1/2}` | `x^{3/2}` | `x^{5/2}` | `x^{7/2}` |
|---|---|---|---|---|
| **identity** | 0 | 0 | 0 | **`q^{13} f_0(q)`** |
| `q → 1/q` | ≠0 | ≠0 | ≠0 | ≠0 |
| `x → 1/x` | ≠0 | ≠0 | ≠0 | ≠0 |
| `ŷ`-degree reversed | ≠0 | ≠0 | ≠0 | ≠0 |
| reversed, `q → 1/q` | ≠0 | ≠0 | ≠0 | ≠0 |
| reversed, `x → 1/x` | ≠0 | ≠0 | ≠0 | ≠0 |
| `q → 1/q` and `x → 1/x` | ≠0 | ≠0 | ≠0 | ≠0 |

> **The identity presentation is the only one that gets even the first three equations right, and
> it is the one that leaves the defect.** Every alternative fails immediately, at `x^{1/2}`. So the
> erratum is not an artefact of how eq (32) was read — **a convention mismatch is excluded.**

An overall monomial in `x` and `q` is divided out before testing, since it cannot affect
annihilation.

## 2. Why this was built now

`fetch/FETCH_REQUEST_CEFF.md` §B'' asks for the operator from the **primary source** Park's own
footnote 12 names. Those authors write in `(M, L)` notation and need not share his conventions —
so an ingester that only accepted Park's exact format would stall on arrival, and worse, a
mismatch could be *misread as disagreement*. `ahat_ingest.py` therefore does not assume a
convention: it takes five coefficients in `M`/`x` and `q`, in labelled lines or a Mathematica list,
normalises away the overall monomial, and **searches the seven presentations above**, reporting
which — if any — annihilates Park's own printed blocks.

**Self-test, which must pass before any external file is trusted:**

* **T1** the printed eq (32) reproduces memo 183's defect exactly, in the identity presentation;
* **T2** no presentation rescues it — §1;
* **T3** eq (32) plus addendum 2's `c_3 = −q^{25/2}x^3` in `a_1` makes `x^{7/2}` **vanish**, so the
  diagnostic can see a repair when there is one.

All three pass.

## 3. What the two outcomes will mean, fixed in advance

Written before the file exists, so the reading is not chosen after seeing it:

* **The primary source's operator annihilates `F⁺`** → it differs from eq (32), the erratum is
  **confirmed against the source**, and the repair is *handed over* instead of fitted — which
  retires memo 183 addendum 4's dead end and unblocks memo 184 §3's preregistered cell.
* **It does not annihilate `F⁺` either** → the defect is **older and further upstream than Park**,
  and the printed coefficients the certificate reports localise where. That is a different and
  larger finding, and it is not a disappointment.

---

## ADDENDUM 7 (2026-09-09) — **the cyclotomic route past `f₅` is closed, and it is closed by computation**

Addendum 4 named the blocker: the reduced quantum trace yields `f_0 … f_5` for `m(5₂)` and the
sequential single-index fit past `f_5` **cannot close**, because `δ_d` determines only
`U_d(0) = Σ_i c_{i,d}Q^i` and not the five `c_{i,d}` separately.

A candidate way around it was floated this session — solve Habiro's cyclotomic coefficients
`C_0 … C_{n−1}` triangularly out of `J_1 … J_n`, then read `f_j` off them. **It is withdrawn.**
`certificates/cyclotomic_vs_fk.py` (memo 185) resolves both preregistered cells to B:

* on `4₁`, the single monomial `x⁰q⁰` of `C_K(x,q)` receives unboundedly many, unboundedly
  large contributions (`+1, 0, +2, −2, +8, −16, +52, −152, … , −2407538` at `m = 0…15`), so
  `C_K` is **not a Laurent power series** and nothing can be read off it term by term;
* on `3₁`, where `C_K` **is** a series, `C_K ≠ λ x^A q^B f_K` for any `λ, A, B` — `f_K`'s
  nonzero coefficients all have absolute value `1/2`, `C_K`'s take 32 distinct absolute values
  in 35 orders.

**So addendum 4's blocker stands.** What is *not* closed: Park's non-naive *inverted* Habiro
series (arXiv:2106.03942, fetch item B2, not held here). That is the named follow-up, ranked
below the quantum A-polynomial data of `fetch/FETCH_REQUEST_CEFF.md` §B''.
