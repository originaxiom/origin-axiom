# B138 — S031: the principal-image direction PROVED (all n); the SL(4) bulk obstruction; an object-clarification (V127)

A "push further" on the **S031** sealing capstone (the metallic SL(n) trace map fixes only the `Sym^{n−1}` image of its
SL(2) fixed point; the SL(n) fixed-point traces lie in the SL(2) trace field `K_m`). Two pieces and one honest
obstruction. MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B137 untouched.

## (1) The principal-image direction — PROVED (all n)

The **easy half** of S031, now stated and proved:

> **Lemma.** The principal `Sym^{n−1}` image of an SL(2) representation defined over a field `K` is itself a trace-map
> fixed point with **all word-traces in `K`**.

**Proof.** The symmetric-power functor `Sym^d` is defined over ℤ — the matrix entries of `Sym^d(g)` are integer
polynomials in the entries of `g` (its action on degree-`d` monomials). Hence `g ∈ SL(2,K) ⟹ Sym^{n−1}(g) ∈ SL(n,K)`,
and every word-trace `tr(W(Sym^{n−1}(A), Sym^{n−1}(B))) = tr(Sym^{n−1}(W(A,B))) ∈ K`. The metallic SL(2) fixed point
lives over `K_m` (m=1: ℚ(√−3); m=2: ℚ(i)), so its principal image is a `K_m`-sealed SL(n) fixed point, for **every n**.
**∎** Verified symbolically for n=2..5, both arithmetic members (m=1 ℚ(√−3), m=2 ℚ(i)).

This proves the **Sym-image component always seals**. The open **hard half** is the converse — that *nothing else*
escapes `K_m` (the uniqueness, all n). SL(3) full sealing is computationally verified: m=1 (B129), m=2 (B137).

## (2) The SL(4) bulk obstruction (honest negative)

Attempting the **B137-style off-sublocus root-find at SL(4)** — find SL(4) trace-map fixed points
`tcoords(A,B)=tcoords(A^m B, A)` and test escape from `K_m` — is **intractable in-session**:
- a *faithful* separating residual (word-traces over `{A,B,A⁻¹,B⁻¹}` up to length 4 = 340 words) makes `least_squares`
  too slow to converge across enough starts (timed out >20 min);
- a *lighter* residual **under-pins** the SL(4) character (too few traces ⟹ convergence to spurious points), so the
  irreducibility (algdim=16) / escape classification is unreliable.

SL(4) sealing evidence was **not obtained**. The clean path needs a proper **complete SL(4) trace-coordinate set**
(à la Lawton for SL(3)) or a symbolic component analysis — future work / NEEDS-EXPERTISE.

## (3) Object-clarification (corrects an in-session mis-conflation — banked so it is not repeated)

S031's "fixes only the `Sym^{n−1}` image" is about the **discrete fixed points of the trace-map automorphism**
`φ_m(A,B)=(A^m B, A)` (B129/B137: saddles, isolated; among them the only genuine *irreducible* one is the `Sym^{n−1}`
image). This is **not** contradicted by B71's V0/W1/W2 (the SL(3) figure-eight **geometric** character variety has 3
positive-dimensional components) — those are components of the **bundle** character variety, a *different object*. A
generic point on a positive-dim geometric component (e.g. `realize_bundle_rep`) has **continuously-varying** traces (no
single number field), so it is **not** a B137-style discrete fixed point and must **not** be used to test `K_m`-sealing
(this is why the known-SL(4)-rep trace-field check returned "OTHER"). *(Recorded because this conflation was made and
caught in-session — a verify-don't-trust note on the reasoning, not just the claims.)*

## S031 status after B138

| piece | status |
|---|---|
| principal-image direction (Sym^{n−1} seals, all n) | **PROVED** (B138) |
| full sealing, SL(3), m=1 (ℚ(√−3)) | computationally verified (B129) |
| full sealing, SL(3), m=2 (ℚ(i)) | computationally verified (B137) |
| full sealing, SL(n≥4) | **OPEN** (bulk intractable in-session) |
| the all-m, all-n converse (the theorem) | **OPEN** |

## Reproduce

```
python frontier/B138_s031_principal_lemma/probe.py
python -m pytest tests/test_b138_s031_principal_lemma.py -q
```

Pure sympy (no heavy deps); runs unconditionally.

**Tier.** MATH (low-dim topology / representation theory). Updates `speculations/S031` (principal direction proved; the
SL(4) obstruction + the object-clarification). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B137 untouched. Ledger **V127**.

**Anchors:** `speculations/S031` (the capstone), B129/`K012` (m=1 SL(3) sealing), B137 (m=2 SL(3)), B71 (the geometric
SL(3) components — the *other* object), `K003`/`K005` (the principal embedding / Sym tower). External: Lawton (SL(3)
trace coordinates — the missing SL(4) analogue is the obstruction).
