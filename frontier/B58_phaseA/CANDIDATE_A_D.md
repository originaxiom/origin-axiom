# Candidate general-`n` `a_d` formula (opposition-involution / θ=−w0 split)

**STATUS: CANDIDATE — structural-conjecture. Verified-match for n=3,4,5 (full tower, every factor);
UNPROVEN (needs the trace-ring identification, B58 proper); INCOMPLETE (the height-1 / wrap
power-assignment and the parity are OBSERVED, not derived). NOT a theorem.**

Date 2026-06-03. Root-system bookkeeping only (B62's existing `probe.theta_split` / `roots_of_height`;
no Jacobian computation). `m=1` throughout; `M=[[1,1],[1,0]]`, `char(M^k)=t²−L_k t+(−1)^k`,
`char(−M^k)=t²+L_k t+(−1)^k`, `L_k=tr(M^k)` (Lucas).

## The object

The `(n²−1)`-dim fixed-line Jacobian is `sl(n)`, graded by root height of `A_{n−1}`: the Cartan
(height 0, dim `n−1`) and, for each `h=1..n−1`, the height-`h` root space (dim `2(n−h)`, the `±h`
roots `e_i−e_j` with `|i−j|=h`). The candidate is that the opposition involution `θ=−w0`
(`e_i−e_j ↦ e_{n+1−j}−e_{n+1−i}`, the exchange `tr W↔tr W⁻¹` on coordinates) splits each graded
piece into its Dickson factors.

**Definition.** On the height-`h` root space let `θ⁺_h = dim(+1 eigenspace of θ)`,
`θ⁻_h = dim(−1 eigenspace)`. Convention (fixed empirically by SL(3), per B62): a θ-fixed root
contributes `+1`; a θ 2-cycle contributes one `+1` and one `−1`. Then `θ⁺_h + θ⁻_h = 2(n−h)`, and
**both `θ⁺_h` and `θ⁻_h` are even** (verified n=3..7, §Checks).

## The exact rule

**(i) Heights `h = 2 … n−1` — the verified part:**
```
   mult( char(M^h) ) = a_h = θ⁺_h / 2 = ⌈(n−h)/2⌉
   mult( char(−M^h) ) = b_h = θ⁻_h / 2 = ⌊(n−h)/2⌋
```
(The closed forms `⌈(n−h)/2⌉ / ⌊(n−h)/2⌋` equal `θ⁺_h/2 / θ⁻_h/2` because `θ⁺_h = (n−h)+1` when
`n+h` is odd and `n−h` when `n+h` is even — i.e. a θ-fixed pair appears iff `i+j=n+1` is solvable at
height `h`, iff `n+h` is odd.) This is the form B62 verified at `h=2`; it reproduces **every** known
`a_h`/`b_h` for `h≥2` at n=3,4,5 (§Checks). NB the earlier prose "`a_h=(θ⁺)/2`" with `θ⁺` read as the
*trace* would be `(±/0)/2` (half-integer) — wrong; `θ⁺_h` here is the **+1-eigenspace dimension**,
always even, and the top height `h=n−1` has a 2-dim (not 1-dim) root space `{e_1−e_n, e_n−e_1}`, so
`a_{n−1}=1`, no half-integers.

**(ii) Height 1 + wrap factors — OBSERVED, NOT derived (the gap):**
```
   height-1 root space (dim 2(n−1))  =  char(M^1)^(n−3) · char(M^−1)^1 · char(M^n)^1
```
i.e. `a_1 = n−3`, plus the inverse factor `char(M^−1)` (mult 1) and the top "Coxeter" factor
`char(M^n)` (mult 1). The dimension matches (`2(n−3)+2+2 = 2(n−1)`) and `a_1=n−3` matches n=3,4,5,
**but the θ-split alone does not assign these powers** — why height-1 carries `M^1, M^−1, M^n`
rather than `M^1/−M^1` is the observed-not-derived piece.

**(iii) Cartan / parity (height 0, dim `n−1`) — also a θ-split, observed:**
```
   (t−1)^p · (t+1)^q,   p = ⌈(n−1)/2⌉,   q = ⌊(n−1)/2⌋
```
(the diagram automorphism `H_i↔H_{n−i}` split; same fixed→+1 convention). Verified n=3,4,5;
degree-1 factors here rather than degree-2 `char(M^0)`.

