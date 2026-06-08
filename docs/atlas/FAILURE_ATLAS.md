# Failure Atlas

Status: obstruction map. Failed routes are first-class results because they
prevent repetition.

## Why This Exists

The project repeatedly found the same pattern:

```text
the proposed mechanism works only after a selector, measure, source, carrier,
unit scale, dictionary, or observable is inserted
```

That is not useless. It identifies the missing object precisely.

## Failure Categories

### Source-Free Zero Cannot Move

If the starting state has no rule, time, source, boundary, or state space, no
calculation can make it leave zero. Routes in this category usually stall before
they become a mathematical system.

Typical missing object:

```text
source law, time step, carrier, boundary condition
```

### Commutative Cancellation Leaves No Residue

If cancellation happens in a commutative setting, inverse contributions cancel
too perfectly. Nothing remains to distinguish order, direction, or memory.

Typical missing object:

```text
distinguishable operations
```

### Selector Inserted Rather Than Derived

Many routes produce multiple valid branches, contours, bases, representations,
or sectors. Picking the useful one is often the whole problem.

Typical missing object:

```text
selection rule
```

### Measure Inserted Rather Than Forced

Statistical and informational routes often work only after choosing a measure
or prior distribution.

Typical missing object:

```text
canonical measure
```

### Units Inserted Rather Than Derived

Dimensionless exact mathematics does not become physics until it has a scale or
unit dictionary.

Typical missing object:

```text
unit bridge
```

### Gauge Dictionary Missing

Topological, algebraic, or spectral structures can resemble gauge data without
specifying which physical fields, groups, charges, and transformations they
represent.

Typical missing object:

```text
field dictionary
```

### Particle Dictionary Missing

A spectrum, representation table, or bound-state calculation is not a particle
model unless the states, masses, couplings, and observables are defined.

Typical missing object:

```text
particle interpretation map
```

### 3+1D Bridge Missing

One-dimensional, two-dimensional, or topological toy systems can be exact while
still lacking a route to observed spacetime.

Typical missing object:

```text
spacetime carrier
```

### Observable Missing

A result becomes physics only when it yields a number, relation, or qualitative
effect that can distinguish it from alternatives.

Typical missing object:

```text
observable with comparison target
```

### Numerology Killed By Controls

Near-hits to famous constants are not evidence unless they survive controls:
alternate conventions, baselines, error models, and independently fixed
parameters.

Typical missing object:

```text
control family
```

### Bridge That Succeeds By Construction

A trace map induced by a substitution is, by definition, the renormalization map
for traces of that substitution's words on the relevant character variety. So a
first-order recursion `psi_{n+1} = M_n psi_n` with `M_n` in `SL(3)` driven by the
metallic substitution reproduces the PC12 trace map *by construction* -- the math
describes the system because the system was built to instantiate the math. Such a
"bridge" is tautological and carries no evidential weight. The honest non-trivial
test is the second-order tight-binding model (`frontier/B52`), which gives `6x6`
symplectic transfer matrices, not `SL(3)`, and fails.

Typical missing object:

```text
a physical system that forces the representation and the modulation independently
```

### Figure-Eight Invariant-Surface Bridge (I = 1/4)

The hope that the figure-eight knot sits on the self-evidencing surface `I = 1/4`
is dead. The diagonal `SL(2,C)` representations (`w^3 - 2w^2 - 2w + 1`, roots
`{-1, phi^2, phi^-2}`) have Fricke-Vogt invariant `I in {4, -17/2 +/- 7 sqrt5/2}`,
none equal to `1/4`; the figure-eight geometric holonomy lives in `Q(sqrt-3)`,
disjoint from this real locus. The `c=1` Eisenstein factor's resemblance to the
figure-eight tetrahedron shape is a cyclotomic coincidence (`Phi_6` is the
simplest discriminant `-3` cyclotomic). See `frontier/B56`. The separate P12
gluing-equation discriminant echo is unaffected.

Typical missing object:

