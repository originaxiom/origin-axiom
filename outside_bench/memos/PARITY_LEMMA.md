# THE PARITY LEMMA — projective ⟺ even orbit: the criterion's second clause is provably redundant, and the parity of matter is decided by the adjoint alone
## (outside bench, 2026-08-25; thirty-fourth memo; campaign cell A5; a lemma-grade sharpening of memo 30, proof by exact exhaustive lattice check)

### The question
Memo 2/30's projectivity criterion for a stratum's 27-parity reads: all weighted-Dynkin
labels even AND ⟨ω₁,H⟩ even. In memo 30's completed 20-row dictionary the AND never
bit — all 9 even-labeled rows were projective. Coincidence of the realized
characteristics, or a theorem?

### THE LEMMA (`certificates/a5_parity_lemma.py`, exact, E₆-specific)
For every even-labeled element of the coroot lattice — not just the 9 realized
characteristics, all **13** dominant {0,2}-labelings with H = Σcⱼωⱼ∨ integral in the
coroot basis (h of an sl₂-triple always lies there) — **⟨ω₁,H⟩ = m₁ is even**,
verified case-by-exact-case. Hence on the 27:

> **PROJECTIVE ⟺ EVEN ORBIT.** The parity of a stratum's matter content is decided
> by the adjoint data alone; the ⟨ω₁,H⟩ clause is redundant for E₆.

All 9 banked even characteristics of memo 30 appear among the 13 candidates
(cross-checked); the odd side needs no lemma (an odd label puts an odd value directly
into the adjoint grading, and memo 30's data shows every 1-labeled row odd on the 27).

### Why it matters
The cleanest citable form of the dictionary: fermion-capability of a stratum = its
Bala–Carter orbit is non-even — a statement entirely in the classical orbit
taxonomy, with the 27 no longer needed to test it. The mechanism behind the
redundancy is the ℤ/3 center (3ω₁ ∈ root lattice: the only possible obstruction to
integrality is 3-torsion, never 2-torsion) — stated as the reading; the proof banked
here is the finite exact check, which for E₆ is exhaustive and unconditional.

### Fences
E₆-specific (the lemma is proved by exhaustion of E₆'s lattice, not claimed for other
types); the Cartan matrix is the bench's banked one (recovered from exact brackets in
memo 30's certificate, asserted symmetric here). Gate 5 untouched.

### Certificates
`certificates/a5_parity_lemma.py`; output `outputs/a5_parity_lemma_out.txt`.

### One sentence for the ledger
Whether a stratum can carry fermions is written entirely in its orbit's evenness — the
27 never has to be consulted — because in E₆ the lattice itself forbids an
even-labeled coroot element from pairing oddly with the matter weight.
