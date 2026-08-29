# R025 — lepton tail-selection correction

## Verdict

R024's coarse Wilson-character result is correct, but its tail-pair paragraph
used a rule specialized to the quark leg `A7` as though it also described the
charged-lepton leg. The correct raw selection equations are

```text
down:    A7  x B_rho x B_sigma,  rho+sigma = 8 mod 12,
lepton:  A11 x B_rho x B_sigma,  rho+sigma = 4 mod 12.
```

For the actual charged-lepton/Higgs sector both `B` legs lie in raw `B2`.
Its pure-tail contribution repeats the unique one-dimensional tail-2
direction, so that contribution vanishes by the alternating `B x B` cup
product. Connecting/connecting and mixed connecting/tail entries remain
unevaluated. Consequently the B1208 identical/independent/absent fork remains
open.

## Primary and chain conventions

The certificate parses a minimal excerpt of the BCDD primary source rather
than rebuilding the charge row from a declared formula. It verifies

```text
Wilson charges: (u^c,Q,e^c,d^c,L/Hd) = (8k,k,6k,2k,9k),
(n1,n2)=(3,4), k=4 or 8,
H1(V) = 3 Reg + chi_1+chi_3+chi_7+chi_9+chi_10+chi_11.
```

Thus both retained branches select physical character zero for `e^c` and
`L/Hd`, with dimensions three and four respectively. The committed
height-308 chain frames give the shifts

```text
A_physical = A_raw + 1,
B_physical = B_raw - 2.
```

Therefore `e^c` comes from raw `A11`, while both `L` and `Hd` live in raw
`B2`. Invariance of a raw triple gives

```text
(a+1) + (rho-2) + (sigma-2) = 0 mod 12,
rho+sigma = 3-a mod 12.
```

For `a=7`, this reproduces the committed quark rule and its unordered tail
pairs `(0,8),(2,6),(4,4)`. For `a=11`, the general tail set
`(0,2,4,6,8)` instead gives `(0,4),(2,2),(8,8)`. After the physical lepton
projection, only `(2,2)` remains. Since the tail-2 multiplicity is one, its
alternating square is zero.

## What this does and does not close

This removes a false lepton-tail analogy from the record. It is a genuine
narrow negative for the pure-tail/pure-tail lepton entry, independent of the
missing determinant comparison and trace normalization.

It does **not** select a generation basis inside `A0`, split the four-dimensional
`B0` space into a distinguished lepton/Higgs frame, construct the chain-level
Serre lift, or evaluate any mixed or connecting entry. Equality of the coarse
characters still does not imply equality of the down and lepton tensors.
OA-C1148 and OA-C1150 therefore remain `OPEN`.

The vendored primary excerpt is intentionally minimal and lives next to the
certificate so the cell runs from any checkout and any current directory.
Its source is Braun--Candelas--Davies--Donagi, arXiv:1112.1097,
`Three_gen_models.tex`.

Reproduce with:

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r025_lepton_tail_selection/lepton_tail_selection.py
```
