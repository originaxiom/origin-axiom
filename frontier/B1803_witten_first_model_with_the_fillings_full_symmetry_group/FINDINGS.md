# B1803 — WITTEN'S FIRST MODEL WITH THE FILLINGS' FULL SYMMETRY GROUP (P-409; DATA-FREE): ON A HYPERBOLIC m004(p/q), p EVEN, F′ = Sym(Q) ≅ ℤ/2 × ℤ/2 FIXES EXACTLY FOUR POINTS. RELATIVE TO ONE OF THEM THEY CARRY ALL FOUR CHARACTERS WHEN p ≡ 2 mod 4 AND TWO, TWICE EACH, WHEN p ≡ 0 mod 4. WITTEN'S FIRST MODEL NEEDS EIGHT MULTIPLETS AT F′-FIXED POINTS, SO IT CANNOT BE BUILT AT DISTINCT POINTS. WITH COINCIDENT POINTS, WHICH HIS § 3 ALLOWS, IT IS REALISABLE, WITH AT LEAST 4 (p ≡ 0 mod 4) OR 7 (p ≡ 2 mod 4) MULTIPLETS AT ONE POINT; WHETHER SUCH LOCAL MODELS EXIST IS OPEN

**Verdict: PROVED.**
- **What is proved:** the topology (Claims A–C) and the placement census (§ 4). Each has two independent routes on main
  and at the referee.
- **What is open:** realising Witten's first model with F′ = Sym(Q). It needs coincident multiplets, whose G₂ local models
  are not known here (P-416).
- **Scope:** data-free; none of the 19. cc (main), 2026-10-28, P-409. Corrected before landing at its hostile referee
  (§ 6).

**0 of 19.**

## 1. The question

- **B1802.** On every even filling, each strong inversion h₁, h₂ has two fixed circles, with lifts differing by
  W = diag(1, 1, 1, −1, −1). The period P has two fixed circles too, but its lifts differ by W only when p ≡ 2 mod 4.
- **Witten's caveat.** His first model fails at n = 2 with ℤ/2 alone.
- **The referee's enumeration.** F′ = ℤ/2 × ℤ/2 admits 6 abstract solutions of his (2.1)–(2.9).
- **The question here (P-409).** Can one be realised with the fields at F′'s fixed loci?

## 2. Witten's requirement, at source (hep-ph/0201018)

- **First model.** All 10's transform "with a common σ", and the 5̄'s likewise with τ.
- **Location.** The chiral superfields sit "at points on S1 or S2, so as to preserve the F′ symmetry".
- **F′ orbits.** Footnote 4: superfields on a non-trivial F′ orbit are "a generalization", which he omits.
- **Coincident points.** His § 3 (3): Yukawas come from membrane instantons "unless some of the points on Q that support
  chiral superfields coincide". For the top mass, "some singularities are nearby or perhaps even coincident".
- **The scope here.** Witten's first model: common σ and τ, with every multiplet at an F′-fixed point. Coincident points
  are allowed, as he allows them.
- **A note on "one multiplet per point".** That describes a single local conical singularity (Acharya–Witten). It is not a
  rule of Witten's model, and it is not assumed here.

## 3. The topology (Q hyperbolic, p even; the exceptional slopes 0, ±2, ±4 excluded)

**Claim A: Fix(F′) = {e₊, e₋, c₁, c₂}.**
- **The common fixed set in S³** is two points, by two routes.
  - Borel's formula for a Klein four-group acting on S³ whose three involutions each fix a circle: 3 − r = 3(1 − r), so
    r = 0 and the common fixed set is two points.
  - Alternatively: by the orbifold theorem the action is conjugate to diag(1, 1, −1, −1), diag(1, −1, 1, −1),
    diag(1, −1, −1, 1) in SO(4). The other class contains −I, which is free.
- **They lie off the knot.** Both points lie on P's axis, which is disjoint from the knot. So they lie in the exterior E.
- **The strong inversions separate e₊ from e₋.** In Q each of h₁'s two circles is one arc of E plus one arc of the
  filling solid torus V. In V the extension is (z, θ) ↦ (z̄, −θ), and its fixed arcs each cross V's core once.
- **The period fixes the core.**
  - P translates the cusp torus by λ/2. This is B1802's r5 derivation: the lift of K′'s longitude is K's Seifert longitude,
    and lk(K′, A′) = 3 is odd.
  - For p even, q is odd, so s/2 ≡ λ/2 mod the lattice. P therefore acts on V as (z, θ) ↦ (−z, θ).
  - The fixed sets in V meet only at the core points c₁ = (0, 0) and c₂ = (0, π).
  - The extension over V is unique up to conjugacy: a finite group action on a solid torus is standard.
