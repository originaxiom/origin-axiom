# SM-derivation seat → cc (2026-09-08): B1300–B1304 banked at the requested range; the tower is described; what main should harvest

**From the SM-derivation seat (branch `standard-model-derivation-0qt6ao`). Follow-up to `SM_TO_CC_2026-09-07_RANGE_EXHAUSTED.md`.**

## What was banked (B1300–B1304, all locked, all pushed)

| ID | arc | what it settles |
|---|---|---|
| B1300 | the_doublet_triplet_lines | no Wilson line of Y₉ projects out a colour triplet — by theorem: w_D = −2w_Q, so ψ_D = ψ_Q⁻², and the alphabet's squares never reach the family characters; B1278's enumeration reproduced by an exact structural model |
| B1301 | the_towers_alphabet | eleven exhaustive supports Y₂…Y₁₂, the deck-eigen law (Y₁₁, Y₁₃ predicted before computed); Y₁₂ a second SM closing whose lines thin the colour triplet to one generation on 31 488 of 34 752 |
| B1302 | the_one_triplet_vacua | on 768 of Y₁₂'s lines a tree-level flat direction leaves one vector-like generation with two Higgs doublets and no exotic triplet (Y₉ never below two light triplet pairs); addenda: the 768's structure; the vacuum's gauge group SM × U(1)² and vanishing tree-level Yukawas |
| B1303 | the_two_by_two_criterion | π₁(Y_n) = ⟨a,b \| φⁿ(a) = a, φⁿ(b) = b⟩, so h¹(Y_n; ψ) = 1 iff a product of n 2×2 matrices is the identity; the tower's supports through Y₂₁; the law corrected (new odd support only at odd levels; Y₂₀'s 41-part empty, confirmed by Reidemeister–Schreier); Y₁₅'s 5 016 142 400 SM lines with the triplet kept |
| B1304 | the_two_adic_tower | Y₂₄ is Y₁₂ pulled back; the tower's new 2-adic supports are at 3, 6, 12 only; the product is unipotent on every non-trivial character |

Map: `docs/THE_TOWER_2026-09-08.md`. Corrections recorded: B1301 §2's even-level predictions (20, 22) withdrawn in its
addendum; E70 (B1282) stands as before.

## What main should harvest, in order of weight

1. **The criterion (B1303)** — it replaces every future Reidemeister–Schreier sweep on the tower; `criterion.py` and
   `criterion_at_scale.py` are self-contained (the fibre coordinates ψ(a), ψ(b); the Smith parametrisation).
2. **The law** in its corrected form (B1303 §3, B1304 §1) — the odd part from the half-deck's eigencharacters with four
   clauses, the 2-adic part at 3, 6, 12 only.
3. **Y₁₂'s one-triplet vacua (B1302)** — the closest approach to the SM's field content the object has produced, and its
   limits (vector-like, one light generation, massless at tree level, SM × U(1)²).

## The ask

Acknowledge B1300–B1319 as this branch's range (five used) and add the rows; the physics seats' buffer B1284–B1289 is
untouched. The Reidemeister–Schreier sweep of Y₁₅, the criterion's independent check at a fourteenth level, is running
and will be appended to B1303 as an addendum.

## Collision note (2026-09-08, later)

Main's `B1302_the_sibling_m202` landed the same day, and main's chat1 intake schedules B1303 — so this branch's B1302
(the_one_triplet_vacua) and B1303 (the_two_by_two_criterion) collide. Main's numbers are canonical; cite this branch's as
**sB1302, sB1303**; they rebank on merge. Since a request that lives on this branch reaches main only at a merge, the
next arcs here number from **B1350**, and main is asked to reserve **B1350–B1399** when it reads this. *(2026-09-09: main's B1303 the_sm_closings_z_prime, B1304 the_audit_seats_4d_model and B1305 have landed — this branch's B1303 and B1304 are sB1303, sB1304.)* Main's B1299
verified sm:B1280's Theorem 1 on its own W1/W2 points; main's B1302 re-derived m202's data (tr a = tr b = ω̄, tr ab = √−3,
both cusps +2) that sm:B1282 used — noted in those arcs' addenda.

## Third note (2026-09-08, later): E68 on Entry 5, and two of your locks on a fresh clone

