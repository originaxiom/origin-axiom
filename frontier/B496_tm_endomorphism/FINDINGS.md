# B496 — The Thue–Morse endomorphism enters the program (the singular monoid on the character variety)

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
pytest ../../tests/test_b496_tm_endomorphism.py
```

## Open (prereg'd)
- **Q1** the mixed semigroup ⟨T_golden, T_TM⟩ on κ=−2 ℚ-points; fate of the figure-eight fixed locus
  under a TM event.
- **Q2** the defect dictionary (TCI Fibonacci defect W²=1+W vs T_TM) — physics-shaped, firewalled.
- **novelty gate** (Axel–Peyrière et al.) when the research tool is available.
- **the spectral lens** (parked, complementary): the symbolic-dynamics/diffraction view — Fibonacci
  (pure-point) × TM (singular-continuous) as a mixed-spectrum construction. See the planned approach.

---

## Q1 — the mixed semigroup ⟨T_golden, T_TM⟩ on κ=−2 (computed 2026-07-10; prereg'd)

**T_golden = (z, x, xz−y)** (σ: A→AB, B→A), verified to PRESERVE κ exactly (it is a unit — the Markov
spine dynamics). Reproducer: `q1_mixed_semigroup.py`.

### Q1(a) — the interaction is EJECTION, not coupling
On κ=−2, one T_TM sends **κ → 2 + 4z² ≥ 2 (over ℝ), never −2** — a **one-way door OFF the Markov
surface** (exact). Example: (3,3,3)→κ′=38; (3,6,15)→κ′=902. Under mixed words the κ-orbit escapes
**super-exponentially** once any TM fires (κ: −2 → 902 → −1.0×10¹⁰ → 1.2×10¹⁷ …); pure-golden words hold
κ=−2 (GGGG stays). So the two monoids do **not** combine into a bounded coupled system on the program's
surface — TM ejects, and golden (κ-preserving) cannot bring a point back. The **shared invariant stage is
the reducible leaf κ=2** (golden preserves every κ; TM fixes κ=2 and acts there as angle-doubling, T4).

### Q1(b) — the figure-eight point: geometry destroyed, ARITHMETIC preserved
The figure-eight A-polynomial curve y=z=x/(x−1) meets κ=−2 at exactly:
- **x = 0** (the reducible/trivial point), and
- **x = (3 ± √−3)/2** — the two **geometric** points (min poly x²−3x+3, the Eisenstein field **ℚ(√−3)** =
  the figure-eight's invariant trace field). These ARE the complete hyperbolic structure's traces.

Under ONE Thue–Morse event:
- the reducible point x=0 → **κ=2** (lands exactly on the TM-fixed reducible leaf), and
- the geometric point x=(3±√−3)/2 → **κ = 8 ∓ 6√−3** (min poly x²−16x+172, disc −432 = −3·144) —
  **still in ℚ(√−3)**. The TM event moves the point OFF the Markov surface (geometry / κ-foliation
  destroyed) but the **Eisenstein field ℚ(√−3) is PRESERVED**.

### Verdict (honest, firewalled)
This concrete form of "interaction" — composing the two trace maps on the shared character variety — is
**destructive, not a bounded coupling**: TM ejects the program's surface to infinity (over ℝ) or to a
generic complex κ (the geometric point), and the monoids share only the reducible κ=2 leaf. So Q1 does
**not** hand the program a delta ingredient in this form — consistent with the "singular/cancellation
verb" reading (S062: the mirror destroys the record). The genuine structural gift: **the arithmetic
signature survives the cancellation** — the figure-eight's Eisenstein field ℚ(√−3) is preserved even as
its geometry is destroyed (the program's recurring theme — residue/field endures, scale/foliation does
not — now visible in the interaction itself). 

**What this narrows:** the trace-map-composition interaction ejects. The remaining live candidate for
"the path" is the COMPLEMENTARY lens (the planned symbolic-dynamics view): Fibonacci (pure-point) × TM
(singular-continuous) as a mixed-spectrum construction — the more physics-natural notion of interaction,
still UNRUN (blocking lit-gate: combined Fibonacci–Thue–Morse aperiodic systems). Q2 (the defect
dictionary) also remains. Firewalled; nothing to CLAIMS.md.
