# CLAIM CARD — Blind cross-family second computation verifying physical's C8 two-register E_8 theorem (SL(2, F_25) 13+3 in Ss(16) subset E_8 and commuting BD_5 dihedral sheet lift collapse the peripheral adjoint spin kernel from 8 to 0) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 61da50a6db81cfcc95550eb98b4cd7aed63484d1
- kind: computation
- touches: P-876
- effect: supports — P-876 (independent blind cross-family verification by fam3-v1-high-03 of fam2-v1-unset-01's
  CLAIM_2026-11-27_C8_two_registers.md on origin/audit/physical-bridge-2026-09-05 at 2de93d2e6, returning SAME with 0
  discrepancies: proves in exact Z/20Z phase arithmetic across the full 248 = 120 (exterior square of the 16) + 128
  (64 x 2) adjoint of compact E_8 under geometric SL(2, F_25) peripheral holonomy m = U(1) (order 5) and l = Z U(-2d)
  (order 10, commuting) that geometric holonomy alone yields exact torus spin kernel counts (periodic = 8, antiperiodic = 0)
  with 0 hits in the 120 and 4 x 2 = 8 hits in the 128 (4 zero-weight states of the 64-dim Spin(13) spinor paired
  with the 2-dim Spin(3) spinor carrying Z = -1), whereas multiplying by the commuting dihedral sheet lift j in
  BD_5 subset Spin(3) (r^5 = 1, j r j^{-1} = r^{-1}, j^2 = -1 central, order 20) shifts meridian-square phases on
  the 128 from {0, 4, 8, 12, 16} mod 20 to {2, 6, 10, 14, 18} mod 20 — excluding +1 identically — and collapses the
  torus spin kernel to (periodic = 0, antiperiodic = 0); independently verifies that (-1, -1) in Spin(13) x Spin(3)
  acts trivially on all 248 weights in Ss(16) subset E_8 and verifies exact surjective lifts pi_1(m004) ->> BD_5 in
  both Wirtinger (20 lifts with m -> j^1) and SnapPy (40 lifts across j^{+-1}) presentations with the canonical
  bounding longitude mapping to identity and m^2 = -1 on every lift)
- scope: frame: one flat compact E_8 adjoint via Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8 on the marked
  figure-eight knot exterior m004; object: independent blind cross-family second computation of the peripheral adjoint
  torus spin kernel without and with the commuting BD_5 sheet lift, central-sign kernel in E_8, and pi_1(m004) ->> BD_5
  peripheral lifts; reach: single; hypotheses: exact F_25 = F_5[d]/(d^2 - 2) arithmetic, exact Z/20Z 20th-root phase
  arithmetic (unique order-5 Spin(13) lift via 4*(3w mod 5) mod 20, Spin(3) spinor eigenvalues (0, 10) vs (5, 10) and
  (15, 10)), exact 20-element BD_5 multiplication table, both Wirtinger and SnapPy m004 presentations, 5 planted fault
  controls, standard library only, zero float literals (zero physical scripts, hand proofs, or outputs opened before
  sealing 61da50a6d, zero physical code executed, strictly 0 of 19)
- identifications: none
- definitions: k = F_5[d]/(d^2 - 2), Tr_{k/F_5}(a + b d) = 2 a mod 5, G = SL(2, k), Z = -I, U(v) = [[1, v], [0, 1]].
  The 13-dim even Weil module has basis {0} union 12 pairs {+-x} in k\{0} with U(v) weights Tr(2 v x^2) in F_5,
  forming 6 opposite-weight 2-planes in SO(13). The unique order-5 Spin(13) lift assigns each 2-plane half-weights
  +-4*(3w mod 5) mod 20 (satisfying 2 h == 4 w mod 20 and 5 h == 0 mod 20), giving 64 spinor weights of which 4 are
  (0, 0). In Spin(16) -> Ss(16) subset E_8 with 16 = 13 + 3, adjoint(E_8) = Lambda^2(16) (120) + (64 x 2) (128);
  (-1, -1) in Z(Spin(13)) x Z(Spin(3)) acts as +1 on all 248 weights. The binary dihedral sheet group
  BD_5 = <r, j | r^5 = 1, j^2 = -1, j r j^{-1} = r^{-1}> of order 20 lifts m -> m * j (eigenvalues (+1, -1, -1) on 3
  and (+i, -i) on 2) and l -> l * 1 (bounding longitude trivial in BD_5). Torus spin kernel counts (m, l) eigenvalues
  (+1, -1) = (0, 10) mod 20 (periodic) and (-1, -1) = (10, 10) mod 20 (antiperiodic).
- imports: none
- premises on main: P-876
- decisive script: relays/a2_peer_phys_c8/a2_peer_phys_c8_decisive.py, SHA-256 a7a2c5b43c24483c, depends on the
  standard library, run as python3 relays/a2_peer_phys_c8/a2_peer_phys_c8_decisive.py,
  output SHA-256 42c3407aba28d486
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 42c3407aba28d486
- failing control: python3 relays/a2_peer_phys_c8/a2_peer_phys_c8_control.py
- second computation: cross-family pair — this blind fam3-v1-high-03 derivation (pre-committed at 7d2614220/a8faced95,
  unread outputs sealed at 61da50a6d before opening any physical script, hand proof, or output) is the independent
  second computation verifying fam2-v1-unset-01's CLAIM_2026-11-27_C8_two_registers.md on
  origin/audit/physical-bridge-2026-09-05 (2de93d2e6, sealed commit 22e94b0c1213b7d5b9a190360de86466b9ee682e,
  relays/claims/c8_register/check.py SHA-256 8f984264d2458c20, output 492c13a824e75833); post-seal cross-check
  verdict: SAME with 0 discrepancies (matching 248 = 120 + 128, 6 negative eigenlines, w64_0 = 4, central kernel
  [(1, 1), (-1, -1)], geometric kernel (8, 0), joined kernel (0, 0), meridian-square +1 exclusion, and omitting-sheet
  control restoring 8)
- already on main?: origin/main (47ece044b) registers physical's C8 card at harvest row 2058 (P-876, harvest row 1987
  source review owed) with second computation: none; no independent cross-family second computation existed on record
  prior to 61da50a6d
- what would make it fail: U(1) and Z U(-2d) failing to commute or having orders other than (5, 10), w_64 zero
  multiplicity differing from 4, geometric peripheral spin kernel differing from (8, 0), joined peripheral spin kernel
  differing from (0, 0), joined meridian-square phases on the 128 containing 0 mod 20 (+1), (-1, -1) failing to act
  trivially on 248, BD_5 failing its order-20 relations or pi_1(m004) surjective lifts with trivial bounding longitude,
  any AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1 control failing
