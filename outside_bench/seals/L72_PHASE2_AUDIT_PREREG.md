# SEAL — L72 PHASE 2: auditing the flagged closure claim

**Sealed before computing.** Object: `frontier/B775_phase2_wave1/cells/P2W5-L72/`, the cell
that ran L72's phases 2–3, and whose row in `FINDINGS_WAVE5.md` reads:

> *"E6 modular data at k=1,2 independently confirmed consistent … **but the cell's Phase-2
> closure claim carries an issue the verifier flagged. Carry with the issue named.**"*

The issue is **not named anywhere in the arc**. Memo 210 identified it as L72's live
remainder. This seal locates it and tests what can be tested on this bench.

## What the cell claims, in its own words

`compute.py`: *"A2 := 6j/F-symbols computed AND verified at level 1 AND at level 2."*
`output.txt`'s discriminating fact: the Z/3 simple-current subcategory is **modular**, so
`E6_2 = Pointed(ℤ/3) ⊠ Centralizer`, and *"that rank-3 factor's S-matrix and twists match
the even part of SU(2)_5 entry-by-entry (errS 4.41e-41, errT 4.46e-41)."*

And `results.json` already fences one residual as EXTERNAL:
*"uniqueness-up-to-gauge of the level-2 F-symbols (constructed + verified, **not
classified**)."*

## CELL 1 — do the cell's two committed artifacts agree?

**Observed:** the verdict string in `output.txt` against `results.json["verdict"]`, and
every gate name/value present in both.

- **Outcome A:** the verdict strings agree and every shared gate agrees.
- **Outcome B:** they do not.

## CELL 2 — the Deligne splitting, rebuilt independently

From an E₆ level-2 stage rebuilt on this bench from the Cartan matrix (the memo-206
instrument, whose nine conformal weights already agree with this cell's exactly).

**Observed:** the set of objects with quantum dimension 1; whether they close under fusion
into a ℤ/3; whether the pointed subcategory is modular (`|det S|` on it, non-zero); the
Müger centraliser's object set and rank; and the worst entrywise error of
`S^{E6_2} − S^{pointed} ⊗ S^{centraliser}` under the object bijection, and likewise for T.

- **Outcome A:** three qdim-1 objects closing into a ℤ/3, pointed subcategory modular,
  centraliser of rank 3, and both product errors below **1e-10**.
- **Outcome B:** any of these fails.

## CELL 3 — is the rank-3 factor the UNITARY SU(2)₅-even, or a Galois conjugate?

The cell identifies the centraliser by matching S and T *entry-by-entry* to SU(2)₅-even at
`q = exp(iπ/7)`. **Modular data does not determine a modular tensor category in general**,
so the identification needs the rank-3 landscape checked, not one candidate matched.

SU(2)_k data: `S_{jl} = √(2/(k+2))·sin(π(2j+1)(2l+1)/(k+2))`, `h_j = j(j+1)/(k+2)`; at
k = 5 the even part is `j ∈ {0,1,2}`. Its Galois orbit is indexed by `k' ∈ (ℤ/7)*`,
replacing `sin(πx/7)` by `sin(πk'x/7)` and `h_j` by `k'·h_j`.

**Observed:** for each `k' ∈ {1,2,3,4,5,6}`, the worst entrywise error between the
centraliser's normalised S and T and the `k'`-conjugate's, and the quantum dimensions of
the centraliser.

- **Outcome A:** exactly one `k'` matches both S and T below 1e-10.
- **Outcome B:** none matches, or more than one does.

## Controls (all must pass before any cell is read)

- **C1 — the stage's own gates**, as in memo 206: |W(E₆)| = 51840; S symmetric and unitary;
  `S²` a 0/1 permutation and equal to the E₆ diagram flip; `(ST)³ = S²`; Verlinde
  coefficients non-negative integers.
- **C2 — cross-bench agreement.** The centraliser's conformal weights and quantum
  dimensions computed here must match the values `P2W5-L72` printed for the same objects
  (`h = 0, 6/7, 9/7`; `qdim = 1, 1.801938, 2.24698`).
- **C3 — MB12 transversality.** The Galois sweep must **reject** at least one `k'` — if
  every conjugate matches, the test cannot discriminate and **CELL 3 may not be read**
  (memo 164).

## Declared priors

- CELL 1: **no prior declared.** The two files were opened far enough to locate the cell and
  no further before this seal was written.
- CELL 2: **Outcome A** expected — the cell reports it and its modular data already agrees
  with this bench's.
- CELL 3: **Outcome A** expected, on the quantum dimensions alone (all three positive and
  > 1 point to the unitary representative). The value of the cell is *which* `k'`, and
  whether the rejection is sharp.

## What this seal does NOT do

It does not classify the rank-3 category. Discharging *"not classified"* requires the
rank ≤ 4 classification of modular tensor categories from the literature; **this bench has
not read that source, and no cell below claims it.**

## Interpretation is not preregistered

Per bench rule #21 the outcomes state only what will be observed.
