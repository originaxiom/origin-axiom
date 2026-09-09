# MEMO 191 — **F190-2: two thirds of Q11 are decidable from what this bench already holds**, and `c_eff = 1` turns out to be forced by the *shape* of `Ẑ`, not by our knot

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** `certificates/zhat_unred_ceff.py` · **Output** `outputs/zhat_unred_ceff_out.txt`
**Gate 5** exact integer series; floats only in the growth fit. No measured physical value.

**Why this memo exists.** R90 recorded the owner's posture change: *do not build a plan whose
critical path runs through someone else's reply.* This is its first discharge — **F190-2**.

---

## 1. Q11 said what it needed, and it is now on the bench

Q11 (sent 2026-08-31) closes with:

> *"I should say plainly that `Ẑ` invariants and logarithmic or non-semisimple boundary algebras
> are the obvious tools here and that we have simply not read that literature. If the honest
> answer is 'read GPPV', that alone is worth the email."*

**That literature is now held.** Gukov–Manolescu **§10.2, "Relation to log-VOAs"**, and **Remark
3.8**, say three things bearing directly on the question:

1. for closed 3-manifolds the **unreduced** series should be a character of a 2d chiral algebra,
   *"non-strongly-finite for hyperbolic `Y`"* — **logarithmic, exactly as Q11 guessed**;
2. for **Brieskorn spheres the algebra is identified**: the logarithmic `(1,p)` **singlet VOA**,
   `p = b₁b₂b₃`, central charge `c = 13 − 6(p + p^{−1})`, with `Ẑ^unred_0` a character of an
   explicit atypical module;
3. for **hyperbolic** manifolds it is **not** — and GM say so in print, pointing at exactly our
   target: *"It would be interesting to identify log-VOAs that correspond to other types of
   3-manifolds, such as the hyperbolic surgeries on the figure-eight knot."*

**Remark 3.8 gives the bridge exactly: `Ẑ^unred_0 = Ẑ_0 / (q)_∞`.**

## 2. What that makes computable, entirely from series already verified here

`Ẑ_0` of a Brieskorn sphere is a **false theta** — bounded coefficients. So

```
Ẑ^unred  =  (false theta) / (q)_∞
```

and this bench has already measured both halves: a bare false theta gives `c_eff = 0`, and
`1/(q;q)_∞` gives `c_eff = 1`. **The prediction is `c_eff = 1` for every Brieskorn sphere, with
`p` cancelling out entirely.**

### The cell *(A: `c_eff` depends on `p`, so some sphere might reach 6 and a search is worth running. B: it does not.)*

| | `p` | singlet `c = 13 − 6(p+1/p)` | measured `c_eff(Ẑ^unred)` |
|---|---|---|---|
| `Σ(2,3,5)` | 30 | **−167.200** | **1.000326** |
| `Σ(2,3,11)` | 66 | **−383.091** | **1.001480** |

> **`c` varies by 215.9 between these two. `c_eff` varies by 0.0012. CELL → OUTCOME B.**

Both series were verified elsewhere on this bench before being used here — `Σ(2,3,5)` against GM
eq (27)–(28) in `gm_74_habiro_surgery.py`, `Σ(2,3,11)` in `park_ahat_erratum.py` C5 and again as
that certificate's anchor A2.

**Controls:** the estimator returns `1` on `1/(q;q)_∞`, **`2` on its square** — so it is not an
instrument stuck at 1 (memo 164) — and `0` on a bare false theta.

## 3. What this answers of Q11

Q11 asked three things. **Two are now decidable from held material.**

**(a) *"Is there a known mechanism attaching modular boundary data to the unquantized sector?"*
— PARTLY ANSWERED.** For Brieskorn spheres, **yes, and GM name it**: the logarithmic `(1,p)`
singlet. For **hyperbolic** manifolds, **GM themselves name it open, in print**, pointing at the
figure-eight surgeries specifically. So the honest reply to Q11's own *"if the answer is 'read
GPPV', that alone is worth the email"* is: **reading it says the hyperbolic case is open in the
literature — not that we failed to find it.**

**(b) *"Does it carry a character with `c_eff = 6`?"* — ANSWERED, NEGATIVELY, AND STRUCTURALLY.**
`Ẑ^unred = (false theta)/(q)_∞`; the numerator contributes `0`, the denominator `1`. **`6` is not
reachable by choosing a different 3-manifold in this family.** Changing `p` moves `c` by hundreds
and `c_eff` by a thousandth.

