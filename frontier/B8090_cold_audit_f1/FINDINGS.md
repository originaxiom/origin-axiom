# B8090 — COLD AUDIT, FINDING 1: B1076's "new exact character" is mis-stated on every summary surface

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Verdict: PROVED** (the defect is proved; B1076's
computation is not in question). Reproducer `character_check.py`. Gate 5 untouched.

**This is the cold audit the owner routed and cc requested.** Scope B1074→B1076. First finding,
delivered ahead of the recomputation because it is decidable from B1076's own record and needs no
algebra at all — only the Klein group's multiplication table.


## THIS CORRECTS MY OWN EARLIER RELAY — read this before the finding above

On the same date I sent cc `CC3_TO_CC_2026-08-19_AUDIT_B1076_ONE_NOTATION_DEFECT.md`, flagging this
same line. **That relay's diagnosis was wrong, and its central assertion was false.**

It said: *"As written this cannot be true. The λ you report are 1, 864/413, 6912/3047, 2304/953 —
**all positive rationals**, so `λ² > 0` at every gauge and no character built from `sign(λ²)` can be
negative anywhere."* It then guessed that `λ²` meant **`λ₂`, the second root**, a subscript rendered
as a superscript.

**Both halves are wrong.** `b1076_results.json` defines `λ² = c²/(qᵢqⱼqₖ)` — a named quantity, not
the square of the reported λ — and its values **are** negative at `I` and `χ_a`. So `sign(λ²)`
really is `(−,−,+,+)` exactly as cc banked it, and cc's **signs were right all along**.

**I made the precise error I was accusing cc of**: I assumed `λ²` meant λ-squared and reasoned from
the assumption instead of the record. That relay states in its own header *"Your scripts not read;
the reported values were taken as claims"* — **I inferred a definition rather than looking it up,
and then sent the inference as a defect report.**

**What survives:** there *is* a defect on that line, but it is **narrower and different**. cc's signs
are correct; the word **"character"** is what fails, because a `−1`-at-identity function is not a
homomorphism. The polarity of the genuine character is then inverted relative to what is banked.

**Standing lesson, and it is the session's recurring one:** an inference about what someone *meant*
is a hypothesis requiring a search, and the search here was one `grep` of a file I had not opened.

## The claim, as banked on three surfaces

`FINDINGS.md`, `arc_verdict.json` and `CHANGELOG.md` all read:

> *"`sign(λ²)` is a NEW nontrivial character of the Klein group (**negative on {I, χ_a}, positive
> on {χ_b, D2}**)"*

## The defect

From B1076's **own recorded values** — `λ²(I) = −1`, `λ²(χ_a) = −(864/413)²`,
`λ²(χ_b) = +(6912/3047)²`, `λ²(D2) = +(2304/953)²` — the signs are indeed `(−, −, +, +)`. **And that
function is not a character.**

**A character sends the identity to `+1`, always**: `χ(e) = χ(e·e) = χ(e)²`. Here
`sign(λ²)(I) = −1`, so `sign(λ²)` fails multiplicativity — **on all 16 products**, checked
exhaustively.

**Two errors compounded:**

1. **Mis-typed.** `sign(λ²)` is called a *character* when it is `−1` at the identity and is
   therefore not a homomorphism at all.
2. **Inverted.** The genuine character is `χ = sign(λ²)/sign(λ²(I))`, which is **`+1` on {I, χ_a}
   and `−1` on {χ_b, D2}** — the **opposite polarity** to what is banked.

## Where the error is NOT — and this matters

**B1076's internal record states it correctly.** `b1076_results.json` says, verbatim:

> *"character of the Klein four-group B¹, **trivial on the subgroup ⟨χ_a⟩ = {I, χ_a}** and equal to
> −1 on the coset χ_b·⟨χ_a⟩ = {χ_b, D2}"*

**So the computation is right and the cell got it right.** The defect is entirely in the
**summary layer** — the headline drifted from the record on the way out, and then propagated to
three surfaces. **The arc's NEGATIVE verdict is unaffected**, as is every other banked result in it
(`CCC = 3!·λ` coset-wide, the λ family, the `denom⁴` law, the 77-vacuity kill).

## Why it is worth raising anyway

This is the corpus's own tracked class — a **headline that no longer matches its record** — and it
is the class that produced E43. It also lands on a claim advertised as *"a NEW exact character"*:
one of the arc's four banked theorems, stated in a form a referee would reject on sight, because
"a character that is `−1` at the identity" is a contradiction in terms rather than a subtle error.

**The fix is exact and costs nothing:** state it as *the nontrivial character of B¹ with kernel
{I, χ_a}*, or equivalently *`sign(λ²)` relative to its value at `I`*. The content survives intact
— there **is** a nontrivial character, and it **does** separate `{I, χ_a}` from `{χ_b, D2}`.

## NOT A BIAS FINDING

The owner's question was whether **systematic negative bias** shaped the outcomes. **This finding is
not evidence of that**, and I will not let it be read as such: a polarity slip in a summary is
direction-neutral, it does not touch the NEGATIVE verdict, and the underlying computation is
correct. **Recorded as a defect in the record, not as a thumb on the scale.**

## SCOPE

A claim-level check on B1076's own recorded values using the Klein group multiplication table.
**Recomputes none of B1076's algebra and casts no doubt on it.** The from-scratch recomputation of
the two new gauges (864/413, 6912/3047), which cc asked be taken deepest, is **still owed** and is
not what this finding rests on.
