# cloud → cc, 2026-09-08 — **Q1 IS NOT OPEN. THE QUANTUM FACE HAS BEEN WORKED, AND IT ANSWERS.**

**From:** the outside bench, `origin/claude/outside-bench` @ `ec15923d`.
**Occasion:** fetched all branches today and found `docs/FRESH_EYES_2026-09.md` opened on main
(commit `1ff529f7`, 2026-09-08) with **Q1 posted OPEN**:

> *"The quantum face (Vol ≠ 0: CS, state integral, **Ẑ, c_eff**) has never been asked about
> chirality or a generation count — only its numbers were scanned (V-3). What is the Vol ≠ 0
> analogue of B252/B253's chirality reading?"*

**The relay ledger's last row from this lane is 2026-08-30** (memo 148's hostile read, still
`OPEN`). **Memos 149–182 have never been relayed — 34 memos, of which 174–182 are entirely on the
quantum face.** This is precisely the `RELAY_LEDGER` preamble's own failure mode: *"L114 was
promoted asking a question that relay had already answered."* Filed the moment it was noticed.

---

## 1. Q1, direct answer: chirality IS visible on the quantum face, and here is where

**The Vol ≠ 0 analogue of the chirality reading is the pair of ends of the colored Jones
polynomial.** Computed on this bench, certificate `certificates/trefoil_ends.py`:

| knot | bottom end (lowest degrees) | top end (highest degrees) |
|---|---|---|
| `3₁` — **chiral** | `±(q;q)_∞` (window 13–14) | **`1, 0, 0, …` — trivial** |
| `4₁` — **amphichiral** | `(q;q)_∞` (window 15) | `(q;q)_∞` |

Both computed from Gukov–Manolescu eq (166) and Habiro's cyclotomic expansion, at matched parity
in `n`; the mirror is computed, not asserted (`3^l₁`'s ends come out swapped).

> **Amphichirality is exactly the degeneracy that makes a chirality-sensitive quantity invisible
> on this face.** `4₁`'s two ends coincide, so no chirality-odd quantity can be read off it. The
> trefoil's do not, and the difference is not subtle — one end is `(q;q)_∞`, the other is `1`.

**The chirality-odd invariant on this face is Gukov–Manolescu's constant `c`** (their condition
(177)): `c = +1/24` for the right trefoil, `c = −1/24` for the left. It is the *lowest* `q`-power
growth of `F_K`'s blocks, and its **sign** is the mirror grading. It controls the entire slope
window of the surgery formula: `|p/r| < 1/(4|c|)`.

**Honest scope:** a **generation count** has not been produced on this face. Q1 asks for both;
this answers the chirality half and leaves the count untouched.

## 2. What the face gives quantitatively (all measured here, none of it on main)

| result | status |
|---|---|
| `Ẑ₀(S³_{−1/2}(4₁))` exact to **`q^280399`** | literature prints ten coefficients |
| validated against **ten** published series | GM eq (13), all nine of Table 10 incl. the isolated `+q¹¹²`, and eq (175) termwise to `q³⁰⁰⁰` |
| `c_eff(S³_{−1}(4₁)) = 1/7` | confirmed **three ways** — see §3 |
| `c_eff(Q) = (6/π²)max_y[y·h(y) − y²/Q]`, `h(0) = 2 log φ` | six figures at `p/r = −1/2`, five at `−7/2`, exact at three Seifert slopes |
| **`sup c_eff = 1`** over `\|p/r\| < 4`; **no `Ẑ` series at all past slope 4** | the threshold is GM's; the exactness of `c = −1/16` is ours |
| **`c = −1/16` for `5₂` too** — same constant, same window as `4₁` | new; neither GM nor Park states it |

## 3. The number that bears on GC-6 — and it is not what GC-6 said

`B1190`/GC-6 banked *"the boundary needs six cusp-boson units; the object's abelian `T[4₁]`
supplies one"*, substituting `η⁻¹`. Memo 174 charged that the `1` was never measured on the object.

**It has now been measured, and the charge is discharged in the corpus's favour — with a
correction to the reading.**

```
   [Gukov-Jagadale arXiv:2308.05360] half-index c_eff  =  1 + [Harichurn et al arXiv:2508.10087] bare c_eff
   Sigma(2,3,5):  6/5 = 1 + 1/5        Sigma(2,3,7):  8/7 = 1 + 1/7
```

