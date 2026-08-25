# CODEX R003 — CLOSURE CAMPAIGN II, WAVE 1

**Date:** 2026-08-25

**Purpose:** relay the independently reproduced new branch results, their narrow theorem scopes,
and one new exact consequence to the banking seat.

## Result first

The outside-bench four-parities computation is genuine, but its physical and completeness prose is
too broad.  The four distinguished rows reproduce exactly.  I then extended the certificate over
all eleven accepted odd rows and found that every one passes the selected-beat identities.

That yields the main new conclusion:

```text
9 even/projective rows need no lift
11 odd rows all accept the selected-beat construction
beat compatibility selects 0 of the 20 rows
```

The beat is therefore a functorial compatibility mechanism after a stratum has been chosen.  It is
not a selector of the A1 landing, a fermion construction, or a generation theorem.

Wave 1 also independently reproduced local B1145 and typed paper B8129--B8133.  None moves the
physical critical path.  The separate audit registry now contains 81 questions:

```text
22 PROVED
29 REFUTED
13 CONDITIONAL
16 EXTERNAL_BLOCKER
1 EMPIRICAL
```

## Source lock

| source | immutable commit |
|---|---|
| public Origin main through B1142 | `d6eac1ed309a2b6eeb38cff4d6a01a0eacbe4593` |
| public outside-bench memo 30 | `22a8a1a4a21eb64919f00c52c5a5a26a2b77ad5f` |
| public paper branch through B8133 | `13f1c5d6f7172d715979c57fc7c9b9d53c5fa663` |
| public Golden memo/manifest branch | `15b3366937af19e643a54d564883253f013fc651` |
| local banking snapshot through B1145 | `9a4eca7ea48c92c2c86d1bd3d6eacff288bef13b` |

The local banking tree was read only.  Its commit is not represented here as a public head.

## C-P1: exact result and exact limitation

The locked `cp1_strata.py` has SHA-256
`8d3e7092d65803529ca68ef2c01b270d01f61871d84d9d7d606c9f1e63b71c46`.  An isolated rerun under
Python 3.12.1 and SymPy 1.14.0 exits zero and is byte-identical to the stored output.

The four accepted distinguished rows are:

| characteristic | orbit dimension | 27 parity |
|---|---:|---|
| `(0,0,0,2,0,0)` | 58 | even/projective |
| `(1,2,1,0,1,1)` | 64 | odd/lift-sensitive |
| `(2,0,0,2,0,2)` | 66 | even/projective |
| `(2,2,2,0,2,2)` | 70 | even/projective |

Every accepted label carries an exact bracket-verified `sl2` witness, so the positive rows are
sound.  The script does not independently prove absence for rejected labels.  Its
`is_characteristic(c, tries=4)` makes four seeded generic trials, then the certificate asserts that
the number found equals the known E6 nonzero-orbit count 20.  Failed random trials are not an
algebraic nonexistence proof.

Consequently:

- four distinguished positive rows and their dimensions/parities: exact;
- the accepted-list parity total `9 even + 11 odd`: exact;
- exhaustiveness of the list: conditional on the standard 20-orbit classification/count;
- “from first principles, no literature input”: not established.

The completeness statement can be promoted after either a deterministic algebraic rejection
certificate for all omitted labels or a precise, type-checked citation of the standard
classification theorem.  Importing the theorem is legitimate; hiding it as a mere control is not.

## New all-odd certificate

[`verify_cp1_all_odd.py`](codex-seat-r003/verify_cp1_all_odd.py) is the new independent
extension.  It refuses a source-hash mismatch, reruns the entire upstream certificate, finds every
accepted odd row from its exact 27 weights, and checks:

```text
relator = I
Omega^2 = A27
Omega gal(A27) Omega^-1 = A27
Omega gal(B27) Omega^-1 = rho27(B^-1 A B A^-1 B)
```

All four identities pass on all eleven odd accepted representatives.

Reproduce from a checkout/archive of the locked outside-bench commit:

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  documents/codex-seat-r003/verify_cp1_all_odd.py \
  /path/to/outside_bench/certificates/cp1_strata.py
