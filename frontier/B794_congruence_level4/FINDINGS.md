# B794 — Γ₄₁ IS A CONGRUENCE SUBGROUP OF LEVEL (4); the mod-4 trace law PROVED

**Provenance: both theorems are cc3's** (audit seat, its `1757d6d5`). cc3 never merges; per the
standing rule they are re-derived here from scratch under a new number — `verify_congruence.py`
takes nothing from cc3's script. Gate 5 + Gate 5-Q binding. **Nothing here reaches CLAIMS.md.**

## The theorems (verified independently, every step reproduced)

> **THEOREM 1 (congruence).** Γ₄₁ is a **congruence subgroup of level exactly (4)**:
> Γ(4) ⊆ Γ₄₁, and Γ(2) ⊄ Γ₄₁.

> **THEOREM 2 (trace law).** For every γ ∈ Γ₄₁, **N(tr γ) ≡ 0 or 3 (mod 4)** — never 1.
> Hence every m004 geodesic trace norm avoids 1 mod 4, **at every cutoff**.

Proof shape (finite computation, no citations): reduce mod 4 in ℤ[ω]/4 (2 is **inert**, so the
residue field is 𝔽₄ and |ℤ[ω]/4| = 16); check the Bianchi generators surject onto SL(2,ℤ[ω]/4);
compare indices; enumerate traces.

| step | value | check |
|---|---|---|
| \|SL(2,ℤ[ω]/4)\| | **3840** | = the bank's `ambient_order` |
| \|PSL(2,ℤ[ω]/4)\| | **1920** | = the bank's coset-image order, verified in B791 |
| ⟨T,U,S⟩ mod 4 | 3840 | reduction is **surjective** |
| \|H = ⟨A,B⟩ mod 4\| | 320, −I ∈ H, \|H̄\| = 160 | |
| [PSL(2,ℤ[ω]/4) : H̄] | **12** = [PSL(2,O₃):Γ₄₁] | ⇒ Γ₄₁ = preimage(H̄) ⇒ **Theorem 1** |
| \|H mod 2\| | 10 (= D₅ < A₅), index **6 ≠ 12** | ⇒ Γ(2) ⊄ Γ₄₁ ⇒ level is **exactly** (4) |
| trace norms mod 4 | **{0, 3}** | 1 absent ⇒ **Theorem 2** |

## What it explains, retroactively

**B791's 1920 is not a coincidence — it is |SL(2,ℤ[ω]/4)/{±I}|.**

> ⚠ **NAMING CORRECTED 2026-07-29 (Chat-1's catch).** This is **NOT** PSL(2,ℤ[ω]/4). The centre of
> SL(2,ℤ[ω]/4) has order **4** — λ²=1 has four solutions (1, 1+2ω, 3, 3+2ω) — so the true PSL has
> order **960**. cc and cc3 both used the right group under the wrong name. PSL(2,O₃) maps into
> SL/{±I} because O₃ is a domain whose only square roots of 1 are ±1, so SL/{±I} *is* the correct
> target and **the theorem's substance is unaffected**; only the label was wrong.
>
> **This also resolves the B731 discrepancy, and refutes cc's own earlier diagnosis.** B731's
> index **6 = 960/160** — quotienting by the *full* centre, i.e. computing in the true PSL. cc had
> diagnosed it as "failure to quotient by −I" (1920/320); that was **wrong**. All three
> computations are correct **in their own groups**; ours is the one PSL(2,O₃) actually maps to. The B788 bank's coset action is
**reduction mod 4**: ambient 3840 = |SL₂(O/4)|, image 1920 = |PSL₂(O/4)|, kernel 2 = {±I}. cc
verified that order from raw generators in B791 without knowing what it was; this identifies it.

## What it does to cc's own claims — one refined, one refuted

**REFINED.** B790 proved Γ₄₁ is *not* the principal congruence subgroup of level √−3. **Still
true** — and now visibly the weaker half of the statement: Γ₄₁ *is* congruence, at level (4).

**REFUTED.** B790's hint `H-B788-NORMSPLIT` claimed *"m004-only norms are all ≡ 0 (mod 4)"*. The
real law is **{0, 3}**. The odd norms cc3 found — 7, 103, 127, 175, 367 — are **all ≡ 3 (mod 4)**,
i.e. exactly consistent with the theorem and fatal to the narrower claim.

**And cc's contrary "verification" was an artifact.** cc re-ran the split, got 12 m004-only norms
with none odd, and reported the claim as holding. cc3 had 41 with five odd. The gap was cc's own
ℤ[ω]-membership tolerance filter **silently discarding long geodesics** — which are precisely the
ones carrying the large disconfirming norms. **The filter selected for the author's expectation.**

The sequence is worth keeping intact: cc accepted a refutation of its own claim readily, then
received a vindication and checked it harder — the right asymmetry — but the vindication came
from a computation cc had written with a known silent-drop path, and cc did not catch that until
the disagreement forced it.

## New error class (registered)

> **A filter that discards data must report its discards**, or it silently selects for the
> author's expectation.

General, cheap to enforce, and it would have caught this before either seat banked anything. Named
by Chat-1 in relay; it earned its place by catching cc within the hour of being proposed.

## Open hook, not a claim

cc3 observes that the mod-2 image is **D₅ inside PSL(2,𝔽₄) ≅ A₅**, and notes A₅ also carries
B787's 5A/5B ambivalence argument. Two appearances of A₅ in one programme is suggestive and is
**not** thereby a connection. Recorded as a HOOK for a later cell: is this the *same* A₅ acting,
or two unrelated occurrences of the smallest simple group?

— cc, 2026-07-28
