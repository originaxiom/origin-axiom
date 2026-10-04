#!/usr/bin/env python3
"""B1537 -- the SM seat's proposals P1-P9 to GENESIS v1.10 (main's B1467), applied to main's text as received.

Main's relay of 2026-10-03 asked the seat to take v1.10 as head and to number its next page changes as proposals to main's
current version, not as versions. So GENESIS.md at the repository root is main's v1.10 byte for byte, and this script writes
the proposed text to proposed/GENESIS_v1_10_with_proposals.md. Every proposal is an exact string of v1.10 and its
replacement, asserted to occur exactly once; every added line carries the mark **[sm P<n>]** so main can adopt, amend or
decline each by its number.
  P1-P4 carry the SM seat's own v1.10 (sm:B1533) lines that main's v1.10 had not read: the six-gaps heading, GAP6's scope,
        FK9's sm:B1527 and Part H lines, and the frontier's item-8 line. Their texts are the seat's v1.10 text with the
        version mark replaced by the proposal mark (checked in genesis_proposals_checks.py).
  P5-P9 are new: the frame's counts on the levels' abelian covers (sm:B1532), the commensurability class (sm:B1532, sm:B1536
        sealed), the other word states (sm:B1530, sm:B1534, sm:B1535), the cap in the frames table (sm:B1535 Theorem C), and
        the frontier's two places where more than one generation can still live in F-HE.

    python3 merge_proposals.py            # writes proposed/GENESIS_v1_10_with_proposals.md
    python3 merge_proposals.py --check    # exit 1 unless the written file is exactly what this produces
"""
import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
SRC = ARC / "received" / "GENESIS_v1_10_main.md"
SEAT_V110 = ARC / "received" / "GENESIS_v1_10_sm.md"
OUT = ARC / "proposed" / "GENESIS_v1_10_with_proposals.md"
SHA_MAIN_V110 = "b3ac6129e6e63ed409c38a7f6fa603767da2194916ffb89463bb15ed3a45b6a8"


def seat_segment(start, end):
    """a segment of the seat's own v1.10 (sm:B1533), from start up to (not including) end"""
    s = SEAT_V110.read_text(encoding="utf-8")
    i = s.index(start)
    j = s.index(end, i)
    return s[i:j]


def carried():
    """P1-P4's texts: the seat's v1.10 lines, with [v1.10]/[v1.8] marks replaced by the proposal's own mark"""
    gap6 = seat_segment("  **[v1.10]** Its scope, from the record (sm:B1531", "\n\n**[v1.2]** **The gaps and the observer.**")
    fk9 = seat_segment("**[v1.8]** Answered near the hyperbolic point (sm:B1527", " The owner's hypothesis of 2026-10-02")
    front = seat_segment(" **[v1.8]** answered near the hyperbolic point in finite volume (sm:B1527)",
                         "\n- **[v1.6]** the fixed loci of the metallic trace maps")
    gap6 = gap6.replace("**[v1.10]**", "**[sm P2]**", 1)
    fk9 = fk9.replace("**[v1.8]**", "**[sm P3]**", 1).replace("**[v1.10]**", "**[sm P3]**", 1)
    front = front.replace("**[v1.8]**", "**[sm P4]**", 1)
    assert "[v1.10]" not in gap6 + fk9 + front and "[v1.8]" not in gap6 + fk9 + front
    return gap6, fk9, front


