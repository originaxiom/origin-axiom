# Exact-spectrum up-Yukawa no-go for the BCDD monad

**Campaign item:** `OA-C1055`  
**Audit date:** 2026-08-25

**R017 provenance note:** copied from the local closure bank on 2026-08-26 with a branch-local,
file-relative certificate.  The source cohomology identities are those of the audited BCDD
construction; this cell certifies their typed consequence and does not claim a fresh derivation
of the source paper's line-bundle cohomology tables.

## Verdict

Varying the holomorphic map inside the same BCDD monad topology cannot produce
a nonzero renormalisable up-type Yukawa while retaining exactly the audited
massless MSSM Higgs content.

The earlier height-308 theorem used surjectivity of the `372 -> 312` map to
identify all of `H^1(Lambda^2 V^*)` with an ambient cohomology group. The
stronger statement here does not need that surjectivity. It needs only the
line-bundle cohomology vanishings that hold throughout the locally-free monad
family:

```text
H^1(X,G_X) = 0,
H^1(X,K_1) = 0.
```

On the same smooth `X`, equivariant `(3,4)` branch and `k=4,8` Wilson choices,
the first kills the images of both matter inputs. The second injects the
ambient Higgs subspace into the bundle Higgs cohomology. That injected subspace
always contains the single `C12` character which gives the audited up-type
Higgs. Every trilinear using this Higgs vanishes by functoriality.

If a rank-jumping map supplies a nonambient Higgs with the same Wilson
character, it adds at least a second massless up-type Higgs before any new
mass/mixing dynamics. It therefore leaves the exact massless MSSM spectrum.

## 1. The two functorial sequences

Write `L=O_X(H)` and use the BCDD sequences

```text
0 -> V -> G_X -> L -> 0,                                      (E)
0 -> K_1 -> Lambda^2 G_X^* -> Lambda^2 V^* -> 0.              (W)
```

The ambient line-bundle calculation gives `H^1(X,G_X)=0`, independently of
the numerical coefficients of the locally-free monad map. Therefore the map

```text
i : H^1(X,V) -> H^1(X,G_X)
```

is zero.

Dualising the defining `K_1` sequence gives

```text
0 -> K_1^* -> G_X(H) -> O_X(2H) -> 0.
```

Both positive bundles have no higher cohomology. Consequently
`H^2(X,K_1^*)=H^3(X,K_1^*)=0` for every locally-free map, whether or not the
map on global sections is surjective. Serre duality on the Calabi--Yau
threefold gives

```text
H^1(X,K_1)=H^2(X,K_1^*)^*=0.
```

The long exact sequence of (W) therefore contains an equivariant injection

```text
j : H^1(X,Lambda^2 G_X^*) -> H^1(X,Lambda^2 V^*).
```

Surjectivity of `372 -> 312` makes `j` an isomorphism, but injectivity is
unconditional in this monad family.

## 2. The ambient subspace contains the unique audited `H_u`

The exact toric Čech computation gives, before the determinant twist,

```text
H^1(X,Lambda^2 G_X^*) = chi_10 + chi_11.
```

For the `(n_1,n_2)=(3,4)` branch, `2 tilde_n=2`, so after the required twist
the injected subspace is

```text
C_amb = chi_0 + chi_1  subset  H^1(X,Lambda^2 V^*).
```

For both Wilson choices `k=4` and `k=8`, the up-type doublet survives in the
`chi_0` sector. Thus `C_amb` supplies one massless `H_u` class at every
locally-free map in this fixed geometric/equivariant setup. It is precisely
the unique `H_u` in the audited MSSM spectrum when stability and the total
surviving multiplicity condition are also retained. Local freeness alone is
not being used as a surrogate for those spectrum hypotheses.

## 3. Naturality kills every coupling to the ambient Higgs

Let `a,b in H^1(X,V)` and let `c=j(c_tilde)` be any Higgs class in the
ambient image. Compatibility of exterior powers, contraction and cup product
with the inclusion `V -> G_X` gives

```text
mu_u(a,b,c)
  = <i(a) cup i(b), c_tilde>
  = 0,
```

because `i(a)=i(b)=0` in `H^1(X,G_X)`. This is an identity of cohomology
classes, not a statement about a chosen basis, residue normalisation or one
arithmetic point.

It follows that the `chi_0` class already present in `C_amb` has zero
renormalisable `10 10 5_H` coupling for every locally-free map in the same
monad topology.

## 4. The rank-jump dichotomy

Let

```text
r = coker-dimension[H^0(G_X(H)) -> H^0(O_X(2H))].
```

Then `r=h^1(K_1^*)=h^2(K_1)`. When `r=0`, the ambient injection is an
isomorphism and the complete up map is zero, reproducing the height-308
theorem.

When `r>0`, nonambient classes can enter `H^1(Lambda^2 V^*)` through the
next long-exact term. There are only two possibilities relevant to `H_u`:

1. no additional nonambient `chi_0` survives the Wilson projection; then the
   unique `H_u` is still the ambient class and its Yukawa is zero;
2. at least one nonambient `chi_0` survives; then the massless cohomology has
   at least two `H_u` doublets before any additional mass/mixing mechanism.

Therefore a nonzero up coupling cannot be obtained merely by moving to a
rank-jumping stable map while keeping the exact audited massless spectrum.

## 5. Scope and escape hatches

This theorem covers the BCDD monad topology, the `(3,4)` equivariant branch,
Wilson `k=4` or `k=8`, and the cohomological massless-spectrum definition.
It does not prove that all conceivable heterotic Standard-Model constructions
have zero up Yukawas.

The exact hatches are now narrower:

- change the monad/topological bundle construction so the unique `H_u` is not
  the ambient-injected class;
- change the visible equivariant/Wilson construction and recompute the full
  spectrum;
- permit extra Higgs/vectorlike states and derive a mass matrix whose light
  combination has a nonambient component;
- generate a genuinely new effective operator through heavy-field mixing,
  torsional worldsheet effects, spacetime nonperturbative physics or
  supersymmetry breaking.

Changing only the coefficients of the same locally-free monad map is not an
escape while the exact massless MSSM Higgs count is retained.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py
```

The certificate checks the source/report hypotheses, the character twist,
the `k=4,8` Higgs selection, and the exact one-Higgs/rank-jump dichotomy.

## Final disposition

```text
same BCDD monad + exact one-Hu spectrum + renormalisable up Yukawa nonzero:
    REFUTED;
nearby coefficient variation as a flavor repair:
    CLOSED;
extra-Higgs/mixing or different-bundle repair:
    OPEN, requires new physical and holomorphic data.
```
