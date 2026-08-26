# B1157 — WF-2 (the dynamics): the ∞-place "dynamical law" reading is **STRUCTURAL RHYME (NULL)**; the closed-Fried antecedent for cc3's B8142b is **REFUTED** by computation

**Status: banked (frontier). Verdict NEGATIVE** — the firewall is **not** crossed (L46 upheld): the object
supplies **no** parameter-free dynamical law at the ∞-place; the "graviton in the analytic torsion / Vol
common scale" reading is generic spectral geometry, not object-specific physics. What is real and banked
is (i) a **decidable mathematics result** — H\*(m004; Sym²ᵐℂ²) is **never acyclic** — that advances cc3's
residue-2 by refuting its naive antecedent, and (ii) the **honest typing** of the story as generic. No
firewall crossing; Gate 5 clean (no SM quantity). Lock `tests/test_b1157_dynamics_null.py`.

## Provenance — the adversarial workflow (WF-2, the masterplan's 2nd)

8 agents (3 scope/verify → gap synthesis → attempt → 2 adversarial refuters → seal; 453k subagent tokens).
The **firewall refuter refuted** the "∞-place dynamical law" framing (structural rhyme); the **correctness
refuter did not refute** the mathematics (`refuted:false`), flagging only a non-fatal toolchain crash. Seal
= **DECIDABLE-RESULT**, banked here as a NEGATIVE (the crossing) + a computed fact (the acyclicity). Every
load-bearing claim re-verified on this bench (`verification/reproduce.sh` → `REPRODUCES`).

## The decidable result — acyclicity fails at every m (own-verified)

The one antecedent cc3 left open in B8142b — *does Fried's theorem apply to ρ(m)=Sym²ᵐℂ² on the cusped
m004?* — was computed from scratch and is **REFUTED for every m**:

| m | dim V=2m+1 | H0(T²) | H1(T²) | (H0,H1,H2)(M) |
|---|---|---|---|---|
| 0 | 1 | 1 | 2 | (1,1,0) |
| ≥1 | 2m+1 | 1 | 2 | (0,1,1) |