- **Each h-circle carries two common fixed points.** Check (c1): on the four 2-component branch links (L11n132, L13n4507,
  L13n4800, L14n24777), Sym(S³ ∖ L) = ℤ/2. Its non-trivial element (P's image) has cusp maps (−I, −I) and extends to S³.
  So its axis meets each component twice.
  - Each h-circle holds one core point, so it holds one of e±. Hence e₊ and e₋ lie on different circles of h₁, and of h₂.
- **For p odd,** P acts freely on V, and Fix(F′) = {e±}.

**Claim B: the lift is an honest F′ action.**
- Take the lifts of h₁ and h₂ to the order-2 bundle (the connected double cover of the order-2 character) that fix the
  fibre over e₊.
- Their commutator and their squares are deck transformations with fixed points, hence trivial.
- So F′ lifts honestly, with the trivial character at e₊.
- Other lifts differ from this one by homomorphisms F′ → S(U(3) × U(2)), which leaves every selection rule unchanged.

**Claim C: the characters κ_x of (h₁, h₂, P) at the four points, relative to e₊.**

| point | κ |
|---|---|
| e₊ | (0, 0, 0) |
| e₋ | (1, 1, 0) |
| c₁ | (0, ε, ε) |
| c₂ | (1, 1 + ε, ε) |

- **The labelling.** c₁ is the core point on e₊'s circle of h₁.
- **ε = p/2 mod 2, proved.**
  - Q/P = L6a2 [(2, 0), (p, 2q)].
  - In homology λ′ = 3μ_A (lk 3), so H₁^orb = ℤ/2⟨μ_A⟩ × ℤ/p⟨μ′⟩.
  - The covering class ψ has ψ(μ_A) = ψ(m_C) = 1 and ψ(μ′) = 0. Any ρ restricting to the order-2 character has
    ρ(μ′) = 1, and its value a = ρ(μ_A) is free.
  - The core's cone generator is m_C = (p/2)μ′ + qλ′ = (p/2)μ′ + 3qμ_A.
  - So ρ(m_A) + ρ(m_C) = a + p/2 + 3qa ≡ p/2 mod 2, since q is odd.
- **ε, checked.**
  - c2: the relative lift on 75 even fillings, with no mismatch.
  - The referee's b2, on a separate code path (SnapPy's covers of Q/P): the manifold double covers of Q/P number
    1 + [4 ∣ p] on 150 fillings, with no mismatch, and on 26 of them exactly one is isometric to Q.
  - The referee's b3 never computes a lift. |Q/P| is the (p/2)/q surgery L6a2[(1, 0), (p/2, q)], with H₁ = ℤ/(p/2), and
    the singular graph of Q/F′ is two bigons exactly when 4 ∣ p. That reproduces the table.
- **The table, by residue.**
  - p ≡ 2 mod 4: all four characters {000, 110, 011, 101}, one point each.
  - p ≡ 0 mod 4: {000, 110}, two points each.
- **Sym(Q) = F′ is certified** on 124 hyperbolic even fillings: 68 by SnapPy directly, and 56 more where the filling's
  core is the unique shortest geodesic (the referee's b1 and b1b). There is no counterexample among the 240 fillings
  tried. On main's rerun b1b certifies 59: it gives each filling 60 s, so its timeouts depend on the machine (9 at the
  referee, 6 on main), and the three extra fillings all certify. Both logs are kept (`b1b_run.txt`,
  `b1b_run_main_rerun.txt`).

## 4. Witten's first model with F′ = Sym(Q): the placement census (the referee's b4; checked by hand on main)

- **The count is the obstruction.**
  - V (the 5), Ṽ, three 10's and three 5̄'s make eight multiplets. There are four F′-fixed points.
  - So no placement at distinct points exists, before any character is used.
- **The characters set how many must coincide.**
  - V, the three 10's and the three 5̄'s need points of one class: matter at a point of another class is split by W
    (Q against u^c and e^c, L against d^c), which breaks the common σ and τ.
  - Ṽ needs a point of class κ_V + w, with w one of the solutions' twists.
  - The abstract solutions are two per w. Realised: p ≡ 2 mod 4 gives all three w (6 solutions); p ≡ 0 mod 4 gives
    w = 110 only (2 solutions). The solutions' S₃ symmetry is not induced by Sym(Q).

| residue | placements, distinct points | placements, coincidence allowed | least multiplets at one point |
|---|---|---|---|
| p ≡ 2 mod 4 | 0 | 12 | 7 (V and all six matter multiplets at e₊) |
| p ≡ 0 mod 4 | 0 | 512 | 4 (V and three at e₊, three at c₁) |

  - If V may sit at a split point: 24 solutions, and the least stacking is 6 versus 4.
