# D5 — THE TRIALITY DECOMPOSITION (sealed prereg; cc2, 2026-07-16)
# ADVISORY for cc's H1(D) lane (L92-adjacent), labeled as such.

**Question:** does B299's trinification Z3 (theta, phi — order-3, commuting, free on
the 27's weights, 9 orbits of 3) act on H1(D; 27), and if so does it grade the five
banked classes into the 3+2 split chat-1's plan assumed (their step 1, done as pure
mathematics)?

**Construction (exact, no floats):** the 27-basis and holonomy matrices A27, B27 (and
the double's third generator) come from the SAME source the banked cell-3 pipeline
used (exec of B575 l51_obstruction.py stages 0-3 + cell3b_stage1 machinery /
stage1_classes.pkl). The triality candidates act on the WEIGHT LABELS by B299's
6x6 Dynkin actions; any actual action on the 27 vector space is a PHASE LIFT:
X = P.D with P the weight permutation and D diagonal (27 unknown phases).

**Sealed decision tree (all outcomes bankable; pattern-first ordering):**
1. WEIGHT BRIDGE: match B299's 27 weight labels to the B575 build's basis order
   (simple-root relabeling search over coordinate permutations mapping weight-set
   to weight-set; every consistent relabeling's induced 27-permutation is carried
   forward as a candidate pattern). If no weight-label list is recoverable from
   the build => OBSTRUCTED-AT-BRIDGE, banked honestly with the fix named.
2. PATTERN SOLVE (exact, the load-bearing step): for each candidate order-3
   pattern P (theta, phi, and their independent products; all consistent
   relabelings): solve X = P.D (27 unknown diagonal entries over the exact field)
   with X M = M X for M in {A27, B27, C27}. dim 0 at every pattern =>
   NO-PATTERN-SOLUTION (banked with constraint ranks; Schur note: if the 27 is
   holonomy-irreducible this is forced — recorded as diagnostic context, computed
   as a float-SVD commutant dimension with the gap stated, labeled non-exact).
   dim >= 1 => ACTION-FOUND:
3. Normalize (X^3 must be scalar; rescale to X^3 = I; verify order 3 exactly), push
   to H1 (X acts on cocycle values; verify it preserves the coboundary space
   exactly), grade the 5 classes by omega-eigenvalue. BANK the grading vector
   (dim_1, dim_omega, dim_omega2). The "3+2 split" prediction (chat-1's assumption)
   is CONFIRMED only if the grading is {3 in one eigenvalue, 2 elsewhere} or
   {1,2,2}-with-a-generation-triple structure — state exactly what is found; any
   grading is a result.
4. If ACTION-FOUND: restrict the banked B637 alternating cubic to graded components
   (which Y[ijk] slots connect which grades — the omega-selection rule: a cubic
   invariant needs total grade 0 mod 3; TEST this selection rule against the banked
   zero law Y[01k] = 0 and the nonzero slots). Prediction P-D5-a (sealed): IF an
   action exists, the banked zero/nonzero pattern must be CONSISTENT with the
   grade-sum-zero selection rule (a violation kills either the action's correctness
   or the rule — audit before banking).

**Gates:** the exec'd pipeline must reproduce stage-1's banked artifacts (h1 = 5
class basis rank; the pkl's classes verified as cocycles: values satisfy the Fox
cocycle condition) before any triality work. Repo read-only throughout (exec of
repo scripts only; PYTHONDONTWRITEBYTECODE=1).
