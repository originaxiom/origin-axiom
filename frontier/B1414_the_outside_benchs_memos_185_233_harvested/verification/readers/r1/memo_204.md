# Reader r1 — Memo 204 (THE_OBJECT_IS_6D4.md, + Addenda 1–5)

## 1. HEADLINE
"THE OBJECT'S D₄ IS OF TYPE 6D4, AND IT CARRIES NO TRIALITY OVER ℚ — B882'S CONJECTURE IS
REFUTED." CELL 1/2/3 = B/B/B, all controls pass. Date **2026-09-11** (base memo); Addenda 1–5
dated 2026-09-11/12/13.

## 2. CLAIMS
1. CELL 1: K (the object's charge cubic) is **non-cyclic** — irreducible, disc not a square,
   squarefree part 77, factors `[1,2]` over K, so `|Aut(K/ℚ)|=1`. Grade: **B (exact)**.
2. CELL 2: Killing signature of the 28 = **(+16,−12,0:0) → so(4,4)**, the SPLIT real form.
   Grade: **B (exact congruence)**.
3. CELL 3: for both dual-pair charges (`ad(x8)²`, `ad(x16)²`), the cubic annihilating them
   generates K, commutes with all 28 of the 28, and bite controls fire correctly (a member of
   the 28, and a random 48×48 matrix, correctly report NOT commuting). Grade: **B (exact)**.
4. Main argument: L not split (K, degree 3, can't embed in Mat₂(ℚ)³) ⇒ object not ¹D₄; L
   non-cyclic ⇒ by Knus–Tignol's type table, **object is type ⁶D₄**; by Theorem 4.1, **no
   trialitarian automorphism over ℚ**. Grade: **THEOREM (conditional on the two quoted KT
   statements)**.
5. **B882's conjecture ("arithmetic S₃ = geometric S₃") REFUTED** — "in the direction nobody
   was checking." Grade: **REFUTED**.
6. §6: flags (does NOT resolve) a conflict with B1077/W4's claim that the "UNDRESSED algebra
   attaches the split cubic ℚ³, trivial discriminant, no 77." Grade: **flagged, unresolved
   at time of writing**.
7. §8: an earlier in-session claim ("the object has triality over ℚ in its bare form") is
   **WITHDRAWN and now REFUTED** (Theorem 4.1's necessary condition misread as sufficient).
8. Addendum 1: over **ℚ(√77)** (minimal, = fixed field of A₃ in the S₃ closure), L becomes
   cyclic, type drops to **³D₄**, L-obstruction gone. "77 is the exact price of buying
   triality at all," not a mechanism. Grade: **B (exact)**; fence: whether E (Allen invariant)
   is split at ℚ(√77) is **NOT verified** in Addendum 1.
9. Addendum 2: sextic `t⁶−15095808t⁴+56970854793216t²−23922095638236364800` is **irreducible
   over ℚ**; F₆=ℚ[ad(x8)|48] is a degree-6 field = **K(√77)**, the Galois closure of K; the
   8-dim representation (splitting E) lives over F₆. A prior mod-p meataxe finding (proper
   submodule dim 24 at two primes) is explained as an artifact — sextic factors [2,2,2] at
   exactly those primes. Grade: **B (exact)**; explicitly does NOT decide if E splits over K
   itself.
10. Addendum 3: **B1077 REPRODUCES** exactly (Gram signature (4,4), signed disc 1/256 square,
    Witt index 4) — "the flagged conflict is NOT a conflict... resolves in B1077's favour":
    B1077's object (bare octonion norm form) and memo 204's object (the e6-embedded cubic from
    forced charges) are different objects; B1077 had predicted the 77 must come from
    "measurement-dressing." Grade: **B (exact)**; conflict from §6 CLOSED, no arc retracted.
11. Addendum 4: reduces the open "is E split over K" question to ramification of ONE
    quaternion algebra over K (dim-12 commutant, centre K, contains K(√77) as max subfield),
    unramified at all 3 real places (from so(4,4)). Grade: **reduction, not a result** —
    explicitly "closes nothing."
12. Addendum 5 (memo 222, not itself assigned to r1): answers Addendum 4's open question —
    **E IS SPLIT** — via KMRT Prop. 43.6 (norm-1 in Br) + exhaustive computation that ramified
    primes of Q=K(√77)/K number `n_p ≤ 1` for every p (hence, by evenness, 0). Grade:
    **B (exact, but scoped: "conditional on this memo's own derivation that the commutant is a
    quaternion algebra over K containing K(√77)" — an input, not re-derived in 222**).

## 3. CERTIFICATE
- `certificates/the_object_is_6d4.py` + `outputs/the_object_is_6d4_out.txt` — **both EXIST**;
  tail matches headline (B882 refuted, real-split-vs-arithmetic-twisted tension resolved,
  conflict with B1077 flagged not resolved) verbatim.
- Addendum 2: `certificates/the_price_is_charged_once.py` + `outputs/..._out.txt` — **both
  EXIST**; tail matches ("77 IS NOT ONE PRICE AMONG SEVERAL... resolves both at the same
  extension").
- Addendum 3: `certificates/b1077_reproduces.py` + `outputs/b1077_reproduces_out.txt` — **both
  EXIST**; tail matches ("B1077 REPRODUCES, AND THE FLAGGED CONFLICT IS NOT A CONFLICT").
- Addendum 5 relies on memo 222's certificate (not this memo's own, and memo 222 is outside
  r1's assignment) — not independently checked here.
- No seal named for memo 204 or its addenda.

## 4. ON MAIN ALREADY?
- **(a) already on main, partially**: K's non-cyclicity itself (Claim 1) is **already
  banked** on main, well before this memo — `docs/NOVELTY_SWEEP_LEDGER.md` ("K's corrected
  characterization... K is NOT cubic-cyclic... K is a NON-GALOIS cubic with splitting closure
  S₃ and quadratic resolvent ℚ(√77)", dated to the 2026-08-13 W4 cell) and
  `docs/RETRACTED_PHRASES.md` (retracts "cubic-cyclic K", states "an S₃ cubic with quadratic
  resolvent ℚ(√77)"). So CELL 1 is a *reproduction* of an already-banked fact, not new.
- **(d)/(c)**: `frontier/B1077_intrinsic_split/FINDINGS.md` (2026-08-19) already identifies
  B882's conjecture as "stateable in KMRT's own language: the dressed datum is the ³D₄ twist
  of the split triple by K" and calls the ³D₄-twisting classification (Knus–Tignol
  arXiv:1409.1718) "the literature floor" still to be opened — i.e. main had gotten as far as
  *expecting* type ³D₄ (Aut=ℤ/3) but had **not** determined K's actual cyclicity-in-context
  or applied the type table to get **⁶D₄** and the outright refutation. `docs/
  NOVELTY_SWEEP_LEDGER.md`'s W4 block states explicitly: "unconditional C77 has no
  non-circular formulation as the bank stands. The 77-echo IS B882's conjecture, exactly, and
  nothing weaker" — i.e., **as of 2026-08-18/19 main considered B882 an open, undischargeable
  question**, not refuted. Memo 204's application of Knus–Tignol's Theorem 4.1 + type table
  (external primary sources first read here, per the owner's own framing "verify load bearing
  math, dont lean on old work") is the genuinely new step.
- **(c) NOT on main**: grep for "B882.*refut", "6D4", "Knus.Tignol"/"Knus-Tignol", "Theorem
  4.1", "no triality over" across `docs/` and `frontier/*/FINDINGS.md` (excluding
  `outside_bench/`) returns **zero hits**. The headline conclusion (type ⁶D₄, B882 refuted)
  has not propagated to any main document.
- **(c) NOT on main**: Addenda 1–5's entire chain (ℚ(√77) buys back ³D₄, F₆=K(√77) splits E,
  the quaternion-algebra reduction, and memo 222's ramification computation) — none of this
  appears outside `outside_bench/`.
- No direct contradiction between memo 204 and main was found; the §6-flagged tension with
  B1077/W4 is explicitly resolved (in B1077's favour) by memo 204's own Addendum 3, using two
  independently-built Gram matrices.

## 5. NEEDS COMPUTATION HERE
1. Claim 1 (K non-cyclic, disc squarefree 77): recompute from B900/B866's own μ or monic
   cubic `x³−12x−5` — factor over ℚ (irreducible), compute discriminant's squarefree part
   (sympy `discriminant`, `factorint`); expect squarefree(disc)=77, non-square.
2. Claim 2 (Killing signature (16,12) = so(4,4)): rebuild the 28-dim adjoint-of-D4-in-e6
   Killing form from e6 structure constants and compute its signature by congruence
   (`sympy.congruence` / Sylvester's law); expect (16,12,0).
3. Claim 3/CELL-3 (cubic generates K, commutes with the 28, bite controls fire): compute
   `charpoly(ad(x8)²|48)`, verify it factors as (irreducible cubic)^16, check commutation with
   all 28 generators (0/28 failures) and the two negative-control cases (a 28-member, a random
   48×48 matrix) correctly fail to commute.
4. Claim 4 (type-table application): DOCUMENTARY (quotes two theorem statements from
   Knus–Tignol verbatim) — verify only that the source PDFs actually contain the quoted text
   on the cited pages (arXiv:1409.1718 p.12 type table, Theorem 4.1; p.3 cyclic-composition
   definition).
5. Addendum 1 (disc = 77×square on 3 independent cubics; ℚ(√77) minimal): recompute
   discriminants of μ, the monic model, and the 48-commutant cubic and check each is 77×(a
   perfect square); verify ℚ(√77) is the fixed field of A₃ in the S₃ Galois closure (Galois
   group computation over the cubic's splitting field).
6. Addendum 2 (sextic irreducible over ℚ, F₆=K(√77), meataxe artifact at two primes):
   factor the sextic over ℚ (expect irreducible) and mod primes 10007, 100003 (expect [2,2,2]
   at both); verify `sqrt(77) ∈ F₆` and the 9 named alternatives (`-77,3,7,11,33,21,-3,5,13`)
   are NOT in F₆.
7. Addendum 5/memo 222's ramification count (`n_p ≤ 1` for every p; disc(K(√77))=3⁸·7³·11³):
   this is the one item flagged as needing a number-theory package (pari/sage) the bench
   itself lacked — a verifier with pari/sage should recompute the local Hilbert symbols /
   Frobenius classes at 3, 7, 11 and a sample of unramified primes to confirm the quaternion
   algebra is everywhere-unramified (hence split).

## 6. SUPERSESSION
No INDEX.md row after 224 or owner-register entry was found retracting memo 204. Internally,
Addendum 3 resolves (does not retract) the §6 conflict in B1077's favour; Addendum 5 answers
(does not retract) Addendum 4's open E-splitting question. The base memo's headline (⁶D₄, no
triality over ℚ, B882 refuted) stands through all five addenda.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** for the core CELL 1–3 computation and Addenda 1–3 (cheap, exact,
sympy-reachable, and the genuinely new step beyond an already-banked fact — worth a harvest
arc: it changes B882 from "open/circular" to "refuted" on main). **DISPUTED-status check
recommended, not confirmed**: memo 204 itself flags then resolves an apparent conflict with
B1077/W4 — verifiers should be aware this looked like a contradiction before Addendum 3, but
per the reproduction in Addendum 3 (two independently-built Gram matrices) it is NOT a live
dispute. Addendum 5's ramification computation (pari/sage-dependent) should be separately
re-verified by a seat with that tooling before fully banking the E-split claim.
