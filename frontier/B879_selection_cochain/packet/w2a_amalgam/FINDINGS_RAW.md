# W2a — THE AMALGAM/MAYER-VIETORIS QUANTUM COCHAIN (seat cc3, 2026-07-17)

Sealed wave-2 cell per `DESIGN_DA.md` and `PREREG_SCC.md` section W2a. Reuses
the scout's construction (`w0d_quantum_scout/quantum_probe.py`, `SCOUT.md`
candidate (d)) and the banked, read-only, test-locked
`frontier/B238_su32_levelrank/su32_wrt.py` (Kac-Peterson SU(3)_k modular
data). Repo untouched throughout. All work under this dir.

Artifacts: `w2a_amalgam.py` (script), `w2a_results.json` (all dims/terms/
verdict), `w2a_run.log` (verbatim `python3 -u` run capture). This file: data
+ documented modeling choices with UNSURE labels; no interpretation beyond
the sealed verdict labels.

## Arithmetic statement

**Exact cyclotomic arithmetic via Python `fractions.Fraction` over a
zeta-power basis** (the first option offered by the task, not sympy) — a
self-contained `CycField` class in `w2a_amalgam.py` represents elements of
Q(zeta_N) in the basis {1, zeta, ..., zeta^{deg-1}} (deg = phi(N)), with
reduction via the exact cyclotomic polynomial Phi_N(x) (computed here by
exact polynomial division of x^N-1 by the Phi_d, d|N, d<N — not looked up
from a table, not from sympy). sympy 1.14.0 and numpy 2.4.0 are present in
this venv but used ONLY for explicitly-marked float64 cross-checks against
the banked `su32_wrt.py`'s own numpy machinery — never on a verdict-path
number. Every rank/nullity/order computation is exact Gaussian elimination
with exact field division (extended Euclid on Fraction-coefficient
polynomials mod Phi_N).

**Validation of the exact construction:** at all four levels (k=1,2,3,4),
S_raw (raw Kac-Peterson sum) and T were built exactly, and independently
cross-checked against the banked `su32_wrt.py::su3_data(k)` float64 output:
`trace(W)`, `nullity(W-I)`, `nullity(T-I)`, and `W` unitarity all match to
float precision at every level (`w2a_run.log`, `crosscheck_match` in the
JSON, all `true`). At k=2 the normalized `S = S_raw/sqrt(K)` matches the
banked `S3` matrix entrywise to `5.3e-16` (development check, reproduced in
the delivered script's own gate). This is strong evidence the exact
cyclotomic implementation is computing the same object as the banked script,
just exactly rather than in float64.

**A derivation worth recording (avoids ever taking a square root):** the
true unitary S-matrix is `S = S_raw / c`, `c = sqrt(K)`, `K = (S_raw^dagger
S_raw)[0,0]`. Since W = T S^{-1} T^{-1} S and `S^{-1} = S_raw^dagger / c`
(from `S_raw^dagger S_raw = K·I` ⟹ `S_raw^{-1} = S_raw^dagger/K` ⟹
`S^{-1} = c·S_raw^{-1} = S_raw^dagger/c`), the two factors of `1/c` combine:
`W = T · S_raw^dagger · T^{-1} · S_raw / K` — a purely RATIONAL rescaling
(`K` was verified to reduce to a positive rational at every level: 48, 75,
108, 147 for k=1,2,3,4). No square root of a non-perfect-square is ever
needed. CONFIDENT, exact algebra, verified by the `S_dagger_S_gate` checks
in the JSON (`offdiag_zero`, `diag_equal`, `K_is_rational` all `true`).

## Controls (run before the amalgam work, as required)

All at kappa=5 (k=2) first, per instructions, then repeated at all four
levels:

1. **Bare-stage reproduction:** `nullity(W-I) = 0` exactly at kappa=5 —
   reproduces the scout's `quantum_probe_output.txt` (h⁰=h¹=0). MATCH.
2. **W unitary check:** `W · W^dagger = I` exactly (not approximately) at
   all four levels. MATCH (`W_unitary_exact: true` throughout).
3. **Weld eigenvalue orders vs scout's cross-check:** exact per-eigenvalue
   multiplicity computation (embedding W into the smallest cyclotomic field
   containing both its native entries and the needed roots of unity,
   `Q(zeta_60)` at kappa=5) gives: four eigenvalues of order 20
   (multiplicity 1 each) and two of order 10 (multiplicity 1 each), total
   multiplicity 6 = n. **Exact match to the scout's float64 "four of order
   20, two of order 10."**
4. **order(W)** (smallest m with W^m = I, exact): 4, 20, 12, 8 at kappa =
   4,5,6,7 respectively.

## The amalgam construction — modeling choices, documented

### 1. Each bundle copy M, M' as a mapping torus

`H^0(M) = ker(W-I)`, `H^1(M) = coker(W-I)`, both equal to `nullity(W-I)`
(square matrix ⟹ rank-nullity gives ker dim = coker dim automatically) —
this reduction is CONFIDENT, standard homological algebra (elementary free
resolution of Z), taken directly from SCOUT.md §3(d) and the task text.

**M' (the mirror copy)'s weld:** task offered "W^{-1} or the conjugated
weld." **Derivation/lemma (CONFIDENT, proved directly, not assumed):** for
ANY invertible operator A, `ker(A - I) = ker(A^{-1} - I)` *as the same
subspace* (v = Av ⟺ v = A^{-1}v), and since similarity conjugation and
transpose/complex-conjugation preserve eigenvalue-1 multiplicity, **every
reading offered by the task (inverse, similarity-conjugate, transpose,
complex-conjugate) gives the identical `nullity(W'-I) = nullity(W-I)`**. So
the ambiguity is immaterial to the computed dimensions. We used the concrete
construction `W' = W^{-1} = W^dagger` (valid since W is exactly unitary,
verified above) and confirmed `nullity(W'-I) = nullity(W-I)` directly by
computation at all four levels (`M_prime_lemma_holds: true` throughout), not
just by invoking the lemma.

**Consequence (a genuine structural finding, CONFIDENT):** because
`h1(M') = h1(M)` always and exactly, the "solo" contribution
`h1(M) + h1(M')` in any assembly of this amalgam is **always an even
number**, at every level, under every boundary choice. The classical split
2 (boundary-born) + **3 (solo)** has an ODD solo count. **An odd solo count
is therefore structurally unreachable by this amalgam model**, independent
of which boundary convention (below) or which level is chosen — a clean
parity obstruction, not a numerical accident of one run.

### 2. The boundary/annulus term — UNSURE, both variants computed

The task's own text: "the boundary Dehn twist acts by T — decide and
DOCUMENT the honest choice." Two variants were built and reported (neither
picked to hit a target number; both computed honestly, and the "trivial"
alternative is reported alongside on equal footing):

