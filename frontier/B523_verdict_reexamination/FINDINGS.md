# B523 — The wrong-leap re-examination: was any negative a premature leap?

**Owner's ask (2026-07-11): "inspect the math and where we missed the step and took the wrong leap to
negative conclusion."** This node treats the program's own negative verdict as the thing to *break*. Each
key "generic / laundered / no-crossing" call is recomputed and classified into exactly one terminal state:
**CONFIRMED-GENERIC** (the control ran, the negative holds — no wrong leap) · **PREMATURE** (a wrong leap;
reopen) · **UNTESTED-RESIDUAL** (existence-negative right, but an object-specific control never run — run it).
Firewalled; nothing to `CLAIMS.md`. The independent audit ([[B521]]) already corroborates the negative;
this pass looks for a leap the corroboration might hide.

## The classification table
| cell | negative call | terminal | why |
|---|---|---|---|
| 1 | the (3,1) Lorentzian signature is generic | **CONFIRMED-GENERIC** (C3 run) | trace-form + Lyapunov both generic (splitting-type / C1); **C3/Malament now run** — only the evolution verb gives a proper cone; the monoid shares none (below) |
| 2 | B518 mixed-chain = "just gap-labeling" | **CONFIRMED** (correct decline) | the composite IS additive Bellissard gap-labeling (a known theorem); declining to call it a crossing is right, not a wrong kill |
| 3 | wild-census S₄-generic | **CONFIRMED-GENERIC** | the census used field-isomorphism (not disc-match) against the Bhargava base rate (D0 gates); S₄-genericity is a proper base-rate statement, not a laundering |
| 4 | seam ℚ(√−15) generic (h=2) | **CONFIRMED** | the *value* question is generic (h=2, 14 fields); the object-specific structure (A1 "product un-taken") is already banked as STRUCTURE (B519), not a physics value |
| 5 | B519 "no crossing" | **CONFIRMED** | corroborated by the independent audit ([[B521]]/CLOSURE_2026-07-11) — two seats, same negative |

**Verdict: NO wrong leap found.** The one genuine UNTESTED-RESIDUAL (C3) was run and it *confirms* the
negative. The negative now stands on firmer ground than before the re-examination.

## Cell 1 (the substantive computation): C3 / Malament — does the four-verb monoid preserve ONE causal cone?
The (3,1) signature's *existence* is generic (trace-form control + C1/tetranacci, both banked). The handoff's
**C3** was the one control never run: Malament's theorem gives a canonical conformal structure only if the
*whole* causal automorphism group preserves *one* cone. Computed here (`c3_malament.py`) — the four banked
verbs (B497), each in the bootstrap coupling `M_v = [[v,v],[v²,v]]`, against M*'s timelike (expanding) cone:

| verb | det(M_v) | own causal type | preserves M*'s cone |
|---|---|---|---|
| **evolution** F=[[1,1],[1,0]] | −1 | **(3,1) proper** (1 timelike) | 1.000 |
| decimation [[2,0],[0,2]] | +16 | **(2,2)** — two time directions | 0.96 |
| decimation [[1,2],[1,0]] | −8 | **(3,1) inverted** — three time directions | 1.000 |
| TM/erasure [[1,1],[1,1]] | 0 | **degenerate** — non-invertible, null direction | — |

*(M* self-preserves its own cone at 1.000 — convention check.)* The four verbs carry **four different
causal types**: only the unimodular **evolution** verb (det ±1, measure-preserving) yields a proper
single-timelike (3,1) Lorentzian cone; decimation (|det|>1, dissipative) gives (2,2) or an inverted (3,1)
with multiple time directions; TM/erasure (det 0) are non-invertible — not causal automorphisms at all.

**⟹ the Level-1 four-verb monoid does NOT preserve a single causal cone.** Malament does not apply to the
monoid; there is **no single object-specific conformal/causal structure**. The (3,1) belongs to the
**evolution sub-dynamics alone**, and there it is generic to any 2-real-1-complex quartic Pisot (C1). **C3
CONFIRMS the negative — not a wrong leap; a completed control that closes the residual.**

### The one structural nugget (banked as STRUCTURE, firewalled — not a crossing)
**Causal structure ⟺ the evolution verb.** The proper (3,1) Lorentzian cone exists exactly for the
unimodular / measure-preserving verb (det ±1); it degenerates for the dissipative verbs (decimation:
extra time directions; TM/erasure: collapse). The "arrow" of causal structure lives on the *reversible*
sub-dynamics. Clean structural fact — but NOT a physics crossing: the (3,1) is generic, and the
confinement-to-evolution merely restates det = ±1. Firewalled.

## Bearing on cell 1: the incoming Level-1 free-product / genus-2 "spacetime" handoff (verified, 2026-07-12)
A cross-seat handoff proposed upgrading Level 1 from the direct product F₂×F₂ to the **free product
F₂*F₂ = F₄**, claiming its substitution `φ: a→abAB, b→aA, A→abaAB, B→aA` is an automorphism (det = −1) whose
mapping torus is a genus-2 fibered hyperbolic 3-manifold (a "Level-1 spacetime"). Verified
(`verify_handoff_L1.py`):
- **SOUND:** the *direct-product obstruction* is real — every 2-dim SL(2,ℂ) irrep of F₂×F₂ tensor-factors
  (Schur), so cross-coupling (κ(a,A)≠2) needs the free product. The conceptual point ("independence =
  freeness, not commutativity") is correct. And **|γ| = 1/√φ exactly** (|γ|² = 1/φ² + (√5−2) = 1/φ ✓) — a
  genuine golden-nesting fact.
- **BROKEN:** the stated φ is **NOT an automorphism.** `φ(b) = φ(B) = aA` (both map to the same word) ⟹ φ
  is **non-injective**; its abelianization matrix has two identical columns and **det = 0, not −1.** The
  genus-2 fibered-hyperbolic-3-manifold construction — and every downstream claim (χ=−3, vol ≥ 3·log β, the
  trace field, the 9d cross-coupled character variety *with this monodromy*) — **does not follow**, because
  Thurston's theorem needs φ to be a pseudo-Anosov *automorphism*.
- **Terminal:** the Level-1 upgrade is **NOT a new door as stated** (the specific map is broken). The idea is
  *possibly* salvageable with a genuine Σ_{2,1} pseudo-Anosov automorphism carrying Perron β=φ(1+√φ), but
  that map has not been exhibited; and even an abelianization-det-±1 endomorphism of a *free* group need not
  be an automorphism. Recorded as a corrected-cross-seat-claim (cf. the β-function handoff): the verify pass
  caught the over-claim before banking. B515–B517 (substitution, Rauzy, Pisot β) are untouched — they live
  at the word level, below the group structure, as the handoff itself notes.

## Terminal state
DOOR B523 — **CLOSED (re-examination complete): NO wrong leap to negative.** Five cells re-checked; the one
UNTESTED-RESIDUAL (C3/Malament) run and CONFIRMS the negative; the proposed Level-1 genus-2 upgrade is built
on a non-automorphism and opens no door as stated. One structural nugget banked (causal ⟺ evolution verb),
firewalled. Lock: `tests/test_b523.py`. Cross-refs: [[B517]] (SIGNATURE_HUNT / C1), [[B497]] (the four
verbs), [[B521]] (audit corroboration), [[K025]] (the value-free theorem), P015/P016 (the reading).
