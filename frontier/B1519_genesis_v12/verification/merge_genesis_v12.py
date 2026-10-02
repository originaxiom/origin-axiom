"""GENESIS v1.2 (sm:B1519): main's v1.1 (B1454, at f655034b) taken as the head, as main asked; the SM seat's own v1.1
amendment (sm:B1517, made the same day on its branch) folded in; and B1519's additions. Exact replacements only, each must
match once. Usage: python3 merge_genesis_v12.py MAIN_V1_1.md OUT.md"""
import hashlib
import sys

SRC, OUT = sys.argv[1], sys.argv[2]
s = open(SRC, encoding="utf-8").read()
SHA_MAIN_V1_1 = hashlib.sha256(s.encode("utf-8")).hexdigest()
V = "**[v1.2]**"


def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new)


# ------------------------------------------------------------------ header
rep("**Version 1.1 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and\n"
    "adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked\n"
    "**[v1.1]** where it adds content. The version log (§10) lists every change; the v1.0 text as received is kept at\n"
    "`frontier/B1454_genesis_v1_verified_and_adopted/received/GENESIS_v1_0.md`.",
    "**Version 1.2 · 2026-10-02 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and\n"
    "adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked\n"
    "**[v1.1]** where it adds content. The SM seat amended v1.0 the same day on its own branch (sm:B1517), also numbered 1.1\n"
    "there, before main's was read. v1.2 (sm:B1519) takes main's v1.1 as the head, as main asked, and adds that amendment and\n"
    "its own, each marked **[v1.2]**. The version log (§10) lists every change; the v1.0 text as received is kept on main in\n"
    "B1454's arc (`received/GENESIS_v1_0.md`).")

# ------------------------------------------------------------------ §0: the sweep, both forms
rep("  `scripts/checks/topic_sweep.py`, and for B1–B500 `docs/EARLY_RECORD_INDEX.md`, whose verdict lines predate today's\n"
    "  vocabulary (WORKING_RULES, the rule of 2026-10-02).",
    "  `scripts/checks/topic_sweep.py`, and for B1–B500 `docs/EARLY_RECORD_INDEX.md`, whose verdict lines predate today's\n"
    "  vocabulary (WORKING_RULES, the rule of 2026-10-02). " + V + " The SM seat's form of the same rule records the sweep as\n"
    "  data (`prior_work` in each verdict file, from sm:B1517) and, from sm:B1519, also in a FINDINGS section headed \"Seen\n"
    "  first\", as main's arcs do from B1454. A sweep's terms include an object's names and explicit forms, not only the\n"
    "  concept's words (sm:B1517's miss of m207, §3).")

# ------------------------------------------------------------------ §2: GM5c, the swap native on one route
rep("every metallic bundle double-covers a non-orientable one (B469); the founding torsor's two bits are the swap and the reversal (B1083). |",
    "every metallic bundle double-covers a non-orientable one (B469); the founding torsor's two bits are the swap and the reversal (B1083). "
    + V + " On the words route the swap is native: the Sturmian morphisms abelianise onto the non-negative GL(2,ℤ) matrices, P among them, and the Fibonacci tick is LP (B1323); it is an added axiom on the records route (main B1422). B14's statement is complete, not a search: every integer square root X of a hyperbolic A has A = tr(X)·X − det(X)·I, which lists them all (sm:B1519 K1; the identity is Skuratovskii's Prop. 1, arXiv:2307.13873). |")

# ------------------------------------------------------------------ §3: states (sm:B1517)
rep("**States.** A state is a signed cyclic word s = (ε, w): w is a primitive word in L and R using both letters, taken up to\n"
    "rotation and the L↔R swap, and ε = ±1. It is realised as the once-punctured-torus bundle with monodromy εw, a hyperbolic\n"
    "3-manifold with one cusp. If the swap P is legal (GM5c), the orientation-reversing bundles join them; the Gieseking manifold\n"
    "m000 is the bundle of LP.",
    "**States.** A state is a signed cyclic word s = (ε, w): w is a primitive word in L and R using both letters, taken up to\n"
    "rotation and the L↔R swap, and ε = ±1. It is realised as the once-punctured-torus bundle with monodromy εw, a hyperbolic\n"
    "3-manifold with one cusp. " + V + " A word and its reverse are two states realised by one manifold, with the same\n"
    "orientation; the swap, already divided out, gives the mirror image (sm:B1517 C4, C6). If the swap P is legal (GM5c), the\n"
    "orientation-reversing bundles join them; the Gieseking manifold m000 is the bundle of LP.")
