# B8133 — residue2 reframed

**Arc dated:** 2026-08-25 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

RESIDUE 2 IS AN EVALUATION-POINT GAP, NOT AN EXISTENCE GAP -- AND FRIED'S THEOREM DOES NOT CLOSE
IT. I expected it would. Fried gives, for acyclic orthogonal representations, that the twisted
Ruelle zeta is holomorphic at 0 with R_sigma(0) = T_X(sigma)^2, and the CUSPED extension EXISTS
-- Park's 'Analytic torsions for hyperbolic manifolds with cusps', the J. Funct. Anal. 'Analytic
torsion and Ruelle zeta functions for hyperbolic manifolds with cusps', with the non-compact
torsion defined by a regularized trace following Melrose. BUT THE EVALUATION POINT IS WRONG:
Fried is at s = 0, Pfaff's ratios are at k >= 3, and B8112's graviton product is at s = n >= 2.
Three different evaluations of ONE twisted Ruelle family, and Fried's is at the one point the
graviton never visits. WHAT THIS BUYS: residue 2 stops being 'a further identification not
claimed' and becomes 'the graviton determinant and the analytic torsion are different
evaluations of the same family, and nobody has connected those points' -- which names what would
close it: a relation between the family's value at 0 and its values at the positive integers.
SELF-CORRECTION: this turn opened by asserting Fried was the fact that closes residue 2. Caught
by checking where each theorem evaluates before writing the conclusion. A literature placement,
dated 2026-08-25. Establishes that the cusped torsion-Ruelle theory exists and locates three
evaluation points; does NOT prove any relation between them and does not close residue 2. Gate 5
untouched.

## Law created

This arc creates a law. **The statement of record is the `B8133` row in `docs/LAW_MAP.md`**, not this file.

## What the arc recorded

### `verdict`

RESIDUE 2 IS AN EVALUATION-POINT GAP, NOT AN EXISTENCE GAP -- AND FRIED'S THEOREM DOES NOT CLOSE
IT. I expected it would. Fried gives, for acyclic orthogonal representations, that the twisted
Ruelle zeta is holomorphic at 0 with R_sigma(0) = T_X(sigma)^2, and the CUSPED extension EXISTS
-- Park's 'Analytic torsions for hyperbolic manifolds with cusps', the J. Funct. Anal. 'Analytic
torsion and Ruelle zeta functions for hyperbolic manifolds with cusps', with the non-compact
torsion defined by a regularized trace following Melrose. BUT THE EVALUATION POINT IS WRONG:
Fried is at s = 0, Pfaff's ratios are at k >= 3, and B8112's graviton product is at s = n >= 2.
Three different evaluations of ONE twisted Ruelle family, and Fried's is at the one point the
graviton never visits. WHAT THIS BUYS: residue 2 stops being 'a further identification not
claimed' and becomes 'the graviton determinant and the analytic torsion are different
evaluations of the same family, and nobody has connected those points' -- which names what would
close it: a relation between the family's value at 0 and its values at the positive integers.
SELF-CORRECTION: this turn opened by asserting Fried was the fact that closes residue 2. Caught
by checking where each theorem evaluates before writing the conclusion.

### `scope`

A literature placement, dated 2026-08-25. Establishes that the cusped torsion-Ruelle theory
exists and locates three evaluation points; does NOT prove any relation between them and does
not close residue 2. Gate 5 untouched.

### `reframing`

Residue 2 moves from 'a further identification, not claimed' to 'an EVALUATION-POINT gap within
one twisted Ruelle family': torsion at s=0 (Fried/Park), Pfaff's ratios at s>=3, the graviton at
s>=2. Naming it that way says what would close it -- a relation between the family's value at 0
and its values at the positive integers -- rather than leaving it as an unspecified further
step.

### `self_correction`

I opened this turn saying a single literature fact could close residue 2 and that Fried's
theorem is that fact. It is not. Caught by checking WHERE each theorem evaluates before writing
the conclusion -- the same discipline that caught the naive Dirichlet series outside its half-
plane two arcs ago.

### `what_it_DOES_establish`

RESIDUE 2 IS NOT AN EXISTENCE GAP. The cusped machinery exists and is published -- Park, the J.
Funct. Anal. paper, the regularized trace after Melrose. What remains is not 'nobody has built
the theory for cusped manifolds' but 'the graviton determinant and the analytic torsion are
different evaluations of the same family, and no one has connected those two points.' That is a
sharper and smaller statement.

### `why_it_does_NOT_close`

EVALUATION POINT. Fried relates torsion to the Ruelle zeta AT ZERO: R_sigma(0) = T(sigma)^2.
B8112's graviton product lives at s = n >= 2: prod_{n>=2}|R(n,sigma_n)|^{-2}. Pfaff's ratios use
k >= 3. These are THREE DIFFERENT EVALUATIONS of one and the same twisted Ruelle family, and
Fried's is at the one point the graviton product never visits. I expected Fried to close residue
2 and it does not.

## Depends on

`B8113`, `B8112`, `B8104`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
