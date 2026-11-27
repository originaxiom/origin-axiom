# CLAIM CARD — on the root, breaking U1-η by a 27 singlet vev leaves no discrete symmetry beyond the SM

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-614 (with P-414 and P-157, as the row cites them); GENESIS v1.12's "Dirac against Majorana … which no arc
  computes" (§8, computed nowhere yet)
- effect: conditions — P-614 and the GENESIS line: Dirac holds only while U1-η is exact; and it scopes the row's "only
  the SM torus survives" (true of the torus; the group is Spin(10) or SU(5))
- scope: frame: the root's E6 bookkeeping, the 27 of E6 and the Y3 closing's SM x U1-eta; object: the stabiliser of
  SM-singlet vevs of the 27 and its discrete part; reach: single; hypotheses: the closing's centraliser is connected
- identifications: U1-η here is B1303's γ times 3, which B1365/B1415 identify with the η model's direction
- definitions: weights are Dynkin labels of main's 27 (B299), Cartan elements are simple-coroot vectors x, pairing mu.x;
  exp(2 pi i x) = 1 on E6 iff x in Z^6; psi = 3 x the fundamental coweight of the 27's top node; chi, Y solved as the
  Cartan directions of SU(5) in D5 and of SU(3) x SU(2) in SU(5), normalised to B1303's table; eta = (3 chi - 5 psi)/4
  (-2 on Q, u^c, e^c; 1 on d^c, L, H_d, Dbar; -5 on nu^c, N; 4 on H_u, D); V_SM = SU(3) x SU(2) coroots + Y,
  V5 = V_SM + R eta; the residual of a vev set w is {x in V : w.x in Z} / ((V cap ker w) + (V cap Z^6)); a matter
  parity is a torus element commuting with SU(3) x SU(2), fixing the vevs, -1 on Q, u^c, d^c, L, e^c and +1 on H_u,
  H_d; E-level stabilisers are the compact stabilisers in the 78 (dimension, and rank as the centraliser dimension of a
  random element); the E5 census is h in Z^6 mod 2 with h even on nu^c and N (the cloud memos 72 and 76)
- imports: none
- premises on main: B299 (_weights_27, E6_CARTAN), B1303 (the 27's table and gamma), B1365/B1415 (gamma = eta),
  B1418 cell 4, B1805, B1831 (Review 74's reader on the cloud memos 61, 72, 76, 77, 85), B1652 (E6 frame: root only);
  the decisive wrapper runs the seat's disclosed relays/sm_r614/posthoc_run.py unchanged, because the sealed
  relays/sm_r614/run.py failed on a one-line colour bug (its colour flip also flipped the singlets)
- decisive script: relays/claims/sm_refile/r614_decisive.py, SHA-256 f2917147ad628e55, depends on the standard library and
  sympy, run as python3 relays/claims/sm_refile/r614_decisive.py, output SHA-256 1277c472aa46f61e
- decisive lines: 14 lines marked "DECISIVE:", SHA-256 1277c472aa46f61e
- failing control: python3 relays/claims/sm_refile/r614_control.py
- second computation: none
- already on main?: grep -il "matter parity\|residual discrete" frontier/*/FINDINGS.md on be8c83d4f gives B1478 (A5:
  "no arc computes the residual discrete symmetry"), B1805, B1802, B1803, B1808, B1809; the closest arc is B1805
- what would make it fail: a nontrivial residual modulo the SM after a nu^c or N vev in SM x U1-eta, or
  exp(2 pi i eta/5) not an SM element, or a matter parity found there, or nu^c and N unequal under eta
