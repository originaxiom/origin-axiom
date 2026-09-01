# VERIFICATION — cell G2_t1_unblock (adversarial pass, 2026-09-01)

Independent verifier seat. Claimed verdict: **UNDERDETERMINED-PROVED** (+ freedom group dim 27
+ codimension analysis + commissioning spec; FORCED-NONZERO checked and NOT available).

## VERDICT: **CONFIRMED**

## 1. Re-runs (byte-level)

All three scripts re-run (copies executed from an isolated scratch directory so the cell's
committed outputs could not be overwritten; the grep/git routes target the repo root, which is
hardcoded, so behavior is identical). All exit 0; every `assert` passed.

- `g1_route_attempts.py` → output **byte-identical** to `g1_out.txt`; `g1_routes.json` identical.
- `g2_underdetermination_theorem.py` → **byte-identical** to `g2_out.txt`; `g2_theorems.json` identical.
- `g3_conditional_locus.py` → **byte-identical** to `g3_out.txt`; `g3_locus.json` identical.

`git status` on the cell directory: clean before this file was added.

## 2. Attack (a) — is the freedom group real, and does it move the 27 values?

**Preserves all committed constraints — yes, and structurally so.** Every generator of
G = (GL(A_7) × P(B_6) × P(B_2) × K^×)/(scalar torus) acts *within* fixed character eigenspaces
(labels 7, 6, 2), so the selection rule ρ+σ≡8 (K1) is label-preserved; the same frame change
applied to the mirror (B_2,B_6) block preserves B-leg antisymmetry (K2); the skew-(4,4) tail
slot is untouched by frame changes at labels 6 and 2 (K3). The parabolic shape
`not (a>=k and b<k)` is exactly g(conn)⊆conn (columns of conn basis vectors land in conn rows)
— verified as the correct filtration-preserving condition for conn = SUB.

**Independent re-derivation, different code path** (exact Fraction Gaussian elimination, not
sympy; seeds 1, 7, 424242, disjoint from the cell's 20260901): the 30×36 linearized action has
rank **27** on every random tensor tried; the three scalar-difference directions
(μ_A·I − μ_6·I etc.) annihilate an independently drawn tensor exactly. Raw dims 9+7+13+1=30
re-counted. So effective dim 27 = generic orbit dim 27 is not seed luck.

**Moves the values — yes.** The cell's own run shows a random G-element changing 9 of the 27
conn values of T_obs and moving T_ann's tail values (re-run confirmed); structurally, scaling
the B_2 conn columns rescales conn entries. The boundary bite (g[3,0]=1, tail→conn leak,
9 conn entries of transformed T_ann go nonzero) re-ran green; the leak element preserves the
character decomposition (tail-2 and conn-2 share label 2) but not the filtration — so the bite
genuinely isolates the filtration as the load-bearing committed datum, as claimed.

**Is G too big** (would make Theorem B overstate the freedom)? The only committed data that
could pin frames further are the five tail-row coordinate strings and the 33-column indices
(17,18 / 6,7,8) — but the strings are coordinates in the basis of an uncommitted presentation
(D and the e_i dictionary verified absent; see §4) and the indices name columns of the
uncommitted 672×33 matrix. Names without vectors fix nothing. Theorem A is independent of G
in any case.

## 3. Attack (b) — smuggled assumption toward FORCED-NONZERO / VALUES-COMPUTED

Not applicable in the incriminating direction: the cell claims the *negative* both ways, and
the committed record corroborates it **in its own words**:

- [M2] `YUKAWA_DOWN_RESIDUE_SPEC_308.md`, Verdict: "No numerical or exact 1×18 down-Yukawa row
  is present in the committed certificates… They do not construct the determinant comparison,
  normalized Calabi–Yau trace, or chain-level Serre realization needed to evaluate a coupling."
  Proof boundary: "Not proved: any nonzero down-Yukawa entry, rank, texture, determinant,
  normalized residue, or tail-coupled value."
- [M1] `YUKAWA_CUP_PRODUCTS_308.md`: "it would be false to infer a generic nonzero determinant,
  a rank, a texture relation, or a numerical coefficient for mu_d from the stable bundle or its
  characters alone"; KS rank 10 "is **not** a proof that mu_d varies."

Theorem A's two witnesses were re-checked through CHK (both PASS; spread 0 vs 6 nonzero exact
deviations) and the models are labeled synthetic throughout.

## 4. Independent corroboration of g1 (not trusting the cell's own probes)