```text
a representation-theoretic reason for the invariant-surface value,
not a shared cyclotomic polynomial
```

### Aubry Self-Duality at lambda = m

The hope that the self-evidencing coupling `lambda = m` is an Aubry self-dual
(metal-insulator transition) point is dead. The duality map `lambda -> m^2/lambda`
has `lambda = m` as its trivial fixed point, so "self-dual at lambda = m" is
vacuous; the off-diagonal m-metallic model has no genuine Aubry self-duality at
`lambda = m` for `m >= 2` (IPR test: `IPR(lambda) != IPR(m^2/lambda)` off the
fixed point). For `m = 1` the known `lambda -> 1/lambda` duality is already
literature. No new metal-insulator observable. See `paths/E21`.

Typical missing object:

```text
a spectral symmetry that is not the trivial fixed point of the duality map
```

### Fixed-Line Jacobian Needs The Ambient Trace Map (SL(n), n >= 4)

The `char(M^k)` factorization (SL(3), B54/B55) is a property of the *ambient*
trace-map Jacobian at the fixed line (all traces `= n`), which is the identity
representation. There the representation-to-trace map is first-order degenerate
(`d tr(W) = 0`; traces are second-order), so picking matrix representations near
the identity and finite-differencing **cannot** recover that Jacobian -- it
captures a different (second-order / representation-Hessian) object. Computing the
fixed-line factorization for `SL(n)`, `n >= 4` therefore requires the explicit
ambient trace map: a minimal generating set of `n^2-1` trace coordinates
(Procesi) plus the substitution's action via the `SL(n)` trace identities. See
`frontier/B58`.

Typical missing object:

```text
the ambient SL(n,C) trace-coordinate map (generators + substitution action)
```

### Cotangent-Subtraction Route To The Tower Multiplicities (CLOSED, B58 Stage 1)

A natural attempt at the open `a_d` multiplicities: compute the full cotangent
spectrum (`d-sigma` on `m/m^2` of the two-traceless-matrix trace algebra at the
trivial representation) and *subtract* the `(n^2-1)` Jacobian to read off the
multiplicities. **Closed.** The cotangent is the genuine Teranishi/Đoković
minimal-generator spectrum -- dim 9 (n=3), 30 (n=4), >= 111 partial (n=5) -- far
larger than the `(n^2-1)` Jacobian (8, 15, 24). The difference (the "excess",
dim 1, 15, >= 87) is **not** a clean Dickson block and is **not** `sigma`-separable
from the Jacobian: the excess is the *secondary* invariants of the trace ring
(n=3: `det[X,Y] = tr([X,Y]^3)/3`, `sigma`-eigenvalue `-1`; n=4: the high-degree
Đoković generators). Primary-vs-secondary is **module structure** (the syzygies),
not `sigma`-weight, so no degree or factor rule peels the Jacobian primaries out.
Sharp demonstration at n=3: the Jacobian tower's `(t+1)` and the excess's `(t+1)`
occupy the *same* 2-dim `sigma`-eigenspace, so the `(n^2-1)` Jacobian is not a
`sigma`-canonical sub-object of the cotangent.

Typical missing object:

```text
the module (syzygy) structure separating primary from secondary trace invariants
-- i.e. the exterior-power Cayley-Hamilton recursion (the B58-proper hand proof)
```

This also retired two adjacent shortcuts. **Symmetric-power / principal-`SL(2)`
(Kostant) decomposition is dead from the multiplicity side too** (B58 Step 2):
`sl(n) = +_{k} Sym^{2k}` gives, for the monodromy `M`, only even powers
overshooting to `char(M^{2(n-1)})` (bare) or only odd powers (coupled with the
`H^1(F_2)=C^2` factor); neither equals the tower (both parities, capped at `M^n`).
B64's even-k/odd-k split is therefore a **sorting, not a formula**. And the
**numerical (representation-perturbation) tower is exhausted at `n >= 6`**: the
fixed-line rank-loss makes the `eps->0` pinv limit gauge-dependent (B66: 9 of 35
modes gauge-corrupted; the matrix is non-canonical), so it cannot be pushed to
higher `n`. All three routes point to the same missing object above. (This last
point is *sharpened* by B58 Phase A below: the pinv tower is not merely ceilinged
at `n >= 6` — it is *wrong* at degenerate root collisions from `n = 5`.)

