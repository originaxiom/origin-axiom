#!/usr/bin/env python3
"""B1600 -- GENESIS v1.23 (main's, B1497) -> v1.24 (main's): THE WEAVE adopted -- the owner's rule named; the test weave or
thread; PF1-PF3 and GM1-GM4 read as weave statements, SE1, SE2 and T-ROOT as thread statements; W1-W4 recorded at FK14 with
their verification; the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.24 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_23_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_23 = "3416d9490480508b80fad8da2feb793edd85fc98aba0a5867c1e837eb73f37b2"

CHANGES = [
 ("**Version 1.23 · 2026-10-07 · canonical.**", "**Version 1.24 · 2026-10-07 · canonical.**"),
 ("## 0. How to read and use it\n",
  "## 0. How to read and use it\n\n**[v1.24] THE WEAVE — the owner's rule, named (2026-10-07; `docs/THE_WEAVE.md`; B1600).** A *thread* is one object the principle allows (m000, m003, m004, +LLLR …): one closed path of the moves through the shared fibre, the two records. *The weave* is the joint action of every allowed move on the records and everything it forces. Before any arc: **weave or thread?** A weave result takes every thread under a rule stated in advance with none hand-picked, is defined by the joint action, and claims about all threads at once; a thread result is anything read on one thread or its covers, labelled so (`weave_or_thread` in every verdict file from B1491) and never presented as the answer to a weave question. On this page §1–§2 (PF1–PF3, GM1–GM4: the records and the moves) are weave statements; §4's selectors SE1, SE2 and T-ROOT pick one thread and are thread statements; the frames of §5 are thread instruments, each built on one thread's holonomy.\n"),
 ("Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines. ",
  "Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines. **[v1.24] The weave's three (the SM seat's W1–W4, verified on main at B1600):** the two records have exactly three non-zero parities; each move fixes one and any two moves cycle all three — the three belongs to no single move (W1); every act of odd trace is a 3-cycle on them (the parity lemma, 988 signed words); the one point of the fibre's characters every move fixes is the quaternion point (W2), from which every odd-trace thread — m004, m003, +LLLR among them — receives the binary tetrahedral group 2T with A₄ below (W3, 54 words to length six); the shared fibre carries one line per non-zero parity and every odd-trace thread acts on the three as one irreducible A₄ triplet, split on even-trace threads (W4). READING, not adopted: the three generations are this triplet — the orbifold standard realised on the shared fibre with no thread chosen. Decisive and open, **W6:** whether each parity line carries a generation (5̄ + 10 with its chirality), which needs a weave instrument. The sign and the swap (GM5b, GM5c) are OPEN; W1–W4 hold either way, the weave's group on the triplet of order 24 with L and R, 48 with all four. "),
 ("  - FK14: T-ROOM-NEEDS-GENUS — the room is the act's invariant closed homology of the fibre of a cover, zero at genus one, so it needs a non-abelian cover of the register; the root has none to degree eight, the sign-twin one at degree five (o10_150691), where the count is still one. FK4 and FK14 read as one question.",
  "  - FK14: T-ROOM-NEEDS-GENUS — the room is the act's invariant closed homology of the fibre of a cover, zero at genus one, so it needs a non-abelian cover of the register; the root has none to degree eight, the sign-twin one at degree five (o10_150691), where the count is still one. FK4 and FK14 read as one question.\n"
  "- **v1.24 · 2026-10-07 · main B1600.** The weave.\n"
  "  - §0: the owner's rule named — thread, the weave, the test weave or thread; §1–§2 weave statements, SE1/SE2/T-ROOT thread statements, the frames thread instruments; `weave_or_thread` on every verdict file from B1491.\n"
  "  - FK14: the weave's three — the three parities of the two records, cycled by every odd-trace thread, the quaternion point, 2T with A₄, the irreducible triplet (the SM seat's W1–W4, verified on main). Reading: the three generations are this triplet; W6 (what each line carries) decides, and needs a weave instrument. The weave program opened on main."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_23, "the received v1.23 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.24 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.24, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