**The mechanism (the discriminating fact, own-verified):** m004 has one cusp; its peripheral π₁=⟨μ,λ⟩≅ℤ²
is **parabolic** (regular unipotent). Sym²ᵐ of a regular unipotent is a **single Jordan block** of size
2m+1, so its invariant subspace is a **1-dim line**, and μ,λ **share** it → H0(T²;ρ(m))=1. Then T² Poincaré
duality gives H1(T²)=2, and **half-lives-half-dies** plants H1(M)=½·dim H1(T²)=1; with H0(M)=0 (ρ(m)
irreducible, m≥1) and χ_ρ=(2m+1)·χ(M)=0, this forces **H1=H2=#cusps=1**. So H\* is **never acyclic** — the
closed-manifold Fried hypothesis is refuted, by a purely **peripheral (parabolic-fixed / Eisenstein)**
defect. **Triply corroborated:** the deformation dim H¹(M;Ad)=1 (m004's unique cusp); Menal-Ferrer–Porti's
even-symmetric-power theorem H¹=#cusps (banked **B581**); the WF-2 attempt's independent Fox-calculus
computation.

**Consequence for cc3's B8142b:** the forced reflection formula
|R(−m,σ_m)|=(c(m)/c(m−1))^{2κ}·exp(−4m·Vol/π)·|R(m,σ_m)| **stays conditional** — the naive route to make it
unconditional (closed Fried) does not exist. R_{ρ(m)}(s) has a **nonzero order of vanishing** at s=0
governed by the computed H1=H2=1, not a finite value equal to a torsion. The correct framework is the
**cusped Park/Pfaff** torsion theory (its acyclicity hurdle cleared by the canonical 1-dim cusp-cohomology
basis), not the closed theorem.

## The firewall verdict — STRUCTURAL RHYME (`verification/firewall_null.txt`)

The object supplies **no** ∞-place dynamical law. Every ingredient — the Sym-power factorization, H1=#cusps,
the exp(−4Vol/π) damping — is **generic to all finite-volume hyperbolic 3-manifolds**, using only the
SL(2,ℂ) holonomy and the volume, **never** the arithmetic (ℚ(√−3), E₆, ξ=[e^{iπ/3}]∈K₃(ℚ(√−3))). The whole
three-link story survives swapping m004 for a non-arithmetic knot **verbatim** — the **B996 lesson**
("reaching E₆ is generic; specialness lives in the grammar, not the destination") now at the ∞-place. The
Vol "coincidence" (B1156's regulator = B8142b's damping) is the tautology **Vol(M)=Vol(M)**: both are
functions of the one hyperbolic structure. "Graviton in the torsion" is a **rep-label** (the top SO(3)
weight of Sym²ᵐ), not dynamics — no propagator, no kinetic term, no Ward identity; the nearest realization
(Ruelle zeta = topological BF) has no propagating graviton. **"Dynamical" is unearned** — spectral geometry
supplies invariants, not equations of motion.

## What is bank-grade vs specialist vs relayed

- **BANK-GRADE (cc3 B8142 credited):** the Sym-power factorization R_{ρ(m)}(s)=∏_{j=−m}^{m} R(s−j,σ_j) —
  independently re-derived two ways (symbolic Sym²ᵐ eigenvalue algebra + numeric) and reproduced on m004 to
  |diff|≤5×10⁻¹⁸ (m=0..4, three controls firing). Elementary; cc3 claims no novelty and none is owed.
- **THIS SEAT'S OWN (decidable):** the acyclicity refutation via the invariant-line mechanism + standard
  topology (`reproduce.sh`), and the Vol/damping numerics.
- **SPECIALIST (sharpened NEEDS-SPECIALIST), three residual items:** (1) the order of vanishing / leading
  Laurent coefficient of R_{ρ(m)}(s) at s=0 in the **Cappell–Miller complex-orthogonal** torsion (ρ(m) is
  orthogonal-not-unitary — preserves J_{i,n−i}=(−1)ⁱ/C(n,i)); (2) the exact Park/Pfaff cusp/Borel–Serre
  scattering correction **as an equation**, and the test that it equals exp(−4m·Vol/π) (ingredient in hand:
  φ(s)=Λ_K(s−1)/Λ_K(s), φ(s)φ(2−s)=1, B8101); (3) the twisted-Ruelle functional equation s↔2−s (named
  B8101, not derived).
- **RELAYED to cc3 (verify-don't-trust catch, non-fatal):** `exact_check.py` in the B8142 toolchain crashes
  at line 39 (sympy **structural** equality on unsimplified entries — ρ(relator)−I is zero only after
  `sp.simplify`), so the "exact ℚ(√−3) re-confirmation, not an SVD artifact" claim is not backed by that
  file as shipped. The conclusion stands anyway (integer-robust numeric ranks, triply corroborated).

## Fences

No firewall crossing claimed — the ∞-place story is generic spectral geometry. Gate 5 clean (no SM number).
The acyclicity result is own-derived + triply corroborated; the Sym-power identity is cc3's (credited,
re-verified); the c(m)/c(2) and Pfaff exp(−2m·Vol/π) structure (B8104/B8112) enter as inputs, not
re-derived. The "object forces a parameter-free dynamical law" synthesis is **quarantined** (refuted by the
firewall lens). Codex/cc3 primary toolchain off-branch (provenance debt, not leaned on).

## Routes

- **kill_graph:** the node *"the object's ∞-place supplies a parameter-free dynamical law that crosses the
  firewall"* is **killed** — structural rhyme (generic to hyperbolic 3-manifolds).
- **L182 / residue-2:** cc3's B8142b reflection stays conditional; the closed-Fried route is refuted; the
  live framework is cusped Park/Pfaff torsion. The three specialist sub-items above are the sharpened bar.
- **Relay:** the `exact_check.py` crash + the acyclicity refutation → CC_TO_CC3 (useful to their residue-2).
