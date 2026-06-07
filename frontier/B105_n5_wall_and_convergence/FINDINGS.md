# B105 — the n=5 wall (characterized), the unified-wall root cause, literature, and the ρ_n convergence

**Status: the resolved-21 computation + the `ρ_n` thesis stand; two prior inferences are DOWNGRADED (V90
audit — Corrections A & B, banked explicitly below).** Executes the CC-web "n=5 Resolution + Literature +
Final Observations" handoff. Pure trace-map / Lie theory; **no physics** (all physical readings POSTULATED +
quarantined); P1–P16 untouched. Script `probe.py`; test `tests/test_b105_n5_wall_and_convergence.py`.

## ⚠ Corrections (V90 audit — explicit downgrades of two B105 inferences)
- **Correction A.** The inference *"the 3 unresolved factors vary across seeds ⟹ gauge noise ⟹ coordinate
  artifact, NOT a structural change"* is **INVALID** and is withdrawn. A rank-deficient `DX·pinv(dx)` (B84:
  `dx` is rank-deficient at that sector) returns approach/seed-dependent values there **regardless of the
  true factorization** — Appendix A demonstrates the contested eigenvalue's seed-spread is *identical*
  whether the true value is the catalog value or a wild deviation, so the true difference is buried under the
  noise. **Seed-variation is uninformative about the truth at the unresolved sector.** A structural deviation
  there is **neither ruled in nor ruled out** by this computation. *(The genuine evidence is the resolved-21
  universal catalog-consistency — kept, see N5.)*
- **Correction B.** *"Natural boundary at n=4, proved structural / mathematically complete at n=4"*
  **OVERSTATES** and is withdrawn. **There is no mathematical boundary:** B103's factor-through-`N` makes
  `char(J(n)) =` the catalog a **class function for all `n`** — the tower does not stop at n=4. What walls is
  the explicit **computation** (eps-series pinv non-convergence, B84; engine-free trace-ring non-closure) — a
  **methodological ceiling, not a theorem**. The cusp collision is a *candidate* common root cause, not a
  proof that it causes the walls.

## N5 — the decisive computation
At SL(5) the Dehn-twist eps-series (B104) resolves **21 of 24** Dickson factors, and **the resolved 21 are
universally catalog-consistent** — `gcd(char(J), two-sequence catalog)` has degree **21** for every monodromy
tested (metallic + genuine non-metallic, both det signs), the same two-sequence catalog across seeds *and*
across monodromies. **This rigidity is genuine, strong evidence on the resolved sector.**

The **3 unresolved factors** are supported as `Sym²` (completing `μ_2=2`) by three independent **structural
routes** — **B89-T** (two-sequence), **B62** (θ-split / opposition involution), **B103** (the `GL(2,ℤ)`-rep
`ρ_n`) — *not* by the seed-variation (Correction A). The seed-variation is the **expected signature of the
eps-series rank-deficiency** (B84), uninformative about the truth there; the eps-series ceiling is 21/24 (cf.
B61's 22).

**Conclusion (honest).** The resolved sector strongly supports the catalog; the unresolved sector is
supported as `Sym²` by structural routes; **the strict "all 3 factors resolved" bar is NOT met**, so **the
explicit n=5 catalog is OPEN**. A structural deviation at the unresolved 3-dim sector is **neither ruled in
nor ruled out** by this computation.

## H6 — the forced cusp spectrum (a structural OBSERVATION, not a boundary proof)
The forced cusp spectrum (`tr A = tr A⁻¹ = 1`, B95) is `{1,i,−i}` (n=3), `{1,1,ω,ω²}` (n=4), `{1,1,1,−1,−1}`
(n=5). The **non-trivial eigenvalues are distinct at n=3,4 but collide at n=5** (`−1` with multiplicity 2); at
**n≥6 no finite-order spectrum exists** (B95). This collision is a **candidate common root cause** of the
three walls that looked independent — the tower wall (3 unresolved factors), the degree=rank wall (`A²=I` ⟹
dihedral ⟹ reducible, B95), the eps-series rank-drop — **recorded as a structural observation, not a proof
that it causes them** (Correction B). The structure `char(J(n)) =` the catalog holds for **all `n`** (B103);
what is bounded at n=4 is the *explicit computation*, not the theorem.

## The convergence (the project's thesis)
Every positive result is a property of **one object: `ρ_n`, the `GL(2,ℤ)`-representation on the SL(n) trace
ring at the trivial point.** The tower **is** `char(ρ_n)`; the module-iso **is** its decomposition into
`Sym^d` pieces (B103); universality **is** the well-definedness of `ρ_n` (B103); the parity **is** its
`det`-sign twist; the Hitchin identification (B101) places `ρ_n` in a known moduli space. `ρ_n` is **fully
characterized at n=3,4** (exact, constructive, universal); the **explicit n≥5 catalog is OPEN** (walled from
two methods).

**The open frontier (the live target, not a finished result).** Prove `char(ρ_n) =` the Dickson catalog
**directly from the `GL(2,ℤ)`-representation `ρ_n`** (B103) together with **B62's** multiplicities — *around*
the σ-construction, never building it. This would close n≥5 **by proof** and settle Correction A's open
question. B105 **sets up** the `ρ_n` thesis but does **not attempt** this proof.

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
