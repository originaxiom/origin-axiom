# B1303 — THE SM CLOSING'S Z′: DESIGN (pre-registration, sealed before any computation)

**Date:** 2026-09-08 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1303 + the chat1 additions (items 0–4) + the
sm:B1300/B1301 addition · **Inputs read in full before this seal:** sm:B1283, sm:B1300, sm:B1301 FINDINGS (pinned worktree
`053727f3`); B1140 FINDINGS and its vendored `spacetime64.py` (re-run, receipt in `verification/`); fc R49 (`659487bb`);
the chat1 relay §1(a)–(c), §5–§6 and its `check_relay.py` (re-run here: ALL CHECKS PASSED, RC=0); B1103 FINDINGS and its
vendored certificate (re-run here, RC=0); Langacker–Plümacher hep-ph/0001204 (all 20 pages); Langacker RMP 0801.1345 pp.
24–25 (text extracted, both quotations below verified verbatim); the abstracts of Buras–De Fazio–Girrbach 1211.1896, ATLAS
2607.28334, Arkani-Hamed–Dimopoulos hep-th/0405159, Giudice–Romanino hep-ph/0406088. **Seat scripts re-run in the pinned
worktree with their own selftests before the seal (receipts in `verification/sm_*_rerun.txt`): sm:B1283
`sm_closing_vacuum.py` PASS; sm:B1300 `dt_structure.py` PASS; sm:B1301 `tower_alphabet.py` PASS (392 s), `e6_roots_qul_derive.py`
RC=0, `lines_from_support.py` on Y₉ and Y₁₂ RC=0.** Nothing below was computed with main's own code before the seal.

## 0. The rules' lines (already banked; absence; the one item that was already ours)

- `already_banked.py "Z'" "Z prime" "FCNC" "family-non-universal" "tadpole" "cubic anomaly" "doublet-triplet" "kaon"
  "split supersymmetry" "M_soft" "Y_12"`: 239 corpus hits, **0 settled arcs matching ≥ 6 of 12 terms** — a MISSING/OPEN claim
  is admissible for the Z′ chain. Nearest (3 terms): B1233, B1253, B1255, B895, B1170 (cc3's [SU(3)]³ condition — an anomaly
  computation on a different U(1)).
- `absence_sweep.py`: "M_soft" PRESENT on 3 heads, all three the 2026-09-08 intake surfaces (no prior computation);
  "kaon mixing" PRESENT only in the loose relay file; **"split supersymmetry" ABSENT on every head, in deleted history and in
  the working tree**; "Green-Schwarz" PRESENT (B951/B971 prior-art scouts); "fine-tuning" PRESENT (CRYSTALLIZATION,
  OPEN_LEADS); "falsifiability cell" PRESENT only via HARVEST_LEDGER — **but `docs/FALSIFIER_REGISTER.md` EXISTS** (B1035:
  P1–P8, sharpness S1–S4; **P7 = "exactly two extra neutral gauge bosons", graded S4 "no scale can be named"**). The plan's
  Phase 4 (5) sentence "the phrase exists on no main surface" was true of the phrase and false of the surface: this arc's
  falsifiability entry goes INTO the register as P9, and P7 gets the addendum that a scale regime can now be named.
- **χ from the odd-plane determinant (chat1 §1(a), HARVEST_LEDGER row 13, "0 files"): ALREADY BANKED.** `frontier/B1103_being_gate/`
  (landed 2026-08-21, "THE BEING GATE: the ζ₃ phase reads exactly the abelianization"), harvested from an outside session's
  self-sufficient package; its `check_being_gate_vendored.py` STAGE 2 is the derivation verbatim (`det(odd R) = ζ₃²`,
  `det(odd L) = ζ₃`, `χ(a) = ζ₃, χ(b) = ζ₃⁻¹`, exponent p − q), exact in ℤ[ζ₃₀]. Re-run here: 1364/1364 words, ALL CHECKS
  PASSED, RC=0. So the seat's "genuinely absent (verified with the working instrument)" is a miss of THE ABSENCE RULE on
  their bench (the record files it under "being gate", not under "determinant"); no ℤ[ζ₃₀] script is needed from the seat.
  Row 13 becomes VERIFIED (already banked, B1103) at landing.

## 1. Literature — what is read in full, what is quoted, what is not claimed

