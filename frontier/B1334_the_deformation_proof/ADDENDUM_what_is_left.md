# B1334 addendum — the map of what is left, and a no-go for the one-cusped case

## 1. Where `dim S > 0` can possibly hold

Half-lives-in-half-dies makes the peripheral image in `H_1(M;Q)` of rank `c`, so

```
dim S  =  b_1(M) - c
```

and the deformation proof applies **exactly when `b_1 > c`**. That is a condition a *one-cusped*
manifold can meet, by having `b_1 >= 2` — so the method is not intrinsically multi-cusped.

Every cover of `m004` to degree ten, one-cusped ones included:

```
(cusps, b_1, dim S) -> count
 (1,1,0) -> 23     (2,2,0) -> 27     (3,3,0) -> 25
 (3,4,1) ->  2     (4,4,0) ->  7     (5,5,0) ->  3
```

**All 23 one-cusped covers have `b_1 = 1`.** Within the object's tower to degree ten the proof
reaches exactly `d10_4` and `d10_35`.

## 2. A no-go: no character deformation can ever reach a one-cusped manifold

Peripheral holonomy is unipotent, so `Sym^m(rho(mu))` has every eigenvalue `1`, and twisting by
`chi` makes every eigenvalue `chi(mu)`. An invariant vector needs eigenvalue `1`, so

```
t_0 > 0   <=>   chi(mu) = chi(lam) = 1   <=>   chi is cusp-trivial
```

and by T5 (`t_0 = 0 => I = 0`) the index is **identically zero off the cusp-trivial locus**.
(This is the prediction B1333 tested: zero violations in 38070 sectors.)

So the entire content of the index sits on `S`. For a one-cusped manifold with `b_1 = 1`, `S` is a
**finite** group, and:

> **The whole content of the index on a one-cusped manifold lives at finitely many rigid
> characters. No deformation argument in the character direction can reach it — not because the
> right family has not been found, but because the locus carrying the content is zero-dimensional.**

Deforming `rho` instead does not help either: moving off the parabolic locus makes the peripheral
holonomy loxodromic, `t_0` drops to `0`, and `T5` makes the index vanish trivially. The parabolic
point is exactly the rigid one, and it is where all the content is.

## 3. The map: which route covers what

Two routes exist. They are **independent** — neither subsumes the other:

| class | route | status |
|---|---|---|
| `dim S > 0` | deformation (B1334) | **PROVED** |
| `dim S = 0`, `L_V` isotropic | isotropy ⇒ `I = 0` (B1332 §1) | reduces to proving isotropy |
| `dim S = 0`, `L_V` **not** isotropic | **neither** | **open** |

Applied to the 14 chiral multi-cusped covers surveyed exactly over `Q(zeta_12)`:

| cover | cusps | `dim S` | isotropic | route |
|---|---|---|---|---|
| `d10_4`, `d10_35` | 3 | **1** | **0 of 2** | deformation |
| `d8_7` | 2 | 0 | 2 of 2 | isotropy |
| `d6_2 d6_3 d6_7 d6_8 d8_3 d8_4 d8_6 d9_1 d9_3 d9_4 d9_5` | 2–3 | 0 | 0–2 of 8 | **NEITHER** |

**2 proved, 1 reduced, 11 uncovered.**

The complementarity is worth seeing: on the two covers where the deformation proof works, isotropy
**fails** — so B1334 is not a dressed-up isotropy argument. And at every one-cusped manifold isotropy
**holds** (B1332, reconfirmed as the control in B1333 add. 2) while deformation fails. The two routes
cover disjoint ground and together still miss the majority of the multi-cusped covers.

## 4. What this makes of the open problem

It splits cleanly in two, and they need different things:

1. **One cusp** — including `m004` itself and B1330's targets `s958`, `t12833`, `t12835`. Here
   §2's no-go closes the deformation direction permanently, and isotropy empirically holds. So the
   whole one-cusped case reduces to B1332's form-free statement: **prove `L_V u L_V = 0` in the
   `SL2`-visible part of `H^2(T;W (x) W)`.** That remains the right target, and it is now known to
   be the *only* live route for the case the programme actually needs.
2. **Several cusps with `dim S = 0` and isotropy failing** — 11 of 14 surveyed. Neither route
   applies and no third one is in hand. This is the genuinely open case, and it is the common one.

Reproduce: `verification/b1scan.py` (the `(cusps, b_1)` census of every cover to degree ten),
`verification/family.py`, `verification/famtest.py`. Logs in `verification/logs/`.
