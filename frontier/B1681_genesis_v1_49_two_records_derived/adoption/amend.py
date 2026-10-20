#!/usr/bin/env python3
"""B1681 -- GENESIS v1.48 (main's) -> v1.49 (main's): GM1 derived given a common point (B1677, sealed; B1679, the SM
seat's W109 proof for every n, verified); the principle's form stated as the family of wordings, with a -> ab, b -> a its
smallest instance under C2b (P-206, the SM seat's proposal; B1676); the log. P-208.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.49 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_48_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_48 = "667cb61663d9f962e4f5ff3922679e1f0f5d13de22cb5aaca18af9ab7d2406cd"
CHANGES = [
 ("**Version 1.48 · 2026-10-16 · canonical.**", "**Version 1.49 · 2026-10-20 · canonical.**"),
 ("| GM1 | Two records: updates act on a pair of integer counts, ℤ² | POSTULATED |",
  "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **DERIVED given one input [v1.49]** (B1677, B1679; P-201, P-205, P-208) |"),
 ("Fork F9 is robust to word length three and fragile at four (main B749 addendum; computed in B1323, corrected at B1414). |",
  "Fork F9 is robust to word length three and fragile at four (main B749 addendum; computed in B1323, corrected at B1414). "
  "**[v1.49] Derived given one input (B1677, sealed; B1679, the SM seat's W109 proof, verified on main).** For every n ≥ 3 "
  "the only character of the free group F_n in SL(2, ℂ) fixed by every move a_i ↦ a_i a_j (or a_i ↦ a_j a_i) is the "
  "trivial one; at n = 2 the record's two moves fix exactly the trivial point and the quaternion point (0, 0, 0). So two "
  "records follow from the input **the records have a non-trivial common character in SL(2, ℂ)**; at n = 2 the finite "
  "image is then forced (tr[a, b] = −2, Q₈), and the triplet follows from that point (T2). The rank-two target stays "
  "priced (P-209 tests higher ranks), and whether this input is weaker than \"two records\" or the same choice renamed "
  "is the web seat's question, open. |"),
 ("into a theorem and a criterion (its C2a and C2b; B1323).",
  "into a theorem and a criterion (its C2a and C2b; B1323). **[v1.49] The principle's form is the family (P-206, the SM "
  "seat's proposal; B1676):** the words route ends at every Sturmian wording — the weave of words, which abelianises "
  "onto exactly the non-negative GL(2, ℤ) matrices (B1323) — and a → ab, b → a is its smallest instance, selected by "
  "the criterion C2b, not forced. Results stated of the golden rule's word, clock or tick are thread results: the "
  "tick's democratic mean belongs to the class of threads with #L ≡ #R (mod 8), not to the principle (B1676)."),
 ("- **v1.48 · 2026-10-16 · main B1662.**",
  "- **v1.49 · 2026-10-20 · main B1681.** GM1 derived given one input (B1677, sealed; B1679, the SM seat's W109 proof for "
  "every n, verified): two records follow from a non-trivial common character of the records in SL(2, ℂ), the rank-two "
  "target priced. The principle's form stated as the family of wordings, a → ab, b → a its smallest instance under C2b "
  "(P-206; B1676: the golden rule's tick is a class property). The v1.29 entry's \"the principle's tick\" reads \"the "
  "golden rule's tick\" (the history is not rewritten). The price is not re-counted here: one postulate is exchanged "
  "for one input.\n"
  "- **v1.48 · 2026-10-16 · main B1662.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_48, "the received v1.48 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.49 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.49, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
