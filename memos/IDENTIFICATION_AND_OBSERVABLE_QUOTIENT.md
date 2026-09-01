# R031D — identify or descend: the correct parameter count

## Verdict

B1231 is right that an unearned identification is an unpriced observer input,
but an identification row is not automatically one scalar or one bit.  Its
price is the inequivalent choice space of typed maps, and a raw choice is not
physical when every downstream observable descends through it.

For every bridge in the programme there are therefore two legitimate closure
modes:

1. **identify:** exhibit the typed map and prove it unique up to the declared
   equivalences; or
2. **descend:** prove that all claimed observables are independent of the
   choice of map or lift.

If neither is done, the remaining input is the image of the typed choice
space in invariant observables, modulo only the equivalences that have
actually been declared and proved to act.  It is not the dimension of a
convenient presentation space, and it is not the number of rows in an
identification ledger.

## Exact quotient lemma

Let

```text
0 -> C -> V -> T -> 0,              dim(T)=1,
```

and let `beta: wedge^2(V) -> W` be alternating.  If

```text
beta|wedge^2(C) = 0,
```

then for `c in C` and `t in T`,

```text
bar_beta(c,t) = beta(c,v),           v any lift of t,
```

is well-defined.  Indeed another lift is `v+c'`, and the difference is
`beta(c,c')=0`.  This does not force `bar_beta` to vanish: the certificate
uses a nonzero mixed block and verifies exact invariance under 125 distinct
lifts.  A planted `C-C` term makes the choice visible, so the result is not a
tautology of the implementation.

Thus a three-dimensional family of lifts can contribute **zero** observable
directions.  Conversely, a single unearned identification can carry a
positive-dimensional or disconnected choice space.  Counting source-space
coordinates or identification rows is only an upper-level inventory, not a
physical parameter count.

## Application to the height-308 Higgs block

R031A proves that the split character data leave a literal

```text
P(B_0) = P^3_C
```

of Higgs lines.  It does **not** follow that the holomorphic theory has three
physical parameters.  R025 documents the physical character shift
`B_phys=B_raw-2`; tensoring by that one-dimensional character keeps the
carrier and exact sequence fixed, so raw `B_2` is the physical `B_0` carrier
in this block.  The long exact sequence has the typed form

```text
0 -> B_2,conn -> B_2 -> B_2,tail -> 0,
dim =             3       4          1.
```

Put `C=(B_2,conn)_phys` and `T=(B_2,tail)_phys`.  If R032's
characteristic-zero computation proves, for every `A_11`/`e^c` leg, that the
lepton tensor vanishes on `wedge^2(C)`, the lemma makes its restriction with
the lepton `B` leg in `C` factor canonically through

```text
C tensor T.
```

Changing the representative of a nonzero tail/Higgs class by any connecting
vector then leaves **that restricted, unnormalised holomorphic pairing**
unchanged.  If the induced mixed map is nonzero, the open stratum
`P^3-P(C)` maps to one point of the projectivised operator space; if it is
zero, the whole restricted pairing is zero.  The pure-connecting boundary
maps to zero for this pairing.  This is a descent statement, not yet a field
redefinition: eliminating a physical choice requires an allowed basis-change
group and descent of every claimed observable, including metrics and
normalisation.

The down operator requires characteristic-zero vanishing on **all** vectors
in its other `B_6` leg.  R032 is adjudicating the 18 scalar entries in
`A_7 tensor B_6,conn tensor B_2,conn`; even if those vanish, the nine entries
in `A_7 tensor B_6,tail tensor B_2,conn` are the remaining descent
obstruction.  Neither block is treated as proved here.  This distinction
prevents the lepton lemma from being silently promoted to the down sector.

## Consequence for “parameter free”

The correct closure object is not a list of canonical source data.  It is the
map

```text
typed realizations / proved equivalences  -->  invariant SM observables.
```

Parameter freedom is the dimension and component structure of its image.
The programme closes an apparent choice either by selecting one equivalence
class or by proving the observable map constant on that choice.  B1231 names
the first obligation; the quotient lemma adds the second.  The listener map
`u` must be audited by this same test rather than counted as one unspecified
input.

## Scope

This cell is exact linear algebra and parameter-accounting discipline.  It
does not assume that R032's finite-field zeros lift to characteristic zero,
does not construct the Serre-tail map or an allowed field-redefinition group,
and does not supply matter metrics, canonical normalization, masses or
mixings.

## Reproduce

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r031d_observable_quotient/observable_quotient.py
```