- **Route B (git)**: my own `git log --all --diff-filter=A` over all 64 commits: **zero** adds
  matching any of the six evaluator artifact names; the only "308"-named files ever added are
  M1, M2, and the unrelated B308/B778 arcs. Confirmed: the evaluator files never entered the
  record on any branch.
- **Route C/D absence**: independent searches for the value-determining inputs found nothing:
  no `.sage` evaluator for 308 anywhere in the tree; no file carrying Φ's 44 coefficients
  (the "Phi_1" code hits are the Faddeev dilogarithm in B787 — unrelated); no 672×33 matrix
  ("672" hits are arc-id B672 and a numeric constant); no C18→C21 matrix D data. The B1162
  witness transcript (`verification/witness_sage.txt`, 11 lines) contains exactly
  `DATA candidate key = 308 / DATA norm = 308` plus rank gates — a name, not a construction,
  exactly as route D states.
- **Route A hits**: all four adjudications independently confirmed (B807's `11 x 18 = 198`
  face/motif count; B1139's hypercharge `"Tr_Y"` token; two prose mentions of the unbuilt
  T_cal in results JSONs).

## 5. Attack (c) — the conditional analysis vs the committed sources

- **Census sources check out against the record**: B1185 FINDINGS INV-2 carries "C12 imposes
  no texture zero, B1161" (permission, verbatim) and the E8 mechanism's "rank **exactly 2**,
  sector-UNIVERSAL"; INV-3 is verbatim "an index the object provably does not carry" with the
  fence "INV-3 is precisely the proof that it cannot be pulled back to the object" — the cell's
  labeled-conditional treatment is exactly right. B1205: "the down block is a 3×3×4 tensor
  (B1185), so [the cubic]" — a shape fact, as the census says. B1232 (PROGRESS_LOG 2026-09-01):
  the fork is real and open ("codex's exact connecting-block computation is still running; only
  the algebra is verified"), and the (3,4,1)/"nine-entry" phrasing matches the 27-vs-9
  discrepancy T1 flagged — the spec's count note routes it correctly and consistently with the
  committed census 36 = 18+9+6+3 ([M2] verbatim; 27 = entries with connecting Higgs leg).
- **Structural K^36 claim**: [M2] line 128–130 confirms the selection rule and that the
  skew-vanishing (4,4) direction is a pure-*tail* pair — outside the block. The three asserts
  (channel saturation, mirror-disjointness, (4,4)∉block) re-ran green.
- **E8-layer numbers re-derived independently** (fresh random points, seed 31337): det Y(t)
  has 20 cubic coefficients; Jacobian rank at a generic common-left-kernel point = **10**
  (dim 26 = 4×6+2 ✓); rank of {conn=0, det M0=0} at a rank-2 annihilating point = **28**
  (dim 8, codim 18 inside the 26-dim component ✓). Both witnesses W1/W2 verified in the re-run;
  the derived cross-check (law + annihilation ⇒ det Ȳ = 0) follows from the constant-pencil
  specialization and is correctly labeled falsifiable-conditional.

## 6. Findings that do NOT change the verdict (recorded for honesty)

1. **g1 route C's per-item grep is decorative**: `hits = grep_files(...)` is computed and then
   *discarded* — the `[ABSENT from committed code/data]` line prints unconditionally, and the
   pattern (first ~20 chars of the item name, e.g. `Phi`) would be noisy anyway. The route-C
   *conclusion* is nonetheless true (independently verified in §4, and stated by [M2] itself),
   but the "instrument has teeth" framing properly belongs to route A, not to route C's
   per-item searches. Recommended fix (not applied — this cell is not mine to edit): assert on
   a meaningful pattern or drop the dead variable.
2. **The K3 plant is caught by K2 first**: the planted nonzero skew-(4,4) diagonal trips the
   antisymmetry clause (v+v≠0 in char 0) before K3's own message is printed. Consistent with
   the cell's own remark that K3 is a theorem of K2 in char 0, but strictly the K3 clause is
   never the *deciding* clause on any planted case. Cosmetic.
3. **CHK's completeness** ("every committed constraint") is not itself machine-checked — it
   rests on the g3 forcing census. I verified the census's ten entries against their sources
   (§5) and the record's own proof-boundary prose (§3); it holds, but a future re-verifier
   should know the checker encodes K1/K2/K3 only.
4. `spread_exact(npts=12)` slices a 6-element list — 54 probes as printed; harmless dead
   parameter.

## 7. Scope

Nothing outside this cell directory was modified; this file is the only addition. All
verification scratch work ran in the session scratchpad. Gate 5: no measured SM value was
consulted or introduced by this verification.
