# B62 status — what the opposition-involution split actually establishes, and for which n

**Date:** 2026-06-03. **Read-and-report only** — no Jacobian computation, no patching, no merge.
Sources read: `frontier/B62_opposition_involution/{README,FINDINGS,probe}.py·md`,
`tests/test_b62_opposition_involution.py`, ledger row V13. The one allowed bounded check
(root-system combinatorics via the existing `probe.theta_split`, **not** the Jacobian machinery)
is reported in §6–7. Proven core P1–P16 untouched.

## 1. Three-state verdict

**B62 as written is STATE 3 for the full `a_d` row, and STATE 2 (verified candidate) for the
`char(M²)`/`char(−M²)` (height-2) piece only.**

- It computes the `θ=−w0` opposition-involution eigenspace split **on the height-2 root space
  only**. It is **explicitly NOT** a general-`n` recipe for all `a_d`: the README and FINDINGS both
  state *"the power-assignment at heights other than 2 is not derived here."*
- For height-2 it is a clean explicit rule, **verified-to-match** at n=3,4 and **applied** (not
  proven) at n=5. B62 itself labels the whole thing a **"LIVE STRUCTURAL RESULT … not a symbolic
  proof"** (README, FINDINGS verdict). Do not read it as a theorem.

A *bounded root-combinatorics check* (§6) shows B62's identification in fact extends — empirically —
to **all heights h ≥ 2**, upgrading the *candidate* to a fuller picture; but it stays STATE 2
(verified-match, not proven), is **incomplete** (the h=1 / `char(M⁻¹)` / `char(Mⁿ)` / parity sector
is separate), and its **first genuinely-new prediction conflicts with B66** (§7).

## 2. The explicit rule B62 actually states (transcribed, not paraphrased)

From `probe.py` (docstring + `theta_split`/`height2_sectors`) and README:

> The exchange involution `P` (`tr W ↔ tr W⁻¹`) is identified with the opposition involution
> `θ=−w0` on the root system of `sl(n)`. On each height-`h` root space `θ` splits into a `+1`
> sector carrying direct factors `char(Mᵏ)=t²−L_k t+(−1)ᵏ` and a `−1` sector carrying sign factors
> `char(−Mᵏ)=t²+L_k t+(−1)ᵏ`. Computed (exactly, by root combinatorics) **for height 2**:
> `mult(char(M²)) = (θ=+1 dim)/2`, `mult(char(−M²)) = (θ=−1 dim)/2`, giving
> `n=3→(1,0)`, `n=4→(1,1)`, `n=5→(2,1)`.

There is **no explicit `f(n,d)`** in B62 for `d≠2` — the general "each height-h" sentence is stated
as the *hypothesis*, but only `h=2` is instantiated. (Even the `+1↔direct / −1↔sign` convention is,
per the `theta_split` docstring, *"fixed empirically by SL(3)."*)

## 3. The precise proof gap (prediction vs identification — they are different)

Two distinct gaps, neither is "the θ-dimensions might be wrong":

1. **Reach gap.** B62 instantiates only height-2. No power-assignment `k(h)` and no validation for
   other heights are given *in B62*. (§6 closes part of this empirically, not by proof.)
2. **Identification gap (this is the V13 caveat).** The `θ`-eigenspace **dimensions are exact, sound
   Lie theory** — pure `A_{n-1}` root-system combinatorics, **not conjectural**. What is unproven is
   the **identification** of that split with the **trace-map Jacobian's** `char(±Mᵏ)` multiplicities.
   V13: *"a symbolic proof still needs the ambient SL(5,C) trace ring."* That trace ring is exactly
   what would tie the (sound) Lie-theory prediction to the (dynamical) Jacobian object — i.e. gap
   type (ii), the identification, **not** (i) the prediction. It is B58's standing open task.

So: the structural *picture* is reliable Lie theory; the *bridge to the dynamical multiplicities* is
the unproven step (plus the empirically-fixed sector convention).

## 4. Count vs sector — kept separate

- **B62 establishes the COUNT** `mult(char(M²))` (=1,1,2 for n=3,4,5) — via `θ`-dimensions — **for
  height-2 only**.
- **B64 establishes the SECTOR** (which parity sector each factor sits in) **symbolically for SL(3)**
  (depth-n CH + P=contragredient + Dickson parity), as a structural mechanism for general n. That is
  *which sector*, **not** *how many* — B64 does not give the count `a_d`.
- For `d ≠ 2`, **neither B62 nor B64 derives the count from first principles**; those multiplicities
  (B59/B60/B61 tower) came from the numerical pinv — the construction Phase A showed under-counts at
  degeneracies. So the only *structural* count in the repo is B62's height-2 `char(M²)`.

## 5. The sign-twist `b_d = [d ≤ n−2]`

It is recorded as "established," but it is itself a **verified-match on n ≤ 5**, not a separate
proof: B62's height-2 `−1` sector gives `mult(char(−M²)) = (θ−1 dim)/2 = 0,1,1` for n=3,4,5, i.e.
`[2 ≤ n−2]` — consistent. The extension (§6) reproduces all `b_d` for n=3,4,5 at h≥2 too. **But the
indicator form `[d≤n−2]` and the θ-split `(θ−1 dim)/2` DIVERGE at n=6**: for `d=2` the indicator
gives `b_2=1`, the θ-split gives `b_2=2`. So `b_d=[d≤n−2]` is an `n≤5` pattern, not an established
general law; it and B62's own θ-split make different n≥6 predictions.

## 6. Bounded check (root combinatorics only) — B62's identification extends to all h ≥ 2

Applying B62's *own* `θ`-split (`probe.theta_split`, exact `A_{n-1}` combinatorics) at **every**
height and reading `a_h=(θ+1)/2`, `b_h=(θ−1)/2` with `k=h`:

