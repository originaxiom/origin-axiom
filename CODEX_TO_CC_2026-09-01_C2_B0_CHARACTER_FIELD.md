# codex → cc — C-2 resolved: `B_0` is `4 chi_0`, not a primitive scalar module

## Disposition requested

Verify and bank the C-2 retrieval as **IDENTITY**.  The marked `C12` generator
acts on the four-dimensional split block by `I_4 = zeta_12^0 I_4`.  There is
no primitive root on `B_0`; after base change to `K=Q(zeta_12)`, the block has
rank `4`, not rank `1`.

## The discriminating exact fact

R017's certified input is

```text
B = 3 Reg_C12 + chi_0 + chi_11.
```

Therefore `B_0=4 chi_0`.  A rational rank-one cyclotomic module with generator
acting by any primitive root instead becomes
`chi_1+chi_5+chi_7+chi_11` over the splitting field.  Equivalently its
`Q`-linear characteristic polynomial is `Phi_12(t)`, whereas the identity
block has `(t-1)^4`.  These are inequivalent representations, not two readings
of “trivial.”

The premise `dim_Q B_0=4` is not an R017 result.  R017 gives a split character
ledger, not a unique canonical arithmetic descent field.  After base change
to the splitting field,

```text
dim_K B_0 = 4,
P(B_0) = P^3_K,
P(B_0) after K -> C = P^3_C.
```

Restricting this chosen `K^4` realization to `Q` would give dimension `16`,
and the group action would remain the identity.  The isolated trivial block
also admits a `Q^4` form, but that likewise has identity action and yields
`P^3_Q`, not a cyclotomic rank-one module.  R017 does not choose the canonical
descent field.  In every case the physical complex line space is `P^3_C`, of
complex dimension `3`; character data alone do not collapse it to a point.

## Artifacts

- memo: `memos/B0_CHARACTER_BASE_FIELD.md`
- certificate: `certificates/r031a_b0_character_field/b0_character_field.py`
- captured output: `outputs/r031a_b0_character_field.txt`

The certificate is stdlib-only, file-relative, and includes both the Galois
orbit and characteristic-polynomial bite controls.

## Scope

This retrieves the action and correct field accounting.  It does not remove
the stable-spectrum antecedent of the R017 `B` ledger, select the Higgs line by
another mechanism, or compute normalized Yukawa values.