**Langacker–Plümacher, PRD 62 (2000) 013006, hep-ph/0001204 — READ IN FULL (the load-bearing source).** Abstract: "assuming that
typical mixings are comparable to the CKM matrix, processes such as coherent μ − e conversion in a muonic atom, K⁰ − K̄⁰ and
B − B̄ mixing, ε, and ε′/ε lead to significant constraints on Z′ bosons in the theoretically and phenomenologically
motivated range M_Z′ ∼ 1 TeV." Introduction (the M_Z′ ∼ M_soft link, verbatim): "in perturbative heterotic string models
with supergravity mediated supersymmetry breaking, the U(1)′ and electroweak breaking are both driven by a radiative
mechanism, with their scales set by the soft supersymmetry breaking parameters, implying that the Z′ mass should be less
than around a TeV [3]. (The breaking can be at a larger intermediate scale if it is associated with a D-flat direction [4].)"
Formalism: eq. (7) B^{ψ_L}_{ij} = (V_L^ψ ε^{(2)}_{ψ_L} V_L^{ψ†})_{ij}; eq. (16)–(18) ρ_i = M_W²/(M_i² cos²θ_W),
y = (g₂/g₁)² (ρ₁ sin²θ + ρ₂ cos²θ), g₁ = g/cos θ_W. **Eq. (41):**
Δm_P = 4√2 G_F m_P F_P² y { ⅓ Re[(B^{q_L}_{ij})² + (B^{q_R}_{ij})²] − [½ + ⅓ (m_P/(m_{q_i}+m_{q_j}))²] Re(B^{q_L}_{ij} B^{q_R}_{ij}) }.
**Eq. (54):** y |Re[(B^{d_{R,L}}_{12})²]| < 10⁻⁸ (Δm_K), y |Re[(B^{d}_{13})²]| < 6·10⁻⁸ (B_d); **eq. (55):** y |Re[(B^{d}_{23})²]| <
2·10⁻⁶ (B_s), y |Re[(B^{u}_{12})²]| < 10⁻⁷ (D); **eq. (56):** y |Im[(B^{d}_{12})²]| < 8·10⁻¹¹ (ε_K). §4 (M_Z′ = 1 TeV, θ = 10⁻³,
g₂ = 0.105, CKM-like mixings): all three families different ⇒ μ-e conversion "six orders of magnitude above the experimental
limits"; first-generation charges set to zero ⇒ K and D mass splittings "larger than the measured values by two orders of
magnitude", ε_K "too large by factors 6·10⁵". Conclusion: "we conclude that any TeV-scale Z′ would almost certainly have
to have equal couplings to the first two families. However, there is still the possibility of different couplings for the
third family." The escape they name: "the flavor changing effects in the B and K systems could be eliminated if the CKM
mixing were due entirely to the u quark sector, i.e., V_CKM = V_L^u, with V_L^d = V_R^d = 1."
**Langacker, RMP 81 (2009) 1199, 0801.1345 (arXiv v3, 31 pp.), pp. 24–25 read; both sentences verified in the extracted text:**
§IV.D: "The limits from K⁰ − K̄⁰ mixing (including CP violating effects) and from μ − e conversion in muonic atoms are
sufficiently strong to exclude significant nonuniversal effects for the first two families for a TeV-scale Z′ with electroweak
couplings. However, nonuniversal couplings for the third family are still possible". §V.E: "Requiring the latter to be in the
range 10² − 10³ GeV implies M_{Z̃′} ≳ 10³ TeV (for electroweak couplings), with the sparticles, exotics, and Z′ around
10 − 100 TeV and the electroweak scale obtained by a fine-tuning, i.e., a version of split supersymmetry (Arkani-Hamed and
Dimopoulos, 2005)." — a specific mediation scenario (U(1)′ unbroken in the hidden sector, Z̃′ massive), not a theorem.
**Abstract-level:** Buras–De Fazio–Girrbach, JHEP 02 (2013) 116: "for M_Z′ > 5 TeV Z′ effects in rare B_{s,d} decays are found
typically below 10%" while K decays "provide an important portal to scales beyond those explored by the LHC". ATLAS,
arXiv:2607.28334 (30 Jul 2026, 13.6 + 13 TeV): "Z′_SSM (5.5 TeV), Z′_χ (5.1 TeV) and Z′_ψ (4.8 TeV)" — family-UNIVERSAL
benchmarks. Split supersymmetry: Arkani-Hamed–Dimopoulos hep-th/0405159 (JHEP 0506:073); Giudice–Romanino hep-ph/0406088
(NPB 699:65) — the scout had attributed 0406088 to Arkani-Hamed–Dimopoulos; corrected on fetch (E68 discipline: every
citation opened). King–Moretti–Nevzorov hep-ph/0510419 (E₆SSM): cited by sm:B1283 for the comparison U(1)_N ≠ this Z′.
Cvetič–Langacker PRD 54 (1996) 3570 (radiative U(1)′ breaking) cited through LP ref. [3], not opened.
**Not claimed from the literature:** a closed-form "M_Z′/g′ ≳ X TeV for anarchic charges" (no source states one — the 10²–10³ TeV
is an order-of-magnitude reading of LP's eq. (54)/(56) with O(1) charge differences, which is what §3 Q2 computes); a
family-non-universal reinterpretation of the ATLAS limits; updated lattice inputs (LP's bounds are vacuum-insertion, no bag
factor, no SM subtraction — order-of-magnitude by construction).

## 2. The view from above

This arc sits where the structure chain's OUTPUT (the SM closing's tree-level vacuum, computed on the arithmetic face's
Y₉) meets the first physics that could kill it. It asks nothing of the quantum face. It does not touch the chirality bit
(every closing is vector-like; B1294–B1297). **If Q1 fails** (the Z′ table does not reproduce) the SM closing's tree-level
vacuum is unknown again and L209/L203 lose their premise. **If Q2's regime fails** (the FCNC floor under CKM-like mixing comes
out below the LHC's 5 TeV) chat1's chain is empty and the falsifiability entry says only "a Z′ heavier than the LHC reach".
**If both pass**, the record gains its first consequence that a measurement can refute — and the honest form of it is
TWO-VALUED on an identification the record does not make (which of the three family characters carries the third family:
the values are 0/19) and lives on an observer-selected vacuum (one of nine branches, on one of 19 624 lines of one of at
least two SM closings). "A regime, not a value" — and a fork, not a number.

