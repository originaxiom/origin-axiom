"""GENESIS v1.5 (sm:B1525): main's head, v1.4 (B1458), taken as the head, as main asked of its v1.3 ("Take v1.3 as the
head, or answer a change by its line", its relay of 2026-10-02, §5). The SM seat's own v1.3 (sm:B1521), made in parallel and
numbered the same, is answered by its line: what main's v1.3 and v1.4 had not made is carried, marked [v1.5]. Added since:
the levels (sm:B1522), the word states (sm:B1523), the bar's null contract (sm:B1524), and the audit lane's refinement of
GAP3 (its relay at 24c039c8). Each carried or added item is checked with the SM seat's own code first
(genesis_v15_checks.py). Exact replacements only; each must match once.
Usage: python3 merge_genesis_v15.py ../received/GENESIS_v1_4_main.md OUT.md"""
import hashlib
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
SHA_V1_4 = hashlib.sha256(s.encode("utf-8")).hexdigest()
assert SHA_V1_4 == "d32456b67ae2cb55e036de57c2a8619a8e546b7656144c1cf7ab008615bd557a", SHA_V1_4
V = "**[v1.5]**"


def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new)


# ------------------------------------------------------------------ header
rep("**Version 1.4 · 2026-10-03 · canonical.**", "**Version 1.5 · 2026-10-03 · canonical.**")
rep("main and records what the own-level law is not, each marked **[v1.4]**. The version log (§10) lists every\n"
    "change; the texts as received are kept on main in the arcs that adopted them\n"
    "(`frontier/B1454_genesis_v1_verified_and_adopted/received/GENESIS_v1_0.md`,\n"
    "`frontier/B1456_genesis_v1_2_verified_and_the_seats_reconciled/received/GENESIS_v1_2.md`).",
    "main and records what the own-level law is not, each marked **[v1.4]**. v1.5 (sm:B1525) takes main's head, v1.4, as\n"
    "main asked of its v1.3. The SM seat's own v1.3 (sm:B1521) was made on its branch in parallel with main's and numbered\n"
    "the same; v1.5 answers it by its line, carries what main's v1.3 and v1.4 had not, and adds the seats' results since,\n"
    "each marked **[v1.5]**. The version log (§10) lists every change; the texts as received are kept on main in the arcs\n"
    "that adopted them (`frontier/B1454_genesis_v1_verified_and_adopted/received/GENESIS_v1_0.md`,\n"
    "`frontier/B1456_genesis_v1_2_verified_and_the_seats_reconciled/received/GENESIS_v1_2.md`), and on the SM seat's branch\n"
    "main's v1.4 and the seat's v1.3 in sm:B1525's (`received/GENESIS_v1_4_main.md`, `received/GENESIS_v1_3_sm.md`).")

# ------------------------------------------------------------------ §5, the frame table
rep("by proof (main B1455; independently sm:B1520) |",
    "by proof (main B1455; independently sm:B1520). " + V + " On the levels M₁…M₁₂ the count-odd mirror of those vacua "
    "breaks from M₅ on, off the unit circle exactly where no golden Galois reflection fixes the twist, and every one of "
    "the 196 firing members of levels 1–6 is fixed (sm:B1522) |")
rep("among them m369 (8) and s639 (16) (main B1434) | never computed | never computed |",
    "among them m369 (8) and s639 (16) (main B1434) | " + V + " each is rigid rel cusp, so carries a one-parameter projective "
    "family at its hyperbolic point, and on 262 of the 536 manifolds no isometry dualises it (sm:B1523); counts never "
    "computed | never computed |")

# ------------------------------------------------------------------ §7: GAP3, GAP4, and the observer line
rep("  the right sign. A one-ended state can get the third only from a relation** (FK8). No report derives the source.",
    "  the right sign.** " + V + " The audit lane's results do not prove that a one-ended state can get the third only from\n"
    "  a relation. They prove that a specified flat counted configuration needs an admitted source or end flux, or a\n"
    "  change of hypotheses. Whether a generated relation supplies it stays open (FK8, FK12), and R77's added fields do not\n"
    "  settle their genesis origin. The audit lane refined main's v1.3 wording here (its relay at `24c039c8`); the\n"
    "  refinement keeps the owner's act-and-register priority (FK12) without installing its solution. No report derives\n"
    "  the source.")
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
    "(sm:B1521 C1): B1297's period-2 symmetry P is the swap's class and fixes ρ_q, so B1297's tower theorem (P inverts every "
    "twist) and the family's (the inversion dualises ρ_q) rest on different symmetries. Run since on the levels (main's L242 "
    "(b); sm:B1522, PROVED, frame F-HE): the count-odd mirror breaks from M₅ off the unit circle and from M₆ on it, up to "
    "0.91 of M₁₂'s 103 680 vacua; off the circle it breaks exactly where no golden Galois reflection fixes the twist; and "
    "every one of the 196 firing members of levels 1–6 is fixed, so the mirror breaks only where nothing chiral has been "
    "found. On the word states (sm:B1523, PROVED): every word state to length 12 carries a one-parameter projective family "
    "at its hyperbolic point; main's one-bit rule (an isometry dualises the family exactly when it inverts the fibre "
    "boundary) holds on all of them; and on 262 manifolds (482 states) no isometry dualises the family, so near the "
    "hyperbolic point B1455's symmetry argument cannot force the count to zero there (Lemma T, a local statement). Whether "
    "it is nonzero is the SM seat's sL-10 item 8, sealed first. The owner's hypothesis of 2026-10-02, \"choice might be "
    "golden\", was tested in these two sealed forms: on the levels, off the unit circle, a golden Galois reflection decides "
    "where the mirror breaks; on the word states, of the 14 manifolds with golden monodromy field exactly ±L⁴RL³R² and "
    "±L⁴RLR³LR² are mirror-broken, selected by their words, not their field |")