> Notation: the precise form is `a_h = θ⁺_h/2`, `b_h = θ⁻_h/2`, where `θ⁺_h` / `θ⁻_h` are the
> **+1 / −1 eigenspace dimensions** of `θ` on the height-`h` root space (always even). The shorthand
> `(θ+1)/2` above refers to that eigenspace-dimension, **not** the trace `θ_h`. See
> `CANDIDATE_A_D.md` for the precise statement and the closed form `a_h=⌈(n−h)/2⌉`, `b_h=⌊(n−h)/2⌋`.
> The numbers in the table below are computed from the combinatorics, not from the shorthand.

```
            n=3       n=4         n=5
 h | (θ+,θ-)  a_h b_h | a_h b_h  | a_h b_h   (θ-recipe)   known a_h/b_h
 1 |          (1, 1)  | (2, 1)   | (2, 2)      <-- DOES NOT MATCH (h=1 is special, see below)
 2 |          (1, 0)  | (1, 1)   | (2, 1)      ==  known   (1,0)/(1,1)/(2,1)  ✓
 3 |                  | (1, 0)   | (1, 1)      ==  known   (1,0)/(1,1)        ✓
 4 |                  |          | (1, 0)      ==  known   (1,0)              ✓
```

**For every height h ≥ 2, the θ-recipe reproduces the known `a_d` AND `b_d` exactly** (all of
n=3,4,5 — 8 direct + matching sign points), not just height-2. This is more than B62 claimed.

**The h=1 sector is genuinely separate and decomposes cleanly** (verified n=3,4,5): the height-1
space (dim `2(n−1)`) is
```
   char(M¹)^(n−3) · char(M⁻¹) · char(Mⁿ)         (a_1 = n−3; dims 2(n−3)+2+2 = 2(n−1) ✓)
```
so `char(M⁻¹)` and the top "Coxeter" factor `char(Mⁿ)` are the **wrap terms** living in height-1,
and the parity `(t∓1)` lives in the Cartan (height 0). The θ-split alone does **not** assign these
height-1 powers — this is exactly the part B62 left underived.

**Status of §6:** a **verified-match candidate formula** (state 2) — explicit and matching all
n≤5 data — **not proven** (same identification gap as §3; empirically-fixed convention; h=1/wrap
power-assignment is observed, not derived).

## 7. n=6 / n=7 predictions and the `a₃` cross-check

θ-recipe (h≥2 part; **conjectural extension**, clearly labeled):
```
 n=6:  a = {a_1=3, a_2=2, a_3=2, a_4=1, a_5=1, a_6=1, a_{-1}=1}   b = {b_2=2, b_3=1, b_4=1}
 n=7:  a = {a_1=4, a_2=3, a_3=2, a_4=2, a_5=1, a_6=1, a_7=1, a_{-1}=1}  b = {b_2=2, b_3=2, b_4=1, b_5=1}
```

**Cross-check against B66's only independent n=6 number — DISAGREEMENT, and it is informative:**

- θ-recipe: **`a₃(n=6) = 2`** (char(M³) doubly-degenerate at n=6).
- B66 numerical pinv: **`a₃(n=6) = 1`**.

This disagreement **reinforces, rather than refutes, the θ-recipe**: Phase A established that B66's
pinv is *non-canonical at a degenerate collision and under-counts* — at n=5 it returned `a₂=1` where
the true value is `a₂=2` (B62). `a₃` at n=6 is the **same situation** (a degenerate multiplicity),
and B66 only ever resolved 26/35 of the n=6 row (9 corrupted). So `a₃(n=6)=1` is most likely the
identical under-count, and the θ-recipe's `a₃=2` is the better-supported value (it matches **all**
n≤5 h≥2 data; B66 is the known-flawed method). **But neither is rigorous, they conflict, so
`a₃(n=6)` is genuinely open** until a degeneracy-aware (canonical) computation or a proof breaks the
tie. Likewise the §5 divergence (`b_2(n=6)`: θ→2 vs indicator→1) is unresolved.

## 8. Implication for the path decision (input only — not a decision)

- **Anchoring `a_d` on B62's θ-split is the most attractive structural route**: it is canonical (no
  degeneracy blindness — the exact failure mode of the pinv tower), and §6 shows it already
  reproduces **all** known `a_d`/`b_d` at heights h ≥ 2, plus a clean height-1 wrap decomposition.
- **But it is not a drop-in answer.** It is (a) **unproven** — the Lie-theory→Jacobian identification
  needs the ambient `SL(n,C)` trace ring (B58's open task), exactly the missing bridge; (b)
  **incomplete** — the h=1 power-assignment (`char(M¹)^{n−3}·char(M⁻¹)·char(Mⁿ)`) and the parity are
  observed, not derived; (c) **conflicting at its first new prediction** (`a₃(n=6)`, `b_2(n=6)`) with
  the only independent (though flawed) n=6 data.
- The honest next steps are joint-decision territory: **prove the identification** (trace ring) to
  promote §6 from verified-match to theorem; and/or obtain an **independent, degeneracy-aware
  `a₃(n=6)`** to confirm `2` over B66's `1`. The pinv tower cannot supply the latter (it is the
  method that blinds at exactly these collisions).

---

**Bottom line.** B62 = **state 3** for the general `a_d` (only height-2 instantiated; identification
unproven; label structural-conjecture, never theorem); **state 2** for `char(M²)/char(−M²)`. The
bounded check upgrades the candidate to *all h ≥ 2 matching n≤5*, with a clean h=1/wrap picture — a
strong but **unproven, incomplete, and (at n=6) B66-conflicting** structural formula. `a₂=2` is
solid (B62 + all n≤5); a general-`n` `a_d` theorem is **not** in hand.