**PRIMARY (T^1 − I), reasoning:** the once-punctured-torus bundle's boundary
torus carries a peripheral pair — the monodromy/longitude direction (already
modeled by W on the M/M' side) and the meridian/fiber-boundary direction
(the curve encircling the puncture, not otherwise represented in this
single-operator toy model of M). `T` is already one of the weld's own two
named generators (`R = T` in the banked convention) and is *literally* the
operator representing a single twist about a curve in the mapping-class-
group presentation — the most natural, least-invented candidate for "one
turn around the meridian." We take `c = 1` (a single such twist) as the
simplest, most literal instance of the task's own "T^c − 1" suggestion,
since no other "banked" value of c was found anywhere in the read-only repo
(searched for "boundary twist", "peripheral", "meridian" near B640/B650/
B664/B662 — nothing named a specific c for this specific new construction;
this is genuinely new territory, as SCOUT.md itself says). **UNSURE**: this
is a reasonable, documented, literal reading, not a derivation from a deeper
topological compatibility proof — see the honesty note below on why a fully
rigorous derivation of the boundary's differential from first principles
was not attempted.
  - Gives: `h0(bd) = h1(bd) = nullity(T-I)` = 0, 0, 0, 4 at kappa = 4,5,6,7.

**ALTERNATE (trivial differential, d_bd = 0):** models the boundary purely
as "the annulus contributes the full stage V" with no monodromy at all
(the task's other offered option). Gives `h0(bd) = h1(bd) = n` (the full
stage dimension) at every level: 3, 6, 10, 15.

We did **not** search over other powers `T^c` (c=2,3,...) or other operators
(L, W, S) to find a value that would hit 5 — doing so after seeing the
target would be fitting, not deriving, and the prereg's exact-arithmetic
discipline is explicitly about honest reporting over curve-fitting. The two
variants above were fixed *by the reasoning stated*, then computed once.

**Honesty note on rigor (UNSURE, stated plainly):** a fully rigorous
Mayer-Vietoris construction requires the restriction maps
`C^*(M) → C^*(bd)`, `C^*(M') → C^*(bd)` to be genuine chain maps
(intertwining each side's differential with the boundary's), which in turn
constrains what `d_bd` is allowed to be relative to `W`. Our single-operator
toy model of M (which discards the once-punctured torus's actual F_2
fundamental group and keeps only the Z generated by the monodromy) does not
carry enough data to derive this compatibility from first principles — this
is exactly the gap SCOUT.md flagged ("nobody has assembled the actual
Mayer–Vietoris sequence and chased dimensions yet"). We resolved this by NOT
attempting a literal double-complex construction (which we verified by hand
does not close, i.e. D²≠0, unless `d_bd` is forced to equal both `W-I` and
`W'-I` simultaneously — impossible in general) and instead using the
dimension-counting form of the sequence exactly as written in the task,
under one explicit simplifying assumption (next section).

### 3. The Mayer-Vietoris connecting maps — assumed ZERO (UNSURE, documented)

The classical sequence `H^0(M)⊕H^0(M') → H^0(bd) → H^1(D) → H^1(M)⊕H^1(M')
→ H^1(bd)` is exact, but exactness alone does not fix `h^1(D)` from the five
flanking dimensions without knowing the RANKS of the two connecting/
restriction maps — data this toy single-operator model does not supply. We
assume **both connecting maps are the zero map** (the simplest, most
conservative choice — no invented cancellation). Under this assumption the
sequence splits cleanly and gives:

```
h0(D) = h0(M) + h0(M')
h1(D) = h0(bd) + h1(M) + h1(M')        [ = "boundary-born" + "solo" ]
h2(D) = h1(bd)                          (informational only, not in the falsifier)
```

**Why this specific assumption, not another (e.g. "generic/maximal rank"):**
it is the ONLY one of the natural candidate assumptions that reproduces the
qualitative SHAPE the task and DESIGN_DA.md ask us to check for — a visible
split into a boundary-born piece (`h0(bd)`) and a solo piece
(`h1(M)+h1(M')`), directly mirroring the classical "2 (boundary-born) + 3
(solo)" decomposition structurally, not just in total count. This is
supporting rationale, not proof, of the assumption — **UNSURE**, flagged
plainly. (We also proved in §1 above that the "solo" piece is forced even
regardless of this assumption, an independent, assumption-free structural
fact.)

## Results

**All values below reproduced independently against the banked
`su32_wrt.py` float64 machinery** (`crosscheck_match` all `true` in the
JSON) in addition to being computed exactly.

| k | kappa | n | nullity(W−I) [=h1(M)=h1(M')] | nullity(T−I) [h0(bd), primary] | h1(D) primary (T-bd) | h1(D) alt (trivial-bd) |
|---|-------|---|---|---|---|---|
| 1 | 4 | 3  | 1 | 0 | **2**  | **5**  |
| 2 | 5 | 6  | 0 | 0 | **0**  | **6**  |
| 3 | 6 | 10 | 0 | 0 | **0**  | **10** |
| 4 | 7 | 15 | 1 | 4 | **6**  | **17** |

`order(W)` exact: 4, 20, 12, 8 (k=1..4). K (rational normalization
constant): 48, 75, 108, 147.

## THE SEALED FALSIFIER — verdict at kappa=5 (k=2)

- **Primary (T-boundary):** h1(D) = 0. Split = (0 boundary-born + 0 solo).
  **h1(D) ≠ 5 ⟹ MISMATCH.**
- **Alternate (trivial boundary):** h1(D) = 6. Split = (6 boundary-born + 0
  solo). **h1(D) ≠ 5 ⟹ MISMATCH.**

Neither variant reaches 5 at kappa=5, and (per §1's parity proof) no variant
of this specific amalgam model at any level or boundary choice can ever
reproduce the classical 2+3 split's ODD solo count. **Verdict: MISMATCH**
(bankable wall), reported exactly as computed — no fitting attempted.

## Secondary — stage-selection probe (levels 1,3,4 vs 5)

- Primary (T-boundary) h1(D) by level [k=1,2,3,4]: **[2, 0, 0, 6]**. kappa=5
  is **NOT** uniquely singular here — it is *tied* with kappa=6 (both give
  0). Stated plainly: no clean jump at kappa=5 under this convention.
- Alternate (trivial-boundary) h1(D) by level: **[5, 6, 10, 17]**. This is
  monotonically increasing with the stage dimension n (h1(D) = n +
  2·nullity(W−I)), so kappa=5's value (6) is technically distinct from its
  neighbors only because n itself is distinct — not a distinguished "jump."
  (Curiosity, reported honestly and not chased further per the no-fitting
  discipline above: under this alternate convention, k=1/kappa=4 — not
  kappa=5 — is the level that numerically equals 5.)

Stated plainly per the task's request: **kappa=5 is not singular among
{4,5,6,7} in either boundary convention computed here.**

## Scope / what this cell does NOT close

- Does not derive the boundary complex's differential (or the Mayer-Vietoris
  connecting maps' ranks) from a first-principles compatibility proof; both
  are documented, honest, UNSURE-flagged simplifying choices, not theorems.
- Does not attempt candidates (a)/(b)/(c) from SCOUT.md (module-functor/
  tube-algebra Hochschild cohomology) — those remain PRICED (need F-symbols
  not banked anywhere in the repo).
- Per the design's own framing, a MISMATCH here is an informative, banked
  result: "the classical 5 is then invisible to this quantum theory, and the
  tube-algebra route becomes the priced next candidate" (DESIGN_DA.md).
