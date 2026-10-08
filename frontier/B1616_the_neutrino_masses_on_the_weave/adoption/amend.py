#!/usr/bin/env python3
"""B1616 -- GENESIS v1.32 (main's, B1611) -> v1.33 (main's): the owner's rulings of 2026-10-08 on four forks (made with the
SM seat and relayed in its section 37; recorded by main) and the neutrino masses on the weave (B1616); the version log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.33 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_32_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_32 = "997a6e044bfcac56bbe908d8061921e443c1a6a977fba49bc499ea338c4840fe"

RULINGS = (" **[v1.33] THE OWNER'S RULINGS OF 2026-10-08 (made with the SM seat, relayed in its section 37, its page "
           "THE_OWNERS_RULINGS_2026-10-08; recorded by main at B1616).** GM5c: **even ticks observed** — the swap is part of the act "
           "but not a symmetry of what is observed; the observed weave is ⟨L, R⟩ with root m004; its three is chiral, CP violation "
           "is allowed, not forced, and which hand is called left is a convention; the P-branch stays computed as the mirror; "
           "revisit if a mechanism makes the vacuum break the mirror by itself. FK11: **Λ a tagged working postulate** — results "
           "computed with W27's link carry \"given Λ\" and FK11 stays formally open; revisit if falsifier P10 fails, a frame is "
           "forced, proton-decay limits bite, or the physical end changes the count. FK10: **flat counts only** — W28's naturality "
           "rules the record's flat counts (±3); the physical end law stays open. GM5d: **positivity kept** — the − threads stay "
           "outside the weave. **The neutrino masses on the weave (B1616, NEGATIVE as sealed):** a Majorana mass for the triplet "
           "lives in Sym² T = 1 + 2 + 3 (no invariant); along RRL, TM1's neutrino-side symmetry, no irreducible of Sym² T has a "
           "fixed vacuum; along RL, L and R the spectra are rigid with exact degeneracies, (1, 1, 1), (½, ½, 1) or (0, 1, 1), each "
           "contradicting the two measured, non-zero splittings — the residual-vacuum reading of the neutrino masses dies on "
           "oscillation data. With B1611, B1612 and B1615: no parameter of the nineteen, and no neutrino mass, is a number of the "
           "weave's group; values need a forced modulus, dynamics or end data.")

CHANGES = [
 ("**Version 1.32 · 2026-10-08 · canonical.**", "**Version 1.33 · 2026-10-08 · canonical.**"),
 ("a phase can come only from couplings, which the weave does not yet force.",
  "a phase can come only from couplings, which the weave does not yet force." + RULINGS),
 ("- **v1.32 · 2026-10-08 · main B1611.** CP on the weave.\n",
  "- **v1.33 · 2026-10-08 · main B1616.** The owner's rulings on four forks; the neutrino masses on the weave.\n"
  "  - GM5c, FK11, FK10, GM5d: the owner's rulings of 2026-10-08 as relayed by the SM seat (even ticks observed; Λ a tagged working postulate, results \"given Λ\"; flat counts only; positivity kept). B1616: no residual-aligned Majorana vacuum survives the oscillation data; the weave's group fixes no neutrino mass.\n"
  "- **v1.32 · 2026-10-08 · main B1611.** CP on the weave.\n"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_32, "the received v1.32 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.33 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.33, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
