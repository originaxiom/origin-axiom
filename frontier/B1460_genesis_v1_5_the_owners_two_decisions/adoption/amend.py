#!/usr/bin/env python3
"""B1460 -- GENESIS v1.4 (main's, B1458) -> GENESIS v1.5: the owner's two decisions of 2026-10-03, and one refinement.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.5 and differs from what this produces

Same form as B1454's and B1456's: every change is an exact string of the received text and its replacement, asserted
to occur exactly once.  Lines that add content are marked [v1.5].
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_4_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_4 = "d32456b67ae2cb55e036de57c2a8619a8e546b7656144c1cf7ab008615bd557a"

FK12_OLD = ("| FK12 **[v1.2]** | The observer: are its closings part of the genesis, or inputs beyond it? (THEOREM_LEDGER C18 makes "
            "them inputs; the owner's question of 2026-10-02: does the act emerge with its observer, the tracker of ab against ba?) | OPEN |")
FK12_NEW = ("| FK12 **[v1.2]** | **[v1.5] The register** (the owner's framing, decided 2026-10-03). The genesis generates a word. The word "
            "keeps the order of its letters (ab against ba); the manifold forgets it — a word and its reverse are one manifold (B1456) — "
            "and the vacuum forgets it again — a direct sum has no order (B1438, B1455). **Is the register that keeps the order part of the "
            "state, carried by the act, or an input from outside?** Four sub-questions, each with a computation: (i) at which step is it "
            "dropped — word→manifold and module→vacuum are the two found; the fibre's involution reverses the order with a sign (B1297, "
            "B1459); (ii) is the choice binary or richer — the record holds two bits (the mirror c; particle against antiparticle) and one "
            "order; (iii) both outcomes at once or at different relations — the slope law gives one term per order, and side by side they "
            "sum to zero (L241); (iv) \"if it can happen it will\" — plenitude, a hypothesis to test, not a premise. What the record does not "
            "show: that the act generates the register rather than receives it. The earlier form of the question: are the observer's "
            "closings part of the genesis, or inputs beyond it? (THEOREM_LEDGER C18 makes them inputs; the SM seat's wording of "
            "2026-10-02: does the act emerge with its observer, the tracker of ab against ba?) | OPEN |")

CHANGES = [
 ("**Version 1.4 · 2026-10-03 · canonical.**",
  "**Version 1.5 · 2026-10-03 · canonical.**"),
 ("**Pending the owner:** the single wording of the principle (§1, fork FK1) is the SM seat's proposal and waits for the owner's\n"
  "confirmation. Everything else here restates the record as it stands,",
  "**[v1.5] Decided by the owner (2026-10-03):** the single wording of the principle (§1, FK1) is confirmed as written, and the\n"
  "observer question (FK12) is framed as the register question. Everything else here restates the record as it stands,"),
 ("**Proposed single wording (v1.0, owner to confirm):**",
  "**The single wording (proposed by the SM seat in v1.0; [v1.5] confirmed by the owner 2026-10-03, main B1460):**"),
 ("| FK1 | The principle's single wording (§1) | proposed | the owner's confirmation or rewording |",
  "| FK1 | The principle's single wording (§1) | **[v1.5] CONFIRMED** (the owner, 2026-10-03) | nothing; the measurer is not in the "
  "principle — it is FK12, where it can be computed and paid |"),
 (FK12_OLD, FK12_NEW),
 ("the right sign. A one-ended state can get the third only from a relation** (FK8). No report derives the source.",
  "the right sign.** [v1.5] The audit lane's qualification (its reply of 2026-10-03, read on main, not re-derived): its results\n"
  "  prove that a specified flat counted configuration needs an admitted source, an end flux, or a change of hypotheses; they do\n"
  "  not prove that a one-ended state can get the third *only* from a relation — whether a generated relation supplies it is FK8\n"
  "  and FK12, and R77's added fields do not settle their origin. No report derives the source."),
 ("  - Unchanged and still the owner's: FK1 and FK12.",
  "  - Unchanged and still the owner's: FK1 and FK12.\n"
  "- **v1.5 · 2026-10-03 · main B1460.** The owner's two decisions, on main's recommendation of the same day.\n"
  "  - **FK1: CONFIRMED** as written (the three faces PF1–PF3). The measurer is kept out of the principle on purpose: as a\n"
  "    premise it could not be paid, as a fork it can.\n"
  "  - **FK12 reframed as the register question** (the wording above, marked [v1.5]): the two steps where the record forgets\n"
  "    the order — word to manifold (B1456), module to vacuum (B1438, B1455) — and the four sub-questions of 2026-10-02, each\n"
  "    with its computation; the open part named.\n"
  "  - GAP3 refined on the audit lane's qualification: \"only from a relation\" was main's sentence, not its result.\n"
  "  - No other status changes."),
]


def build():
    raw = open(SRC, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SHA_V1_4, "the received v1.4 is not the text these changes were written against"
    t = raw.decode("utf-8")
    for old, new in CHANGES:
        assert t.count(old) == 1, ("not found exactly once", old[:90], t.count(old))
        t = t.replace(old, new)
    return t


def main(argv):
    t = build()
    if "--check" in argv:
        cur = open(OUT).read() if os.path.exists(OUT) else ""
        if "**Version 1.5 ·" in cur and cur != t:
            print("GENESIS.md is at v1.5 and differs from amend.py's output"); return 1
        print("VERDICT genesis-amend-v1.5: PASS (%d changes)" % len(CHANGES)); return 0
    open(OUT, "w").write(t)
    print("wrote GENESIS.md v1.5: %d changes" % len(CHANGES)); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
