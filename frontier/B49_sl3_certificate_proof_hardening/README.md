# B49 -- SL(3) Certificate-To-Proof Hardening

## Question

Can the B48 fixed-line integer splitting classification be decomposed into a
compact, human-reviewable proof architecture rather than remaining only a broad
certificate scan?

## Status

```text
PROOF-HARDENING FRONTIER
PC12 SUPPORT
NO CLAIM PROMOTION
```

B49 does not mark PC12 as proven or draftable. It identifies the proof modules
that a mathematical note must write cleanly.

## Run

```bash
python frontier/B49_sl3_certificate_proof_hardening/probe.py
```

## What It Checks

```text
universal discriminant/parity splitting criterion
direct positive split families and isolated cases
square-gap propagation lemma
finite positive strip 4 <= c <= 14
negative strip and boundary -11 <= c <= -2
```

The remaining prose task is to turn these checked modules into a readable proof,
especially the global coefficient-positivity exclusions used outside the finite
strips.
