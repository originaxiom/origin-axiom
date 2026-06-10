# B148 — κ/Fricke–Vogt pinned, the metallic monodromy as the SL(2,ℤ) MCG action, and the class-S open question (V137)

This stage records computations that arose in a cross-session scrutiny pass on the project's "core question"
reframed against physics, **independently re-derived here** (verify-don't-trust on a handoff — every claim below was
re-proved symbolically in `probe.py`, not inherited). The honest payoff is a precise characterization of *what the
tower's symmetry is*, plus the two reading/proof tasks where the real leverage now sits.

## §0 — The firewall (state first, do not lose)

A scale-free conserved invariant — κ = tr[A,B], a pure number / element of ℂ/π²ℤ under the Chern–Simons reading —
has no β-function, no RG flow, no anomaly, and **cannot become a dimensionful energy density without an externally
supplied scale**. Every established case where a dimensionless/topological quantity touches a dimensionful observable
(θ in the QCD vacuum, the CS level, quantized Hall conductance, anomaly coefficients) sets a **quantized/dimensionless
ratio**; the **scale is always supplied independently** (Λ_QCD⁴, e²/h, ℏ/level). **Consequence:** everything in this
stage is *mathematics about the tower's symmetry* — **not** a bridge to vacuum energy or the Standard Model. The
physics aspiration is **POSTULATED** and quarantined (`MB11`); nothing promotes to `../../CLAIMS.md`. The dimensional
argument is strong but is formally *an absence*, not a cited no-go theorem; its decisive primary-source confirmation is
the OPEN reading task §4.B.

*(Context, POSTULATED: the reframed core question is the cosmological-constant problem in the sharp form "why does
exact cancellation fail by a tiny **forced** amount." κ is the candidate skeleton of that residue. The grounding pass
established that mainstream physics does **not** force a commutator-type obstruction; the closest real analogue is the
de Sitter swampland "no exact dS, quasi-dS forced" structure — itself conjectural and under live observational test.
This is firewalled motivation, not a result.)*

## §1 — κ = 4·I_FV + 2, pinned exactly (re-derived)

From generic SL(2,ℂ) matrices `A, B` with `det = 1` enforced, `(x,y,z) = (tr A, tr B, tr AB)`:

- **Fricke commutator identity (exact):** `tr(ABA⁻¹B⁻¹) = x²+y²+z²−xyz−2 =: κ`. (Difference simplifies to 0.)
- **The half-trace convention is the one that gives 4I+2.** With trace-map variables as **half** the full traces
  (`x=2X`): `κ(2X,2Y,2Z) = 4X²+4Y²+4Z²−8XYZ−2 = 4·(X²+Y²+Z²−2XYZ−1) + 2 = 4·I_FV + 2`, exactly.
- **Each invariant belongs to its own trace map (both verified invariant):** the full-trace map `F(x,y,z)=(xy−z,x,y)`
  preserves κ; the half-trace map `T(X,Y,Z)=(2XY−Z,X,Y)` preserves `I_FV`.
- **Verdict:** "κ = 4I+2 under standard conventions" is **correct**; the precise convention is *trace-map variable =
  half the full trace*. The literature uses both the `−1` form (half-trace, Fricke–Vogt) and the `−2` form (full-trace,
  commutator); they are the same object on the `F₂` character variety.

## §2 — The metallic monodromies are the SL(2,ℤ) mapping-class action (re-derived)

`R=[[1,0],[1,1]]`, `L=[[1,1],[0,1]]`.

- **`tr(RᵐLᵐ) = m²+2` exactly** (symbolic in `m`; `det = 1`). The figure-eight monodromy is `RL` (m=1), trace 3.
- **The Dehn twists `τ_a:(x,y,z)→(x,z,xz−y)` and `τ_b:(x,y,z)→(z,y,yz−x)` both preserve κ** — so this is genuinely
  the `Out⁺(F₂) ≅ SL(2,ℤ)` mapping-class-group action on the character variety ℂ³, not a lookalike.
- **κ=−2 slice = the Markov surface:** substituting `(x,y,z)=(3p,3q,3r)` into κ=−2 gives exactly `p²+q²+r²=3pqr`.
- **Precision catch (banked):** the geometric Markov root `(3,3,3)` and the Q₈ point `(0,0,0)` **both** satisfy κ=−2.
  κ=−2 is a 2-dimensional **surface** containing both the Markov tree and the Q₈ point; "the symmetric states on the
  edge" are two specific orbits on that surface, **not** the surface itself. (Do not write "(3,3,3) is the κ=−2 point.")

## §3 — Invariant data of the metallic monodromies (what a class-S comparison must reproduce)

