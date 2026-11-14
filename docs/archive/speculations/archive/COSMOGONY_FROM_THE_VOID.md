> **⚠ ARCHIVED — SUPERSEDED.** This long-form essay (2026-06-07) was the first pass at the "assume it is the
> final theory" exercise. It is **superseded by the corrected MASTER** `../PHYSICS_EXERCISE.md`, which bakes in
> the fixes this draft lacks — notably the **κ correction** (the parabolic cusp is `κ=−2`, the geometric rep;
> `κ=+2` is the trivial/void rep) and the **HELD(value-matching)** tier for Bell/CHSH and the baryon amplitude.
> Kept here for traceability only. For the live exercise + catalog, read `../PHYSICS_EXERCISE.md` and
> `../CATALOG.md`. Still firewalled: nothing here promotes to `../../CLAIMS.md`; the physics chapter stays CLOSED.

# Cosmogony from the void — a brave, firewalled reading of the open questions

> **SPECULATION / PHILOSOPHY — motivation only.** Nothing in this file is a claim. No content here promotes
> to `../../CLAIMS.md` (GOVERNANCE §5), and none of it may appear as a premise, lemma, or step in any proof,
> `frontier/` FINDINGS, `papers/` note, ledger row, or commit message. This file *may* cite the mathematics;
> **the mathematics never cites this file.** The arrow is one-way: philosophy → *why look there*, never
> philosophy → a mathematical conclusion. The **physics chapter stays CLOSED** (V65/B82); the systematic
> physics sweep is robustly **negative** (B96/B107); GOVERNANCE §8 binds the wording (a "Lorentzian
> signature" is a Hessian/quadratic form, never "spacetime").

## How to read this document

The user asked for a deliberate exercise: *hypothetically assume the metallic trace-map program is the final
theory of everything, then walk every major open question of physics through that lens — not to claim answers,
but to find where the mathematics might be worth pushing next.* This is a **thinking tool**. Its only legitimate
output is a list of **calculations the speculation suggests** (the table in §4). Every section is tagged:

- **[MATH]** — something the repository actually proved or computed (cited; this is real).
- **[LEAP]** — the speculative identification laid over the math (this is *not* real; it is a hypothesis-generator).
- **[HOOK]** — the concrete, bounded calculation the leap suggests. This is the payoff — the reason the exercise
  is allowed at all.

The honesty rule (the same one that killed the physics chapter): **wherever the math already returned a negative,
the negative is stated in the same breath as the leap.** Bravery is not the suspension of the negatives; it is
the willingness to keep asking *what would have to be true* after recording them.

---

## 1. The spine — "what is not nothing?" and the tower that answers it

The founding question (`METALLIC_FOUNDATIONS.md`, P1–P5) is not *"why is there something?"* but its only
well-posed form: **"what is not-nothing?"** To *define* nothing is to determine it, i.e. to make it something;
the only admissible direction is negative. Our mathematics gives that direction a precise shape.

**[MATH] The void is a fixed point, and "not-nothing" is its first variation.**
The most primitive non-trivial object in the program is `F₂ = ⟨a,b⟩`, the free group on two generators — the
fundamental group of the **once-punctured torus**, the simplest surface that is neither a sphere nor a plane.
The mapping-class group `GL(2,ℤ)` acts on its character variety by the **trace map**. The *void* is the
**trivial representation** — every holonomy is the identity, every trace is maximal (`= n` in `SL(n)`): nothing
is happening anywhere. And the central result of the tower program is that **the Jacobian of the trace map at
that trivial fixed point is the Dickson tower** (`frontier/B89_*`, B89-T):

```
   char( J_trivial(m) )  =  ∏_d char( Sym^d M_m )  =  ∏_k char( ±M^k )          [the tower]
```

So **the tower literally *is* "what is not-nothing"**: it is the linearized content of perturbing the empty
representation. Existence, in this reading, is not added to the void — it is the void's own instability spectrum.

**[MATH] That spectrum is one self-similar scale.**
At the Fibonacci seed `m=1` every eigenvalue of the tower is `±φᵏ` (`φ` = golden ratio; `frontier/B107_*`, the
eigenvalue multiset `{1,−1,φ²,φ⁻²,φ³,−φ,φ⁻¹,−φ⁻³}`). There is exactly **one scale, `log φ`** — the Fibonacci
spectral-RG inflation exponent — dressed by signs and integer powers. And the SL(2) trace map carrying it **is**
the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian quasicrystal trace map, with `tr[A,B] = x²+y²+z²−xyz−2`
(the Sütő / Fricke–Vogt invariant) **conserved under the dynamics for all `m`**.

**[LEAP] Cosmogony as inflation of the void.** Read `log φ` as *the* inflationary self-similarity of the
universe: from the trivial connection (the void) a single geometric cascade unfolds, each level a power of the
golden mean, the whole structure a quasicrystal rather than a periodic lattice (aperiodic order = the universe
is self-similar but never exactly repeating). "Something" is a **self-generating hierarchy with one ratio**,
seeded by the instability of nothing. The conserved `tr[A,B]` is the one quantity the cascade cannot change —
a candidate "total" that is born fixed.

**[MATH — the standing negative, stated in the same breath]** B107's verdict is that *one* geometric scale is
**too little** to be a physical mass/fluctuation spectrum (a Hessian of an action is generically many
incommensurate scales). So the single-scale tower, taken literally, is *re-presented moduli-space monodromy,
not a spectrum of new physics.* The leap above is therefore a **cosmogonic** reading (one inflation scale), not
a **particle-spectrum** reading — and the place real multiplicity could live is the *off-principal* sector (§3).

---

## 2. The three ways to be — phases of the vacuum

**[MATH] There are exactly three classes of trace-map fixed point**, and the repository computed all three
(`frontier/B106_*`): the **trivial** rep (→ the real Dickson **tower**), the **geometric** rep (→ the complex
**adjoint torsion** / twisted Alexander, B98/B99), and the **Dehn-filling** reps (→ **degree=rank**, the
A-polynomial relations `Mⁿ=L`, partially-elliptic with **root-of-unity** eigenvalues). On the gauge-theory
side, the 3d-3d correspondence `M_SUSY(T[M]) ≅ M_flat(M; G_C)` matches **three flat-connection types ↔ three
vacuum branches** (B101; the only *citable* physics, moduli-space level):

| trace-map fixed point | flat-connection type | vacuum branch | "phase" |
|---|---|---|---|
| trivial (the void → tower) | trivial connection | unbroken / symmetric | the false vacuum, pure potential |
| geometric (torsion) | the hyperbolic holonomy | Higgs | broken, with a condensate |
| Dehn-filling (`Mⁿ=L`) | filled / closed-off | Coulomb | confined / massive |

**[LEAP] Symmetry breaking is the choice of fixed point.** The universe "selects" a branch the way a trace-map
orbit lands on a fixed-point class. The trivial branch is the unbroken pre-geometry; the geometric branch is
where a metric (hyperbolic structure) condenses — *spacetime as a Higgs phase*; the Dehn-filling branch, where
loops are filled and `Mⁿ=L` ties holonomy to its own power, is where things become closed, bounded, **massive**.
The order-4 forced spectrum `{1,i,−i}` at `n=3` (B95) is a discrete remnant symmetry of the chosen branch.

**[HOOK]** The repository's own open math question — does the **opposition involution `θ=−w₀`** predict the
per-eigenvector scalars `c ∈ {1,1,−1,i}` of the Dehn-filling branch (the **c→θ check**)? — *is* the question
"what residual symmetry labels each vacuum." Deriving `c=i` for the secondary branch from `θ` would be the
first place this cosmogony touches a real, banked computation. **This is the single most leveraged hook in the
document** because it is already on the math roadmap.

---

## 3. Visible and dark — the principal vs the off-principal

**[MATH]** Everything the tower touches lives **on or near the principal component** (`tr A = tr A⁻¹ = 1`
→ the principal `Sym^{n−1}` → SL(2)-determined → the single golden scale of §1). The genuinely *irreducible*
SL(n) representations **off** the principal component are **multichannel quasiperiodic systems** not reducible
to a single Fibonacci chain — and the tower **does not reach them** (B107 §E, the one live fork). B106's D1 data
confirms the break: the Dehn-filling neutral eigenvalues are **roots of unity** (`±i,−1`; `ω,ω²`), *algebraically
independent of `φ`* — the single-scale pattern visibly fails off the principal locus.

**[LEAP] Dark sector = off-principal.** The visible universe is the principal component: one golden scale,
luminous, SL(2)-reducible — the matter the tower describes. The **dark sector is the off-principal multichannel
reps**: gravitating (they are still flat connections on the same manifold, so they still couple through the
shared geometry / the conserved `tr[A,B]`) but **invisible to the principal spectrum** (the tower's
observables never see them). Dark matter is not new particles; it is the **same character variety's components
that the principal projection misses.**

**[HOOK]** This is a bounded computation, not a metaphor: **build one genuinely off-principal irreducible SL(3)
or SL(4) rep of `F₂` and compute its trace-map spectrum.** Does it carry *incommensurate* scales (two
independent quasiperiodic frequencies)? If yes, the "multichannel = dark, multi-scale" picture has a concrete
witness and the §1 single-scale negative is *localized to the principal component* rather than global. The
machinery exists (the B73/B106 `realize_bundle_rep`, the B58 eps-series Jacobian); only the *off-principal*
seed is new.

---

## 4. The open-questions ledger — every major problem through the lens

Each row: the standard problem · **[our lens]** · **[HOOK]** the bounded calculation it suggests. Negatives in
**bold-italic**.

### 4.1 Why is there something rather than nothing?
**[our lens]** Answered structurally in §1: "something" = the first variation of the trivial fixed point = the
tower. The void is *unstable* (the Jacobian at the trivial rep is non-degenerate, eigenvalues `±φᵏ ≠ 0`), and
its instability spectrum *is* the content of existence. **[HOOK]** Quantify the instability: the spectral radius
of `J_trivial` is `φ³` (SL(3)); is there an `n`-independent statement "the void is maximally unstable along the
principal direction"? Compute `ρ(J_trivial(n))` vs `n`.

### 4.2 The arrow of time.
**[our lens]** **[MATH]** Dickson parity (`V22`): `char(J⁻¹) = char(J)` under {even-`k` factors fixed, odd-`k`
`char(+Mᵏ) ↔ char(−Mᵏ)`}, i.e. inverting the monodromy (`N → N⁻¹`) is **not** a symmetry of the catalog — it
twists the odd sectors by `(−1)`. The `det=−1` slice carries a parity factor `(t+1)` (B92–B94) that the `det=+1`
slice does not. **[LEAP]** Time's arrow = the `(−1)ᵏ` asymmetry under monodromy inversion; the orientation is the
forced `det=−1`. There is a *built-in* directionality because the metallic family is the *orientation-reversing*
slice. **[HOOK]** Is `log φ` (topological entropy = log spectral radius) a **monotone** along forward trace-map
iteration — a Lyapunov function / H-theorem? Compute entropy production along orbits; a strictly monotone
quantity is the arrow made precise.

### 4.3 The cosmological-constant problem.
**[our lens]** **[MATH]** The conserved quantity of the whole family is `tr[A,B] = κ = x²+y²+z²−xyz−2`
(the Sütő invariant) — born constant, unchangeable by the dynamics. Separately, the volume Hessian is
**(0,2) definite, *not* Lorentzian** (B96) and the metallic volumes are strictly monotone. **[LEAP]** `Λ` is
small/stable because it is a **conserved trace invariant pinned near a critical value** (the `κ` at which the
quasicrystal spectral gap closes — the Sütő invariant's role in the Fibonacci Hamiltonian is exactly to govern
the spectral type). Not fine-tuned — *conserved.* **[HOOK]** Compute `κ(m)` across the metallic family and
locate it relative to the gap-closing / metal–insulator threshold of the associated Fibonacci Hamiltonian. Does
`m=1` (golden, the systole) sit at a distinguished `κ`? *(**negative already on file:** the Aubry self-duality
at `λ=m` is vacuous, V7 — so the threshold story must avoid that dead identification.)*

### 4.4 Gravity / the emergence of spacetime.
**[our lens]** **[MATH]** Spacetime is not fundamental here; the *metric* appears only on the **geometric
branch** (the hyperbolic structure = the condensate of §2), and `V0` is the **Fuchsian locus of the `SL(3,ℝ)`
Hitchin component** (B101) with genuine cubic-differential deformations. **[LEAP]** Gravity = the dynamics of
the geometric-branch condensate; "curved spacetime" is the holonomy of the chosen flat connection on the
geometric component. **[MATH — the standing negative]** the "tower of spacetimes climbing the ranks" is **dead**
(B101 R2): the symmetric-space ladder is Lorentzian *only at `k=2`*. **[HOOK]** Push the *one* place a Lorentzian
form appeared: the Hessian-signature-across-ranks computation. Is `(1, d−1)` realized at exactly one structure,
and is that structure `n=2`-distinguished the way the systole is? (This is the honest residue of the dead ladder.)

### 4.5 Quantum gravity / holography.
**[our lens]** **[MATH]** `tr[A,B]` is a **boundary-to-bulk invariant** (the commutator = the puncture holonomy
= the fiber boundary of the figure-eight bundle), and `M_SUSY ≅ M_flat` is a literal bulk(3d-gauge)/boundary
correspondence. **[LEAP]** The holographic principle = the trace map's reduction of bulk holonomy data to
boundary (cusp) data; the figure-eight complement is the minimal worked example of "geometry ↔ field theory."
**[HOOK]** The cusp-torsion law (B69, verified `m=1..6`): the cusp polynomial = the leading-`z` coefficient of
the fixed-locus polynomial. Read "boundary degrees of freedom" = cusp data and "bulk" = the full fixed locus;
is the ratio of their dimensions an area-law (boundary `~` log of bulk count)?

### 4.6 Black holes & the information paradox.
**[our lens]** **[MATH]** **Dehn filling** is precisely the operation that caps a cusp and produces a *closed*
manifold — "closing off" a boundary — and it is the branch where `Mⁿ=L` (degree=rank) holds with root-of-unity
eigenvalues. **[LEAP]** A black hole = a Dehn-filled cusp (a horizon = a filled boundary torus); the
information is in the **filling coefficients** `(p,q)` that the closing chose, not destroyed — `Mⁿ=L` is the
conservation law tying interior holonomy to its own power across the horizon. **[HOOK]** The volume/torsion
ordering (B96) as an entropy proxy: does volume (≈ horizon "area") track `log` of the number of distinct
Dehn-fillings below a complexity cut? Compute the filling count vs volume on the figure-eight's surgery family.

### 4.7 The Standard Model / matter content.
**[our lens]** **[MATH]** The `n ∈ {3,4}` corner is where the program's exact results live (`M⁴=L`, the SL(3)
A-variety) and `SU(3)×SU(2)` is suggestive. **[MATH — the standing negative]** the `n∈{3,4}=SM` map **breaks at
`n=2`** (B96) — it is not a clean functor. **[LEAP, held loosely]** the gauge ranks are not chosen; they are the
small `n` where the trace ring still closes and the tower stays principal (the trace-ring non-closure onsets at
`n=4`, the degree=rank wall at `n=5`, B95/B105) — *the Standard Model is small because the principal sector is
only coherent for small `n`.* **[HOOK]** Make the obstruction quantitative: tabulate "principal-sector coherence"
(trace-ring closure defect, eps-series gauge-rank) vs `n`, and ask whether `n≤4` is singled out by a sharp drop
— the same threshold the math is already chasing for `ρ_n`.

