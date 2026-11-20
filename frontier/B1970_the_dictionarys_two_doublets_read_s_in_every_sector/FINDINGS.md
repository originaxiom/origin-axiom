# B1970 — The record's dictionary gives two Higgs doublets of opposite hypercharge, one for the up quarks and one for the down quarks and leptons; with the frame's holomorphic coupling every sector then reads S, and the cusp mixing aligns

**Verdict: PROVED** for the checks D1 to D5 (exact in D1 to D3, numerical in D4 and D5; D4 a second computation of the
web seat's W-H1). The conclusion that the
reading leaves the menu holds **given H1 to H3**, stated below. Main, 2026-11-20. Data-free. Register rows P-295 and
P-847; identification I-37. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /two doublets|two Higgs doublets|H_u|H_d|Type II|holomorph|superpotential|10 of SO\(10\)|reading rule|conjugate Higgs|doublet index/: 47 of 1710 arcs on main match (NEGATIVE 14, OPEN 4, PROVED 29); 55 register rows match (DONE 38, QUEUED 17)`.
- **B1790 (NEGATIVE): "the reading is not derived in B1656's frame".** It names "the holomorphic superpotential's
  need for two doublets (the MSSM's H_u, H_d)" as the textbook analogue, and says nothing on record derives a reading
  of this kind. This arc is that derivation, under H1 to H3.
- **The dictionary:**
  - B1253 (PROVED) found the 10 of the record's 27 to be "two Higgs doublets + the colour-triplet pair (not
    assumed)", with the Standard Model's Yukawa sector in the 10·16·16 terms. B1252 derived the hypercharge.
  - B1253 did not say which doublet each operator uses.
- **The reading rule:**
  - P-295 asks for it, and names "Type II (two doublets sharing a flavour section)" as a deciding route.
  - P-847 has the relative reading fixed by charge, for one doublet.
  - I-35 is the one-doublet sign rule (UNEARNED).
  - FL-09: the conjugate reading is imported by hand, because the frame has no doublet index.
- **The alignment:**
  - B1946: frame C's mixing is aligned when every sector reads S.
  - The web seat's W-D2 D-1 (harvest row pending, 2026-11-19, at the author's word): two doublets of opposite
    hypercharge sharing one fibre triplet align the cusp mixing on the act's line, and the mixing then falls with
    height.
  - B1742: two nearly null directions read S everywhere give alignment with mixing too small.
- **The web seat's W-H1 makes the holomorphy argument first and computes it more fully** (2026-11-20, 07:43, at the
  author's word; registered at harvest row 1986).
  - The frame's three Higgs coefficients and all 11 non-zero channel residues are holomorphic (residual 5e-41).
  - With S, every unnormalised channel coupling is holomorphic. With S̃, none is (residual 1.19 to 25).
  - The real norms break holomorphy, by an amount that falls with height.
  - Post hoc and exactly, S̃(τ) = −Q_K S(−τ̄) Q_K⁻¹.
  - Its step 5 takes the need for a second doublet as the standard reason. Its step 6: frame C's Higgs never uses its
    hypercharge, so both doublets carry one triplet and the reading is (S, S, S).
  - **This arc's own part:** the grounding of step 5 in the record's dictionary (D1 to D3: the dictionary's up and down
    operators use two distinct doublets carrying exactly the frame's charges), and a second computation of W-H1's
    core holomorphy check (D4) on main's code.
- **The rejected claim this is not:** agy-exp's withdrawn F3 (P-847, rows 1798 and 1799) said holomorphy picks one
  Higgs world. Main rejected it because twists of either sign are holomorphic. D4 shows the distinction: this arc's
  holomorphy is of the Higgs's coefficients in τ, which the conjugate reading breaks. A twist's sign does not break it.
- **The literature:**
  - In a holomorphic (supersymmetric) theory a Yukawa coupling cannot use the conjugate doublet, so the up and the
    down quarks need two doublets of opposite hypercharge (standard; the MSSM's H_u and H_d).
  - In SO(10) both lie in one 10, with 16·16·10 giving every Yukawa (standard).
  - With a single 10, Y_u and Y_d are aligned and the quark mixing is too small (standard; realistic SO(10) models add
    more Higgs representations).

## What was run (`verification/two_doublets.py`; main's code throughout, B1253's and B1945's imported unchanged)

| check | result |
|---|---|
| **D1** the 10's hypercharges | Y = +1/2 twice, −1/2 twice, +1/3 three times, −1/3 three times: two SU(2) doublets of opposite hypercharge and a colour-triplet pair |
| **D2** which 10-state each Standard Model operator uses (40 Yukawa-type triples 10·16·16, every one conserving Y) | Q u^c and L ν^c use the Y = +1/2 doublet (states 4, 9). Q d^c and L e^c use the Y = −1/2 doublet (states 15, 22). The up and down operators' states are disjoint; the down and lepton operators share theirs |
| **D3** the frame's sector charges (B1656: Q 1, u^c −4, d^c 2, L −3, e^c 6, in 6Y) | Each coupling needs a Higgs of charge −(q_L + q_R): up +3 (Y = +1/2), down −3 and leptons −3 (Y = −1/2). Each equals the hypercharge of the doublet the dictionary's operator uses |
| **D4** holomorphy in τ | The frame's Higgs coefficients (DR's three components) and a matter residue's theta product satisfy ∂/∂τ̄ = 0 (relative 1e-25). The conjugate reading's coefficients conj(c_k) satisfy ∂/∂τ = 0 instead. A theta product with both characteristics negated stays holomorphic (the F3 case) |
| **D5** every sector reading S, height 30, three points of order 5 | Smallest diagonal \|V\| 1.000000, largest off-diagonal 6.3e-5 (B1946's numbers) |

## What it means

- **The record's own dictionary meets the frame's charge requirement with two distinct doublets.** The up sector needs
  Y = +1/2 and gets the doublet the dictionary's Q u^c term uses. The down quarks and leptons need Y = −1/2 and get
  the other. No sector needs the conjugate of another's Higgs.
  - The conjugate reading (H̃ for the up quarks) is how the minimal Standard Model meets the same charges with one
    doublet. The record imported it (FL-09). The dictionary does not need it.
- **Holomorphy then fixes the reading.**
  - The frame's coupling is real norms times factors holomorphic in τ, the supergravity Yukawa form, and B1790
    established it.
  - The conjugate reading makes the Higgs's factor antiholomorphic (D4).
  - So if every sector keeps the frame's holomorphic form, each reads S with its own doublet. This fixes the global
    bit as well: all S, not all S̃.
- **The cusp mixing is then aligned** (D5; B1946 at 24 points; W-D2 D-1 on the act's line). The clash of B1739,
  B1740 and B1966 belongs to the one-doublet reading.
- **The problem moves.** In the standard theory one 10 gives too little mixing, and W-D2 finds the off-diagonal
  mixing falling exponentially with height. So the open questions become:
  - the size of the mixing;
  - the split between leptons and down quarks, still tied (the lepton factor A10).

## Hypotheses, and what this arc does not establish

- **H1, the dictionary.** B1253's 27, with B1252's derived hypercharge, is tagged ("given Λ").
- **H2, the identification (I-37, UNEARNED).** The frame's Higgs is identified with the 10's doublet pair: up with
  H_u, down and leptons with H_d. Whether both share one fibre mode, as in W-D2's D-1, or carry independent
  directions, as in B1742, is a further choice. Both give alignment.
- **H3, holomorphy as a requirement.** It is the frame's own form and the supergravity analogue. It is not derived
  from the principle.
- **Main's ruling on the standing,** which W-H1 asks for:
  - Holomorphy as a criterion for the reading is on record before the look. P-847's note of 2026-11-14 names "a
    structure the exchange of S and S̃ does not keep" as the only way the global bit can be fixed.
  - Its two-doublet form, and the aligned world it gives, are stated after the look (W-D2 on 2026-11-19, W-H1 and this
    arc on 2026-11-20).
  - So the reading is recorded as **derived given H1 to H3, found after the look**, not as removed outright.
  - Before any card rests on it, the reading enters a sealed card as a declared option. The record's alternative, the
    one-doublet conjugate reading, sits beside it, and the look is counted.
- **Found after the look, disclosed.**
  - B1946 (2026-11-15) showed that the all-S reading aligns the mixing.
  - P-847's note of that day and P-861 ruled that choosing it then would be post hoc.
  - This arc's premises are all older: B1253 (September), B1790 and B1656's charges (October). The argument was
    assembled now, after the look.
  - So the reading counts as removed only given H1 to H3, and any comparison built on it is a second attempt on the
    same idea (the look ledger).
- **Not established:**
  - the mixing's size;
  - the lepton–down split;
  - any comparison with data.

## Files

`verification/two_doublets.py` and `two_doublets_run.txt`. The lock is `verification/test_b1970_two_doublets.py`.

0 of 19.
