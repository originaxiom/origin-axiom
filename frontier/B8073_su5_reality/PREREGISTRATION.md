# PREREGISTRATION — B8073: is the object's `su(5)` τ-stable?

**Sealed before the first run.** Reproducer `cell31_B.py`. Gate 5: no physical identification
anywhere in this arc; every statement is about `e₆`, the `27`, and a conjugation of `e₆`.

## BANKED IDENTITY: what the pipeline reproduces inside itself before any new number is read

Before this cell reads anything new it must reproduce, in the same process, the banked
`A = Stab_{e₆}(e_i, ēbar_j, s) = (dim 34, Killing rank 24)` of `frontier/B8068_j2t_charge_field/`
`cell11_compose.py`, together with cell5's two gates (`Φ·Ψ = W`, Casimir multiplicities
`[1,10,16]`). If `A` does not reproduce at (34, 24), the run stops and nothing is read.

## PRIOR ART: the bank grep run at design time

`grep -rn "254" docs/LAW_MAP.md frontier/B8068_j2t_charge_field/*.md` and a read of
`frontier/B8068_j2t_charge_field/CELL_ITEM1_FINDINGS.md`, `PREREG_A_TAU_A.md`,
`cell16_reality.py`, `cell18_realforms.py`, `cell20_outer.py`. Established before designing:

- the banked negative **"`su(5)` is real in NO real form of `E₆` reachable this way — 254 of 254"**
  (`CELL_ITEM1_FINDINGS.md:13`) was computed on **`Stab(s)`**, the stabiliser of the pure spinor
  alone (dim 61), **not** on the composed `A`;
- its conjugations are the **64 inner sign gradings** plus 128 outer composites — the **2-torsion
  slice** of the family of root-lattice characters;
- **none of `cell16`, `cell18`, `cell20` checks that its τ intertwines** — i.e. that
  `T(X·v) = θ(X)·T(v)`. That check is absent from all three files.

No prior in-sandbox computation of `A ∩ τ(A)` exists.

## The question

`B = A ∩ τ(A)`, its dimension and Killing rank, where τ is an involutive conjugation of `e₆`
carrying the `27` to the `27̄`. For a complex subalgebra `A` and antilinear τ, `A ∩ τ(A)` is the
largest τ-stable subalgebra of `A`, and its τ-fixed points are a real form of it.

**τ is not inherited.** It is built as a general root-lattice character `T(e_r) = c_r·e_{−r}` with
`θ(h) = −h`, `θ(e_α) = d(α)·e_{−α}`, and `c` is **solved from the intertwining requirement**, not
assumed. The 64 sign gradings are a proper subfamily and are run as a **control**, not as the
family.

## Declared outcomes — all live, no preferred result

| result | reading |
|---|---|
| `B` = **(24, 24)**, Lie rank 4, Casimir multiplicities `[2,10,15]` | the `su(5)` is τ-stable: it **has a real form**. The 254-case negative is then **true of `Stab(s)` and false of `A`**, and is re-scoped, not deleted. |
| `B` = **(45, 45)** | τ-stability collapses to `so(10)`; the chirality/reality tension is structural and that is the finding. |
| `B` = anything else | reported as found, type named by Casimir multiplicities and Lie rank, never by dimension. |
| no intertwining τ exists in the swept family | the question is ill-posed as framed; report that, and say what family was swept. |

## Controls — every one runs before the result is read; a failure exits the script

1. **`A` reproduces at (34, 24)** on the defining so(10) pair, at every prime used.
2. **The intertwining gate** — `T(X·v) = θ(X)·T(v)` over all `78 × 27` pairs, zero failures.
   *This is the control absent from `cell16`/`cell18`/`cell20`.*
3. **`T` is bijective `27 → 27̄`**, 27 of 27, both directions.
4. **`τ² = id`** on every object used.
5. **`τ(e_i)` is a rank-1 idempotent of the `27̄`** — gated at stabiliser dim **61**, and matched
   against the `27̄`'s own idempotent list, not assumed.
6. **Generic-character control** — random characters must **not** return (24, 24). If a generic
   character gives 24, the instrument is measuring nothing. (The banked lesson: 44 was generic.)
7. **Instrument negative control** — with the *same* τ, `Stab(s) ∩ Stab(τs)` must still return
   **(45, 45)**, the number the 254-case sweep reported, on the object that sweep measured. This
   proves the declared alternative outcome is reachable and that the instrument can say 45.
8. **Type identification by Casimir multiplicities `[2,10,15]` and Lie rank 4** — never by
   dimension alone. `so(10)` returns `[1,10,16]` on the same code path as a positive control.
9. **≥ 3 primes** where `x³ − 12x − 5` splits completely: 811, 937, 991, 1093.

## Banned (THE_RULE, carried)

"X is impossible" with no class · a type named from a dimension alone · "exhaustive" applied to a
sample · a negative before the detector has found the thing elsewhere · any physical identification.

## Scope stated in advance

Over `F_p` at split primes; this is a statement about the **complex** algebra's τ-stability, and
**not** about which real form (`su(5)` vs `su(4,1)` vs `su(3,2)` vs `sl(5,ℝ)`) — all four have
dim 24 and Killing rank 24, so **rank cannot separate them**. That separation needs `dim(B ∩ k)`
in characteristic zero and is explicitly **not** claimed here.