- **All `RᵐLᵐ` are hyperbolic** (`|tr| = m²+2 > 2` for all `m ≥ 1`) — genuine Anosov/bundle monodromies.
- **Top eigenvalue = (metallic mean)²:** the larger eigenvalue of `RᵐLᵐ` equals `λ_m²`, with `λ_m=(m+√(m²+4))/2`
  (verified symbolically). Structural reason for the tower's `degree=rank`/`Mⁿ=L` shape: `RᵐLᵐ` is the square of the
  primitive metallic matrix's conjugacy class.
- **Boundary fixed slopes on ℝP¹** are the roots of `t² + m t − 1 = 0` (the Möbius fixed points
  `c t² + (d−a) t − b = 0` for `W=[[a,b],[c,d]]`). m=1: `(−1±√5)/2 ≈ {0.618, −1.618}`; m=2: `−1±√2`; m=3: `(−3±√13)/2`.
- **Eigenvalue/trace field = ℚ(√(m²+4))** (the metallic field), **reduced**: m=1→ℚ(√5), m=2→ℚ(√2), m=3→ℚ(√13),
  m=4→ℚ(√5). The discriminant `tr²−4 = m²(m²+4)` prints unreduced as 5, 32, 117, 320 — but these are `1·5, 16·2, 9·13,
  64·5`, so **m=1 and m=4 share ℚ(√5)**. Reduce the radical; do not read the unreduced discriminants as distinct fields.

## §4 — Where the real leverage now sits (OPEN; reading/proof, NOT sandbox-computable)

**A. The class-S coincidence question — the one direction with genuine mathematical traction.**
Well-posed: *does the SL(2,ℤ) trace-map / mapping-class action on the once-punctured-torus character variety coincide
with (is it conjugate to) the known S-duality / mapping-class action on the Coulomb branch of the class-S theory of the
once-punctured torus?* The §3 invariant data (hyperbolic conjugacy classes, eigenvalue `λ_m²`, fixed slopes in
ℚ(√(m²+4))) is exactly what such a comparison must reproduce.
- Read: Gaiotto–Moore–Neitzke (spectral networks / Coulomb branch, arXiv:0907.3987); Cantat–Loray (mapping-class
  dynamics on the once-punctured-torus character variety, Painlevé VI); Gaiotto class S.
- Benchmark to justify a deep effort: the metallic trace map **is** (conjugate to) a known duality/monodromy action
  with independent physical meaning. Benchmark that kills it: the gauge group is free input and the substitution adds
  no constraint (the expected outcome).
- Honest scope: even a positive result is **mathematics** (the tower's symmetry = a known duality action). It does
  **not** cross the firewall (§0).

**B. The firewall confirmation — the decisive physics-boundary check.**
Verify in primary sources that, for the once-punctured-torus bundle (figure-eight, monodromy `RL`), the complex volume
/ Cheeger–Chern–Simons invariant is a pure element of ℂ/4π²ℤ entering the 3d–3d partition function **only** as a
dimensionless exponent, with all dimensionful content carried by `ℏ↔k` and the squashing/lens-space radius.
- Read: Garoufalidis–Thurston–Zickert (Duke 2015, arXiv:1111.2828); Dimofte (arXiv:1409.0857); Córdova–Jafferis
  (arXiv:1305.2891).
- If confirmed (evidence strongly indicates yes), the firewall is decisively closed: κ-type invariants cannot source a
  physical scale, and the physical-magnitude aspiration is barred regardless of structural rhymes. That is the result
  to bank as the honest boundary of the physics aspiration.

## Reproduce

```
python -m pytest tests/test_b148_kappa_fricke_metallic.py -q     # 5 passed (pyenv; pure sympy)
python frontier/B148_kappa_fricke_metallic/probe.py              # 16 symbolic checks + the invariant-data table
```

Pure sympy — no SnapPy/Sage/cypari needed.

**Tier.** MATH. Updates `docs/OPEN_LEADS.md` (the two open tasks §4.A/§4.B + the banked §1–§3) and
`docs/STRATEGIC_SYNTHESIS.md` (the reframed core question + the dimensional firewall, both firewalled). Nothing to
`CLAIMS.md`; P1–P16, B85, the merged B124–B147 untouched. Ledger **V137**.

**Anchors:** B147/B146/B145 (the chirality arc), B141 (the Q₈ point / finiteness-density), B131 (the κ-fork), B125
(metallic arithmeticity), `K017`, `docs/STRATEGIC_SYNTHESIS.md`. External: Fricke–Klein; Goldman (trace coordinates,
arXiv:0901.1404); Kohmoto–Kadanoff–Tang / Sütő (Fibonacci trace map); Roberts–Baake (trace-map invariants);
Damanik–Gorodetski–Yessen (the Fibonacci Hamiltonian); Cantat–Loray; Gaiotto–Moore–Neitzke; Garoufalidis–Thurston–
Zickert; Dimofte; Córdova–Jafferis; Weinberg 1989 (CC no-go); Obied–Ooguri–Spodyneiko–Vafa / Ooguri–Palti–Shiu–Vafa
(de Sitter swampland).
