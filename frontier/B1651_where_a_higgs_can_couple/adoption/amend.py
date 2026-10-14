#!/usr/bin/env python3
"""B1651 -- GENESIS v1.44 (main's, B1648) -> v1.45 (main's): the field's genesis as fork FK15 (the owner's question of
2026-10-14; the three passages of the day agree on "forced to exist, not forced which"; the "which" half banked by B1651:
where a Higgs can couple the fibre's zero modes is not forced), and FK9 (selection) named as the missing ingredient
(POINT_REGISTER P-139); the log.

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.45 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_44_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_44 = "4bcf30ab43200e4a59e4278bf3d822c24f7c09dd73ff0cdb921ab2fa006d7b9d"

FK9 = (" **[v1.45] Named as the missing ingredient (main, 2026-10-14; POINT_REGISTER P-139).** Every \"which\" on the "
       "record comes out free: τ, the Higgs's direction (B1646), its locus among the fibre's fixed points (B1651), the "
       "vacuum. By B990's law an invariant construction picks only its symmetric points, and none tested gives a "
       "hierarchy: τ = ω and the cusp (the SM seat's W65, W67), the real locus (B1646), the democratic class (B1651). So "
       "selection must be a dynamics that lands at a computable point that is not symmetric. The owner assigned its study "
       "to the web seat as insight (2026-10-14); main tests it first at the joint potential (P-132), sealed first.")
FK15 = ("| FK15 **[v1.45]** | The field's genesis (the owner, 2026-10-14: \"how can a field be forced into existence … "
        "same as from philosophy to the seed\") | OPEN | Three passages of the same day agree on \"forced to exist, not "
        "forced which\": the SM seat's P024 (the end carries a source; its W71: it holds given Λ, no R-holonomy and "
        "U(1)_em), the web seat's (the field is what the seed can be), and main's meditation "
        "(`speculations/S_THE_FIELDS_GENESIS.md`, firewalled), whose Step 1 is a candidate fourth face of the principle, "
        "\"what exists is read\" (the owner's decision, P-130). The \"which\" half, banked: where a Higgs can couple the "
        "fibre's zero modes is not forced. No harmonic Higgs couples in the bulk; every point coupling is isotropic; the "
        "moves carry the pairing's triplet exactly; under an even, single-point Higgs the covariant loci are the "
        "puncture, the half-period orbit, or both (B1651). Settled by a derivation of the field's existence from "
        "PF1–PF3, or the owner's adoption of PF4, together with the selection of its \"which\" (FK9) |")
CHANGES = [
 ("**Version 1.44 · 2026-10-14 · canonical.**", "**Version 1.45 · 2026-10-14 · canonical.**"),
 ("7 364 indices, all zero |", "7 364 indices, all zero." + FK9 + " |"),
 ("Revisable by a better argument, not by preference |", "Revisable by a better argument, not by preference |\n" + FK15),
 ("- **v1.44 · 2026-10-14 · main B1648.**",
  "- **v1.45 · 2026-10-14 · main B1651.** The field's genesis as fork FK15 (the day's three passages; the \"which\" half "
  "banked: the Higgs's locus is not forced, B1651); FK9 named as the missing ingredient (P-139).\n"
  "- **v1.44 · 2026-10-14 · main B1648.**"),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_44, "the received v1.44 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.45 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.45, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
