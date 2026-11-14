# Origin Axiom: Execution Plan

## STATUS: What's Done

### Completed Computations (all code in /paper1/code/)
- [x] 01_hurwitz.py — Hurwitz bound saturation, decay exponents, CF analysis
- [x] 02_hofstadter.py — Spectral gaps, fractal dimension, gap scaling
- [x] 03_small_denominators.py — Perturbative correction sums, three-body denominators
- [x] 04_markov_chain.py — Markov tree, Lagrange spectrum, Kashaev invariant
- [x] 05_berry_phase.py — FHS Chern numbers, Berry curvature uniformity
- [x] Negative results: Casimir, NC torus, phonon stability, Chern scaling

### Paper 1: Written (draft)
- File: paper1_golden_ratio_quantum_spectra.md
- Status: Complete first draft, needs formatting for journal submission

---

## IMMEDIATE NEXT STEPS (Days 1-14)

### 1. Format Paper 1 for submission
- **Target journal:** Letters in Mathematical Physics (matches scope exactly)
- Convert markdown to LaTeX
- Add proper equation numbering
- Generate publication-quality figures from computation data
- Ensure all references are complete with DOI/arXiv numbers

### 2. Create public code repository
- GitHub repo: origin-axiom-computations
- Include all 5 scripts with README
- Add requirements.txt (numpy, scipy)
- Include raw JSON data files
- License: MIT

### 3. Critical computation: Jeffrey's formula
- **Paper found:** Jeffrey, "Chern-Simons-Witten invariants of lens spaces and torus bundles" — gives Z(X_U, r) for torus bundle with SL(2,Z) monodromy U
- **What to compute:** Evaluate Z for U = [[2,1],[1,1]] (figure-eight/Fibonacci) versus other hyperbolic monodromies: [[3,1],[1,0]], [[3,2],[1,1]], [[4,1],[1,0]], etc.
- **What we're looking for:** Is the figure-eight partition function extremal (minimal or maximal) among all hyperbolic torus bundles?
- This is the missing computation for Paper 2

---

## SHORT-TERM STEPS (Weeks 3-8)

### 4. Literature deep-dive
Key papers to read and cite:

**Quantum Teichmuller:**
- Chekhov & Fock, "Quantum Teichmuller space" (1999) — foundational
- Kashaev, "Quantization of Teichmuller spaces" (1998) — Lett. Math. Phys.
- Frenkel & Kim, "Quantum Teichmuller space from quantum plane" (2010) — connects to quantum torus, mentions projective modules indexed by rationals

**Volume Conjecture:**
- Kashaev (1997) — original conjecture
- Murakami & Murakami (2001) — identification with colored Jones
- Wong & Yang (2020) — proved for Dehn surgeries on figure-eight

**3d/3d Correspondence:**
- Terashima & Yamazaki (2011) — CS on mapping torus = 3d N=2 theory
- Dimofte, Gaiotto, Gukov (2014) — 3-manifolds and 3d theories

**Markov surface and character varieties:**
- Goldman (1997) — symplectic structure on character varieties
- Bowditch (1998) — Markov triples and quasi-Fuchsian groups

### 5. Compute: WRT invariant as function of monodromy
- The Witten-Reshetikhin-Turaev invariant for mapping tori can be computed from the trace of the quantum representation of the mapping class group element
- For SU(2) at level k: Z(X_U, k) = Tr(rho_k(U)) where rho_k is the level-k representation on the Hilbert space of the torus
- The Hilbert space has dimension k-1, and the representation is given by Dehn twist matrices
- **Concrete calculation:** Compute |Z(X_U, k)| for U = F^n (n-th power of Fibonacci matrix) and for other hyperbolic elements, at levels k = 3,4,...,50

---

## MEDIUM-TERM STEPS (Months 2-6)

### 6. Paper 2: The Topological Obstruction
**Title:** "Topological frustration and the golden ratio: extremality of the figure-eight knot in quantum Chern-Simons theory"