rep("- **Census** (DERIVED; re-derived by sm:B1516 C4 and C5): 2, 2, 4, 6, 10, 18, 32, 56, 102, 186 and 340 states at lengths 2\n"
    "  to 12, 758 in all, as main's B1434 and B1439 count. A word of length n gives a manifold of n ideal tetrahedra. The 24\n",
    "- **Census** (DERIVED; re-derived by sm:B1516 C4 and C5): 2, 2, 4, 6, 10, 18, 32, 56, 102, 186 and 340 states at lengths 2\n"
    "  to 12, 758 in all, as main's B1434 and B1439 count: " + V + " twice OEIS A000048 summed over those lengths. **They realise\n"
    "  536 distinct manifolds**, twice OEIS A000046: 222 states pair off as a word and its reverse, the first pair at length 7\n"
    "  (+LLLRLRR and +LLLRRLR), and SnapPy's isometry signatures give exactly that partition (sm:B1517 C1–C3). A word of length n\n"
    "  gives a manifold of n ideal tetrahedra: the monodromy triangulation, which is canonical (Goodman–Heard–Hodgson 2008,\n"
    "  Lemma 3.2; Guéritaud 2006, §3.2). The 24\n")

# ------------------------------------------------------------------ §3: the signed powers, placed
rep("  main's notation Mₙ; the SM seat's older Yₙ is ambiguous, see ERROR_LEDGER E72).\n",
    "  main's notation Mₙ; the SM seat's older Yₙ is ambiguous, see ERROR_LEDGER E72).\n"
    "- " + V + " **Signed powers.** For u primitive and k even, −uᵏ is a legal signed monodromy (GM5b) that is neither a state\n"
    "  (uᵏ is not primitive) nor a level of a state: (εv)ⁿ = −uᵏ would need εⁿ = −1, so n odd, and vⁿ = uᵏ, so v = u and n = k,\n"
    "  which is even. The audit lane's R78 (sealed 2026-10-02) raised it and tests the bookkeeping at −(LR)². Every hyperbolic\n"
    "  monodromy is exactly one triple (u, k, ε) ↦ εA(u)ᵏ, u primitive with both letters, since the cyclic word of a\n"
    "  hyperbolic class is unique up to rotation and swap (Salepci, arXiv:1006.0752, §7). A state is k = 1, and the n-fold\n"
    "  level of (u, k, ε) is (u, kn, εⁿ). So −uᵏ is a level of a state exactly when k is odd; for k even its seeds are −u²,\n"
    "  −u⁴, −u⁸, …, a tower above each u. The first is **m207 = −(LR)²**, H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3, in m004's commensurability class\n"
    "  (its double cover t12839 is m004's fourth level). It was in the record before it was asked about: sm:B1385 §2 S4\n"
    "  (±(LR)², ±(LR)³, ±(LR)⁴), main B1418's class census and B1224's CS census, among nineteen arcs; R78 recovered it and\n"
    "  proved it is no level of any signed seed (sm:B1519 K5 reproduces both). The census above counts states (k = 1); a\n"
    "  count over the full grammar says whether it includes the signed seeds. Their legality is GM5b's (FK4). R78's\n"
    "  representation is adopted.\n")

# ------------------------------------------------------------------ §3: B979's slip
rep("load-bearing and it is one bit — it is where φ enters rather than −φ or φ². B1323: it is the placement of the swap\n"
    "inside the tick, (LP)² = LR against (PL)² = RL.",
    "load-bearing and it is one bit — it is where φ enters rather than −φ or φ². B1323: it is the placement of the swap\n"
    "inside the tick, (LP)² = LR against (PL)² = RL. " + V + " B979's record says LR and RL are conjugate \"via P\"; they are\n"
    "conjugate by L, as above, and P sends LR to RL, not to (LR)⁻¹ (sm:B1519 K3).")

