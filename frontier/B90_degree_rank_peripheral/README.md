# B90 — the peripheral form of degree=rank (Task 1b), CORRECTED after the CC-web audit

The original B90 framing ("Lemma 1 reduces degree=rank to a collapse-lemma; exponent = rank from
Cayley–Hamilton") overstated the result. After the CC-web audit, the honest content is:

- **`probe.py`** — runs the three audit checks:
  - **L1b** `XμX⁻¹=μA` (`X=AμA⁻¹`) is **genuine** (fails off the bundle constraint), proved uniform —
    the clean meridian form of the second bundle relation.
  - **L1a** `λ=μX⁻¹μY⁻¹` is a **tautology** (holds on random non-bundle `(A,t)`) — a rewriting, not content.
  - **the hinge test** — both SL(4) Dehn-filling components satisfy L1b and both have 4×4 A (CH degree 4),
    but give **different exponents** (principal `M⁴`, secondary `{prim 8th}` `M³`) ⇒ **"exponent = CH
    degree = rank" is REFUTED**.
- **`FINDINGS.md`** — the corrected record.

**Net.** degree=rank `[A,B]=(−1)ⁿ⁻¹μⁿ` stays **PROVED only at n=3,4** (B71, B89); uniform-n is **OPEN**
and is *not* reduced to L1b + CH. The genuine new content is **L1b** alone. The sharpened open question:
why does the *principal* spectrum give exponent = n (the secondary does not) — a spectrum/root-order
question (cf. B88), not Cayley–Hamilton.

```bash
python frontier/B90_degree_rank_peripheral/probe.py
python -m pytest tests/test_b90_degree_rank_peripheral.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
