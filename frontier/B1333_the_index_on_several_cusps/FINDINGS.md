# B1333 — the index on several boundary tori: derived, verified, and the blocker cleared

**Verdict: PROVED, instrument.** The *derivation* is the deliverable and it is complete and verified;
the *evaluation* it enables is running and is recorded in an addendum, not claimed here.

§14 of THE PAPER names one thing standing between the programme and its own upgrade trigger:

> *the $54$ multi-cusped chiral covers to degree ten are named, but **the index on several boundary
> tori must first be derived from the same pair sequence** before it can be evaluated there.*

This arc does that derivation, verifies it, and reproduces the targets. The evaluation follows.

---

## 1. The derivation — every step checked against the cusp count

B1297 derived, for `M` one-cusped with cusp torus `T`:

```
n(V) := dim im(H^1(M,T;V) -> H^1(M;V)) = a_1 - r_1
I(V) := n(V) - n(V*)                   = (a_0 - a*_0) + t*_0 - r_1
in domain D (a_0 = a*_0, t_0 = t*_0):   I = t_0 - r_1
```

Take `dM = T_1 u ... u T_c` and set `t_k := sum_i h^k(T_i;V)`. The derivation uses exactly five
inputs. Each is checked for a hidden dependence on `c = 1`:

| | input | survives `c > 1`? |
|---|---|---|
| (1) | `a_3 = 0` — `M` is homotopy equivalent to a 2-complex | yes, no cusp count enters |
| (2) | `a_0 - a_1 + a_2 = 0` — `chi(M;V) = d·chi(M) = 0` | yes |
| (3) | `a_2 = b*_1` — Poincare–Lefschetz `H^k(M;V) = H^{3-k}(M,dM;V*)^*` | yes |
| (4) | `b*_1 = (t*_0 - a*_0) + n(V*)` — exactness, **using `H^0(M;V*) -> H^0(dM;V*)` injective** | **yes**: the map is `v |-> (v,...,v)` on `c` components and `M` is connected |
| (5) | `r_1 + r*_1 = t_1` — `L_V` and `L_{V*}` are mutual annihilators | **yes**: the pairing on `H^1(dM)` is the direct sum of the per-torus pairings, and a direct sum of perfect pairings is perfect |

(4) and (5) are the two that could have failed, and neither does. So **the formula is unchanged**:

> ## `I(V) = (a_0 - a*_0) + t*_0 - r_1`, and in `D`, `I = t_0 - r_1 = sum_i t_0^(i) - r_1`.

## 2. What *does* change, and it is not nothing

- **Coboundaries become a direct sum.** `B^1(dM;V) = (+)_i B^1(T_i;V)` — each torus carries its own,
  so `dim B^1(dM) = sum_i (d - t_0^(i))`, not `d - t_0`. Code that reuses a single-cusp coboundary
  space silently computes the wrong `r_1`; this is the one place a naive extension breaks.
- **Isotropy becomes a condition on a sum.** B1332 reduced `I = 0` to `L_V` being Lagrangian. With
  several tori the pairing is `sum_i` of the per-torus pairings, so it can vanish by **cancellation
  between cusps** — impossible with one cusp, and the only structurally new phenomenon here.

## 3. A prediction the derivation makes, and it is tested not assumed

Peripheral holonomy of a cusped hyperbolic manifold is **unipotent**, so `Sym^m` of it has every
eigenvalue `1`; multiplying by a primitive cube root of unity leaves no eigenvalue `1`. Hence at a
cusp where `psi` is **non**-trivial, `t_0^(i) = t*_0^(i) = 0`, so `t_1^(i) = 0` and that cusp
contributes nothing to `t_0`, `t_1` or `r_1`.

> **The index sees only its LIVE cusps** — those where `psi` is trivial. B1332's mechanism applies at
> each of them, so cancellation between cusps needs **at least two live cusps**. That is the sector
> to aim at, and the runs report it per row.

The runs check the prediction directly (a live cusp where `psi` is non-trivial would be a violation)
rather than taking the argument's word.

## 4. Verification of the derivation

Representations are found **honestly** — enumerate `rho: pi_1 -> SL2(F_q)` and keep the tuples that
kill every relator — then twisted by `F_q^x` characters (a self-dual `V` gives `I = 0` by T3 and
would test nothing) and pushed through `Sym^m`.

| | manifolds | sectors | identity failures |
|---|---|---|---|
| one-cusped control (must reproduce B1297) | `m004`, `m003` | 132 | **0** |
| two-cusped | `m129` alone | 96 | **0** |
| two-cusped | 30 census manifolds `m125`–`s602` | 3304 | **0** |

Identities checked on every sector: `r_1 + r*_1 = t_1`, `t_1 = t_0 + t*_0`,
`I = (a_0 - a*_0) + t*_0 - r_1`, `I(V*) = -I(V)`. Of the 3304 two-cusped sectors, **274 are live**
(`t_0 >= 1`; T5 forces `I = 0` when `t_0 = 0`, so the rest test nothing), 182 of those with
`t_0 >= 2`. **All returned `I = 0`.**

**The strongest check is an exact reproduction.** Run at `c = 1` on `s958` over `Q(zeta_12)`, the
multi-cusp code must agree sector-for-sector with B1332's already-validated one-cusp code. It does:

| | `t_0=1,t_1=2,r_1=1` | `t_0=2,t_1=4,r_1=2` | `t_0=3,t_1=6,r_1=3` |
|---|---|---|---|
| `iso.py` (one-cusp, validated) | x6 | x9 | x3 |
| `mcexact.py` (multi-cusp, `c=1`) | **x6** | **x9** | **x3** |

All 18 rows identical, `I = 0` throughout. The generalisation did not perturb the special case.

A guard is built in: a run that tests **no** sector reports failure, not success. It fired once
during development, when the first rep-finder returned nothing and the validator cheerfully printed
"all identities hold" over an empty set.

## 5. The targets, reproduced independently

`m004`'s multi-cusped covers to degree ten, chirality by `symmetry_group().is_amphicheiral()` (the
orientation-*aware* test; `is_isometric_to(mirror)` is orientation-blind and that error is on this
record):

```
multi-cusped covers to degree 10 : 64
of which CHIRAL                  : 54      <- matches THE PAPER's count exactly
by (degree, cusps): (5,2):2 (6,2):6 (7,3):4 (8,2):4 (9,3):6 (10,2):10 (10,3):14 (10,4):6 (10,5):2
```

**51 of the 54 are recognised exactly over `Q(zeta_12)`**, and every relator evaluates to `+-I`
(no exceptions) — so the evaluation runs on exact arithmetic on the object's own tower, not on
floating point. Three resist PSLQ at 60 digits and are recorded as unrecognised rather than
approximated.

Where a cover's lift is projective (`-I` on some relator), only **even** germs are valid, since
`Sym^even(-I) = +I` — the guard from B1330 addendum 2, which fired again here.

---

## Reproduce

- `verification/mc_lib.py` — the derivation, with each step's cusp-count dependence in the docstring
- `verification/mc_val.py <manifold>` — identity verification on honest `SL2(F_q)` reps
- `verification/mc_scan.py <manifolds...>` — the general question, any manifold
- `verification/covers.py` — enumerate and classify `m004`'s multi-cusped covers
- `verification/covrecog.py` — exact `Q(zeta_12)` recognition of the 54
- `verification/mcexact.py`, `verification/mcrun.py` — the exact evaluation on the covers

Logs in `verification/logs/`.
