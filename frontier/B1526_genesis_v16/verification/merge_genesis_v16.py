"""GENESIS v1.6 (sm:B1526): main's head, v1.5 (B1460, the owner's two decisions), taken as the head, as main asked of both
seats ("Please take v1.5 as head", its relay of 2026-10-03). The SM seat's own v1.5 (sm:B1525), made on main's v1.4 in
parallel and numbered the same, is answered by its line: what main's v1.5 had not made is carried, marked [v1.6]; GAP3's
refinement is main's already; FK12's carried text is fitted to the owner's framing (the register question), the
experiential question kept apart under Gate 5-Q; FK9 names P as the fibre's elliptic involution (C3). Each carried item is
checked with the SM seat's own code first (genesis_v16_checks.py). Exact replacements only; each must match once.
Usage: python3 merge_genesis_v16.py ../received/GENESIS_v1_5_main.md OUT.md"""
import hashlib
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
SHA_V1_5 = hashlib.sha256(s.encode("utf-8")).hexdigest()
assert SHA_V1_5 == "67d554e9868b0164685ce8b71b6d3d1dea19b892b937b709a8a45a232879fa12", SHA_V1_5
V = "**[v1.6]**"


def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new)


# ------------------------------------------------------------------ header
rep("**Version 1.5 · 2026-10-03 · canonical.**", "**Version 1.6 · 2026-10-03 · canonical.**")
rep("main and records what the own-level law is not, each marked **[v1.4]**. The version log (§10) lists every\n",
    "main and records what the own-level law is not, each marked **[v1.4]**. v1.5 (main's B1460) records the owner's two\n"
    "decisions: FK1 confirmed as written, and FK12 framed as the register question. v1.6 (sm:B1526) takes main's head, v1.5,\n"
    "as main asked. The SM seat's own v1.5 (sm:B1525) was made on main's v1.4 in parallel with main's and numbered the same;\n"
    "v1.6 answers it by its line and carries what main's v1.5 had not made, each marked **[v1.6]**. On the SM seat's branch\n"
    "main's v1.5 and the seat's v1.5 are kept as received in sm:B1526's `received/` (`GENESIS_v1_5_main.md`,\n"
    "`GENESIS_v1_5_sm.md`), and main's v1.4 and the seat's v1.3 in sm:B1525's. The version log (§10) lists every\n")

# ------------------------------------------------------------------ §5, the frame table (sm:B1525, carried)
rep("by proof (main B1455; independently sm:B1520) |",
    "by proof (main B1455; independently sm:B1520). " + V + " On the levels M₁…M₁₂ the count-odd mirror of those vacua "
    "breaks from M₅ on, off the unit circle exactly where no golden Galois reflection fixes the twist, and every one of "
    "the 196 firing members of levels 1–6 is fixed (sm:B1522) |")
rep("among them m369 (8) and s639 (16) (main B1434) | never computed | never computed |",
    "among them m369 (8) and s639 (16) (main B1434) | " + V + " each is rigid rel cusp, so carries a one-parameter projective "
    "family at its hyperbolic point, and on 262 of the 536 manifolds no isometry dualises it (sm:B1523); counts never "
    "computed | never computed |")

# ------------------------------------------------------------------ §7: GAP4 and the observer line (GAP3 is main's in v1.5)
rep("graded DERIVED, REPRODUCED,",
    "graded DERIVED (" + V + " PASSED since sm:B1524: a rarity screen, not a derivation), REPRODUCED,")
rep("built does not repair those maps. The end condition chosen rather than derived (GAP2, FK10) is the space closing.",
    "built does not repair those maps. " + V + " What survives is the structure: a measurement as a choice of fibre functor\n"
    "with a Galois ambiguity, without either group assignment (the audit lane's AR6; sm:B1521 C4). The end condition chosen\n"
    "rather than derived (GAP2, FK10) is the space closing.")

# ------------------------------------------------------------------ §8: FK9, FK12 and the frontier
rep("graded by `docs/THE_BAR.md` (**[v1.4]** on main from B1458) (**[v1.2]** sm:B1518; GAP4).",
    "graded by `docs/THE_BAR.md` (**[v1.4]** on main from B1458) (**[v1.2]** sm:B1518; GAP4). " + V + " Its null contract "
    "(sm:B1524) names the laws under which the bar's p is a probability, corrects several looks by Bonferroni, and renames "
    "the top grade PASSED: a rarity screen, necessary for WHAT_WOULD_COUNT's DERIVED and never sufficient for it, and never "
    "a physical admission.")
rep("Silent on a sourced vacuum, on other states and on selection by a relation |",
    "Silent on a sourced vacuum, on other states and on selection by a relation. " + V + " Carried from the SM seat's v1.3 "
    "(sm:B1521 C1, with sm:B1512 Lemma I): B1297's period-2 symmetry P is the fibre's elliptic involution, whose extension "
    "to every level is main's B1459, and in Ballas' presentation it is the swap's class; it fixes ρ_q (sm:B1526 C3: on m004 "
    "it is the one non-trivial outer class that keeps the orientation and the base, and it inverts the fibre's homology). "
    "So "
    "B1297's tower theorem (P inverts every twist) and the family's (the inversion dualises ρ_q) rest on different "
    "symmetries. Run since on the levels (main's L242 (b); sm:B1522, PROVED, frame F-HE): the count-odd mirror breaks from "
    "M₅ off the unit circle and from M₆ on it, up to 0.91 of M₁₂'s 103 680 vacua; off the circle it breaks exactly where no "
    "golden Galois reflection fixes the twist; and every one of the 196 firing members of levels 1–6 is fixed, so the "
    "mirror breaks only where nothing chiral has been found. On the word states (sm:B1523, PROVED): every word state to "
    "length 12 carries a one-parameter projective family at its hyperbolic point; main's one-bit rule (an isometry "
    "dualises the family exactly when it inverts the fibre boundary) holds on all of them; and on 262 manifolds (482 "
    "states) no isometry dualises the family, so near the hyperbolic point B1455's symmetry argument cannot force the "
    "count to zero there (Lemma T, a local statement). Whether it is nonzero is the SM seat's sL-10 item 8, sealed first. "
    "The owner's hypothesis of 2026-10-02, \"choice might be golden\", was tested in these two sealed forms: on the "
    "levels, off the unit circle, a golden Galois reflection decides where the mirror breaks; on the word states, of the "
    "14 manifolds with golden monodromy field exactly ±L⁴RL³R² and ±L⁴RLR³LR² are mirror-broken, selected by their "
    "words, not their field |")
