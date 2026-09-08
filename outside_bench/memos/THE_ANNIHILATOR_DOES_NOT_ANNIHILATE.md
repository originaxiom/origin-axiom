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
