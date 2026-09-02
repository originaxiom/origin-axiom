# R40 — B516: "among the metallic family only golden gives a Pisot number under x → x(1+√x)"

`r40.py` (PARI): β_m = x_m(1+√x_m) for the metallic means x_m = (m+√(m²+4))/2, minimal polynomial by `algdep`, all
conjugates by `polroots`.

| m | β | minimal polynomial | other conjugates (abs) | Pisot |
|---|---|---|---|---|
| 1 (golden) | 3.676205 | x⁴−2x³−5x²−4x−1 | 0.4401, 0.7862, 0.7862 | **yes** |
| 2 (silver) | 6.165356 | x⁴−4x³−12x²−8x−2 | 1.3369, 0.4926, 0.4926 | no |
| 3 (bronze) | 9.305088 | x⁴−6x³−29x²−16x−3 | 2.6995, 0.3456, 0.3456 | no |
| 4 | 12.954620 | x⁴−8x³−62x²−28x−4 | 4.4825, 0.2625, 0.2625 | no |

**Verdict: MATCH** (bank: 3.676 yes; 6.165, 9.305, 12.955 no; binding conjugate x(√x−1) = 0.440 for golden, 1.337 for
silver). B516's own reading of what this means ("dimensions forced by a Pisot ceiling") is marked DEAD by B516 itself.
**Physics content:** none. "No observable content."
