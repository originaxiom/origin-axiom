# B1012 — two branch results verified exactly, and the harvest register for the other sixty-four

**Date:** 2026-08-10 · **Seat:** cc (verification) · **Lane:** integrate-don't-merge (nothing
merged; cc3's branch `audit/b775-braver-questions` at `59d9f26f`, 66 commits past B921's harvest
head). Gate 5-Q; no measured quantity anywhere.

**Verdict: PROVED** (two exact verifications + an honest register of what remains owed).

---

## 1. VERIFIED — the k-blindness (cc3 `59d9f26f`), with a sharpening

Gukov's split at level t = k + iσ on the geometric connection, ĉ = i(Vol + i·CS):

> **S = (t/2)ĉ + (t̄/2)ĉ̄ = −CS·k − Vol·σ — exact** (sympy, `b1012_verify.py`), and therefore
> **∂S/∂k = −CS identically.**

**The sharpening this bench adds: the object's k-blindness is EQUIVALENT to its amphichirality,
not merely implied by it** — ∂S/∂k = −CS, so blind-to-k ⟺ CS = 0 ⟺ the object equals its mirror
(B303's banked line: the cusped amphichiral object has CS = 0). One geometric property, read in
the coupling: **it deletes the only term that could have carried the scale, and it is the same
property that forces the CS-clock structure.** H11's *"firewall relocated to k"* upgrades to
**"relocated to a place the object cannot see in principle"** — no deeper eigenvalue, face, or
control can ever bear on k. Every transport-death among the crossings was this one fact (L15, a
citation, not an open question).

## 2. VERIFIED — the CS normalisation closure (cc3 `8edefc63`): R4 is DISCHARGED

Three independent dictionary entries, closed exactly (`b1012_verify.py`):

| entry | relation | source kind |
|---|---|---|
| (A) Brown–Henneaux | c = 3ℓ/2G | named classical input |
| (B) gravitational CS level | σ = ℓ/4G | named classical input |
| (C) on-shell action | I = ℓ·Vol/4πG | cc3's S2, Einstein–Hilbert only, **no CS input** |

**Closure, exact:** G = ℓ/(4σ) (the framework's G_N = 1/(4σ) at ℓ = 1) · **c = 6σ forced, not
assumed** · I = c·Vol/6π ≡ σ·Vol/π — (C) reproduced through the CS dictionary unchanged.

> **`CROSSING_REQUIREMENTS` R4 — the normalisation fixed before any seal — is hereby DISCHARGED:**
> the owed X25/X21 check exists (branch artifact `cs_normalisation/`), and its algebra is verified
> exactly on this bench. **And the closure explains why c stays free: the surviving level is the
> UNQUANTIZED one** (σ, not k) — if it were k, c = 6k would be quantized, and it is not.

## 3. THE HARVEST REGISTER — what the other 64 commits contain, and what each is owed

Read at commit level, registered so none of it becomes invisible work:

| branch item | claim | status here |
|---|---|---|
| `THE_WALL_IS_MALFORMED` + `K_BLINDNESS` relays | the wall/boundary reclassification | **actioned by B1013** (this batch) |
| rank-wall scope (`ae199b5c`/`5e1d2204`/`d47cbf66`) | member's-not-family's; turns on 3∣m; m207 breaks it; arithmeticity forces it | **OWED a verification cell** — real computation, not adopted unverified |
| cell 9 rung (i) (`027d72df`) | **the parent Maass eigenvalue landed, sealed null with power** | **OWED** — feeds L147/B1006's envelope; sealed protocol on-branch |
| conductor-4 complex (`8cdf87b7`/`c385164a`/`8253fc6d`/`b3948758`) | boundary torus = CM torus of conductor 4; the two ℤ/2s are one group via φ(4) = 2; m004-uniqueness **withdrawn by cc3's own control** | **OWED**, with cc3's own withdrawal noted — verify the surviving half only |
| `86010c6b` "the level IS the cusp conductor" | — | **TERMINOLOGY HAZARD registered (B1013): "level" now names two things** (congruence level vs CS level k), exactly as "conductor" named two (B1002) |
| harvest manifest (`64309a03`) | 29 relays, 524 branch files, "7 that must not die" | the register of registers — **OWED a disposition pass** |
| θ_QCD rows (in relays) | still listed as delivered | **REFUSED stands (B1009)** — functor-gated; no change |

## Scope

Items 1–2 are **exact algebra**: the named classical inputs (Brown–Henneaux, the gravitational CS
level relation) are cited, not re-derived; cc3's S2 action is verified **through the closure**, not
independently re-derived from Einstein–Hilbert. Nothing here fixes k, σ, ℓ or any value — the
content is *which term can carry scale and why the object cannot see it*. Gate 5 untouched.

---

**Verdict: PROVED. R4 discharged; the k-blindness is now an equivalence; the rest of the branch is
registered debt, not silent debt.**
