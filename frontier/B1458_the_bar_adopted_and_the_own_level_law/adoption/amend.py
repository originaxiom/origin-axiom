#!/usr/bin/env python3
"""B1458 -- GENESIS v1.3 -> v1.4: the bar is on main; the own-level law's refinement.  Same form as B1454's and B1456's.

    python3 amend.py            # writes GENESIS.md
    python3 amend.py --check    # exit 1 if the root file is at version 1.4 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_3_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_3 = "36c2a83d3c20930009ee428483d8f793e6df46a6884b167c2db0f104b38be0c3"
BAR_OLD = "THE_BAR.md (under docs/ on the SM seat's branch; not yet on main)"
CHANGES = [
 ("**Version 1.3 · 2026-10-02 · canonical.**", "**Version 1.4 · 2026-10-03 · canonical.**"),
 ("with the three seats' results of the same day folded in, each marked **[v1.3]**.",
  "with the three seats' results of the same day folded in, each marked **[v1.3]**. v1.4 (main's B1458) brings the bar onto\nmain and records what the own-level law is not, each marked **[v1.4]**."),
 ("(main B1439; **[v1.2]** 87 of 536 manifolds, sm:B1517 C5; no criterion in the fibre torsion and the sign decides which, sm:B1518), among them m369 (8) and s639 (16) (main B1434) |",
  "(main B1439; **[v1.2]** 87 of 536 manifolds, sm:B1517 C5; no criterion in the fibre torsion and the sign decides which, sm:B1518; **[v1.4]** re-derived on main by manifold and group structure: 22 (G, sign) strata each hold a firing and a silent manifold, the smallest m369 against o9_00001, both ℤ/12 and sign −, B1458), among them m369 (8) and s639 (16) (main B1434) |"),
 ("  - Named, not changed: THE_BAR is a page of the SM seat's branch and is not yet on main.",
  "  - Named, not changed: THE_BAR is a page of the SM seat's branch and is not yet on main.\n"
  "- **v1.4 · 2026-10-03 · main B1458.** The bar adopted on main for the class-index frame (`docs/THE_BAR.md`, from sm:B1518,\n"
  "  its census claim re-derived by manifold and group structure); §5 and FK9 now point to it on main. No status changes."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_3, "the received v1.3 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    n = t.count(BAR_OLD); assert n == 3, n
    t = t.replace(BAR_OLD, "`docs/THE_BAR.md` (**[v1.4]** on main from B1458)")
    return t, n


def main(argv):
    t, n = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.4 ·" in cur and cur != t:
            print("GENESIS.md is at v1.4 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.4: PASS (%d changes, %d relabels)" % (len(CHANGES), n)); return 0
    open(OUT, "w").write(t); print("wrote GENESIS.md v1.4: %d changes, %d relabels" % (len(CHANGES), n)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
