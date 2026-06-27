# B233 — synthesis: the hyperbolicity-split theorem (H13) + why "5" governs golden (H17)

**Status: banked synthesis (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Promotes hints **H13** and **H17** (NOTICED → CHECKED). Run: `python verify_five.py` (pyenv).

These are the two cross-finding questions surfaced by the first QUESTION pass. Both resolve to **honest
partial statements**, not slogans — each verified or precisely scoped.

---

## H13 — the hyperbolicity-split, stated precisely (a candidate synthesis from 3 witnesses)

**The motif** (3 banked witnesses): the golden object recurs on *both sides* of a hyperbolic / non-hyperbolic
divide as **genuinely distinct manifolds**, joined only by a hyperbolicity-blind datum.

| witness | non-hyperbolic / closed / algebraic face | hyperbolic / cusped / geometric face | shared (hyperbolicity-blind) datum |
|---|---|---|---|
| **B217** | the **closed** torus bundle (Sol) — the WRT **period**, `\|H₁\|` | the **cusped** punctured-torus bundle — the **volume** (Borromean parent) | the monodromy class `γ∈SL(2,ℤ)` |
| **B226** | TCI minimal model on a **Seifert** 3-manifold (`T[SU(2)]`) | figure-eight `T[4₁]` (hyperbolic 3d-gravity, `SL(2,ℂ)`) | `SU(2)₃` (the golden level) |
| **B229** | TCI **ordinary** Seifert `S²(3,4,5)` (`\|H₁\|=83`) | TCI **super** Seifert `S²(3,3,5)` (`\|H₁\|=66`) | the coset / `SU(2)₃` data |

**The candidate theorem (stated, scoped to a pattern — not proven "for every axis"):**
> *The golden datum — the monodromy conjugacy class `γ∈SL(2,ℤ)`, equivalently its `SU(2)₃` quantum data — is
> **hyperbolicity-blind** (pure algebra). On every axis examined it is realized **twice**: once on a
> non-hyperbolic 3-manifold (closed Sol / Seifert) carrying the **algebraic/quantum** face (period, `\|H₁\|`,
> minimal-model CFT), and once on a **hyperbolic** 3-manifold (cusped punctured-torus / `T[4₁]`) carrying the
> **geometric** face (volume, complex Chern–Simons). The two faces never coincide on one manifold.*

**Honest status:** a real recurring motif (3 independently-proven witnesses, each B217/B226/B229), stated
precisely; **"every axis" is an extrapolation from 3 data points, not a theorem.** Registered as a candidate
synthesis (H13 → CHECKED), not promoted to a claim. The unifying mechanism is genuine: an `SL(2,ℤ)` conjugacy
class is hyperbolicity-blind, so it can seed both a Sol/Seifert (non-hyperbolic) bundle and a hyperbolic bundle —
distinct manifolds by construction. This is why the firewall's "the invariant carries no scale" (K018) has a
geometric shadow: **the scale-bearing (geometric/volume) face and the scale-free (algebraic/period) face live on
different manifolds.**

---

## H17 — why "5" governs golden everywhere (one reason or a pile-up?)

**Verdict: NOT a pile-up — one cascade + one genuine number coincidence (a *partial* unification).**
Verified exactly (`verify_five.py`):

- **ROOT A** = golden is `m=1` = the smallest metallic mean, field `ℚ(√5)`, discriminant `5` (`5 = min m²+4`).
  **Eight of eight** "5"-faces cascade from A through the **single field `ℚ(√5)` / prime 5**: golden = smallest
  mean; dynamical extremality (systole `4 log φ`); least volume (`2 v_tet`); the anyon level `k=3`,
  `n=k+2=5=m²+4`; the SUSY coset denominator `SU(2)₃`; the WRT period's `5`-divisibility (`disc ℚ(√5)=5`); the
  character-variety conductor `40=2³·5`; and the `E₈` McKay shadow (`ℚ(√5) → SL(2,F₅)=2I=E₈`).
- **ROOT B** = `5` is the **largest** prime `p` for which `SL(2,F_p)` is an exceptional McKay group
  (`p=3 → 2T=E₆`, `p=5 → 2I=E₈`; `E₇=2O`, order 48, is **never** `SL(2,F_p)` — structurally excluded, the B210
  fact, re-verified here).
- **The single genuine coincidence:** the value `min(m²+4)=5` (root A) is *also* the largest McKay prime (root B).
  Everything else cascades from A; B contributes only this one number-theoretic identity. The `E₈` face is exactly
  where A meets B (the field `ℚ(√5)` has discriminant `5`, and `5` is the `E₈` McKay prime).

So the answer sharpens SYNTHESIS.md §9's "the minimal point and the exceptional point are the same point, for the
same reason: 5" — into: **one causal cascade (the field `ℚ(√5)`) plus one coincidence (the smallest metallic
discriminant is the largest McKay prime).** Not eight independent miracles; not a single root either.

---

## Anchors
B217/B226/B229 (the three split witnesses), B210 (dual McKay / `E₇` exclusion), B206–B211 (the "5" web),
B218/B224/B231 (the golden-only boundary `λ_m<2`). Synthesis homes: `papers/metallic_one_object/SYNTHESIS.md` §9,
`docs/STRATEGIC_SYNTHESIS.md` §9.