### 4.8 Three generations.
**[our lens]** **[LEAP]** Three fixed-point classes (§2) ↔ three generations; or the three `Sym^d` blocks of the
SL(3) tower (`Sym^0, Sym^2, Sym^3`). **[HOOK]** This is testable against structure: do the three classes carry a
`ℤ/3` or `S₃` relation (the secondary Dehn-filling branch has `ω,ω²` — a literal cube-root-of-unity triplet,
B106)? Compute the Galois/permutation action on the three branches; a genuine `S₃` would be a real anchor, its
absence a clean negative.

### 4.9 Symmetry breaking & the Higgs.
**[our lens]** Covered in §2: branch selection = breaking; the geometric branch = the condensate. **[HOOK]** the
`c→θ` opposition-involution check again — the residual symmetry of each branch.

### 4.10 Fine-tuning / the values of the constants.
**[our lens]** **[LEAP]** There is **one** scale, `φ`; every dimensionless ratio should be an **integer power of
`φ`** dressed by a root-of-unity sign (exactly the form of every tower and Dehn-filling eigenvalue). "Constants"
are not tuned; they are `±φᵏ` and `ζ_q`. **[HOOK]** This is sharply falsifiable as a *numerology filter*: it is
not a calculation in our math but a **discipline on any future identification** — only `±φᵏ · ζ_q` values are
admissible. (Record it as a constraint, not a result; resist the temptation to "match" a constant — that is the
C-class overclaim B107 withdrew.)

