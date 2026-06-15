# An SL(4,C) Dehn-filling slope of the figure-eight knot — narrow note (PC13)

> **SUPERSEDED (2026-06-15).** The "component" framing here is **refuted** (round-2 deformation theory,
> verified): `{1,1,ω,ω²}` is not rigid, so the family is a codimension-1 **slice**, not a component. The
> honest, stronger result is the **rank-stratified degeneration of degree=rank** (component at n=3, slice
> at n=4, absent at n=5) — banked in `frontier/B153_degree_rank_degeneration/`. This note is retained as a
> record and is to be **rewritten to the B153 thesis** before any external use. `[A,B]=−µ⁴` on the family
> and the completeness-for-the-fixed-spectrum remain correct as *slice* statements.

The post-review rewrite of the flagship's mathematical core, scoped to one submittable result.

**Scope.** One SL(4,ℂ) figure-eight component: the Dehn-filling slope `L=−M⁴` (matrix identity
`[A,B]=−µ⁴`, so `µ⁴[A,B]⁻¹=−I` central) and its completeness (the 4-parameter family is the entire
irreducible locus for the `{1,1,ω,ω²}` spectrum). The metallic trace-map tower (Dickson factorisation,
proved n≤4, with the corrected n=2 base case) is context. The philosophical essay of the flagship is
**split off** and not part of this note.

**Honest framing (from the review-gate resolution).**
- `L=−M⁴` is a **Dehn-filling slope** — the SL(4) analogue of Falbel's SL(3) `M³=L`, **not** exotic
  A-polynomial geometry.
- It is a **different component** from the convex-projective (Ballas / Cooper–Long–Thistlethwaite)
  families, whose meridians are unipotent; ours is finite-order `{1,1,ω,ω²}`.
- The **family is n=3 (known) + n=4 (this paper)** only; the SL(5) case is **open** (the n=5
  "impossibility" had a semisimplicity gap — see §5).
- **Completeness** is badged honestly: symbolic primary decomposition (the components) + exact F_p
  Burnside (irreducibility), validated against a hand-proved reducible stratum — not a blanket PROVED.
- **Novelty:** `NEEDS-SPECIALIST`. The convex-projective quadrant is excluded; the extended-Ptolemy
  machinery (Zickert) is the right tool but published only at n=2. A specialist email is the close.

**Build.** `make figures && make pdf` (needs latexmk + pyenv numpy/matplotlib; fig_strat reads
`frontier/B149/irreducibility_fp.json`). Code & a finite-field certificate to be deposited (Zenodo DOI)
at submission; the symbolic certificates are in the appendix meanwhile.

Files: `main.tex`, `sections/`, `refs.bib`, `figures/gen.py`.