**Core computation:** Show that among all hyperbolic once-punctured torus bundles, the figure-eight (Fibonacci monodromy) extremizes some physically meaningful quantity:
- The absolute value of the WRT invariant?
- The rate of growth of the Kashaev invariant?
- The spectral gap of the quantum Teichmuller representation?

**Key insight from today's literature:** 
- Terashima-Yamazaki (2011) show CS on mapping torus reproduces hyperbolic volume in classical limit
- The figure-eight has MINIMAL volume (Cao-Meyerhoff)
- Therefore the figure-eight should have the MINIMAL classical CS action
- Question: does minimality persist at the quantum level?

### 7. Contact collaborators
**Priority targets (in order):**

1. **Rinat Kashaev** (Geneva) — invented the invariant, works on quantum Teichmuller. Bring: Paper 1 + the extremality computation.

2. **Tudor Dimofte** (Edinburgh) — 3d/3d correspondence, mapping tori, Chern-Simons. Bring: the specific question about monodromy dependence.

3. **Stavros Garoufalidis** (SUSTech / Max Planck) — resurgence in CS theory, q-series. Bring: the connection between Hurwitz irrationality and CS asymptotics.

4. **Sergei Gukov** (Caltech) — quantum knot invariants, physics of 3-manifolds. Bring: the full chain from phi to quantum gravity.

**What to say:** "I have numerical evidence that the golden ratio's number-theoretic extremality (Hurwitz theorem) propagates through the Fibonacci chain, Markov surface, and character variety to the figure-eight knot complement, whose Chern-Simons partition function computes 2+1 quantum gravity. Is the partition function extremal at Fibonacci monodromy? Here's my computation."

---

## LONG-TERM STEPS (Months 6-24)

### 8. The 3+1 extension
Two possible routes:

**Route A: Holographic.** AdS_3/CFT_2 relates 2+1 gravity to 2d conformal field theory. The modular properties of the CFT partition function (which involve the Dedekind eta function, which we computed at tau = i*phi) might encode information about the 3+1 bulk.

**Route B: 4-manifolds.** The figure-eight knot complement geometrically bounds a hyperbolic 4-manifold with Euler characteristic 1 (Slavich 2017, found in literature search). This means there IS a 4-manifold whose boundary is the phi-controlled 3-manifold. The Seiberg-Witten or Donaldson invariants of this 4-manifold might carry information relevant to 3+1 physics.

### 9. Paper 3: The Origin Axiom
Only after Papers 1 and 2 are published and vetted.

**Core philosophical claim:** Existence is a topological frustration. The character variety of punctured spacetime cannot reach zero. Among all possible punctures, the one controlled by phi produces the minimal nonzero value — the most irreducible form of existence.

**Mathematical formalization:** The cosmological constant is related to the hyperbolic volume of the simplest knot complement through: Lambda ~ exp(-Vol/(G_Newton * something)). If the figure-eight volume 2.0299 can be connected to the observed Lambda through dimensional analysis, the circle closes.

---

## RESOURCES NEEDED

1. **arXiv access:** Free (all papers above are on arXiv)
2. **Computing:** Laptop sufficient for all computations done so far
3. **Collaborator:** Essential for Papers 2 and 3. One physicist who works on quantum Teichmuller or Chern-Simons theory.
4. **Conference:** Attend one meeting on quantum topology or mathematical physics to present Paper 1 results. Targets: Strings (annual), QTS (Quantum Topology and Symmetry), Knots in Washington.

---

## SUCCESS CRITERIA

**Paper 1 (achievable independently):**
Published in a peer-reviewed mathematics/mathematical physics journal. Establishes the computational chain and reports honest negative results.

**Paper 2 (requires collaborator):**
Shows the figure-eight knot's quantum invariants are extremal among torus bundles. This would establish that phi is selected by quantum gravity, not assumed.

**Paper 3 (speculative):**
Connects the topological structure to the observed cosmological constant. This is the moonshot — high risk, transformative if correct.
