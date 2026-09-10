# MEMO 186 — **THE FENCE GOES FROM 7 COEFFICIENTS TO 52, ON FOUR KNOTS**, five tails identified in closed form, and the false/genuine theta split turns up inside a single one-parameter family

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificates** `certificates/cj_table_ingest.py` (identification + controls) ·
`certificates/tail_tables.py` (the measurement)
**Outputs** `outputs/cj_table_ingest_out.txt` · `outputs/tail_tables_out.txt`
**Data** `data/cj_tails.json` (certified prefixes only, with provenance; the raw tables are 12 MB and are not vendored)
**Gate 5** exact integer arithmetic. No fitted constant. No measured physical value.

**Already-banked check (memo 153).** Terms searched: `colored jones tail`, `twist knots`,
`Rogers-Ramanujan product`, `false theta`, `genuine theta`, `Andrews-Gordon`. The sweep returns
matches, but on inspection every one is a **lexical collision on generic words** (`twist`,
`chirality`, `sweep`) with arcs about unrelated subjects — `B944_dynamics_chirality_sweep`,
`B1127_antilinear_completion`, `B1139_symmetry_point_table`, `B1093_route_a_arithmetic`. **No
settled arc concerns colored Jones tails.** Nothing here is a MISSING/OPEN claim in any case;
these are positive measurements.

---

## 1. What arrived, and what did not

The owner supplied five gzipped `CJTwist.<p>.txt` files from Garoufalidis–Sun's
`twist.knot.data` — `J_{K_p,n}(q)` for `n = 1…60`, normalised `J_{p,1} = 1`.

**Memo 185 §5 fixed the rule before any file arrived**: `K_{−1} = 4₁` and `K_1 = 3₁` are free
controls, to be run *before* anything is claimed from any other file. That rule immediately
earned its keep, because **a filename is not a knot**:

| file as named | determinant `|J_2(−1)|` | what it actually is |
|---|---|---|
| `CJTwist.0` | 1 | unknot ✓ |
| `CJTwist.1` | 3 | `K_1 = 3₁` ✓ |
| `CJTwist.1` (second copy) | **5** | **`K_{−1} = 4₁`** — a lost minus sign |
| `CJTwist.2` | **9** | **`K_{−2} = 6₁`** — a lost minus sign |
| `CJTwist.4` | 15 | `K_4 = 9₂` ✓ |

Twist knots satisfy `det(K_p) = 4p − 1` and `det(K_{−p}) = 4p + 1`, so the determinant alone
recovers both `|p|` **and the sign of `p`** — exactly the information a filename can lose.

> **`5₂` is not in the set.** The file that came through as `CJTwist.2` is `6₁`. `5₂ = K_2`
> has `det = 7`; no file has determinant 7. **The one knot the bench most wanted is the one
> that is missing.**

### Controls on the data itself, all PASSED

| | control | result |
|---|---|---|
| T1 | `J_1 = 1` for every file | PASSED |
| T2 | determinant identifies each knot | PASSED (two filenames flagged) |
| T3 | `J_n(1) = 1` for all `n`, every file | PASSED |
| T5 | `3₁`: every `J_n` equals **GM eq (24)**'s cyclotomic expansion, `n = 1…12` | PASSED |
| T6 | `4₁`: every `J_n` equals **GM eq (166)**, `n = 1…12` | PASSED |

T5 and T6 are the controls memo 185 §5 promised, run against the same two formulas that
`certificates/cyclotomic_vs_fk.py` uses. **The tables are trustworthy.**

## 2. The measurement: seven coefficients becomes fifty-two

Memo 184 measured the tail of `m(5₂)` behind a fence of **seven** stabilised coefficients,
because seven was all the `F_K` blocks could certify. A coefficient is certified here when the
last five `n` **at step 2** (`n, n−2, …, n−8`) agree on it; the step-1 window is computed and
printed beside it, and the difference is informative rather than noise.

```
knot     p     low end                        high end            step1 / step2
----     --    -------                        --------            -------------
unknot    0    1                              1                     70 / 70
3_1       1    1                              -(q;q)_inf             0 / 52
4_1      -1    (q;q)_inf                      (q;q)_inf             56 / 52
6_1      -2    (q;q)_inf                      theta,  modulus 20    56 / 52
9_2       4    false theta, modulus 16        -(q;q)_inf             0 / 52
```

