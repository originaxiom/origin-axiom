# B865 — the padding lemma: the re-anchoring rule is VERDICT-IRRELEVANT, and the "dropped" singlets are the anomaly ballast

cc banking seat, 2026-08-03, the critic's G2. Mathematics scope; nothing to `CLAIMS.md`; Gate 5
untouched. **Not preregistered** — the lemma is *proved*, then machine-verified; the rerun is
exhaustive over the cascade's own menus.

## 1. The gap (G2, the referee's "your ket changes at every step")

B861's ket silently changes per step: the 27 at step 1, the 16's branching at step 2, 10+5̄ at
step 3. No arc stated or audited the rule "matter at step k+1 = chiral core of matter at step k."

## 2. THE PADDING LEMMA — proved, one line

> In the free commutative monoid of multisets, `M + S = conj(M) + S ⟺ M = conj(M)`
> (cancellation), and `conj(M+S) = conj(M) + S` for self-conjugate S.
> **Hence chirality(M + S) = chirality(M): adding self-conjugate content never flips the
> verdict.** ∎

Machine-verified on **2000 random multisets** over the full rep vocabulary (self-conjugate pads
built from self-dual reps plus conjugate pairs): zero violations.

## 3. THE FULL-27 RERUN — every verdict and winner unchanged

Re-running every cascade step with the **entire descended 27** as ket:

| step, option | full-27 multiset (dial-stripped) | chiral? |
|---|---|---|
| 2, SU(5)×U(1) | {10, 5̄×2, 5, 1×3} | **YES** (10 unpaired, 5̄ excess) |
| 2, Pati–Salam | {(4,2,1), (4̄,1,2), (6,1,1), (1,2,2), (1,1,1)} | **YES** (the 16-part alone) |
| 3, SM | generation + {(3,1),(3̄,1),(1,2)×2,(1,1)×3} | **YES** ((3,2) still unpaired) |
| 3, SU(4)×U(1) | {6, 4×2, 4̄×2, 1×4} | **NO** — vector-like |

**Winners identical to B861 at every step.** The re-anchoring is a *presentational* choice — the
lemma guarantees it, and the rerun exhibits it. The referee's attack closes.

## 4. The singlets' fate — not dropped, load-bearing elsewhere

The "discarded" content is never physically dropped: **10₋₂ + 1₊₄ are exactly the anomaly ballast**
making the dial traceless at parent level (B864: 16−20+4 = 0), and the chain's singlets land in
**(1,1)₀ at the SM level — the right-handed-neutrino slot**. Being self-conjugate dial-stripped,
they never touch a verdict (the lemma) — but they are why the parent-level anomaly bookkeeping
closes.

## 5. A defect in this arc's own first draft, caught before banking

The first script built two multisets with **dict literals containing duplicate keys** — which
silently collapse (later keys overwrite), recording wrong singlet counts in `results.json`. No
verdict moved (singlets are self-conjugate — the lemma again), but the recorded data was wrong.
Rebuilt from lists, which cannot collapse; dead code removed in the same pass.

## 6. What this does NOT establish

- It does **not** derive *why* the chiral core is the matter (that is the registerability story +
  B864's anomaly arrow); it shows the choice of ket **cannot affect the cascade's outcomes**.
- Nothing about values, generations, the real form, or spacetime.

## Carried forward

G6 (the three involutions — next), G4 (the false-positive control), G7 (the lift), G5 (the
keystone stage).

`tests/test_b865_padding.py`
