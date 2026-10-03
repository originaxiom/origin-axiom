# B1530 — THE INTERIOR EXTENSIONS: at the hyperbolic point, B1515's frame carries one generation (10′ + 5̄′ in one W) on the two silver squares — m135's interior class at κ = 1 and m136's classes at κ = −1, one class on their common double cover; the golden form of the hypothesis fails

cc (the SM-derivation seat), 2026-10-03. Sealed at `1d359734` before `run_a.py` or `census_bc.py` read any outcome
(`PREREGISTRATION.md`, sha-256 `f39d185d…`, SEAL_LEDGER).
- **The run.**
  - The banked identity first: `controls.py`, re-run unchanged at 15:42Z, reproduces `controls.json` in every field but the
    timings (S, K1–K4 all hold; 59 s).
  - `run_a.py` (Part A: m135's eight characters at κ = 1, routes E and N) ran 15:43–15:46Z, 172 s.
  - `census_bc.py` (Parts B and C: the 541 rows, three workers) ran from 15:48:55Z to 22:04Z, 18.7 hours of worker time and
    no error. Its rows on M₂–M₆ reproduce `dry_run_bc.json` in every field, the margins included.
  - `post_run_b.py` (the seal's §4) was written when the census's row for +LLRR, one of its first, showed the κ = −1 hits.
    It read m136's two members at 15:57Z while the census ran on, and wrote its summary from the finished census at 22:07Z.
    `read_out.py` read the sealed predictions at 22:07Z.
- **Verdict: PROVED** (the seal's §9: P2 holds, the routes agreeing).
  - **m135 = −LLRR, κ = 1.** At both non-simple members, u₁ = (0, ½) and u₂ = (½, 0), W₁ at the interior class reads
    (I(W₁), I(Λ²W₁)) = (−1, −1). Routes E (exact over ℚ(ζ₂₄)) and N (60 digits) agree class by class. In B1509's dictionary
    that is N(10′) = N(5̄′) = 1: **one 10′ and one 5̄′ in one W, the cubic anomaly I(Λ²W) − I(W) = 0.** W₂ reads (+1, +1), the
    anti-generation (Lemma M).
  - **m136 = +LLRR, κ = −1 (population B).** Route T reads h¹(ν ⊗ ρ) = 1 at κ = −1 at the same two fibre characters, with
    route G agreeing. So population B is not empty, and P6 fails. Read after the census, as the seal's §4 says
    (`post_run_b.py`, routes N and W), both members are case (a) and read (−1, −1): generation-shaped, as Lemma N allows.
    They read the same exactly (route E, `post_run_e136.py`) and on SnapPy's own presentation and holonomy (route S).
  - **One class on the common double cover** (after the run, exact; §4.4). ±LLRR have the same square. On the bundle of
    (LLRR)², at u₁ and u₂ with ν(t₂) = 1, h¹ = 2 with one interior class, and W₁ there reads (−1, −1). By the transfer this
    one class is m135's κ = 1 interior class and m136's κ = −1 class.
  - **No other κ = −1 member.** Routes T and G read h¹ = 1 at κ = −1 on m136's two characters and h¹ = 0 at the other
    47,331 characters of the 541 rows. Route T's other 24 hits at κ ≠ 1 are at ω and ω², on −LR, M₂ and M₄, and none is a
    fifth power, so they make no member.
  - **Golden: G fails.** Both states are silver. Their monodromies ±L²R² have trace ±6 and eigenvalues ±(1 ± √2)², so up to
    sign each is the square of GENESIS GM5c's silver member L²P. The golden squares ±LR (m004 and m003) carry no
    generation-shaped member. Every κ = 1 member there is simple (sm:B1529), and Part C reads Λ_A ∩ π_A = 0 at their
    characters, so I(Λ²W₁) = bit = 0 (Lemma 8). Population B is empty there, and −LR's eight route-T hits at ω and ω² make
    no member. The same holds on all fourteen golden word states and on M₂–M₆. On m004's levels sm:B1515's two routes read
    it directly; on the other word states it rests on Part C, which is one cohomology route read two ways (§1.3).
- **As sealed: 7 of nine predictions held** (P1–P5, P7 and P8; P6 and G fail). The priors expected 7.4.
- **After the run (disclosed; §4).**
  - Route S reads m135 and m136 on SnapPy's own presentation and polished holonomy, at every character of order dividing 12.
  - `post_run_b.py` reads the κ = −1 members, as the seal's §4 says, in routes N and W.
  - `post_run_e136.py` reads m136 exactly.
  - `post_run_cover.py` reads the two states' common double cover exactly.
  Every reading agrees with the sealed routes.
- **What it is, and what it is not** (§5). One generation's matter content, in one W, at the hyperbolic point of two
  word states, in B1515's frame and B1509's dictionary.
  - It is not three generations.
  - The cusp is not sealed (t1 > 0), so the count comes with continuous spectrum and is main's interior index, not a
    Fredholm index (B1392).
  - m135 is amphichiral and the reading is mirror-even. Its sign is a choice between W₁ and its dual W₂, the member's two
    stacking orders, which carry the generation and the anti-generation (as main's B1466 found at m004's counted point). The index does not make that choice (§5.2).
  - The non-split W₁ is not a stationary vacuum of the bare flat action. Per the audit lane's R76, the potential along the
    extension has its infimum at the split limit, which carries no count. Holding the member needs an end, a source or a
    coupled field (§5.2b).
  - Nothing is claimed off the hyperbolic point, about selection, or about I-26. **0 of 19 stays 0.**
- **Prior work: EXTENDS** (§6). Bart–Scannell, Kapovich and Ballas–Paupert–Will (2026) study the four's parabolic-preserving
  deformations into SO(4, 1); none twists by a character or reads a punctured-torus bundle. B1515's frame exists only in this
  repository.

## 0. What was found

- **Part A, m135's eight characters at κ = 1** (`run_a.json`; routes E and N, class by class):
  - **Two non-simple members**, u₁ = (0, ½) and u₂ = (½, 0). Both are case (a): ν² = 1, so L = 1 and V_η = V = V ⊗ L.
    - h¹(V) = h¹(V_η) = h¹(V ⊗ L) = 2, with one interior class each.
    - W₁ reads (−1, −1) at the interior class c_int, and (0, −1) at every boundary-type class read (c_b, c_b ± c_int,
      c_b + 2c_int).
    - W₂* reads, through the mirror, (+1, +1) at c′_int and (0, +1) at c′_b and c′_b + c′_int.
    - Route N's own interior class, found by its own kernel, also reads (−1, −1).
  - **The mechanism at u₁ and u₂** (route E, exact):
    - S₀ on C has Jordan type (2, 2) at 1, with χ_C = (s − 1)⁴;
    - x ∪ c_int = 0 and x ∪ c_b = 0;
    - c_int lifts to H¹(Λ²W₁), and its restriction μ lies outside Λ_A (dim Λ_A = 2; μ is not a P-coboundary);
    - bit = 0 at c_b.
    That is Lemma A (I(W₁) = −1), Lemma B (I(Λ²W₁) = −[μ ∉ Λ_A] = −1), Lemma C (Jordan type (2, 2), so I(W₁) = 0 at
    boundary-type classes) and Lemma D (I(Λ²W₁) = bit − 1 = −1 there).
  - **Six simple members** read (0, 0), and W₂ reads (0, 0). Their Jordan types are (2) at u = (0, 0) and (½, ½), and (4) at
    the four characters of order 4. x ∪ c = 0 and bit = 0 at each, so Lemma 8 gives (1 − b0 − δ, bit) = (0, 0).
  - **Margins** (route N): the smallest singular value kept is ≥ 7.3 × 10⁻⁵ and the largest dropped is ≤ 2.4 × 10⁻⁵⁸. The
    frames' conjugator X is the kernel of its linear system: relative singular values 1.05 × 10⁻⁶¹ (the kernel) and 0.031
    (the next).
- **Part B, population B** (`census_bc.json`):
  - Route T's characters with h¹(ν ⊗ ρ) ≥ 1 at κ ≠ 1: 26. Two are at κ = −1, m136's (0, ½) and (½, 0). The other 24 are
    at ω and ω², at the order-5 characters of −LR, M₂ and M₄ (eight each).
  - Route G at κ = −1 on every character (47,333: the word states' 46,826 and the levels' 507): h¹ = 0 at 47,331 and
    h¹ = 1 at m136's two. Routes T and G agree at all 51,677 comparisons, and H⁰(F) = 0 at every character.
  - Members (ν⁵ a hit): two, both at κ = −1, both on m136. None at ±i, ω or ω².
- **Part C** (`census_bc.json`): Λ_A ∩ π_A = 0 at all 31,489 characters χ = ν², by rank and by pairing, with
  h¹(Λ²V) = 2 and dimensions (2, 2) at every one.
- **The κ = −1 members** (`post_run_b.json`): two, both on m136, both case (a), both reading (−1, −1) in routes N and W, at
  the basis class (h¹(V_η) = 1, so the sum of the basis is the same class).
  - On m136 the data behind the reading, in route W (Lemma E): W₁ has (h¹(W), h¹(W*), a0, b0, t0, s0) = (1, 2, 0, 1, 1, 1),
    so I = 2 − 1 − 2 + 1 − 1 = −1. Λ²W₁ has (3, 2, 0, 0, 2, 2), so I = 2 − 3 = −1.
- **The golden question.** The owner's hypothesis, that the choice might be golden, was sealed in the form G: every state
  carrying a generation-shaped member is golden. It fails. The members are on the silver squares, and the golden squares
  carry none (§5.4).
- **The experiential question.** GENESIS FK12 holds it under Gate 5-Q, and nothing in this arc bears on it. Per the owner's
  instruction of 2026-10-02 (nothing load-bearing ignored, the experiential question included), that is recorded here.

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The repo sweep (`scripts/checks/prior_work.py`) ran over five
heads in two batches of twelve and ten terms. sm:B1515, sm:B1529, sm:B1509, sm:B1513 and main's B1297/B1440/B1444 bear and
are cited there. In the literature, Bart–Scannell, Monroe (arXiv:2604.22004), Menal-Ferrer–Porti (arXiv:1001.2242) and
Daly (arXiv:2411.04431) were read. Lemmas A–D, the relative second-order obstruction of an interior class of the four, and
any reading of B1515's frame off m004's levels were found nowhere.

**Refreshed at banking** (2026-10-03, after `git fetch --all`; twice, the second at 22:20Z). Since the seal main has moved
from `399b0bc2` to `3f8dc11a` (B1465, B1466, GENESIS v1.8 and v1.9) and the audit lane from `ddd345a8` to `c7aa3a29` (R82).
The other seats are as at the seal. The sweep ran again with sixteen terms, the post-run vocabulary included:
"generation-shaped", "m136", "+LLRR", "LLRRLLRR", "silver square", "common double cover", "both partners",
"parabolic-preserving", "Paupert", "m036", "b++LLRR", "anti-generation", "stacking order", "count is the order",
"abelian cover", "trivial on the cusp". The lines the moved heads added were read for each term.
- **Main's B1466** (sealed at b3565230, banked at 3f8dc11a) bears on §5.2: at m004's counted point the two stacking orders
  count −1 and +1, each other's dual through the inversion, and the two fused count 0. It is cited there.
- **Main's B1465** verifies sm:B1527's Part H by its own route (no count at the complete points of the mirror-broken
  states). It does not read B1515's frame.
- **The audit lane's R82** scopes Chern–Simons critical-value blindness; its "both partners" is the currents of a relation,
  another usage. Nothing on the moved heads reads a twisted four or an extension on m135 or m136.
- **"generation-shaped"** is on every head, and mostly in another frame, F-CI (sm:B1374's Standard-Model frame). There the
  backgrounds are reducible non-split SL(2)_β × ℂ*² connections ρ_χ = [[χ, c], [0, χ⁻¹]], read with main's B1418 index in
  six sectors.
  Generation-shaped backgrounds are banked in that frame:
  - on m004's cyclic covers: M₃ = s961 has 48, M₄ = t12839 has 12,800 and M₆ has 2,160 (sm:B1374, B1375, B1506);
  - B1378's exact three-generation-shaped index from M₆'s deck orbit;
  - on the word state m369 = −LLRLR, 8 (sm:B1518).
  None is at the hyperbolic point of the geometric representation, and none is in B1515's frame, F-HE (§6). In F-HE the
  record has the audit lane's R40 block on m010 (control K2), which has no harmonic background.
- **"m136", "+LLRR" and "b++LLRR"** occur in census tables of amphichiral manifolds, Chern–Simons values and torsions (B152,
  B622's exterior torsion −16 of the silver bundle, B1224), and in main's B1434/B1438/B1439. Those count orbits and couplings
  by slope: (+, LLRR) carries no orbit of three there, and (−, LLRR) carries 144. They also occur in sm:B1523's flexibility
  census (E31's cusp-frame row). None computes a twisted four or an extension on m136.
- **"LLRRLLRR"** occurs only in census and conjugacy-class tables (B1011, B128's probe, B1385, B1439). Nothing reads the bundle
  of (L²R²)² as a cover of ±L²R².
- **"common double cover"** is used of other pairs: m003 and m004, and the orientation double covers (B1208, B1235, B1369,
  B1379).
- **"both partners"** is sm:B1515's lead 3, which this arc answers (§5.1), together with the audit lane's general usage.
- **"anti-generation"** is sm:B1374's and B1389's; **"m036"** occurs only in census tables (B152, B993); **"Paupert"** and
  **"parabolic-preserving"** occur in no head outside this arc and sm:B1529's draft.

**The literature, read at banking** (2026-10-03):
- **S. A. Ballas, J. Paupert, P. Will, "Parabolic-preserving deformations of cusped hyperbolic lattices"**, arXiv:2605.03161
  (2026-05-04). Read from the arXiv PDF; the text is in the seat's scratchpad.
  - Definition 1: ρ is *parabolic-preserving* if it sends parabolics to parabolics (and boundary-elliptics to
    boundary-elliptics), and *strongly* so if it also keeps every parabolic subgroup discrete.
  - Introduction: the SO(4, 1) problem "has been studied by Scannell [Sc], Bart–Scannell [BSc], and Kapovich [Kap] who prove
    some rigidity results"; in the cases they consider, "the deformations into SO(n + 1, 1) are not parabolic-preserving".
  - Proposition 4.4: the bending deformations ρ_θ of the Bianchi groups into SO(4, 1) along the modular surface are not
    strongly parabolic-preserving unless θ = 0 or π.
  - Bearing: actual deformations of untwisted lattices. m135 and m136 are commensurable with PSL(2, ℤ[i]); their twisted
    interior classes (on the double covers ker ν) are infinitesimal parabolic-preserving deformations into SO(4, 1), and at
    m135's, μ ∉ Λ_A says the cusp-held deformation is obstructed at second order (Remark B′, §5.3). That is consistent with
    the paper and is not in it.
- **D. Cooper, D. Long, M. Thistlethwaite, "Computing varieties of representations of hyperbolic 3-manifolds into
  SL(4, ℝ)"**, Experimental Math. 15 (2006), 291–305, §5 (p. 298): *"K. Scannell [Scannell 00] has proved that m036(−3, 2),
  the double cover of Vol3, admits infinitesimal deformations into SO(4, 1); however, numerical evidence suggests that these
  are not integrable."* A closed analogue: an infinitesimal SO(4, 1) deformation on a double cover that does not appear to
  integrate. Here the obstruction is exact and relative to the cusp.
- **Not found in the sources read:** B1515's frame, or any reading of a rank-five extension of a twisted four, on any
  manifold; m136's twisted classes; a common-double-cover account of two quotients' classes.

## 1. The run (as sealed)

### 1.1 The banked identity

`controls.py` was re-run unchanged at 15:42:15Z, before `run_a.py`. Its `controls.json` equals the sealed one in every field
but the four `seconds` entries, and `controls_run.txt` differs only in its timestamp and timings. The re-run's files are kept
in the seat's scratchpad, and the sealed files were restored, so that `ARTIFACT_HASHES.txt` still checks. S, K1, K2, K3
and K4 hold.

### 1.2 Part A: m135's eight characters at κ = 1

| u | h¹ (V, V_η, V ⊗ L) | interior | Jordan (S₀ at 1) | W₁ (E ∣ N) | W₂ (E) | x ∪ c = 0 | μ ∉ Λ_A | bit |
|---|---|---|---|---|---|---|---|---|
| (0, 0) | (1, 1, 1) | 0 | (2) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |
| (0, ½) | (2, 2, 2) | 1 | (2, 2) | c_int (−1, −1) ∣ (−1, −1); c_b (0, −1) ∣ (0, −1) | c′_int (1, 1); c′_b (0, 1) | yes (c_int, c_b) | yes | 0 |
| (¼, ¼) | (1, 1, 1) | 0 | (4) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |
| (¼, ¾) | (1, 1, 1) | 0 | (4) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |
| (½, 0) | (2, 2, 2) | 1 | (2, 2) | c_int (−1, −1) ∣ (−1, −1); c_b (0, −1) ∣ (0, −1) | c′_int (1, 1); c′_b (0, 1) | yes (c_int, c_b) | yes | 0 |
| (½, ½) | (1, 1, 1) | 0 | (2) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |
| (¾, ¼) | (1, 1, 1) | 0 | (4) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |
| (¾, ¾) | (1, 1, 1) | 0 | (4) | (0, 0) ∣ (0, 0) | (0, 0) | yes | — | 0 |

- At u₁ and u₂ the boundary-type classes c_b + c_int, c_b − c_int and c_b + 2c_int read (0, −1) in both routes, as c_b does,
  and W₂* at c′_b + c′_int reads (0, 1).
- Every reading carries B1297's identity, the annihilator identity and Lemma E (route E asserts them; route N's
  `cusp_lib.class_index` checks them).
- Route E's h¹ rows are sm:B1529's exact record (K3).

### 1.3 Parts B and C: the census

`census_bc.json`: sm:B1529's 541 rows (the 536 word states, read as its census read them, and M₂–M₆), at the hyperbolic
point, 60 digits, no error.

| | word states (536) | M₂–M₆ (5) | all (541) |
|---|---|---|---|
| characters u (the D summed) | 46,826 | 507 | 47,333 |
| route T: h¹(ν ⊗ ρ) ≥ 1 at κ = −1 | 2 (m136) | 0 | 2 |
| route T: h¹ ≥ 1 at ±i | 0 | 0 | 0 |
| route T: h¹ ≥ 1 at ω, ω² | 8 (−LR) | 16 (M₂, M₄) | 24 |
| route G at κ = −1: h¹ = 0 ∣ h¹ = 1 | 46,824 ∣ 2 | 507 ∣ 0 | 47,331 ∣ 2 |
| routes T and G compared ∣ disagreeing | 51,116 ∣ 0 | 561 ∣ 0 | 51,677 ∣ 0 |
| H⁰(F) ≠ 0 | 0 | 0 | 0 |
| Part C: characters χ = ν² | 31,234 | 255 | 31,489 |
| Λ_A ∩ π_A ≠ 0, by rank ∣ by pairing | 0 ∣ 0 | 0 ∣ 0 | 0 ∣ 0 |
| (h¹(Λ²V), dim Λ_A, dim π_A) ≠ (2, 2, 2) | 0 | 0 | 0 |

- **Margins.** Route T kept singular values ≥ 1.9 × 10⁻¹⁰ (+L⁷RL²R²) and dropped ≤ 2.0 × 10⁻⁵² (M₄). Route G kept
  ≥ 2.2 × 10⁻¹¹ and dropped ≤ 1.2 × 10⁻⁵⁵. Part C kept ≥ 5.7 × 10⁻⁹ and dropped ≤ 1.2 × 10⁻⁵⁰, and Λ_A and π_A are
  isotropic to 4.0 × 10⁻⁵⁰ (relative). The smallest kept value exceeds the largest dropped one by at least 41 orders of magnitude in each of the three.
- **The levels** reproduce the sealed dry run (`dry_run_bc.json`) in every field, the margins included: population B empty
  at κ = −1, the sixteen hits at ω and ω² on M₂ and M₄, and Λ_A ∩ π_A = 0 at the 255 χ.
- **What the census is, as evidence.** Population B is read by two routes that share no linear algebra (T and G), and they
  agree at all 51,677 comparisons. Part C is one cohomology route (route G's cocycles of Λ²V), read two ways (rank and the
  torus pairing). On m004's levels sm:B1515's routes T and L read the same quantity's consequence, I(Λ²W₁) = 0 at every
  simple member, independently; on the other word states Part C is the one route.

### 1.4 The read-out

`read_out.json`, `read_out_run.txt` (22:07Z, re-run at 22:11Z with the same output): P1, P2, P3, P4, P5, P7 and P8 hold,
P6 and G fail; the verdict string is "PROVED: m135's interior class is generation-shaped (both routes)", and the states
carrying a generation-shaped member are −LLRR and +LLRR (the latter through `post_run_b.json`, as the read-out's rule
says).

## 2. The theorems (as sealed), and what the run supplies

- **Lemma T** (the cusp is shape-blind) was checked exactly on m135's cusp at the seal (S). The census reads on every word
  state's cusp through it.
- **Lemma 5.** No reading at κ ∈ {±i, ω, ω²} is generation-shaped. The census finds no member there at all: route T's 24
  hits at ω and ω² are at characters u′ that are not fifth powers 5u, so no ν has ν⁵ among them.
- **Proposition P** (the populations). At κ = 1 the non-simple members of the word states are exactly m135's two, from
  sm:B1529's census; Part A confirms h¹ = (2, 2, 2) there and (1, 1, 1) at the other six.
- **Lemma 8** at every simple member: (I(W₁), I(Λ²W₁)) = (1 − b0 − δ, bit). Part C reads Λ_A ∩ π_A = 0 at all 31,489 χ,
  so bit = 0 at every simple member of every word state and level, and no simple κ = 1 member is generation-shaped.
- **Lemmas A and B** at m135's interior classes: I(W₁) = −1 and I(Λ²W₁) = −[μ ∉ Λ_A] = −1. The run reads both directly
  (the index of the 5- and 10-dimensional modules) and the mechanism separately (x ∪ c_int = 0, the lift, μ ∉ Λ_A). The two
  agree.
- **Lemmas C and D** at the boundary-type classes: the Jordan type is (2, 2), so I(W₁) = 0, and bit = 0, so
  I(Λ²W₁) = 0 − [μ′ ∉ Λ_A + ℂ e ∧ c_P] = −1 at the four boundary-type classes read, all (0, −1). Lemma C makes
  I(W₁) = 0 at every boundary-type class, so none is generation-shaped. The Λ² value can change at a special class of
  Lemma J's pencil (sm:B1532). sm:B1534's controls (K4, before its seal) find one such class on each member, a rational s
  outside the four read; its reading belongs to sm:B1534.
- **Lemma M** (the mirror): W₂ reads −W₁ at corresponding classes at all eight characters (and on m136 at κ = −1,
  `post_run_e136.py`).
- **Lemma N** at κ = −1: a generation-shaped member is case (a) and reads (−1, −1). m136's two members are case (a), with
  x ∪ c = 0 (exact), and read (−1, −1).

## 3. The predictions

| | prediction | prior | as read |
|---|---|---|---|
| P1 | Lemma A: I(W₁) = −1 at c_int, both members, both routes | 97% | **holds** |
| P2 | (I(W₁), I(Λ²W₁)) = (−1, −1) at c_int, both routes, both members | 55% | **holds** |
| P3 | Lemmas C and D: one I(W₁) value at the boundary-type classes, equal to [Jordan (3, 1)]; none generation-shaped | 90% | **holds** (Jordan (2, 2), I(W₁) = 0, (0, −1)) |
| P4 | m135's six simple members read (0, 0) | 95% | **holds** |
| P5 | W₂ reads −W₁ at corresponding classes, all eight characters | 97% | **holds** |
| P6 | population B at κ = −1 empty on every word state and level | 75% | **fails**: m136's two characters, and no other |
| P7 | Λ_A ∩ π_A = 0 at every χ = ν², by rank and by pairing | 97% | **holds** (31,489 χ; dimensions (2, 2) throughout) |
| P8 | x ∪ c_int = 0 and c_int lifts, both members | 97% | **holds** |
| G | every state carrying a generation-shaped member is golden | 40% | **fails**: m135 and m136 are silver |

Seven of nine held; the priors summed to 7.43.

## 4. Post-run checks (written after the run; disclosed)

Each was written after `run_a.py` had read m135, and the last three after the census had found m136's members. None is a
sealed quantity, and none changes a sealed reading.

### 4.1 Route S: SnapPy's presentation and holonomy (`post_run_s.py`)

Routes E and N share two inputs: the group (`family_lib.word_group`, the bundle presentation ⟨a, b, t⟩, with its cusp words)
and the hyperbolic point (both on that presentation). Routes T, G, N and W of Part B share the same two. A slip in either
would reach every route alike. Route S takes both from SnapPy 3.3.2 instead.
- **The manifolds.** `b+-LLRR` and `b++LLRR`, SnapPy's names for −LLRR and +LLRR. identify() returns m135 and m136; both have
  all tetrahedra positively oriented and volume 3.66386 (the Whitehead link's). SnapPy's simplified presentations have three
  generators and two relators. The peripheral curves are read from SnapPy, and the polished holonomy at 256 bits. SnapPy's
  `lift_to_SL2C` raised a TypeError on these bundles (H₁ has torsion), so PSL(2, ℂ) was taken; the four is blind to the
  sign.
- **The residuals.** The relators hold on the four to 6 × 10⁻⁵⁹ and the cusp's generators commute to 4 × 10⁻⁵⁹.
- **κ without the fibration.** The fibre's boundary is the peripheral class that dies in H₁(M; ℤ) (found by solving over
  ℤ), and ν is 1 on it. So ν(P) = ⟨κ⟩, and the order of ν(P) gives κ up to inversion.
- **The characters.** Every ν: π₁ → μ₁₂: 96 on m135 and 48 on m136.
- **m135.** The eight κ = 1 characters reproduce `run_a.json` as a multiset, in (h¹, interior dimension, the reading at the
  interior class, every reading). That is two members with (2, 1) reading (−1, −1) at the interior class and (0, −1) at
  boundary-type classes, and six with (1, 0) reading (0, 0). No character at κ of order 2, 3 or 4 has h¹ ≥ 1, as route T
  finds.
- **m136.** At κ = −1 there are two characters with h¹ = 1, as route T finds; each reads (−1, −1) at its class, as
  `post_run_b.py` finds. The four κ = 1 characters are simple and read (0, 0).
- A first pass on m135 at μ₄ (32 characters; `post_run_s_mLLRR_mu4.json`) agreed and is kept.

### 4.2 The κ = −1 members (`post_run_b.py`; the seal's §4)

Every κ = −1 member, ν = (u, −1) with ν⁵ among route T's hits, read in routes N and W at every class of an orthonormal basis
of H¹(V_η) and at the sum of the basis.
- Two members, both on m136, u = (0, ½) and (½, 0); both case (a), every class interior (the cusp acyclic), both reading
  (−1, −1) in both routes.
- On m136: h¹(V_η) = 1 at each member. Route W's data are in §0.

### 4.3 m136 exactly (`post_run_e136.py`)

m136's holonomy was read exactly, by sm:B1529's reader (`post_run_exact_m135.exact_sl2`, its sign set to +). In the frame
where the cusp's fixed point and its images under a and b go to 0, 1 and ∞:

  a = [[0, (−1 + 7i)/50], [1, (−3 + i)/5]],  b = [[1, (−27 − 11i)/50], [1, (−2 − i)/5]],  t = [[1, (1 + 3i)/5], [0, 1]]

in PGL(2, ℚ(i)). The relators hold exactly on the four.
- At κ = 1 the four base points are simple: h¹ = (1, 1, 1), no interior class, W₁ and W₂ (0, 0), x ∪ c = 0.
- At κ = −1, u = (0, 0) and (½, ½) carry nothing (h¹ = 0).
- u = (0, ½) and (½, 0) have h¹ = (1, 1, 1), every class interior. There W₁ reads **(−1, −1)** and W₂ (+1, +1), exactly, with
  x ∪ c = 0 (Lemma N: I(W₁) = −[x ∪ c = 0] = −1).

### 4.4 The common double cover (`post_run_cover.py`)

−LLRR and +LLRR have monodromies −φ and +φ, φ = L²R². Their squares agree, so the bundle of φ², Γ₂ = ⟨a, b, t₂⟩, is the
level 2 of both states (GENESIS §3: the n-fold level of (ε, w) has monodromy (εw)ⁿ). By Mostow rigidity it carries one
hyperbolic structure. At u₁ both members have ν(a) = 1, ν(b) = −1 and ν(t) = −1: on m135 κ = ν(abt) = 1, and on m136
κ = ν(t) = −1.
- **Read exactly on Γ₂ = +LLRRLLRR**, the silver level 2 (not a census state: (LLRR)² is a proper power), with m136's exact
  four and t₂ ↦ t²:
  - at u₁ and u₂ with ν(t₂) = 1: h¹ = 2 with one interior class, and W₁ reads **(−1, −1)** at it and (0, −1) at a
    boundary-type class;
  - with ν(t₂) = −1: h¹ = 0.
- **The transfer.** H¹(Γ₂; π*V) = H¹(Γ; V) ⊕ H¹(Γ; V ⊗ ε), with ε the deck character.
  - From m136: the κ = −1 member (one interior class) plus the simple κ = 1 character at u₁ (one boundary-type class) give
    2, with one interior class.
  - From m135: its κ = 1 member (2, one interior) plus nothing at κ = −1 give 2, with one interior class.
  - m135's member must restrict to ν(t₂) = 1, since ν(t₂) = −1 carries nothing.
- So one interior class on the silver level 2 descends to both states. It reads (−1, −1) there, on m135 at κ = 1 and on
  m136 at κ = −1. The index is not doubled on the cover: the class is one-dimensional upstairs and downstairs.

## 5. What the reading means

### 5.1 The count, in the sealed frame and dictionary

At m135's interior class, W₁ = [[V, c_int], [0, 1]] is an exact representation, not an infinitesimal one: the off-diagonal
block is a cocycle. In B1509's dictionary (GENESIS's frame F-HE: E₈ ⊃ (SU(5) × SU(5)′)/ℤ₅ on the harmonic convex-projective
vacuum), N(10′) = −I(W) = 1 and N(5̄′) = −I(Λ²W) = 1, and the anomaly I(Λ²W) − I(W) is 0.

This answers sm:B1515's lead 3 ("One W with both partners") at m135 and m136. Read with the record:
- sm:B1509 put the 10′ and the 5̄′ on different backgrounds. m004's projective family carries the 10′ but, for q ≠ 1, no 5̄′.
  The audit lane's R40 block on m010 carries an anomaly-free 10 + 5̄ but has no harmonic background (F01).
- sm:B1515 found the 5̄′ can live only at q = 1, the hyperbolic point, through interior classes. Through level 6 on m004 its
  members carried the wrong pairing, a 10̄′ with a 5̄′.
- Here both partners sit in one W at the hyperbolic point of the state's own projective family, the harmonic frame's q = 1
  point, with the anomaly cancelled.

The caveats are the seal's (§9), unchanged:
- The cusp is not sealed (t1 > 0). The count comes with continuous spectrum, and the twisted operator is not Fredholm
  (B1392).
- The count is main's interior index. Proposition E's ranges are not used, and no end condition is chosen to rescue a count
  (sL-8's rule, B1392:115).
- In case (a), L = 1, so W₁ is an affine extension of V by the trivial line, and W₁* has an invariant vector (b0 = 1).

### 5.2 Mirror-even; the sign is a choice between W₁ and its dual

- **The geometric mirror does not change the count.** m135 is amphichiral (sm:B1224 and B1226). The record's theorem
  (B1224, generalised in B1227) is that a mirror-odd invariant obeys 2·I = 0 in its value group, so a ℤ-valued one vanishes
  on an amphichiral state. I(W₁) = −1 there, so this count is mirror-even.
  - That is what its definition gives. The index is a group-cohomology invariant of (Γ, P, W). The reversing isometry acts on
    (Γ, P), and on the set of members, without changing any index. u₁ and u₂ read alike.
  - GENESIS FK9 says it in general: "The geometric mirror does not change a count at all; dualising does" (main B1297,
    B868, B871).
- **Dualising does.** By Lemma M, W₂ at c′ is the dual of W₁ at β⁻¹c′, interior class to interior class. W₂ reads (+1, +1),
  one 10̄′ and one 5′.
  - The two are the member's two stacking orders, each other's dual.
  - Each is generation-shaped, since I(W) = I(Λ²W) ≠ 0 is unchanged by W ↦ W*. One carries the generation and the other the
    anti-generation.
  - Non-split extensions are where this can happen: the vector-like theorem holds for the rank-one twist only, and
    non-semisimple V and V* evade it (sm:B1393's scope; R27, B1418, sm:B1374).
- **So the state supplies a generation's shape, not its sign.** The shape is ∣N(10′)∣ = ∣N(5̄′)∣ = 1 with the anomaly
  cancelled. The sign, W₁ or W₁*, is a ℤ/2 choice the index does not make.
  - That is where sm:B713 put "which chirality": a non-canonical ℤ/2 bit, the observer's.
  - It is also how the wall "chirality not self-supplied" (sm:B1234's table, from B713 and B760; GENESIS's archimedean line)
    reads here. The sign is not supplied; the shape is.
  - This arc reads no quantity that selects the order.
- **Main's B1466 found the same at another point.** At m004's counted point q₀ = 17 ± 12√2, μ = −1, the two stacking orders
  count −1 and +1 and are each other's dual seen through the inversion; the mixed direction is unobstructed and leads to an
  irreducible flat module, the two fused, which counts 0: "the count is the order, and the count is a bit". At m135 the
  duality is direct (V ≅ V* through β), with no inversion. Whether m135's two orders fuse the same way was not read here.

### 5.2b Is the member a vacuum? The record's own dynamics says: not in the bare model

This is load-bearing for any physical reading of §5.1, and it comes from the record, not from this run.
- **Main's B1455 and sm:B1520** ran the selection-rule deciding test on m004's harmonic family: is there a mirror-symmetric
  potential whose minima are not mirror-symmetric? The answer was negative. Every vacuum of that family is fixed by a symmetry
  under which the count is odd, so the count is zero there.
- **The audit lane's R76** (`FLAT_VACUUM.md`, conditional authored analysis with exact finite controls) is about a non-split
  extension of exactly this kind: a cocycle that is zero on the cusp generators and non-split globally.
  - In the supplied bare action, a smooth stationary flat point with finite energy on a complete boundaryless base must be
    harmonic (R76). The lane's F01 finite-energy splitting obstruction "still applies to a smooth complete source-free
    nonsplit W" (`COEFFICIENT_PARENT_PROOF.md`, R40's rank-five W). R41 writes its mechanism as a flag balance,
    ∫ tr(ξ S) = 4 ∫ |η|² with η the extension block: with no source, η = 0. So a non-split W₁ is not such a point. This is
    the lane's theorem in its model, quoted here, not re-derived for m135's W₁.
  - Along the extension scaled by t > 0, the potential is a t² + c t⁴ with a ≥ 0 and c > 0. Its infimum is at the split limit,
    which is at infinite target distance.
  - So in the bare flat model the split configuration V ⊕ L, which carries no count, is where the energy goes. The non-split
    W₁ that carries the generation is not held.
- **What R76 leaves open** is exactly where a non-split member could be held: non-flat, coupled-field, sourced, physical-end and
  singular models. R76 names the constructive duty, a parent source, core or end action yielding the compact current under its
  own variations. The audit lane's R81 (`DIRICHLET_ADMISSION.md`) admits a unique harmonic metric for R75's non-split
  rank-five W on every smooth compact cusp truncation with supplied boundary metric (Wu–Zhang, Prop. 3.3). That is a
  zero-potential stationary background of the bare action, held by its boundary: the outward projector flux must be
  strictly negative, 2 flux = −5 ∫ |η|². Its boundary data are "a supplied input, not yet a physically generated law".
- **So:** B1530 reads a generation in the frame's index, on a configuration the bare flat action does not select. Whether
  an end or a source holds it is the open physical question. It is registered with the next questions (§7).

### 5.3 What μ ∉ Λ_A says about the classes (Remark B′; an interpretation, not used by the reading)

On the double cover ker ν, c_int is a parabolic-preserving infinitesimal deformation into SO(4, 1) (Bart–Scannell §2.1;
sm:B1529). μ is its relative cup square, the second-order obstruction with the cusp held. μ ∉ Λ_A, so c_int is not tangent to
a curve of representations into SO(4, 1) that holds the cusp's image up to conjugacy. In particular it is not a bending
along a closed embedded totally geodesic surface of ker ν (Bart–Scannell §2.2). The absolute obstruction vanishes:
H²(M, ∂M; Λ²V) → H²(M; Λ²V) is zero. This answers the seal's §10 question on the classes' geometric origin in the negative
for bending. Compare Cooper–Long–Thistlethwaite's report of Scannell's m036(−3, 2) (seen first, above).

### 5.4 Silver, not golden

- **The metallic squares.** GENESIS GM5c's swap-extended metallic family LᵐP has squares LᵐRᵐ.
  - m = 1: ±LR, m004 and m003, golden.
  - m = 2: ±L²R², m136 and m135, silver.
  - m = 3 to 6: ±L³R³ (trace ±11), ±L⁴R⁴ (±18, a golden trace: (LR)³ has it too), ±L⁵R⁵ (±27) and ±L⁶R⁶ (±38). On all
    eight, every κ = 1 member is simple (sm:B1529), route T has no hit at any κ ≠ 1, and Part C is clean. None carries a
    generation-shaped member.
- Through length 12 the generation-shaped members found are on the silver squares and nowhere else, and one class on the
  silver square's φ²-bundle accounts for all of them (§4.4). "Nowhere else" is read in B1515's frame at the hyperbolic
  point, on the word states to length 12 and M₁–M₆. It rests on sm:B1529's census for the non-simple κ = 1 members, on
  routes T and G for population B, and, for the simple members off m004's levels, on Part C's one route (§1.3).
- G, the sealed golden form of the owner's hypothesis, fails. Read on the record's terms: the golden squares carry no
  generation-shaped member in B1515's frame at the hyperbolic point, and the silver ones do.

## 6. Prior work and standing

**EXTENDS.** The parabolic-preserving (cuspidal) cohomology of the four is Scannell's, Bart–Scannell's and Kapovich's
object, and Ballas–Paupert–Will (2026) study parabolic-preserving deformations of cusped lattices into SO(4, 1). This arc
reads it twisted by characters on punctured-torus bundles, inside B1515's rank-five frame, and reads the second-order
obstruction at m135's interior class. None of that was found in the sources read. The frame, the dictionary (sm:B1509) and
the index (main's B1297) are this repository's.

**Within the record** (GENESIS §5's frames).
- **F-CI**, the class-index frame (main's B1418 index on reducible non-split SL(2)_β × ℂ*² doublet modules, read sector by
  sector), already has generation-shaped backgrounds:
  - on m004's covers (sm:B1374, B1375, B1378, B1506);
  - on 95 word states at their own levels (main B1439), m369 among them (sm:B1518).
  Those are reducible connections, not the hyperbolic holonomy.
- **F-HE**, this frame, had an anomaly-free 10 + 5̄ only on the audit lane's R40 block on m010, which has no harmonic background
  (F01; this arc's control K2). Its counts at the hyperbolic point of m004's levels had the wrong pairing (sm:B1515).
- So within F-HE, m135's and m136's members are the first generation-shaped ones on a harmonic background: the twisted
  geometric representation itself, extended at the hyperbolic point. The claim is scoped to F-HE and to that background.

## 7. What this arc does not decide (the next questions)

- **Three.** The member carries one generation, and on the silver level 2 the class did not multiply (§4.4). Two routes to
  three in one W, each a separate sealed question:
  - **The silver tower.** B1515's frame on the levels of ±L²R², the bundles of (L²R²)ⁿ to n = 6, are in X_gen and in no
    census so far. By the transfer, members pulled back from a state do not multiply: the twisted summands at κ ≠ ±1 carry
    nothing there. New members can come only from characters that φ fixes at level n and not before. A deck orbit of three
    such members is the shape of sm:B1378's triplet, in F-CI. In a rank-five W it is three vacua, not one (sm:B1506's "one
    background, one count").
  - **Abelian covers.** These are commensurability moves of X_gen, with several cusps. For a finite regular abelian cover
    with deck characters B, the index of a pulled-back module is a sum over B (Shapiro and Mackey; sm:B1532's Lemma S):
    (I(p*W), I(Λ²p*W)) = Σ_{χ∈B} (I(W ⊗ χ), I(Λ²W ⊗ χ)). A character that leaves the cusp acyclic adds 0 (the argument of
    sm:B1532's Lemma Z). So:
    - at m135's κ = 1 members, where W₁|_P is unipotent, only the eight characters trivial on P can add anything;
    - at m136's κ = −1 members, where V|_P has the eigenvalue −1 and L|_P = 1, only the eight characters with χ(t′) = ±1
      can. The common double cover's deck character is one of them, and it adds (0, 0) (§4.4).

    Every abelian cover's count at the pulled-back members is therefore a sum over a subgroup of one group of order eight.
    Finitely many exact readings decide all of them, at every class. They are sealed as their own arc before they are
    computed. sm:B1532 asks the same question on m004's levels M₂–M₆.
  - **A bound withdrawn.** An earlier draft of the paragraph above bounded the count on the covers trivial on P by two
    generations. Its argument bounded one sign only: W₁'s generations at the interior class (I(p*W₁) ≥ −2). It said nothing
    of the other sign, which is W₂'s generations, nor of the boundary-type classes. It is withdrawn (ERROR_LEDGER).
    sm:B1532's seal quotes that bound (its §0 and §10); its FINDINGS will carry this correction.
- **Off the hyperbolic point.** sL-10 item 10 (b): the coincidence loci near ρ_hyp (sm:B1529 §9). Whether the
  generation-shaped reading survives a deformation is open.
- **The couplings.** The up-type coupling 10′·10′·5′_H (sm:B1513's relative triple product) at the member's W, and whether
  the Higgs bulk Λ²V supplies a 5′_H there.
- **The choice of order, and what holds the member.** What, if anything, selects W₁ over W₂ at a member. Before that, what
  holds a non-split member at all: R76's bare model does not (§5.2b), so the question is an end, a source or a coupled
  field (R76's duty; R81's compact-boundary admission).
- **Beyond length 12 and level 6** (sm:B1515 lead 2).

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt` (sealed files; `sha256sum -c` passes).
- `verification/exact_lib.py`, `exact_states.py`, `route_n.py`, `census_lib.py` (sealed libraries).
- `verification/controls.py`, `controls.json`, `controls_run.txt` (sealed; re-run before reading, §1.1).
- `verification/run_a.py` → `run_a.json`, `run_a_log.txt` (Part A, as sealed).
- `verification/census_bc.py` → `census_bc.json` (Parts B and C, as sealed; `census_bc.jsonl` is the working file, not
  tracked).
- `verification/read_out.py` → `read_out.json`, `read_out_run.txt`.
- Post-run (disclosed, §4): `post_run_s.py` → `post_run_s_mLLRR.json`, `post_run_s_pLLRR.json` and their logs, and the μ₄ pass
  `post_run_s_mLLRR_mu4.json`; `post_run_b.py` → `post_run_b.json`; `post_run_e136.py` → `post_run_e136.json`;
  `post_run_cover.py` → `post_run_cover.json`.
- For main's blind route: `verification/export_members.py` → `members_for_main.json` (the members, no readings; pushed at
  `56f46d4f`).
- `arc_verdict.json`; the lock `tests/test_b1530_the_interior_extensions.py`.
