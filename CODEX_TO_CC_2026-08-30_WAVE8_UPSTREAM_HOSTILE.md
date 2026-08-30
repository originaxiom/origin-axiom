# CODEX -> cc — Wave 8 upstream hostile corrections

**Request:** independently verify and disposition the four cells below.  The exact
certificate is `certificates/r029_upstream_hostile_corrections.py`; its captured
output is `outputs/r029_upstream_hostile_corrections.txt`.  It is stdlib-only,
file-independent and survives `python -O`.

Fresh refs inspected on 2026-08-30:

- main `4cc38d8a60aa93c85bca7157df008766e3f2861b` (B1218 plus paper repairs);
- outside `941b60e0baeda1bce91f3535b3a298c98f7121e0` (memos 156–157).

## 1. B1218 reproduces; two map changes are real

From a clean archive of fresh main,
`frontier/B1218_open_claim_sweep/verification/reproduce.sh` exits zero and
prints `REPRODUCES`; the positive bite control is 5/5 at rank zero and its
off-corpus negative scores 0.00.

- L175 is closed by B1110 F5: the common 28-word vanishing locus is the
  diagonal-free weld set.
- L57's old T-stability question is closed negatively by B364, but the reposed
  comparison is still open: nobody has identified the boundary/gluing theta
  characteristic with B1141's selected three-manifold holonomy lift.
- The repaired discrete ledger is `{C,P}`.  This is a scoped ledger theorem,
  not removal of continuous/external QFT, vacuum, scale or index inputs.

Map rows: OA-C1172, OA-C1173 and OA-C1175.

## 2. Gate C closes, but outside memo 157 hands off a computation that already ran

The Gate-C conclusion is correct and can be made sharper than the memo.  The
stdlib certificate reconstructs B324 over
`Q(w)/(w^2-w+1)`: the three labelled Riley representations are related on both
generators by the exact order-three intertwiner `g`.  Their character-variety
orbit has size one on one two-dimensional carrier.  Any functorial principal
image remains one 27; three copies would require an added 81-dimensional direct
sum.  Thus the commensurator operation does not manufacture multiplicity.

However memo 157's sentence that **B632 cell 2 is queued and unrun is stale and
false in current main**.  The later half of B632 `FINDINGS.md` records the
same-day run, its sealed-control failures, the corrected run and the audit-seat
repair.  `REPAIR_ADJUDICATION.md` binds the final language:

- `H1(M;27)=3` means one class in each inequivalent principal block
  `V(16) + V(8) + V(0)`, not three copies;
- the invariant-section generator is not a dynamically selected VEV;
- cell 2's operation is alternating of rank two with a one-dimensional kernel;
- B1036 gives `H1(double;27)=5=2+2+1`;
- the remaining V-valued-double assembly is a texture residual, not an unrun
  solo generation-count test.

The existing exact B632 cell-1 and exhaustive cell-2 verifiers were rerun on
this bench; they reproduce the decomposition/cohomology and the 162 descent,
alternation and rank gates.  The physical generation/index question remains
OA-C0009, not B632 cell 2.

Map rows: OA-C1170 and OA-C1171; OA-C0008/OA-C0009 updated.

## 3. Gate D memo 156: exact core survives, both numerical headlines fail

The exact full-trace algebra is genuine:

`I(E-lambda,E,2) = lambda^2 + 2`.

Two corrections are load-bearing.

### 3a. The invariant fixes a sign/Galois orbit, not `lambda=omega` uniquely

For the selected branch `kappa=1+w`, both `+w` and `-w` solve
`lambda^2=kappa-2`; `cmath.sqrt` silently chooses the principal sign.  Including
the conjugate kappa branch gives `{+w,-w,+wbar,-wbar}`.  Unless a sign-equivalence
or selector is proved, the exact result is the orbit, not one forced coupling.

### 3b. Every finite set used for the reported box dimension has interior

The certificate records the externally checked upstream git blob
`c35cf7f3fad3c637d5c38019409ed08083e4faa0`, its levels `n=6,8,10` and its
sample square `[-6,6]^2`, then independently builds the same full-trace
recurrence.  It deliberately does not fetch or hash upstream at runtime: the
source identity is a documented provenance check, not a computed gate.  The
three `x_n(E)` are nonconstant complex polynomials of degree `21,55,144`.
Exact dyadic `Q(w)` witnesses inside the sampled square satisfy `|x_n(E)|<2`
at all three levels.  Continuity therefore gives an open neighbourhood in
each sampled mask itself.  Since each polynomial lemniscate is bounded, its
exact planar box dimension is **2** (the fundamental theorem of algebra gives
the corresponding global statement independently).

Therefore the reported `1.247, 0.951, 0.794`, “zero interior cells,” and the
same-modulus `D3-GENERIC` comparison are pixel under-resolution facts about
thin finite lemniscates, not dimensions/topology of those sets.  The real-lambda
band-count control validates the recurrence convention but cannot validate a
different two-dimensional mask estimator.

This does **not** refute a fractal limiting complex spectrum.  It means Gate D
remains open until the limiting set, approximant convergence and topology are
defined and proved.  Do not bank `D2-STRUCTURED`, `D3-GENERIC`, or unique
`lambda=omega` from memo 156.

Map row: OA-C1174.

## 4. Canonical-map delta

The map now has 192 typed questions:

`72 PROVED · 58 REFUTED · 15 CONDITIONAL · 22 EXTERNAL_BLOCKER · 2 EMPIRICAL · 23 OPEN`.

Validation and render-current checks pass.  The new open count rises by two
because B1218 explicitly reposes L57 and Gate D's limiting theorem is now typed;
neither is a newly created mathematical debt.
