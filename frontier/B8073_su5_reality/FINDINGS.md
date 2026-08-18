# B8073 — the object's `su(5)` is NOT τ-stable: a cross-seat claim that does not reproduce

**Date:** 2026-08-17 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical
identification anywhere; every statement is about `e₆`, the `27`, and a conjugation of `e₆`.

**Verdict: NEGATIVE.** Criteria sealed in `PREREGISTRATION.md` before the first run. Reproducer
`cell31_B.py`, run at the three completely-split primes **811, 991, 1093**.

## Why this arc exists

A multi-agent panel reported `B = A ∩ τ(A) = (dim 24, Killing rank 24)` — the object's `su(5)`
τ-stable, hence carrying a real form. `WORKING_RULES` §2 and §12 forbid banking a cross-seat claim
that has not been reproduced in-sandbox (*"never asserted/cited/proxied"*). This is that
reproduction.

## The banked identity reproduces

At all three primes: `A = Stab_{e₆}(e_i, ēbar_j, s) = (34, 24)` — B8068's `cell11_compose.py`
result, rebuilt in the same process, with cell5's gates (`Φ·Ψ = W`, Casimir `[1,10,16]`) passing
first. Nothing was read before that passed.

## The control that was missing everywhere else

τ here is a general root-lattice character, `θ(h) = −h`, `θ(e_α) = d(α)·e_{−α}`, `T(e_r) = c_r·e_{−r}`,
with **`c` solved from the intertwining requirement, not assumed**. The gate

> `T(X·v) = θ(X)·T(v)` over all `78 × 27 = 2106` pairs — **0 failures at every prime**

**is absent from `cell16_reality.py`, `cell18_realforms.py` and `cell20_outer.py`.** None of the
three files contains any check that its τ intertwines. That is a real methodological gap in the
254-case sweep and is registered separately.

## The result — the panel's number does not reproduce

Swept per prime: the **2-torsion slice** (65 — trivial + the 64 sign gradings, exactly the family
the 254-case sweep used), the **uniform μ-family** `d(α_i) = μ` over **all of `F_p^*`**, and **400
random characters** as a generic control. Per prime that is ~1557 characters; three primes.

| | p = 811 | p = 991 | p = 1093 |
|---|---|---|---|
| `A` reproduces (34,24) | ✓ | ✓ | ✓ |
| intertwining, 2106 pairs | 0 fail | 0 fail | 0 fail |
| **characters giving Killing rank 24** | **0** | **0** | **0** |
| random characters giving 24 | 0/400 | 0/400 | 0/400 |
| dominant outcome | `B = (3,3)` | `B = (3,3)` | `B = (3,3)` |

**`B = A ∩ τ(A)` has Killing rank 3, not 24.** The largest τ-stable subalgebra of the object's
`su(5)` is 3-dimensional.

**And the panel's discriminating filter discriminates nothing:** `τ(A) = (34, 24)` for **every
character swept**, at every prime. It was reported as the filter that pins the spinor conjugation;
it is satisfied identically. So `τ(A) ≅ A` as a type while `A ∩ τ(A)` is 3-dimensional — τ carries
`A` to a *different* `su(5)` meeting it in 3 dimensions.

**Instrument negative control:** with the same τ, `Stab(s) ∩ Stab(τs) = (45, 45)` — exactly the
number the 254-case sweep reported, on the object that sweep actually measured. The tool can
produce 45; it is not stuck on one answer, and a 24 was reachable had it been there.

## What this does and does not settle

**The 254-case negative is a true conclusion reached by a wrong argument.** Its stated result —
*"`su(5)` is real in no real form of `E₆` reachable this way"* — **survives** contact with the
right object. Its **argument** was wrong twice over: it measured `Stab(s)` (dim 61) rather than the
composed `A`, and its τ was the 2-torsion slice with no intertwining check. The corpus already
carries one true-conclusion-wrong-argument (B971 on orbifolds) and the pattern must not repeat
silently, so it is recorded that way rather than quietly ratified.

**Not established here:**
- **That no τ anywhere makes `A` stable.** The swept family is the 2-torsion slice, the uniform
  μ-family, and 400 random characters. **Not swept:** non-uniform characters outside those
  families — the full space is `(p−1)⁶`. The honest statement is *"no character in the swept
  family"*, never *"no conjugation exists"*.
- **Which real form anything is.** All four real forms of `su(5)` have dim 24 and Killing rank 24;
  rank cannot separate them. That needs `dim(B ∩ k)` in characteristic zero — `frontier/B8071_reality_gate/`
  has the method, and the char-0 rebuild of `A` over `ℚ(√−3)` is registered as owed.
- Anything about chirality, generations, values or scale.

## The methodological finding, stated plainly

A cross-seat result with strong-looking controls did not survive in-sandbox reproduction. The
controls that mattered were the ones the panel did **not** run — the intertwining gate — and the
one it reported as discriminating turned out to be identically satisfied. **This is exactly the
case `WORKING_RULES` §2 exists for**, and it is the second such catch in one session.
