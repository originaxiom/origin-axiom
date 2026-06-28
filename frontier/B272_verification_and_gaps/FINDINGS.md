# B272 — adversarial verification pass over the E₆-bridge arc (B262–B271): confirmed, corrected, and what's missing

**Status: banked verification record (frontier). FIREWALLED. Nothing to `CLAIMS.md`.** "Verify verify verify, and
see what we're missing." Two independent audit agents + orthogonal hand-checks re-derived the riskiest claims from
scratch (motivated by the earlier `Sym`-convention bug that had produced a clean-looking *wrong* answer).
`verification_and_gaps.py`.

## What survived independent re-derivation (method ≠ the banked code)
- **`dim H¹(Sym^{2k})=1` for all k** — three ways: exact `ℚ(√−3)` arithmetic, mod-`p` Fox over large primes
  `{61,103,9973,99991}`, and convention re-validation. Matches Thurston (k=1) and Menal-Ferrer–Porti. The
  convention bug is **gone**.
- **figure-eight group ↠ `SL(2,𝔽₃)=2T`** — GAP `StructureDescription = SL(2,3)`, order 24; `ω→1, t→2 mod (√−3)`
  re-derived.
- **binary-polyhedral only `q∈{3,5}`** — by isomorphism to the SU(2) finite-subgroup list + Frobenius–Schur
  indicators (faithful quaternionic 2-dim irrep only at `2T`, `2I`).
- **E₆-Zariski-density of `{4,8}`** — Sage re-run reproduces (`78` vs `52`); Dynkin fact correctly applied.
- **τ-fixed = genuinely type F₄, and τ outer** — rank 4 + dim 52 + semisimple (Killing nondegenerate) *forces* F₄;
  the diagram automorphism `(1 6)(3 5)` has Cartan signature `(+1)⁴(−1)²` ⟹ outer (the real form EIV).
- **cup-product check non-vacuous** — `rank d¹ = 2 < 3` (proper image, `H²` 1-dim), `Q(ξ)≠0`, and `Q(ξ)∈im d¹` is a
  *real* vanishing (a random vector is not).
- **`Vol(4₁)=2.0298832`** (SnapPy), both tetrahedra `e^{iπ/3}`.
- **"τ-broken = E₆-density" is exact** (tangent level): a deformation generates `e₆` ⟺ it has a `{4,8}` component
  ⟺ it breaks τ.

## Three framing overclaims — corrected (in each FINDINGS)
1. **B265 "E₆-irreducible connections EXIST" → "expected to exist."** Solid: `dim H¹=6=rank` + Zariski-density.
   *Not* proven: **integrability** of the `{4,8}` directions — the `e₆`-bracket-coupled obstruction
   `H¹×H¹→H²(e₆)` is uncomputed (B270 did only the `SL(2)`/exponent-1 block). MFP is the *dimension count*, not an
   E₆ smoothness theorem. **Residual open item: the `{4,8}` obstruction.**
2. **B267 "five independent invariants ⟹ one E₆" → a consistency check.** The geometric side is E₆ *by
   construction*; once the arithmetic side is E₆, `h`/dim/exponent-sum/Molien agree *automatically*. Genuine
   content = exactly two facts: the arithmetic *independently* lands on E₆, and its exponent set matches B264's
   grading. (`e6_coherence.py` hard-codes the E₆ Dynkin; the real `McKay(2T)` derivation is in B266.)
3. **B266 "only `q∈{3,5}`" justification — fixed.** The stated reason skipped `q=4` (`=A₅`, the icosahedral
   near-miss to `2I=SL(2,5)`). Decisive criterion = the faithful quaternionic irrep, not the center test alone
   (which passes for all odd `q`). Conclusion unchanged.

## The extended gap map — walls the 5-wall map (B259/B268) did *not* contain
| gap | kind | in 5-wall map? |
|---|---|---|
| **input-E₆ = output-E₆** | **CRUX** | wall #2 (reduced) — but understated |
| **family replication (3 generations)** | **WALL** | **ABSENT** |
| **SM matter content / E₆→SM breaking** | **WALL** | **ABSENT** |
| cosmological-constant **SIGN** (Λ<0 hyperbolic vs Λ>0 observed) | WALL | wall #5 is *magnitude-only* |
| principal `sl(2)→E₆` embedding is a choice | ASSUMPTION | implicit in B264 |
| no dynamics / vacuum selection | ASSUMPTION | walls #3/#5 |

- **The crux:** the whole bridge rests on the *single* unproven conjecture that the 3d-3d **input type** equals the
  arithmetic McKay-E₆. The 3d-3d type `G` is a *free choice*; B266 makes the arithmetic E₆ canonical but does not
  force the 3d-3d input to match it. B268's "REDUCED — no math obstruction left" *understates* this.
- **Two real walls are absent from the map:** *family replication* (one figure-eight → one character variety; the
  `ℤ/3` is the Eisenstein cube-root, **not** 3 generations — B257; B254 dead) and *SM matter content / the E₆→SM
  breaking* (generic, not object-specific — B252/B254/B207). Deflated *elsewhere* in the repo, but invisible to a
  reader of the B268–B271 arc.
- **The Λ-sign** is separate from wall #5's 122-order magnitude: all the E₆ structure lives on the hyperbolic
  `Λ<0` (AdS) end, while observed dark energy is `Λ>0` (dS). Flagged only in `speculations/` (S042/S043).

## Net
The **core mathematics survived** independent re-derivation (the convention bug is gone, the Lie theory is forced,
the volume and cohomology are exact). The weaknesses were all in **framing** (now corrected) and in **scope of the
wall map** (now extended). The honest one-line status: *the figure-eight carries E₆ coherently from two
directions, with chirality identified as its E₆-density directions — but the bridge to physics hangs on one
unproven conjecture (input = output E₆), and the map was silent on family replication, SM matter, and the Λ-sign.*

Anchors: B262–B271 (the arc), B259/B268 (the 5-wall map), B257 (the ℤ/3 ≠ 3 generations), B254/B207 (SM-content
negatives), S042/S043 (the Λ firewall). Method: two adversarial general-purpose audit agents + SnapPy/GAP/sympy
hand-checks.

## Update (2026-06-28 / B273) — the B265 residual is resolved
The "residual open item" recorded above for B265 (the uncomputed `e₆`-bracket-coupled `{4,8}` obstruction) has been
**computed in B273**: the full quadratic cup product `H¹×H¹→H²(e₆)` is **identically zero** (exact, two primes, all
directions + generic). B265's status moves from "expected to exist" to "established to second order." The remaining
gaps in the extended map (the `input-E₆=output-E₆` CRUX; family replication; SM matter; the Λ-sign) are unchanged.
