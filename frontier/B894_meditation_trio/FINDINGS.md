# B894 — THE TORSION-PRIME BRIDGE (M4) + the four-column exponent ledger (M6 keystone)

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** computed, exact integer arithmetic throughout

## The question (M4)

The solo seat's adjoint torsion τ_ad and the charge cubic μ come from opposite
ends of the programme — τ from the twisted Alexander tower on the knot side
(B581, banked per-block values), μ from the e₆ enhancement pencil (B866/B854).
Do their prime supports know each other? Hypothesis on the table: τ_ad's primes
≤ 13 are exactly the charge-field primes.

## The computation (`m4_bridge.py` → `m4_bridge.json`)

All inputs are the **banked** B581 block torsions τ_m for m ∈ {1,4,5,7,8,11}
(repo-official; their product equals the solo-tier τ_ad — verified exponent by
exponent), against disc(μ) = 2³²·3¹⁰·5²·7³·11·13⁶.

**Result 1 — SUPPORT IDENTITY (TRUE).** The small-prime block (p ≤ 13) of
τ_ad = ∏ τ_m is

> 2⁶¹ · 3²⁰ · 5⁵ · 7¹⁷ · 11⁴ · 13⁵ — support {2, 3, 5, 7, 11, 13}

and supp(disc μ) = {2, 3, 5, 7, 11, 13}. **Equal as sets.** The torsion tower's
small primes are exactly the charge-cubic's primes — no charge prime missing
from the tower, no small tower prime absent from the discriminant.

**Result 2 — NO EXPONENT IDENTITY (honest negative).** 7¹⁷ vs 7³, 13⁵ vs 13⁶,
2⁶¹ vs 2³² — no divisibility in either direction, also not for the
measured-pair product τ₄·τ₈ (small block 2²¹·3⁴·5·7⁴·11·13). The bridge is a
**support-level** fact, not an arithmetic identity. Verdict phrasing:
*support identity, exponents unrelated at first order*. The 7/11/13 entry
pattern already banked in B581 (11 first divides τ_m at m = 7; 13 at m = 5;
7 saturates all m ≥ 4) is the registered follow-up mechanism.

Base-rate honesty: {2,3,5,7,11,13} is the six smallest primes, so a support
match alone is weak evidence; what makes it non-vacuous is the *converse*
direction — τ_ad contains twelve further primes (17…160453) and **none of them
enters disc(μ)**; the cut at 13 is clean on both sides.

## The keystone (M6): the four-column ledger closes

With B893's signature census this session, four independently banked structures
now agree on which two of the four torus charges are measured:

| torus slot | exponent m | θ-parity (B353/B581) | sign τ_m (B581) | ad-spectrum (B893) | role |
|-----------|-----------|----------------------|-----------------|--------------------|------|
| x₈  | 4  | **odd**  | **+** | **split (real)** | **measured** (FMT plane) |
| x₁₆ | 8  | **odd**  | **+** | **split (real)** | **measured** (FMT plane) |
| x₁₄ | 7  | even | − | compact (imaginary) | unmeasured; 7 → resolvent |
| x₂₂ | 11 | even | − | compact (imaginary) | unmeasured; 11 → resolvent |

- The B581 sign law ("τ_m > 0 exactly at the θ-odd exponents") was banked
  **before** the FMT selected ⟨x₈, x₁₆⟩ as the measured plane. The torsion
  signs mark the measured plane in advance.
- The unmeasured pair's exponents multiply to **77 = 7·11 = the squarefree
  discriminant part shared by all three cubics** (B888) — the resolvent field
  ℚ(√77) is built from exactly the unmeasured slots.
- The golden 5 is in neither column: it is **model-borne, not ramified** —
  disc μ carries 5² through the integral model ℤ[t]/μ while **5 ∤ disc K =
  6237 = 3⁴·7·11** (5 is unramified in K and in the whole S₃ closure,
  splitting with shape [1,2], the value primes' shape); τ₅ is the
  {2,3,5,7,13}-smooth block — the third, non-slot channel. *(Corrected
  2026-08-18: this line formerly said "it enters by ramification"; see the
  addendum below.)*

**Claim discipline:** each column is a banked theorem or banked computation;
the *concordance* is the new object. It is a finite check (4 slots × 4
columns), locked in `tests/test_b894_bridge.py`. No physics reading enters the
claim; the observer-reads-the-split-directions sentence stays in B893's
firewalled paragraph.

## Files

- `m4_bridge.py` → `m4_bridge.json`
- Locks: `tests/test_b894_bridge.py`

## Depends on

B581 (block torsions + sign law), B866 (μ, disc μ), B854/P69 (the FMT plane),
B888 (77 = the shared resolvent), B893 (the signature census).

---

## ADDENDUM 2026-08-18 — the ramification clause corrected (audit-seat catch, bench-verified)

The audit seat's relay of 2026-08-15 caught that this file's third-channel line (and its
echoes in `THEOREM_LEDGER` C28, `LAW_MAP`'s concordance row, and the M6 line of
`STRUCTURE_TO_NATURE_MASTERPLAN`) misnamed where the golden 5 lives. Verified on this
bench by independent computation (sympy, exact; not the audit seat's script):

- **The reduced model.** K = ℚ[t]/μ ≅ ℚ[x]/(x³ − 12x − 5) — the isomorphism is real
  (μ acquires a linear factor over ℚ(β), β a root of the reduced cubic), the model is
  monogenic (index 1 by Dedekind at 3: f ≡ (x+1)³ mod 3, criterion gcd = 1), so
  **disc K = 6237 = 3⁴·7·11**, squarefree part 77 — C28's resolvent clause now has a
  one-line derivation.
- **The correction.** A ramified prime divides the field discriminant; **5 ∤ 6237**. In
  K the prime 5 is unramified with splitting shape [1,2] — *the same shape as the value
  primes 953, 1129, 421493* — and it is unramified in ℚ(√77) (77 ≡ 1 mod 4, disc 77),
  hence in the entire S₃ closure. The 5 that M6 saw is real but **model-borne**:
  disc μ = 2³²·3¹⁰·5²·7³·11·13⁶ vs disc K = 3⁴·7·11 — the 5² (and the 13⁶; 13 is inert,
  and 2³² likewise: 2 is unramified) belong to the non-maximal integral model ℤ[t]/μ,
  a property of how the pencil was normalised, not arithmetic of the field.
- **Scope.** The keystone is untouched: the concordance is support-level, and
  5 ∈ supp(disc μ) is true. Only the word "ramification" was wrong. The dependents sweep
  (this bench, full-corpus grep): no argument anywhere treats 5 as an arithmetic
  invariant of K; the sweep-ledger row 6's channel name is renamed in place. B888's own
  priced next step ("the field discriminants proper, vs polynomial discs") is exactly
  the computation that decided this — part-paid today.
- **Registry.** `ERROR_LEDGER` E41 (model invariant read as field invariant);
  `RETRACTED_PHRASES` row 9; lock `tests/test_c28_ramification.py`.
