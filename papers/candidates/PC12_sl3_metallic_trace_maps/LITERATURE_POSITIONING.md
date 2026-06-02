# PC12 Literature Positioning

Status: positioning note + completed literature screen (2026-06-01). The
classification section below is a non-specialist screening pass, not specialist
peer review.

## Best Short Description

PC12 is an `SL(3,C)` rank-two character-variety trace-map dynamics candidate for
the metallic substitution family:

```text
a -> a^m b
b -> a
```

The natural audience is mathematics: character varieties, trace identities,
algebraic dynamics, and computationally assisted arithmetic classification.

## Primary Neighborhoods

```text
SL(3,C) character varieties of free groups
Procesi/Razmyslov trace invariant theory
classical SL(2) trace maps and Fricke-Vogt invariants
Out(F2) and mapping-class actions on character varieties
Bellon-Viallet algebraic entropy and degree growth
```

## Required Framing

The eight trace variables should be framed as standard trace generators in the
rank-two `SL(3,C)` character algebra, not as globally free affine coordinates.
The commutator traces are recovered as a two-valued invariant pair.

The `SL(2)` trace-map literature is an analogy and predecessor. PC12 should not
claim to generalize the full spectral theory of substitution Hamiltonians.

The compact `SU(3)` slice is a compact-unitary restriction of the trace dynamics.
It is not `SU(3)` particle physics.

The multichannel Fibonacci physics literature is a separate bridge question.
Standard matrix-valued or strip tight-binding models use doubled phase-space
transfer matrices, typically `2L x 2L` symplectic matrices for `L` channels.
B52 records this as a negative control for the naive `L=3` bridge.

## Likely Novelty To Validate

```text
explicit metallic SL(3) trace-map family in eight trace generators
commutator trace-pair preservation for the metallic family
exact entropy computation for this family
fixed-line integer splitting classification
compact diagonal SU(3) survival classification
cross-n char(M^k) fixed-line factorization tower (n=3,4 complete, n=5 partial;
  numerical; Appendix A of DRAFT_NOTE.md)
```

Each item must be checked against the literature before PC12 can become
`DRAFTABLE`.

## Conservative Citation Targets

```text
Procesi, The invariant theory of n x n matrices
Lawton, Minimal affine coordinates for SL(3,C) character varieties of free groups
Lawton, Algebraic independence in SL(3,C) character varieties of free groups
standard SL(2) trace-map / Fricke-Vogt references
Bellon-Viallet, Algebraic entropy
degree-growth literature for polynomial or rational maps
matrix-valued / block Jacobi transfer-matrix literature for bridge controls
algebraic entropy = spectral radius for mapping-class actions on character
  varieties (arXiv:0812.0853) -- directly supports the Thm 3 entropy value
Procesi / Sikora SL(n,C) trace generators (for the Appendix A cross-n tower)
```

## Wording To Avoid

```text
new physics
quark model
particle/antiparticle derivation
derived gauge sector
spacetime dictionary
awareness or self-modeling
Origin-core proof
```

Correct wording:

```text
standalone higher-rank trace-map arithmetic candidate
```

---

## Literature Classification (2026-06-01)

Screening pass against the neighborhoods above. **This is a non-specialist
literature screen, not peer review by an `SL(3,C)` character-variety or
substitution-dynamics specialist; overlaps may exist that this screen misses.**
Verdicts: `KNOWN` / `STANDARD_REPACKAGE` / `APPARENTLY_NEW` / `UNCLEAR`.

| Block | Verdict | Basis in the literature |
|---|---|---|
| Thm 1 -- metallic `SL(3)` trace-map formula | STANDARD_REPACKAGE | The coordinate ring of the rank-two `SL(3,C)` character variety is a hypersurface in `C^9` with explicit minimal trace generators (Lawton 2008). Trace maps induced by free-group automorphisms are classical (Horowitz; Procesi). The metallic-family recurrences follow from Cayley-Hamilton reduction in these coordinates. Higher-than-`SL(2)` Fibonacci trace maps already appear in the physics literature (N-ary / ternary Fibonacci lattice, Phys. Lett. A, 1994). |
| Thm 2 -- commutator trace-pair invariant | KNOWN / STANDARD_REPACKAGE | The two values `{tr[A,B], tr[A,B]^-1}` are the standard double-valued commutator coordinate of Lawton's `C^9` hypersurface. Invariance reduces to the group identity `[a^m b, a] ~ [a,b]^-1`, a one-line fact; the automorphism action on the commutator coordinate is standard mapping-class/character-variety theory. |
| Thm 3 -- algebraic entropy `= log` metallic mean | STANDARD_REPACKAGE | Bellon-Viallet algebraic entropy is the exponential degree-growth rate; the "no-cancellation => degree dominance => entropy `= log`(growth rate)" argument is the standard Bellon-Viallet mechanism (degree growth becomes exponential precisely when cancellations are absent). The growth rate is the Perron root of the metallic substitution matrix `[[m,1],[1,0]]`, i.e. the metallic mean `(m+sqrt(m^2+4))/2`. |
| Thm 4 -- fixed-line integer splitting classification | APPARENTLY_NEW (niche / elementary) | No source found classifying when this specific fixed-line Jacobian quartic splits over `Z`. It is an elementary Diophantine classification, not a spectral result; the Damanik-Gorodetski spectral theory of the Fibonacci trace map addresses a different question (hyperbolic non-wandering set, Cantor spectrum). Low general interest, but not located in the literature. |
| Thm 5 -- compact `SU(3)` slice | STANDARD_REPACKAGE / minor | Compact-unitary restriction; the mapping-class action on `SU(3)` character varieties is studied (e.g. arXiv:1909.10968). A small explicit-representative computation. |
| Exchange-symmetry block decomposition | STANDARD | Reversing-symmetry sector decomposition of trace maps is exactly the Baake-Grimm-Roberts "symmetries and reversing symmetries of trace maps" framework (arXiv:math/9901124). |
| Symbolic-`m` factorization proof | STANDARD technique | Symbolic linear algebra over the triple-root `(r-1)^3` Cayley-Hamilton recurrence; proves a sub-component of Thm 4. |

