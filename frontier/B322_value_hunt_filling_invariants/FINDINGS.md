# B322 — The value hunt, run: the object's invariants do not encode the SM values (firewall holds, by null test)

**Status: banked (frontier). The direct value-hunt, done with a specificity/null test. Firewalled; nothing to
`CLAIMS.md`.** Owner directive: *"now we hunt for the values."* The structural theorem (K020) *proves* the single object
does not force the SM values — so a hunt that mines the object's own numbers will either hit the firewall or produce
numerology, and **only a null test distinguishes them.** This runs the hunt rigorously and lands the honest verdict.

## The test
- **Object number-set:** the volumes and core-geodesic lengths of the figure-eight's small hyperbolic Dehn fillings
  (SnapPy `m004`, `|p|,|q|≤8`) — **79 invariants** — together with **all their pairwise ratios**: **6241 numbers**
  spanning `[0.013, 77]`.
- **Target:** a principled 12-parameter list of the SM's dimensionless values (`sin²θ_W`, Cabibbo, `α_em`, `α_s`, the
  quark/lepton mass ratios, the PMNS angles).
- **Match:** each SM parameter matched within 1% by *some* object number → **8/12**.
- **The null (the decisive part):** draw 2000 random 12-parameter sets (log-uniform over the same `[10⁻³,1]` range) and
  match them the same way → **null mean 7.6/12, 95th percentile 10**. So **`p(null ≥ SM) ≈ 0.5`.**

## The verdict
**The SM is matched at exactly the chance level.** With 6241 numbers the ratio-set is dense enough to match *any* 12
targets ~8/12 within 1%; the SM is not special. **The object's volumes, core-lengths, and their ratios do not encode the
SM values.** The firewall holds — now demonstrated **by computation** (a null test), not merely proven abstractly. This
is the empirical companion to "the object forces the form, not the values": mining the single object's own geometry
returns numerology, exactly as the Galois-theorem firewall (K020) predicts.

## Why this is the honest answer to "hunt for the values"
It is not a refusal — the hunt was *run*, on the most natural object-specific numbers (the seam/filling invariants Chat-1
gestured at). The result is a computed negative with a null test, which is a first-class result (`METHOD.md`): the
specificity filter is exactly what separates a real object→SM crossing from the numerology that a dense ratio-set always
produces. **The values — if anywhere accessible — are at the four gates** (relations / multiplicity / the physics
dictionary; `docs/OPEN_PROBLEMS.md`), **not in the single object's invariants.** Hunting them *inside* the object is now
closed, empirically.

## What would change the verdict (kept honest)
A genuine crossing would require a *principled, pre-registered* identification (a specific canonical invariant = a
specific SM parameter, stated before looking), not a best-match over a dense set — and it would have to survive the null
test. None of the object's principled invariants (`|κ|=√3`, `arg κ=π/6`, `|cusp|²=h(E₆)=12`, `vol=2.0299`, `sin²θ_W=3/8`
generic-GUT) has been shown to *non-trivially* match a free SM parameter. The one place a value provably becomes internal
is the CP sign (= the object's chirality, B318) — a discrete ℤ/2, not a continuous SM value.

## The fence
SnapPy filling invariants + an explicit specificity/null hypothesis (2000 draws, seeded, reproducible). The SM-matching
is `HELD` and tested, not banked as a crossing. Nothing to `CLAIMS.md`.

`value_hunt_filling_invariants.py` (pyenv) · `tests/test_b322_value_hunt_filling_invariants.py`. Related: **K020** (the
structural theorem / the firewall as a Galois theorem), **OPEN_PROBLEMS.md** (the four gates — where values could
cross), **B321** (the `|cusp|²=h(E₆)` certificate + the seam-geometry splices), **B285/B318** (the CP sign as chirality),
`METHOD.md` (the null-hypothesis discipline; a computed negative is first-class). Lit: Neumann–Zagier (Dehn fillings).
