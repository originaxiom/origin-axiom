# Main delta audit: B1146 and B1147

**Audit date:** 2026-08-26

**Immutable main source:** `9d6979db424c0b878c62541a3f21e0a2ca39f274`

**Outside source through memo 40:** `dc937010132e913db66ccb6e915df490ac185577`

**Method:** clean-tree inspection plus independent exact reruns; no write to `main`

## Verdict first

B1146 contains a genuine correction.  The old statement that the relevant `2T` action factors
through `A4` was true only for the principal-A1 adjoint frame.  On the selected minimal A1 the
complete restrictions are

```text
27:  {-1: 6, 0: 15, 1: 6}                 -> 12 odd states
78:  {-2: 1, -1: 20, 0: 36, 1: 20, 2: 1} -> 40 odd states
```

Thus the central `-I` of `2T` is visible on both representations.  This closes OA-C1079 and
repairs OA-C0006's evidence.  It does **not** select the minimal A1 from the surviving menu and it
does not identify an internal central action with four-dimensional fermion parity.

B1147's mathematical harvest is mostly reproducible, but its clean-lock record is not
self-contained.  The immutable commit requires
`frontier/B1147_clane_harvest/verification/reproduce.log`; that file is absent.  Running its exact
test from a clean archive therefore gives `1 failed, 4 passed` with `FileNotFoundError`.  This is
OA-C1091: a record defect, not a refutation of the separately rerun memo certificates.

## Memos 31-40: narrow dispositions

| memo | campaign row | hostile disposition |
|---:|---|---|
| 31 | OA-C1068 | `PROVED`: marked peripheral action is exactly `diag(1,-1)`, determinant `-1`, order `2`. |
| 32 | OA-C1065 | `PROVED`: the selected cubic invariant line is one-dimensional and covariant for the fixed beat linearization. |
| 33 | OA-C1066 | `PROVED`: rational `T` closes on the full specified basis. OA-C1067 stays `OPEN`: this is not the complete semilinear-Sigma action. |
| 34 | OA-C1070 | `PROVED`: parity redundancy holds for integral E6 characteristics. Completeness of the inherited 20-row orbit census stays conditional in OA-C1058. |
| 35 | OA-C1073 | reproduced symmetric counts; an independent ordered-tensor computation below closes the broader row. |
| 36 | OA-C1069 | partial only: the `H^1` linear restriction is zero, but the geometric Pin-minus obstruction and affine torsor have not been constructed. |
| 37 | OA-C1078 | `REFUTED`: the unoriented peripheral character is generically two-to-one; oriented `L` versus `L^-1` can retain the missing bit. |
| 38 | OA-C1074 | stays `OPEN`: the leading coefficient and a 108-zero scan reproduce, but no explicit argument-principle error bound is proved. |
| 39-40 | OA-C1075 | `PROVED` only on the frozen finite domains: the naive rung-to-rung tower has valuation exactly 2 in six cells; Taylor-to-germ coherence has valuation at least `N` in all 24 cells. No universal p-adic theorem follows. |
| C3 i9 run | OA-C1076 | `REFUTED` for the preregistered protocol: about 17/13 stable digits, not the required 60, through `N<=4000`. This is not a no-go for every asymptotic method. |
| C4 | OA-C1077 | `OPEN`: the large-T GUE computation has not landed in the audited source. |

## Independent exact invariant closure

`experiments/certify_e6_27_invariants.sage.py` was rerun independently against the locked E6/27
implementation.  It gives

```text
dim Sym^d(27*)^E6, d=1,2,3,4: 0, 0, 1, 0
degree-3 Cartan-zero basis / exact rank: 45 / 44
dim (27 tensor 27 tensor 27)^E6: 1
selected A2^3 ordered / symmetric invariants: 9 / 4
```

All 72 root generators and six Cartans annihilate the normalized 45-term cubic.  Exact
semilinear coefficient comparison gives covariance scalar `1` for the locked
`Omega=exp(q rho(E)) o gal`.  Rescaling `Omega` by `lambda` changes this scalar by `lambda^3`, so
the value is a linearization convention, not a new object-selected number.  This closes OA-C1072
and OA-C1073, and sharpens OA-C1065's scope.

## Exact parity lemma

`experiments/oa_c1070_omega1_parity.py` reruns the locked 20 rows and checks all 64 even-label
vectors.  If `c=A t` is even and `t` is an integral E6 coroot characteristic, the E6 Cartan matrix
is invertible modulo two, hence `t` is even and every 27 weight has even pairing.  Arbitrary even
labels are insufficient: `c=(2,0,0,0,0,0)` gives `t_1=8/3`.  The integral-characteristic
hypothesis is therefore necessary and explicit.

## Physics fence

None of these cells supplies a four-dimensional QFT functor, tangent spin structure, chiral index,
vacuum, physical Yukawa cup product or normalized Standard-Model value.  They strengthen the
structure layer and close several finite algebra questions; they do not cross the physics bridge.
