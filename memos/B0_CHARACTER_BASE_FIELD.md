# R031A — the exact character and base field of `B_0`

## Verdict

The C-2 fork is resolved in the identity direction, but its proposed field
counts need one correction.  In the certified character ledger

```text
B = 3 Reg_C12 + chi_0 + chi_11,
```

`B_0` is, by definition, the four-dimensional `chi_0` isotypic space after
passing to a splitting field such as `K = Q(zeta_12)`.  The marked generator
acts as

```text
g|B_0 = zeta_12^0 I_4 = I_4.
```

There is no primitive root to report.  After base change to `K`, `B_0` is free
of rank `4`, not rank `1`, as a `K`-vector space.  Its Higgs-line parameter
scheme in that realization is `P^3_K`; after an archimedean embedding it is
`P^3_C`, of complex dimension `3`.  Thus the character datum does not select
a Higgs line.

## Why the scalar alternative is a different representation

A one-dimensional `Q(zeta_12)` module regarded as a four-dimensional
`Q`-space, with the generator acting by multiplication by a primitive root,
has rational characteristic polynomial

```text
Phi_12(t) = t^4 - t^2 + 1.
```

After extension to `K`, it splits into the four Galois-conjugate characters

```text
chi_1 + chi_5 + chi_7 + chi_11,
```

for every choice of primitive root.  It does not become `4 chi_0`.  By
contrast, the exact action on `B_0` has characteristic polynomial `(t-1)^4`
over its displayed four-dimensional carrier.  Calling primitive scalar
multiplication “trivial” only means trivial on projective points; it is a
nontrivial linear representation and is excluded by the character label.

The full multiplicity vector supplies a second check:

```text
(m_0,...,m_11) = (4,3,3,3,3,3,3,3,3,3,3,4).
```

It is not Galois-invariant over `Q` (`m_1=m_5=m_7=3`, while `m_11=4`), so the
full 38-dimensional display is not the split decomposition of a rational
representation with those multiplicities.  It is a split-character
calculation.  Restricting the chosen `K^4` realization of the block to `Q`
would give dimension `4*[K:Q]=16`, with the group action still the identity.
The isolated trivial block also admits the evident `Q^4` form.  R017 does not
decide which descent field is geometrically canonical; neither option changes
the generator into primitive scalar multiplication.

## Field discipline

The unconditional physical statement is obtained after complexification:
`P^3(C)`, carrying three complex continuous directions.  For a chosen
`K`-model the parameter scheme is `P^3_K`; if an independent `Q`-form is
established it may instead be written `P^3_Q`.  R017 alone does not choose
between those arithmetic models.  This preserves B1230/C-1's useful field
rule without changing the representation or collapsing its dimension.

The conclusion consumes the already certified R017 input
`B=3 Reg+chi_0+chi_11`; it does not upgrade the conditional stable-spectrum
antecedent behind that input, select the three lepton directions, or compute
physical normalized Yukawa values.

## Reproduce

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r031a_b0_character_field/b0_character_field.py
```