def changes():
    gap6, fk9, front = carried()
    return [
        # P1: the heading counts six gaps (v1.9 added GAP6 under "Five gaps")
        ("**Five gaps**, none of which work on one state can close:",
         "**Six gaps** **[sm P1]**, none of which work on one state can close:"),
        # P2: GAP6's scope, the seat's v1.10 paragraph
        ("  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.\n",
         "  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.\n"
         + gap6 + "\n"),
        # P3: FK9, the seat's sm:B1527 and Part H lines
        ("it is nonzero is the SM seat's sL-10 item 8, sealed first. The owner's hypothesis of 2026-10-02",
         "it is nonzero is the SM seat's sL-10 item 8, sealed first. " + fk9 + " The owner's hypothesis of 2026-10-02"),
        # P4: section 8's frontier, the item-8 line
        ("- **[v1.6]** the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
         "  seat's sL-10 item 8);\n",
         "- **[v1.6]** the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
         "  seat's sL-10 item 8);" + front + "\n"),
        # P5: F-HE on m004's levels: the finite abelian covers (sm:B1532)
        ("and every one of the 196 firing members of levels 1–6 is fixed (sm:B1522) |",
         "and every one of the 196 firing members of levels 1–6 is fixed (sm:B1522). **[sm P5]** On every finite abelian cover "
         "of M₂–M₆ no λ = 1 pulled-back member carries a generation-shaped count, at any class, in either order (sm:B1532, "
         "NEGATIVE, run as sealed; two routes, 68,596 counts each); the members at κ⁵ = 1 add none |"),
        # P6: F-HE on the commensurability class
        ("| fires on five arithmetic members: s958, v2873, t12833, t12835, o10_150701 (main B1418; sm:B1374) | never computed |",
         "| fires on five arithmetic members: s958, v2873, t12833, t12835, o10_150701 (main B1418; sm:B1374) | **[sm P6]** the "
         "finite abelian covers of the levels, which are in the class (sm:B1532: no generation-shaped count); every connected "
         "cover of degree ≤ 12 of m004 and m003 and their Q₈ towers are sealed as sm:B1536 |"),
        # P7: F-HE on the other word states
        ("on 262 of the 536 manifolds no isometry dualises it (sm:B1523); counts never computed |",
         "on 262 of the 536 manifolds no isometry dualises it (sm:B1523). **[sm P7]** Counts at the hyperbolic point: one "
         "generation in one W on the silver squares m135 and m136, through interior classes of the four, and none on the golden "
         "word states (sm:B1530); at most one on every finite abelian cover of m135 and m136 at the pulled-back "
         "members (sm:B1534); at most one at every finite-order member and every class of every word state and level "
         "(sm:B1535, Theorem C with Lemma W) |"),
        # P8: the frames table, F-HE: the cap
        ("| F-HE | Harmonic E₈ frame | E₈ ⊃ SU(5) × SU(5)′ on the harmonic convex-projective vacuum; rank-five extensions W with "
         "N(10′) = −I(W) and N(5̄′) = −I(Λ²W) |",
         "| F-HE | Harmonic E₈ frame | E₈ ⊃ SU(5) × SU(5)′ on the harmonic convex-projective vacuum; rank-five extensions W with "
         "N(10′) = −I(W) and N(5̄′) = −I(Λ²W). **[sm P8]** At a finite-order member on any finite cover, at every class and in "
         "either order: N(5̄′) ≤ n(ν³ ⊗ ρ) and N(10′) ≤ b0 + n(ν⁴), so g generations need both supplies ≥ g (sm:B1535, "
         "Theorem C) |"),
        # P9: section 8's frontier: where more than one generation can still live in F-HE
        ("- **[v1.6]** the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
         "  allowed; the audit lane's AR4).\n",
         "- **[v1.6]** the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
         "  allowed; the audit lane's AR4);\n"
         "- **[sm P9]** F-HE where both of Theorem C's supplies can grow (sm:B1535, Corollary C3): the covers' own characters on\n"
         "  the fibre-direction covers of word states (puncture characters, where the line's interior supply can be non-zero),\n"
         "  non-abelian covers beyond sm:B1536's population, and non-unitary characters on covers with several cusps.\n"),
    ]


def build():
    src = SRC.read_bytes()
    assert hashlib.sha256(src).hexdigest() == SHA_MAIN_V110, "main's v1.10 as received has changed"
    text = src.decode("utf-8")
    for old, new in changes():
        assert text.count(old) == 1, ("anchor count", text.count(old), old[:80])
        text = text.replace(old, new, 1)
    return text


def main():
    text = build()
    if "--check" in sys.argv:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == text
        print("proposed text reproduces:", ok)
        sys.exit(0 if ok else 1)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print("wrote", OUT.relative_to(ARC), len(text), "characters;", sum(1 for _ in changes()), "proposals applied")


if __name__ == "__main__":
    main()
