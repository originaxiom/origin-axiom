# STEP 8 — PREREG AMENDMENT 1 (V1 operationalization; sealed before the
amended cell runs)

**2026-07-15. The sealed V1 cell was executed and found VACUOUS at the
operational level: its mirror operation v_m → mconj(v_m) is the IDENTITY
because v₄ and v₈ are real matrices (checked in-sandbox — the
discriminating fact; run preserved at `p3_v1_vacuous_run.txt`, which
necessarily reproduced the unmirrored values bit-for-bit and therefore
could not meet the swapped-class expectations). Per MB12 this invalidates
the CELL AS OPERATIONALIZED, not the map: the verdict of that run is
INVALID-VACUOUS, carrying no outcome weight. The sealed INTENT — "the map
must intertwine the classical mirror with stage conjugation" — stands
unchanged and is re-operationalized here, hashed before running.**

## V1′ — the copy-exchange mirror (non-vacuous)

The mirror of the double is M = σ ∘ γ: the copy-swap σ (indices 1 ↔ 2 on
the word alphabet) composed with complex conjugation γ. The mirrored
CONFIGURATION puts the twist on copy 1: the letter dictionary becomes
  b1 → c·B27·c⁻¹ (twisted plain b, c = exp(t·v_m) as before),
  b2 → mconj(B27) (the untwisted mirror letter), a1 = a2 = A27 unchanged;
this is structurally a different computation from step 4b (which twisted
copy 2), so the cell can genuinely fail.

PREDICTION (from mirror-equivariance of the candidate map): for every
word w of the frozen 20-list,
  r^{V1′}(σ(w)) lies in the γ-CONJUGATE phase class of the banked
  r^{4b}(w),
with the zero set mapped by σ. Concretely: at m = 4, every σ-image of a
4b-loud word must respond in ℚ^×·(1−w) with the σ-image of the mixed word
in ℚ^×·(1+w); at m = 8, the conjugate classes. A zero response on a
σ-loud word, a class violation, or a zero-set mismatch FAILS V1′
(outcome D via the locked table, V1 row).

No other change to the sealed prereg. V2/V3 unchanged. Run order:
V1′ → V2 → V3, each banked blind.