## 3. Pre-registered questions — predictions written before the scripts exist; PASS and FAIL both reachable

**Q0 — B1140 vs fc R49 (the disputed banked verdict; first).** `b1303_centraliser.py` (written before this seal, NOT run) builds
main's exact e₆ in the SL(3)³ frame and two embeddings of sl₂ ⊕ sl₂ ⊕ sl₃: (T) B1138/B1140's, the two sl₂'s PRINCIPAL in the
first two sl₃'s (h = diag(2,0,−2)); (R) the REGULAR A₁A₁A₂ embedding (root sl₂'s, h = diag(1,−1,0)). For each: the 64's
weight table with colour content; the zero-weight colour-singlet count (the number `spacetime64.py` prints beside "0 = NO
hypercharge room"); the centraliser of the 14 inside the 64 = trivial sl₂ ⊕ sl₂ strings in the colour-singlet sector.
**Predictions:** (T): zero-weight singlets **2**, centraliser **0**, 64 = (4,0) + (0,4) singlets + 6 × (2,2) coloured = 5 + 5 + 27 + 27;
(R): zero-weight singlets **2**, centraliser **2**. **PASS** iff all hold; **FAIL** otherwise. Reading if PASS: B1140 (b) "invariant
content = 0" is correct FOR ITS EMBEDDING and its printed "2" is the pair of spin-2 middle weights; fc R49's "two u(1)s of
room" is correct FOR THE REGULAR EMBEDDING, where the same count is the centraliser; the certificate's sentence "0 = NO
hypercharge room" beside a count of 2 is a verdict string no assertion tests (the relay's dead-verdict shape) — grade
**VERIFIED-DIFFERS** (different embeddings, both right about their own), B1140's verdict STANDS with the scope clause
"under the fork's principal embedding", and R49's request ("do not carry 'no room' to main") is met by the clause. Reading
if FAIL on (T): B1140 is wrong and is retracted-keeping-the-computation.

**Q1 — sm:B1283's Z′, re-derived with main's own code** (`b1303_zprime.py`). Inputs taken from the record: the 27's (ψ, χ)
charges (SO(10) ⊃ SU(5) tables: ψ = 1, −2, 4 on 16, 10, 1; χ = −1, 3, −5 on the 10, 5̄, 1 of the 16 and 2, −2 on the 5, 5̄ of
the 10), the SM quantum numbers of the eleven multiplets with their state counts (Q 6, u^c 3, d^c 3, L 2, e^c 1, ν^c 1, N 1,
H_u 2, H_d 2, D 3, D̄ 3 = 27), the family torus as ANY basis of the traceless diagonal u(1)² on three generations (S_ij, i ≠ j,
charge e_i − e_j; X_j charge e_j; conjugates negative), and the 14 singlet monomials of B1276's one-coupling cubic as the seat
states them (S_ij N_j N̄_i, S_ij ν^c_j ν̄^c_i, S₁₂S₂₃S₃₁, S₂₁S₃₂S₁₃) — their U(1)⁴-invariance is CHECKED with my charges,
their derivation from d_abc is not repeated (fence). **Predictions:** (a) β = (ψ+χ)/4 and γ = −5ψ/12 + χ/4 reproduce the
seat's (q_β, q_γ) table on all eleven multiplets; (b) the squarefree F-flat rule on 18 singlets gives **85** maximal F-flat
coordinate subspaces; (c) exact D-flatness (Farkas/LP over the four charges) leaves **9** maximal SM-preserving branches,
**all conjugate-paired**, surviving abelian rank **1** on three and **2** on six, so the minimal rank is 1 (no branch breaks
all four); (d) on each maximal branch the surviving direction has E₆ part **(5ψ − 3χ)/2** up to scale and sign — charges 4 on
Q, u^c, e^c; −2 on d^c, L; 10 on ν^c, N; −8 on H_u, D; −2 on H_d, D̄ — and, with the family part fixed by neutrality of the
VEV'd fields, the per-generation table (VEV'd g: 0, −6, −12, −18, −12; the other two, equal: 15, 9, 3, −3, 3) up to overall
scale and sign; (e) the μ-matrix on each maximal branch has rank **2** (one light Higgs pair, one light D pair); the
three-N control has rank 3. **PASS** = (a)–(e); **FAIL** = any count or any charge differs (then the discrepancy is the finding).
**Q1′ — chat1's chain, items 1–3, computed:** (f) on branch g the F-flat rule forbids exactly the flavons S_gj, S_jg (four of
the record's SIX off-diagonal flavons) and allows S_hk, S_kh — chat1's printed sets include the pairs (1,1), (2,2), (3,3),
which are not fields of the record (VERIFIED-DIFFERS in bookkeeping only; the conclusion identical); (g) every VEV'd field of
every maximal branch is Z′-neutral (**6/6 on each of 3 branches**); (h) the cubic anomaly Σ q³ over the three 27s is
**−20250** and over the 27̄s **+20250** (own multiplicities), and the [SU(3)]²Z′, [SU(2)]²Z′, Y²Z′, YZ′², gravitational
coefficients each vanish, the 27s alone non-zero on each as the positive control; (i) the no-tadpole statement is REGISTERED
as a theorem with its hypotheses made explicit: *Z′ anomaly-free ⇒ W_np is Z′-invariant (no Green–Schwarz/instanton charge)
⇒ any term of W_eff linear in a Z′-charged field carries another charged field ⇒ with only neutral VEVs no tadpole at any
order* — the anomaly result (h) is what extends chat1's item 2 to the non-perturbative terms. **PASS** = (f)–(h) as predicted.

