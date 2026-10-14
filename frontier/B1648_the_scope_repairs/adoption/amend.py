#!/usr/bin/env python3
"""B1648 -- GENESIS v1.43 (main's, B1641) -> v1.44 (main's): Review 63's scope repairs (R63-3, POINT_REGISTER P-119 and
P-122): FK10's B1629 sentences in their quantified scope (B1629's addendum), with the owner's tagging of the unit
standing as the owner's ruling; v1.43's lift agreement at the one point it was checked, the coherence check over
Aut+(F2) owed (the Banking Seat's Gate 12, P-074), and M_{1,2} as the weave's object the seat's reading (W19); the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.44 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_43_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_43 = "a69bccaca5647e452853749e481f57951dfb9f5e8f0322d941667ecb5ca5f28f"

FK10 = (" **[v1.44] Scoped (Review 63, B1648; B1629's addendum of 2026-10-09).** Two sentences above are B1629's as first "
        "banked, and its addendum sharpens both. The fraction of letters in runs of length ≥ k tends to (k + 1)/2^k and is "
        "within 2.4% of it at every n = 10 … 18; it is the limit, not the value at every length. \"Not dynamical\" holds in "
        "this scope: no datum the principle forces (the tick, the clock) and no expectation under the weave's uniform "
        "measure on threads of an observable in ever-deeper horoballs gives the cusp a non-zero weight; other measures and "
        "other dynamics are not excluded. The owner's tagging of the unit (v1.39) is the owner's ruling and stands in "
        "either reading.")
LIFT = (" **[v1.44] Scoped (Review 63, B1648).** The agreement with the ruled moves was checked at Δ⁴ alone; coherence of "
        "the lifts over all of Aut⁺(F₂) is the Banking Seat's Gate 12 (POINT_REGISTER P-074), still owed. \"The two objects "
        "are one\" takes the weave's surface to be M₁,₂, the SM seat's reading (W19, verified on main in part, B1624). The "
        "results built on this (B1642, B1644–B1646) carry both conditions.")
CHANGES = [
 ("**Version 1.43 · 2026-10-13 · canonical.**", "**Version 1.44 · 2026-10-14 · canonical.**"),
 ("Revisit when the audit lane derives an end mechanism at the cusp, or a forcing is found.",
  "Revisit when the audit lane derives an end mechanism at the cusp, or a forcing is found." + FK10),
 ("is not the puncture condition's orientation at the representation level.",
  "is not the puncture condition's orientation at the representation level." + LIFT),
 ("- **v1.43 · 2026-10-13 · main B1641.**",
  "- **v1.44 · 2026-10-14 · main B1648.** Review 63's scope repairs: FK10's B1629 sentences in their quantified scope "
  "(the owner's tagging stands); v1.43's lift agreement at Δ⁴ alone (Gate 12 owed) and M₁,₂ as the seat's reading.\n"
  "- **v1.43 · 2026-10-13 · main B1641.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_43, "the received v1.43 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.44 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.44, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
