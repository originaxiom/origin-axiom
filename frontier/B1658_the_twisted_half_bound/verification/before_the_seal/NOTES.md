# P-163 — the Higgs's defect in B1656's twisted, quaternionic frame (main's exploration notes, firewalled)

2026-10-15 ~14:30, after W90 (verified on main: audit/drafts/p163/verify_w90.py — one Higgs defect shared by the sectors
under B1657's UNTWISTED laws fits no assignment at 2 or 3 sigma).

quat_probe.py (B1656's sealed instrument's definitions loaded, line (1/9, 1/9) at omega):
- every sector's residue quaternion M_R is null (det ~ 1e-16);
- ANY null Higgs quaternion (det S = 0) gives rank one (1, 0, 0) in every sector: B1645's cone theorem, twisted;
- one shared null Higgs S0 perturbed by eps X: m2/m3 = k_s |det S|/|S|^2 with k_s stable to 1e-4 between eps = 1e-3 and
  1e-4, and SECTOR-DEPENDENT: trials (up, down, lep) = (1.258, 1.402, 1.042), (0.559, 0.924, 0.757), (1.107, 1.015, 1.041).
  So one Higgs CAN give sector-dependent middle masses in the twisted frame (the escape from W90's tension: the Higgs's
  defect is shared, its coefficient is not).

The candidate sealed computation (P-163):
- at omega the order-3 move fixes the identity channel and permutes i, j, k (B1656 §1 item 2), so its null symmetric
  Higgs quaternions are R(omega) and Rbar(omega) in the i, j, k part (s0 = 0): parameter-free S0;
- then k_up : k_down : k_lep on W59's lines are DEFINITE numbers (by line class), and the matter's side D_s/(2 pi L)
  (B1656) gives the other light mass; L cancels in cross-sector ratios of like masses;
- the data's middle-mass ratios (HZ2021 at M_Z): m2/m3 = 0.003685 (up), 0.01872 (down), 0.05887 (lep): down/up 5.08,
  lep/up 15.98, lep/down 3.14 — DO NOT tune to these; seal the prediction first (value contact: KIND_TABLE, L91 checklist).
- to settle first, by hand: the conjugate Higgs for the up sector (H vs Htilde: ubar = -3w vs +3w — already in M_R?);
  which light mass is the Higgs's (k|d_S|) and which the matter's (D/2piL) in each sector; first-order validity.

## 2026-10-15 ~15:00 — the twisted half bound (quat_tensor.py; exploration, random S and M only)
- B1656's coupling is a fixed bilinear form Y(s, m) in the quaternion components (printed by quat_tensor.py);
  det S = s0^2 + s.s, det M = m0^2 + m.m.
- For any NULL matter quaternion M (det M = 0): adj Y(S, M) = det S * A(M), A independent of S (spread ~1e-15, 3 x 4
  random draws). Since rank Y <= 2: sigma1 sigma2 = |det S| ||A(M)|| and sigma1^2 + sigma2^2 = ||Y(S, M)||^2, EXACTLY.
  So m2/m3 -> |det S| ||A(M_s)|| / ||Y(S, M_s)||^2 for a nearly null Higgs: B1645's half bound, twisted.
- k_s(S0) = ||A(M_s)|| |S0|^2 / ||Y(S0, M_s)||^2: the sector dependence is how M_s sits relative to the Higgs.
- To check: is ||A(M)|| = c ||M||^2 for null M (then k_s depends only on the "angle" between S0 and M_s)?

## 2026-10-15 ~15:20 — the twisted half bound, proved in part; the arc it implies
- SYMBOLIC (quat_symbolic.py): for null M = p q^T and ANY S, adj Y(S, M) = det S * A(M), A's rows (p.p, 2i p0 p1,
  -i(p0^2 - p1^2)) x (q's quadratic forms): ||A|| = 2 |p|^2 |q|^2 = 2 ||M||^2.
- So under P4' (C0's one normalisation; the matter's residue exactly null): each sector's spectrum is EXACTLY
  (1, m2/m3, 0) with m2/m3 = t, t + 1/t = ||Y(S, M_s)||^2 / (2 |det S| ||M_s||^2); for a nearly null Higgs
  m2/m3 -> k_s |d_S|, k_s = 2 ||S||^2 ||M_s||^2 / ||Y(S, M_s)||^2.
- NUMERIC (quat_tensor.py, 30 Nelder-Mead starts): ||Y(S, M)||^2 in [1, 4] ||S||^2 ||M||^2 over null S, M  =>  k_s in
  [1/2, 2]  =>  for ONE Higgs the sectors' Higgs-sourced masses lie within a factor 4 of each other. (Prove the range.)
- The data's spread (HZ2021 at M_Z, seen): m2/m3 = 0.00368, 0.0187, 0.0589 (span 16); m1/m3 = 7.3e-6, 9.4e-4, 2.8e-4
  (span 128); no choice of one light mass per sector lies within a factor 4 (by hand, central values).
- => the arc: THE TWISTED HALF BOUND (P-163, replacing the symmetric-S0 test, which the bound makes moot): T1 the
  factorisation (symbolic), T2 ||A|| = 2||M||^2, T3 the range [1, 4] (optimisation + a proof if found), T4 the exact P4'
  spectrum on W59's lines, T5 the census against HZ2021 with W90's predicate (a scoreboard: data seen), T6 a control (three
  sector-dependent Higgs fields CAN fit — the census can pass). Scope: P4', first order in the Higgs's defect, one Higgs;
  under P4 the matter's D_s/(2 pi L) adds a second light mass — the joint law is owed.

## 2026-10-15 ~15:30 — the range, in closed form (range_fit.py: exact fit, residual 5e-15 over 400 random unit draws)
||Y(u v^T, p q^T)||^2 = (1 + |u^dag p|^2)(2 - |v^T q|^2) for unit u, v, p, q  =>  range [1, 4], attained.
So k_s = 2/((1 + x_s)(2 - y_s)) in [1/2, 2], x_s = |u^dag p_s|^2 (the Higgs's left factor against the sector's), y_s =
|v^T q_s|^2 (right factors, bilinear). One Higgs: the sectors' middle masses within a factor 4 (P4', first order in the
Higgs's defect). To prove symbolically in the arc (expand both sides with u, v, p, q symbolic and their conjugates).

## 2026-10-15 ~16:30 — the joint law (joint_law.py; exploration)
- det Y(S, M)/(det S det M) is not a simple trace pairing (no candidate fits); set aside.
- adj Y(S, M) = det S A(M) + det M A~(S) + O(eps^2) (relative residual 1.5e-3 at eps 1e-3, 1.5e-4 at 1e-4): at leading
  order the two defects ADD in the adjugate. So under P4 each sector's middle mass ~ ||d_S A(M_s) + d_M,s A~(S)|| /
  ||Y(S, M_s)||^2, with d_M,s = D_s/(2 pi L) sector-dependent (B1656: 1.03, 2.46, 2.74; leptons 0 on W59's lines).
- Direction (no data used beyond what is known): the leptons have no matter term on W59's lines yet nature's largest
  m2/m3; the up quarks' smallest m2/m3 would need destructive interference of the two terms — a tuning. The next arc
  (B1659?): the joint law in closed form (A~(S), the relative geometry of A(M) and A~(S)), and its census.