**Q2 — the FCNC regime, computed from LP's own equations** (`b1303_fcnc.py`; PDG 2024 / FLAG inputs stated in the script).
(a) **Convention control:** re-derive eq. (54) from eq. (41) with a pure left-handed coupling and Δm_K^exp = 3.484·10⁻¹² MeV:
predicted y|B₁₂|² bound between **5·10⁻⁹ and 3·10⁻⁸** for F_K ∈ {113, 156} MeV (the two decay-constant conventions), i.e. LP's
"10⁻⁸" within a factor 3 either way. (b) **Normalisation:** Q′ scaled so that Tr Q′² over the three 27s equals Tr Y_GUT² = 9
(the Killing-form convention under which every U(1) ⊂ E₆ has the same trace on a 27); predicted factor √(9/6210) ≈ 0.0381,
so the charge difference between the VEV'd and the heavy generations, 15 units on Q, u^c, d^c, L, e^c, is Δε ≈ 0.571 in
units where g₂ ≈ g_GUT-like couplings apply; y = g₂² v²/(4 M_Z′²) for small mixing (from eq. 16–18 with M_W = gv/2).
(c) **Case I — the VEV'd generation is one of the two light families, V_L^d ≈ V_CKM:** B^{d_L}_{12} ≈ Δε·V_{11}V*_{21} ≈ 0.571 λ;
predicted floors: Δm_K ⇒ **M_Z′/g₂ ≳ 1.5·10² TeV**; ε_K with an O(1) phase (eq. 56) ⇒ **≳ 1.5·10³ TeV**; the up-sector escape
(V_L^d = 1 ⇒ V_L^u = V_CKM) ⇒ D-mixing (eq. 55) ⇒ **≳ 5·10¹ TeV** — the escape lowers the floor by ~3, not to the LHC scale.
**PASS** = every route in Case I gives M_Z′/g₂ ≥ 10 TeV (the "10²–10³ TeV" regime stands, with the escape priced);
**FAIL** = any route < 10 TeV. (d) **Case II — the VEV'd generation is the third family:** the 1–2 element is V_{13}V*_{23} ~ 3·10⁻⁴,
so the K floor is empty (predicted < 1 TeV); the B_d and B_s floors from eqs. (54)–(55): B_{13} ≈ 0.571|V_td|, B_{23} ≈
0.571|V_ts| ⇒ predicted **2–3 TeV each** — the LHC regime (ATLAS universal-benchmark 4.8–5.5 TeV, not recomputed for these
couplings). **PASS** = both B floors < 10 TeV (the fork between the cases is ≥ one order of magnitude, i.e. real);
**FAIL** = a B floor ≥ 10 TeV (then Case II is not an escape and the regime is unconditional). (e) **The scale link** M_Z′ ∼ M_soft
is a scenario, not a computation: registered with LP's sentence and its stated alternative (breaking along a D-flat
direction at an intermediate scale — but B1283's D-flat directions are all Z′-NEUTRAL, so on the record's own vacuum that
alternative is not available: Q1′(g)); the other branch of the alternative — no breaking above the EW scale — leaves an
EW-scale Z′ with O(g) couplings to first- and second-family leptons (charges 3, 9 on the heavy generations' L, e^c),
excluded by LEP/LHC in every case. So B1283's vacuum REQUIRES Z′ breaking from outside the SUSY tree level; radiative
breaking by soft masses is the only mechanism the record's own ingredients supply, and it puts M_Z′ at M_soft. (f)
Fine-tuning reported as Δ ≈ (M_soft/m_Z)² for M_soft ∈ {5, 100, 1000} TeV — predicted 3·10³, 1.2·10⁶, 1.2·10⁸ — a Barbieri–Giudice
scaling, not a computed measure. (g) **Identification status:** "which family character is the third family" is a VALUE
statement (JOIN 2, 0/19); it is fenced as the observer's in the falsifiability entry and registers NO identification row
(no ratchet move); the vacuum choice is the closing's (L203).

**Q3 — sm:B1300 re-derived** (`b1303_dt.py`). (a) The weights of the 27 modulo the SM roots in the basis (w_Q, w_u^c, w_L),
solved from the eleven zero-sum triples of the 27's cubic couplings (own linear algebra): predicted **w_D = −2 w_Q**, w_e^c =
2w_Q − w_u, w_H_u = −w_Q − w_u, w_d^c = w_Q − w_u + w_L, w_H_d = −2w_Q + w_u − w_L, w_D̄ = −w_Q − w_L, w_S = 3w_Q + w_L,
w_ν^c = w_Q + w_u − w_L. (b) With B1278's support theorem as input (h¹ = 1 exactly on ((C₁ ∪ C₂) × V₄) ∖ {1} in (ℤ/76)²), an
own enumerator over the 145³ = 3 048 625 lines: predicted three-generation **758 593**, SU(5)-broken **737 568**, SM vacua
**706 464**, full **568 656**; doublet–triplet split lines **0**; D loses a generation on **0** lines; a multiplet is projected iff
its character is a family character. (c) The protection theorem re-checked: the square of every letter is a letter and no
square is a family character. **PASS** = all numbers; **FAIL** = any differs.

**Q4 — sm:B1301 re-derived where main's own code can** (`b1303_tower.py`). (a) The deck-eigen law's ARITHMETIC without Fox
calculus: for n = 2 … 12, |H₁(Y_n)| = L_n² (n odd) or 5F_n² (n even), its primes, the roots of Δ = t² − 3t + 1 mod p and their
exact orders; the law predicts an odd-order support of 2(p − 1) per prime p carrying a root of exact order d ≥ 3 with d | n,
pulled back from level d: predicted odd supports **Y₅ 20, Y₇ 56, Y₉ 36, Y₁₀ 20 (from Y₅), Y₁₁ 396**, and **0** at n = 2, 3, 4, 6, 8, 12
(plus the 2-adic parts the law does not cover: Y₃ 3, Y₆ 27, Y₉ 3, Y₁₂ 123 − 0 odd). **PASS** = the odd counts match the seat's
table at every level; **FAIL** = any mismatch (then either the law or my reading of it is wrong — the finding). (b) The Y₁₂
census from the seat's `support_Y12.json` with an own enumerator (the support itself is the seat's 392 s Fox computation,
re-run here with its own selftest — receipt — not re-derived): predicted SM lines **34 752**, full **3 264**, D thinned to exactly
one generation on **31 488** (10 496 per generation), letters 97 of orders {1, 16}. **PASS/FAIL** per number.

