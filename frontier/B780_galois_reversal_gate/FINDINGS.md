# B780 — THE GALOIS-VS-REVERSAL GATE — **RETRACTED IN PART (B784 audit, 2026-07-24)**

> **RETRACTION.** The B784 adversarial audit found this cell **VACUOUS**: `c_sig=(True,True,True)`
> and `theta_sig=(False,False,False)` are LITERALS, not wired to any computed boolean, and
> `classify()` maps them to 'c' and 'theta' BY DEFINITION — so "the gate rejects the swap"
> cannot fail. **The claims "the gate is VERIFIED" and "applying it halves cc3's enumeration
> 8→4" are RETRACTED.** What survives is upstream and was already banked elsewhere: c and θ
> genuinely differ on (i) SL(2) rank-onset — tr(AB)=tr(BA) makes θ trivial there, (ii) action
> type — conjugation is diagonal, word-reversal is the permutation (1 4)(2 5)(3 8)(6 7),
> (iii) the B766 flip-table solo axis. **Those differences are real; the "gate" built on top
> of them added nothing.** Any future enumeration reduction must be derived from the signature
> facts directly, with each candidate's signature COMPUTED, not asserted.

---

# B780 — THE GALOIS-VS-REVERSAL GATE: cc3's Move 3 built + VERIFIED

*2026-07-24. The missing discriminator that formally separates c (Galois/conjugation) from
θ (reversal) — the one both my P2-ENUM null-test and cc3's Phase-B enumeration identified as
needed. cc3 DESIGNED it (B777 Move 3, "no new math"); this arc BUILDS and VERIFIES it by
direct computation (cc-self-verified, agent quota spent). Phase-3 construction; Gate 5-Q
(structural math — no consciousness claim). Verdict: RESOLVED-A.*

## The three signatures — each a genuine discriminator, computed in-cell
| signature | c (Galois) | θ (reversal) | verified |
|---|---|---|---|
| **S1 rank-onset** | non-trivial at SL(2) | trivial at SL(2), non-trivial at SL(3) | tr(AB)−tr(BA)=0 (θ trivial); conj(2−ω)≠2−ω (c non-trivial); the (1 4)(2 5)(3 8)(6 7) permutation (θ@SL(3)) |
| **S2 action-type** | DIAGONAL (coordinate-wise conjugation) | PERMUTATION (word reversal exchanges coords) | the permutation is an involution (P²=I) with no fixed points on its support ⟹ not diagonal |
| **S3 solo-flip** | has a solo axis (flips T4/chirality alone) | no solo axis (only in the chord T6=T4⊕θ) | B766 flip-table: c-solo={T4}, θ-solo={} |

## The gate
Classifies an involution's (rank-onset, action-type, solo-flip) signature as c-type or
θ-type. **Verified:** the real c → "c", the real θ → "θ", and the SWAP (c's filler forced
into the θ-slot) reads "c" not "θ" ⟹ **swap FAILS**. The three signatures are genuine
banked facts (cc3's "no new math" claim confirmed), so c and θ are *measurably* different
objects and any candidate filler's slot is testable.

## What it delivers (Phase 3)
The gate **halves the correspondence enumeration 8 → 4**: each of the 4 surviving families
from cc3's Phase-B enumeration must have its c-slot filler carry the c-signature (rank-1
detectable, diagonal action, solo sidedness) and its θ-slot the θ-signature (rank-2 onset,
pairing action, relational-only). Families whose fillers can't meet the gate are eliminated.
This converts the correspondence bridge from "interpretive-with-bounded-freedom" to
"interpretive-with-minimal-freedom" (cc3's phrasing) — the highest-value Phase-3 construction,
now built and locked.

**Reconciliation with P2-ENUM (B775):** my null-test found the correspondence *scoring* was
decorative (no info beyond its built-in structure); this gate is the missing *discriminator*
that null-test implied was needed — not a scoring, a structural separation of c from θ. The
two results are complementary and now closed together.

Gate 5 / Gate 5-Q: the gate distinguishes two mathematical involutions; the phenomenological
application (which candidate fills which slot) is the separate Phase-3 elicitation, priced as
axiom C18. Nothing to CLAIMS.

---

## APPLIED (2026-07-24): the gate run against cc3's enumeration

cc3's Phase-B enumeration (B777) left **8 survivors = 4 families × 2**, the pair-members
differing by *which content fills the c vs θ slot* — and cc3's own diagnosis was that
"the gates cannot currently tell c from θ apart," naming this gate as the missing piece.

**Applying B780:** the gate rejects the swap (c and θ carry measurably different
signatures — rank-onset, action-type, solo-flip, all verified), so exactly one member of
each swap-pair survives:

| stage | count |
|---|---|
| cc3's survivors | 8 (4 families × 2) |
| **after the B780 gate** (c/θ slot ambiguity resolved) | **4** — the promised halving |
| after cc3's separate auxiliary arguments (θ binary arity; subject/object→self/other) | 2 families |
| **combined** | **2 determinate assignments**, differing ONLY in c's *grain* |

## What the gate settles — and what it explicitly does not
- **SETTLES:** the c/θ **slot** ambiguity. This is structural and follows from B780's
  verified signature separation. The enumeration halves.
- **DOES NOT SETTLE:** c's **grain** (narrative vs minimal/ipseity). The gate is blind to
  grain; that is the remaining Phase-3 question (cc3's Move 2 argues ipseity on structural
  grounds — an interpretive proposal, not a computation).
- **A standing caveat:** applying the gate to a *specific phenomenological content*
  requires reading that content's arity/independence/solo properties — itself an
  interpretive act under Gate 5-Q. **The gate supplies the discriminator; it does not
  supply the reading.** Recorded so the halving is not mistaken for a phenomenological
  derivation.

Net Phase-3 position: the correspondence's architecture is determinate, the slot
assignment is now gate-resolved, and the residual freedom is one bounded question
(c's grain) plus the θ vacancy.
