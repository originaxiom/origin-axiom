# B90 — the uniform peripheral reduction of degree=rank (Task 1b)

**Status:** Lemma 1 **PROVED uniform** (group algebra from the bundle relations); degree=rank **PROVED**
n=3,4; the fully uniform-`n` statement **REDUCED** to one named collapse-lemma. Standalone low-dim
topology / group theory; **no Origin-core claim**; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b90_degree_rank_peripheral.py`.

## The goal
degree=rank — `[A,B] = (−1)ⁿ⁻¹ μⁿ` on the principal figure-eight Dehn-filling component (`μ=A⁻¹t`, V46)
— is PROVED exact at n=3 (B71/V47) and n=4 (B89/V72). B77 showed the mechanism is **peripheral** (the
cusp), not the trace ring, but left the "why exponent = rank" derivation open. This stage makes the
peripheral mechanism **explicit and uniform in n**.

## Lemma 1 — the uniform peripheral identity (PROVED, any n, no spectrum)
The figure-eight bundle relations `tAt⁻¹=A²B`, `tBt⁻¹=AB` with `μ=A⁻¹t`, written via `t=Aμ` and
`B=A⁻²tAt⁻¹=A⁻¹μAμ⁻¹A⁻¹`, give by direct computation:
```
   (L1a)   λ := [A,B] = μ (Aμ⁻¹A⁻¹) μ (A⁻¹μ⁻¹A) = μ X⁻¹ μ Y⁻¹ ,      X = AμA⁻¹,  Y = A⁻¹μA
   (L1b)   X μ X⁻¹ = μ A                       (from tA⁻²tA = A⁻¹tAt, i.e. the 2nd bundle relation)
```
So the longitude is the explicit **cusp word `μ X⁻¹ μ Y⁻¹`** in the meridian and its A-conjugates, and
the bundle imposes the clean conjugation law `X μ X⁻¹ = μ A`. (L1a) uses only the first relation; (L1b)
is the second. Both are pure group-algebra consequences of the relations — **uniform in n, no spectral
assumption**. Verified here to ~1e-13 at n=3, ~1e-10 at n=4, and **L1b exactly over ℚ(ω)** on the B89
symbolic family.

## The reduction (degree=rank ⟺ one collapse-lemma)
```
   COLLAPSE-LEMMA:  L1a + L1b + (A satisfies its degree-n minimal polynomial)  ⟹  λ = (−1)ⁿ⁻¹ μⁿ.
```
- **Why exponent = rank.** `A` is `n×n`: its Cayley–Hamilton / minimal polynomial has **degree n**.
  Collapsing the A-conjugates `X, Y` in `μ X⁻¹ μ Y⁻¹` against the conjugation law (L1b) consumes exactly
  that degree-n relation, producing the n-th power `μⁿ`. The exponent is the rank because `A` is rank-n.
- **The sign** `c=(−1)ⁿ⁻¹` is the n-th root of unity forced by `det` (`cⁿ=det[A,B]/det(μ)ⁿ=1`, B77);
  verified `c=+1` at n=3, `c=−1` at n=4.
- The collapse-lemma is **PROVED at n=3** (B71, A-spectrum `{1,i,−i}`, `A⁴=I`) and **n=4** (B89,
  `{1,1,ω,ω²}`, `A³=I`), where A's explicit finite order makes the collapse a finite symbolic check. The
  fully uniform collapse (general n, A only constrained by `tr A=tr A⁻¹=1` + its degree-n CH) is the lone
  open item.

## Net
Task 1b is reduced: the peripheral identity (L1a, L1b) is **proved uniformly**, answering B77's open
"the mechanism is peripheral" with an explicit cusp-word identity; and degree=rank for all n is now
exactly the **collapse-lemma**, with "why n" answered structurally (A's rank-n Cayley–Hamilton). This is
the degree=rank analogue of B89-T's reduction of the tower to one module-iso: a single clean remaining
lemma, n≤4 in hand.

```bash
python frontier/B90_degree_rank_peripheral/probe.py
python -m pytest tests/test_b90_degree_rank_peripheral.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
