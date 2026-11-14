#!/usr/bin/env python3
"""B1933 -- the foundation at version 1.69: the m000 row of the table of frames, and the list "Computed nowhere yet".

Card C21 of the building session (main's M33 and M36; register row P-320, GENESIS currency). Three places of the
foundation change, each named here by its whole old line, which must stand once:

  1. the table's row for m000: F-FC and F-CI computed (B1926; the web seat's W-C8 part 2a, harvest rows 1755 and 1768;
     B1926's addendum, on three codes); F-HE and F-AP still never computed, offered to the SM seat (its page, M28);
  2. the list's entry "the Gieseking manifold m000 in any frame" narrowed to the two frames not computed;
  3. the list's first entry, the harmonic frame's counts outside m004's levels, marked as computed once by agy-exp's
     X-NEVER (harvest row 1797), its second computation owed; it stays on the list (main's M36).

No item's status changes but these cells; the entry of the log stands above 1.68's, and the version's line moves.

    python3 write_version_1_69.py            # checks, and writes nothing
    python3 write_version_1_69.py --write    # writes GENESIS.md
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LOG_HEAD = "## 10. Version log"
HEADER_WAS, HEADER_IS = "**Version 1.68 · 2026-11-13 · canonical.**", "**Version 1.69 · 2026-11-14 · canonical.**"
ROW_WAS = "| m000, the Gieseking manifold | never computed | never computed | never computed | never computed |\n"
ROW_IS = ("| m000, the Gieseking manifold | **[v1.69]** closed: b₁ = 1 and cusp rank 1 at every level n = 1 to 8 (B1926, "
          "verifying an independent sealed computation, harvest rows 1755 and 1768) | **[v1.69]** no sector module at any odd "
          "level: the cusp's meridian inverts the scar, so no class over a character trivial on it is free on the scar; "
          "over the characters twisted by the orientation every class is (B1926); the twisted classes are the double "
          "cover's matter seen from below (B1926's addendum; the result stands on three codes). Whether the twisted "
          "modules count as the frame's matter is a stated choice (B1926) | never computed (offered for computation, "
          "2026-11-14) | never computed (offered for computation, 2026-11-14) |\n")
LIST_WAS = "- the Gieseking manifold m000 in any frame;\n"
LIST_IS = ("- **[v1.69]** the Gieseking manifold m000 in F-HE and F-AP (offered for computation); F-FC and F-CI are "
           "computed (B1926, the table above);\n")
FIRST_WAS = ("- the harmonic frame's counts on any state outside m004's levels (**[v1.6]** its projective family exists on every word\n"
             "  state to length 12, sm:B1523);\n")
FIRST_IS = ("- the harmonic frame's counts on any state outside m004's levels (**[v1.6]** its projective family exists on every word\n"
            "  state to length 12, sm:B1523); **[v1.69]** computed once, on eight chiral word states outside m004's levels, by\n"
            "  an independent computation (harvest row 1797), its second computation owed: it stays on this list until then;\n")
ENTRY = ("- **v1.69 · 2026-11-14 · B1933.** The m000 row of the table of frames: F-FC and F-CI computed (B1926, verifying "
         "an independent sealed computation; its addendum on three codes); F-HE and F-AP not computed, offered for computation. "
         "\"Computed nowhere yet\": the m000 entry narrowed to those two frames; the harmonic frame's counts outside m004's "
         "levels marked as computed once (harvest row 1797), the second computation owed, and kept on the list. Register row "
         "P-320.\n")


def version_1_69(text, say=lambda line: None):
    """the foundation's text at version 1.68 -> at version 1.69; stops if a line it replaces is not there once"""
    i = text.index(LOG_HEAD)
    living, log = text[:i], text[i:]
    for was, now, name in ((ROW_WAS, ROW_IS, "the m000 row"), (LIST_WAS, LIST_IS, "the list's m000 entry"),
                           (FIRST_WAS, FIRST_IS, "the list's first entry")):
        n = living.count(was)
        say("%s stands %d time(s) in §§ 0 to 8" % (name, n))
        assert n == 1, "%s stands %d time(s), not once" % (name, n)
        living = living.replace(was, now)
    assert log.count("\n- **v1.68 ") == 1, "the entry of version 1.68 is not there once"
    k = log.index("\n- **v1.68 ") + 1                      # each version's entry stands above the one before it
    log = log[:k] + ENTRY + log[k:]
    text = living + log
    assert text.count(HEADER_WAS) == 1 and HEADER_IS not in text, "the line that names version 1.68 is not there once"
    return text.replace(HEADER_WAS, HEADER_IS)


if __name__ == "__main__":
    page = ROOT / "GENESIS.md"
    new = version_1_69(page.read_text(encoding="utf-8"), print)
    if "--write" in sys.argv:
        page.write_text(new, encoding="utf-8")
        print("written")
    else:
        print("every line stands once; nothing written")