### Pinv-Limit / Ambient-Jacobian Under-Counts Degenerate Multiplicities (B58 Phase A)

The representation-perturbation / "ambient Jacobian" construction (B59–B66, and the
exact B58 Phase A engine) computes the `(n^2-1)` fixed-line Jacobian as the `eps->0`
least-squares pinv limit `DT_0 = lim DX·pinv(Dx)`. **At a degenerate root collision
-- where a Dickson factor repeats, e.g. `char(M^2)^2` and `(t+1)^2` at `n = 5` -- this
limit is non-canonical and UNDER-COUNTS the multiplicity.** It is not merely
numerically ceilinged; it is *wrong*, in every field and at every precision. At `n = 5`
three independent realizations -- `F_p` random metric; `F_p` with `S = I`, prime-stable
(`= Q` mod `p`); real positive-definite `mpmath` -- all return `a_2 = 1` where the true
multiplicity is `2` (B62 structural + every `n <= 5` datum). The collision renders as a
defective **non-Dickson** cubic (`{-0.734, -0.734, 2.695}`) instead of the doubled clean
factors. Phase A's exact engine reproduces B65's `n = 4` tower EXACTLY (`a_d = (1,1,1,1)`)
-- the construction is correct on non-degenerate spectra -- and inherits the under-count
at `n = 5`; the exact-`Q` "field fix" (hypothesis: finite-field non-canonicity) was
**REFUTED** (the canonical positive-definite real pinv under-counts identically).

**Scope (important).** Only *degenerate* (repeated-factor) multiplicities are unreliable.
Non-degenerate results stand: B65's full `n = 4` tower; B66's clean singletons (e.g. the
`|k| = 3` quadratics at `n = 5` root-match cleanly). But any multiplicity the structural
candidate predicts `>= 2` is suspect from the pinv tower -- e.g. `a_3(n=6)`: candidate `2`,
B66 numerics `1` (OPEN); B66's "3rd `|k|=3` mode discarded as gauge-corrupted" is the
under-count signature.

Typical missing object:

```text
a canonical (degeneracy-aware) limit, OR the structural multiplicity directly:
the opposition-involution theta-split form (B62; frontier/B58_phaseA/CANDIDATE_A_D.md)
+ the ambient SL(n,C) trace ring to PROVE the identification (B58 proper)
```

Consequence: this **CLOSES the pinv / ambient-Jacobian route as a path to *degenerate*
`a_d`.** The sole remaining route that both computes degenerate `a_d` reliably *and*
proves it is B62-structural (the form) + the B58 trace ring (the identification and the
proof) -- which sharpens B58 from a purist open item to the only viable path to the
multiplicity formula.

### Spacetime Does Not Climb The Ranks (3+1D At SL(3), CLOSED — B101 R2)

The hope that Lorentzian signature **climbs the principal-`SL(2)` ladder** — that a 3+1-dimensional
spacetime would appear at `SL(3)` or higher where `SL(2)` gives only 2+1 — is dead by computation. The
principal `SL(2)` (the `Symᵏ` ladder) lands in **split real forms**: `Sp(k+1,ℝ)` (odd `k`), `SO(p,p±1)`
(even `k`). Split forms are **maximally balanced** — the structural *opposite* of Lorentzian (one timelike).
Lorentzian occurs at **exactly `k=2` (`SO(2,1)`)** and does not recur: `k=4→SO(3,2)`, `k=6→SO(4,3)`,
`k=8→SO(5,4)`. `Sp(4,ℝ)=Spin(3,2)` / `SO(3,2)` (k=3,4) are the real AdS₄ / 2+1-conformal groups, but their
symmetric spaces are higher-rank (dim 6), not the rank-1 spacetimes a universe needs. The phase-space-
dimension "3+1D at SL(3)" argument is therefore structurally void.