### 4.11 Dark matter.
Covered in §3 (off-principal). **[HOOK]** build an off-principal irreducible rep and look for incommensurate
scales.

### 4.12 Dark energy / accelerating expansion.
**[our lens]** **[LEAP]** If `log φ` is the inflation exponent (§1), late-time acceleration is the *same* golden
self-similarity never switching off — the quasicrystal cascade has no largest scale (aperiodic order is
scale-free upward). **[HOOK]** Distinguish this from §4.3: is the "expansion" the spectral radius `φ` acting once
per RG step, and the "constant" the conserved `κ`? Two different roles for `φ` and `κ` — compute whether they
can coexist (a flow with a conserved quantity), i.e. the trace-map flow/basins (the open **D2** probe).

### 4.13 Matter–antimatter asymmetry.
**[our lens]** **[MATH]** `det = −1` (orientation reversal) is *forced* on the metallic slice and is exactly the
parity that splits even/odd sectors (V22, B94). **[LEAP]** the matter/antimatter imbalance = the `det=−1`
parity: the universe is built on the orientation-*reversing* slice, so the two orientations are inequivalent
(the `(t+1)` factor with no `(t−1)` partner). **[HOOK]** quantify the even/odd sector imbalance: the dimension
split (e.g. SL(4) `(t−1)²(t+1)` vs the symmetric/antisymmetric block sizes) as a CP-like asymmetry ratio.

