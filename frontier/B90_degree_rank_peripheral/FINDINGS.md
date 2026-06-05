# B90 — the peripheral form of degree=rank (Task 1b), CORRECTED after the CC-web audit

**Status (post-audit, honest):** one genuine uniform result (**L1b**), one tautology (**L1a**, relabelled),
one **refuted** mechanism ("exponent = rank from Cayley–Hamilton"). degree=rank stays **PROVED only at
n=3,4** (B71, B89); uniform-n is **OPEN** and is *not* reduced to "L1b + CH". Standalone low-dim topology
/ group theory; no Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b90_degree_rank_peripheral.py`.

> **AUDIT (2026-06-05, CC-web verification chat).** The original B90 framing — "Lemma 1 reduces
> degree=rank to a collapse-lemma; exponent = rank from A's degree-n Cayley–Hamilton" — overstated the
> result. Three decisive checks (run in `probe.py`) corrected the record. This file is the corrected
> version; the ledger carries the original V74 row plus a correction row (V75).

## What survives — L1b (genuine, proved uniform)
```
   (L1b)   X μ X⁻¹ = μ A ,     X = A μ A⁻¹ .
```
L1b is a real consequence of the bundle relations (it is the `(*)` equation `tA⁻²tA=A⁻¹tAt` of B89 with
`t=Aμ`), proved uniformly in n, and it **fails on a random non-bundle `(A,t)`** (dev O(10)). It is the
clean meridian form of the second bundle relation — the honest peripheral content of this stage.

## What was corrected
- **L1a is a TAUTOLOGY.** `λ=[A,B]=μX⁻¹μY⁻¹` (with `B:=A⁻²tAt⁻¹`, `Y=A⁻¹μA`) is a pure algebraic
  **rewriting** of the longitude — it holds for an *arbitrary* `(A,t)` pair, even when the bundle
  constraint fails (verified dev ~1e-10 on random non-bundle inputs). So L1a is **not** constraint
  content and does **not** count toward any reduction. (The original FINDINGS framed it as "derived from
  the bundle relations.")
- **"Exponent = rank = Cayley–Hamilton degree" is REFUTED.** The **hinge test**: both SL(4) Dehn-filling
  components satisfy L1b and both have 4×4 `A` (CH degree 4) — but the principal `{1,1,ω,ω²}` gives
  `M⁴=L` while the secondary `{prim 8th roots, z⁴+1}` gives `M³=L`. **Same n, same CH degree, L1b on
  both, different exponents (4 vs 3).** So the exponent is *not* determined by `L1b + degree-n CH`; it
  reads the specific (principal) A-spectrum. The CH mechanism for "why n" does not hold.

## Honest status
- The genuine result is **L1b** (the uniform meridian form of the bundle constraint).
- degree=rank `[A,B]=(−1)ⁿ⁻¹μⁿ` is **PROVED only at n=3,4** (B71, B89); the uniform-n statement is OPEN
  and is **not** reduced to L1b + CH (refuted by the secondary component).
- The real open question, sharpened: **why does the principal spectrum (and not the secondary) give
  exponent = n?** L1b is component-blind, so the mechanism must read the A-eigenvalue structure (the cusp's
  cyclic boundary holonomy / root-orders, cf. B88's degrees {3,4}) — **not** Cayley–Hamilton. This is the
  honest continuation (pairs with the secondary-component degree question, B88/Task D).

## Verdict per the discipline
This is a **reformulation**, not a reduction: L1a is a tautology and the CH-exponent claim is refuted;
only L1b (genuine, uniform) is new content. Banked honestly as a corrected negative.

```bash
python frontier/B90_degree_rank_peripheral/probe.py
python -m pytest tests/test_b90_degree_rank_peripheral.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