rep("Main carries the question as the standing lead L241 |",
    "Main carries the question as the standing lead L241. " + V + " Carried from the SM seat's v1.3 (sm:B1521 C2–C3): B130 "
    "shows that κ takes a continuum of values on the fixed locus, but its reading that a unit is internally fork-free rests "
    "on an elimination that cannot exclude isolated components (the audit lane's AR4), so the componentwise question is "
    "open. For the register question, the record's registering datum at the group layer is B599's pairing datum, whose "
    "evaluation A = mult_ρ − mult_ρ̄ is odd under the θ swap (B871). Kept apart from the register question, as the SM "
    "seat's v1.3 kept it apart from the owner's act-and-register priority of 2026-10-02 (the audit lane's "
    "`philosophy/P_ACT_AND_REGISTER_2026_10_02.md`): the experiential question, an explicit hypothesis held under Gate 5-Q "
    "(`philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`), never a consequence of the register question and never a claim |")
rep("- the harmonic frame on any state outside m004's levels;",
    "- the harmonic frame's counts on any state outside m004's levels (" + V + " its projective family exists on every word\n"
    "  state to length 12, sm:B1523);")
rep("- **[v1.1]** F-MC on any state other than the root.",
    "- **[v1.1]** F-MC on any state other than the root;\n"
    "- " + V + " the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
    "  seat's sL-10 item 8);\n"
    "- " + V + " the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
    "  allowed; the audit lane's AR4).")

# ------------------------------------------------------------------ §9: four rows (sm:B1525, carried)
rep("| **[v1.2]** signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |",
    "| **[v1.2]** signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |\n"
    "| " + V + " \"the trace map never reads κ\" | B20, B37 | FK12, in B37's literal sense only (the audit lane's AR3) |\n"
    "| " + V + " \"no forced choice in the trace ring\": a unit internally fork-free; the seeds' fields ℚ(√(m²+4)) called "
    "distinct | B130; `docs/OPEN_PROBLEMS.md` gate A | FK12: κ takes a continuum on the fixed locus, but the fork-free reading "
    "rests on an elimination that cannot exclude isolated components (AR4). m = 1, 4 and 11 share ℚ(√5); the seeds stay "
    "non-conjugate by their traces (AR5) |\n"
    "| " + V + " \"the observer is built\" at the β = 1 transition | B723 | §7, with the B942 and B957 retractions: the "
    "structure kept, both group assignments retracted |\n"
    "| " + V + " the three lines L1–L3 of the selection rule | main's B1455 §1 | B1297's properties of the class index (main's "
    "B1455 addendum); FK9 |")

# ------------------------------------------------------------------ §10
rep("  - GAP3 refined on the audit lane's qualification: \"only from a relation\" was main's sentence, not its result.\n"
    "  - No other status changes.",
    "  - GAP3 refined on the audit lane's qualification: \"only from a relation\" was main's sentence, not its result.\n"
    "  - No other status changes.\n"
    "- **v1.6 · 2026-10-03 · sm:B1526.** Main's head, v1.5, taken as the head, as main asked of both seats (its relay of\n"
    "  2026-10-03: \"Please take v1.5 as head\"). The SM seat's own v1.5 (sm:B1525), made on main's v1.4 in parallel and\n"
    "  numbered the same, answered by its line (sm:B1526 §2). Each carried item was checked with the SM seat's own code\n"
    "  first (sm:B1526 C1–C5).\n"
    "  - Already in main's v1.5, in main's words: GAP3's refinement on the audit lane's qualification.\n"
    "  - Carried from sm:B1525 (marked [v1.6]): in §5, the levels and the word states; at FK9, P's class, the levels, the\n"
    "    word states and the owner's \"choice might be golden\" in their two sealed forms; at FK9 and GAP4, the bar's null\n"
    "    contract; in §7, what of B723 survives (AR6); at FK12, B130's scope (AR4); in §8's frontier, the harmonic frame's\n"
    "    counts off m004's levels, the class index on a mirror-broken family (sL-10 item 8) and B130 component by\n"
    "    component; in §9, four rows.\n"
    "  - Fitted to the owner's framing of FK12: of the three questions sm:B1525 kept apart, the first is the register\n"
    "    question's (i), and the second's group-layer datum (B871) is placed in the register question; the experiential\n"
    "    question stays apart, under Gate 5-Q.\n"
    "  - Made precise at FK9: B1297's P is the fibre's elliptic involution, the class main's B1459 extends to every level\n"
    "    (sm:B1526 C3).\n"
    "  - No status changes. FK1 and FK12 as the owner decided (v1.5).")

open(OUT, "w", encoding="utf-8").write(s)
print("sha256(v1.5, main) =", SHA_V1_5)
print("sha256(v1.6) =", hashlib.sha256(s.encode("utf-8")).hexdigest())
print("[v1.6] marks:", s.count(V))