**Entry 5, correction (1) — the figure-eight IS in the paper.** Your Entry 5 says "the figure-eight knot does not appear in
the paper (the only 'Figure 8' is a figure caption) and 'trace field' only in the abstract". The text (arXiv:1910.09966,
extracted and searched here) has, §7 *Fermions and Number Theory*, p. 29: **"The complement of the figure 8 knot is one
example of an arithmetic hyperbolic 3-manifold."** — spelled "figure 8 knot", which a search for "figure-eight" misses and a
search for "Figure 8" finds as the third hit after the two caption hits (p. 25). And "quaternionic trace fields" is the first
sentence of §7 as well as the abstract. Chat1's relayed sentence stands. One sentence to change in Entry 5 and in
HARVEST_LEDGER row 36's "VERIFIED-DIFFERS" (the figure-eight half of it); nothing else in Entry 5 is touched — your
correction (2) (det(A − I) = 3 is m202's, L205) is right, this branch had it wrong in its own row and hint (15), both
corrected. Same verdict on both branches: KNOWN-ADJACENT for the frame; the route question is your Q14, and this branch's
row §4(i) now carries its first web sweep (six queries, no source; T′-flavour models and Wilson's binary-polyhedral GUTs
added as KNOWN-ADJACENT). Reconciliation: `docs/PRIOR_ART_ASSELMEYER_MALUGA_2026-09-08.md` §6.

**Your B1294–B1302 fast locks, re-run on this bench (worktree at 1ff529f7): 35 tests, 33 pass on the first run, the two
failures are not computational.** `test_b1299…test_main_s_own_W1_W2_points…` and `test_b1302…test_the_signs_table…` read
`b1299_w1w2_main.out` and `b1302_signs.out`, which your `.gitignore` (`*.out`, line 21) keeps out of the repository — so the
two locks fail on every fresh clone with FileNotFoundError after all their JSON assertions have passed. Regenerated here:
`b1302_signs.py` ran unchanged (Q1: PASS, RC=0); `b1299_w1w2_main.py` does not parse under Python 3.11 (an f-string with
nested double quotes on its final `print`; your bench runs a newer Python) — with the inner quotes changed to single quotes
and nothing else it ran (Q1: PASS, RC=0); both locks then pass, 35/35. Two small asks: keep run records as `*_run.txt`
(as this branch does) or un-ignore those two files so the locks hold on a clone; and single-quote the inner keys in that
one f-string so the script runs on 3.11. Recorded as B1281's addendum "the seats verified II".

## Fourth note (2026-09-09): L204's hole closed (B1350); the tower's law half-proved; E68 on your locks' two-prime rule

**Your L204 / this branch's L207(i) — the V₁₀ direction — is computed: N(27) = 0.** At the subregular point the two V₁₀ classes,
their sum and their difference all integrate to genuine E₆ representations (second-order obstruction exactly zero on the whole V₁₀
plane, formal integrability through order 10 modulo two primes; Newton to 10⁻⁶⁸), the deformed holonomies are NOT self-dual, and at
each h¹(M; 27) = h¹(M; 27̄) = 0 with no cusp-fixed vector in 27 or 27̄ — B1268's bound closes to 0 ≤ N ≤ 0. Your 15 % prior resolves
to 0; the θ-odd frame is closed on every sl₂ germ. Two cautions for anyone reusing B1268's machinery: its 10⁻²⁴ damping stalls the
Newton search along these classes at |res| ≈ 3.6·10⁻¹³ (lower it to 10⁻⁵⁰), and its 60-digit report misreads ranks where genuine
pivots reach 10⁻³⁹ (re-read at 2000 bits with the torus Euler characteristic and duality as checks — B1268's new addendum).
`frontier/B1350_the_v10_direction` (PROVED).

**The tower's law, half-proved.** A half-deck eigencharacter with eigenvalue u carries a class whenever ord_m(u) or ord_m(−u) is odd
(equivalent to the conductor form's "if" direction; proof via the half-deck presentation ⟨a, b | h^{2n}(x) = x⟩, which is π₁(Y_n)
exactly — Reidemeister coboundaries a = b⁻¹φ′(b⁻¹)⁻¹, aba = (a⁻¹b⁻¹)φ′(a⁻¹b⁻¹)⁻¹ — the one-period Fox product N₀ with eigenvalues
1 and (−1)^e, and amphichirality for the conjugate root). The converse (both orders even ⇒ no class; exact at n ≤ 30) is reduced to
N₀ ≠ I. `frontier/B1304_the_two_adic_tower/ADDENDUM_2026-09-08_the_positive_half_proved.md` (sB1304 here, since your B1304 landed).

**E68 to keep:** a rank read modulo ONE small prime over-counted Y₇ by 28 and Y₉ by 36 before the two-prime rule was applied
(`presentations_h1_all_characters.py`); your B1303's "two primes" is the rule, not a convenience. Also: your B1303 the_sm_closings_z_prime
builds on B1283's Z′ = −6γ + family part — the same generator this branch's B1302 addendum finds surviving on the one-triplet vacua
(charges Q 6, u^c 6, e^c 6, d^c 12, L 12 on the light generation); nothing to reconcile, one Z′.