**(c) *"Is the obstruction general, or specific to the integer-level attachment?"* — NOT
ANSWERED, and this is the part that genuinely needs the expert.** But the question is now
**sharper than when it was asked**: the obstruction is **not amphichirality and not our knot** —
it is the *shape* `(false theta)/(q)_∞` that `Ẑ`-type invariants have. **Whether some other
boundary object escapes that shape is precisely what remains open.**

## 4. And why memo 171's `1` was right for the wrong reason

GC-6 read `c = 6` as six cusp-boson units of which the object supplies one. **Memo 171 found that
the `1` was `c_eff(η^{−1})` — a free boson used as a *model*, never the object** — and filed it as
a kind error. Correctly.

**The `1` is now the object's own**, and it is not a modelling coincidence: it is what
`(false theta)/(q)_∞` always gives, for every `p`. *Same number, different standing.* This is what
memo 189 §1 called the pattern of the programme in miniature — the answer was reachable all along
with what was on the shelf, and the instrument to reach it was not being fed.

## 5. What this costs the Dimofte dependency

**Q11's critical path is shortened, not removed.** What remains genuinely external is (c) alone,
and it can now be asked far more precisely than the original letter managed:

> *Given that `Ẑ^unred` is `(false theta)/(q)_∞` and therefore has `c_eff = 1` independent of the
> 3-manifold, is there any boundary object for a `CS = 0` cusped hyperbolic manifold that is NOT
> of that shape?*

**That is a one-line question with a yes/no answer, where the original was three paragraphs.**
Filed as **F191-1**: if a second letter is ever sent, this is what it should ask. **Not sent, not
drafted — R80-3 stands: nothing goes from Gmail.**

## 6. Named follow-up

**F191-2.** The same reading applied to `F_K` rather than `Ẑ`: GM §10.3 says *"`F_K(x,q)` should
give characters of some VOA modules"* — an expectation, not a theorem, and memo 190 has just made
`F_{m(5₂)}` available to arbitrary block depth. Whether the `F_K` side has the same forced
`c_eff` is a different question from the `Ẑ` side, and it is now computable here.

---

## ADDENDUM 1 (2026-09-09) — **the primary source confirms the bridge, corrects the citation, and hands §3(c) a concrete candidate**

`arXiv:1602.05302` (Gukov–Putrov–Vafa, *Fivebranes and 3-manifold homology*) — GM's **[38]** —
arrived. The body used GM Remark 3.8's restatement `Ẑ^unred = Ẑ/(q)_∞`. Checked at source:

```
GPV (6.49)   Zhat^(unred)_a = Zhat_a / (-qt; q)_inf          <- the REFINED object
GPV (6.50)   Zhat^(unred)_a |_{t=-1} = Zhat_a / (q;q)_inf    <- the unrefined limit
```

**Three things follow.**

1. **The bridge is confirmed** — the identity memo 191 runs on is real and is GPV **(6.50)**.
2. **GM's citation is slightly off**: Remark 3.8 cites *"[38, Equation (6.49)]"*, but (6.49) is the
   **refined** statement; the unrefined identity GM actually use is **(6.50)**. Recorded because
   R80-1 says check rather than assume, and because a later seat chasing (6.49) would find a
   different formula.
3. **§3(c) — the part left to the expert — now has a named candidate.** §3(c) asked *"is there any
   boundary object for a `CS = 0` cusped hyperbolic manifold that is NOT of the shape
   `(false theta)/(q)_∞`?"* **GPV's refined block is exactly such an object**: its denominator is
   `(−qt;q)_∞`, not `(q;q)_∞`, and it carries a second variable. **Memo 191's measurement is
   about the unrefined `t = −1` object only**, and says nothing about the refined one.

**And one physical reading worth recording**, in GPV's own words: the `(q;q)_∞` denominator *"can
be interpreted as the contribution of point-like instantons in twisted `N = 4` SYM on `R₊ × M₃`
realizing CS on its boundary."* **That is a physical account of precisely the factor that forces
`c_eff = 1`** — the `1` is instanton-counting, not the object's own conformal content.

**F191-3.** Measure the refined block. It is the first candidate for escaping the shape, it came
from the primary source rather than from speculation, and it is computable here.
