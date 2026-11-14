# E5 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

(a) **The minisuperspace WKB calculation reproduces the standard Vilenkin
exponent and the amplitude is non-zero.** Closed-form,
`B(Λ) = ∫₀^{a_max} √V(a) da = 1/Λ` (natural units), confirmed numerically
to ~10⁻¹⁴ over `Λ ∈ {0.1, 0.3, 1, 3, 10}`:

| Λ    | a_max = √(3/Λ) | B = 1/Λ | exp(−2B)      |
|-----:|---------------:|--------:|--------------:|
| 0.1  | 5.48           | 10.00   | 2.06 × 10⁻⁹   |
| 0.3  | 3.16           | 3.33    | 1.27 × 10⁻³   |
| 1.0  | 1.73           | 1.00    | 0.135         |
| 3.0  | 1.00           | 0.33    | 0.513         |
| 10.0 | 0.55           | 0.10    | 0.819         |

(Dimensionful conventions multiply by an O(1) prefactor — e.g. `3π/(2G)`
in some operator-ordering schemes; the `1/Λ` dependence and the
non-zero-amplitude conclusion are convention-independent.)

So condition (a) from the README — *non-zero tunneling amplitude* — is met.

(b) **Genericity (condition (b)) fails.** The result is artefactual to
several choices made before the calculation begins:

1. **Topology.** The closed `S³` FRW ansatz is one choice. An open `H³` or
   flat `R³` slicing has no classical turning point and no barrier; the
   "tunneling from nothing" picture does not exist there. The mechanism
   relies on the spatial topology being assumed.
2. **Minisuperspace truncation.** The full Wheeler–DeWitt equation has
   infinitely many degrees of freedom (every gravitational and matter mode
   on every spatial slice). Truncating to a single homogeneous `a(t)` is a
   drastic simplification. There is no theorem that the truncation's
   tunneling exponent survives in the un-truncated theory, and explicit
   counter-examples are known (mode-by-mode contributions can dominate).
3. **The cosmological constant `Λ` is an input parameter.** The probe
   sweeps it as a knob and finds `B = 1/Λ` for whatever value is chosen.
   Vilenkin's mechanism does not derive `Λ`; it consumes it. A theory of
   emergence-from-nothing that takes `Λ` as data has not produced `Λ`.
4. **Operator ordering and integration measure** are not uniquely
   determined by the formalism. Different choices give different
   O(1) prefactors in `B`, and different relative signs in the exponent —
   the latter is precisely the source of the
   Vilenkin-vs-Hartle–Hawking sign dispute (`exp(−2B)` vs `exp(+2B)`).
5. **Boundary-condition choice.** "Tunneling from nothing" is one boundary
   condition; "no-boundary" (Hartle–Hawking) is another; "DeWitt"
   (`ψ(0) = 0`) is a third. Each is well-defined; each gives a different
   amplitude. The choice is not forced by the formalism — it is the
   physical input being tested. The Feldbrugge–Lehners–Turok line argues
   even the no-boundary path integral is not well-defined as written.

(c) **Interpretation (condition (c)) fails.** Even granting the
computation, the WKB amplitude `|ψ(a)|` is a ratio of amplitudes inside a
Hilbert space whose construction assumed FRW cosmology. To call this "the
probability of a universe" requires a normalised probability measure over
universes, which requires a meta-framework that quantifies "all possible
universes" — exactly the structure "nothing" is supposed to lack. The
calculation gives an amplitude *of something inside the framework*; it
does not give a probability *of the framework*.

(d) **What "nothing" actually is in this setup.** It is `a = 0` in the
minisuperspace coordinate — a particular boundary corner of a Hilbert
space already built on a chosen topology (`S³`), a chosen truncation
(homogeneous isotropic), a chosen value of `Λ`, a chosen operator
ordering, and a chosen boundary condition. *That is not nothing.* It is a
specific, structured cosmological starting point with one coordinate set
to zero. The mechanism is "tunneling from a zero-volume FRW Hilbert
basis vector," not "creation from the absence of everything."

## What this means for the Origin Axiom program

E5 closes out the **quantum-physical** candidate ingredient with a
`STALLED` verdict — the third in Phase C's first batch. Together with E14
(`STALLED` — formal) and E11 (`STALLED` — statistical), the first batch
exhibits a **consistent pattern across three orthogonal mechanism
classes**:

- E14 (Class F, formal): well-defined *target*, no *force*.
- E11 (Class E, statistical): well-defined *force*, but only inside a
  pre-existing *target* (configuration space + measure).
- E5 (Class B, quantum-physical): well-defined *force and target*, but the
  target is a cosmological Hilbert space — the *framework* the mechanism
  was supposed to produce is the framework it presupposes.

Each probe identifies its specific smuggled input precisely:

| Probe | What it supplies | What it smuggles |
|---|---|---|
| E14 | A clean characterisation of "nothing" | The meta-framework that does the characterising |
| E11 | An exponential pull toward populated states | The configuration space and measure |
| E5  | A non-zero tunneling amplitude | FRW topology, minisuperspace truncation, Λ, ordering, boundary choice |

The Phase C kickoff hypothesis — that most paths would `STALL` at the same
wall, and that recognising the wall as universal would itself be a finding
— is supported, with `n = 3` probes from three different classes. The
wall has a consistent shape: **every candidate mechanism is well-defined
*as a function on* its inputs and does not derive its inputs.** This is
exactly the *force-vs-target* asymmetry E14's stall first named.

This does not prove every path will stall — the second batch is meant to
probe classes that might genuinely supply both — but it tightens the
prior considerably. Promising next batches are those that aim, at least
in their statement, at the *framework* rather than at a mechanism *inside*
a framework:

- **E18** (bootstrap / self-consistency, Class I) — consistency as a
  framework-level selector.
- **E15** (boundary / holographic, Class G) — the framework arises as
  data on a structure with no inside.
- **E16** (RG flow, Class H) — the framework itself runs with scale; the
  question of "what is the framework" depends on where one looks.

Two paths look most likely to inherit the stall:
- **E20** (de Sitter / positive Λ, Class K) is structurally an E5 variant
  with a different choice of vacuum sector; inherits the smuggled-Λ
  problem.
- **E9** (SSB, Class D) is textbook physics applied inside an already-given
  Hilbert space; very likely the same target-without-force pattern as E11.

A *failed* `STALLED` in the second batch — i.e. a probe that does not stall
and does derive its framework — would be the program's first
`PRODUCES-OBSERVABLE` candidate.

## Verdict

**`STALLED`**

The Vilenkin tunneling computation is correct as a minisuperspace WKB
exercise. It produces a non-zero amplitude (condition (a) met). It is not
generic across truncations, ordering, topology, or boundary-condition
choice (condition (b) fails), and the "probability of a universe"
interpretation requires a meta-measure that the framework does not supply
(condition (c) fails). The "nothing" in the setup is the `a = 0` corner of
a Hilbert space already built on FRW cosmology; the mechanism is
"tunneling from a zero-volume basis vector inside an assumed cosmological
framework," not "creation from the absence of everything."

The unconstructed step is the same one E14 named in its own terms: the
formalism (here the Wheeler–DeWitt Hilbert space and its truncation) must
be supplied externally; the mechanism then operates *inside* it. E5 is the
sharpest instance of the pattern so far because the framework it
presupposes is the one it claims to produce.
