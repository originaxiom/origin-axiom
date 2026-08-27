# R022 — V₄ named-action audit

Read-only source archaeology and a self-contained exact finite comparison for OA-C1133.
The executable certificate is `certificates/r022_v4_torsors/v4_named_action_audit.py`; its
captured output is `outputs/r022_v4_torsors.txt`.

## Source locks

- OA-C1133 remains `OPEN` in `documents/PROGRAM_QUESTION_ANSWER_MAP.md`.
- B1161 branch orbit: commit `7941dc18368c86520b014cd5484076bc1b2e040c`,
  `frontier/B1161_frontier_sweep/{FINDINGS.md,b1161_results.json,verification/frontier_map.txt}`.
- B1166 pair comparison: commit `85307a926d77851567be0beea53449436e8f89b0`,
  `frontier/B1166_charter_attack/{FINDINGS.md,b1166_results.json}`.
- B1024 primary presentation: commit `9b6d0bfc8ee1cb7427f1e9178ebea0198d2d5c37`,
  `frontier/B1024_l153_bits/b1024_cells.py`.
- B1065 convention reconciliation: commit `e5adf4278cd6dc0dea37b6e0181b742a3f87ef71`;
  it proves that the `(1,0)` versus `(0,1)` fork-twin delta is the Dynkin-node
  axis swap used below.
- An alternate B1024 execution at commit `5231b45e03e93e4d9c3c395eab57fa8fe076a934`
  (outside/new-session ref) applies the structure coordinate
  `chi*chi_plus` and exposes the first-axis transposition.
- B936 H¹ classification: commit `4b92b097c93a2458959d7e416af761d4e2749f87`.
- B700 V₄ field seam: commit `c8acd2fd90273370e11bbb726bcccf6c1cbc9c9a`.
- B713 being/chirality: commit `40c787dc9743f04df18143c933eb7c5c4623b052`.
- B766 eight-point measurement closure: commit `ac3dd82f790d07b4c5b6fcedcbfb8e8f0b6397cc`.
- B782 eight-point choice wall: commit `e8ac1d27f5cc35ea715b0bcbdf36ecdca323a6f4`.

## The three finite presentations

The B1161 object is a four-element set of surviving bundle/Wilson branches with a free
transitive action of
`Gal(Q(zeta_12)/Q) = V₄`. B1161 does not commit a canonical branch-by-branch label table;
`B00,B10,B01,B11` in the certificate are explicitly audit coordinates, not source labels.
The field is `Q(i,sqrt(3))`, discriminant `144 = 2^4*3^2`, with quadratic subfields
`Q(i), Q(sqrt(3)), Q(sqrt(-3))`.

The being-by-hearing product is the explicit four-point set
`{(b+,h+),(b-,h+),(b+,h-),(b-,h-)}`. Here
`b±=(3±sqrt(-3))/2` are the two being characters and `h±=(phi,-1/phi)` are the two
hearing values/irrep labels. Its field is `Q(sqrt(-3),sqrt(5))`, with quadratic subfields
`Q(sqrt(-3)), Q(sqrt(5)), Q(sqrt(-15))`, discriminant `225 = 3^2*5^2`.
Being-conjugation flips the first coordinate; hearing-conjugation flips the second.

B1024's actual carrier is not a four-point torsor. B936 gives 16 cocycles
`X^tau`, where `X=T_ad[2]=(Z/2)^6`; the quotient by the four-element coboundary subgroup is
`H¹(<tau>,X)=(Z/2)^2`, with coordinates at the two tau-fixed Bourbaki nodes
`(alpha_2,alpha_4)`. Each quotient class has four cocycles. Class labels carry extra
fixed-algebra annotations: `(0,0),(1,0),(0,1)` have `(dim,type)=(36,C4)`, while `(1,1)` has
`(52,F4)`.

At quotient level, B1024 maps reversal/bare tau-lift to `(1,1)`. Conjugation is `(1,0)` if
the direct inner-character coordinates are used, but `(0,1)` if the structure coordinate
`chi*chi_plus` is used. The two are a coordinate transposition; both generate all four H¹
classes with reversal. The certificate prints both tables and keeps this fence visible.

## Exact action and invariants

Every free transitive V₄ action on four points has the regular table:

| group element | cycle type | fixed count |
|---|---|---:|
| `1` | `1^4` | 4 |
| any nonidentity element | `2^2` | 0 |

The permutation character is `(4,0,0,0)` and decomposes as
`1 + chi_1 + chi_2 + chi_12`. Consequently all three four-point presentations are
equivariantly isomorphic after erasing labels and choosing a generator identification.

If admissible maps are defined to preserve the displayed field/subfield annotations,
the field labels separate the first two. `Q(zeta_12)` has ramification set `{2,3}` and
cannot contain `Q(sqrt(5))`, since 5 is unramified in discriminant 144. Thus the named
second legs are `sqrt(3)` versus `sqrt(5)`, not the same labelled action. This is the exact
version of B1166's candidate separator.

The full B766 measurement object is an eight-point free transitive `(Z/2)^3` torsor, not a
V₄ torsor. Its identity has 8 fixed points and each of its seven nonidentity elements has
zero. Therefore the phrase “measurement V₄ torsor” is not well-typed until OA-C1133 chooses
the B1024 H¹ quotient rather than the B1024 16-point carrier, B766's 8-point carrier, or
B700's 2-point golden torsor.

## Verdict

- Unlabelled four-point regular V₄ actions: equivariantly isomorphic.
- In the explicitly field-annotation-preserving category: branch-selection and
  being-by-hearing are not label-preserving;
  their quadratic-field/ramification data differ.
- Full three-way claim: presently ill-typed/open. A closing certificate must freeze the four
  branch labels and explicitly select the measurement carrier and its admissible label map.

No claim is made that all free V₄ torsors are equivalent under the programme's named-label
notion; that equivalence is only the unlabelled regular-action statement.
