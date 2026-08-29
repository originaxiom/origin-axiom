# R026 — explicit height-308 Yukawa determinant frame

## Verdict

The determinant comparison named as missing in the height-308 down-Yukawa
specification is constructible from data already fixed by the branch. Relative
to the ordered twelve Cox rays, the integral Euler basis, the selected six
Euler characters and the marked `C12` generator, R026 gives a reproducible
exact frame

```text
Delta_G : det(G) -> L,
epsilon : Lambda^5(V) -> O_Y.
```

It also collapses every connecting-sector local cup term to one sparse
`12 x 12` determinant with a proved positive sign. The determinant step is
therefore no longer the computational obstruction to the `1 x 18` row.

This does **not** evaluate that row. The hypersurface connecting trace
`H^3(O_Y) -> Q(zeta_12)` and the chain-level Serre-tail lift remain absent,
and physical Yukawas additionally require matter metrics and a selected
vacuum.

## Exact frame

Write

```text
0 -> W=6 O_Y -> B=sum_i O_Y(D_i) -> G -> 0,
0 -> V -> G -> L=O_Y(H) -> 0.
```

The selected branch has ordered Euler characters

```text
W: (0,2,6,8,9,10).
```

R026 reconstructs the integral `12 x 8` Euler matrix and its exact order-12
action. For every one-dimensional character line it applies the Fourier
projector

```text
P_q = (1/12) sum_(m=0)^11 zeta^(-qm) G_Euler^m
```

to the earliest nonzero integral Euler anchor, maps the result into the
ordered twelve-ray frame and normalizes its earliest nonzero ray coefficient
to one. This fixes both the order and scale of the six Euler columns over
`Q(zeta_12)` without relying on Sage's choice of a kernel basis.
If `U_(i,q)` is the resulting coefficient matrix, the actual sheaf column is

```text
w_q = sum_i U_(i,q) x_i e_i,
```

with `x_i` the canonical Cox section of `O(D_i)`; the certificate's exact
matrix is this coefficient frame, not a replacement of the Cox sections by
numbers.

As a nonvanishing exact pivot, the six-by-six Euler minor on ordered ray rows
`(0,1,2,3,6,7)` is

```text
-72 zeta^2
```

in this normalization. Thus the chosen six-frame is certified already in
characteristic zero; the good-prime calculation is a separate control.

If `w_1,...,w_6` are those columns and `g_1,...,g_6` are sections of `G`
with arbitrary lifts to `B`, define

```text
Delta_G(g_1 wedge ... wedge g_6)
  = det_B(w_1,...,w_6,gtilde_1,...,gtilde_6).
```

Here the ordered determinant of `B` is identified with
`L=O_Y(sum_i D_i)`. Changing any lift by a `W`-column inserts a repeated
direction, so the expression is lift-independent. Changing the chosen
splitting of `G -> L` changes it by a sixth `V` direction; this also vanishes
because `rank(V)=5`.

The equivariant ledger closes independently. The twelve-ray permutation is a
single 12-cycle, hence `det(B)` has character 6. The selected six Euler lines
have determinant character

```text
0+2+6+8+9+10 = 11 mod 12,
```

so `det(G)` has character `6-11=7`, equal to the omitted pair `3+4`. The
unique BCDD determinant-restoring twist solves

```text
5 t + 3 + 4 = 0 mod 12,
```

namely `t=1`; the twisted rank-five determinant character is therefore zero.

## Sparse connecting formula

On four refined opens put `s_a=e_a/Phi_a` and
`theta_ab=s_b-s_a`. With `c in H^0(L)` and
`k_1,k_2 in H^0(V tensor L)`, the local connecting term is ordered as

```text
theta_ab*c wedge theta_bc wedge k_1 wedge theta_cd wedge k_2.
```

Using `s_a` as the sixth determinant direction, exterior multilinearity gives
the exact identity

```text
(s_b-s_a) wedge (s_c-s_b) wedge k_1
  wedge (s_d-s_c) wedge k_2 wedge s_a
= s_a wedge s_b wedge s_c wedge s_d wedge k_1 wedge k_2.
```

The sign is `+1`. Consequently the degree-zero rational Cech cochain is

```text
c * det_B(w_1,...,w_6,e_a,e_b,e_c,e_d,ktilde_1,ktilde_2)
  / (Phi_a Phi_b Phi_c Phi_d).
```

Here, in a local frame `ell` of `L`, `ktilde_j` is a `B`-lift of
`k_j/ell in V`. The two resulting `ell` factors and the four inverse-`L`
splitting factors leave one inverse `L`, which the section `c` cancels. This
is substantially smaller than expanding three transition differences. It is
also independent of the two `B`-lifts.

The certificate proves the exterior identity formally, constructs the exact
cyclotomic Euler eigenframes using a standard-library implementation of
`Q[zeta_12]`, and runs a nonzero good-prime control in the actual selected
six-column quotient frame. The control is deliberately nonzero so a broken
sign or fake lift-invariance cannot pass vacuously.

## Remaining trace map

The next finite construction is now sharply isolated. Since
`H=-K_Z` and `Y=(f=0)`, the restriction sequence gives

```text
delta_f : H^3(Y,O_Y) -> H^4(Z,K_Z).
```

For `Z=dP6 x dP6`, both sides are one-dimensional and `delta_f` is an
isomorphism. A connecting cochain can be lifted off `Y`; its Cech differential
is divisible by `f`, and division by `f` gives a top canonical-bundle cocycle.
Reducing that cocycle against the product of the two normalized `dP6` top
classes produces the missing scalar. Overall nonzero trace normalization is
irrelevant to tensor rank, though it matters for exact holomorphic coordinates
and does not replace physical Kähler normalization.

The [generalized ambient-type vanishing theorem](https://arxiv.org/abs/2103.10454)
is not a shortcut here: it is formulated for a same-bundle `SU(3)` cubic with
the bundle at the quotient end of a resolution. This is the mixed `SU(5)` product
`H^1(V) x H^1(Lambda^2 V)^2`, and `V` is the kernel in
`0 -> V -> G -> L -> 0`. No required mixed-resolution vanishing is established.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r026_yukawa_determinant_frame/determinant_frame.py
```
