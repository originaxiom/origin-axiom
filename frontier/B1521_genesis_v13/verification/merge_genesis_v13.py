"""GENESIS v1.3 (sm:B1521): v1.2 (sm:B1519) as the head, with the audit lane's corrections of three old results (its relay of
1e3d17b9, ACT_REGISTER AR3-AR6), the deciding test's outcome on both benches (main's B1455, sm:B1520) with the correction that
the dualising symmetry is the inversion and not B1297's P, and the owner's priorities of 2026-10-02. Each item is checked with
the SM seat's own code first (which_class_is_P.py, audit_corrections.py). Exact replacements only, each must match once.
Usage: python3 merge_genesis_v13.py ../received/GENESIS_v1_2.md OUT.md"""
import hashlib
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
SHA_V1_2 = hashlib.sha256(s.encode("utf-8")).hexdigest()
assert SHA_V1_2 == "9cf581654dfdac6b52db4f3a7235e1dff6d7a864ee2474388ec7e680afb581a8", SHA_V1_2
V = "**[v1.3]**"


def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new)


# ------------------------------------------------------------------ header
rep("**Version 1.2 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and\n"
    "adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked\n"
    "**[v1.1]** where it adds content. The SM seat amended v1.0 the same day on its own branch (sm:B1517), also numbered 1.1\n"
    "there, before main's was read. v1.2 (sm:B1519) takes main's v1.1 as the head, as main asked, and adds that amendment and\n"
    "its own, each marked **[v1.2]**. The version log (§10) lists every change; the v1.0 text as received is kept on main in\n"
    "B1454's arc (`received/GENESIS_v1_0.md`).",
    "**Version 1.3 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and\n"
    "adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked\n"
    "**[v1.1]** where it adds content. The SM seat amended v1.0 the same day on its own branch (sm:B1517), also numbered 1.1\n"
    "there, before main's was read. v1.2 (sm:B1519) takes main's v1.1 as the head, as main asked, and adds that amendment and\n"
    "its own, each marked **[v1.2]**. v1.3 (sm:B1521) carries the audit lane's corrections of three old results, the deciding\n"
    "test's outcome on both benches and the owner's priorities of 2026-10-02, each marked **[v1.3]**. The version log (§10)\n"
    "lists every change; the v1.0 text as received is kept on main in B1454's arc (`received/GENESIS_v1_0.md`), and v1.2's in\n"
    "sm:B1521's (`received/GENESIS_v1_2.md`).")

# ------------------------------------------------------------------ §7: B723 with both retractions (AR6)
rep("closing — a filling slope, an arrow, a chirality (a Galois sheet), a basepoint; \"measurement is the symmetry-breaking\n"
    "choice\" (B717, with B716 and B723). The end condition chosen rather than derived (GAP2, FK10) is the space closing.",
    "closing — a filling slope, an arrow, a chirality (a Galois sheet), a basepoint; \"measurement is the symmetry-breaking\n"
    "choice\" (B717, with B716 and B723). " + V + " B723 is cited with the two retractions on its own banner. B942: complex\n"
    "conjugation is not in Gal(K^ab/K), so the sheet's ℤ/2 is the quotient Gal(K/ℚ), arithmetic and present at every\n"
    "temperature, not produced by a cooling. B957: the values clause too, since B700's torsor has group ℤ/2 over a quadratic\n"
    "field and CMR's is the infinite idèle class group of ℚ(√−3). What survives is the structure, a measurement as a choice of\n"
    "fibre functor with a Galois ambiguity, not either group assignment (the audit lane's AR6; sm:B1521 C4). The end\n"
    "condition chosen rather than derived (GAP2, FK10) is the space closing.")

# ------------------------------------------------------------------ §8: FK9, the deciding test run; the golden hypothesis registered
rep("**[v1.2]** A symmetric law can have states its symmetry does not fix: main's B1455 (sealed 2026-10-02, not yet run) tests "
    "whether each vacuum of the bridge's harmonic family on m004 is fixed by a symmetry under which the count is odd; a vacuum fixed "
    "by none comes with a mirror partner of equal action |",
    "**[v1.2]** A symmetric law can have states its symmetry does not fix: main's B1455 (sealed 2026-10-02) tests "
    "whether each vacuum of the bridge's harmonic family on m004 is fixed by a symmetry under which the count is odd; a vacuum fixed "
    "by none comes with a mirror partner of equal action. " + V + " Run on both benches the same day by routes that share no "
    "code (main's B1455; sm:B1520): every vacuum μ ⊗ ρ_q at level one is fixed by the inversion followed by dualising, so the "
    "count is zero on the whole family and the vacuum does not select there (NEGATIVE; frame F-HE, reach single). The three "
    "lemmas are B1297's (main's B1455 addendum). The dualising symmetry is the inversion, not B1297's period-2 symmetry P: P is "
    "the swap's class and fixes ρ_q (sm:B1521 C1). B1297's tower theorem (P inverts every twist) and the family's (the inversion "
    "dualises ρ_q) therefore rest on different symmetries, and the levels stay open (main's L242 (b)). The owner's hypothesis of "
    "the same day, \"choice might be golden\", is registered here and tested only in forms sealed before computing |")

