# EXTERNAL REVIEW — THE PAPER, 2026-09-09

An outside pass over `main.tex` and the verification package: independent re-derivation, prior-art
adjudication, and an assessment of whether a neighbouring programme's machinery is usable here.
Written for the banking seat. Nothing below was read off the record; every number was recomputed
(SnapPy 3.3.2, sympy 1.14.0, own anomaly/group code).

---

## 1. What reproduced independently

The hypercharge cubic is exactly `-18(t-3)(t+3)` with the two known rays; `SL(2,Z/4)` has seven
involutions so it is not `2O`; the adjoint is absent from `27x27` (27 is complex, so its zero weight
has multiplicity 0 against the adjoint's 6); 87 covers to degree 10 splitting 9 cyclic + 1 regular
(amphichiral) + 77 irregular with 66 chiral; 12 chiral one-cusped and 54 multi-cusped chiral covers;
2804 census manifolds with `H1 = Z` to seven tetrahedra splitting 2794/7/3 with m004 among the three;
cusp-fixed parity over 1200 one-cusped manifolds with the two-cusp control firing; `M^2 = RL`;
`C(10,5) = 252`; the metallic-grammar level argument and its `N=4` near-miss.

Every one matched. The base-rate discrepancy of §2 was resolved against the first implementation
(145/400 and 124/400, counting up to `Aut(SL(2,3))`).

**This is worth stating in the paper.** The appendix currently says all verification is internal,
which to a referee reads as *nothing has been checked by anyone else*. That is no longer true.

---

## 2. Structural opinion (requested)

**The structure is good; the problem is that it is not one paper.** It is four: a mathematics paper
(Thm 4.1, the chain, §7), a physics paper (§5, §6), an epistemology paper (§2, §8, §9, the Scope
notes), and a programme status report (§12, the appendix). No single referee is competent for all
four — math.GT will not assess anomaly cancellation, hep-th will not assess the covers census, and
neither will referee §8. The likely failure is not rejection on the merits but a desk rejection or a
referee who reviews the fifth they know.

**Length will not fix this; it worsens it.** Past ~40pp referees skim, and skimming is where errors
survive — as the §8 sentence did, retracted in this repository on 2026-09-02 and still in the draft a
week later.

Recommended split, strongest-first:

- **Paper 1 (math.GT, ~20pp)** — §7's results plus Thm 4.1. Novel, checkable, and *independent of
  whether the E6/SM story is right*. Also the easier arXiv endorsement.
- **Paper 2 (hep-th/math-ph)** — §5's arena/content division, the `Z6` global form, termination, §6.
- **Paper 3** — §2, §8, §9, §12. Foundations-of-Physics territory, or an unsubmitted preprint.

Keep exactly as they are: the inversion (genericity before any positive claim), §10's practice of
moving items off the novelty list, §9 as the spine, §11's executable bounds, the Scope-note device.

Four concrete referee-facing items: (a) say the results were independently reproduced; (b) deposit
with a Zenodo DOI — referees accept Zenodo, they do not audit git branches; (c) the chain table claims
34 theorems while the paper contains exactly one `theorem` environment — state them or stop calling
them theorems; (d) the author block is still `[author]`/`[affiliation]`, a hard blocker.

---

## 3. Prior art: Asselmeyer-Maluga — adjudicated

Sixteen papers read (448pp, ligature-normalised so the scans are reliable; a naive grep gives false
negatives because the PDFs use `fi`/`fl` ligatures).

**He reaches the doorway.** Fermions as hyperbolic knot complements; Mostow rigidity as the reason for
the category; §7 of 1910.09966 titled *Fermions and Number Theory*; quaternion algebras and arithmetic
Kleinian groups defined; Maclachlan–Reid cited as [73]; and, verbatim:

> "The complement of the figure 8 knot is one example of an arithmetic hyperbolic 3-manifold."

**And stops.** That section closes:

> "We hope to use this relation in the future to obtain more properties of fermions by using number theory."

His number theory is used only for **volume** (Bloch–Wigner, dilogarithm). Across all sixteen papers:
**McKay 0, binary tetrahedral 0, E6-as-Lie-algebra 0, SL(2,3) 0, hypercharge 0, anomaly cancellation 0,
commensurability 0, amphichirality 0.** The trace-field → 2T → McKay → E6 route is flagged and untaken,
ten years on. **The prior-art gate holds on the specific route.**

Differences that matter: his gauge group comes from torus-bundle isotopy classes (1+3+8), not McKay;
his charge from the Hirzebruch defect; his three generations from Donaldson forbidding fewer than three
`S^2 x S^2` in K3. On selection he writes that asking which knot is the electron "is meaningless in our
approach", because the branching set of a 3-manifold is not unique — an objection specific to his
branched-cover construction, which does not apply to arithmetic selection here. **But** Scope 8 already
concedes the trace field is a commensurability invariant that does not separate m004 from m003, so both
programmes have a selection problem reached by different roads. Do not claim ours is solved.

**Correction to the internal reading note:** the "three generations convergence" is not one. His three
is a claim; §7 here explicitly declines three (the cusp-fixed count is even, and three appears only
through the vector-like `Z/3` descent). There is nothing to adjudicate.

**§10 entry recommended** — the disclosure strengthens the paper, since §2 already spends credibility
buying honesty about genericity. Also add the 3d-3d correspondence (Dimofte–Gaiotto–Gukov et al.),
where the figure-eight complement is the canonical worked example; different target, but a hep-th
referee will ask within thirty seconds.

---

## 4. Is his machinery usable? — the honest split

**His 4d is not the 4d this programme needs.** K3-as-spacetime, exotic smoothness, Akbulut corks and
Casson handles are a *spacetime* construction. The index theorems that license a generation count act
on an **internal** space (CY3, G2). His generation count is a smoothness obstruction, not an index
theorem. Transplanting it imports contested machinery for no gain against Scope 14.

**But the 4d question should not be dropped — it should be re-aimed.** The applicable framework is
**Atiyah–Patodi–Singer index theory on a 4-manifold with boundary**, and it is absent from the paper:
`Atiyah`, `APS`, `eta invariant`, `signature defect`, `Hirzebruch` appear **nowhere** in `main.tex`.

### 4a. `Omega_3^SO = 0` is being read backwards — the main technical finding

The record grades the 4d filling **IMPOSSIBLE-BY-THEOREM as canonical** (B716, B717, B724,
GRAND_COMPUTATION_LEDGER A3): fillings exist, are infinitely non-unique, nothing selects one.

That conflates two different things:

- *selecting* a filling — indeed impossible, **and unnecessary**;
- obtaining a **filling-independent invariant** — which is precisely what APS is built to deliver.

APS is designed so the bulk integral's dependence on the filling is cancelled by the eta-invariant
boundary correction. The signature defect is the classical instance: `sign(W)` and `int_W L(p_1)` each
depend on `W`, but the combination defines `eta(M)` intrinsically. **`Omega_3^SO = 0` is not the
obstruction; it is the enabling hypothesis** — it guarantees a filling exists at all, which is what APS
requires. Non-uniqueness is handled, not fatal.

If this holds, a wall currently graded impossible-by-theorem is instead a computation.

**Status: a lead, not a result.** What must be checked before any claim: (i) that APS applies in the
*twisted, non-unitary* `E6` setting used in §7, where the published twisted-duality theorems were
already found not to apply; (ii) the cusped (non-compact) case, which needs the Atiyah–Donnelly–Singer
treatment rather than plain APS; (iii) whether the resulting index is the same functional as
`I(V) = t_0 - r_1` or a different one.

Note the earlier sweep (B940) did meet this literature but asked a different question — it was hunting
for *numerical Dirac eigenvalues* and correctly concluded "all analytic, no numbers." The index-theoretic
use proposed here was not the question then.

**This is where Asselmeyer-Maluga is genuinely useful.** His Hirzebruch defect `h = 3 sigma(M) - p_1(M,Sigma)`
is a signature-defect construction — the same family of invariant — used by him for charge. The
suggestion is to take the *invariant*, not his use of it. And for cusped hyperbolic manifolds the
signature defect is classically expressed through **L-functions of the number field** — which here is
`Q(sqrt-3)`. That is a direct line between the trace field the paper already carries and the 4d wall it
has declared shut.

### 4b. A second lead: the sigma row and trinification are the same structure

The `sigma` row needs the boundary theory to be `(E6)_1`, at `c = 78/13 = 6`. Verified: `c(su(3)_1) = 2`,
and `3 x 2 = 6`, so **`su(3)_1 x su(3)_1 x su(3)_1 subset (E6)_1` is a conformal embedding** (central
charges match exactly). The trinification frame of §5 — three orthogonal `A2`s — is that same
decomposition at the chiral-algebra level. The paper currently treats the two as unrelated. If the
boundary theory is to be identified as `(E6)_1`, its `su(3)^3` conformal subalgebra is the natural
place to look, and the anti-numerology clause is satisfied because the frame is already the object's,
not imported to fit.

**Status: a lead.** It does not by itself supply the graded character or meet the six conditions.

---

## 5. Summary for the seat

| item | status |
|---|---|
| independent reproduction of the checkable claims | **done, all matched** |
| prior-art gate on trace-field → McKay → E6 | **holds** (16 papers, verified absent) |
| Asselmeyer-Maluga §10 entry | **recommended**, wording in §3 above |
| 3d-3d correspondence citation | **recommended** |
| "three generations convergence" | **not a convergence** — drop it |
| his 4d (K3, exotic smoothness) | **not usable** for Scope 14 |
| APS / eta on a bounding 4-manifold | **the lead worth taking**; `Omega_3^SO = 0` re-read as enabling |
| `su(3)_1^3 subset (E6)_1` for the sigma row | **lead**, central charges verified |
| paper structure | **split recommended**; length is not verifiability |
