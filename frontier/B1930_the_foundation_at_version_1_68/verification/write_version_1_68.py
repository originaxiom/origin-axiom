#!/usr/bin/env python3
"""B1930 -- the foundation at version 1.68: its paths into the moved folders.

The record's historical folders moved under docs/archive/ (docs/REORGANIZATIONS.md, its third entry; card C18 of the
building session, approved by main in its M28). The foundation is changed only by a version, so its paths into the
moved folders change here, by this script, in the same patch as the move. Six paths stand in its living sections
(§§ 0 to 8): four into philosophy/, one into paths/, one into speculations/. The version log (§ 10) is dated text and
keeps its paths as written. No item is added and no status changes; no word but the paths changes.

This script holds no sentence of the foundation: it replaces each path, which it names, and checks that each stands once
in §§ 0 to 8 and that none of the six is left there.

    python3 write_version_1_68.py            # checks, and writes nothing
    python3 write_version_1_68.py --write    # writes GENESIS.md
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PATHS = ("philosophy/P000_what_is_not_nothing.md", "philosophy/P019_the_genesis_axiom_chain.md",
         "philosophy/P008_non_cancellation_is_fricke_vogt.md", "philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md",
         "paths/PATHS.md", "speculations/S_THE_FIELDS_GENESIS.md")
ARCHIVE = "docs/archive/"
LOG_HEAD = "## 10. Version log"
HEADER_WAS, HEADER_IS = "**Version 1.67 · 2026-11-12 · canonical.**", "**Version 1.68 · 2026-11-13 · canonical.**"
ENTRY = ("- **v1.68 · 2026-11-13 · B1930.** Paths only: the record's historical folders moved under `docs/archive/` "
         "(`docs/REORGANIZATIONS.md`, its third entry), and the six paths of §§ 0 to 8 into `philosophy/`, `paths/` and "
         "`speculations/` are written so. No item is added and no status changes; the version log keeps its paths as written.\n")


def version_1_68(text, say=lambda line: None):
    """the foundation's text at version 1.67 -> at version 1.68; stops if a path, the log or the header is not there as expected"""
    i = text.index(LOG_HEAD)
    living, log = text[:i], text[i:]
    for p in PATHS:
        n = living.count("`" + p)
        say("%s stands %d time(s) in §§ 0 to 8" % (p, n))
        assert n == 1, "%s stands %d time(s), not once" % (p, n)
        living = living.replace("`" + p, "`" + ARCHIVE + p)
    assert log.count("\n- **v1.67 ") == 1, "the entry of version 1.67 is not there once"
    k = log.index("\n- **v1.67 ") + 1                      # each version's entry stands above the one before it
    log = log[:k] + ENTRY + log[k:]
    text = living + log
    assert text.count(HEADER_WAS) == 1 and HEADER_IS not in text, "the line that names version 1.67 is not there once"
    return text.replace(HEADER_WAS, HEADER_IS)


if __name__ == "__main__":
    page = ROOT / "GENESIS.md"
    new = version_1_68(page.read_text(encoding="utf-8"), print)
    if "--write" in sys.argv:
        page.write_text(new, encoding="utf-8")
        print("written")
    else:
        print("every path stands once; nothing written")