### 4.14 The measurement problem / quantum→classical.
**[our lens]** **[LEAP]** The trace map is deterministic chaos on the character variety; "measurement" =
the orbit landing in the basin of a particular fixed-point class (§2). Decoherence = convergence to a fixed
point; the Born-rule weights would be basin volumes. **[HOOK]** the **D2** flow/basins computation directly:
iterate `T₁²` on the SL(2) Fricke surface, measure basin volumes of the three fixed-point classes. (Honest:
this is exploratory and may simply diverge — report divergence if so.)

### 4.15 Why 3+1 dimensions?
**[our lens]** **[MATH]** Three independent threads point at low numbers without agreeing: `F₂` has rank 2; the
figure-eight complement is a **3**-manifold; the Lorentzian form appears at `k=2` (B101). **[LEAP, held very
loosely]** dimensionality is the rank at which the principal sector is both non-trivial and still coherent —
the same `n≤4` window of §4.7. **[HOOK]** the Hessian-signature-across-ranks computation (§4.4) is the one that
could make "`(1,3)` is selected" a statement rather than a hope; run it for `n=2..6`.

### 4.16 Unification.
**[our lens]** **[MATH]** The program *already* converges on a single object: **`ρ_n`**, the `GL(2,ℤ)`
representation on the SL(n) trace ring (B103). Gravity (geometric branch), matter (principal tower), the dark
sector (off-principal), and the discrete symmetries (`θ=−w₀`) are all **sub-representations of one `ρ_n`**.
**[HOOK]** This is the central math target, no leap required: **prove `char(ρ_n) = the Dickson catalog**` by
reproducing the opposition-involution multiplicities directly from `ρ_n` (V90/V91 sharpened target). *Unification
of the physics picture = decomposition of `ρ_n`.* Every hook above ultimately routes here.