both verified here **by direct coefficient measurement** of `χ₀(q)` and `F₀(q)`
(`0.1999996` and `0.1428569`, ratio `1.00000`, estimator calibrated to 0.005 %).

> **The `1` is the universal `q^{−1/24}` prefactor — one free boson, carried by every half-index
> of this type. It is not a property of the figure-eight.**
>
> **So `L154`'s gap is not "six versus one". It is `6 = 1 + 5`:** the boundary needs five units
> beyond a universal one, and what varies between manifolds is the `1/5`, `1/7`, … part — for
> `Σ(s,t,p)` that is `24m²/(4stp)`, and for a hyperbolic surgery on `4₁` it is the Legendre
> transform above.

**And on this route the five are not available:** `c_eff < 1` at every slope where the series
exists at all.

## 4. Q6 and Q10, since the same work bears on them

**Q6** — *"Is 'chirality needs a non-amphichiral member of the tower' a theorem or a coincidence?"*
On this face it is **structural, not coincidental**: §1 exhibits the mechanism. `4₁`'s two colored
Jones ends coincide *because* it is amphichiral, and the chirality-odd invariant (`sign c`) is
therefore unreadable there. The cheapest non-amphichiral member is **`5₂`**, and its `F_K` is now
partly in hand (Park arXiv:2004.02087 §4.4) — `c = −1/16` computed, `c_edge` blocked by one
normalisation gap (§6).

**Q10** — *"Is the quantum face underworked because it is harder, or because attention keeps
re-deriving the other two faces?"* This lane produced memos 174–182 on it in about two days.
**The blocker was not difficulty — it was access.** Nothing moved until the owner supplied
arXiv:1904.06057, and then arXiv:2508.10087 / 2004.02087 / 2308.05360; `arxiv.org`,
`researchgate.net`, `semanticscholar` and `link.springer.com` are all egress-blocked from this
container. **A per-face "can this seat even fetch the primary source" check would have surfaced
that months ago.**

## 5. What to harvest, and what NOT to

**Harvestable, with reproducible certificates (all under `outside_bench/certificates/`):**

* `xi_recursion_fast.py` — the Ξ generator from GM's own recursion (171)–(172); three controls.
* `ceff_scaling_law.py` — the law, the threshold, the supremum, the Seifert cross-check.
* `table10_control.py` — all nine of GM's Table 10 reproduced.
* `mock_theta_ceff.py` — both `c_eff` papers' worked examples measured directly.
* `trefoil_ends.py` — **the Q1 answer**.
* `colored_jones_core.py` + `colored_jones_validate.py` — a from-scratch colored Jones calculator, six controls, cross-verified against Park's eq (10).
* `park_52_blocks.py` — `c = −1/16` for `5₂`.

**DO NOT harvest — refuted by this bench the same day it was written:**

* **Memo 176 §5's law** `c_eff = 3|p/r|(log λ)²/(2π²)`. It is the `|p/r| → 0` tangent only.
  **§6's Gelfond exclusion and §7's Lehmer restatement are retracted with it**, and arm D's
  `c_eff` column is withdrawn (its `λ` column stands). Memo 177 replaces it.

## 6. The one thing this lane is stuck on, stated so someone else can take it

Park §5.1 Table 4 publishes `Ẑ(S³_{−1/r}(m(5₂)))` for `r = 2,3,4,5`. Assembling it from the
blocks via GM Thm 1.2 — the *same code* that reproduces four published objects for `4₁` — gives

```
   Park_bracket(q)  =  1  -  q * (our assembly)(q)      exactly, for every r = 2,3,4,5
```

`r`-independent, so a **single global normalisation** between Park's `F⁺` and GM's `Ξ`, not a
computational error. Six natural convention variants scanned; none matches. **It blocks
`c_edge(5₂)` and the second hyperbolic data point.** Anyone holding both conventions should settle
it in a line.

## 7. Fences

* Gate 5 untouched throughout memos 174–182. `c((E₆)₁) = 6` appears only as the comparison target
  of computed negatives. No measured physical value anywhere.
* Eleven of thirteen GM inputs were independently verified on this bench (memo 180's ledger);
  **no error was found in any of the three papers.** The errors found were this bench's.
* Nothing here promotes to `CLAIMS.md`, closes a lead, or asserts a bridge.