Typical missing object:

```text
a Lorentzian (rank-1, signature (p,1)) symmetric space above k=2
```

### Goldman Metric Is Riemannian, Not Lorentzian (CLOSED)

The hope that the moduli space carries an intrinsic `(1,1)` Lorentzian metric — a "phase space with a time
direction" — fails: the Goldman / Weil–Petersson symplectic-paired metric on the relevant character-variety
slice is **`(2,0)` Riemannian** (positive-definite), not `(1,1)`. The Fisher-information form computed in E21
is exactly `16/disc(char(M²)) = 16·g_WP` — a positive Weil–Petersson coefficient (V6), an elementary
chain-rule identity, with no timelike direction to provide.

Typical missing object:

```text
an indefinite (1,1) metric on the moduli space
```

### Hessian-Signature And Fisher-On-k Heuristics Are Not Spacetime (CLOSED)

Two recurring "Lorentzian emergence" heuristics are dead as physics. (i) The **volume-functional Hessian**:
computed (B96) to be **`(0,2)` negative-definite** at the complete structure (Mostow maximum) — Euclidean,
no timelike direction. (ii) The **Fisher metric on the parameter `k`/`m`**: it is the same positive
Weil–Petersson coefficient as above (a 1-D positive metric on a parameter line), not a spacetime metric.
Both are genuine mathematics (a definite Hessian; a positive Fisher form); neither carries the indefinite
signature the "emergence" reading needs. The single genuine Lorentzian object in the whole project is the
`so(2,1)` gauge algebra on the `SL(2,ℝ)` component (B97), a toy-2+1-gravity gauge structure, present by
construction — see `speculations/archive/PHYSICS_RESONANCES.md` Path 1.

Typical missing object:

```text
an indefinite signature that is not put in by hand
```

## Consolidated dead-ends register (2026-06-07)

A single-place index of the project's killed ideas (CC-web "Final Computation Arc" Task 7). Each row: a one-line
description, the **kill mechanism**, the `V`/`B`/`P` where it died, **DEAD** (permanent — a structural argument)
vs **REVIVABLE** (killed by a *computational* limitation, with a candidate exact/structural revival), and the
**structural pattern** it belongs to. The full prose for each lives in the category sections above and in
`speculations/TOMBSTONES.md`; this is the navigation table. Status `dead → anything` is forbidden (GOVERNANCE §5).

### Pattern A — numerology / value-matching (a number with no derivation; the discipline that killed Λ)
| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| A1 | `φ^φ` as the axiom | computationally falsified | CLAIMS/atlas | DEAD |
| A2 | `Λ = Λ_Planck·φ^{−2N}` (and `k≈137`) | null hypothesis (~60% of random constants match) + circular (`N` defined by the answer) | CLAIMS D1–D2 | DEAD |
| A3 | dynamic dark energy `Λ(t)`, `w≈−0.04` | ruled out ~30σ by observation | CLAIMS D3 | DEAD |
| A4 | specific masses / "14 ratios ≈ 16 masses" | numerology without an identification | S-tier T4 | DEAD/HELD |
| A5 | e-fold count `62≈60`; CMB tilt `0.965` | iteration-count ≠ e-folds; no `k`→angular-scale map | S008 | HELD |
| A6 | baryon `|Z(W1)/Z(W2)|≈10⁻⁹` | no derivation that the ratio *is* `n_B/n_γ`; no null test | S005 | HELD |

