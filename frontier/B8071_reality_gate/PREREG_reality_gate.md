# PREREG — B8071: the reality gate, in characteristic zero

**Sealed before the compute is read.** Reproducer `reality_gate.py`.

## Why this cell exists

Two independent panels closed this week and **both stopped at the same wall**:

- the **su(5) panel**: `B = A ∩ τ(A)` is `(24, 24)` at four completely-split primes, identified
  as `su(5)` by Lie rank 4 and Casimir multiplicities `[2,10,15]`. Its own falsifier 5, verbatim:
  *"My computation cannot distinguish su(5) from su(4,1), su(3,2) or sl(5,ℝ)."*
- the **nilpotent panel**: rank 4 is reached, exhaustively over all 64 standard Levis, exactly at
  nilpotent orbits `A2` (centraliser `su(3)⊕su(3)`, dim 16) and `2A1` (centraliser `so(7)⊕u(1)`,
  dim 22). Its own scope note: *"Everything above is over ℂ… whether they have real points in the
  form the object actually lives in is NOT tested and is the live gate."*

Mod-`p` Killing **rank** is identical for every real form of a given complex algebra. Rank cannot
separate them. This cell moves to characteristic zero.

## The method, and why it needs no floating-point signature

Real forms of a complex simple `g` correspond to involutions `θ` of the compact form `u`, with
`g_ℝ = k ⊕ i·m` for `u = k ⊕ m` the `±1` eigenspaces. `k` is the maximal compact subalgebra, and
the Killing form is negative definite on `k` and positive definite on `i·m`. **So a real form is
named by `dim k` alone** — an exact integer, no signature arithmetic.

For a `θ`-stable complex subalgebra `c ⊆ e₆`, the induced real form `c^σ` has maximal compact
`c ∩ k`, so **`dim(c ∩ k_ℂ)` names it.** The targets:

| `su(5)` real form | `dim k` | | `su(3)⊕su(3)` real form | `dim k` |
|---|---|---|---|---|
| `su(5)` **compact** | **24** | | **compact** | **16** |
| `su(4,1)` | 16 | | `su(3)⊕su(2,1)` | 12 |
| `su(3,2)` | 12 | | `su(3)⊕sl(3,ℝ)` | 11 |
| `sl(5,ℝ)` split | 10 | | `su(2,1)⊕su(2,1)` | 8 |

Inner involutions are the 64 sign characters `ε` on the root lattice; `dim k = 6 + #{r : ε(r)=+1}`.

## Declared outcomes — all live

| result | reading |
|---|---|
| a rank-4 centraliser comes out **compact** in a form the object occupies | the chain closes over ℝ **in a gaugeable form**. Relay immediately; do not soften. |
| every real point gives an **indefinite** form | the chain closes over ℝ but **not in a form physics can gauge**. That is the finding, and it names the obstruction precisely. |
| the orbit has **no real points** in the object's form | the nilpotent route is complex-only. Report with the class named. |
| `dim(c ∩ k)` lands on **no** value in the table | my identification of `c` is wrong. Stop and fix before reading anything. |

## Controls, aimed at the claim itself (the B8070 lesson)

B8070 failed this week because its headline was a printed constant and its controls tested
quantities *adjacent* to the claim. Here every control targets the measured number.

1. **The real-form census must reproduce known E₆ theory unprompted:** the 64 inner sign
   characters must give `dim k ∈ {78, 46, 38}` and **nothing else** — compact, `e₆(−14)`,
   `e₆(2)`. If a fourth value appears, the involution construction is wrong. This also
   independently reproduces B907's reported inner sweep `{78×1, 46×27, 38×36}`.
2. **`θ` is verified to be an automorphism** — `θ[x,y] = [θx, θy]` on sampled brackets, not
   assumed from its diagonal form.
3. **The orbit is identified by centraliser dimension, not by name:** `dim z(e)` must be **46**
   for `2A1` and **36** for `A2`, matching the Bala–Carter table; the reductive parts must be
   **22** and **16**. If they do not, the representative is not in the orbit claimed.
4. **The nilpotent is verified nilpotent** — `ad(e)` must be a nilpotent matrix.
5. **False-positive control:** a subalgebra of the *wrong* dimension must fail to land on any
   table value; and `dim(c ∩ k)` must **vary** across the 64 characters. If it is constant, the
   instrument is measuring nothing.

## What this cell cannot settle, stated in advance

- It does **not** compute the object's own `B` over ℚ — `B` was built mod `p` over `ℚ(√−3)` and
  rebuilding it in characteristic zero is a separate cell. **This cell computes which real forms
  are *available* to the relevant complex algebras**, which is the necessary first half. Claiming
  the object *occupies* a particular one requires the char-0 rebuild and is **not** claimed here.
- No physical identification (Gate 5). "Compact" here is a statement about a Killing form.
- No scale, no value. The scale-torsor theorem stands.