# ------------------------------------------------------------------ §8: FK12, AR3 and AR4 scoped; the owner's three questions; the measurer's referent
rep("the trace map conserves κ = tr[a, b] and never reads it (B20, B37). A symmetric law can still land in a state it does not "
    "fix (FK9, main's B1455). The owner's framing decides whether the genesis generates the partner with the act |",
    "the trace map conserves κ = tr[a, b] and never reads it (B20, B37). " + V + " That holds in B37's literal sense only: its "
    "test is for the presence of a symbol, which a vacuous rewriting on the record graph r = κ turns on without changing the "
    "dynamics, so it neither shows nor excludes a self-model (the audit lane's AR3; sm:B1521 C2). B130 shows that κ takes a "
    "continuum of values on the fixed locus, but its reading that a unit is internally fork-free rests on an elimination "
    "that cannot exclude isolated components (AR4; sm:B1521 C3); the componentwise question is open. A symmetric law can still land in a state it does not fix (FK9, main's B1455). " + V + " On "
    "m004's family it does for half of the symmetries, one kind of mirror among them, and never for a count-odd one (main's "
    "B1455 §3; sm:B1520). The owner's framing decides whether the genesis generates the partner with the act. " + V + " The "
    "owner's priority of 2026-10-02 (the audit lane's `philosophy/P_ACT_AND_REGISTER_2026_10_02.md`): the primitive may be an act "
    "of distinction together with the relation that registers it. Three questions stay apart: whether a reduction loses data a "
    "declared later operation needs (exactly when that operation fails to descend, the audit lane's AR1 and AR2); whether the "
    "architecture derives a registering mechanism (an action, a state and an interaction, in one theory; at the group layer the "
    "record has one, a chirality-registering measurement as B599's pairing datum, whose evaluation A = mult_ρ − mult_ρ̄ is "
    "odd under the θ swap, B871); and the experiential "
    "question, an explicit hypothesis held under Gate 5-Q (`philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`), never a consequence "
    "of the other two and never a claim. The measurer has one exact referent on the record: the count \"is blind to every "
    "symmetry of the space, mirrors included, and sees only which of a module and its dual is read as the particle\" (main's "
    "B1455 §5), and the same two pieces stacked in the two orders count −1 and +1 and side by side 0 (main's L241, exploratory; "
    "in the class-index frame B1438's slope law, main's B1455 addendum). A vacuum, being a direct sum, forgets the order |")

# ------------------------------------------------------------------ §8: the frontier list
rep("- **[v1.1]** F-MC on any state other than the root.\n",
    "- **[v1.1]** F-MC on any state other than the root;\n"
    "- " + V + " the deciding test (FK9) on any level of m004 or on any other state (main's L242 (b));\n"
    "- " + V + " the fixed loci of the metallic trace maps component by component (B130's question with isolated components\n"
    "  allowed; the audit lane's AR4).\n")

# ------------------------------------------------------------------ §9: crosswalk
rep("| **[v1.2]** signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |",
    "| **[v1.2]** signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |\n"
    "| " + V + " \"the trace map never reads κ\" | B20, B37 | FK12, in B37's literal sense only (AR3) |\n"
    "| " + V + " \"no forced choice in the trace ring\": a unit internally fork-free; the seeds' fields ℚ(√(m²+4)) called distinct | B130; `docs/OPEN_PROBLEMS.md` gate A | FK12: κ takes a continuum on the fixed locus, but the fork-free reading rests on an elimination that cannot exclude isolated components (AR4). m = 1, 4 and 11 share ℚ(√5); the seeds stay non-conjugate by their traces (AR5) |\n"
    "| " + V + " \"the observer is built\" at the β = 1 transition | B723 | §7, with the B942 and B957 retractions: the structure kept, both group assignments retracted |\n"
    "| " + V + " the three lines L1–L3 of the selection rule | main's B1455 §1 | B1297's properties of the class index (main's B1455 addendum); FK9 |")

# ------------------------------------------------------------------ §10: the version log
rep("  - No status changes. FK1 and FK12 are the owner's to frame.\n",
    "  - No status changes. FK1 and FK12 are the owner's to frame.\n"
    "- **v1.3 · 2026-10-02 · sm:B1521.** The audit lane's relay of `1e3d17b9` answered, and the deciding test's outcome carried;\n"
    "  each item checked with the SM seat's own code first (sm:B1521 C1–C4).\n"
    "  - §7: B723 cited with the B942 and B957 retractions on its banner (AR6).\n"
    "  - §8: FK9 carries the run of main's B1455 and sm:B1520 (NEGATIVE at level one, reach single), the lemmas credited to\n"
    "    B1297, and the correction that the dualising symmetry is the inversion, not B1297's P, which is the swap's class and\n"
    "    fixes ρ_q; the levels stay open (main's L242 (b)). The owner's hypothesis \"choice might be golden\" is registered at\n"
    "    FK9, untested. FK12: the never-reads sentence scoped to B37's literal test (AR3); B130's fork-free reading scoped (AR4); the\n"
    "    owner's act-and-register priority with its three questions kept apart, the experiential one under Gate 5-Q; the\n"
    "    measurer's exact referent (main's B1455 §5 and L241, with B1438).\n"
    "  - §8's frontier list: two items. §9: four rows (AR5's field label among them).\n"
    "  - No status changes. FK1 and FK12 stay the owner's to frame.\n")

open(OUT, "w", encoding="utf-8").write(s)
print("GENESIS v1.3 written from v1.2 sha256", SHA_V1_2[:16])