### Pattern B — wrong dictionary (a real correspondence over-read)
| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| B1 | tower eigenvalues = masses / operator dimensions | moduli-space monodromy (`±φᵏ`, single scale), not a fluctuation Hessian | B107 / V94 | DEAD |
| B2 | torsion = masses | same category error (linearized monodromy ≠ operator content) | B107 / V94 | DEAD |
| B3 | `n∈{3,4}` = the Standard Model gauge group | the map breaks at `n=2` (no clean functor) | B96 / V80 | DEAD |
| B4 | `det=−1` = CPT (a manifold invariant) | it is a trace-map/parity fact (B94), not a manifold invariant | V80 | DEAD |
| B5 | "Fibonacci anyon physics" | rescoped to an exact Fibonacci *fusion-count* dictionary only | GOVERNANCE §8 | DEAD (rescoped) |

### Pattern C — 3+1 / spacetime (type-mismatch, or a Riemannian form read as Lorentzian)
| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| C1 | the volume/Goldman Hessian is Lorentzian | computed **(0,2)/(2,0) definite**, Riemannian | B96 / V80 | DEAD |
| C2 | phase-space "3+1D at SL(3)" (dim count) | the count is arithmetic; the metric is Riemannian | B101 / V85 | DEAD |
| C3 | the spacetime tower climbs the ranks | the split-form ladder is Lorentzian **only at `k=2`** | B101 R2 / V85 | DEAD |
| C4 | Fisher-metric-on-CS-level-`k` emergence | heuristic, not rigorous | atlas | DEAD |
| C5 | 3+1D from Cartan geometry (`sl(2,ℂ)≅so(3,1)`) | the 3d→4d extraction is a structural **type-mismatch wall**, not a queued calc | S020 | **WALLED** |

### Pattern D — coincidence bridges / refuted readings
| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| D1 | figure-eight ↔ `I=1/4` invariant-surface bridge | cyclotomic coincidence | B56 / V4 | DEAD |
| D2 | Aubry self-duality at `λ=m` | vacuous (`λ=m` is the trivial fixed point of `λ→m²/λ`) | V7 | DEAD |
| D3 | entanglement = holographic | **log** entanglement = generic 1D-CFT criticality; emergent geometry AdS-like but **generic** | V37 | TESTED-NEGATIVE |
| D4 | Bell/CHSH on the classical Fricke surface | `z=f(x,y)` deterministic ⇒ CHSH ≤ 2 (classical hidden variables) | S006 / B108 | TESTED-NEGATIVE |
| D5 | "one collision causes all the walls" | three *distinct* `A₄` obstacles at `n=5` (different eigenvalues, derivations, onsets) | V91 | WITHDRAWN |

