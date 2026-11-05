#!/usr/bin/env python3
"""B1843 -- GENESIS v1.61 (main's) -> v1.62 (main's): THE JOINT CONFIRMATION. The owner's ruling of 2026-11-05 on the SM
seat's sections 351-352 ("if you also agree with sm about the rule, i aprove it"; main agreed, with three conditions:
through this amendment, the statistic verified by main, the claim's wording fixed). GAP1's v1.60 conditions 3 and 4 grade
the held-out targets jointly; a seventh condition holds them unspent when the card cannot succeed. Adopted before B1839's
look was read.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.62 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_61_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_61 = "6f5e9a19d4dbee9137579852344c48a4962048748403ff7de890d23ccb40a572"
OLD3 = ("  3. *Passed.* Each is graded PASSED by V: the measured value inside the prediction's stated 68% band, and\n"
        "     p_V < 0.01/m_V against the matched null (F's pipeline re-run over its whole CHOSEN menu, B1798).\n"
        "  4. *Two at least.* At least two held-out quantities, not functions of one another, pass on the same card.\n")
NEW3 = ("  3. *Passed.* **[v1.62] Graded jointly (the owner's ruling, 2026-11-05; B1843).** Each held-out quantity's measured\n"
        "     value lies inside its prediction's stated 68% band; and the joint p_V is below 0.01/m_V in its exact 97.5% upper\n"
        "     end. The joint p_V is the rank, among the matched null's worlds (F's pipeline re-run over its whole CHOSEN menu,\n"
        "     B1798), of the product of the targets' marginal rank p-values, with leave-one-out ranks for the null worlds, ties\n"
        "     counted against the frame and the data counted in the null. m_V counts the attempt's held-out targets and every\n"
        "     prior look at each of them recorded in docs/LOOK_LEDGER.md, sealed or unsealed, across seats. (Under v1.60 each\n"
        "     target needed p_V < 0.01/m_V on its own, which a correct frame at the screen's allowance almost never meets.)\n"
        "  4. *Two at least.* At least two held-out quantities, not functions of one another (no identity of F ties them),\n"
        "     pass jointly on the same card. The claim reads \"jointly confirmed, each within its band\", never \"each\n"
        "     confirmed\".\n")
OLD6 = ("     record kept, if a later sealed held-out prediction of F through the same identification is graded NEGATIVE.\n")
NEW6 = (OLD6 +
        "  7. *Worth spending.* **[v1.62]** Before any measured value of the targets is opened, main computes the card's\n"
        "     power from the matched null's predictions alone (their spread, never their location or any measured value):\n"
        "     the chance that a frame whose true error is 5% passes. If it is below 10%, the targets are held, unspent, and the\n"
        "     card is not run; a held-out target is spent once.\n")
CHANGES = [
 ("**Version 1.61 · 2026-11-03 · canonical.**", "**Version 1.62 · 2026-11-05 · canonical.**"),
 (OLD3, NEW3),
 (OLD6, NEW6),
 ("quantities under GAP1's v1.60 rule (each at p_V < 0.01/m_V, two at least);",
  "quantities under GAP1's rule (v1.60, graded jointly since v1.62: each within its band and the joint p_V < 0.01/m_V, two at least);"),
 ("- **v1.61 · 2026-11-03 · main B1829.**",
  "- **v1.62 · 2026-11-05 · main B1843.** The owner's ruling on the SM seat's §§ 351–352 (\"if you also agree with sm about "
  "the rule, i aprove it\"; main agreed, with three conditions): GAP1's condition 3 grades the held-out targets jointly — "
  "each inside its 68% band, and the joint p_V (the product of the targets' marginal rank p-values under the matched "
  "null, ranked among the null worlds) below 0.01/m_V in its 97.5% upper end; m_V counts every recorded prior look, sealed "
  "or not, across seats; condition 4 reads 'pass jointly', the claim 'jointly confirmed, each within its band'; a new "
  "condition 7 holds the targets unspent when the card's location-free power for a 5%-accurate frame is below 10%. "
  "Adopted before B1839's look was read. The statistic's calibration was checked by main (1.02%, 0.97%, 0.83% at "
  "α = 0.01: independent targets, ρ = 0.9, three targets). The v1.61 entry below is not rewritten.\n"
  "- **v1.61 · 2026-11-03 · main B1829.**"),
]


def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_61, "the received v1.61 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:70], out.count(old))
        out = out.replace(old, new)
    return out


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.62 · 2026-11-05 · canonical.**" in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out)
    print("GENESIS.md written at v1.62")
