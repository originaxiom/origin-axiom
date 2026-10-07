#!/usr/bin/env python3
"""B1604 -- GENESIS v1.26 (main's, B1602) -> v1.27 (main's): FK11 marked UNEARNABLE within F-HE/F-CI on threads and their
covers by T-NO-INDEX-IN-THREE, with the earning condition; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.27 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_26_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_26 = "2974cfeb9304246857486948bfe25b2a8cf227f3b259a19ddc6795ca0d013425"

CHANGES = [
 ("**Version 1.26 · 2026-10-07 · canonical.**", "**Version 1.27 · 2026-10-08 · canonical.**"),
 ("| FK11 | The dictionary (I-26) | UNEARNED | a frame derived from M-theory or from the principle, with its scope proved |",
  "| FK11 | The dictionary (I-26) | UNEARNED — **[v1.27] UNEARNABLE within F-HE and F-CI on any thread or cover of a thread (T-NO-INDEX-IN-THREE, B1604):** every twisted Euler characteristic on a cusped 3-manifold vanishes, so no count of flat-module cohomology there is an index with the physical shape identity n_5̄ = n_10; the class index is a difference of interior ranks in degrees one and two, governed by no characteristic class (B1603: eight kinds of reading on 442 classes). What would earn a dictionary: an even-dimensional object the weave forces, carrying a non-flat bundle whose index is the count, or the orbifold standard read as what it is — a sector selected by a character, a selection | a frame derived from M-theory or from the principle, with its scope proved; or an even-dimensional object of the weave with a non-flat bundle |"),
 ("- **v1.26 · 2026-10-07 · main B1602.** The forced cover on every thread; main's weave items renamed WM1, WM2.\n",
  "- **v1.27 · 2026-10-08 · main B1604.** The class index is not an index.\n"
  "  - FK11: UNEARNABLE within F-HE/F-CI on threads and their covers (T-NO-INDEX-IN-THREE): every twisted Euler characteristic vanishes on a cusped 3-manifold; the class index is a difference of interior ranks, no characteristic class governs it; the earning condition named (an even-dimensional object of the weave with a non-flat bundle, or a sector selected by a character — a selection).\n"
  "- **v1.26 · 2026-10-07 · main B1602.** The forced cover on every thread; main's weave items renamed WM1, WM2.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_26, "the received v1.26 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.27 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.27, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
