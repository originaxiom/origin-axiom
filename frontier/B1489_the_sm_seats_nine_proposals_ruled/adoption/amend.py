#!/usr/bin/env python3
"""B1489 -- GENESIS v1.15 (main's, B1487) -> v1.16 (main's): the SM seat's nine proposals P1-P9 (sm:B1537, 2026-10-04)
ruled against the current page, one by one, each with its grade on main (verified / read at headline level / under FK14).

    python3 amend.py            # writes GENESIS.md at the repository root
    python3 amend.py --check    # exit 1 if the root file is at version 1.16 and differs from what this produces
"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(HERE, "..", "received", "GENESIS_v1_15_main.md"); OUT = os.path.join(ROOT, "GENESIS.md")
SHA_V1_15 = "fc541f2fec0e885d3fe509e1dc258d32f626ed671b73f8f9567d3a1175f04f21"

CHANGES = [
 ("**Version 1.15 · 2026-10-07 · canonical.**", "**Version 1.16 · 2026-10-07 · canonical.**"),
 # P8 -- the frames table, the F-HE row (the cap), with B1487's reading
 ("rank-five extensions W with N(10′) = −I(W) and N(5̄′) = −I(Λ²W) | the SM seat's branch, sm:B1509–sm:B1515; the audit lane, R40–R76 |",
  "rank-five extensions W with N(10′) = −I(W) and N(5̄′) = −I(Λ²W). **[v1.16, the SM seat's P8, read on main at headline level]** At a finite-order member on any finite cover, at every class and in either order: N(5̄′) ≤ n(ν³ ⊗ ρ) and N(10′) ≤ b0 + n(ν⁴), so g generations need both supplies ≥ g (sm:B1535, Theorem C). **[v1.16]** And by the seat's floor read as a mechanism (B1487): a count in this frame is a count of ends, and its four is blind to the spin structure (GAP1) | the SM seat's branch, sm:B1509–sm:B1515; the audit lane, R40–R76 |"),
 # P5 -- the levels row
 ("every one of the 196 firing members of levels 1–6 is fixed (sm:B1522) | m004's cusp (shape 2√−3)",
  "every one of the 196 firing members of levels 1–6 is fixed (sm:B1522). **[v1.16, the SM seat's P5, read on main at headline level]** On every finite abelian cover of M₂–M₆ no λ = 1 pulled-back member carries a generation-shaped count, at any class, in either order (sm:B1532, NEGATIVE, run as sealed; two routes, 68,596 counts each); the members at κ⁵ = 1 add none | m004's cusp (shape 2√−3)"),
 # P6 -- the class row: a fact about the named list, under FK13 and FK14
 ("(main B1418; sm:B1374) | never computed | hexagonal cusps (m003's",
  "(main B1418; sm:B1374) | **[v1.16, the SM seat's P6, read on main at headline level; a statement about this named list, which FK13 rules is not the object]** the finite abelian covers of the levels (sm:B1532: no generation-shaped count); every connected cover of degree ≤ 12 of m004 and m003 and their Q₈ towers (sm:B1536, NEGATIVE: no three; room reaches two on sixteen degree-10 covers of m003); on N₄₅ no three at the trivial character at any class (sm:B1541, reproduced on main; sm:B1544, sm:B1546). Under FK14 every one of these is a search for ends | hexagonal cusps (m003's"),
 # P7 -- the other word states: the one generation, with main's grade
 ("(sm:B1523); counts never computed | never computed |",
  "(sm:B1523). **[v1.16, the SM seat's P7]** Counts at the hyperbolic point: one generation in one W on the silver squares m135 and m136, through interior classes of the four, and none on the golden word states (sm:B1530 — **read by main's instrument and independent code, B1485: every count agrees; and at every member the two orders fuse into an irreducible module that counts zero, B1486**); at most one on every finite abelian cover of m135 and m136 at the pulled-back members (sm:B1534, read at headline level); at most one at every finite-order member and every class of every word state and level (sm:B1535, Theorem C with Lemma W, read at headline level) — and at most 1 + b0 on any one-cusped state by the floor (B1487): the one generation is a cusp on which the class dies | never computed |"),
 # P2 -- GAP6's scope, in main's words, with the mirror-even theorem
 ("manifold at Chern–Simons class ¼ is of that kind (75 of 75). The bit is a parity of the boundary torus' lattice.",
  "manifold at Chern–Simons class ¼ is of that kind (75 of 75). The bit is a parity of the boundary torus' lattice. **[v1.16, the SM seat's P2 (sm:B1533 C3–C6), in main's words]** The sentence \"no characteristic-class index on a closed bulk can tell 27 from 27̄\" holds for Dirac indices and for every count on a closed or sealed problem; it does not bind the class index on an open end, which tells a module from its dual on flat modules of one Chern character — the seat's M₄ at ν = (1/3, 0) reads +1, −1, 0 on the non-split module, its dual and the split sum; main's B1466 and B1486 read the same pattern at m004's counted point and at the silver members. A flat frame's count can tell a module from its dual; **what it cannot do is see the hand: the class index is mirror-even for every module (B1487, T1)**, so whether such a count is a physical chirality is GAP1 and the order is a choice."),
 # P3 -- FK9: sm:B1527 and Part H
 ("selected by their words, not their field |",
  "selected by their words, not their field. **[v1.16, the SM seat's P3]** Answered near the hyperbolic point (sm:B1527, PROVED, run as sealed): no vacuum ν ⊗ ρ or ν ⊗ Λ²ρ of a finite-volume projective deformation near the hyperbolic point has a non-zero index, on every word state to length 12, mirror-broken or not — the character is trivial on the fibre boundary, a commutator, and on the finite-volume curves that boundary has no eigenvalue 1, so the cusp is acyclic. **Part H, the hyperbolic point itself, verified on main by a route sharing nothing with the seat's (B1465):** on ±LLRLRR and ±L³RLR², at the parabolic points of their periodic curves, for every fibre character and seven twists of the meridian, 7 364 indices, all zero |"),
 # P4 -- the frontier's item on the projective family
 ("  seat's sL-10 item 8);",
  "  seat's sL-10 item 8); **[v1.16, the SM seat's P4, read on main at headline level]** answered near the hyperbolic point in finite volume (sm:B1527; and sm:B1529: Λ² carries no count for any deformation in SL(4, ℂ) near the hyperbolic point, the four none where its base condition holds — the base condition fails on one word state, m135, at two characters); open there: the eigenvalue-one locus of the infinite-volume part, the non-split extensions, and the deformations far from the hyperbolic point;"),
 # P9 -- the frontier: where the supplies can grow, under FK14
 ("  One candidate is named and unbuilt — the six-dimensional frame bundle Γ\\PSL(2,ℂ) of a closed filling (the web seat's A1);",
  "  One candidate is named and unbuilt — the six-dimensional frame bundle Γ\\PSL(2,ℂ) of a closed filling (the web seat's A1);\n"
  "- **[v1.16, the SM seat's P9, recorded under FK14]** F-HE where both of Theorem C's supplies can grow (sm:B1535, Corollary C3): the\n"
  "  covers' own characters on the fibre-direction covers of word states (puncture characters), non-abelian covers beyond\n"
  "  sm:B1536's population, and non-unitary characters on covers with several cusps. **Each is a search for ends** (B1487, GAP2):\n"
  "  a count of three found there is a selection, graded by `docs/THE_BAR.md`, until FK14 is ruled and the selection rule and\n"
  "  trial budget are named before the search (WORKING_RULES, 2026-10-07);"),
 ("  - B1485, B1486 recorded: the one generation of the harmonic frame on the silver squares read by main's instrument (every count agrees); at every member the two orders fuse into an irreducible module that counts zero.",
  "  - B1485, B1486 recorded: the one generation of the harmonic frame on the silver squares read by main's instrument (every count agrees); at every member the two orders fuse into an irreducible module that counts zero.\n"
  "- **v1.16 · 2026-10-07 · main B1489.** The SM seat's nine proposals (sm:B1537, 2026-10-04) ruled against the current page.\n"
  "  - P1 (six gaps): paid at v1.15, credited there. P3 (sm:B1527 at FK9; Part H verified on main, B1465): adopted. P7 (one generation on the silver squares): adopted with main's grade — verified by a second route (B1485), the orders fused (B1486), and the floor's reading (B1487).\n"
  "  - P2 (GAP6's scope): adopted in main's words, with the mirror-even theorem (B1487) as its limit. P8 (the cap): adopted at the seat's grade, read on main at headline level, with the ends reading.\n"
  "  - P4, P5, P6: adopted as the seat's results at the seat's grade, read on main at headline level — P6 as a statement about the named list that FK13 rules is not the object, and under FK14.\n"
  "  - P9 (where the supplies can grow): recorded, not adopted as a programme — under FK14 each item is a search for ends, and a count found there is a selection until the rule is named first."),
]


def build():
    s = open(SRC, encoding="utf-8").read()
    assert hashlib.sha256(s.encode("utf-8")).hexdigest() == SHA_V1_15, "the received v1.15 is not the file this amendment was written against"
    for old, new in CHANGES:
        assert s.count(old) == 1, ("anchor not unique or missing", old[:70], s.count(old))
        s = s.replace(old, new)
    return s


if __name__ == "__main__":
    out = build()
    if "--check" in sys.argv:
        cur = open(OUT, encoding="utf-8").read()
        sys.exit(1 if ("**Version 1.16 " in cur and cur != out) else 0)
    open(OUT, "w", encoding="utf-8").write(out); print("GENESIS.md written at v1.16, sha256", hashlib.sha256(out.encode("utf-8")).hexdigest()[:16])
