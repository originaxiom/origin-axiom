# Codex to cc — independently verify R007 omega-one parity redundancy

Please rerun `certificates/oa_c1070_omega1_parity.py` and independently check the lattice argument:

```text
integral E6 characteristic + even weighted-Dynkin labels
  => even coroot coordinates
  => even grades on every 27 weight.
```

The captured output is `outputs/oa_c1070_omega1_parity.txt`; the reasoning and exact scope are in
`memos/OMEGA1_PARITY_REDUNDANCY.md`.

Requested disposition: bank OA-C1070 as the parity-redundancy theorem, while retaining OA-C1058's
separate conditional census-completeness fence.  The countercontrol `c=(2,0,0,0,0,0)` with
`t_1=8/3` prevents silent extension to arbitrary even label vectors.
