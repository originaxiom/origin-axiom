# PATHS — emergence-path registry

The 25 enumerated candidate paths by which "nothing being unstable" could produce
reality (E1–E20, P1–P5); `E21+` are concrete instantiations of an already-listed
mechanism, added as they are probed. Status updated after every probe. See
`MECHANISM_CLASSES.md` for class structure and `README.md` for ground rules.

**Verdict legend:** `PRODUCES-OBSERVABLE` · `STALLED` · `DEAD` · `NEEDS-EXPERTISE` ·
`UNTOUCHED` (no probe yet) · `IN-PROGRESS` (probe partially complete).

## Registry

| ID | Class | Path | Status | Probe / cross-link |
|---|---|---|---|---|
| **E1** | A | Self-reference iteration `x → 1+1/x`; φ as universal attractor | IN-PROGRESS (narrow) | `../frontier/B1`, `../frontier/B4` |
| **E2** | A | Continued-fraction / Gauss map dynamics on the modular surface | IN-PROGRESS (narrow) | `../frontier/B2`, `../frontier/B4` |
| **E3** | B | Vacuum-mode cancellation failure (frustrated cancellation) | DEAD (narrow forms) | `../docs/ARCHIVE.md` D1–D7 |
| **E4** | B | Heisenberg uncertainty / vacuum fluctuations as ontological floor | UNTOUCHED | — |
| **E5** | B | Spontaneous nucleation / Vilenkin tunneling from nothing | **STALLED** | `E5_vilenkin_tunneling/` |
| **E6** | C | Non-trivial fundamental group / homology forbids the void | IN-PROGRESS (narrow) | P6, P8–P10 in `../CLAIMS.md`; `../frontier/B3` |
| **E7** | C | Causal sets (Sorkin) — discrete pre-geometry, minimum causal content | UNTOUCHED | — |
| **E8** | C | Univalent / higher-homotopy generation from the empty type | UNTOUCHED | — |
| **E9** | D | Spontaneous symmetry breaking — symmetric vacuum unstable | UNTOUCHED | — |
| **E10** | D | Action principle — only nontrivial extrema; trivial vacuum is not one | UNTOUCHED | — |
| **E11** | E | Entropic emergence — "nothing" is one microstate, "something" many | **STALLED** | `E11_entropic_emergence/` |
| **E12** | E | Information-theoretic / it-from-bit — distinction itself is information | UNTOUCHED | — |
| **E13** | E | Measure-theoretic — no well-defined measure on nothing; any measure has support | UNTOUCHED | — |
| **E14** | F | Initial-object / empty-type — what does "nothing" mean as a mathematical object? | **STALLED** | `E14_categorical_initial_object/` |
| **E15** | G | Bulk-from-boundary; "outside of nothing" carries structure | UNTOUCHED | — |
| **E16** | H | RG flow — empty at one scale, structured at another | UNTOUCHED | — |
| **E17** | H | Extended objects (strings) — point-particle vacuum dissolves to string vacuum | UNTOUCHED | — |
| **E18** | I | Self-consistency / bootstrap — only consistent "somethings" exist | UNTOUCHED | — |
| **E19** | J | Diophantine non-existence — no zero solution; smallest nonzero is reality | UNTOUCHED | — |
| **E20** | K | De Sitter / positive-Λ — empty space is locally de Sitter, self-driving | UNTOUCHED | — |
| **E21** | I | Self-evidencing closure — `λ=m` self-consistency of the metallic trace map (instantiates E18) | **STALLED** | `E21_self_evidencing_closure/` |
| **P1** | L | Negation-as-creation (linguistic) | UNTOUCHED | `../philosophy/PHILOSOPHICAL_PATHS.md` |
| **P2** | L | Gödelian / undecidability | UNTOUCHED | `../philosophy/PHILOSOPHICAL_PATHS.md` |
| **P3** | L | Anthropic / observer-required | UNTOUCHED | `../philosophy/PHILOSOPHICAL_PATHS.md` |
| **P4** | L | Process (Whitehead) — non-occurrence is itself occurrence | UNTOUCHED | `../philosophy/PHILOSOPHICAL_PATHS.md` |
| **P5** | L | Apophatic / theological — the unnamable precedes naming | UNTOUCHED | `../philosophy/PHILOSOPHICAL_PATHS.md` |

