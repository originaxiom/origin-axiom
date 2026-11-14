#!/usr/bin/env python3
"""B1904 -- the foundation at version 1.67, written by main's script of Review 80 with four corrections.

Main's script `genesis_v1_67.py` holds seven pairs: a passage of the foundation in which the owner is quoted, and the same
in plain words.  It stands as main wrote it, byte for byte, in the arc B1898 (held there by its hash) and in main's
folder of 2026-11-12.  THIS SCRIPT HOLDS NO PASSAGE.  It loads main's pairs from the arc B1898 and applies them, so that
the owner's words stand in no new file; and it differs from main's script in four things, each at main's word (its M18
to the builder) or said to main in this arc's findings:

  1. the log's entry.  Main's ended "No item is added and no status cell changes."  That is wrong: the third passage
     stands in the status cell of row FK13.  The cell's label is as it was, and the account in its bracket
     is put in plain words.  The entry says so;
  2. the entry's arc, which main wrote B[[N]], is B1904;
  3. the line that names the version is moved to 1.67, as each version before moved it.  Main's script left it;
  4. main's script printed the first 90 characters of each passage it replaces.  This one prints a passage's number
     and how often it stands, and nothing of its words.

    python3 write_version_1_67.py            # checks that every passage is there once, and writes nothing
    python3 write_version_1_67.py --write    # writes GENESIS.md
"""
import pathlib
import sys
import types

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAINS = ROOT / "frontier" / "B1898_review_80_one_hundred_findings_and_what_main_checked" / "verification" / "checks" / "genesis_v1_67.py"

ENTRY_AS_MAIN_ENDED_IT = "No item is added and no status cell changes.\n"
ENTRY_ENDS = ("No item is added and no status changes: the words of one status cell change (row FK13: the account in its bracket "
              "is put in plain words; its label is as it was).\n")
HEADER_WAS, HEADER_IS = "**Version 1.66 · 2026-11-12 · canonical.**", "**Version 1.67 · 2026-11-12 · canonical.**"


def mains():
    """main's script as a module, its last block not run (that block runs only when the script is the program).  It is read
    and compiled here, and not imported: an import leaves a folder of compiled files beside it, in the arc B1898, whose lock
    counts the files of that folder.  (Corrected 2026-11-12, after this arc was first sent: it was imported, and B1898's
    lock failed on its second run in a checkout where this arc's lock had run.)"""
    m = types.ModuleType("mains_genesis_v1_67")
    m.__file__ = str(MAINS)
    exec(compile(MAINS.read_text(encoding="utf-8"), str(MAINS), "exec"), m.__dict__)
    return m


def the_entry(m):
    entry = m.LOG_ENTRY
    assert entry.count("B[[N]]") == 1 and entry.endswith(ENTRY_AS_MAIN_ENDED_IT)
    return entry.replace("B[[N]]", "B1904")[:-len(ENTRY_AS_MAIN_ENDED_IT)] + ENTRY_ENDS


def version_1_67(text, say=lambda line: None):
    """the foundation's text at version 1.66 -> at version 1.67.  Stops if a passage, the anchor or the header is not there once."""
    m = mains()
    assert len(m.EDITS) == 7
    for number, (old, new) in enumerate(m.EDITS, 1):
        n = text.count(old)
        say("passage %d stands %d time(s)" % (number, n))
        assert n == 1, "passage %d stands %d time(s), not once" % (number, n)
        text = text.replace(old, new)
    assert text.count(m.LOG_ANCHOR) == 1, "the entry of version 1.66 is not there once"
    text = text.replace(m.LOG_ANCHOR, the_entry(m) + m.LOG_ANCHOR)
    assert text.count(HEADER_WAS) == 1 and HEADER_IS not in text, "the line that names version 1.66 is not there once"
    return text.replace(HEADER_WAS, HEADER_IS)


if __name__ == "__main__":
    page = ROOT / "GENESIS.md"
    new = version_1_67(page.read_text(encoding="utf-8"), print)
    if "--write" in sys.argv:
        page.write_text(new, encoding="utf-8"); print("written")
    else:
        print("every passage stands once; nothing written")