# ------------------------------------------------------------------ §4: T-ROOT's formula credited (sm:B1517)
rep("and C5 (SnapPy: of 46 orientation-reversing bundles to length 6, only m000 is torsion-free). |",
    "and C5 (SnapPy: of 46 orientation-reversing bundles to length 6, only m000 is torsion-free). " + V
    + " The formula is H₁ = ℤ ⊕ coker(φ − 1) (Chun, Gukov, Park and Sopenko 2019, §2.2 eq. (11)), read with det φ = ±1. |")

# ------------------------------------------------------------------ §4: SE2's cost, the base rate named
rep("since π₁(m000) has the same 48 surjections onto 2T. What dropping SE2 would break is not computed. B1003 locks the prices of all seven forks. |",
    "since π₁(m000) has the same 48 surjections onto 2T. What dropping SE2 would break is not computed. B1003 locks the prices of all seven forks. "
    + V + " Re-derived (sm:B1519 K4, K6): 48 surjections each for π₁(m000) and π₁(m004). The 6 of 200 are m003, m004, m135, m136, m206 and m207 — the root and its relatives — and the 40 double covers are not matched to them in cusps or size, so the comparison does not pass the third step of the bar (`docs/THE_BAR.md`, comparable objects). |")

# ------------------------------------------------------------------ §5: 87 of 536 (sm:B1517)
rep("while 95 of the 758 carry a generation-shaped background at their own level in F-CI (main B1439). **A result is a statement\n"
    "about a frame applied to an object, never about the architecture as such.**",
    "while 95 of the 758 carry a generation-shaped background at their own level in F-CI (main B1439): " + V + " 87 of the\n"
    "536 manifolds they realise (sm:B1517 C5). **A result is a statement about a frame applied to an object, never about the\n"
    "architecture as such.**")
rep("| The other word states (758 to length 12) | closed (sm:B1385 T1) | 95 carry a background at their own level (main B1439), among them m369 (8) and s639 (16) (main B1434) | never computed | never computed |",
    "| The other word states (758 to length 12; " + V + " 536 manifolds) | closed (sm:B1385 T1) | 95 carry a background at their own level (main B1439; " + V + " 87 of 536 manifolds, sm:B1517 C5; no criterion in the fibre torsion and the sign decides which, sm:B1518), among them m369 (8) and s639 (16) (main B1434) | never computed | never computed |")

# ------------------------------------------------------------------ §6: count units and the sweep (sm:B1517)
rep("The tag lives in an arc's verdict file (field `scope`) and in each kill-graph entry (field `scope`).",
    V + " A count over states names its unit, word states or manifolds: a word and its reverse are two states and one manifold\n"
    "(§3). An arc also records what it swept before it claims anything, in the repo and in the literature (§0).\n\n"
    "The tag lives in an arc's verdict file (field `scope`) and in each kill-graph entry (field `scope`).")

# ------------------------------------------------------------------ §7: GAP4 and the bar; the observer's closings
rep("- **GAP4, selection and coincidence.** With hundreds of states, four frames, many levels and several end conditions, a\n"
    "  Standard-Model-like feature somewhere is expected by chance. A selection rule and a null model must be fixed before a\n"
    "  match counts.",
    "- **GAP4, selection and coincidence.** With hundreds of states, four frames, many levels and several end conditions, a\n"
    "  Standard-Model-like feature somewhere is expected by chance. A selection rule and a null model must be fixed before a\n"
    "  match counts. " + V + " The null model and the grading are fixed: `docs/THE_BAR.md` (sm:B1518), a card, the base rate\n"
    "  in a named unit, the comparable objects, selection and trials, and B614's gate p < 0.01, graded DERIVED, REPRODUCED,\n"
    "  FITTED or UNJUDGED. Nothing in the record clears it: the root's higher levels fire as their neighbours do (REPRODUCED),\n"
    "  m369 and s639 were found by a scan (FITTED if offered as evidence), and the harmonic frame's counts are UNJUDGED. The\n"
    "  selection rule (FK9) is still open.")
