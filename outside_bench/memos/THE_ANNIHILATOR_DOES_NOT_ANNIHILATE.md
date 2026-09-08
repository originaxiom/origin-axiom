# MEMO 183 — **THE QUANTUM A-POLYNOMIAL PRINTED FOR `m(5₂)` DOES NOT ANNIHILATE THE SERIES IT IS PRINTED TO ANNIHILATE**

**Date** 2026-09-08 · **Lane** outside bench · **Branch** `claude/outside-bench`
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
