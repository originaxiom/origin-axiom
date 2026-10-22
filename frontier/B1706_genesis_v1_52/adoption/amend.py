#!/usr/bin/env python3
"""B1706 -- GENESIS v1.51 (main's) -> v1.52 (main's), P-237 and Review 67's R67-3, after Review 67's full suite: sm:B1518's
sentences scoped to what B1458 re-derived (the own-level strata; THE_BAR's null model, grading and the torsion's AUC the
seat's, unverified, row 823); of the audit lane's R57 only the quotient F2 -> Z^2 re-derived (B1457, row 189); R89 tagged
(row 981); v1.51's tags lifted where the seat result is now verified (rows 888, 937, 939; B1689) and scoped where partly
(rows 828, 897, 898, 1061; and §5's note: sm:B1369 verified, sm:B1368, B1370, B1385 partly, B1690); FK10: the newest
frame's hierarchy uses the tagged unit as the coupling triplet R uses it (B1700); the log.  The version log's own lines are
not rewritten.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.52 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_51_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_51 = "fcf63934785d177c8c2728e01d3f6eb56cd29b95ed59888cb4bc7777404755e3"
R57 = " [of R57 only its quotient F₂ → ℤ² is re-derived on main (B1457); the rest the audit lane's, unverified on main: row 189; v1.52]"
B1518 = " [v1.52: the own-level strata re-derived on main (B1458); THE_BAR's null model and grading and the torsion's AUC the seat's, unverified on main: row 823]"
CHANGES = [
 ("**Version 1.51 · 2026-10-21 · canonical.**", "**Version 1.52 · 2026-10-22 · canonical.**"),
 # (a) sm:B1518, the body sites (273, 350, 422); the log's (555, 570) are history
 ("no criterion in the fibre torsion and the sign decides which, sm:B1518;",
  "no criterion in the fibre torsion and the sign decides which, sm:B1518 [v1.52: this claim re-derived on main, B1458; the seat's further claims read, not re-derived, row 823];"),
 ("(**[v1.4]** on main from B1458) (sm:B1518), a card, the base rate", "(**[v1.4]** on main from B1458) (sm:B1518" + B1518 + "), a card, the base rate"),
 ("(**[v1.2]** sm:B1518; GAP4)", "(**[v1.2]** sm:B1518" + B1518 + "; GAP4)"),
 # (b) R57, the body sites (107, 118, 194, 421, 486); the log's (520, 522) are history
 ("its \"RP\" is the core's LP (the audit lane's R57).", "its \"RP\" is the core's LP (the audit lane's R57" + R57 + ")."),
 ("(R57; the audit lane's operational contract)", "(R57" + R57 + "; the audit lane's operational contract)"),
 ("audit lane's words (R57): *", "audit lane's words (R57" + R57 + "): *"),
 ("filling descent is one candidate (sm:B1508, R57) |", "filling descent is one candidate (sm:B1508, R57" + R57 + ") |"),
 ("| GM4, the puncture CONDITIONAL (R57) |", "| GM4, the puncture CONDITIONAL (R57" + R57 + ") |"),
 # (c) R89, the body site (375); the log's (631) is history
 ("the audit lane's R89 (\"narrow GAP6", "the audit lane's R89 [the lane's, read and credited, unverified on main: row 981; v1.52] (\"narrow GAP6"),
 # (d) v1.51's tags, lifted or scoped
 (" [the seat's, unverified on main: row 939; v1.51]", " [verified on main since, B1689: row 939; v1.52]"),
 (" [the seat's, unverified on main: row 939, P-156; v1.51]", " [verified on main since, B1689: row 939; v1.52]"),
 (" [the seat's, unverified on main: row 937, P-156; v1.51]", " [verified on main since, B1689: row 937; v1.52]"),
 (" [the seat's, unverified on main: row 888; v1.51]", " [verified on main since, B1689, given Garland–Raghunathan: row 888; v1.52]"),
 (" [the seat's, unverified on main: rows 897, 898; v1.51]",
  " [partly verified on main since, B1689: Lemmas F and F′ checked; the census, Lemma G″, Proposition D and Corollary G not re-derived: rows 897, 898; v1.52]"),
 (" [the seat's, unverified on main: row 828; v1.51]", " [partly verified on main since, B1690: P2 and P5; the rest the seat's: row 828; v1.52]"),
 (" [the seat's, unverified on main: its c-gauge frame, row 1061, P-053; v1.51]",
  " [partly verified on main since, B1689: its c-gauge frame's CKM clause; the PMNS cells the seat's: row 1061; v1.52]"),
 ("the verifications are queued by consequence, P-229).",
  "the verifications are queued by consequence, P-229). **[v1.52] Verified on main since: sm:B1369 (B1690, row 646). Partly: "
  "sm:B1368, sm:B1370 and sm:B1385 (B1690; rows 645, 647, 660 name the cells re-derived).**"),
 # (e) FK10: the Higgs's end data (B1700)
 ("The results built on this (B1642, B1644–B1646) carry both conditions. | an end condition derived from physics (sL-8) |",
  "The results built on this (B1642, B1644–B1646) carry both conditions. **[v1.52] The Higgs's end data are this unit (B1700).** "
  "The newest frame's cusp hierarchy (B1691, B1694–B1699) needs the Higgs to carry one unit of end data on v₊. That is the "
  "tagged unit used as the coupling triplet R uses it, not a second postulate. Given the unit (W46's uniform twist), the "
  "weight-3/2 sections of ρ_T = ρ_R form a three-dimensional space, W46's three. ∂R is its only member holomorphic off v₊ "
  "and the only one giving a hierarchy, so those results hold given Λ, the unit and H-cov in R's own module. "
  "| an end condition derived from physics (sL-8) |"),
 # the log
 ("- **v1.51 · 2026-10-21 · main B1685.**",
  "- **v1.52 · 2026-10-22 · main B1706.** P-237 and Review 67's R67-3, after Review 67's full suite. sm:B1518's statements "
  "in the body are scoped to what B1458 re-derived (the own-level strata); THE_BAR's null model and grading and the "
  "torsion's AUC stay the seat's, unverified (row 823). The v1.2 and v1.4 entries below are read in that scope. Of the audit "
  "lane's R57 only the quotient F₂ → ℤ² is re-derived on main (B1457); the body's five sites say so, and the log's (v1.x) "
  "are read so. R89 is tagged (row 981). v1.51's tags are lifted where the seat's result is now verified on main (rows "
  "888, 937, 939; B1689; and §5's sm:B1369, B1690) and scoped where it is partly verified (rows 828, 897, 898, 1061; "
  "sm:B1368, B1370, B1385). FK10 records that the Higgs's end data are the tagged unit (B1700). No status changes.\n"
  "- **v1.51 · 2026-10-21 · main B1685.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_51, "the received v1.51 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.52 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.52, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
