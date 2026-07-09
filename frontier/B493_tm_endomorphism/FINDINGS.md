# B493 — The Thue–Morse endomorphism enters the program (the singular monoid on the character variety)

**The exploration-seat handoff (2026-07-09) independently re-derived and verified by the banking seat
(`verify_tm.py`, from scratch — Cayley–Hamilton, symbolic (x,y,z) identities, F_p guards at p=101 &
10007). All of T1–T5, T7 reproduce EXACTLY. E1 kept CITED-CONDITIONAL (not proven). Novelty gate PENDING
(research tool in cooldown). Firewalled — nothing to CLAIMS.md.**

## The object
Thue–Morse a→ab, b→ba is the canonical **singular** element of End(F₂): abelianization [[1,1],[1,1]],
**det 0**, eigenvalues {2, 0}. Where the program's metallic maps are the invertible units (det ±1,
GL(2,ℤ), pure-point/Pisot), TM is the non-invertible, singular-continuous, parity-symmetric complement
(t(b) = swap t(a); the Thue–Morse sequence = parity of the binary digit-sum = the program's own ℤ/2
residue made into a substitution). This probe is the first time the singular part of End(F₂) acts on the
program's Fricke stage X(F₂), coordinates (x,y,z)=(tr A, tr B, tr AB).

## Verified results (all EXACT, independently re-derived)
- **T1 — the TM trace map:** T(x,y,z) = **(z, z, xyz − x² − y² + 2)**. Derived via A²=xA−I, B²=yB−I
  (tr A²B² = xyz − x² − y² + 2); confirmed on 20 random SL(2,ℚ) pairs. ✓
- **T2 — the κ law + factorization:** κ′ = κ² − (κ−2)z² − 2, and it factors **exactly**:
  **κ′ − 2 = (κ − 2)(x² + y² − xyz)** (symbolic 0; F_p-guarded at two primes). So the reducible locus
  κ=2 is invariant (semi-invariant ideal (κ−2), multiplier x²+y²−xyz), and the program's Markov surface
  **κ=−2 is mapped OFF every level set to κ′ = 2 + 4z²** — the singular map *destroys the whole
  κ-foliation except the reducible leaf.* ✓
- **T3 — collapse + cocycle:** the image lies in the plane x=y after one step (det-0 seen dynamically);
  on that plane (u=x=y, v=z), the map is (u,v)→(v, u²(v−2)+2), i.e. in w=v−2: **w′ = u²·w** — frustrated
  self-cancellation as a multiplicative cocycle. ✓
- **T4 — exact angle-doubling:** γ(θ) = (2cos θ, 2cos 2θ) satisfies **F(γ(θ)) = γ(2θ)** exactly, and γ
  lies inside κ=2. The cancellation dynamics is literal angle-doubling on the classical (reducible)
  slice. ✓
- **T5 — degree growth 2:** iterate degrees [3,5,11,21,43,85] (n≤6), recursion a′=b, b′=2a+b, **Perron
  root 2** = the TM substitution eigenvalue. (State as degree growth, not entropy.) ✓
- **T6 — the Perron dichotomy:** TM carries **log 2**, Fibonacci carries **log φ** — the two primordial
  comparisons of End(F₂) carry the two constants. ✓
- **T7 — invariant sweep (negative):** no polynomial invariant of the plane map up to total degree **8**
  except constants (nullspace dim 1). ✓ (extended past the handoff's degree 6.)

## Tiering (honest)
| ID | status |
|---|---|
| T1–T4, T7 | **EXACT, BANKED** (independently re-derived + F_p-guarded) |
| T5 | exact degree data + elementary recursion; "degree growth 2", NOT entropy |
| T6 | exact (substitution eigenvalues) |
| **E1** h_top = log 2 | **CITED-CONDITIONAL** — lower bound exact (T4), upper bound needs Gromov/Dinh–Sibony + noncompactness caveat; NOT banked as proven |
| E2 metallic entropy 2 log λ_m | literature (Cantat 2009) — cite, never claim |
| novelty of T1/T2/T4 | **PENDING lit-gate** (Axel–Peyrière 1989; Allouche–Shallit; Bellissard) — the map T1 is likely KNOWN; the κ-factorization T2 and the exact γ-curve T4 are the candidate-new content. **No "novel" claim until gated.** |
| S (defect-dictionary rhymes) | speculation → speculations/S062, firewalled |
| P014 | philosophy, one-way cite |

## The structural reading (banked as mathematics)
The invertible monoid (metallic units) preserves the κ-foliation and walks the Markov spine — the object
records and survives its own reflection (det −1: distinction survives). The singular monoid (TM) **destroys
the foliation except the reducible leaf**, collapses to the diagonal, and acts as exact angle-doubling
inside κ=2 — the object attempts to cancel itself against its negation (det 0: the mirror destroys what it
copies). The two carry log 2 (TM) and log φ (Fibonacci). This is a real, exact result about how the two
kinds of End(F₂) element act on the shared stage — the concrete form of "the interaction of the two
objects." Whether the interaction supplies a delta ingredient is Q1/Q2 (prereg'd, gated).

## Reproduce
```
python3 verify_tm.py                    # T1-T5, T7 + F_p guards
pytest ../../tests/test_b493_tm_endomorphism.py
```

## Open (prereg'd)
- **Q1** the mixed semigroup ⟨T_golden, T_TM⟩ on κ=−2 ℚ-points; fate of the figure-eight fixed locus
  under a TM event.
- **Q2** the defect dictionary (TCI Fibonacci defect W²=1+W vs T_TM) — physics-shaped, firewalled.
- **novelty gate** (Axel–Peyrière et al.) when the research tool is available.
- **the spectral lens** (parked, complementary): the symbolic-dynamics/diffraction view — Fibonacci
  (pure-point) × TM (singular-continuous) as a mixed-spectrum construction. See the planned approach.
