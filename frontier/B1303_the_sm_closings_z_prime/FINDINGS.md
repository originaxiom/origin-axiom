# B1303 — THE SM CLOSING'S Z′: the tree-level vacuum of the closing that has the Standard-Model group leaves SM × U(1)_Z′ (rank 5) — the Z′ family-non-universal, anomaly-free (its only anomaly is the family torus's, cancelled by the 27̄s), untouchable by the superpotential at any order — and its first testable consequence is a FORK the record cannot resolve: kaon mixing puts it at 10²–10³ TeV·g₂⁻¹ if the VEV'd generation is a light family, at a few TeV if it is the third; B1140 and fc R49 were both right about different embeddings; chat1's "absent" χ-determinant is B1103

**Date:** 2026-09-08 · **Seat:** cc (main) · **MASTERPLAN v3.1 Phase 1, fourth harvest arc** · **DESIGN sealed** `9f44f4c3…` (`DESIGN.sha256`)
before any of main's computations; every pre-registered question below is graded against its written prediction · **Status:**
**VERIFIED** (sm:B1283, sm:B1300, sm:B1301 — each re-run in the pinned worktree `053727f3` with its own selftest AND re-derived here
with independent code; B1103 re-run) + **VERIFIED-DIFFERS** (B1140 vs fc R49 — two embeddings, each right about its own; chat1's
flavon labels) + **REGISTERED** (the no-tadpole theorem with its hypotheses; the scale link as a scenario; `FALSIFIER_REGISTER` P9)
+ **the fork finding** (Q2(d)) · **Price:** unchanged (no identification row; the fork is a VALUE the record does not fix, JOIN 2) ·
**Seats credited:** the SM-derivation seat (sm:B1283 2026-09-07, sm:B1300 2026-09-07, sm:B1301 2026-09-08 @ `053727f3`), the physics
seat (fc R49 @ `659487bb`), chat1 (relay 2026-09-08, archived here), the outside session behind B1103 (2026-08-21).

## 0. What each seat said, first (§1a rule 2), and what happened to it here

| seat item | the seat's headline (verbatim) | here |
|---|---|---|
| sm:B1283 | "every SM-preserving flat direction leaves one extra U(1) unbroken — a definite Z′ with computed charges — and carries exactly one light Higgs pair, one light colour-triplet pair and a ν^c VEV" | **VERIFIED** — 85 F-flat sets, 9 branches, all paired, rank 1 on three, (5ψ − 3χ)/2, the per-generation table, μ-rank 2: all reproduced with own code (§2) |
| sm:B1300 | "none of Y₉'s 706 464 Standard-Model Wilson lines projects out a single colour triplet D — by theorem, because w_D = −2 w_Q" | **VERIFIED** — the weight table from the LATTICE (a second route), the census from B1278's support theorem alone, the protection theorem (§4) |
| sm:B1301 | "the h¹ support of every closing Y₂ … Y₁₂ obeys a deck-eigen law … Y₁₂ is a second Standard-Model closing, on which the Wilson lines thin the colour triplet to ONE generation on 31 488 of its 34 752 SM lines" | **VERIFIED** — the law's arithmetic reproduces the odd support at every level 2–12 and the seat's forward list to 24 with no Fox calculus; the Y₁₂ census from the pinned support file with an own enumerator (§5) |
| fc R49 | "the certificate's own count contradicts its printed verdict ('no hypercharge room') … the object's e6 leaves two u(1)s of room next to so(3,1) ⊕ su(3), exactly as the rank count says" | **VERIFIED-DIFFERS** — true for the REGULAR embedding fc's rank count describes; B1140's fork uses the PRINCIPAL sl₂'s, where the centraliser is 0 and the printed 2 is a pair of spin-2 middle weights (§1) |
| B1140 (main) | "invariant content = 0 — no (spin-0, spin-0; singlet) term anywhere … Hypercharge cannot organize there" | **STANDS, scoped** to the fork's principal embedding; the certificate's sentence "0 = NO hypercharge room" beside a count of 2 is an unasserted verdict string (E69, minted) |
| chat1 §1(a) | "χ from the odd-plane determinant — 0 files … this derivation is not [in the record]" | **ALREADY BANKED** — B1103 THE BEING GATE (2026-08-21), its vendored certificate's STAGE 2 is the derivation verbatim; re-run here 1364/1364, RC=0 (E54 instance, cross-seat) |
| chat1 §1(c) | "M_soft ≳ 100 TeV, electroweak fine-tuning ~10⁶ … a definite, unfashionable, falsifiable position" | **VERIFIED as one branch of a fork** — every step computed (§2–§3); the number holds if the VEV'd generation is a light family and does not if it is the third, and the record does not say which (§3) |

