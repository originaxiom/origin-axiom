#!/usr/bin/env python3
"""B1715 -- GENESIS v1.52 (main's) -> v1.53 (main's), after S185's full suite: FK10's four-dimensional sentence (P-254;
B1708, B1710) and Gate 12 closed (P-074; B1678); FK9's measure (P-093); FK12's CP sign (P-149); GM5c read against v1.49
(P-215); the log.  The version log's own lines are not rewritten.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.53 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_52_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_52 = "c75512f67d76f9e375660bc9ccaad2dc1166238a812e7a3de0b5e5186c699ee8"
CHANGES = [
 ("**Version 1.52 · 2026-10-22 · canonical.**", "**Version 1.53 · 2026-10-22 · canonical.**"),
 # FK10: Gate 12 closed since (B1678)
 ("(POINT_REGISTER P-074), still owed.",
  "(POINT_REGISTER P-074), still owed. **[v1.53] Closed since (B1678): kept with its coefficient action, the act lifts "
  "through the central double cover of Aut⁺(F₂) to one coherent action of the four wordings on matter and boundary "
  "(P-074); the joint image is reducible, so the extreme domain stays chosen.**"),
 # FK10: four-dimensional gravity does not supply the unit (P-254)
 ("so those results hold given Λ, the unit and H-cov in R's own module.",
  "so those results hold given Λ, the unit and H-cov in R's own module. **[v1.53] Four-dimensional gravity does not "
  "supply the unit (B1708, B1710; the SM seat's W120, W121; P-254).** The closed torus-fibred 4d vacua over the weave's "
  "τ-line close at 12 or 24 strings, and the moves' ℤ/12 makes their units of end data a multiple of twelve. The triplet "
  "lives only where χ(O_S) "
  "is even (K3 the least), and its count there is −15χ(O_S) or −18χ(O_S) (−30 and −36 on K3), never three. FK10's single "
  "unit at the weave's cusp stays a tagged postulate."),
 # FK9: a selection may select a measure (P-093)
 ("B990's law concerns the orbit of one point. |",
  "B990's law concerns the orbit of one point. **[v1.53] A selection may select a measure (the SM seat's relay §64, "
  "with the owner's framing of a field of maximality against the seed of minimality; P-093).** A rule may pick a "
  "distribution over states rather than a point, and its test is then statistical. The sealed calibrations since B1695 "
  "are tests of that kind: the fraction of random hierarchies a model fits as well as the data. The seat's own test of "
  "the seed's invariant measure (W57) found no draw within 32σ of the ten numbers, and its uniqueness premise is scoped "
  "by the audit lane (P-107). |"),
 # FK12: where a CP sign is chosen (P-149)
 ("never a consequence of the register question and never a claim |",
  "never a consequence of the register question and never a claim. **[v1.53] Where a CP sign is chosen (the web "
  "seat's selection report §6.2; B1652's addendum; P-149).** In the thread frame the couplings keep the word's order, "
  "which the manifold forgets. A word and its reverse carry conjugate couplings at equal weight, so the word's order is "
  "where a CP sign is chosen: a convention between CP-conjugate vacua, CP broken vacuum by vacuum. |"),
 # GM5c: read against v1.49 (P-215)
 ("forced, elementary (A + B = n), its physical meaning open. |",
  "forced, elementary (A + B = n), its physical meaning open. **[v1.53] Read against v1.49 (P-215; the web seat's map "
  "§0 5(a)).** v1.49 states the law's form as the family of wordings, whose smallest instance a → ab, b → a is L∘P and "
  "contains the swap. v1.33's ruling concerns which ticks are observed, the even ones. The two do not conflict: the law "
  "contains the swap, so CP is a symmetry of the law (v1.32), and on the observed even ticks the swap is not a move, so "
  "CP violation there is allowed, not forced (B1611). Whether stating the principle as the family reopens v1.33's choice "
  "is the owner's. |"),
 # the log
 ("- **v1.52 · 2026-10-22 · main B1706.**",
  "- **v1.53 · 2026-10-22 · main B1715.** After S185's full suite.\n"
  "  - FK10: four-dimensional gravity does not supply the unit. The closed torus-fibred 4d vacua give units only in "
  "twelves, and the triplet's count on them is never three (B1708, B1710; P-254). Gate 12 closed since (B1678; P-074).\n"
  "  - FK9: a selection may select a measure, tested statistically (P-093).\n"
  "  - FK12: the word's order is where a CP sign is chosen, a convention between CP-conjugate vacua (P-149).\n"
  "  - GM5c read against v1.49: no conflict with v1.33. Whether the family reopens v1.33's choice is the owner's (P-215).\n"
  "  - The price is unchanged: nothing here is an identification or an axiom (P-270).\n"
  "- **v1.52 · 2026-10-22 · main B1706.**"),
]
def build():
    src = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(src.encode("utf-8")).hexdigest() == SHA_V1_52, "the received v1.52 is not the pinned one"
    out = src
    for old, new in CHANGES:
        assert out.count(old) == 1, ("anchor not unique", old[:60], out.count(old))
        out = out.replace(old, new)
    return out
if __name__ == "__main__":
    text = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("Version 1.53" in cur[:400] and cur != text) else 0)
    open(OUT, "w", encoding="utf-8").write(text); print("GENESIS.md written at v1.53")