### Pattern E — the n=5 wall: **REVIVABLE kills** (killed by a computational limit, not a structural argument)
*The high-value lens.* These died because the **eps-series numerics scattered** (gauge-degeneracy) or a *shortcut*
collapsed — not because the result is false. Each has a candidate exact/structural revival. Templates: **B62**
(the eps-series numerics were dead at `n=5`, but the opposition involution `θ=−w₀` revived `char(M²)²` exactly);
the **engine-free `n=3`** (the eps-series degenerated, but the exact Lawton maps recovered it).
| # | dead end | kill mechanism | where | revival candidate |
|---|---|---|---|---|
| E1 | SL(5)+ tower via the eps-series `pinv` | rank-deficient `pinv` **under-counts degenerate multiplicities** at the `char(M²)²` collision (every field/precision) | B58 Phase A / B84 / V24 | **B62 `θ`-split (structural)** + the engine-free Lawton/Dehn-twist composition (B103/B104) |
| E2 | cotangent-subtraction route to the multiplicities `a_d` | the excess is the *secondary* invariants, not a `σ`-weight (Djoković cross-check) | B58 Stage 1 / V21 | the **exterior-power Cayley–Hamilton** hand proof (B58 proper) |
| E3 | `max(n−d,1)` multiplicity formula (SL(6) `|k|=3`) | measured `=2` but entangled with the pinv under-count | B66 / V17 | the `θ`-split candidate (`a₃(n=6)=2`) + the symbolic SL(n) trace ring |
| E4 | the `Sym^{2k}` even-only (Kostant principal) tower decomposition | the tower needs **both** parities; even-only is too small | V21 / V27 (kill #25) | the **two-sequence** (both-parity) `⊕Sym^d` product (proved `n≤4`, B103) |
| E5 | the cohomological (`H¹`) shortcut to the all-`n` tower | gives `char(M)^{n²−1} ≠` tower (trivial-rep fixed line); 3rd dead shortcut (after B84/B85) | B89-T / V73 | the explicit two-sequence `Sym` product (E4) is the live route — not a shortcut |
| E6 | the naive weight-space `θ → c` (degree=rank scalar) | `θ` is an involution (order 2); the secondary `c=i` is order 4 — unreachable | B108 / V95 | the **`ℤ/4` cusp spectrum** `{1,i,−i}` (B95) as the order-4 source |
| E7 | the `A↔D` Lie-type tower unification | refuted | B77 | — (DEAD) |

### Pattern F — specific-manifold empties (a clean negative, scope-limited)
| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| F1 | off-locus irreducible content for `4₁` at SL(3) | the 3 irreducible components (HMP) all lie **on** the forced locus | B110 / V97 | DEAD for `4₁`/SL(3); general fork **OPEN** |

### Pattern G — superseded framings & standard-theory kills (B111–B124)

The representation-program arc produced its own first-class negatives — framings that dissolved and "discoveries"
that were the ambient theory's definitions. Tombstoned in `speculations/TOMBSTONES.md`; recorded here for the map.

| # | dead end | kill mechanism | where | status |
|---|---|---|---|---|
| G1 | the "promotion" `char(M¹)→char(Mⁿ)` (two separable halves) | dissolved by the Sym-selection reframing — the tower is **one** object (the two-sequence); height-1 is a `Sym¹` absence, not a promotion | B117 / V104 | SUPERSEDED |
| G2 | `θ → c` (opposition involution predicts the degree=rank scalar) | order-2 symmetry cannot single out the order-4 secondary `c=i` | B108 / V95 | DEAD |
| G3 | `s_n → c` (the tower sign predicts the scalar) | same parity argument (`ℤ/2` can't reach `ℤ/4`) | B111 / V98 | DEAD |
| G4 | the CS-crossover `k≈4 ↔ n=4` | m-dependent (`k≈2` at m=2) — a figure-eight-volume coincidence, not structure | seven-hints A4 | DEAD |
| G5 | five quantum/knot "bridges" (unitarity `|λ|=1`, roots-of-unity tautology, Kashaev=volume conjecture, `z₀`/k=4 phase, "three regimes") | standard theory in our notation — the ambient framework's definitions, not framework-specific | Chat-2 triage | DEAD |
| G6 | `⌊n/2⌋` as the exact sign-sector excess constant | bookkeeping-dependent; the raw `±1` excess is period-4, not monotone | B124 / V113 | DEAD (exact constant OPEN) |

*Asset, not a kill (recorded so it is not re-killed):* the `det=−1` middle-eigenvalue `−1` is the **proved B121
parity** (the external monodromy `det=−1` grading), re-derived via fig-8 = golden² (B122) — anchored at `B121`/`S024`.

**Reading the register.** Patterns A–D and G are *permanent* (structural arguments, numerology controls, or
standard-theory kills) — never re-chase them. Pattern **E is the live frontier in disguise**: every E-row is a
*computational* kill with a named structural revival, and they all converge on the same destination — the **`ρ_n`
catalog proof** (now sharpened to the functorial `Sym(W)→trace-ring` construction, `knowledge/K008`). Pattern F is
scope-limited (the figure-eight at SL(3) is closed; higher rank / other manifolds remain open). See
`speculations/TOMBSTONES.md` for the physics epitaphs and `speculations/CATALOG.md` for the live items.

## Current Lesson

The obstruction is not one failed computation. It is a repeated structural
pattern. The project should continue to name missing objects explicitly rather
than rebranding them as discoveries.

Primary ledgers:

- `docs/ARCHIVE.md`
- `paths/PATHS.md`
- `frontier/`
- `PROGRESS_LOG.md`
