# P-592, decided by main at Review 74 (2026-11-04, S299)

The reader's report (returned by hand-back; the harness refused its file write) advised DECLINE for all six. Main verified
at source on the lane's 90149211 before deciding:
- custody: each checks.py's sha256 equals its pin in its SOURCE_REVIEW_INVENTORY.json (all six);
- no data contact: no measured-value word in any checks.py (all six);
- package 4 (neutral_up_lift): Z = charge*s.eye(10), a scalar matrix (checks.py ~121), so every commutator with Z is
  identically zero; the 'charged Cartan must fail' control checks comm(h, e) != 0 with nothing substituted -- vacuous;
- package 5 (neutral_full_kernel): charged_counts' up count is 2*int(kminus == 0) + 2*int(kplus == 0) (the claim as a
  formula) and the lepton ranks enter as arguments -- the counts encode the premises;
- package 6 (register_flavour_joint): the three 'states' are (source, g_L.source, g_R.source) read by three fixed probes,
  table 1 + I; its own covariant test shows the quartic unchanged when the reference co-moves -- one state seen from three
  fixed references; checks.py carries no tolerance or max_err, so the agy lane's reported 'max_err' run was not this
  package's exact code alone.
DECISION: all six DECLINED for admission (none tests a result main relies on; three verified vacuous or circular; package 2
the closest call, B1652 F3's scoped cells, whose verdict cannot move). The lane may run any package on its own branch as seat
evidence (READ, not VERIFIED). Main's own-code checks noted for when the rows move: (a) w.b = 0 and w.(10, 6, 4) = 0 and
(b) the chi^3 != 1, chi^10 != 1 roster criterion on P-396 and P-593; (c) [Y0, Y0+] = H/10 with the 12 -> 9 stabiliser on
P-396; (d) the quartic r^4 + s_x^2 under 2O with the fixed-versus-co-moving reference question on P-593.
