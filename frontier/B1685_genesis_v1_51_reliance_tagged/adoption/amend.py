#!/usr/bin/env python3
"""B1685 -- GENESIS v1.50 (main's) -> v1.51 (main's): every reliance on a seat result that is not verified on main, found
untagged by Review 66's reliance census, now carries "the seat's, unverified" with its harvest row (P-228, R66-5); FK11's
W45 and W46, registered when written, read as verified since (B1632, B1641); the GM1 row's tie to PF1 read as circular
through kappa unless PF1 is read rank-free (the SM seat's relay 168; P-221); the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.51 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_50_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_50 = "98a8dda5ee926d1943b6dd801fb2fb770fa665d1c793c37e17bd34392659ca12"
U = " [the seat's, unverified on main: %s; v1.51]"
CHANGES = [
 ("**Version 1.50 · 2026-10-21 · canonical.**", "**Version 1.51 · 2026-10-21 · canonical.**"),
 # GM1: the tie to PF1 (P-221)
 ("So GM1 is tied to GM4's punctured torus and to PF1's commutator, without deriving either.",
  "So GM1 is tied to GM4's punctured torus and to PF1's commutator, without deriving either. **[v1.51] Joined through κ the "
  "tie is circular, since PF1's formal face is written for the two letters (the SM seat's relay §168; P-221): what B1682 "
  "shows without circularity is that the moves keep the commutator class at n = 2 and nothing at n ≥ 3; a join to PF1 "
  "needs PF1's rank-free reading.**"),
 # the generated state space
 ("| DERIVED, at the level of definition (sm:B1384) |", "| DERIVED, at the level of definition (sm:B1384" + U % "row 659" + ") |"),
 # GM5c's notes (v1.30, v1.33, v1.36)
 ("reversed by P: the SM seat's W30).", "reversed by P: the SM seat's W30" + U % "row 946" + ")."),
 ("W28's naturality rules the record's flat counts (±3);", "W28's naturality" + U % "row 944" + " rules the record's flat counts (±3);"),
 ("Where c is gauge (W44), TM1 and TM2", "Where c is gauge (W44" + U % "its c-gauge frame, row 1061, P-053" + "), TM1 and TM2"),
 ("In W24's frame only c is flavour and nothing is constrained.", "In W24's frame" + U % "row 939" + " only c is flavour and nothing is constrained."),
 # §5: the frames-by-object table
 ("| m000, the Gieseking manifold | never computed | never computed | never computed | never computed |",
  "| m000, the Gieseking manifold | never computed | never computed | never computed | never computed |\n\n"
  "**[v1.51] The seats' results in this table** — the SM seat's sm:B1368–B1388, B1501, B1503, B1515, B1522, B1523, B1532 and "
  "B1534–B1536, B1544, B1546, and the audit lane's R40 and F01 — **are the seat's, unverified on main, except where a cell "
  "says otherwise** (Review 66's reliance census, `docs/progress/REVIEW_66_RELIANCE_CENSUS.md`; the verifications are "
  "queued by consequence, P-229)."),
 # GAP2 and GAP3
 ("(sm:B1544, sm:B1545; checked on main on 390 readings)", "(sm:B1544, sm:B1545; checked on main on 390 readings; the proofs" + U % "rows 897, 898" + ")"),
 ("(sm:B1392 places the count at the", "(sm:B1392" + U % "row 667" + " places the count at the"),
 ("+1 and +1 on m010 (R40),", "+1 and +1 on m010 (R40" + U % "rows 711, 712" + "),"),
 ("sources between its ends (R19, R24),", "sources between its ends (R19, R24" + U % "rows 71, 539" + "),"),
 ("(R69) — each fenced by its author as not a physical count.", "(R69" + U % "the audit lane's, no row yet, P-230" + ") — each fenced by its author as not a physical count."),
 # FK9
 ("(sm:B1521 C1, with sm:B1512 Lemma I)", "(sm:B1521 C1, with sm:B1512 Lemma I" + U % "Lemma I, row 687" + ")"),
 ("(main's L242 (b); sm:B1522, PROVED, frame F-HE)", "(main's L242 (b); sm:B1522, PROVED by the seat, frame F-HE; verified on main on M₁–M₆ only, row 827 [v1.51])"),
 ("On the word states (sm:B1523, PROVED):", "On the word states (sm:B1523, PROVED by the seat" + U % "row 828" + "):"),
 ("(sm:B1527, PROVED, run as sealed)", "(sm:B1527, PROVED by the seat, run as sealed; its Part H verified on main, Part A" + U % "row 832" + ")"),
 ("(the SM seat's W65, W67)", "(the SM seat's W65" + U % "row 1125" + ", W67, verified)"),
 # FK11
 ("(the SM seat's W45, given Λ, registered):", "(the SM seat's W45, given Λ, registered; **[v1.51] verified on main since, B1632**):"),
 ("(the SM seat, registered, not re-run on main):", "(the SM seat, registered, not re-run on main; **[v1.51] both verified on main since, B1632 and B1641**):"),
 # FK12
 ("Exact, from the SM seat's sm:B1528 (its own code at m004's complete point):", "Exact, from the SM seat's sm:B1528 (its own code at m004's complete point" + U % "row 833, adopted as consistent with B1465" + "):"),
 # FK14
 ("the SM seat's Theorem C (sm:B1535) caps the count", "the SM seat's Theorem C (sm:B1535" + U % "row 888" + ") caps the count"),
 ("has room 3 and reaches two (sm:B1547);", "has room 3 and reaches two (sm:B1547" + U % "rows 904–906" + ");"),
 ("— W24's D4 proves the chiral gauge reading", "— W24's D4" + U % "row 939, P-156" + " proves the chiral gauge reading"),
 ("give at most two complete generations (W23);", "give at most two complete generations (W23" + U % "row 937, P-156" + ");"),
 # the frontier list
 ("(the cloud seat's memo 122 is NEGATIVE for the", "(the cloud seat's memo 122" + U % "row 371, scheduled" + " is NEGATIVE for the"),
 # the log
 ("- **v1.50 · 2026-10-21 · main B1683.**",
  "- **v1.51 · 2026-10-21 · main B1685.** Review 66's reliance census (P-124) found GENESIS relying, untagged, on seat results "
  "not verified on main; each such site now carries \"the seat's, unverified on main\" with its harvest row (P-228), and §5's "
  "frames-by-object table carries one note for its seat-sourced cells. FK11's W45 and W46 read as verified since (B1632, "
  "B1641). GM1's tie to PF1 read as circular through κ unless PF1 is read rank-free (P-221). No status changes; nothing is "
  "re-graded. The verifications are queued by consequence (P-229).\n"
  "- **v1.50 · 2026-10-21 · main B1683.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_50, "the received v1.50 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.51 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.51, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
