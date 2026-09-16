# s4 — L214, L215 (docs/OPEN_LEADS.md, worktree `<home>/origin-axiom/audit/wt-sm` @ f17dd84e)

## L214 — THE LEVEL MISMATCH: THE THREE ON Y₃, THE STANDARD-MODEL LINES ON Y₉ AND Y₁₂
(registered 2026-09-15; the closing's synthesis)

**The question it registers.** A deck orbit of three apexes exists only at the level whose deck has order 3, i.e. only on Y₃
(B1356); but Y₃'s alphabet is (ℤ/4)² and — per B1277/B1300 — carries no Standard-Model Wilson line, while the record's actual
SM lines (and its one-triplet vacua) live on Y₉ and Y₁₂ (B1283, B1302), hyperbolic levels with no flat background and deck
orbits of nine and twelve respectively. So, as first registered, **no single closing in the record carried both the three
chiral 27s and the E₆ → SM symmetry breaking** — the three and the breaking sat at different levels of the tower.

**Computation named as next step (as originally registered):**
(i) the descent's Wilson lines — whether an SM line exists on the object's own closing (one apex, one neutral 27);
(ii) a breaking of E₆ on Y₃ by something other than a flat connection;
(iii) whether three apexes on Y₉ or Y₁₂ can be placed as a non-deck-orbit consistent with the sum rule and Witten's inflow.

**What is already done on the seat (arc by arc, all same day, 2026-09-15):**
- B1363: (i) settled negative for *abelian* lines — the descent's H₁ = ℤ/3, and Kac's six order-3 inner-automorphism classes of
  E₆ contain no Standard Model class (nor any of the eleven order-4 single-element classes). Non-abelian lines of P2₁3 left open.
- B1364: **L214 RESOLVED as design.** A *non-abelian* Wilson line does it: the SM's centraliser in E₆ is SU(2)_β × U(1)²
  (dim 5 = B1269's c(s)); a Q₈ ⊂ SU(2)_β (24 surjections F(2,6) ↠ Q₈) has centraliser SU(6); one order-4 character of the
  U(1)² kills exactly the 8 Standard-Model roots of SU(6): unbroken group SU(3)×SU(2)×U(1)_Y×U(1)′ exactly, B1269's minimum.
  This dissolves the mismatch because the generations sit at the apexes (full 27s), not in h¹ — B1277's "no SM line on Y₃" was
  a statement about the *h¹ generation-counting framework*, which the apex design does not use. The descent cannot follow (its
  order-3 characters leave ≥ 17 unbroken generators, B1363/B1364).
- B1365: the resolved line's bulk computed (U(1)′ = U(1)_η, B1283's Z′ charges, family-universal; H¹(Y₃;78_ρ) = three flat
  moduli + one vector-like (3,1)_{−1/3} pair, no doublet) — and at this next step the *resolved* design fails the neutrino
  test (no seesaw) → spawned L215.

**What would be a false owner-call (E79) — i.e. decidable now, not a judgement call.** Two things in this lead are pure
computation, not a design/taste choice, and calling them "open for the owner to decide" would be an E79-class error:
1. Whether the non-abelian-line resolution (B1364) is internally consistent as *group theory* (root system enumeration,
   the count of surjections, which roots the order-4 character kills) — this is fully computed and checked (B1364, "root
   system; enumeration"); there is no residual judgement call here, only whether one accepts the apex-vs-h¹ *framing*
   (which is itself forced once one accepts B1356's deck-orbit argument, not a free choice).
2. Whether the abelian-line route (i) is exhausted — B1363 computed Kac's full classification (six classes) and found none
   match; this is decidable by table lookup against Kac, already done, not an open judgement.
What genuinely remains a computation (not decidable now, correctly left open): the non-abelian lines of P2₁3 beyond what
B1364 covers on Y₃ itself would only bear on the *descent's* prospects, and item (iii) (three apexes on Y₉/Y₁₂ as a
non-deck-orbit) has not been attempted at all — that is a real open computation, not a place for an owner call either.

---

## L215 — THE 27̄ SECTOR AND THE SEESAW
(registered 2026-09-15, B1365; the design's next structural step)

**The question it registers.** The three-apex closing (with the U(1)_η line resolving L214) has, as its only E₆-charged
Standard-Model singlets, the apex 27s' N and ν^c, both carrying the *same* U(1)_η charge (γ = −5/3) — so U(1)_η cannot break
above the soft scale on any singlet VEV, the Majorana mass ν^c ν^c is forbidden, and with the E₆ cubic's single coupling
(B1276, y_ν = y_u) the neutrinos come out Dirac at up-quark masses: **the design is excluded unless a 27̄ sector is added.**

**Computation named as next step:**
(a) **anti-apexes** — since the deck acts freely on Y₃'s apexes, 27̄s must come in orbits of three; net chirality
3(n₊ − n₋) = 3 forces nine apexes total (six 27, three 27̄): compute the nine-charge sum rule, the selection rule (which
cubic couplings survive), the vacuum (which pairs get Dirac masses off the bulk moduli, which stay light), and whether the
twistor/Kronheimer local models even admit an apex of opposite E₆ chirality;
(b) **the tower's h¹ sector** — an E₇ or E₈ gauge group on the E₆ locus, whose Wilson line leaves E₆-charged bulk modes
133 ⊃ 27 ⊕ 27̄ (B1277/B1278's three-vector-like-pair mechanism) alongside the three chiral apex 27s: compute the line's
centraliser in E₇, the bulk spectrum by B1365's Fox-calculus method, and the resulting vacuum;
(c) in either case, the neutrino sector itself: M_R, the light masses, and whether B1361's hollow tree-level texture survives
once 27̄ couplings are added.
The document is explicit: "Until (a) or (b) is computed, the closing's design is excluded by neutrino masses."

**What is already done on the seat (same-day analysis, not yet a spent arc):** the seat did a closer read (git commit
`3500f4f7`, "L215 read more closely (analysis, not computed)") that closes route (b) by pure representation theory — the
78 of E₆ contains no 27̄, and E₇/E₈ makes the apex matter vector-like under E₆ itself, pushing the chirality problem into a
U(1) the line must then break — so **27̄s must be anti-apexes, route (a).** It then identifies three binding constraints on
route (a), none of them computed: (1) y_ν = y_u needs M_R ≳ 10¹⁴–10¹⁵ GeV, i.e. ⟨ν̄^c⟩ ≳ 10¹⁶ GeV along a flat direction;
(2) any 27_A 27̄_C membrane-instanton pairing mass is E₆-invariant, so it lifts ⟨N_A N̄_C⟩/⟨ν^c_A ν̄^c_C⟩ exactly when it makes
the pair's quarks heavy — a flat singlet direction and a heavy vector-like generation cannot come from the same pairing;
(3) an unpaired pair's charged components would then get mass from (27_A 27̄_C)²/M, whose F-term caps the flat direction at
⟨N⟩ ~ 10¹⁰–10¹¹ GeV, giving M_R ≲ 10⁴ GeV — two-to-three (first generation) to ten (third generation) orders of magnitude
short. No arc number is spent on this; it is registered "so that the vacuum of nine apexes is not computed before its
inputs exist." The named next instrument (not yet built) is the instanton pairing spectrum of the apexes on the design's
background (the 3-cycles between apex orbits and their C-field charges).

**What would be a false owner-call (E79) — i.e. decidable now.** The document is careful to distinguish "not yet computed"
from "a place for taste": the representation-theoretic exclusion of route (b) (27̄ cannot live in E₆'s 78, so a bigger group
is needed and that then makes the matter vector-like) is fully decided now, by table lookup + logic — there is no judgement
call left in "route (a) or (b)?": (a) is forced. Conversely, calling (a)'s outcome an open judgement would also be an E79
error in the other direction — the three numerical constraints (1)–(3) above are not matters of taste, they are inequalities
already computed to be in tension (10¹⁶ GeV needed vs 10¹⁰–10¹¹ GeV available); what genuinely is not decidable without new
computation, and is correctly left open rather than owner-called, is only the instanton pairing spectrum itself (which zeros
a charged-instanton matrix might have) and whether some non-perturbative flat direction outside the record's inputs exists —
the document names both explicitly as "an assumption the object does not force," i.e. not something to be settled by owner
fiat either.