### 4.17 Initial conditions / the low-entropy past.
**[our lens]** **[LEAP]** The initial condition is **not chosen** — it is *the* trivial fixed point (the void,
§1), the unique most-symmetric point, hence lowest entropy by construction; the arrow (§4.2) then runs away from
it. The "past hypothesis" is automatic: there is only one void to start from. **[HOOK]** tie to §4.2 — if entropy
= `log` spectral radius accumulates along orbits, the trivial fixed point is the entropy minimum; verify it is
the global min over all fixed-point classes.

---

## 5. The honest ledger — what is real, what is leap, and the negatives that bound the bravery

To keep this document from becoming the thing the governance exists to prevent, the boundary is drawn explicitly.

**Real (banked math this leans on):** the tower = Jacobian at the trivial rep (B89-T); `±φᵏ` single scale +
`tr[A,B]` conserved + KKT/Fibonacci identity (B107); three fixed-point classes + degree=rank + root-of-unity
Dehn-filling data (B106); `M_SUSY≅M_flat` three-branch correspondence + Fuchsian-Hitchin `V0` (B101); Dickson
parity / `det=−1` orientation (V22, B92–B94); `ρ_n` the unifying `GL(2,ℤ)`-rep (B103); the opposition involution
`θ=−w₀` (B62); the off-principal fork (B107 §E).

