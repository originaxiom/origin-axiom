# B138 — S031: the principal-image direction proved; the SL(4) obstruction

A "push further" on the **S031** sealing capstone.

**(1) Principal-image direction — PROVED (all n).** The principal `Sym^{n−1}` image of an SL(2) rep over `K` has all
word-traces in `K` (since `Sym^d` is ℤ-defined: entries of `Sym^d(g)` are integer polynomials in g's entries). So the
metallic SL(2) fixed point (over `K_m`: ℚ(√−3) for m=1, ℚ(i) for m=2) lifts to a `K_m`-sealed SL(n) fixed point for
every n. Verified symbolically n=2..5, both m=1, m=2. This is the *easy half* of S031; the converse (nothing else
escapes) is open.

**(2) SL(4) bulk obstruction.** The B137-style off-sublocus root-find at SL(4) is intractable in-session: a faithful
340-word residual is too slow to converge; a lighter one under-pins the SL(4) character. SL(4) sealing evidence not
obtained — needs a complete SL(4) trace-coordinate set or a symbolic component analysis (NEEDS-EXPERTISE).

**(3) Object-clarification.** S031 concerns **discrete trace-map fixed points** `(A^mB,A)` (B129/B137), not B71's
**positive-dim geometric** components (V0/W1/W2). A generic geometric-component point has continuous traces (no number
field) — so `realize_bundle_rep` doesn't test sealing (it returned "OTHER"). Banked so the conflation isn't repeated.

```
python frontier/B138_s031_principal_lemma/probe.py
python -m pytest tests/test_b138_s031_principal_lemma.py -q
```

**S031 status:** principal direction PROVED; SL(3) sealing verified m=1 (B129), m=2 (B137); SL(n≥4) + the all-n
converse OPEN. **Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B137 untouched. See `FINDINGS.md`; ledger
**V127**.