## Per-path stubs

Each path's stub: *what the mechanism proposes · what would distinguish it · what
remains to do.* Once a path has a probe directory, the stub here is the summary;
the directory's `README.md` carries the full setup.

### Class A — Fixed-point / attractor

**E1 — Self-reference iteration → φ attractor.** *Mechanism:* the simplest
self-referential update `x_{n+1} = 1 + 1/x_n` converges to `φ` from any positive
start; "nothing reflecting on itself" is unstable, the iteration is forced, and `φ`
is the unique attractor. *Distinguisher:* the iteration's structure should map to
something physical (a relaxation rate, a coupling). *Status:* the φ-attractor and
its sl(2,ℝ) closed form are exact (P11) and the iteration is real, but no
operational connection to a physical observable has been constructed. Probed
partially by `frontier/B1` and `frontier/B4`.

**E2 — Continued-fraction / Gauss map dynamics.** *Mechanism:* `φ` is the noble
fixed point of the Gauss map `x → {1/x}`; the modular surface's ergodic theory
selects continued-fraction orbits, with the figure-eight orbit shortest.
*Distinguisher:* would need a physical reason the Gauss-map dynamics governs an
observable. *Status:* probed by `frontier/B2` and `frontier/B4`; the figure-eight
orbit is exactly the shortest primitive (B4), but its 37.8% Gutzwiller share is
modest, not dominant. The "leading is not selected" lesson came from here.

### Class B — Quantum zero-point

**E3 — Vacuum-mode cancellation failure.** *Mechanism:* QFT vacuum modes do not
sum to zero; the residual *is* existence. *Distinguisher:* a specific calculation
yielding the residual's magnitude. *Status:* narrow forms `DEAD` — every concrete
attempt (k≈137, `Λ = φ^{−2N}`, dynamic dark energy, Casimir-energy-depends-on-φ,
phonon stability) failed. See `docs/ARCHIVE.md` D1–D7. The *broader* idea — that
the cancellation must fail for some structural reason yet unidentified — is
unprobed but inherits the dead narrow forms' lessons.

**E4 — Heisenberg uncertainty / vacuum fluctuations.** *Mechanism:* `ΔxΔp ≥ ℏ/2`
forbids a state of pure rest; vacuum fluctuations are an ontological floor.
*Distinguisher:* the floor's structure (zero-point spectrum, vacuum
correlations) must match observation in a non-trivial way that doesn't reduce to
standard QFT vacuum energy. *Status:* untouched. The risk: it is *too close* to
E3's dead forms; if it just restates them, it inherits their fate.

**E5 — Vilenkin / Hartle–Hawking tunneling.** *Mechanism:* the universe is the
result of quantum tunneling from a "nothing" state (no spacetime, no matter) into
a de Sitter–like state. There is a mainstream literature: Vilenkin 1982,
Hartle–Hawking 1983, "no-boundary proposal." *Distinguisher:* whether the
tunneling-from-nothing wavefunction (a) gives a non-zero amplitude, (b) is generic
or fine-tuned, (c) actually has a defensible interpretation. *Verdict
(2026-05-27):* **`STALLED`.** The minisuperspace WKB calculation reproduces the
standard Vilenkin exponent `B(Λ) = 1/Λ` exactly (cross-checked numerically to
~10⁻¹⁴) and the amplitude `exp(−2B)` is non-zero — (a) met. But (b) fails:
the result is artefactual to the FRW topology choice, the minisuperspace
truncation, the operator-ordering and measure, and the boundary-condition choice
(Vilenkin vs Hartle–Hawking vs DeWitt all give different answers; `Λ` is an
input, not derived). And (c) fails: "probability of a universe" requires a
meta-measure the framework does not supply. The "nothing" in the setup is
`a = 0` in a Hilbert space already built on FRW cosmology — the framework the
mechanism claims to produce is the framework it presupposes. See
`E5_vilenkin_tunneling/FINDINGS.md`.