### Overall position

PC12 sits at the **intersection of two established frameworks** -- Lawton's
`SL(3,C)` rank-two character-variety coordinates and the Baake-Grimm-Roberts
theory of substitution trace maps. Thm 1-3, the exchange decomposition, and the
symbolic factorization are **standard methods applied to the metallic family**.
The only component not located in the literature is **Thm 4**, the fixed-line
integer splitting classification, which is elementary and niche.

### Recommendation

Rescale PC12 from a theorem-note to a **short computational report / note**: the
metallic `SL(3)` trace-map family written down explicitly, with entropy and the
commutator invariant credited to standard methods (Bellon-Viallet; Lawton; BGR),
and Thm 4 presented as the one possibly-new arithmetic observation, flagged as
elementary. Heavy theorem-paper proof prose for Thm 1-3 is not warranted. A
specialist read remains the only way to confirm the Thm 4 novelty and the
framing.

### Sources (screening)

```text
Lawton, Minimal Affine Coordinates for SL(3,C) Character Varieties of Free
  Groups -- arXiv:0709.4403 (J. Algebra 320, 2008)
Lawton, Algebraic Independence in SL(3,C) Character Varieties of Free Groups
  -- arXiv:0807.0798
Baake, Grimm, Joseph, Trace maps, invariants, and some of their applications
  -- arXiv:math-ph/9904025
Baake, Roberts, Symmetries and reversing symmetries of trace maps
  -- arXiv:math/9901124
Bellon, Viallet, Algebraic entropy -- Comm. Math. Phys. 204 (1999)
Damanik, Gorodetski, Hyperbolicity of the Trace Map for the Weakly Coupled
  Fibonacci Hamiltonian -- arXiv:0806.0645
Trace map for an N-ternary Fibonacci lattice -- Phys. Lett. A (1994)
The mapping class group action on SU(3)-character varieties -- arXiv:1909.10968
A remark on the trace-map for the silver mean sequence -- arXiv:1010.2476
```

---

## Refresh (2026-06-02)

A second non-specialist web pass, run when the reviewer packet was assembled
(again **not** specialist peer review). It confirmed the 2026-06-01 screen and
added one directly useful citation; it did not overturn any verdict.

- **Thm 3 (entropy) basis strengthened.** "Algebraic Entropy and the Action of
  Mapping Class Groups on Character Varieties" (arXiv:0812.0853) proves
  `e_alg(f) = rho(f)` (algebraic entropy equals the spectral radius of the
  induced action). For `T_m` this is the Perron root of `M=[[m,1],[1,0]]`, i.e.
  `log mu_m` -- so the entropy value is a direct instance of a published theorem,
  reinforcing `STANDARD_REPACKAGE`.
- **Sec 5 sector factorization** remains squarely inside Baake-Grimm-Roberts
  reversing-symmetry theory (arXiv:math/9901124; arXiv:math-ph/9904025);
  the `char(M^k)` form for this family is the open question (Q2 of the packet).
- **Thm 4 splitting classification** and the **Appendix A cross-n tower**: no
  prior source located for either. The neighborhoods are active (Lawton; Sikora;
  Brown on Fricke-character automorphisms; Newhouse phenomena in the Fibonacci
  trace map, arXiv:1507.07912), but nothing matching the specific Diophantine
  classification or the `char(M^k)` fixed-point-linearization tower surfaced.
  Both stay items for the specialist (packet Q1, Q3).

### Additional sources (refresh)

```text
Algebraic entropy and the action of mapping class groups on character varieties
  -- arXiv:0812.0853
Newhouse phenomena in the Fibonacci trace map -- arXiv:1507.07912
```
