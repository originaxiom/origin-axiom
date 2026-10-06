#!/usr/bin/env python3
"""B1482 -- GENESIS v1.13 (main's, B1480) -> v1.14 (main's): the sign of a word state needs one move, -I, and no inverse
letter; positivity is what excludes it; FK4 sharpened.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.14 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_13_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_13 = "9855b9f762d644e9471093d77e8ae8cf650d2cac3671715d98e018bd6a2baa4a"

CHANGES = [
 ("**Version 1.13 · 2026-10-07 · canonical.**", "**Version 1.14 · 2026-10-07 · canonical.**"),
 ("Needed for the signed states: −I = (L²R⁻¹)² (sm:B1384 S0). Invertibility of a matrix is not legality of its inverse as an update (R57). |",
  "Needed for the signed states: −I = (L²R⁻¹)² (sm:B1384 S0). Invertibility of a matrix is not legality of its inverse as an update (R57). **[v1.14] Not needed for them (B1482):** the signed states need exactly one move beyond L and R — the central −I, which negates both records — and −I does not bring inverse letters with it (L⁻¹ is not ± a positive word). GM5b and the sign are independent forks. |"),
 ("A sector restriction, not a consequence of using L and R (R57; the audit lane's operational contract). Not needed to select the root (§4). |",
  "A sector restriction, not a consequence of using L and R (R57; the audit lane's operational contract). Not needed to select the root (§4). **[v1.14] It is what excludes the sign (B1482):** −I sends a pair of counts to its negative. Under positivity the grammar generates the + states and, with P, the non-orientable ones; the − states — on which every spin structure carries a hand (B1479, B1481) — are exactly what positivity removes. |"),
 (" If it does, the place where a hand can be registered on a fermion emerges; if not, it is an added choice |",
  " If it does, the place where a hand can be registered on a fermion emerges; if not, it is an added choice. **[v1.14] Sharpened (B1482):** the sign needs no inverse letter — only the central move −I, the negation of both records; words in L, R and P never give it (their entries stay non-negative), and no − state is the square of any act (tr X² ≥ −2 in GL(2,ℤ), tr(−w) ≤ −3), so act-plus-register cannot produce one. The fork is: **is negating the records a legal move?** Positivity (FK6, CHOSEN) forbids it; PF1's own verb — cancelling — names it (a reading, not a derivation) |"),
 ("    bit are independent there, and the next cell is the index under the mirror's swap of spin structures.",
  "    bit are independent there, and the next cell is the index under the mirror's swap of spin structures.\n"
  "- **v1.14 · 2026-10-07 · main B1482.** The sign located in the grammar.\n"
  "  - GM5b: inverse letters are not needed for the signed states; one central move, −I, is, and it brings no inverse letter.\n"
  "  - GM5d: positivity is what excludes −I, hence the − states, hence every handed spin structure (B1479, B1481).\n"
  "  - FK4 sharpened to one question — is negating the records a legal move? — with PF1's verb as a reading, not a derivation.\n"
  "  - B1481 recorded: on the − states every spin structure carries a phase its mirror partner negates."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_13, "the received v1.13 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.14 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.14, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
