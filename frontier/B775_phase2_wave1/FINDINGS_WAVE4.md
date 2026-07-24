# B775 FINDINGS — PHASE 2 WAVE 4 (8 cells; addendum ddf99ceb)

*2026-07-24. Workflow wf_8d6eef66-733 (interrupted once, resumed from cache). **4 banked, 4 carry** (corrected after the full verify records landed). Z1 cc-self-verified (its verify record was still landing; the claim is directly
checkable and cc checked it). Machine table wave4_results.json.*

## Banked (4)

| cell | verdict | result |
|---|---|---|
| **P2W4-L54** | **RESOLVED-A** | the adjoint Reidemeister torsion of 4₁ computed EXACTLY in-cell by first-principles Fox/Wada (torsion polynomial T²−5T+1, τ₁=−3) — one gate-A residual closed. **CORRECTION (full verify):** "two independent ways" OVERSTATED — route B was *cross-checked against B98's banked Jacobian formula (re-substituted), not recomputed in-cell*. The verifier recomputed it and B98 is right, and found something STRONGER: the identical torsion arises on BOTH conjugate geometric reps, so Galois-invariance holds at the level of the whole first-principles torsion. |
| **P2W4-R2** | **RESOLVED-B → CLOSED (negative)** | R2's fixed locus Fix(T₂²) is **POSITIVE-DIMENSIONAL** (Krull dim 2, and still dim 2 after the full self-dual/SL reduction) — **R2 sealing genuinely FAILS**. A question closed by a real negative. |
| **P2W4-HEAR** | **RESOLVED-B → an AXIOM REPRICED** | H-EAR forces only the Galois PAIR {SU(3)₂ κ=5, SU(5)₁ κ=6}, **not κ=5 alone** — so the "minimal bearing stage κ=5" is a **PRICED CHOICE, not a theorem**. A correction to the program's own accounting (an assumed theorem demoted to a declared choice — exactly what the going-forward rule demands). |
| **P2W4-L38** | **RESOLVED-B → EXTERNAL** | the κ=−2 deformation scale computed with full structure — exponent **Vol₀ = 2.0298832128** (the figure-eight volume itself), deformation law κ+2; no forced tiny number (Gate 5: structural, no SM Higgs claim, pin untouched). |

## Carry (4) — B772/MB12-class catches + one cc write-up error

| **P2W4-Z1** | **verdict RESOLVED-B is CORRECT and fully reproduced**, but the claim text carries two false statements — **one of them cc's own**: (a) **cc wrote irrationality "exactly when 5\|κ" (an IFF). FALSE** — κ=15,20,25 are divisible by 5 with rational Z. Only **irrational ⟹ 5\|κ** is forced; the cell's own output correctly said "only at", and cc introduced the iff in the write-up (an **E4: necessary-read-as-sufficient**, cc's own instance). (b) the cell's characteristic-prime exemplars are wrong (κ=32,34,39 DO have characteristic primes; the computed C5-failing set is {14,15,18,20,21,28,29,31}). The genuine content survives: the ladder IS lawless in the level and every Z_k ∈ ℤ[φ] (scope: k≤28). Carry: fix both statements, and replace the lock's six hardcoded values with a recomputation. |
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