rep("  of it has been turned into a potential, a breaking or a running that fixes a value.",
    "  of it has been turned into a potential, a breaking or a running that fixes a value.\n\n"
    + V + " **The gaps and the observer.** Several open items of this page are, under other names, closings in the record's\n"
    "observer line. The object supplies four incompletenesses (space, time, charge, value) and the observer supplies every\n"
    "closing — a filling slope, an arrow, a chirality (a Galois sheet), a basepoint; \"measurement is the symmetry-breaking\n"
    "choice\" (B717, with B716 and B723). The end condition chosen rather than derived (GAP2, FK10) is the space closing.\n"
    "SE2's orientable root is amphichiral by construction, and eight of the record's walls pass through that amphichirality\n"
    "(§4, B1234), among them no dimensionful quantity, CS = 0 and chirality not self-supplied: at the archimedean place the\n"
    "object fixes only what is mirror-even and dimensionless, and the mirror-odd orientation and the scale are the\n"
    "observer's (B1168, OPEN). The record went further. THEOREM_LEDGER C18 prices the line: the object is \"a fully\n"
    "transparent, self-naming, integrated speaker that cannot choose\" (B759–B762). It names itself and cannot sign itself,\n"
    "and the missing sign is one ℤ/2 class, the orientation (B1183 and B1184, PROVED; B1163 and the synthesis B1169, OPEN).\n"
    "Main's B1327 (OPEN) proposes re-typing most closings as relations, invariants of a pair that need a partner rather than\n"
    "an act; only a choice with neither an invariant selector nor a relation needs anybody. v1.0 did not carry the line,\n"
    "and v1.1 lists C18 beside F-MC (§9). Whether the closings belong to the genesis is fork FK12 (§8).")

# ------------------------------------------------------------------ §8: FK3, FK6, FK9, FK12
rep("| FK3 | The swap P: legal move, and of what type | OPEN | an operational meaning for P (redescription, parity, time reversal) that the frames can test |",
    "| FK3 | The swap P: legal move, and of what type | OPEN | an operational meaning for P (redescription, parity, time reversal) that the frames can test. " + V + " B1083 types the swap as the C-type bit and the reversal as a parity bit, with the arrow on neither (read with main's naming addendum); conjugation by P sends LR to RL, not to (LR)⁻¹, and LR is conjugate to its inverse by J = [[0,1],[−1,0]] in SL(2,ℤ) (B16; sm:B1519 K3). On m004 the swap, the arrow and the mirror carry one relation: its eight isometries act on the cusp by diag(s_m, s_l), each sign pair twice, with orientation sign s_m·s_l; main's B1327 (OPEN) reads s_m as the arrow and s_l as the swap, so the mirror is the swap times the arrow, and asks, without asserting it, whether the genesis books one of the three bits twice (sm:B1519 K7) |")
rep("| FK6 | Positivity (GM5d) | CHOSEN | a reason the physical states are the non-negative cone |",
    "| FK6 | Positivity (GM5d) | CHOSEN | a reason the physical states are the non-negative cone. " + V + " One candidate is on record and not adopted: B1083 reads positivity as the arrow's home, \"never a choice\" |")
rep("| FK9 | Selection: what makes a state physical | OPEN | a rule fixed before computing, with a null model (GAP4) |",
    "| FK9 | Selection: what makes a state physical | OPEN | a rule fixed before computing, graded by `docs/THE_BAR.md` (" + V + " sm:B1518; GAP4). " + V + " A symmetric law can have states its symmetry does not fix: main's B1455 (sealed 2026-10-02, not yet run) tests whether each vacuum of the bridge's harmonic family on m004 is fixed by a symmetry under which the count is odd; a vacuum fixed by none comes with a mirror partner of equal action |")