rep("Main carries the question as the standing lead L241 |",
    "Main carries the question as the standing lead L241. " + V + " Carried from the SM seat's v1.3 (sm:B1521 C2–C3): B130 "
    "shows that κ takes a continuum of values on the fixed locus, but its reading that a unit is internally fork-free rests "
    "on an elimination that cannot exclude isolated components (the audit lane's AR4), so the componentwise question is "
    "open. The owner's priority of 2026-10-02, an act of distinction together with the relation that registers it (the audit "
    "lane's `philosophy/P_ACT_AND_REGISTER_2026_10_02.md`), keeps three questions apart: whether a reduction loses data a "
    "declared later operation needs ((iii) above); whether the architecture derives a registering mechanism, an action, a "
    "state and an interaction in one theory (at the group layer the record has one: B599's pairing datum, whose evaluation "
    "A = mult_ρ − mult_ρ̄ is odd under the θ swap, B871); and the experiential question, an explicit hypothesis held under "
    "Gate 5-Q (`philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`), never a consequence of the other two and never a claim |")
rep("- the harmonic frame on any state outside m004's levels;",
    "- the harmonic frame's counts on any state outside m004's levels (" + V + " its projective family exists on every word\n"
    "  state to length 12, sm:B1523);")
rep("- **[v1.1]** F-MC on any state other than the root.",
    "- **[v1.1]** F-MC on any state other than the root;\n"
    "- " + V + " the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM\n"
    "  seat's sL-10 item 8);\n"
    "- " + V + " the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
    "  allowed; the audit lane's AR4).")

# ------------------------------------------------------------------ §9: four rows
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
rep("  its census claim re-derived by manifold and group structure); §5 and FK9 now point to it on main. No status changes.\n"
    "  - Unchanged and still the owner's: FK1 and FK12.",
    "  its census claim re-derived by manifold and group structure); §5 and FK9 now point to it on main. No status changes.\n"
    "  - Unchanged and still the owner's: FK1 and FK12.\n"
    "- **v1.5 · 2026-10-03 · sm:B1525.** Main's head, v1.4, taken as the head, as main asked of its v1.3 (its relay of\n"
    "  2026-10-02, §5: \"Take v1.3 as the head, or answer a change by its line\"). The SM seat's own v1.3 (sm:B1521), made in\n"
    "  parallel and numbered the same, answered by its line (sm:B1525 §2). Each carried or added item was checked with the SM\n"
    "  seat's own code first (sm:B1525 C1–C6).\n"
    "  - Already in main's v1.3, in main's words: the deciding test's run at FK9 and in §5; the B723 corrections; B37's\n"
    "    literal reading; the count as an order, with B1297 and B1438.\n"
    "  - Carried (marked [v1.5]): at FK9, that B1297's P is the swap's class and fixes ρ_q; at FK12, B130's scope (AR4) and\n"
    "    the owner's three questions kept apart, the experiential one under Gate 5-Q; in §7, what of B723 survives (AR6); in\n"
    "    §8's frontier, B130 component by component; in §9, four rows.\n"
    "  - Not carried: the SM seat's quotation of main's B1455 §5 at FK12. Main's (i) and (ii), with L241, carry its content,\n"
    "    and the quotation brought a word of Gate 5-Q's Q5 outside the governed rooms.\n"
    "  - Added since: at FK9 and in §5, the levels (sm:B1522) and the word states (sm:B1523), and the owner's \"choice might\n"
    "    be golden\" in their two sealed forms; at FK9 and GAP4, the bar's null contract (sm:B1524); at GAP3, the audit\n"
    "    lane's refinement of \"only from a relation\"; in §8's frontier, the class index on a mirror-broken family (sL-10\n"
    "    item 8).\n"
    "  - Left to main: its B1459 (the zeros at B1451's 188 complete points made a theorem, run at `77714caf` after v1.4), for\n"
    "    main's next version in its own words.\n"
    "  - No status changes. FK1 and FK12 stay the owner's to frame.")

open(OUT, "w", encoding="utf-8").write(s)
print("sha256(v1.4) =", SHA_V1_4)
print("sha256(v1.5) =", hashlib.sha256(s.encode("utf-8")).hexdigest())
print("[v1.5] marks:", s.count(V))