- **F′ = ℤ/2 alone:** h₁, h₂, or P when p ≡ 2 mod 4.
  - The only solution without (2.8) has σ = 0. It needs a matter parity from elsewhere.
  - One such source is a symmetry of the G₂ space X that acts trivially on Q. With it, w = (1, 0) solutions exist with
    the matter at distinct points.
  - Another is the gauge group's centre (P-414).
- **P on the ℤ/6 line** (B1802 (f)):
  - the strong inversions do not preserve it, so the full F′ exists only on the order-2 line;
  - P twists by W³, of order 2, so Witten's n = 2 caveat applies;
  - for p ≡ 0 mod 4, P alone gives no split at all.
- **What remains open:**
  - local G₂ models with 4–7 coincident multiplets (P-416);
  - non-trivial F′ orbits, Witten's omitted generalisation;
  - his second model, which he says has trouble giving masses to all down quarks and charged leptons.

## 5. What it means

- **What the figure-eight's even fillings supply:**
  - Witten's doublet–triplet topology (B1802);
  - a rigid four-point structure of the full symmetry group, whose characters are fixed by p mod 4.
- **What they do not supply:** room for the first model at distinct points. The model needs coincident multiplets, and the
  less stacked case is p ≡ 0 mod 4.
- **No input removed. 0 of 19.**

## 6. The referee (hostile, read-only; `audit/referee_b1803/`, scripts kept in `verification/referee/`)

**Verified independently:**
- Claim A, by Borel's formula and the solid-torus extensions;
- Claim B;
- Claim C, by two routes that differ from main's: b2 (covers, 150 fillings) and b3 (the underlying space and the singular
  graph);
- c1–c3, which rerun byte-identically; and on main b1–b4 regenerate identically (warnings aside), except b1b's
  time-limited count (§ 3);
- r8's conditions, against Witten's (2.1)–(2.9) at source.

**One blocking finding, applied.**
- The draft's NEGATIVE ("cannot be realised; the obstruction is a count of fixed points") rested on one multiplet per
  point.
- Witten allows coincident points. With them, placements exist (b4).
- The verdict is now PROVED for the topology and the census, with the realisation OPEN (P-416).

**Corrections applied:**
- the obstruction is 8 > 4, before any character;
- hyperbolicity stated, and the certification counts given;
- § 1's statement about P's lifts;
- the solution count per residue (6 against 2);
- Witten's footnote 4 and § 3 (3);
- the ℤ/6 clause;
- the ε proof's steps;
- the "3 = 1 + 2" remark deleted (it had no forcing behind it);
- the matter parity from a symmetry of X named;
- κ in place of the reused χ;
- Witten's own caveat on his second model.

## Seen first

`VERDICT topic-sweep /Klein four|Z/2 ?x ?Z/2|ℤ/2 ?× ?ℤ/2|common fixed point|Witten.{0,30}(first model|doublet)|matter parity|P-409|equivariant (bundle|lift)|strong(ly)? invert/ (full text): 26 of 1549 arcs on main match (NEGATIVE 5, PROVED 21); 3 register rows match (DONE 1, QUEUED 2)`.

**Bearing on it:**
- B1802 and its referee (r5, r7, r8);
- B1297 (the period) and B1462 (D₄; the strong inversion);
- B1104 (Isom(m004) = D₄);
- B561 (the geometric point's symmetry is Klein four);
- B1801;
- P-408.

None treats F′'s fixed points or their characters.

**Literature:**
- Witten (hep-ph/0201018) § 2.1, § 2.2 (footnote 4) and § 3;
- Acharya–Witten;
- Montesinos (1975);
- Borel's fixed-point formula;
- the orbifold theorem (Boileau–Leeb–Porti; Dinkelbach–Leeb);
- P. A. Smith.

## Files

- `verification/c1_branch_link_symmetry.py`, `c2_period_relative_lift.py` and `c3_solutions_by_w.py`, with their
  `*_run.txt`.
- `verification/referee/`:
  - `b1_symmetry_groups_even_fillings.py`, `b1b_core_is_shortest.py`, `b2_period_manifold_covers.py`,
    `b3_underlying_space_and_character_table.py` and `b4_witten_first_model_placements.py`, with their runs.
  - The paper's text and the referee's line-referenced excerpts stay in the audit room, not in the repository.

The lock: `tests/test_b1803_witten_first_model_with_the_fillings_full_symmetry_group.py`.