### Class C — Topological / geometric obstruction

**E6 — Non-trivial fundamental group / homology.** *Mechanism:* a topology with
non-trivial π₁ or H₁ cannot be continuously deformed to a point; the topology is
itself the obstruction to nothingness. *Distinguisher:* a physical reason the
specific topology of reality has the non-trivial structure we assert. *Status:*
the figure-eight characterization (P1–P13) is one instantiation but does not
*derive* that the universe has this topology. Probed partially by Phase A and
`frontier/B3`.

**E7 — Causal sets (Sorkin).** *Mechanism:* Sorkin's causal set program treats
spacetime as a discrete pre-geometric partial order; the void is not a causal set;
the minimum non-empty causal set has structure. *Distinguisher:* a derivation
that the continuum limit produces our spacetime, or a prediction that distinguishes
causal sets from other discrete approaches. *Status:* untouched.

**E8 — Univalent / higher-homotopy from the empty type.** *Mechanism:* in
homotopy type theory the empty type `0` has only the identity morphism (and
identities of identities, ...); higher-homotopy iterates from `0` itself.
*Distinguisher:* whether this iteration generates non-trivial structure or
collapses. *Status:* untouched. Adjacent to E14.

### Class D — Symmetry / variational

**E9 — Spontaneous symmetry breaking.** *Mechanism:* the symmetric vacuum
(Mexican-hat-style) is unstable to perturbation; the system spontaneously selects
a direction. *Distinguisher:* the selected direction's structure should match
observation in a way not already accounted for by standard SSB. *Status:*
untouched. Risk: textbook physics is already this; the question is what's *new* about applying it to "nothing-vs-something."

**E10 — Action principle.** *Mechanism:* physics is governed by stationary
action; the trivial (zero-everywhere) configuration is not a non-degenerate
extremum; non-trivial configurations are forced. *Distinguisher:* would need a
specific action whose only non-trivial extrema are physical. *Status:* untouched.

### Class E — Statistical / informational

**E11 — Entropic emergence.** *Mechanism:* "nothing" is exactly one microstate
(everything empty); "near-nothing" is exponentially many; the second law forces
departure from the empty state. *Distinguisher:* whether counting alone suffices,
or whether you need additional dynamics to populate microstates. *Verdict
(2026-05-27):* **`STALLED`.** The combinatorics are exact — `P(empty) = 2⁻ⁿ`,
peak multiplicity `∼ 2ⁿ/√n`, entropic pull linear in `n` — but counting only
selects *within* a configuration space and measure that must be supplied
externally. Counting is a selection mechanism, not a generation mechanism; the
empty measure space (no σ-algebra, no measure) does not even support the
inequality `1 ≪ 2ⁿ`. Same shape as E14's stall — formalism without force, force
without target. See `E11_entropic_emergence/FINDINGS.md`.

