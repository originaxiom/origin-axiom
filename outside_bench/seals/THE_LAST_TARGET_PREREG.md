# PREREGISTRATION — t12835, the one target B1330 left uncomputed

*Outside bench, 2026-09-14. Sealed before t12835 is run. Gate 5 untouched.*

## What this is, and what it is NOT

Phase 3 filed **BENCH ERROR #34**: this branch is a strict subset of the record (1246 arcs vs 1281), and
two claims of this bench were read off the gap. **This cell begins by applying the fix that error
demands** — read the sibling branch *before* calling anything unrun — and the fix immediately paid:

**B1330's "NOT DONE: s958, t12833 and t12835 … are named, not computed" is itself stale.** Two addenda
dated **2026-09-11** computed them:

| manifold | addendum | result |
|---|---|---|
| **s958** | ADDENDUM 1 (over ℚ(ω)) and ADDENDUM 2 (over ℚ(ζ₁₂)) | **20 exact in-domain sectors, 8 at t₀ ≥ 2, every index zero** |
| **t12833** | ADDENDUM 2 | **16 exact sectors, t₀ to 4, 12 at t₀ ≥ 2, zero** |
| **t12835** | ADDENDUM 2 | *"(pending at write time; its odd-power non-zeros are the same artifact)"* |

**So exactly one target remains, and it is t12835.** Had this cell been planned without reading the
sibling branch, it would have recomputed two settled manifolds and called it new — #34 for the second
time in one session.

## The near-miss this cell must not repeat, in B1330's own words

> The first exact run reported **NON-ZERO INDEX: 10** on `t12833` and again on `t12835`. Values of
> `I = -2, -4, -6`. Taken at face value that is falsifier 6 firing … **It was wrong, and the record's
> own banked theorem caught it.** T5 says `t_0 = 0 ⇒ I = 0` … The run reported `t_0 = 0` with `r_1 = 2`.
> **Impossible.**

**The cause: t12835's holonomy is a projective (PSL₂) lift** — its relators evaluate to **−I**, and on
`Sym^m` with m **odd**, −I acts as −1, so Fox calculus (which assumes a genuine homomorphism) is
invalid. B1330's fix is the `GERMS` list: **even powers only**.

> `t12835   'aaBcbac' -> -I    'aCAbcaCAbcaaaBB' -> -I     projective`

## Method — B1330's own code, vendored UNCHANGED

`outside_bench/certificates/lib/b1330/{q12.py, recog12.py, final_index.py}`, byte-identical to
`origin/claude/paper-verification-ufp0zn:frontier/B1330_the_best_case_object/verification/`, with the
source commit recorded in `PROVENANCE.md`. **No line is modified.** The script already defaults to
exactly these three manifolds and already carries the even-only `GERMS` list.

## THE TWO OUTCOMES

- **A — every in-domain sector on t12835 vanishes.** B1330's "NOT DONE" line is discharged, the last of
  the four best-case objects joins the others, and the vanishing stands on all four.
- **B — some in-domain sector has I ≠ 0**, with relators validated as ±I, even germs only, and the
  identities intact. That would be the first live positive in characteristic zero on a real manifold.

## CONTROLS

| # | control | catches |
|---|---|---|
| **V1** | **s958 and t12833 are re-run FIRST on the vendored path and must reproduce the addendum's banked numbers** (s958: every index zero; t12833: 16 sectors, t₀ to 4, 12 at t₀ ≥ 2, zero) — **a failure stops the cell** | a method that drifted in transit; without it a fresh null on t12835 means nothing |
| **V2** | **the relator images are printed for every manifold** before any twisted computation — B1330's own lesson: *"Always print the relator images before trusting a twisted computation. A −I lift silently invalidates every odd-weight germ."* | the exact failure that produced the false NON-ZERO INDEX: 10 |
| **V3** | **T5 is asserted on every sector**: `t₀ = 0 ⇒ I = 0`. A sector reporting t₀ = 0 with I ≠ 0 is **impossible** and fails the cell rather than being reported | the false positive, caught the way B1330 caught it |
| **V4** | the in-domain population is printed before any conclusion; **at least one sector must be in-domain** | the `B1197` vacuity trap |

## WHAT THIS CELL MAY NOT CONCLUDE

**Nothing about generations** — I-26 is **UNEARNED**. **Nothing about a net chiral spectrum.** And it
must not be sold as a live test of the vanishing: since B1330 was written, **B1334 has PROVED I = 0 on a
stated domain**, and **B1331/B1332 reduced the one-cusped case to ISOTROPY**, which has held across 128
genuine scalar equations on six further manifolds with zero non-isotropic. **A sixth zero is bookkeeping,
not news**, and this cell says so in advance. No value. Gate 5 untouched.

---

# ADDENDUM 1 (2026-09-14) — "BOOKKEEPING, NOT NEWS" WAS TOO WEAK, AND THE REASON IS COMPUTABLE

The seal above rated t12835 **"bookkeeping, not news"** on the grounds that **B1334 has PROVED I = 0 on
a stated domain**. That rating is **wrong on these manifolds**, and the correction is arithmetic.

**B1334's theorem quantifies over S⁰** — the identity component of
`S = Hom(H₁(M)/⟨peripheral⟩, ℂ*)`, *"a torus of dimension rank(H₁(M)/⟨peripheral⟩)"*. So its reach on a
given manifold is decided by that rank. Computed here, on the four best-case objects:

| manifold | H₁ | gens | rank(rels + peripheral) | **rank(H₁/⟨peripheral⟩)** |
|---|---|---|---|---|
| s958 | ℤ/3 ⊕ ℤ | 3 | 3 | **0** |
| t12833 | ℤ/6 ⊕ ℤ | 3 | 3 | **0** |
| t12835 | ℤ/6 ⊕ ℤ | 3 | 3 | **0** |
| v2873 | ℤ/6 ⊕ ℤ | 2 | 2 | **0** |

**Rank 0 means S⁰ is a single point — the trivial character.** So on exactly these manifolds **B1334's
theorem covers χ = 1 and nothing else**, and **every order-3 cusp-trivial sector — which is the entire
reason these are the "best-case" objects — lies OUTSIDE the proof.**

This agrees with, and makes concrete, B1332's own framing: *"B1334's addendum leaves isotropy as the
ONLY live route for the one-cusped case."* **The computed reason it leaves it open is that the
one-cusped best-case objects have rank(H₁/⟨peripheral⟩) = 0.**

**The corrected rating.** t12835 is **not** a sixth confirmation of a theorem that already covers it. It
is the last un-run member of the only family where the vanishing is observed but **unproved**, in
sectors no banked theorem reaches. That is a higher value than the seal first assigned — and the
correction is recorded here, before the result is known, rather than after.

**What does NOT change:** the outcomes A/B, every control, and every fence. In particular B1331/B1332's
isotropy evidence still stands and still holds across 128 scalar equations, and a null on t12835 is
still a null, not a proof. **No value. Gate 5 untouched.**
