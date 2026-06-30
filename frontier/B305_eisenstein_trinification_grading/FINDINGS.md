# B305 — The Eisenstein trinification grading: E₆ → SU(3)³ at ω (verified); the saddle is SU(2)³, not SU(3)

**Status: banked (frontier). One verified object-relevant result + one re-refutation; nothing to `CLAIMS.md`.**
Chat-1 proposed a forced breaking cascade `E₆ → SU(3)³ → SU(3)` along the character-variety deformation `u`, at the
Eisenstein values. Assessed verify-don't-trust (after B304 already refuted the same "saddle SU(3)" once). A root `α`
survives `exp(u·h)` (`h` = the principal grading element, `α(h) = height`) iff `u·height(α) ∈ 2πiℤ`:
`u = 2πi/3 → height ≡ 0 mod 3`; `u = iπ/3 → height ≡ 0 mod 6`.

## Verified — and object-relevant (the real result)
At the **Eisenstein point `u = 2πi/3`** (`height ≡ 0 mod 3`): **9 surviving positive roots** (heights 3,6,9 → 5+3+1),
in **3 mutually-orthogonal components of 3 each = A₂×A₂×A₂ = SU(3)³ = trinification** (Sage-verified). This is the
standard ℤ₃ grading of E₆ — but its **grading eigenvalue is `ω = e^{2πi/3} ∈ ℚ(√−3)`**, the *same* Eisenstein root
that gives `2T` (B266) and `±π/6` (B285). So **the figure-eight's arithmetic `ω` is the trinification grading**, and
the orbifold `(θ,φ)` (B299) is the **triality permuting the three SU(3)'s** — the gauge breaking and the `(θ,φ)`
structure are the *same object*. This consolidates B266 (`ℚ(√−3)→2T→E₆`), B285 (`±π/6`), and B299 (the triality) into
one Eisenstein-`ω` structure that is *both* the McKay arithmetic *and* the trinification breaking.

## Refuted (a clean verify-don't-trust catch — the 2nd time)
At the **saddle `u = iπ/3`** (`height ≡ 0 mod 6`): **3 surviving positive roots, all mutually orthogonal →
A₁×A₁×A₁ = SU(2)³, NOT A₂ = SU(3).** (And `A₂` is impossible: it needs a height-12 root, but E₆ tops out at 11.)
So the cascade is **`E₆ → SU(3)³ → SU(2)³ × U(1)³`**, *not* `→ SU(3)`. Chat-1's "SU(3) color at the saddle" is wrong
(now refuted twice, B304 + B305).

## What's forced / not forced
- **Forced (math):** the trinification ℤ₃ grading (`height ≡ 0 mod 3 = A₂³`) and the saddle SU(2)³ (`height ≡ 0 mod
  6`). The trinification *grading itself* is standard E₆ rep theory (generic); the **object connection** is that the
  grading eigenvalue `ω` is the figure-eight's Eisenstein root.
- **Not forced / firewalled `[LEAP]`:** *which* SU(3) is color (the triality permutes them — external, B299/B301);
  and "`u` = the energy scale, the character variety = RG trajectories, the topology = the Higgs mechanism" (the
  deformation-as-RG reading is unverified physics → S045). The cascade does **not** reach SU(3) color or the SM; it
  reaches trinification (forced) then SU(2)³ (forced), and the color identification is the external choice.

## Where it lands
A genuine consolidation: the figure-eight's Eisenstein `ω` is *simultaneously* the McKay-2T arithmetic (B266), the
`±π/6` CP phase (B285), the orbifold triality (B299), **and** the E₆→SU(3)³ trinification grading (B305). One
arithmetic atom, now four faces. The "cascade to SU(3) color" is refuted; getting color needs the external
trinification→color choice. The structural theorem holds: the *grading/breaking structure* is forced (object-relevant
via `ω`), the *color identification* (a value/choice) is external.

## The fence
E₆ root-system computation (Sage-verified) + the `ω` connection. The trinification grading is standard E₆; the
deformation-as-RG reading is firewalled `[LEAP]`. Nothing to `CLAIMS.md`.

`eisenstein_trinification_grading.py` (sage-python: the E₆ surviving-root components) · `verdict.py` (pyenv) ·
`tests/test_b305_eisenstein_trinification_grading.py`. Related: `B266` (`ℚ(√−3)→2T→McKay-E₆`), `B285` (`±π/6`),
`B299` (the `(θ,φ)` trinification triality), `B301` (the chirality filter keeps SU(3)³), `B304` (the saddle refutation,
1st time), `S045` (the firewalled RG reading).
