# Height-308 down Yukawa: exact missing cyclic/Serre map

## Verdict

No numerical or exact `1 x 18` down-Yukawa row is present in the committed certificates.  The
existing artifacts prove the `33+5` presentation, characters, connecting representatives, and
finite-field Cech/exterior signs.  They do not construct the determinant comparison, normalized
Calabi--Yau trace, or chain-level Serre realization needed to evaluate a coupling.

This note fixes the type-correct formula and identifies one common missing artifact.  It is a
construction specification, not a claimed Yukawa value.

## Connecting representatives

Let

```text
L = O_Y(H),       Phi : G_Y -> L,       V = ker(Phi),
K = ker(G tensor L -> L^2) = V tensor L.
```

On each of the 432 refined opens choose

```text
s_alpha in G tensor L^-1,    Phi(s_alpha)=1,
theta_alpha,beta = s_beta-s_alpha in V tensor L^-1.
```

Define

```text
p(x wedge y) = Phi(x)y-Phi(y)x,
r_alpha(v tensor ell) = s_alpha wedge (v tensor ell).
```

Then `p r_alpha = 1_K`.  For `c_i in H0(L)` and `k_j in H0(K)`, the connecting
cocycles are

```text
a_i = delta(s c_i) in Z1(U,V),
b_j = delta r(k_j) in Z1(U,Lambda2 V),

(a_i)_alpha,beta = theta_alpha,beta c_i,
(b_j)_alpha,beta = theta_alpha,beta wedge k_j.
```

## Determinant and trace

The ordered twelve-ray frame and ordered six-Euler frame must induce a fixed comparison

```text
Delta_G : det(G) ~= L.
```

It gives the local expression

```text
epsilon(v1 wedge ... wedge v5)
  = Delta_G(v1 wedge ... wedge v5 wedge s_alpha),
epsilon : Lambda5 V ~= O_Y.
```

The expression is independent of `alpha`, but this independence and its equivariant phase must be
certified in the actual Cox/Euler frames.  With a normalized trace

```text
Tr_(Y,Omega) : H3(Y,O_Y) -> Q(zeta_12),
Omega_Y = Res_Z(Omega_Z/f),
```

the desired entries are

```text
T_i,j,k = Tr_(Y,Omega)(epsilon(a_i cup b_j cup b_k)),

(a_i cup b_j cup b_k)_alpha,beta,gamma,delta
 = (a_i)_alpha,beta wedge (b_j)_beta,gamma wedge (b_k)_gamma,delta.
```

Interchanging the two degree-one `B` inputs changes sign.  In the selected connecting bases,

```text
i = 1..3 for A_7,
j = 1..2 for B_6 (33-column indices 17,18),
k = 1..3 for B_2 (33-column indices 6,7,8),
```

so this formula is exactly a `1 x 18` row.  The raw characters sum to
`7+6+2=3 mod 12`; equivalently, the determinant comparison carries `chi_-3`.  After applying the
physical shifts `(+1,-2,-2)`, the product is invariant.  The compensating phase must not be applied
twice.

## Tail realization

The five printed tail rows are elements of `(coker D)^*`, not
`Lambda2(V)`-valued Cech cocycles.  A tail insertion needs a chain-level Serre map

```text
S : (coker D)^* -> Z1(U,E),       E=Lambda2 G_Y.
```

For `e_r=S(q_r)`, solve

```text
delta h_r = p(e_r),       h_r in C0(U,K),
```

using `H1(K)=0`, and set

```text
bhat_r = e_r-delta r(h_r) in Z1(U,Lambda2 V).
```

The same `T(a,b,b')` formula then accepts connecting or tail inputs.  For the physical selected
block,

```text
B_6 = B_6,conn^2 + <bhat_6>,
B_2 = B_2,conn^3 + <bhat_2>.
```

The full block therefore has 36 entries:

```text
18 conn/conn + 9 tail6/conn + 6 conn/tail2 + 3 tail6/tail2.
```

For general raw characters with `A_7`, selection requires `rho+sigma=8 mod 12`.  The pure-tail
pairs are `(0,8)`, `(2,6)`, and `(4,4)`; the repeated one-dimensional `(4,4)` direction vanishes by
skewness.

## Single next artifact

The smallest honest implementation is a normalized cyclic/Serre quasi-isomorphism

```text
Tcal : Tot Cech(U, monad exterior complex) -> Q(zeta_12)[-3]
```

whose components include `Delta_G`, `Tr_(Y,Omega)`, and the Serre-adjoint `S`.  Construct it
character by character using the idempotents

```text
e_r = (1/12) sum_(m=0)^11 zeta^(-rm) g^m.
```

The `18 -> 21` map then splits into small blocks.  Work first over `Q(zeta_12)`, localized away
from explicit denominators and 1009.  A nonzero pivot modulo 1009 certifies a corresponding
characteristic-zero rank lower bound, but a finite-field scalar is not a characteristic-zero
residue value.

## Reproduced record discrepancy

Running `certify_yukawa_down_tail_cech_308.sage` on 2026-08-25 reproduces rank 16, coker dimension
5, raw labels `(0,4,6,8,10)`, and dual tail labels `(0,2,4,6,8)`.  Its emitted coordinates disagree
with `certify_yukawa_down_tail_cech_308.md` in two rows:

```text
tail 0 runtime: e_0-e_11       markdown: e_0-e_7
tail 6 runtime: e_2-4e_17-6e_18
       markdown: e_2-4e_15-6e_16 (only 20 coordinates, not 21)
```

Rows 2, 4, and 8 agree.  A separate consistency certificate proves that the documented tail-0 row
fails both its annihilator and phase equations in the current basis, while documented tail 6 is
not even dimensionally well formed.  The executable rows satisfy all defining identities and are
the source of truth for this certificate version.  The Markdown record has now been regenerated;
the consistency certificate retains the stale coordinates as failing controls and this discrepancy
remains recorded as provenance.

## Proof boundary

- Proved: source/target dimensions, rank `16`, `33+5` decomposition, character blocks,
  connecting representatives, and the scoped Cech/exterior sign identities.
- Not proved: any nonzero down-Yukawa entry, rank, texture, determinant, normalized residue, or
  tail-coupled value.
- Next proof obligation: the exact `Q(zeta_12)` cyclic/Serre augmentation above, followed by an
  explicit row and Wilson-restricted rank calculation.
