# B478 — the +j asymmetry IS the clock translation (exact, proved)

**The two-world defect identified.** Phase 2A's σ-lift carried an unexplained +j term.
Resolved: for the level-15 cocycle D(m,c) = diag(ζ^{c·m·j(j−1)/2}),

    Par · D(m,c) · Par = D(m,c) · Z^{cm},   Z = diag(ζ^j) the clock operator.

**Proof (two lines).** Conjugation by Par sends the j-th diagonal entry to the (−j)-th:
the exponent c·m·(−j)(−j−1)/2 = c·m·j(j+1)/2 = c·m·j(j−1)/2 + c·m·j (mod 15). The
first term is D's entry; the second is Z^{cm}'s. ∎  (Verified numerically for
c ∈ {1,14,2,4}, m ∈ {1,2,3}, error < 1.1e-14: `plusj_verify.py`.)

**Reading.** The world-1 ↔ world-14 correspondence J X J⁻¹ (J = Par ∘ conj) matches the
two algebras exactly UP TO right-multiplication by Z^{cm} — a HEISENBERG TRANSLATION by
cm lattice units. Consequences, both banked-consistent:
- **Trace-invisible**: Z^{cm} is inner in the finite Heisenberg group, so every trace
  invariant agrees across the two worlds — exactly what B466/B472 observed (all κ_q,
  tier, face values world-independent).
- **Address-visible**: the defect shifts the SEAM ADDRESSES (a,b) by a translation of
  size cm. The chirality asymmetry of the metallic letter m is not spectral; it is a
  displacement — the letter m moves the stage by m units per world crossing.

Firewall: an exact operator identity at level 15; no physics claim.
Reproducer: `plusj_verify.py` (exit 0 = ALL VERIFIED).