## Full candidate tower
```
  char(M^−1)^1 · char(M^1)^(n−3) · ∏_{h=2}^{n−1} char(M^h)^{⌈(n−h)/2⌉} · char(M^n)^1
              · ∏_{h=2}^{n−1} char(−M^h)^{⌊(n−h)/2⌋}
              · (t−1)^{⌈(n−1)/2⌉} (t+1)^{⌊(n−1)/2⌋}
```

## Checks (all run via root combinatorics; no Jacobian)

1. **Integer-validity** — every `a_h, b_h, p, q` is a non-negative integer for n=3,4,5,6,7
   (`θ⁺_h, θ⁻_h` are even at every height; asserted in code). **PASS** (kills the `(θ⁺/trace)/2`
   half-integer reading).
2. **Dimension-sum** — the full decomposition sums to exactly `n²−1` for n=3,4,5,6,7:
   `(n−2)(n−1)` [heights 2..n−1] `+ 2(n−1)` [height-1+wrap] `+ (n−1)` [parity] `= (n−1)(n+1) = n²−1`.
   **PASS** (exact, all five n).
3. **Tower reproduction** — the complete factor multiset equals the known tower **exactly** for
   n=3,4,5 (not just `a_h`):
   - n=3: `char(M^−1)·char(M^2)·char(M^3)·(t−1)(t+1)` — **exact**
   - n=4: `char(M^−1)·char(M)·char(M^2)·char(M^3)·char(M^4)·char(−M^2)·(t−1)^2(t+1)` — **exact**
   - n=5: `char(M^−1)·char(M)^2·char(M^2)^2·char(M^3)·char(M^4)·char(M^5)·char(−M^2)·char(−M^3)·(t−1)^2(t+1)^2` — **exact**
4. **Top-height / half-integer** — `h=n−1` root space is 2-dim → `a_{n−1}=1`; no half-integers
   anywhere. **PASS**.

## Predicted full rows (CONJECTURAL, n=6,7)
```
 n=6:  a_d = {1:3, 2:2, 3:2, 4:1, 5:1, 6:1},  char(M^−1):1,  b_d = {2:2, 3:1, 4:1},  (t−1)^3(t+1)^2
 n=7:  a_d = {1:4, 2:3, 3:2, 4:2, 5:1, 6:1, 7:1},  char(M^−1):1,  b_d = {2:2, 3:2, 4:1, 5:1},  (t−1)^3(t+1)^3
```

## The `a₃(n=6)` cross-check — OPEN, candidate (2) better-supported

| source | `a₃(n=6)` |
|---|---|
| this candidate (θ-split) | **2** |
| B66 numerical pinv | **1** |

**OPEN.** They disagree. `a₃` at n=6 is a *degenerate* multiplicity (`char(M³)` repeated), exactly
the collision type where Phase A proved the pinv-limit **under-counts**: at n=5 the pinv returned
`a₂=1` where the truth is `2` (B62 structural + all n≤5 data). So `2` is the better-supported value
(the candidate matches every n≤5 factor; B66 is the method demonstrably wrong at this collision and
only resolved 26/35 of the n=6 row). **But neither is rigorous**, so `a₃(n=6)` is recorded OPEN —
not asserted — pending a degeneracy-aware (canonical) computation or the trace-ring proof.

Also OPEN at n≥6: `b_d`. The candidate gives `b_2(n=6)=2`, whereas the old pattern `b_d=[d≤n−2]`
gives `1`; these agree only for n≤5 and **diverge at n=6**. (See VALIDATION_LEDGER downgrade.)

## What would settle it

The candidate's `θ`-eigenspace dimensions are exact `A_{n−1}` Lie theory; the unproven step is the
**identification** with the trace-map Jacobian multiplicities — the ambient `SL(n,C)` trace ring
(B58 proper). Proving that identification would promote this from verified-match to theorem and
simultaneously decide `a₃(n=6)`. The pinv/ambient-Jacobian route cannot: it is the construction that
under-counts at exactly these degenerate collisions.