rep("| FK11 | The dictionary (I-26) | UNEARNED | a frame derived from M-theory or from the principle, with its scope proved |",
    "| FK11 | The dictionary (I-26) | UNEARNED | a frame derived from M-theory or from the principle, with its scope proved |\n"
    "| FK12 " + V + " | The observer: are its closings part of the genesis, or inputs beyond it? (THEOREM_LEDGER C18 makes them inputs; the owner's question of 2026-10-02: does the act emerge with its observer, the tracker of ab against ba?) | OPEN | for each closing, a partner that supplies it as a relation (main B1327, OPEN) or a proof that none can. Within the object the sign is settled: the object cannot sign itself (B760, NEGATIVE; B1183, B1184, PROVED), and no rule built only from its own invariants selects it canonically (B1225; its self-name is mirror-even, B1184); the trace map conserves κ = tr[a, b] and never reads it (B20, B37). A symmetric law can still land in a state it does not fix (FK9, main's B1455). The owner's framing decides whether the genesis generates the partner with the act |")

# ------------------------------------------------------------------ §9: crosswalk
rep("| **[v1.1]** C18, the observer's closings | THEOREM_LEDGER | not part of the genesis: an input of F-MC (§5) |",
    "| **[v1.1]** C18, the observer's closings | THEOREM_LEDGER | not part of the genesis: an input of F-MC (§5). " + V + " The record's observer line runs from B716–B723 through B759–B762, B1168, B1169, B1183 and B1184 to main's B1327; whether the closings belong to the genesis is FK12 |\n"
    "| " + V + " signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |")

# ------------------------------------------------------------------ §10: the version log
rep("  - Unchanged and still the owner's: FK1.\n",
    "  - Unchanged and still the owner's: FK1.\n"
    "- **v1.1 on the SM seat's branch · 2026-10-02 · sm:B1517.** Made the same day as main's v1.1, before it was read, and folded\n"
    "  into v1.2 (marked [v1.2] there). The first sweep under the rule of that date applied to v1.0's own claims: the 758 word\n"
    "  states realise 536 manifolds, a word and its reverse giving the same oriented manifold and the swap the mirror image\n"
    "  (sm:B1517 C1–C6; OEIS A000048 and A000046; Goodman–Heard–Hodgson 2008 and Guéritaud 2006); signed powers recorded as\n"
    "  neither states nor levels; T-ROOT's homology formula credited; main's 95 of 758 is 87 of 536 manifolds; a count names\n"
    "  its unit, and arcs record their prior-work sweep.\n"
    "- **v1.2 · 2026-10-02 · sm:B1519.** Main's v1.1 taken as the head, as main asked; every one of its 23 changes accepted.\n"
    "  Main's corrections of v1.0 are the SM seat's errors, logged in its ERROR_LEDGER: the misquotation of B1434 and GAP5's\n"
    "  unswept absence.\n"
    "  - Folded in: the SM seat's v1.1 (sm:B1517), above.\n"
    "  - §3: the signed powers placed as the triples (u, k, ε) with ε = −1 and k even, seeds −u^(2^a), m207 = −(LR)² named\n"
    "    (R78; already in sm:B1385 §2 S4, main B1418 and B1224). sm:B1517's \"open\" missed the seat's own record (an E54\n"
    "    instance). B979's \"via P\" noted.\n"
    "  - §2: the swap native on the words route (B1323) and B14 complete by Cayley–Hamilton. §4: B1234's base rate named\n"
    "    and graded; the 48 surjections re-derived.\n"
    "  - §0 and §6: the two seen-first forms, `prior_work` and the \"Seen first\" section. §7: GAP4 points to THE_BAR\n"
    "    (sm:B1518), and the observer line is carried: C18, the parity law, naming without signing (B759–B762, B1168,\n"
    "    B1183, B1184) and main's B1327. §8: FK3 (B1327's relation, sm:B1519 K7), FK6 and FK9 (main's B1455) carry their\n"
    "    records, and FK12, the observer, is registered. §9: two rows.\n"
    "  - No status changes. FK1 and FK12 are the owner's to frame.\n")

open(OUT, "w", encoding="utf-8").write(s)
print("GENESIS v1.2 written from main's v1.1 sha256", SHA_MAIN_V1_1[:16])
