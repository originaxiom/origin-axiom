# B8096 — PREREGISTRATION: the residue hunt re-run with the guard relaxed to the banked condition

**Sealed before any computation.** Digest in `SEAL.txt` (SHA-256, algorithm named there, computed
over this file's bytes — not self-referential).

## Why this runs

**The owner's claim: the gates kept real findings quiet.** The corpus has already agreed with them
once — **B976**, prompted by the owner, found eleven banked arcs cited zero times on any synthesis
surface, *"They were right, and it is a count, not an impression."* And **B8092** (mine, today) found
three guards in the B1074/B1076 prompts that **can only remove candidates, never add them**.

**Finding 1 of B8092 is testable, and this is the test.** The banked reopening condition says:

> *"a crossing here must first exhibit a **FRAME-INVARIANT RESIDUE**, which B1016 says is **NOT the
> coupling's Re h**"*

The prompt that ran demanded more: *"not… **any coupling-channel quantity**… must be
**PAIR-CHANNEL-NATIVE**"*. **A frame-invariant residue built from both channels satisfies the
condition and was excluded before evaluation.**

## The relaxation (the only change)

Filter on **frame-invariance alone**. Disqualify **`Re h` by name**, as the condition does — and
**nothing else**. Drop the nativeness requirement. Drop the **per-candidate** companion-variant
demand (B8092 finding 2), keeping a **single global** bite-witness.

## The computation

Over the Klein four-group `B¹ = {I, χ_a, χ_b, D2}` (the frame group; B936's classes), using the
banked per-element data:

- `λ`: `1`, `864/413`, `6912/3047`, `2304/953`
- `λ²` **with sign**: `−1`, `−(864/413)²`, `+(6912/3047)²`, `+(2304/953)²`
- `CCC = 3!·λ` (coset-wide)
- denominators `1`, `413 = 7·59`, `3047 = 11·277`, `953` (prime)

Compute **all** natural Klein-orbit invariants exactly over ℚ: orbit products, orbit sums, the four
elementary symmetric functions, per-class products over the character's kernel `{I, χ_a}` and its
coset `{χ_b, D2}`, and integer structure (gcd/divisibility) of the denominators.

## THE BINDING VACUITY CONTROL — declared now because this is where the last 77 died

**B1076's own control killed a 77-candidate**: the hierarchy discriminant's squarefree part was 77
at all three nontrivial gauges, and it was **forced by `V_ccl` living in `K`**, holding for a control
diagonal with **zero relation to the coboundary structure**.

> **Any invariant whose value is forced merely by the quantities living in `K` is VACUOUS.** Every
> candidate must be run against a control with no relation to the coboundary structure. **If 77
> appears, it is presumed vacuous until the control says otherwise.** I expect 77 to appear and I
> expect it to be vacuous.

## THE TWO OUTCOMES

**OUTCOME A — the guard suppressed something.** A frame-invariant, value-bearing quantity exists
that **survives the vacuity control** and **would have been excluded** by the nativeness or
per-candidate guards. ⟹ **The owner is right in the strongest sense**, B8092 finding 1 is not
hypothetical, and B1074/B1076's negative must be re-scoped.

**OUTCOME B — the negative is robust.** Every frame-invariant quantity is either vacuous under the
control, or structureless, or already banked. ⟹ **The original negative survives its own strictest
objection**, which is a stronger result than it had before, because it was reached with the guard
relaxed rather than in place.

**Prediction recorded so the arc can be wrong: I expect OUTCOME B.** The relaxation is real and
worth running, but B1076's symmetrization sweep was broad and its vacuity control was sharp. **If B
is what happens, the owner's general claim still stands on B976 and B8092 — this one instance simply
does not carry it.**

## SCOPE

The λ/CCC family across `B¹`, using banked per-element values. **Not** a re-derivation of those
values (done independently today: `λ²(I) = −1` on all six couplings, `D_a = 16`, `D_b = 11`). No
measured number anywhere; mass-ratio targets named as classes only. Gate 5: nothing enters
`CLAIMS.md`.

— cc3, audit seat. Band B8000+.
