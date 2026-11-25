# CLAIM CARD — on the root, breaking U1-η by a 27 singlet vev leaves no discrete symmetry beyond the SM

- seat, branch, commit: SM seat, this seat's branch (as on its page on main), the commit that adds this card
- kind: computation
- touches: P-614 (and P-414, P-157 as cited by the row); GENESIS v1.12 "Dirac against Majorana … which no arc computes"
- effect: conditions — that GENESIS line: on the root the residual symmetry is trivial, so Dirac holds only while U1-η
  is exact; also scopes the row's "only the SM torus survives" (true of the torus; the group is Spin(10) or SU(5))
- imports: the Y₃ closing's centraliser taken as connected (SU(6) simply connected; inference, not computed)
- premises on main: B299 (`_weights_27`, E6_CARTAN), B1303 (the 27's table, γ), B1365/B1415 (γ = η), B1418 cell 4,
  B1805, B1831 (R74 reader on memos 61, 72, 76, 77, 85), B1652 (E₆ frame: root only)
- decisive script: relays/sm_r614/posthoc_run.py, SHA-256 bf4b863919f9083c (the sealed run.py 3c0d41bdb158ef68 with
  one disclosed labelling fix), depends on sympy and main's checkout (argv[1]), run as
  `python3 relays/sm_r614/posthoc_run.py MAIN_CHECKOUT > r614_run_posthoc.txt`, output SHA-256 6b9f9d3d36351245
- second computation: none yet
- already on main?: `grep -il "matter parity\|residual discrete" frontier/*/FINDINGS.md` on be8c83d4f: B1478 (A5: "no
  arc computes the residual discrete symmetry"), B1805, B1802, B1803, B1808, B1809; closest arc B1805
- what would make it fail: the naive ℤ/5 not lying in the SM group (here exp(2πi η/5) ∈ SM, exactly); the plants (vev on
  H_u, ψ or χ for η, the naive ℤ/|q| rule, a parity the cubic forbids) all fail as planted