## 1. Q0 — B1140 vs fc R49: two embeddings, both right (`b1303_centraliser.py`, PASS as pre-registered)

On main's exact e₆ in the SL(3)³ frame, sl₂ ⊕ sl₂ ⊕ sl₃ embedded two ways and the 64-dimensional complement decomposed:

| embedding | 64 = | states at weight (0,0) | of them colour singlets | centraliser of the 14 in the 64 |
|---|---|---|---|---|
| (T) B1138/B1140: the two sl₂'s PRINCIPAL in the first two sl₃'s | (4,0;1) + (0,4;1) + 6 × (2,2; coloured) = 5 + 5 + 27 + 27 | 8 | **2** | **0** |
| (R) the REGULAR A₁A₁A₂: root sl₂'s | (1,0)×2 + (0,1)×2 + **(0,0)×2** singlets; 6 × [(1,1)+(1,0)+(0,1)+(0,0)] coloured | 8 | **2** | **2** |

So B1140 (b) — "invariant content 0, no room for a u(1)" — is **correct for its embedding**, and its printed "2" is the two
spin-2 middle weights, members of multiplets. fc R49's argument ("the two Cartan directions orthogonal to the subalgebra's roots
commute with all its root vectors") is **correct for a regular subalgebra** — the principal sl₂'s raising operator is a SUM of two
root vectors, and the Cartan direction of A₂ orthogonal to ρ^∨ does not commute with it. The dispute dissolves into a scope
clause on B1140 ("under the fork's principal embedding") and R49's request is met: "no hypercharge room" is not carried to
main as an embedding-independent statement. What remains true of the certificate is chat1's point: `spacetime64.py` prints
`color-singlet (0,0) content in the complement: 2 (0 = NO hypercharge room; matches memo 11)` with no assertion — a verdict
string its own number does not test. That shape is minted as **E69** (below) with the fix rule: every printed verdict is an
assertion, and the receipt's exit code decides.

## 2. Q1 — the Z′, re-derived with own code (`b1303_zprime.py`, PASS; 8 s)

Inputs from the record: the 27's (ψ, χ) charges, the eleven multiplets' SM numbers and state counts, ANY basis of the family
torus, and the fourteen singlet monomials of B1276's one-coupling cubic as the seat states them (checked U(1)⁴-invariant here;
not re-derived from d_abc — the one fence). Everything else computed here: β = (ψ + χ)/4 and γ = −5ψ/12 + χ/4 reproduce the seat's
table on all eleven multiplets; the squarefree F-flat rule (a maximal-independent-set enumeration on the 18 singlets'
co-occurrence graph) gives **85** maximal F-flat sets; **exact** D-flatness (a rational certificate for every subset of every
F-flat set: a strictly positive combination of the charge vectors vanishing, or Gordan's dual) leaves **nine** maximal
branches, **all conjugate-paired**, three of six fields with surviving rank **1** and six of four fields with rank **2** —
**no branch breaks all four extra U(1)s, and no unpaired D-flat direction exists at all**. On each maximal branch the surviving
direction has β-coefficient **0**, E₆ part exactly **(5ψ − 3χ)/2** — charges **4** on Q, u^c, e^c; **−2** on d^c, L; **10** on ν^c, N;
**−8** on H_u, D; **−2** on H_d, D̄ — and, with the family part fixed by the neutrality of the VEV'd fields, the table

| generation | N, ν^c | Q, u^c, e^c | d^c, L | H_u, D | H_d, D̄ |
|---|---|---|---|---|---|
| g (VEV'd) | **0** | −6 | −12 | −18 | −12 |
| the other two | 15 | 9 | 3 | −3 | 3 |

— the family part is **(−10, 5, 5)** uniformly, so the heavy − VEV'd difference is **15 units on every multiplet**. The μ-matrix
μ_jk = λ|ε_ijk|⟨N_i⟩ has rank **2** on every maximal branch (one light Higgs pair, one light D pair) and rank 3 with three N's
(det 2λ³N₁N₂N₃, the control). **The seat's arc reproduces in full.**

**chat1's chain, items 1–3, computed (Q1′).** (f) On branch g the F-flat rule forbids exactly the four flavons S_gj, S_jg and allows
the other pair's S_hk, S_kh — chat1's printed sets name the pairs (1,1), (2,2), (3,3), which are not fields of the record (six
off-diagonal flavons; VERIFIED-DIFFERS in bookkeeping only, conclusion identical). (g) Every VEV'd field of every maximal branch
is Z′-neutral, 6/6 × 3 — by construction of the surviving direction, which is the content of "the Z′ survives". (h) The cubic
anomaly of the three 27s is **−20250**, of the 27̄s **+20250**, total 0 — and every MIXED coefficient ([SU(3)]²Z′, [SU(2)]²Z′, Y²Z′,
YZ′², gravitational) vanishes **on the 27s alone**: E₆ is a safe group and the family torus is traceless, so the −20250 is purely
the family torus's cubic, 27 · Σ f_i³ = 27 · (−1000 + 125 + 125). (The DESIGN's control sentence expected the 27s alone to be
non-zero on each coefficient; that was wrong for the mixed ones and is recorded as a mis-stated control — the substance, total
0 with the cubic as the live positive control, is as pre-registered.) (i) **The no-tadpole theorem, registered with its
hypotheses:** *Z′ anomaly-free ⇒ the non-perturbative superpotential is Z′-invariant (no instanton-induced charge, no
Green–Schwarz term to absorb one) ⇒ every term of W_eff linear in a Z′-charged field carries another charged field ⇒ with only
Z′-neutral VEVs, no tadpole at any order.* Item (h) is what extends chat1's item 2 to W_np. Consequence: **at the SUSY tree
level, and at every order in W, nothing on B1283's vacuum breaks the Z′ above the electroweak scale** (the light Higgs pair,
charges −18, −12, breaks it at v). sm:L209's "break, OR leave as a Z′" has one live branch: the Z′ is left, and something outside
W must break it — which is where the scale enters (§3).

