# B1334 — a proof of `I = 0`, where a deformation exists: generic rank plus inversion symmetry

**Verdict: PROVED**, on a stated and narrow domain. This is the record's first *proof* of the index
vanishing rather than a computation of it — and it needs none of the three mechanisms this bench
proposed and then killed.

## The theorem

Let `M` be a cusped hyperbolic 3-manifold with `dM = T_1 u ... u T_c`; let `W` be a local system
whose restriction to `dM` is self-dual (`Sym^m` of an `SL2` holonomy qualifies); let

```
S  = Hom( H_1(M) / <peripheral curves> , C* )      the cusp-trivial characters
S^0 = its identity component, a torus of dimension  rank( H_1(M)/<peripheral> )
```

> ### For every `chi` in `S^0`:  `I(W (x) chi) = 0`.

## The proof

1. **`t_0`, `t_0*`, `t_1` are constant on `S`.** `chi` is cusp-trivial, so `(W (x) chi)|_{dM} = W`
   for every `chi` — the cusp matrices never move. `W|_{dM}` self-dual gives `t_0 = t_0*`, and with
   B1297's `t_1 = t_0 + t_0*`, **`t_0 = t_1/2`**.
2. **`r_1` is lower semicontinuous on `S^0`.** `r_1(chi) = rank(R(chi) + Bt) - rank(Bt)`, where `Bt`
   is built from the cusp matrices and so is *constant* by (1), and `R(chi)` has entries that are
   Laurent polynomials in the torus coordinate (Fox calculus). The locus `rank <= k` is closed, so
   `r_1` attains its **maximum** `rho` on a Zariski-open dense `U ⊆ S^0`.
3. **`r_1(chi) + r_1(chi^-1) = t_1`** for every `chi` — Poincare–Lefschetz on `(M,dM)`: `L_V` and
   `L_{V*}` are mutual annihilators. (B1297's first identity; verified in every sector below.)
4. **`U` meets `iota(U)`.** Inversion `iota: chi -> chi^-1` is an automorphism of the torus `S^0`,
   so `iota(U)` is Zariski-open dense too, and `S^0` is **irreducible**, so two dense opens meet.
5. **`rho = t_1/2`.** Take `chi in U n iota(U)`: then `r_1(chi) = rho` and, since `chi^-1 in U`,
   also `r_1(chi^-1) = rho`. By (3), `2 rho = t_1`.
6. **Every `chi`, not just the generic one.** For any `chi in S^0`, (2) gives `r_1(chi) <= t_1/2`
   and `r_1(chi^-1) <= t_1/2`, and (3) makes them sum to `t_1`. So **both equal `t_1/2`**.

With (1), `I = t_0 - r_1 = t_1/2 - t_1/2 = 0`. ∎

## Why this is the right shape

The evidence had already killed every mechanism proposed for the vanishing, and this proof uses
none of them:

| proposed mechanism | status | used here? |
|---|---|---|
| Galois conjugation carries `V` to `V*` | ruled out — the targets are **chiral** (B1331 §3) | no |
| the cusp data determines `L_V` | ruled out — `L_psi` moves with `psi` (B1332 add.) | no |
| `L_V` is isotropic / Lagrangian | ruled out as general — fails in 36 of 40 multi-cusp sectors (B1333 add. 2) | no |

It needs only an identity that is **symmetric under inversion** and a family **irreducible** enough
for genericity to bite. That is exactly why it survives chirality, survives non-isotropy, and
survives `L_V != L_{V*}`: **only the dimensions ever enter.**

And it says why cusp-triviality was never optional — step (1) is where it does its work, holding
`t_1` still while `chi` moves.

## Where it applies, and the two covers

Non-vacuous exactly when `dim S^0 > 0`. Across `m004`'s 54 chiral multi-cusped covers to degree ten,
computed here:

```
dim S = 0  for 52 covers      (b_1(M) equals the peripheral rank)
dim S = 1  for  2 covers      d10_4 and d10_35, both 3-cusped, b_1 = 4
```

On both, the cusp-trivial order-3 characters are **exactly** the cube-root-of-unity points of `S^0`:

| | free direction `phi` | order-3 cusp-trivial characters | cube-root points of `S^0` |
|---|---|---|---|
| `d10_4` | `[0,1,0,1]` | `(0,0,0,0), (0,1,0,1), (0,2,0,2)` | **identical** |
| `d10_35` | `[0,1,1,0]` | `(0,0,0,0), (0,1,1,0), (0,2,2,0)` | **identical** |

So on these two members of the object's own tower the theorem covers **every twist the programme
uses**, and `I = 0` there is now proved, not observed.

## The numerical confirmation, which the proof did not need

Every step is checked at 36 points of the family (all of `F_37^*`), on both covers, both germs:

```
d10_4    Sym^1  t0=0 t1=0 r1=0 I=0    t_1 constant: True | r_1 constant: True   x36
d10_4    Sym^2  t0=3 t1=6 r1=3 I=0    t_1 constant: True | r_1 constant: True   x36
d10_35   Sym^1  t0=2 t1=4 r1=2 I=0    t_1 constant: True | r_1 constant: True   x36
d10_35   Sym^2  t0=3 t1=6 r1=3 I=0    t_1 constant: True | r_1 constant: True   x36
```

`r_1 = t_1/2` at every sampled point, the four identities intact at every one, zero skips.

## What this does NOT prove, stated plainly

**The cases the programme most needs are not covered.** `dim S = 0` for 52 of the 54 covers and for
**every one-cusped manifold** — including `m004` itself and B1330's targets `s958`, `t12833`,
`t12835` — because there `b_1(M)` equals the peripheral rank and `S` is a **finite** group. A finite
set has no Zariski-dense proper open subset, so steps (2), (4) and (5) have nothing to stand on.
The vanishing there remains observed and unproved.

So this is a proof exactly where a deformation exists, and it converts the open problem into a
sharper one:

> **Find a substitute for Zariski density when `S` is finite** — some other symmetry or rigidity
> that forces `r_1 = r_1^*` at an isolated character. Inversion is still available there as a
> symmetry of the *identity*; what is missing is a connected family for it to act on.

Reproduce: `verification/family.py` (dimensions of `S` for every cover),
`verification/famtest.py <tags>` (the family sampled at every point of `F_p^*`). Logs in
`verification/logs/`.
