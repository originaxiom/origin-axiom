#!/usr/bin/env python3
"""B1683 -- GENESIS v1.49 (main's) -> v1.50 (main's): GM1 regraded from DERIVED given one input to POSTULATED, in an
equivalent form -- the input characterises two records, it is not weaker (the web seat's read; B1682, with the SM seat's
W110, verified) -- with the extension of the moves and the reading of persistence named beside it (P-212); GM5b's "only
this reading never settles" scoped to the two readings B1662 compared (R65-3); the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.50 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_49_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_49 = "347ea2d24d63687c3b9fab3cbac4ba98c09237c1721939ea51b413d1760506f4"
CHANGES = [
 ("**Version 1.49 · 2026-10-20 · canonical.**", "**Version 1.50 · 2026-10-21 · canonical.**"),
 ("| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **DERIVED given one input [v1.49]** (B1677, B1679; P-201, P-205, P-208) |",
  "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **POSTULATED, in an equivalent form [v1.50]** (DERIVED given one input at v1.49, regraded; B1677, B1679, B1682; P-201, P-205, P-208, P-212) |"),
 ("is the web seat's question, open. |",
  "is the web seat's question, open. **[v1.50] Answered: equivalent, not weaker (the web seat's read; B1682, with the "
  "SM seat's W110, verified on main).** For n ≥ 2 the input holds exactly when n = 2 — at n ≥ 3 by B1679, at n = 2 by "
  "the quaternion point — so, as a statement about the number of records, it is GM1 in another form. v1.49's status "
  "read it as a weaker premise; GM1 is an assumption, now stated as an invariance of the moves. The same holds on words, "
  "with no target: for n ≥ 3 no non-trivial conjugacy class of F_n keeps even its length under every move, and at "
  "n = 2 the classes the record's moves keep are the powers of [a, b], whose trace is PF1's κ (B1682). So GM1 is tied "
  "to GM4's punctured torus and to PF1's commutator, without deriving either. **What the form assumes, named:** "
  "\"persistent\" means fixed up to the target's conjugation (read as a finite orbit, every character with finite image "
  "persists at every n, and nothing is selected); and the moves extend beyond two records democratically, every "
  "a_i ↦ a_i a_j. A surface's moves keep the boundary word at every genus, so on words the count of two rests on that "
  "extension; on characters, whether the prime 2 then gives two records is open (P-211). |"),
 ("at equal strength only this reading never settles (the walk on SL(2, ℤ) is transient, Kesten; the reading in which "
  "the pull-back only undoes the last step is recurrent).",
  "at equal strength, of the two readings B1662 compared, only this one never settles (the walk on SL(2, ℤ) is "
  "transient, Kesten, and its returns saturate; under the reading in which the pull-back only undoes the last step the "
  "walk is recurrent and the returns grow) **[v1.50: \"only\" scoped to those two readings, Review 65, R65-3]**."),
 ("- **v1.49 · 2026-10-20 · main B1681.**",
  "- **v1.50 · 2026-10-21 · main B1683.** GM1 regraded from DERIVED given one input (v1.49) to POSTULATED, in an "
  "equivalent form: for n ≥ 2 a non-trivial common character in SL(2, ℂ) (B1679) or a non-trivial kept conjugacy class "
  "(B1682, the SM seat's W110) exists exactly when n = 2, so the input characterises two records and is not weaker (the "
  "web seat's read, checked on main); the democratic extension of the moves and persistence as fixed up to conjugation "
  "named beside it (P-212). GM5b's \"only this reading never settles\" scoped to the two readings B1662 compared "
  "(R65-3). The price is not re-counted: GM1 stays one assumption, in an equivalent form.\n"
  "- **v1.49 · 2026-10-20 · main B1681.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_49, "the received v1.49 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.50 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.50, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