## 3. Q2 — the FCNC regime, from Langacker–Plümacher's own equations (`b1303_fcnc.py`, PASS)

**Convention control.** Eq. (41) with a pure left-handed coupling against Δm_K^exp = 3.484·10⁻¹² MeV gives y|B₁₂|² <
**1.31·10⁻⁸** (F_K = 155.7 MeV) or **2.63·10⁻⁸** (the 110 MeV convention) — LP's eq. (54) "< 10⁻⁸" within a factor 3 either way, so
their bounds are used as printed. If both chiralities mix alike the LR bracket of eq. (41) is −8.40 against ⅓, and the K floor
rises by a factor 5 — reported, not used.
**Normalisation.** Tr Q′² over the three 27s (integer table) = **6210**; Tr Y_GUT² = 9; scale √(9/6210) = 0.0381; the 15-unit
difference is **Δε = 0.571** in units where the coupling is g₂ ~ g_GUT-like. y = g₂²v²/(4M_Z′²) for small mixing (eqs. 16–18 with
M_W = gv/2), so a bound y|B|² < b is M_Z′/g₂ > v|B|/(2√b).
**The two cases** (V_L^d ≈ V_CKM, LP's own illustration; PDG 2024 magnitudes):

| the VEV'd generation is … | \|B₁₂\| | Δm_K (eq. 54) | ε_K, O(1) phase (eq. 56) | D mixing if the CKM is up-sector (eq. 55) | B_d (eq. 54) | B_s (eq. 55) |
|---|---|---|---|---|---|---|
| **the first family** | 0.125 | **154 TeV** | **1720 TeV** | **49 TeV** | 2.4 | 0.1 |
| **the second family** | 0.125 | **154 TeV** | **1720 TeV** | **49 TeV** | 2.7 | 2.0 |
| **the third family** | 8.9·10⁻⁵ | 0.11 | 1.2 | 0.03 | 1.1 | **2.1 TeV** |

(all floors on M_Z′/g₂). **Case I** (a light family VEV'd): every route, including LP's named escape "V_CKM = V_L^u, V_L^d = 1"
(which moves the same 1–2 mixing into D–D̄ mixing), gives **≥ 49 TeV**, and the K system gives **10² TeV (Δm_K) to 10³ TeV (ε_K)** —
chat1's regime, priced: the escape costs a factor 3, not the regime. **Case II** (the third family VEV'd): the K floor is empty
and the B_s floor is **~2 TeV·g₂⁻¹** — the LHC regime (ATLAS 2026, universal benchmarks: Z′_SSM 5.5, Z′_χ 5.1, Z′_ψ 4.8 TeV; not
recomputed for these couplings). This is LP's conclusion in the record's own numbers: "any TeV-scale Z′ would almost certainly
have to have equal couplings to the first two families. However, there is still the possibility of different couplings for the
third family" — and B1283's Z′ has exactly two equal families and one different one. **Which family the VEV'd one is, is not in
the record**: the family characters χ_g are permuted by the deck 3-cycle, and the mass ordering of the generations is a value
(JOIN 2, 0/19). So the chain's number is a **fork on an unnamed identification** — the relay did not name it; this arc does.
**The scale link and the fine-tuning.** M_Z′ ∼ M_soft is LP's introduction ("their scales set by the soft supersymmetry breaking
parameters") and Cvetič–Langacker's radiative mechanism — a scenario, registered as such. Its stated alternative, breaking
along a D-flat direction at an intermediate scale, is **not available on the record's own vacuum** (every D-flat direction is
Z′-neutral, Q1′(g)); the remaining alternative — no breaking above v — leaves an electroweak-scale Z′ with O(g) couplings to
first- and second-family leptons (charges 3, 9), excluded by LEP/LHC in every case. So B1283's vacuum **requires** Z′ breaking
from outside the SUSY tree level, and radiative breaking by soft masses is the only mechanism the record's ingredients supply.
Given it: Case I puts M_soft at 10²–10³ TeV with Δ ∼ (M_soft/m_Z)² = 10⁶–10⁸ (Langacker's RMP §V.E names the same regime, "a
version of split supersymmetry", for a different mediation scenario); Case II puts it at the LHC scale with Δ ∼ 10³. **A regime,
not a value — and a fork, not a number.** Registered as `FALSIFIER_REGISTER` **P9** (sharpness S3 with an S2 half: a
family-non-universal Z′ found below 10 TeV with its light generation a light family would falsify B1283's vacuum), and P7
("no scale can be named") gains the addendum that a regime can now be named, conditionally.

## 4. Q3 — sm:B1300 by a second route (`b1303_dt.py`, PASS; 4 s)

In the trinification frame of main's exact E₆ (27 = (3,3̄,1) + (3̄,1,3) + (1,3,3̄); colour = the first sl₃; SU(2)_L on the second's
indices {0,1}; SU(2)_R on the third's {0,1}) the functionals Y = w₁[2]/2 − 2w₂[0]/3 + w₂[1]/3 + w₂[2]/3 and ψ = 3(w₁[2] − w₂[2])
reproduce the hypercharges and the SO(10) grading of all 27 states — two independent charges confirming the multiplet
assignment. P (the ℤ-span of the 27's weights) has rank 6, Q_SM (6 colour + 2 SU(2)_L roots) rank 3, and the 6 × 6 determinant of
{a ℤ-basis of Q_SM} ∪ {w_Q, w_u^c, w_L} in P's coordinates is **1**: **P/Q_SM is free of rank 3 with that basis** (the seat's
"coefficient determinant 1", now from the lattice). The weights mod Q_SM: **D = (−2,0,0)**, e^c = (2,−1,0), H_u = (−1,−1,0), d^c =
(1,−1,1), H_d = (−2,1,−1), D̄ = (−1,0,−1), N = (3,0,1), ν^c = (1,1,−1) — the pre-registered table, and the eleven zero-sum triples
(the seat's route) give the same. The 72 roots: **8** trivial (the SM's), **12** at ±(w_Q − w_u^c) (SU(5)'s X, Y), 52 others; the
seat's `e6_roots_qul.json` multiset is identical. With B1278's support theorem as the only input (h¹ = 1 exactly on
((C₁ ∪ C₂) × V₄) ∖ {1} in (ℤ/76)², C₁, C₂ the deck eigenlines of the roots 6 and 16 of Δ mod 19), an own enumerator over the
145³ = 3 048 625 lines gives **758 593 / 737 568 / 706 464 / 568 656** (three generations / SU(5) broken / SM vacua / full),
doublet–triplet split lines **0**, D loses a generation on **0** lines (D total is 3 on every one of the 3 048 625 candidates),
D̄ on 29 376, H_u 30 240, H_d 29 376, N 28 512, ν^c 28 512, and the seat's (H_u, H_d, D, D̄) histogram exactly; the square of every
letter is a letter and no square is a family character. (One criterion was misread on first writing: "full" is the seat's
subset of SM lines keeping all 81 states, not all-eleven-counts-3 on any line — 578 017 → 568 656 once read as the seat defines
it; not a discrepancy.)

## 5. Q4 — sm:B1301: the law's arithmetic and Y₁₂ (`b1303_tower.py`, PASS)

With no Fox calculus: |H₁(Y_n)| = L_n² (n odd) or 5F_n² (n even) matches the seat's invariant factors at every level 2–12, and the
law's odd-order count — 2(p − 1) for each prime p whose p-part is (ℤ/p)² and whose roots of Δ = t² − 3t + 1 mod p have exact
order d ≥ 3 with d | n — equals the seat's odd support at every level: **Y₅ 20 (p = 11, roots 5, 9, order 5), Y₇ 56 (29; 7, 25;
order 7), Y₉ 36 (19; 6, 16; order 9), Y₁₀ 20 (Y₅'s), Y₁₁ 396 (199; 63, 139; order 11), and 0 at 2, 3, 4, 6, 8, 12** (3 and 7 inert
for Δ, 5 a double root of order 2, Y₁₂'s 3-part (ℤ/9)² inert). Read forward, the arithmetic reproduces the seat's list to n = 24
(new at 13: 521 → 1040; 15: 31 → 60 plus Y₅'s 20; 17: 3571; 19: 9349; 20: 41; 21: 211 plus Y₇'s 56; 22: 89; 23: 139 and 461; none new
at 14, 16, 18, 24). From the seat's pinned `support_Y12.json` (sha `ccf5759f…`; the support itself is its 392 s Fox computation,
re-run here with its own selftest, receipt) an own enumerator gives **97 letters** (orders {1: 1, 16: 96}), **190 849 / 181 440 /
34 752 / 3 264**, the colour triplet **D thinned to exactly one generation on 31 488 SM lines (10 496 per generation)** and kept in
all three on the 3 264 full lines; D̄ loses on 18 528, H_u 15 744, H_d 16 608, N 12 000, ν^c 0; the Y₉ file as control gives Q3's
numbers. **Y₁₂ is a second Standard-Model closing, and enters L203.**

## 6. What this arc settles, and what it opens

- **The E53 scope fix, at source:** "the SM group is reached" (B1293's headline, B1294, MAIN_GOAL) is the Wilson line's gauge
  algebra; the tree-level vacuum is **SM × U(1)_Z′, rank 5**. Dated addenda on B1293 and B1294; a scope paragraph in MAIN_GOAL;
  CAMPAIGN_STATUS.
- **The first consequence a measurement can kill — as a fork.** P9 in the falsifier register; the plan's Phase 4 (5)
  "falsifiability cell" was already a surface (`FALSIFIER_REGISTER.md`, B1035) — the phrase was absent, the register was not.
- **L203 registered** — selection among the closings: Y₉'s 19 624 vacua AND Y₁₂'s 34 752 lines; the deck-eigen law is the only
  object-native selector on the table. **L205 registered** — the owner's D3 decision (one bounded arc after Phase 1).
- **B1103 is chat1's item.** The seat's "0 files" is an E54 instance on their bench; the record's name for the derivation is
  "the being gate". Cross-seat, recorded; the held reply says so.
- **Not settled:** which family character is the third family (a value); the instanton superpotential on the three moduli
  (sm:L209(i)); Y₁₂'s vacuum branches (L210/L203); RG running and lattice-improved inputs (order-of-magnitude by design).

## Receipts, verification, credit

Seat scripts, pinned worktree `053727f3`, own selftests: `sm_b1283_sm_closing_vacuum_rerun.txt` (PASS), `sm_b1300_dt_structure_rerun.txt`
(PASS), `sm_b1301_tower_alphabet_rerun.txt` (PASS, 392 s), `sm_b1301_e6_roots_qul_derive_rerun.txt`, `sm_b1301_lines_from_support_Y9/Y12_rerun.txt`
(the first invocation lacked the script's two arguments and was discarded); main's `main_b1140_spacetime64_rerun.txt` (the
unasserted line reproduced), `main_b1103_being_gate_rerun.txt` (ALL CHECKS PASSED); chat1's `chat1_check_relay_rerun.txt` (ALL
CHECKS PASSED; script archived as `chat1_check_relay.py`, sha f71c2fd7…). Own code: `b1303_centraliser.py` (Q0), `b1303_zprime.py`
(Q1/Q1′), `b1303_fcnc.py` (Q2), `b1303_dt.py` (Q3), `b1303_tower.py` (Q4), each with `.out` and `.json`; inputs pinned in
`verification/inputs/` with `SHA256SUMS`. Lock: `tests/test_b1303_the_sm_closings_z_prime.py` (DESIGN seal; Q0, Q1, Q2, Q3 by RUNNING;
Q4's arithmetic by running and its census pinned from JSON; receipts present). Literature read in full: Langacker–Plümacher
hep-ph/0001204; Langacker RMP 0801.1345 pp. 24–25 (both quotations verified in the text); abstracts: BDG 1211.1896, ATLAS
2607.28334, Arkani-Hamed–Dimopoulos hep-th/0405159, Giudice–Romanino hep-ph/0406088 (the scout's 0406088 = "Arkani-Hamed–
Dimopoulos" corrected on opening). HARVEST_LEDGER rows 28–35 (+ rows 13, 15, 20 updated). The chat1 relay is archived in this
directory; the reply is drafted and HELD (owner: all sends hold).
