# B105 — the n=5 wall (characterized), the unified-wall root cause, literature, and the ρ_n convergence

**Status: the N5 result is a `characterized-wall` (decisive negative); H1–H6/C1–C4 are tabulated by their
own proof status; the convergence is the synthesis.** Executes the CC-web "n=5 Resolution + Literature +
Final Observations" handoff. Pure trace-map / Lie theory; **no physics** (all physical readings POSTULATED +
quarantined); P1–P16 untouched. Script `probe.py`; test `tests/test_b105_n5_wall_and_convergence.py`.

## N5 — the decisive computation: coordinate artifact, not structural change
**Question (handoff):** is the n≥5 tower degeneracy a *coordinate artifact* (the eps-series fails to resolve
a structure that exists) or a *structural change* (the tower formula genuinely differs at n=5)?

**Verdict: COORDINATE ARTIFACT.** At SL(5) the Dehn-twist eps-series (B104) resolves **21 of 24** Dickson
factors. Three findings pin the verdict:
1. **The resolved 21 are universally catalog-consistent.** For every monodromy tested (metallic + genuine
   non-metallic, both det signs), `gcd(char(J), two-sequence catalog)` has degree **21** — the resolved part
   is always exactly the catalog minus one `Sym²`.
2. **The corrupted 3-dim factor is GAUGE NOISE.** Across seeds it takes **distinct values** (the metric/gauge
   choice), while the resolved 21 are invariant. *A structural change would give a fixed wrong answer; gauge
   noise is the signature of a coordinate artifact.*
3. **The eps-series ceiling is 21/24** (over 20 seeds), consistent with B61's 22 (inverse-word + SVD). The
   doubly-degenerate `−1²` sector **cannot be pinned** by the eps-series.

Three independent structural routes — **B89-T** (two-sequence), **B62** (θ-split / opposition involution),
**B103** (the `GL(2,ℤ)`-rep `ρ_n`) — agree the unresolved 3-dim piece is `Sym²` (completing `μ_2=2`).

**Conclusion (honest, per the handoff's strict bar).** The n=5 catalog is **strongly supported** (21/24 +
three structural routes) and the alternative "the formula changes at n=5" is **ruled out** (the corruption is
gauge noise, not a fixed wrong answer). But the strict "all 3 factors resolved" bar is **NOT met**: the
remaining obstruction is the **eps-series gauge-degeneracy at the cusp's repeated `−1` eigenvalue** — a
*computational* wall, not a structural one. The n=5 catalog remains formally `open`; the obstruction is now
pinned to a single, characterized degeneracy.

## H6 — the unified n≥5 wall (structural)
The forced cusp spectrum (`tr A = tr A⁻¹ = 1`, B95) is `{1,i,−i}` (n=3), `{1,1,ω,ω²}` (n=4),
`{1,1,1,−1,−1}` (n=5). The **non-trivial eigenvalues are distinct at n=3,4 but COLLIDE at n=5** (`−1` with
multiplicity 2); at **n≥6 no finite-order spectrum exists at all** (B95). This single collision is the
**common root cause** of three walls that looked independent:
- the **tower wall** — 3 corrupted Dickson factors (B84/B104, this N5 result);
- the **degree=rank wall** — `A²=I` ⟹ involution ⟹ dihedral ⟹ reducible (B95);
- the **eps-series rank-drop** — the doubly-degenerate sector that cannot be inverted.

So the project has a **natural boundary at n=4**, *proved structural*: the algebra that makes both flagship
theorems work — distinct root-of-unity cusp eigenvalues — exists only at `n∈{3,4}`.

## The convergence (the project's thesis)
Every positive result is a property of **one object: `ρ_n`, the `GL(2,ℤ)`-representation on the SL(n) trace
ring at the trivial point.** The tower **is** `char(ρ_n)`; the module-iso **is** its decomposition into
`Sym^d` pieces (B103); universality **is** the well-definedness of `ρ_n` (B103); the parity **is** its
`det`-sign twist; the Hitchin identification (B101) places `ρ_n` in a known moduli space. `ρ_n` is
**completely characterized for n=3,4** (exact, constructive, universal) and its **natural boundary at n=4 is
proved** (eigenvalue collision at n=5, impossibility at n≥6). One object, fully characterized in its natural
range, with its boundary proved.

## Literature (cited observations)
- **L1 — Gang–Koh–Lee–Park, arXiv:1305.0937** ("Superconformal Index and 3d-3d Correspondence for Mapping
  Cylinder/Torus"): assigns 3d theories to once-punctured-torus bundles via **duality domain-wall theories
  in 4d N=2\***; **SL(2,ℂ)** Chern–Simons only. *No higher-rank (SL(3)) construction, no Dehn-filling, no
  systematic `SL(2,ℤ)`-monodromy family* in the paper. ⟹ our SL(3) Dehn-filling data (B71) and the metallic
  sub-family are **new within the framework of [GKLP]** (cited, not claimed).
- **L4 — Fock–Goncharov / Hitchin for the once-punctured torus** (Bonahon–Dreyer arXiv:1209.3526;
  Douglas–Sun arXiv:2011.01768): FG coordinates for SL(3) on punctured surfaces via an ideal triangulation;
  the Hitchin component = positive framed local systems (shearing + FG positivity). The once-punctured torus
  is the standard guiding example. *Consistent with* B101 (V0 = the Fuchsian locus of the FG-positive /
  Hitchin component) and B102 (W1/W2 are excluded from the positive component — by ellipticity).

## H1–H5 (computed; tabulated by status, computed in the cited stages)
- **H1** (`COMPUTED`, B96/physics_probes): `S(N)=log|⟨N⟩| ~ vol·N/(2π)` for the figure-eight Kashaev
  invariant = the **volume conjecture** (Kashaev 1997; Murakami–Murakami 2001); `G_eff=π/(2vol)=0.774` if
  `S=A/4G` — POSTULATED reading, quarantined.
- **H2** (`PROVED`, B71/B89): `Mⁿ=L` reduces `2(n−1)` boundary DoF to `(n−1)` — **compression ratio 1/2**,
  constant across n=3,4.
- **H3** (`COMPUTED`, B96): `vol(m=1)=2.030 < vol(m=2)=3.664 < vol(m=3)=4.814` strictly monotone; `m=1`
  simplest by systole (B92) and volume.
- **H4** (`COMPUTED`, B98/B99): two trace-map fixed points, two invariants — trivial→Dickson tower,
  geometric→adjoint torsion.
- **H5** (`COMPUTED`, B101): gauge-algebra Killing signatures `sl(2,ℝ)=(2,1)`, `sl(3,ℝ)=(5,3)`,
  `sl(4,ℝ)≅so(3,3)⊃so(3,1)`; Lorentzian only at the `k=2` rung of the split-form ladder.

## C1–C4 (corrections recorded)
**C1** Goldman metric is `(2,0)` Riemannian, not `(1,1)` Lorentzian (Goldman 1984; FAILURE_ATLAS/B101).
**C2** phase-space 3+1D at SL(3) killed by the split-form ladder (B101). **C3** the Cayley–Hamilton
mechanism for degree=rank is refuted (V75 hinge test). **C4** the SL(5) principal spectrum is
`{1,1,1,−1,−1}` (tr=1), not the earlier `{1,1,1,ω,ω²}` (tr=2) — corrected in B95.

```bash
python frontier/B105_n5_wall_and_convergence/probe.py
python -m pytest tests/test_b105_n5_wall_and_convergence.py -q
```
No physics claim; no `CLAIMS.md` promotion; proven core P1–P16 untouched; physics chapter stays CLOSED.
