# Origin Axiom: Handoff Document

## Project Status: May 21, 2026

### What's Proven (all verified computationally)

**The Matrix:**
- A = [[2,1],[1,1]], det=1, trace=3, eigenvalues φ² and φ⁻²
- Characteristic polynomial t²−3t+1 = Alexander polynomial of figure-eight knot
- F = [[1,1],[1,0]], A = F² (orientation-preserving square)
- P·N²_τ·P = A (Fibonacci fusion operator lock, exact matrix identity)

**The Sieve (five independent filters, all selecting A):**
1. Trace-3 algebraic sieve: only trace satisfying hyperbolic + torsion-free for punctured torus bundles
2. Minimum volume: V = 2.0299 (Cao-Meyerhoff theorem, smallest cusped hyperbolic)
3. Amphichirality + CS=0: figure-eight uniquely satisfies among vol < 3.5 census
4. Rank-2 categorifiability: only m=1 (Fibonacci) categorifies (Ostrik classification)
5. Eisenstein triangulation: only figure-eight + sister built from regular ideal tetrahedra; sister eliminated by torsion + CS

**The Factorization (verified in three coordinates):**
- State-integral: (p²−3p+1)(p²+p+1) = (disc 5)(disc −3)
- Gluing equation: (z²−z−1)(z²−z+1) = (disc 5)(disc −3)
- Invariant data: monodromy disc 5, trace field disc −3
- Competitor polynomial p⁴−2p³−5p²−2p+1 is irreducible (verified)
- Census: factorization unique among 11 tested manifolds

**The Gluing Identity (verified by Sympy):**
- S_A(q,Q) = ext_{m,s} [S_L(m,Q) − F_R(q,s) + ms]
- On-shell: S_A = q² − qQ + Q²/2 (matches A exactly)
- Boundary recurrence: q_{n+1} − 2q_n + q_{n-1} = 0 (trace 2, massless)
- Bulk recurrence: q_{n+1} − 3q_n + q_{n-1} = 0 (trace 3, massive)
- Mass gap emerges from gluing: Δtrace = 3−2 = 1

**Causal Emergence (verified numerically):**
- L preserves only [[0,0],[0,c]] (rank 1, degenerate)
- R preserves only [[a,0],[0,0]] (rank 1, degenerate)
- A preserves G = [[-2,1],[1,2]] (rank 2, non-degenerate, indefinite, det=−5)
- Null directions of G = φ-eigenvectors of A (G(φ,1) = 0, verified to machine precision)
- The gluing creates: mass, metric, and causal structure simultaneously

**Continuum Limit (Step 1B, verified):**
- Wick-rotated dispersion: ω² = k² + m² (standard massive Klein-Gordon)
- Mass gap: m·a = √(T−2) = 1 for trace T=3
- Momentum at mass shell: ka = arccosh(3/2) = log(φ²)
- H = log(A) is real symmetric, eigenvalues ±log(φ²)

**SnapPy Data (Step 3A, verified):**
- Figure-eight: vol=2.0299, H₁=Z, CS=0, amphichiral, shape z=e^{iπ/3}
- Sister m003: vol=2.0299, H₁=Z⊕Z/5, CS=0.25, NOT amphichiral by CS
- Trace field: Q(√−3) (Eisenstein)
- Tetrahedra: 2 regular ideal, both Eisenstein

**A-polynomial (Step 4A, verified):**
- A(M,L) = L²M⁴ + L(−M⁸+M⁶+2M⁴+M²−1) + M⁴
- Complete structure: (M,L) = (1,−1), double point
- Gluing equation z²(z−1)²=1 factors as (z²−z+1)(z²−z−1) = (Eisenstein)(golden)

### What's Dead (negative results, do not revive)

- k ≈ 137 cosmological constant (wrong CS normalization)
- Λ = φ^{−2N} without derived N (circular)
- Dynamic Λ(t) ~ t^{−1.925} (ruled out at 30σ, w ≈ −0.04)
- |Z| = 1/φ as unique to figure-eight (generic cyclotomic)
- Casimir energy depends on φ (universal, not distinguished)
- Phonon stability at φ (flat across ratios)
- Cusp shape minimizes Epstein zeta (figure-eight cusp is RECTANGULAR, not equilateral)
- Naive Jones-root φ² equality (|V(e^{2πi/5})| = √5−1, not φ²)
- Fixed Fibonacci Turaev-Viro returning φ² (normalization cancels)
- Combined bulk+cusp vacuum energy minimality (cusp claim was wrong)

### What's Next (the path to 3+1 Einstein)

**Step 3B** (NEXT — map gluing to discrete CS flatness equation):
- Map S_L, F_R to CS connection components (e, ω)
- Show stationarity conditions = flatness F=0
- Key question: does W = S_L − F_R + ms map to F_CS = 0?

**Step 4B** (evolution on moduli space):
- A acts on A-polynomial curve as (M,L) → (M²L, ML)
- Track orbits near complete structure (1,−1)
- Continuum limit of orbit equation → gravity EOM?

**Step 5A** (build 4D Regge complex):
- Stack figure-eight slices by monodromy A
- Count 4-simplices, edges, triangles
- Explicit combinatorial construction

**Steps 5B-5C** (Regge equations → Einstein):
- Compute deficit angles on 4D complex
- Write Regge equations
- Continuum limit → Einstein's equations with Λ?

**Step 6** (identify Λ from figure-eight data):
- Which invariant sets the cosmological constant?
- Candidates: Vol/(4π²), log(φ²), torsion, Borel regulator
- THE OPEN PRIZE

### Repository Structure

```
origin-axiom/
├── README.md
├── requirements.txt (numpy, scipy, sympy, snappy-manifolds)
├── src/
│   ├── algebra/        # F, A, L, R, generating functions, preserved forms
│   ├── topology/       # SnapPy interface, manifold data, census
│   ├── symplectic/     # Gluing identity, Hessians, causal structure
│   ├── dispersion/     # Continuum limits, Wick rotation
│   ├── moduli/         # A-polynomial, deformation space, evolution
│   └── regge/          # 4D complex, deficit angles, Regge equations
├── tests/
│   ├── test_algebra.py     # Assert trace=3, det=1, eigenvalues=φ²
│   ├── test_gluing.py      # Assert S_A = ext[S_L - F_R + ms]
│   ├── test_causal.py      # Assert G null directions = φ eigenvectors
│   ├── test_factorization.py  # Assert (disc 5)(disc -3) split
│   ├── test_dispersion.py  # Assert Klein-Gordon dispersion
│   └── test_snapdata.py    # Assert all SnapPy values match
├── notebooks/
│   ├── 01_selection_sieve.ipynb
│   ├── 02_gluing_identity.ipynb
│   ├── 03_causal_emergence.ipynb
│   ├── 04_path_to_einstein.ipynb
│   └── 05_frontier.ipynb
├── paper/
│   ├── origin_axiom_final.tex
│   ├── figures/
│   └── origin_axiom_final.pdf
└── data/
    ├── manifold_census.json
    ├── factorization_results.json
    └── snapdata.json
```

### Key Numbers (for test assertions)

```python
phi = 1.6180339887498949
phi_sq = 2.6180339887498949
log_phi_sq = 0.9624236501192069
vol_fig8 = 2.0298832128
arccosh_3_2 = 0.9624236501192069  # = log(phi^2) exactly
det_G = -5  # preserved form determinant
cs_fig8 = 0.0  # Chern-Simons invariant
cs_sister = 0.25
```