```

The final line must be:

```text
ALL 11 ODD ACCEPTED CHARACTERISTICS PASS THE SELECTED-BEAT IDENTITIES
```

This closes the source certificate's all-odd computational coverage gap for the selected rational
representatives.  It does not classify all semilinear sections or change the 20-orbit completeness
dependency.

## Why this is a selector no-go

The source prose treats coverage of the odd side as strengthening the A1/fermion landing.  Exact
coverage says something different.  Because the same upstream `W=exp(qe)` mechanism works for all
eleven odd accepted triples, beat compatibility cannot distinguish the minimal A1 row from the ten
other odd rows.  The nine even rows already factor projectively and do not need the bit.

Thus the composition

```text
parity partition + selected beat
```

classifies how each already chosen row handles the lift, but chooses no row.  The A1 row remains
selected by a separate SM-compatibility criterion.  That is phenomenological filtering, not an
origin-derived unique landing.

## B1145 / SP-2

The local independent certificate reproduces:

- all `3003/3003` E6/27 Chevalley bracket identities;
- `27|A1 = 6*2 + 15*1`, or weights `6(-1)+15(0)+6(+1)`;
- nontrivial central parity, its square and centrality;
- the fixed relator and all three semilinear beat identities.

This is a good second implementation: it reuses banked B1102 machinery rather than the Golden
certificate.  The defensible theorem is:

> For the fixed matrix holonomy, fixed beat section, positive sign lift, and selected `ROOTS[0]`
> A1 embedding, the exact 27 module has six internal doublets and fifteen singlets and admits the
> stated semilinear beat action.

It does not construct:

- a lift of the tangent-frame/deck action to a specified spin or Pin group;
- a four-dimensional Lorentzian spin bundle or Weyl/Dirac field;
- a kinetic operator, action or Dirac index;
- net chirality or removal of the conjugate E8 branch;
- three physical copies of the 27;
- a source-native selector of the A1 row;
- all semilinear sections beyond the fixed-beat/scalar-rescaling problem.

Internal A1 doublets are not automatically Lorentz spinors.  The internal central element acts
nonuniformly across the 27, unlike the Lorentz spin central action on a spin factor.  Therefore the
matrix theorem should be banked, while “the beat reaches the fermions,” “generation's kinematic
seat closes,” and “zero free bits” should remain interpretation or be narrowed.

## Paper B8129--B8133

- **B8129:** three finite length cutoffs show no observed breakdown at `n=2,s=2`.  This is bounded
  numerical evidence, not convergence, order independence, or analytic continuation.
- **B8130:** the quadratic L-factor belongs to scalar cusp scattering, not a finite geodesic
  Ruelle factorization.  Independently, the m004 systole lies strictly between `log 2` and `log 3`,
  which refutes every finite product/ratio of shifted ordinary Dirichlet L-functions in the same
  variable by uniqueness of generalized Dirichlet series.
- **B8131:** the current `J3(O)`/“27-reality”/“64 fixed dimensions” Beilinson proposal is ill-typed.
  It specifies no arithmetic scheme or motive, class, degree/weight, Deligne target, lattice, or
  physical observable map.  The 64 is a sign-solution count, not a 64-dimensional space.  A
  well-typed replacement is a new external construction, not an unrun scalar integral.
- **B8132:** two spin structures occur for several family members.  The count is not m004-specific;
  a matrix sign choice still needs a typed map to the geometric spin torsor.
- **B8133:** Fried-type torsion at `s=0`, Pfaff ratios at positive `k>=3`, and the proposed tower
  starting at `n=2` are different evaluations and determinant problems.  None directly supplies
  the gauge-fixed cusped spin-2/vector/scalar graviton determinant.

## Banking disposition

Recommended narrow rows for integration:

| result | disposition |
|---|---|
| four distinguished positive rows and all-eleven-odd beat identities | PROVED |
| full 20-row completeness / total nine projective | CONDITIONAL on standard orbit count |
| beat as a unique stratum selector | REFUTED by compatibility with all odd rows and irrelevance on even rows |
| B1145 selected-A1 semilinear module theorem | PROVED narrowly |
| B1145 physical fermion/chirality/generation aggregation | NOT PROVED |
| finite shifted-Dirichlet-L Ruelle factorization | REFUTED |
| `n=2,s=2` convergence | EXTERNAL analytic blocker; finite evidence retained |
| direct torsion/scalar-cusp graviton feed | REFUTED as typed |
| actual cusped one-loop gravity determinant | EXTERNAL construction blocker |
| present Albert/Beilinson value route | REFUTED as ill-typed |
| newly specified Albert arithmetic/physical route | EXTERNAL construction blocker |

This branch remains integration-only.  The banking seat should re-run the new certificate, assign
its own arc identifier, narrow the physical prose, update all required surfaces, and cherry-pick or
reimplement the result rather than merge this branch wholesale.

## Next trunk work

Wave 2 should now begin on flavor:

1. finish the missing `1 x 18` down-Yukawa determinant/residue trace row;
2. construct the five chain-level Serre-dual tail representatives;
3. lift the relevant blocks exactly to `Q(zeta_12)`;
4. scout source-derived topology or extra-Higgs/vectorlike mixing alternatives for the up sector;
5. run the exact one-`H_u` no-go before spending on any candidate;
6. continue C0/C1 physical-realization work in parallel.

No new parity identity substitutes for those gates.