**A step-1 window of zero with a step-2 window of 52 is not a failure** — it says the stable
series is there and its overall **sign alternates with the parity of `n`**. That is why both
numbers are reported.

Every one of the five distinct series is **identified in closed form on every certified
coefficient** — matched, not fitted:

```
theta_20 :  sum over n = ±3, ±7  (mod 20)  of  ± q^{(n^2 - 9)/40}
false_16 :  sum over n = ±3, ±5  (mod 16)  of  ± q^{(n^2 - 9)/16}
```

## 3. Two preregistered cells, both resolved to B

**CELL 1 — is the stable end of a twist knot always `(q;q)_∞`?** *(A: yes; B: no.)*
**→ B.** `6₁`'s high end and `9₂`'s low end are not. Memo 184 argued from Armond–Dasbach that
the ceiling is knot-by-knot; **it is now measured rather than argued.**

**CELL 2 — for an end that is not `(q;q)_∞`, genuine theta or false theta?** Resolved only when
**two independent signatures agree**: the sign pattern of the nonzero coefficients, and the
exponents `a_n` in `Φ = ∏_{n≥1}(1−q^n)^{a_n}` (periodic and bounded ⇒ an eta-quotient, hence
genuine by Jacobi's triple product; aperiodic and unbounded ⇒ not). *(A: all genuine; B: both
kinds occur.)* **→ B**, and the two signatures agree in both cases:

| end | signs | `a_n` | verdict |
|---|---|---|---|
| `6₁` high | `+ − − + + − − + +` | periodic, period **5**: `a_n = 0` exactly for `n ≡ 2,3 (mod 5)` | **GENUINE theta** |
| `9₂` low | `+ − + − + − +` | aperiodic, `|a_n|` reaching **19** by `n = 45` | **FALSE theta** |

## 4. Armond–Dasbach's prediction, confirmed by name

`tail_mechanism.py` recorded the reason to expect knot-by-knot behaviour: *"tails of alternating
links are not all `(q;q)_∞`: by Armond–Dasbach the tail is that of the reduced all-A state graph,
and richer graphs give higher products and **Andrews–Gordon-type series**."*

`6₁`'s tail is `∏_{n ≢ 2,3 (mod 5)} (1 − q^n)` — **the Rogers–Ramanujan modulus**. Equivalently,
by Jacobi's triple product, `Σ_n (−1)^n q^{n(5n+3)/2}`, whose support `0, 1, 4, 7, 13, 18, 27,
34, 46, 55` is exactly what was measured. **The predicted object arrived, with its classical
name attached.**

## 5. The finding nobody asked for

**The false/genuine theta distinction occurs inside one one-parameter family.** `K_{−2} = 6₁`
carries a genuine theta at one end; `K_4 = 9₂` carries a false theta at the other. Both are
alternating twist knots differing only in the twist parameter.

This matters because that distinction is the one **memo 173 got backwards and memo 177 §1 now
turns on**. Until now it was a distinction between unrelated knots. It is now visible inside a
family small enough to enumerate — `p = −14 … 15`, thirty knots, of which four are measured
here. **Whatever selects false from genuine is a function of `p`, and `p` is an integer.**

## 6. What this does not do

**It does not reopen the `c_eff` route.** Register **R83** stopped paying for it on the ground
that its *success would not have been evidence*, since `c_eff(1/(q;q)_∞^m) = m` is available to
order. Nothing here changes that. These are measurements of the **tails themselves**, which are
the cheaper object memo 184 addendum 1 asked for and memo 185 §5 reason 1 promised.

## 7. Named follow-ups

**F186-1.** Get `CJTwist.2` (`5₂`, `det 7`) — it is the knot memo 183/184 are about and it is the
one that did not arrive. Also `CJTwist.-3` (`8₁`), `CJTwist.3` (`7₂`).
**F186-2.** Measure the whole family `p = −14 … 15` and read the false/genuine split as a
function of `p`. Cheap: `tail_tables.py --from-tables <files>` already does it.
