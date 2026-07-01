# B327 — The hierarchy CRUX = `27|₂T` self-duality: `n₁=n₂` is forced by *self-duality*, not spin (Chat-1 handoff, verified + sharpened)

**Status: banked (frontier). Verify-don't-trust on the Chat-1 → CC handoff (2026-07-01). Firewalled; nothing to
`CLAIMS.md`.** Chat-1 sharpened the mass-hierarchy bottleneck to **one representation-theoretic lookup** — the branching
`27|₂T` under the McKay embedding `2T ↪ E₆`, deciding whether the two light generations split at **Level 3** (E₆ cubic,
computable, `n₁≠n₂`) or stay degenerate → **Level 4** (the commensurator gate, `n₁=n₂`). This seat computed the pieces
in-sandbox (per *compute-before-deferring*), **caught a direct contradiction between the two chats**, and **sharpened the
atom** past where either chat left it.

## What Chat-1 asked CC to do
Compute `27|₂T` (seven integers `m₁,m₁',m₁'',m₂,m₂',m₂'',m₃`), then
`n₁ = m₁'−m₂'`, `n₂ = m₁''−m₂''` (the `ω`, `ω²` coefficients of `χ₂₇(g)` at an order-3 element `g`).
`n₁≠n₂` ⟹ Level 3 (computable hierarchy); `n₁=n₂` ⟹ Level 4 (specialist gate).

## 1. A cross-chat contradiction — resolved by direct E₆ computation
The two chats gave **incompatible** principal-SL(2) decompositions of the 27:
- **Chat-2:** `27 = V(16)+V(8)+V(0)` (spins 8, 4, 0).
- **Chat-1:** `27 = 9·V₀ ⊕ 6·V₁` (spins 0, 1).

Generating the 27 weights of E₆ as the Weyl orbit of `ω₁` and computing the principal grading
`⟨μ, 2ρ^∨⟩` gives the grade multiset
`{±16:1, ±14:1, ±12:1, ±10:1, ±8:2, ±6:2, ±4:2, ±2:2, 0:3}` →
**`27 = V(16) + V(8) + V(0)` (spins 8, 4, 0).**
**Chat-2 is correct; Chat-1's `9·V₀⊕6·V₁` is wrong** (its grades would range only `±2`). Chat-1's *downstream*
conclusion — that `−I` acts trivially (all integer spins) in the principal embedding — is nonetheless right:
`χ₂₇(−I) = 27`, and `χ₂₇(g) = 0` on the order-3 element (real).

## 2. The real mechanism — `n₁=n₂` is forced by SELF-DUALITY, not integer spin
Chat-1's proposed escape: the "McKay SL(2)" carries **half-integer** spins, which might give `n₁≠n₂`. **This fails.**
The reason `n₁=n₂` is *not* integrality:
- For any `2T ⊂ SU(2) ⊂ E₆`, `27|_{SU(2)} = ⊕ nⱼ Vⱼ` is a sum of SU(2) irreps, **every one self-dual** — so
  `27|_{SU(2)}` has **real character**, hence so does `27|₂T`. (The 27 of E₆ is *not* self-dual, but its restriction to
  any SU(2) is, automatically.)
- The binary tetrahedral group's two order-3 classes have the **same** SU(2) trace (`−1`); an SU(2)-restricted character
  is therefore **equal on both**, forcing the `ω` and `ω²` multiplicities equal: `n₁=n₂`.
- **Half-integrality does not help:** spin-½ is itself self-dual (real character on 2T). Only a **non-self-dual**
  (complex) embedding can give `n₁≠n₂`.

Verified: `χ₂₇(g)=0` (real) for the principal embedding ⟹ `n₁=n₂`; and 2T's class structure (built from the 24 Hurwitz
unit quaternions) confirms the two order-3 classes share trace `−1`.

## 3. The atom, sharpened
The genuine fork is therefore **not** "principal vs McKay SL(2)" (every SU(2)-factoring embedding gives `n₁=n₂`). It is:

> **Does the arithmetically-forced `2T ↪ E₆` factor through a self-dual (quaternionic) SU(2), or through a
> non-self-dual (complex) embedding?**
> - **Self-dual / quaternionic SU(2)** → `n₁=n₂` → light generations degenerate at Level 3 → hierarchy needs **Level 4**.
> - **Non-self-dual** (e.g. via the complex 2-dim `2'`/`2''` of 2T, or a larger complex subgroup) → `n₁≠n₂` possible →
>   hierarchy computable at **Level 3**.

The arithmetic `2T` (unit Hurwitz/Eisenstein quaternions) in its **standard** realization *is* the quaternionic 2-dim
`2 ⊂ SU(2)` — **self-dual** — which points toward `n₁=n₂` / **Level 4**. Confirming that the E₆-relevant embedding is
this standard one (rather than a twisted `2'`/`2''`-type) is the residual specialist datum — a sharper statement of the
CRUX than "seven integers, one lookup."

## The firewall (held)
Everything here is the *structure* of the branching (self-duality, the ω/ω² pairing), not a mass value. `n₁=n₂` vs
`n₁≠n₂` decides **which level the hierarchy computation lives at**, not the hierarchy itself; even `n₁≠n₂` gives
`O(1)`-split *distinct* eigenvalues, not the `10⁻⁵` magnitude (the structural theorem still forbids the value from the
single seed). Nothing to `CLAIMS.md`.

## Verdict
Banked as a **[VERIFIED + SHARPENED]** analysis of Chat-1's gate: the principal `27` decomposition is
`V(16)+V(8)+V(0)` (Chat-2 correct); `n₁=n₂` is forced by **self-duality** (Chat-1's half-integer-spin escape refuted);
the atom is now "is the arithmetic `2T↪E₆` self-dual (quaternionic → Level 4) or not (→ Level 3)," with the standard
quaternionic realization favouring **Level 4**. This lives **inside gate B** (the CRUX); `OPEN_PROBLEMS.md` gate B is
updated to this atomic form.

## The fence
Exact E₆ Weyl-orbit + principal grading (sympy); 2T built from Hurwitz quaternions (numpy) — conjugacy classes and
SU(2) traces. No physics values. Nothing to `CLAIMS.md`.

`mckay_branching_gate.py` (pyenv) · `tests/test_b327_mckay_branching_gate.py`. Related: **B324** (the ω-circulant),
**B325** (the earlier ℤ/3-"protection" refutation — a *different* mechanism from this self-duality one), **B326** (the
congruence-torsion texture datum), **B302** (`ℚ(√−3) → 2T`, index 12), **OPEN_PROBLEMS.md** gate B (the CRUX). Lit:
Kostant (principal SL(2)); the McKay correspondence `2T ↔ Ẽ₆` (Gonzalez-Sprinberg–Verdier, Slodowy); binary tetrahedral
character table.
