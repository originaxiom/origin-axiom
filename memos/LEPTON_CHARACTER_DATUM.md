# R024 — the height-308 lepton character datum

> **R025 scope correction.** The coarse character-zero result below remains
> correct. The displayed `(0,8),(2,6),(4,4)` tail list uses the residue
> specification's `A7`-specific quark equation and is not a lepton-tail list.
> For the raw lepton leg `A11`, the sum is 4; see
> `LEPTON_TAIL_SELECTION_CORRECTION.md`.

## Verdict

The committed height-308 character ledger determines the coarse Wilson sectors
of both charged-lepton legs:

```text
chi(e^c) = 0 mod 12
chi(l)   = 0 mod 12
```

This is not B1208 fork (a). It does not determine the generation-level frame
embedding of either leg, a lepton-specific raw-character pair, or a second
`3 x 3 x 4` tensor. Therefore it establishes none of the three preregistered
fork outcomes: identical tensor, independent tensor, or absent lepton operator.

## Exact derivation

For both retained Wilson branches `k=4,8`, the committed charge table gives

```text
e^c  -> A_(-6k) = A_0, dimension 3,
l/Hd -> B_(-9k) = B_0, dimension 4.
```

The branch-local certificate rebuilds the complete `A` and `B` character
multiplicity vectors and verifies those indices and dimensions. A `k=1`
control yields characters `(6,3)`, so the zero result is a fact about the two
retained branches rather than a constant formula.

The down-tail specification independently leaves raw tail labels
`(0,2,4,6,8)`. Under its exact selection rule `rho+sigma=8 mod 12`, the
unordered admissible pairs are

```text
(0,8), (2,6), (4,4).
```

The repeated one-dimensional `(4,4)` channel vanishes by skewness. The other
two pairs prove only that abstract admissible tail classes exist. Nothing in
the committed frames identifies either with the physical `l,e^c` generation
representatives.

## Boundary

The missing data remain exactly those in
`documents/program-question-map/evidence/YUKAWA_DOWN_RESIDUE_SPEC_308.md`:
the Cox/Euler determinant phase, normalized Calabi--Yau trace, chain-level
Serre map, physical representatives and the characteristic-zero cup product.
Thus OA-C1148 and OA-C1150 remain OPEN.

Reproduce with:

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r024_lepton_character_datum.py
```
