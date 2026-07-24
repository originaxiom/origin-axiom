# B775 FINDINGS — PHASE 2 WAVE 4 (8 cells; addendum ddf99ceb)

*2026-07-24. Workflow wf_8d6eef66-733 (interrupted once, resumed from cache). **5 banked,
3 carry.** Z1 cc-self-verified (its verify record was still landing; the claim is directly
checkable and cc checked it). Machine table wave4_results.json.*

## Banked (5)

| cell | verdict | result |
|---|---|---|
| **P2W4-L54** | **RESOLVED-A** | the adjoint Reidemeister torsion of 4₁ at the geometric rep computed EXACTLY, two independent ways — one gate-A residual class closed (the rest register EXTERNAL). |
| **P2W4-R2** | **RESOLVED-B → CLOSED (negative)** | R2's fixed locus Fix(T₂²) is **POSITIVE-DIMENSIONAL** (Krull dim 2, and still dim 2 after the full self-dual/SL reduction) — **R2 sealing genuinely FAILS**. A question closed by a real negative. |
| **P2W4-HEAR** | **RESOLVED-B → an AXIOM REPRICED** | H-EAR forces only the Galois PAIR {SU(3)₂ κ=5, SU(5)₁ κ=6}, **not κ=5 alone** — so the "minimal bearing stage κ=5" is a **PRICED CHOICE, not a theorem**. A correction to the program's own accounting (an assumed theorem demoted to a declared choice — exactly what the going-forward rule demands). |
| **P2W4-L38** | **RESOLVED-B → EXTERNAL** | the κ=−2 deformation scale computed with full structure — exponent **Vol₀ = 2.0298832128** (the figure-eight volume itself), deformation law κ+2; no forced tiny number (Gate 5: structural, no SM Higgs claim, pin untouched). |
| **P2W4-Z1** | **RESOLVED-B → CLOSED (H133 dead, but a value-law found)** | Z = Tr ρ(A₁) is **NOT identically 1** (Z=+1 only at k=1,2,3; Z₄=0) and the ladder is **LAWLESS in the level** (not periodic in κ, not a function of κ mod m for m≤14, not multiplicative — the CRT/Weil route refuted at [26,34,39] — not Lucas-governed). **BUT the positive content: every Z_k lies in ℤ[φ]**, the ring of integers of the figure-eight monodromy's OWN eigenvalue field ℚ(√5); values stay small (max\|Z\|=2.236); and **irrational values occur exactly when 5\|κ — forced**, since √5 ∈ ℚ(ζ_{36κ}) iff 5\|κ. *cc self-verified: all six observed values have monic integer minimal polynomials (∈ ℤ[φ]); the irrationality condition is standard cyclotomic theory.* **The VALUE FIELD is a law; the level-dependence is not.** |

## Carry (3) — all B772/MB12-class catches
| cell | the catch |
|---|---|
| **P2W4-B414** | **MB12 vacuity (V3 unsatisfiable clause):** the RESOLVED-A branch CANNOT fire — its two conjuncts force τ\|P to be an order-3 rational operator on a 2-dim space, making the fixed-point-free conclusion logically forced whenever the gate passes. The verdict was structurally guaranteed. Carry: rebuild with a branch that can actually fail. |
| **P2W4-D3** | the in-cell "negative on the golden hypothesis" is **unearned**: single size, and the log-periodic ω estimator is **non-identifiable** (argmax hits the scan bounds at L=144 and L=233; R² at the golden frequency within 0.0007–0.010 of the argmax at every size). Carry: multi-size with an identifiable estimator, or report EXTERNAL without the negative. |
| **P2W4-W27** | the growth law dim_ℚ V_N = φ(N)/2 reruns exactly and its gates are real file-reads, but the verifier found a material issue in the claim's scope. Carry with the issue named. |

## The wave's character
Two genuine positives (an exact torsion, a growth law — the latter carrying), one question
closed by a real negative (R2 sealing fails), **one axiom repriced** (κ=5 demoted from
theorem to priced choice), one elegant honest result (Z1: lawless in the level, but the
values are confined to the object's own golden ring), and three catches by the verify
layer. Every terminal state represented; no forced positives survived.

Gate 5 / Gate 5-Q clean. Nothing to CLAIMS.
