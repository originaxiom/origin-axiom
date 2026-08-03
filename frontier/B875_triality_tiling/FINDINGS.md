# B875 — the triality-tiling theorem VERIFIED on this seat's build: e₆ = (so(8)⊕u(1)²) ⊕ V₁ ⊕ V₂ ⊕ V₃ with the cyclic law

cc banking seat, 2026-08-03. Verification of the solo seat's triality-tiling theorem (their
JOINT NOTE + three-prime certificates) on this seat's **fully independent** B854 build.
Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 1. What was claimed (solo seat, same day)

The three enhanced centralizers K₁, K₂, K₃ (at the S₃ Galois triple of distinguished charges)
tile e₆: Kᵢ = core ⊕ Vᵢ with core = so(8)⊕u(1)² (dim 30) and dim Vᵢ = 16; pairwise
Kᵢ∩Kⱼ = core; jointly they span e₆; and the sectors obey **[Vᵢ,Vᵢ] ⊆ core** (charge-2 gate)
and **[Vᵢ,Vⱼ] = V_k** (the cyclic law). Each so(10)ᵢ = core ⊕ Vᵢ; each generation pair
(the coset 16⊕16̄) = Vⱼ ⊕ V_k — *"choose a breaking and your matter is the other two ways of
seeing."*

## 2. Verified here — three legs, one reproducer

| leg | result | verdict |
|---|---|---|
| **skeleton** (30 digits) | kernels (46,46,46) at t = 13×banked roots; K∩K = **30** all three pairs; span = **78** | ✓ |
| **core type** (mod 40009, 40037 — this seat's own primes) | dim 30, derived 28, center 2; derived rank ≤ 4 forces **D₄ = so(8)** | ✓ |
| **the law** (30 digits, oblique) | [Vᵢ,Vᵢ] → core purely; [V₁,V₂] → V₃, [V₁,V₃] → V₂, [V₂,V₃] → V₁; foreign components ~**1e-23** | ✓ |

Sectors built with the solo seat's canonical definition Vᵢ = ad(z)(Kᵢ), z generic in the core's
center = span(x₈, x₁₆) (each invariant is central in its own centralizer — no extra computation
needed to see the center).

## 3. The trap this arc documents: the sectors are NEARLY PARALLEL

The three Galois roots lie within ~10⁻³ of each other, so K₁, K₂, K₃ are close perturbations and
the sectors V₁, V₂, V₃ are **nearly parallel as subspaces**. Consequence, recorded because it
will bite any future rerun: **orthogonal projections cannot separate the sectors** — a naive
projector test reads 1.0 on every sector for every bracket (observed here first, diagnosed
second). The law is only readable in the **oblique direct-sum basis** [core|V₁|V₂|V₃] (exact
rank 78 by the skeleton; condition ~1.3×10¹¹, comfortable at 30 digits). The solo seat's mod-p
component method is immune to this trap; floating-point reruns are not.

## 4. What this does and does not establish

- The tiling now stands on **two seats, two independent builds, two method families** (their
  mod-p certificates; this seat's high-precision oblique numerics + own-prime type check).
- Combined with B874: the **soft plane of the census IS the triality direction** — the census
  cliff (30 vs 12) is the so(8) core showing through.
- The generation reading — each breaking's matter = the two foreign sectors — remains **a
  structure, not a generations mechanism**. The solo seat's own wording ("unproven as
  generations") is kept. The deciding computation is THE DESCENT (the graded multiplication
  table at the SM level), queued as the next joint cell.
- Nothing here touches values or Gate 5.

`tests/test_b875_tiling.py`