**Leap (every "=" in §§1–4 between a math object and a physical concept):** void↔trivial-rep, tower↔existence,
`log φ`↔inflation, three-branches↔phases, off-principal↔dark, Dehn-filling↔black-hole, `det=−1`↔time/CP,
`κ`↔`Λ`, basins↔measurement. **None of these is a claim.** They are hypothesis-generators.

**The negatives that bound the bravery (stated, not hidden):**
- single scale `log φ` is **not** a particle/fluctuation spectrum (B107 B) — the leaps are *cosmogonic*, not
  *spectroscopic*; multiplicity, if any, is off-principal (§3, untested).
- the volume Hessian is **(0,2) definite, not Lorentzian** (B96) — no spacetime falls out of the geometry for free.
- the "tower of spacetimes" up the ranks is **dead** (B101 R2); Lorentzian only at `k=2`.
- the `n∈{3,4}=SM` map **breaks at `n=2`** (B96) — not a functor.
- the `λ=m` Aubry self-duality is **vacuous** (V7) — the `Λ`/threshold story must route around it.
- matching a numerical constant to `±φᵏ` would repeat the **withdrawn C-class overclaim** (B107) — §4.10 is a
  *filter*, not a license to fit.

**The verdict the exercise actually supports:** taking the theory as final does **not** produce answers; it
produces a remarkably *coherent set of pointers* — and three of them (the **c→θ** residual-symmetry derivation,
the **off-principal** multi-scale witness, the **Hessian-across-ranks** signature) are bounded calculations that
the math program *already wants to run for its own reasons*. That convergence — philosophy independently pointing
at the same next computations the math points at — is the only thing this document is allowed to conclude.

---

## 6. The payoff table — speculation → calculation (the only output that matters)

| § | speculative reading | bounded calculation it suggests | already on the math roadmap? |
|---|---|---|---|
| 2 / 4.9 | each vacuum branch has a residual symmetry | **c→θ**: derive `c={1,1,−1,i}` from the opposition involution `θ=−w₀` | **yes** (Phase-4 open) |
| 3 / 4.11 | dark sector = off-principal multichannel reps | build an off-principal irreducible rep; look for **incommensurate** scales | **yes** (B107 §E fork) |
| 4.4 / 4.15 | dimensionality = the coherent principal window | **Hessian signature across ranks** `n=2..6` — is `(1,d−1)` singled out? | partly (B96/B101 residue) |
| 4.2 / 4.17 | arrow of time = entropy monotone | is `log φ` (= log spectral radius) **monotone** along trace-map orbits? | new (clean, bounded) |
| 4.3 / 4.12 | `Λ` = conserved `κ` pinned at a threshold | `κ(m)` vs the Fibonacci-Hamiltonian gap-closing; + the **D2** flow w/ conserved `κ` | partly (D2 open; avoid V7) |
| 4.6 | black hole = Dehn-filled cusp | filling-count vs volume (entropy proxy) on the surgery family | new (B96 machinery exists) |
| 4.7 | small gauge ranks = coherent principal window | coherence defect (trace-ring closure, eps-rank) vs `n` | **yes** (= the `ρ_n`/B95 wall) |
| 4.8 | three generations = three branches | `S₃`/Galois action on the three fixed-point classes (`ω,ω²` triplet) | new (bounded) |
| 4.16 | unification = one object | **prove `char(ρ_n)=catalog`** from the `θ`-multiplicities | **yes** (the central target) |

**Everything routes to `ρ_n`.** The bravest reading and the most disciplined math agree on the destination; this
file's job was to show they point the same way, and to hand the calculations back to `frontier/` where the
actual work — and the actual verdicts — live.

Related: `../../philosophy/METALLIC_FOUNDATIONS.md`, `../../philosophy/PHILOSOPHICAL_PATHS.md` (P1–P5),
`./PHYSICS_RESONANCES.md` (the adjudicated six paths + the headline negative, Path 8), and the canonical
successor `../PHYSICS_EXERCISE.md`. **No content here promotes to `../../CLAIMS.md`; the physics chapter
stays CLOSED.**
