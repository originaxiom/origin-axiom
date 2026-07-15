# Cell F verbatim result (the seat's full report)

## VERDICT
COMPUTED, PARTIALLY IDENTIFIED. All six Sym^{2m} exterior Wada torsions for m136 (silver RRLL bundle, monodromy [[5,2],[2,1]]) were computed at 150-250 digit precision from SnapPy's actual discrete-faithful holonomy, via a from-scratch Fox-calculus/Wada pipeline generalized to m136's 3-generator/2-relator deficiency-1 presentation. The pipeline was FIRST calibrated to reproduce all six banked B581 fig-8 values EXACTLY (a real bug was found and fixed mid-run: an early magnitude-based "trim near-zero coefficient" heuristic wrongly amputated the true leading term when it is much smaller than the polynomial's peak coefficient — exactly the skew-palindromic structure these torsion polynomials have; replaced with a rigorous large-t asymptotic degree probe). m=1,4,5 come out as EXACT RATIONAL INTEGERS (m=1 independently cross-checks the already-banked B622 value -16, via a completely different method — Fox calculus vs. Porti/Tran-Yamaguchi). m=7,8,11 come out as genuinely COMPLEX (non-real, non-integer) high-precision numbers; exact closed-form identification (PSLQ against {1,x1,x1^2,x1^3} and against {1,sqrt5} bases) did NOT succeed within budget — reported as 50+ digit numerics per the task's fallback instruction, unidentified pending further symbolic work. The (-1)^m sign law found in B581 for the fig-eight EXTENDS to m136 for all six exponents, via sign(Re(tau_m)).

## NUMBERS
SILVER BUNDLE (m136) six-exponent exterior torsion family, Sym^{2m} at the discrete rep, Wada/Fox-calculus convention identical to B581 (monic-normalized quotient, tau_m = Delta_m'(1)):

m=1  (d=3):  tau_1  = -16                                    [EXACT integer; = -2^4; MATCHES the already-banked B622 value (independent method: Porti/Tran-Yamaguchi formula) to the digit]
m=4  (d=9):  tau_4  = +11682800640                            [EXACT integer; = 2^10 * 3^3 * 5 * 7 * 12073; residual ~2e-40 at dps=250]
m=5  (d=11): tau_5  = -1357126041600000                       [EXACT integer; = -(2^21 * 3^2 * 5^5 * 7 * 19 * 173); residual ~1e-28]
m=7  (d=15): tau_7  = -19633485709495167168282623995.69214678699016213487756801486794678799... - 3.03626992598112624130183838894483342010638290681809265570890648294828...i   [NOT an integer; complex; held-out validation maxrel ~1e-52]
m=8  (d=17): tau_8  = +2502525465140358290282809720855596278.46889224379702069125379040149673604853693410365077329671893445197624884586... - 280895050746869353.66091925873964957425402423795730206410034863395875391566069160293813726064619134605285398429848300861567985...i   [NOT an integer; complex; maxrel ~1e-47]
m=11 (d=23): tau_11 = -1519818402359908041696091678080521808336358781974967.578944427132153071582490074454622046484628042238503510189058393830949959175778378764357390317449930962401120211331190152305455975119648894607907613778793559382928187121816201978231952804147603628399... - 889782740178568876924953370968738699532884382351145.853792316332740745871428205830191001094867635531084693942070676877013728316659698350035377580071843718555961184692855836883438778184029498509830282215651853850566501619032603650340212347580168351900931...i   [NOT an integer; complex; maxrel ~1.4e-41]

SIGN LAW vs (-1)^m (using sign(Re(tau_m)) for m=7,8,11):
m=1: (-16) -> sign - , (-1)^1=-1  MATCH
m=4: (+11682800640) -> sign + , (-1)^4=+1  MATCH
m=5: (-1357126041600000) -> sign - , (-1)^5=-1  MATCH
m=7: Re<0 -> sign - , (-1)^7=-1  MATCH
m=8: Re>0 -> sign + , (-1)^8=+1  MATCH
m=11: Re<0 -> sign - , (-1)^11=-1  MATCH
=> The fig-eight's sign(tau_m)=(-1)^m law (B581) EXTENDS to the silver bundle's exterior family, all six exponents, via the real part.

CALIBRATION (fig-8, via a from-scratch 2-gen/1-relator SnapPy presentation "aaabABBAb", DIFFERENT from B581's hand-built "abABaBAbaB" presentation — same field/rep, independent Fox-calculus code):
m=1: -3 (exact match)
m=4: 260736 (exact match)
m=5: -165110400 (exact match)
m=7: -3257341296168960 (exact match)
m=8: 100636318520821923840 (exact match)
m=11: -6908092175170718629633808125667573760 (exact match, matched only after the trim-bug fix described in caveats)
All six reproduce the banked B581 FINDINGS.md values to the digit (30-70+ correct digits each), via an independently-derived presentation — this both validates the new pipeline and gives B581 an independent cross-check.

qdeg (exact polynomial degree found by the large-t asymptotic probe) for m136: m=1->5, m=4->11, m=5->13, m=7->17, m=8->19, m=11->25 (pattern: qdeg = d+2 = 2m+3 in every case, d=2m+1).

## FINDINGS
## Method

Built a from-scratch numeric Fox-calculus/Wada twisted-Alexander-polynomial pipeline
(`pipeline.py` in the scratchpad), independent of B581's exact-field/E6-embedding
machinery, using:
- SnapPy's own high-precision (`Manifold.high_precision()`) discrete-faithful SL(2,C)
  holonomy for the manifold's own fundamental-group presentation (not a hand-built one).
- An explicit closed-form Sym^{2m} representation-matrix construction for 2x2 SL(2,C)
  matrices (multinomial expansion in the monomial basis) — this replaces B581's elaborate
  E6-in-gl(27) principal-embedding route with the much simpler direct fact that the
  Sym^{2m} irrep of SL(2,C) IS what those E6 isotypic blocks compute; verified this
  by full 6/6 exact reproduction of B581's fig-8 numbers via the direct route.
- A generalized Wada/Fox-calculus formula for deficiency-1 presentations with n
  generators / n-1 relators (m136's SnapPy presentation is 3 generators, 2 relators —
  the natural HNN-type presentation of a once-punctured-torus-bundle group does NOT
  reduce to 2 generators for m136 the way it does for the figure-eight): the abelianization
  character alpha (which generator carries the free Z factor of H1) is computed from the
  relators' exponent-sum nullspace (a:0, b:1, c:0 for m136 — b is dropped/denominator,
  a and c form the 2x2 block numerator).
- High-precision (150-250 digit) mpmath arithmetic; polynomial recovery via Lagrange
  interpolation at real integer nodes (roots-of-unity nodes were tried and rejected —
  some landed too close to actual poles of Den(t), causing large point-local error).

## A real bug found and fixed mid-task

The first working version used an ANALYTIC (conservative, cushion-padded) upper bound
on the shifted-numerator's degree, then trimmed apparent leading zero coefficients by
a magnitude-relative threshold. This passed for m=1,4,5,7,8 (fig-8) but silently gave a
WRONG answer for m=11 (off by ~10^7 in magnitude, wrong digit pattern entirely) — even
after cranking precision from 200 to 350 digits with NO change in the wrong answer,
proving it was not a precision issue. Diagnosis: fig-8's torsion polynomials are
skew-palindromic with tiny (+-1-ish) leading/trailing coefficients but ASTRONOMICALLY
larger middle coefficients (e.g. m=11's true top coefficient is 1, but the peak
mid-degree coefficient is ~1.3e37) — a magnitude-relative trim wrongly zeroed out the
TRUE small leading coefficient, silently using the wrong (2-too-low) degree. Fixed by
replacing the trim heuristic with a rigorous large-t asymptotic probe
(log|Q(t)|/log(t) -> exact integer degree as t -> 10^13ish), which is immune to this
failure mode. After the fix, ALL SIX fig-8 values match B581 exactly (m=11 confirmed
to ~30+ correct digits), and this fixed pipeline (`compute_tau_exact` in `pipeline.py`)
is what produced the m136 numbers reported above.

## Verification levels achieved

- Calibration: 6/6 fig-8 values exact vs B581, via an independent presentation.
- m136 m=1 (adjoint): -16 exact, matching the ALREADY-BANKED B622 value computed via a
  totally different method (Porti/Tran-Yamaguchi character-variety formula) — a genuine
  cross-method verification, not just internal self-consistency.
- m136 m=4,5,7,8,11: held-out-point validation (points beyond the interpolation fit
  window, re-derived independently from the same block_numerator/denominator functions)
  match the fitted polynomial to 40-70+ correct digits in every case — strong internal
  consistency evidence, though NOT an independent second method the way m=1 is.
- Sanity checks: relators map to the identity matrix under the holonomy to ~60 digits;
  SL(2,C) determinants =1 to ~60 digits; abelianization character verified by direct
  Smith-normal-form-style nullspace computation matching SnapPy's own H1 = Z/2+Z/2+Z.

## What is NOT done / open

- m=7, 8, 11 for m136 are reported as high-precision complex numerics only; PSLQ
  attempts against {1, x1, x1^2, x1^3} (x1 = the quartic trace-field generator,
  min poly t^4-4t^2+8) and against {1, sqrt(5)} (motivated by B622's "field crossover"
  note that the m=1 Jacobian eigenvalues live in Q(sqrt5) despite the quartic trace
  field) both failed to find a relation within a modest coefficient/step budget. This
  does not mean no such closed form exists — it means the search so far was not
  exhaustive (bigger field, bigger PSLQ coefficient bound, or a different natural basis
  is likely needed, and this is compute-budget-limited, not conceptually blocked).
- No independent second METHOD (analogous to B622's Porti/Tran-Yamaguchi check for m=1)
  was run for m=4,5,7,8,11 — Porti's simple "3-tr(Jacobian)" formula is specific to the
  adjoint (m=1) representation; the higher exponents would need a genuine second
  Fox-calculus route (e.g. a different SnapPy presentation of m136, analogous to the
  fig-8 cross-check) to get the same double-method confidence m=1 has. Time budget did
  not allow this for m136.
- The four largest values (m=5,7,8,11) were not independently factored/reduced beyond
  what sympy trivially gives for the two exact integers (m=4, m=5).

## Deliverables (scratchpad, not committed — repo is read-only per task instructions)

- `/private/tmp/.../scratchpad/cellF/pipeline.py` — the reusable Fox-calculus/Wada
  pipeline (alpha_map, sym_power_matrix, block_numerator/denominator, probe_degree,
  compute_tau_exact).
- `/private/tmp/.../scratchpad/cellF/run_m136_six.py` — the m136 driver script.
- `/private/tmp/.../scratchpad/cellF/m136_six_run.log` — full run log with all six
  m136 results, qn coefficient arrays, and held-out validation numbers.
- `/private/tmp/.../scratchpad/cellF/fig8_calib_run3.log`, `fig8_m11_retry.log` — the
  fig-8 calibration record (post-fix, all six exact).
- `/private/tmp/.../scratchpad/cellF/m136_six_results.pkl` — pickled raw results.

## CAVEATS
1. m=7, 8, 11 for m136 are NOT exact/symbolic yet — reported as 50+ digit complex numerics per the task's own fallback instruction; two PSLQ identification attempts (quartic trace-field basis; {1,sqrt5} basis) did not converge in the time available. Do not present these three as "the exact silver values" — only m=1, 4, 5 are exact integers.
2. The pipeline's overall SIGN/unit convention (which of the two kept generators is listed first in the 2x2 block, i.e. ['a','c'] vs ['c','a']) was fixed once and used consistently for all six m136 exponents, matching B581's convention style (monic-normalize the quotient, tau=Delta'(1)) — but this is a genuine "up to units ±t^j" ambiguity per B581's own Units Note; the relative signs across the six m136 values are meaningful (same convention throughout) but the absolute sign convention was not cross-validated against an independent external convention for m136 (unlike m=1, which cross-validates against B622's independently-conventioned -16).
3. A real computational bug (magnitude-based coefficient trimming silently picking the wrong polynomial degree) was caught only because fig-8 m=11 has a KNOWN banked answer to check against; the fix (asymptotic degree probing) is more robust in principle, but m136's m=7/8/11 values have no independent banked reference, so a subtler version of the same failure mode surviving the held-out-point check cannot be 100% ruled out — the held-out validation (40-70+ digits) is strong but, as the fig-8 m=11 incident showed, tiny held-out error is necessary but was once insufficient by itself before the degree bug was found and fixed by a different diagnostic (far-point extrapolation + exact-value comparison). For m136 m=7/8/11 a far-point extrapolation cross-check WAS run for m=7 (relative error ~1e-38 at t=500, outside the fit window) as an extra safeguard, giving reasonable additional confidence, but this is weaker evidence than the fig-8 case (which had a known exact target and reached 1e-58 agreement at t=100).
4. Precision used: 150-250 decimal digits (mpmath), chosen empirically per m to keep the Lagrange-interpolation conditioning loss (which scales badly with degree at consecutive-integer nodes) comfortably below the digits needed for the final answer; not formally profiled against a worst-case conditioning bound.
5. This work is exploratory/frontier-style computation done in the scratchpad per the task's own repo-read-only instruction — nothing was committed, no FINDINGS.md was written in the repo, and no banking/CLAIMS.md action was taken; that determination is left to the requesting agent.
