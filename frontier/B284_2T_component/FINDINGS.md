# B284 — adjudicating chat-1's five claims (verify-don't-trust, both directions)

**Status: banked. Math (claim 3) computed here; physics (claims 1,2,4,5) firewalled in S044.** chat-1 responded to
the Alexander-paper reading with five claims — some correcting *me*, some overstated. Each adjudicated by in-sandbox
verification. Net: chat-1 corrected my position on **2 of 5**; I corrected chat-1 on **2 of 5**; **1** is a fair open
reframe. Both chats made errors — exactly why we verify.

## The computed core — claim 3: the 2T-factoring representation
chat-1: *"the figure-eight has a 2T-factoring component with structure the generic smooth point lacks."*

Computed (`twoT_component.py`, exact):
- **The finite-image 2T rep exists exactly.** Order-3 meridians at the **tetrahedral angle cos α = −1/3**, relator
  residual `2e-15`, **image order 24 = 2T**. It is the arithmetic **reduction mod 3** of the geometric rep: the
  Riley polynomial is `u(u²+u+1)²`, geometric root `u = ω ∈ ℚ(√−3)`, meridian trace `2 → −1 (mod 3)` = the 2T
  rep's trace. Object-specific: exists only because `π₁(4₁) ↠ 2T` (B282: 5₂/6₁/6₂/7₄ do not).
- **But its local structure is GENERIC.** `dim_ℂ H¹(Ad) = 1` — identical to the geometric rep (matches B264). So the
  2T rep is a **special finite-image POINT on the generic canonical component**, a smooth point with the ordinary
  cusp-deformation dimension, **not** a distinguished component with anomalous local structure.

**Verdict (claim 3): kernel RIGHT, stronger form FAILS.** Object-specific *existence* — yes; anomalous *component* —
no. This **reinforces B282**: the figure-eight's object-specificity is *global/arithmetic* (does the character curve
pass through a 2T point at all) not *local/geometric* (the local deformation theory is generic everywhere).
*(Method note: H¹ must use the complex sl₂ adjoint; a real-su(2) projection is valid only for the SU(2) 2T rep and
wrongly gives 0 for the SL(2,ℂ) geometric rep — caught mid-verification.)*

## The other four claims
| # | claim | call | basis |
|---|---|---|---|
| 1 | Λ dynamical / conjugate to CS-time (the dynamics I dismissed) | **chat-1 RIGHT, I was wrong** | arXiv:1807.01381 (Alexander–Magueijo–Smolin 2018) is real and says exactly this. I mis-attributed by reading only the 2026 PRL. *Residual:* conjugacy + uncertainty, **not** a derived `k(t)`, so "k runs 3→10¹²²" is still unshown. |
| 2 | `Γ ~ exp(−k·Vol)` is standard semiclassical physics | **partially right** | the hyperbolic volume in CS/WRT asymptotics is real (volume conjecture). I over-dismissed the kernel. But reading it as a *cosmological tunneling rate* (4₁ = the instanton) is a modeling step, not textbook. |
| 4 | `S = k/2`, `T = √(k/2π)` from `Λ=6π/(kG)` + Gibbons-Hawking | **S=k/2 right; T mislabeled** | `S = k/2` exact (= the earlier `k = 2·S_dS`). `√(k/2π)` is the de Sitter **radius**, not the temperature; GH temperature `= 1/√(2πkG) ~ 1/√k`. chat-1's own slip. |
| 5 | Λ-sign from the CS level (k>0 ⟹ Λ>0), not 4₁'s curvature | **conceptually fair (candidate wall-dissolution)** | in CSK `Λ=6π/(kG)` ⟹ `sign Λ = sign k`, Kodama = de Sitter (Λ>0); 4₁'s hyperbolicity is a *different* 3-manifold. So the B278 "hyperbolic→Λ<0" wall may be a category error. Caveat: requires 4₁'s role not be the spacetime metric. Recorded, not yet banked as dissolving the wall. |

## chat-1's meta-claim (synthesis across papers)
Fair: the dynamics is in the **2018** paper, the protection in the **2026** paper, and no single source is the whole
picture — my per-paper checking under-weighted the 2018 source. Granted. But "synthesis" does not lower the bar: the
2018 paper gives *conjugacy + uncertainty*, not a *solved k(t)*; the volume-rate is a *model*, not a theorem; and the
figure-eight still appears in **none** of the papers (the object↔framework identification remains the program's HOOK).

`twoT_component.py` · `verdict.py` · `tests/test_b284_2T_component.py`.