**E12 — Information-theoretic / it-from-bit.** *Mechanism:* the most primitive
thing is a distinction (Wheeler's "it from bit"); the absence of distinction is
itself information about absence; "nothing" carries information.
*Distinguisher:* whether information-theoretic arguments produce predictions
beyond Shannon-style content. *Status:* untouched.

**E13 — Measure-theoretic.** *Mechanism:* a probability measure with support
only on the empty configuration is degenerate; any well-defined measure has
non-trivial support; the support *is* the something. *Distinguisher:* whether the
forced support has structure matching reality. *Status:* untouched.

### Class F — Categorical / formal

**E14 — Initial-object / empty-type.** *Mechanism:* what does "nothing" mean
formally? In category theory it is the initial object; in type theory the empty
type. The mechanism asks whether *the formal object itself* has structural
properties that force emergence. *Distinguisher:* whether "nothing" admits a
sharp formal definition; if it does, what it forces. *Verdict (2026-05-23):*
**`STALLED`.** All four standard frameworks (set theory, category theory, type
theory, HoTT) give clean, unique formal characterizations of "nothing" — and
*precisely none of them, by itself, forces emergence.* Each is defined by
having minimal structure. The mathematizable conclusion is the philosophical
P1 made formal: the formalism supplies the *target* but not the *force*; every
other E* probe must supply the dynamical ingredient explicitly. See
`E14_categorical_initial_object/FINDINGS.md`.

### Class G — Boundary / holographic

**E15 — Bulk-from-boundary.** *Mechanism:* if reality is holographic, the bulk
emerges from the boundary; "outside of nothing" is at minimum a boundary
condition, which is itself structure. *Distinguisher:* the boundary's structure
must determine the bulk's; the holographic dictionary must apply.
*Status:* untouched.

### Class H — Renormalization / scale

**E16 — RG flow.** *Mechanism:* the answer to "is there something?" depends on
scale. At one RG point you see nothing; at another, full structure. *Distinguisher:* an RG flow whose UV is empty and IR is occupied (or vice
versa) in a non-trivial, physical way. *Status:* untouched.

**E17 — Extended objects (strings).** *Mechanism:* point-particle vacuum is
empty, but for extended objects (strings, branes) the vacuum is necessarily
populated by ground-state oscillations. *Distinguisher:* the string-vacuum
content's match to observation. *Status:* untouched.

### Class I — Bootstrap / consistency

**E18 — Self-consistency / bootstrap.** *Mechanism:* only some "somethings" are
self-consistent; "nothing" is not; consistency is the selector that picks reality.
*Distinguisher:* a precise consistency condition that rules out "nothing" and
rules in a specific something. *Status:* untouched. Related to the S-matrix /
conformal bootstrap programs in mainstream physics. Instantiated by **E21**.

**E21 — Self-evidencing closure (instantiates E18).** *Mechanism:* the metallic
trace-map coupling `λ=m` is the unique value where the linearized half-return
reproduces `char(M)` of the substitution's own generator — read as
selection-by-self-consistency. *Distinguisher:* a framework where the discrepancy
`D(I)=(4I−m²)²` is a *bona fide* free energy (not a relabeled residual), plus an
observable the coupling controls. *Verdict (2026-06-01):* **`STALLED`.** The exact
fact is the single identity `4c²−2=m²+2`; the variational-free-energy reading is a
structural analogy, not a derivation, and predicts no observable. The exact
algebra is kept as standalone trace-map math (`../frontier/B51`, `../frontier/B54`,
PC12); the framing is quarantined here. See `E21_self_evidencing_closure/`.

### Class J — Number-theoretic

**E19 — Diophantine non-existence.** *Mechanism:* certain equations have no
zero solution (e.g., `x² + y² = −1` over ℝ); the smallest non-zero solution is
forced; reality is the minimal non-trivial solution of *some* fundamental
equation. *Distinguisher:* identifying the equation. *Status:* untouched.
Adjacent to the figure-eight's number-theoretic factorization observations
(disc 5 × disc −3) but those are about the *answer*, not the *mechanism*.

### Class K — Cosmological

**E20 — De Sitter / positive Λ.** *Mechanism:* a positive cosmological constant
makes empty Minkowski space unstable to de Sitter expansion; "empty" is not a
fixed point of Einstein's equations. *Distinguisher:* a derivation of why Λ > 0
rather than zero, from inside the framework rather than from observation.
*Status:* untouched. Most prone to inheriting D1–D3's dead forms.