**Q5 — registrations and repairs (no computation):** L203 registered (selection among the closings: Y₉'s 19 624 vacua AND Y₁₂'s
34 752 lines; the deck-eigen law as the only object-native candidate selector); **L205 registered — THE SIBLING'S LOCALIZED
COUNT (owner decision 2026-09-08: D3 reopened as ONE bounded arc after Phase 1; PW eq. 3.18 on m202 with fc's two choices as
identification rows; the three-line tetrahedral class searched for a golden-face member; not a door until it earns one)**;
the E53 scope fix "the SM gauge algebra is reached; the tree-level vacuum leaves SM × U(1)_Z′ (rank 5)" on MAIN_GOAL,
CAMPAIGN_STATUS, B1293 (dated addendum), B1294 (dated addendum); FALSIFIER_REGISTER P9 (+ P7 addendum); HARVEST_LEDGER rows
for sm:B1283, sm:B1300, sm:B1301, fc R49, B1140's certificate, chat1 rows 11–20 dispositions updated (13 → VERIFIED/B1103;
15 → VERIFIED with the two-case fork); the two loose relays archived inside this arc; hint rows.

## 4. Priors (stated so the outcome can be graded against them)

Q0 both predictions hold: 90 %. Q1 reproduces (a)–(e): 90 %. Q1′ (f)–(h): 90 %. Q2(c) Case I regime ≥ 10 TeV on every route:
80 %; Q2(d) Case II floors < 10 TeV (the fork real): 85 %. Q3: 90 %. Q4(a): 75 % (even levels and pull-backs are where a
naive count would slip); Q4(b): 85 %. Expected verdict: **VERIFIED (sm:B1283, sm:B1300, sm:B1301, B1103) + VERIFIED-DIFFERS
(B1140/R49; chat1's flavon labels) + REGISTERED (the no-tadpole theorem, the scale link, P9) + the fork finding** (the M_soft
regime is conditional on which family the VEV'd generation is — a point the relay did not name).

## 5. Method, controls, discipline

Every script asserts its predictions and prints the count that could have differed (MB12); PASS and FAIL lines both exist;
pytest's own rc, never through a pipe (E39); seat scripts run in the pinned worktree `053727f3` with their own selftests and
the receipts kept; main's re-derivations use main's code only (B1297's E₆ frame; own graph/LP/enumerators); every quotation
above was grepped in its source (E68); no seat grade is lowered without a computation here (§1a rule 2); the seats are
credited by branch + pin; loose relay files are archived inside this arc, never at root. Out of scope: the instanton
superpotential (sm:L209(i)); Y₁₂'s vacuum branches (L203/L210); Z–Z′ and kinetic mixing; RG running; updated lattice inputs;
a family-non-universal LHC reinterpretation.
