# B1688 — THE TRICRITICAL ISING MODEL AS ISING TIMES FIBONACCI (P-226): THE RECORD'S c = 7/10 THREAD IS THE PRODUCT OF THE QUBIT LAYER AND THE SEED'S GOLDEN LAYER, AT THE LEVEL OF FUSION AND TWISTS

**Verdict: PROVED (a check of a reading; known mathematics, connected to the record).** cc (main), 2026-10-21.
POINT_REGISTER P-226. 0 of 19.
- **What is checked.** The fusion ring of the tricritical Ising model M(5, 4) (c = 7/10), computed from its S-matrix by
  Verlinde's formula, equals the product of the Ising fusion ring (1, σ, ε) and the Fibonacci fusion ring (1, τ). There is
  exactly one bijection of labels (fixing the identity).
- **The twists.** Under that bijection the conformal weights agree mod 1 with exactly one product of an Ising-type and a
  Fibonacci-type theory: Ising with ν = 7 (h_σ = 7/16) times the conjugate Fibonacci theory (h_τ = 3/5). Its central
  charge is 7/2 − 14/5 ≡ 7/10 mod 8, the tricritical Ising model's own.
- **The map.** ε″ (h = 3/2, the N = 1 supercurrent) ↔ ε ⊗ 1; σ′ (7/16) ↔ σ ⊗ 1; ε′ (3/5) ↔ 1 ⊗ τ̄; ε (1/10) ↔ ε ⊗ τ̄;
  σ (3/80) ↔ σ ⊗ τ̄. So the supercurrent is the Ising layer's fermion.
- **The reading it supports (P-223, P-225; a reading, not a result).** The weave's common point is the one-qubit Pauli point,
  whose anyonic shadow is the Ising (Clifford) layer. The rule's H₁ matrix LP = [[1, 1], [1, 0]] is the Fibonacci fusion
  matrix, the golden layer. Their product is, at the level of fusion and twists, the first N = 1 superconformal theory:
  the record's banked SUSY thread (c = 7/10; B228, B236). The physical link is known: a chain of Fibonacci anyons with
  antiferromagnetic coupling (the golden chain) is critical at the tricritical Ising point.
- **What it does not do.** It fixes no number of the 19. Fusion rings and twists are discrete data; this is one more
  instance of the record's pattern, that the foundation supplies discrete structure (P-224, B1612, B1615, B1620).

## 0. Seen first

`VERDICT topic-sweep /tricritical|7/10|Fibonacci.*Ising|Ising.*Fibonacci|M\(5,4\)|M\(4,5\)/ (full text): 29 of 1457
arcs on main match (NEGATIVE 9, PROVED 20)` — chiefly B236 (the ordinary and super tricritical Ising cosets are the same
coset (SU(2)₁ × SU(2)₂)/SU(2)₃, and E₇ appears as a coset algebra), B218 (the metallic anyon selection names golden,
Fibonacci and tricritical Ising together), B484 (the relayed "SM gauge group = Fibonacci braiding" frame does not
survive) and B492 (the Verlinde lens returns only the golden ratio). None states the fusion-ring identity.
**Literature:** the fusion rules of the minimal models as su(2)_{p−2} ⊗ su(2)_{q−2} modulo the ℤ/2 identification (the
standard coset construction; Di Francesco–Mathieu–Sénéchal, ch. 10 and 17); the golden chain (Feiguin, Trebst, Ludwig,
Troyer, Kitaev, Wang, Freedman, Phys. Rev. Lett. 98 (2007) 160409), whose antiferromagnetic critical point is the
tricritical Ising model. The identity checked here is known; the check is main's own.

## 1. The computation (`verification/tci_vs_ising_fib.py` → `tci_vs_ising_fib.json`)

- The Kac table of M(5, 4) with the identification (r, s) ~ (4 − r, 5 − s): six primaries, h = 0, 1/10, 3/5, 3/2,
  7/16, 3/80.
- The S-matrix S_{(r,s),(r′,s′)} = 2 √(2/(pq)) (−1)^{1+sr′+rs′} sin(π p r r′/q) sin(π q s s′/p); orthogonality checked.
- Verlinde's N_ab^c = Σ_x S_ax S_bx S_cx / S_0x, integral to 10⁻⁹.
- The product ring, compared under every bijection of the six labels fixing the identity: one matches.
- The twists, compared mod 1 for the eight Ising-type theories (ν odd, h_σ = ν/16) times Fibonacci or its conjugate:
  one matches, ν = 7 with the conjugate.

## 2. Files

- `verification/tci_vs_ising_fib.py`, `verification/tci_vs_ising_fib.json`.
- The lock: `tests/test_b1688_tricritical_ising_as_ising_times_fibonacci.py`.
