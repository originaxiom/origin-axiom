# B1333 addendum — isotropy is a ONE-CUSP phenomenon: B1332's reduction does not generalise

This corrects B1332 and B1331, both authored on this bench the day before.

## What B1332 claimed

> *If `L_V` is **isotropic**, then `L_V ⊆ L_V^perp = L_{V*}`, so `dim L_V <= t_1/2` … **`I = 0` follows
> from isotropy alone.** The whole theorem is one question: **is `L_V` isotropic?***

The **implication** is sound and stands. What does not stand is treating it as *the* theorem — and
B1331's stronger reading, that `L_V` and `L_{V*}` are **the same subspace**.

## The test

Cusp-triviality makes the cusp matrices identical across the whole cusp-trivial character family, so
`L_psi` and `L_{psi^-1}` are subspaces of one space and compare directly. Two independent quantities
are computed per sector: whether the subspaces coincide, and whether the cup-product Gram on `L_psi`
vanishes (the pairing on `H^1(dM;W)` being the **sum** of the per-torus pairings). Given equal
dimensions the two are equivalent, so agreement between them is a check on the code.

**Control first.** The same code, run on the one-cusped `s958` and `t12833`:

```
s958   Sym^2      t0s=[1] t1=2 r1=1 I=0 | L==L*: True | ISOTROPIC: True
s958   Sym^2+Sym^2 t0s=[2] t1=4 r1=2 I=0 | L==L*: True | ISOTROPIC: True
t12833 both germs                        | L==L*: True | ISOTROPIC: True
```

It reproduces B1332. So what follows is not a bug in the multi-cusp pairing.

## The result

40 sectors across 14 chiral multi-cusped covers of `m004` (2 and 3 cusps), exact over `Q(zeta_12)`:

| | count |
|---|---|
| `I = 0` | **40 of 40** |
| `L_psi` **isotropic** | **4 of 40** |
| `L_psi = L_{psi^-1}` | **4 of 40** |

The last two agree in all 40 rows, as they must.

> ## With several cusps `L_V` is usually **not** isotropic and `L_V != L_{V*}` — and the index
> ## vanishes anyway, in every sector.

## What this changes

- **Isotropy is sufficient but NOT necessary.** B1332's implication is fine; its reduction is not an
  equivalence. Proving `L_V` isotropic would prove the **one-cusped** case and nothing more.
- **B1332 §2–§3 are one-cusp statements.** "`L_V` is Lagrangian", the form-free cup vanishing, and
  the whole isotropy framing hold at one cusp and fail at two. They should be read with that scope.
- **B1331 §2 is likewise one-cusp.** "Not merely equal in dimension — **identical**" is false for
  several cusps: the dimensions still agree (hence `I = 0`), the subspaces do not.
- **The vanishing is more robust than any mechanism yet proposed for it.** Galois was ruled out
  (B1331 §3), strong cusp-locality was ruled out (B1332 addendum), and now isotropy is ruled out as
  the *general* reason. The index keeps vanishing while every proposed explanation for it fails.

That last point is the honest headline, and it cuts both ways: it is evidence that a vanishing
theorem exists, and evidence that this bench does not yet have its proof.

## What to prove now

Not "is `L_V` isotropic?" — that question is settled (sometimes yes, sometimes no) and does not
decide the theorem. The surviving question is the original one, unreduced:

> **why is `dim L_V = dim L_{V*}`** — i.e. `r_1 = r_1^*` — when the subspaces themselves differ?

Reproduce: `verification/mccup.py <tags>` (the multi-cusp isotropy and subspace test),
`verification/mccup_ctrl.py <manifolds>` (the one-cusped control — run this first),
`verification/orbit.py <tag>` (the fibres of `psi |-> L_psi`). Logs in `verification/logs/`.
