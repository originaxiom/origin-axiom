#!/usr/bin/env python3
"""B1466 -- GENESIS v1.8 (main's, B1463) -> GENESIS v1.9 (main's): the count is a bit at the counted point (FK12 (ii)), the
flatness of every frame named as a gap (GAP6; lead L244), and the fresh reader's confirmation in the observer line.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.9 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_8_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_8 = "2d652d30c1cb68332d4d8c4c8cd87eba7e3206cb1e4d0e6b815472f7ae02e152"

CHANGES = [
 ("**Version 1.8 · 2026-10-03 · canonical.**", "**Version 1.9 · 2026-10-03 · canonical.**"),
 # FK12 (ii): the count is a bit at the counted point
 ("and a vacuum in the harmonic sense is a direct sum, which has no order.",
  "and a vacuum in the harmonic sense is a direct sum, which has no order. **[v1.9]** At the counted point itself (main B1466, "
  "sealed): the two orders count −1 and +1 and are each other's dual seen through the inversion, so their counts are opposite by "
  "L1–L2; the mixed direction is unobstructed and leads to an irreducible module — the two pieces fused — that counts 0, as the "
  "direct sum does. The flat configurations near the split point are richer than a bit; **the count is a bit**: ±1 on the two "
  "orders, 0 side by side, 0 fused — \"both at once\" cancels. A source along one line does not choose (t and −t are the same "
  "extension); a source on both lines drives into the fused, count-zero region unless the potential's mixing quartic returns it "
  "to an axis — a quantity on no report."),
 # GAP6: the flatness
 ("  of it has been turned into a potential, a breaking or a running that fixes a value.\n",
  "  of it has been turned into a potential, a breaking or a running that fixes a value.\n"
  "- **[v1.9] GAP6, the flatness.** Every frame on this page is a frame of flat bundles, and a flat bundle has ch = rk: no\n"
  "  index built on it can tell 27 from 27̄ (Chern–Weil; the record's Chern–Weil row). The chirality of the Standard Model is a\n"
  "  statement about curvature — instantons, a bulk — that no flat frame carries. Named as a gap on the web seat's reading of\n"
  "  2026-10-03 (lead L244), which sorts the record's negatives into three kinds — symmetry pairing things that cancel, the\n"
  "  absence of curvature, the absence of uniqueness — with three remedies: a breaking (GAP3, FK12), curvature (this gap), a\n"
  "  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.\n"),
 # the observer line: confirmation from a fresh reader
 ("choice\" (B717, with B716 and B723). **[v1.3]** B723's identification",
  "choice\" (B717, with B716 and B723). **[v1.9]** A fresh reader (the web seat, 2026-10-03; lead L244) reached this sentence from "
  "the record's negatives alone — every positive at an interface, none in the object — without having read it here: taken as "
  "confirmation that the thesis is forced by the data, not as a new reading. **[v1.3]** B723's identification"),
 ("  Lead L243 (a) paid.",
  "  Lead L243 (a) paid.\n"
  "- **v1.9 · 2026-10-03 · main B1466.** Three additions, no status change.\n"
  "  - FK12 (ii): the counted point computed (B1466, sealed): the two orders ±1 and dual through the inversion; the fused\n"
  "    module irreducible and counting 0; the count a bit; the source's mixing quartic named as the next quantity.\n"
  "  - GAP6, the flatness, named (lead L244): every frame is flat; chirality needs curvature; no frame with it is on the record.\n"
  "  - The observer line: the web seat's reading of 2026-10-03 taken as confirmation from a fresh reader (L244's sweep: B717,\n"
  "    B128, B849, B1327 and FK12 already state it)."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_8, "the received v1.8 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.9 ·" in cur and cur != t:
            print("GENESIS.md is at v1.9 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.9: PASS (%d changes)" % len(CHANGES)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.9: %d changes" % len(CHANGES)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
