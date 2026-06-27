# B238 — L49 remainder: the SU(3)₂ WRT of the figure-eight + level-rank SU(2)₃ ↔ SU(3)₂

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
The last computable item of the chat1 handoff. Pure numpy (no SnapPy) — fully reproducible. Run: `python su32_wrt.py`.

## What was built
The **SU(3)₂ modular data** `(S,T)` from Kac–Peterson (6 primaries; Casimir `C₂=⟨λ,λ+2ρ⟩=(2/3)(a²+ab+b²)+2(a+b)`),
**gate-verified** against the modular relations (S unitary & symmetric, `S²=C` a permutation, `(ST)³ ∝ S²`). A
Casimir-normalization bug (factor 2) was caught by the gate and fixed before any result was read — the gate is the
correctness lock.

## Result
**The figure-eight WRT coincides across the level-rank pair:**
> `Z(4₁=RL closed bundle; SU(2)₃) = Z(4₁; SU(3)₂) = −1/φ` (= −0.618034), **exactly.**
(The SU(2)₃ value reproduces B204; the c/24 framing cancels in any `RᵃLᵃ` word, so `Z` is framing-clean.)

**But this is NOT a general level-rank equality** (verify-don't-trust — tested across words):

| word | SU(2)₃ | SU(3)₂ | equal? |
|---|---|---|---|
| RL (figure-eight) | −0.618 | −0.618 | **yes** |
| RRLL (silver) | 0 | 1 | no |
| RRRLLL (bronze) | 1 | 3 | no |
| RRL / RLL | 0 | −0.5∓0.866i | no |

The 4-dim (SU(2)₃) and 6-dim (SU(3)₂) modular reps have genuinely different traces; only the figure-eight (RL)
coincides.

## The "why" (the honest mechanism) — and another "golden is special"
Level-rank duality `SU(N)_k ↔ SU(k)_N` shares **`κ = k+N`**: `SU(2)₃ → 3+2 = 5` and `SU(3)₂ → 2+3 = 5`. The **same
`κ=5`** means the same golden cyclotomic field `ℚ(ζ₅)` (hence `φ`). The figure-eight — the **minimal/golden**
monodromy — lands on `−1/φ` for both; the non-golden metallic bundles (silver, bronze) do **not** coincide. And
`c(SU(2)₃)+c(SU(3)₂) = 9/5+16/5 = 5 = c(SU(6)₁)`, the level-rank conformal embedding `SU(2)₃×SU(3)₂ ⊂ SU(6)₁`.

So L49's level-rank check resolves to: **the duality is real (shared `κ=5`, the SU(6)₁ embedding), and the
figure-eight invariant coincides at `−1/φ` because of the shared golden `κ=5` — but it is a figure-eight-specific
coincidence, not a general WRT equality.** One more entry in the "`5`/golden is special" table (cf. B233/B234): the
shared `κ=5` is again the root.

## Anchors
B204 (the SU(2)_k WRT period; `Z(SU(2)₃)=−1/φ`), B233/B234 (the "5"/golden specificity), B210 (level-5 cyclotomic).
The SU(3)₂ data is standard (Kac–Peterson / Di Francesco–Mathieu–Sénéchal); the figure-eight level-rank coincidence
at `−1/φ` is the computed observation. Resolves the last open piece of L49 (the table was B235).
