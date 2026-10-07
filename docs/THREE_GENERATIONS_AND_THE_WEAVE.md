# THREE GENERATIONS AND THE WEAVE — what the physical three is, and what the weave derives, reads, leaves open, and cannot see

cc (the SM-derivation seat), 2026-10-07. The owner, verbatim: "should we do a deep research on three generations to
underatand tham first, so we dont expect eyes from the blind? ... do as u recomend, try everything, end goal is three
generations derived".

**The sources.**
- **The index side** (smooth and orbifold mechanisms): main's research page, its B1496 (`docs/THREE_GENERATIONS_RESEARCHED.md`
  on main, cited, not copied), and main's two standards (S79, the relay THE TWO STANDARDS FOR THREE).
- **The flavour side, the data and the checklist:** this seat's literature pass of the same day (§5). Main's run did not
  reach this side: its fourth query produced no surviving claim.
- **The weave's side:** `docs/THE_WEAVE.md` and `docs/dossiers/the_weave_2026-10-07/`.

**Scope.** Nothing here is promoted. Statuses are DERIVED (GENESIS), PROVED (here, by code beside the dossier),
COMPUTED, READING, OPEN and BLIND. 0 of 19.

## 1. The target: what the physical three is

**What the data fix (PDG 2026; NuFIT 6.1; the JUNO first result).**
- **Exactly three light doublet neutrinos:** N_ν = 2.9963 ± 0.0074 after the 2020 luminosity re-analysis (Janot and Jadach,
  arXiv:1912.02067).
- **A sequential fourth generation is excluded at 5.3σ** by the Higgs rates (Eberhardt et al., arXiv:1209.1101).
- **One generation is 5̄ ⊕ 10 (⊕ 1) of SU(5),** and the three are identical in gauge content. Lepton universality holds
  at the 0.3% level (LEP/SLD, hep-ex/0509008).
- **Anomalies cancel generation by generation,** so anomaly freedom does not constrain the number.
- **The generations differ only in their Yukawas.**
  - The masses span 10⁶ among the charged fermions.
  - The CKM is small and hierarchical (λ = 0.225).
  - The PMNS has two large angles and one small: sin²θ₁₂ = 0.3088 ± 0.0067, sin²θ₂₃ = 0.470, sin²θ₁₃ = 0.0225.
- **JUNO's first result:** sin²θ₁₂ = 0.3092 ± 0.0087 (arXiv:2511.14593).

**How "three" is obtained in physics.**
- **Nobody derives three.** Every mechanism selects it or forces only N ≡ 0 (mod 3) plus a bound: main's B1496, and this
  seat's pass (3-3-1; Dobrescu–Poppitz; Calabi–Yau and F-theory indices; branes; orbifolds; discrete and modular flavour
  groups; algebraic approaches).
- **Main's two standards (S79).**
  - The smooth standard is one rank-five bundle of index three.
  - The orbifold standard is three sectors of index one under an order-3 symmetry, distinguished by characters. Their 5̄'s
    are summed per sector.
  - Which one the genesis means is GENESIS's FK14.

**The checklist** (this seat's pass, §D).

| kind | items |
|---|---|
| structural | S1 replication; S2 chirality; S3 exactly three light; S4 anomaly freedom per generation; S5 the flavour group and how the three transform; S6 its breaking (residual subgroups per sector) |
| dynamical | masses, CKM, PMNS, CP phases, neutrino scale and nature |

- **A flavour group alone gives S5, S6 and mixing patterns.** It gives no masses: Schur's lemma makes an unbroken triplet
  degenerate.

## 2. What the weave gives, item by item

| item | the weave | status |
|---|---|---|
| **S3: three** | the two records' non-zero parities, 2² − 1. No single move treats them alike; any two moves make them one undistinguished three (W1). The fourth parity, zero, is the puncture and is not a line. | DERIVED from GENESIS GM1–GM2 (PROVED, W1) |
| **S5: the flavour group and the triplet** | A₄ on every odd-trace thread (W3), from the one structure all threads share, the quaternion point (W2). It acts irreducibly on the three lines, the parity-twisted cohomology of the shared fibre (W4). The moves add the transpositions, and the group on the lines is O_h; its rotations are S₄. W1's three parities by themselves are a permutation set (1 ⊕ 2); the irreducible triplet needs the fibre's sign flips, and those are W4's. | PROVED |
| **S1: replication (the three alike)** | Theorem G: whatever matter one line carries, the other two carry the same, carried around by the weave's 3-cycle | PROVED (structure) |
| **content: a generation on each line** | on +LR every line carries six sectors on the third level, each reading (−1, −1): one generation of each of six types (three classes up to the other order and the spin twist). The census of every odd-trace thread to length 6 finds generations on no other thread so far: eleven of twelve read at order 4, eight at order 3, the rest running. | COMPUTED (sm:B1550's sealed two-route counts; the census is design-time structure) |
| **the standard met** | the orbifold standard on +LR's third level: per type, three sectors of index one, distinguished by the parity characters and cycled by the 3-cycle. The cover is forced (W3), not chosen by a character, and three is never selected. | READING of the dictionary (GENESIS FK14) |
| **the smooth standard** | not met at orders 4 and 3 on any thread's forced cover. Its fibre has genus one, so it has no room (main's T-ROOM-NEEDS-GENUS); no member is fixed by A₄. Only the spin cover, of genus 3, has room, and there m004's members are all pulled back. | OPEN (excluded at these orders) |
| **S2: chirality** | the frame's index per line. Which way the extension runs decides generation against anti-generation (main's "the count is the order", B1466, B1486, B1499), and the weave does not fix it | OPEN (GENESIS GAP3) |
| **S4: anomalies per generation** | each line's sector reads I(W₁) = I(Λ²W₁): as many 5̄′ as 10′, the SU(5)-anomaly-free shape, line by line | COMPUTED on +LR |
| **S6 and mixing** | see §3 | READING |
| **masses and hierarchy** | an exact triplet is degenerate (Schur); values need dynamics | BLIND |

## 3. Mixing: the weave's own subgroups against the data (READING; `the_mixing.py`)

- **The rule** (Lam 2008, arXiv:0804.2622; Altarelli and Feruglio, arXiv:1002.0211). A sector that keeps a subgroup has its
  mass matrix diagonal in that subgroup's eigenbasis. Two sectors then mix by the overlap.
- **One sector: the golden thread's 3-cycle on the triplet.** Its eigenvalues are distinct, so the mixing is fixed. Every
  odd-trace thread gives a conjugate ℤ₃, and the patterns depend only on the pair up to conjugation.
- **The other sector keeps an involution of the weave, or a Klein group of them:**

| the other sector keeps | the mixing it gives | against the data |
|---|---|---|
| **the swap P** (or LPL, RPR, L·a, R·b) | **TM1**: the tri-bimaximal first column (2/3, 1/6, 1/6) is kept | **viable**: sin²θ₁₂ = 0.318 at the measured θ₁₃; +1.0σ against JUNO, +1.4σ against NuFIT 6.1 |
| the sign −I, or a fibre translation | TM2: the second column (1/3, 1/3, 1/3) is kept | disfavoured: +3.7σ against JUNO (Ding, Li, Lu and Petcov, arXiv:2512.03809: 3.6σ) |
| a single shear, L or R | θ₁₃ = 0 | excluded (θ₁₃ is about 40σ from zero) |
| a Klein group: a single move with a translation | tri-bimaximal | excluded since 2012 |
| the fibre's translations (V₄) | every entry 1/3 | excluded |

- **The weave's group on the triplet contains S₄,** the smallest group giving tri-bimaximal mixing for all couplings
  (Lam). The weave puts every one of these patterns within reach.
- **The swap is the one elementary move whose residual gives the pattern the data still allow.**
- **Mod 2 the golden thread LR is ST,** the order-3 rotation that fixes τ = ω, and the swap P is S, which fixes τ = i.
  These are the modular-flavour fixed points: the threads play τ = ω and the swap plays τ = i. That answers the
  literature's question of what plays τ for a framework built from Anosov words (§5, question 8).
- **The swap is the move main pairs with the Breath pulse** (det −1; main's wave programme). So the reading is that lepton
  mixing is the mismatch between the golden act and the breath.
- **What makes it a reading.** Which sector keeps which subgroup is not forced. The row assignment and the CP phases are
  not fixed either.
- **What would test it.** TM1 predicts sin²θ₁₂ = (1 − 3s₁₃²)/(3(1 − s₁₃²)), and cos δ tied to θ₂₃: δ ≈ 262° at
  sin²θ₂₃ = 0.470. JUNO's six-year precision of about 0.5% on sin²θ₁₂ decides it if the central value holds.

## 4. The derivation, step by step

| step | status | what |
|---|---|---|
| 0 | DERIVED (GENESIS) | PF1–PF3 → two records, the shears L, R (GM2); the sign and the swap OPEN (GM5b, GM5c) |
| 1 | PROVED (W1) | three non-zero parities; one undistinguished three only when moves act together |
| 2 | PROVED (W2) | the one structure every move fixes: the quaternion point |
| 3 | PROVED (W3) | from it, the same A₄ (and 2T) on every odd-trace thread; GENESIS's SE1 admits only such threads |
| 4 | PROVED (W4) | one irreducible triplet on the shared fibre, the same on every odd-trace thread; the weave's group O_h ⊃ S₄ |
| 5 | PROVED (Theorem G) | whatever one line carries, all three carry |
| 6 | COMPUTED | on +LR each line carries one generation of each type; on no other odd-trace thread to length 6 read so far (eleven of twelve at order 4) |
| 7 | READING (GENESIS FK14) | the three generations are the three lines: the orbifold standard, with the cover forced |
| 8 | READING | the weave's S₄ with the golden 3-cycle and the swap gives TM1 mixing |
| 9 | OPEN | chirality (the order); the smooth standard (room); masses; the six types; GENESIS GM5b and GM5c for the weave |

**Graded by GENESIS's `docs/THE_BAR.md`.**
- **Steps 1–5 are laws over every odd-trace thread,** not positives on a state.
- **Step 6 is a positive on one state.** With twelve threads, if none of the eleven others carries, its p is about 0.29.
  It is not a selection the bar would credit. The census of the whole GENESIS population would be needed for that.
- **So "the weave picks m004" is not claimed.**
- **What is claimed:** the three, its alikeness and its flavour group are the weave's, and on the one thread the census
  finds carrying content, every line carries a generation.

## 5. Sources (this seat's literature pass, 2026-10-07; read in full by the seat)

**Data.**
- PDG 2026 (pdg.lbl.gov, read 2026-10-07).
- NuFIT 6.1 (2025; with NuFIT 6.0, arXiv:2410.05380).
- JUNO, arXiv:2511.14593.
- Janot–Jadach, arXiv:1912.02067; Voutsinas et al., arXiv:1908.01704; LEP/SLD, hep-ex/0509008.
- Eberhardt et al., arXiv:1209.1101; Djouadi–Lenz, arXiv:1204.1252.

**Mechanisms.**
- CHSW, NPB 258 (1985) 46.
- Blumenhagen–Cvetič–Langacker–Shiu, hep-th/0502005.
- Ibáñez–Marchesano–Rabadán, hep-th/0105155.
- Kobayashi–Nilles–Plöger–Raby–Ratz, hep-ph/0611020.
- Altarelli–Feruglio–Lin, hep-ph/0610165.
- Pisano–Pleitez, hep-ph/9206242; Frampton, PRL 69 (1992) 2889.
- Dobrescu–Poppitz, hep-ph/0102010.
- García-Etxebarria–Montero, arXiv:1808.00009.
- Distler–Garibaldi, arXiv:0905.2658.
- Furey, arXiv:1405.4601; Gresnigt, arXiv:2609.10569.
- Chamseddine–Connes, arXiv:0706.3688.

**Flavour.**
- Ma–Rajasekaran, hep-ph/0106291; Babu–Ma–Valle, hep-ph/0206292.
- Altarelli–Feruglio, hep-ph/0504165, hep-ph/0512103, arXiv:1002.0211.
- King–Luhn, arXiv:1301.1340.
- Lam, arXiv:0804.2622, arXiv:0809.1185.
- Fonseca–Grimus, arXiv:1405.3678.
- Feruglio–Hagedorn–Ziegler, arXiv:1211.5560; Holthausen–Lindner–Schmidt, arXiv:1211.6953.
- Ding–Li–Lu–Petcov, arXiv:2512.03809.
- Feruglio, arXiv:1706.08749 (modular).
- Harrison–Perkins–Scott, hep-ph/0202074.

**Arithmetic.**
- Bowditch–Maclachlan–Reid, Math. Ann. 302 (1995) 31, as reported by Goodman–Heard–Hodgson, arXiv:0801.4815.
  - The arithmetic orientable once-punctured-torus bundles are w = LR, LLR, LLRR and their powers, each with its ± sister.
  - So among odd-trace primitive threads only ±LR. In the census these are exactly the threads with members, a pattern
    on twelve threads and not a theorem.
- Riley (1975), and Leininger, arXiv:math/0011113: the figure-eight group is of index 12 in PSL(2, O₃) and contains Γ(4).
- Riley (1972): its surjection onto PSL(2, F₃) ≅ A₄.

**Flagged as UNSURE in the pass, and not relied on here:** BMR's theorem number and exact wording; some journal
references (ACT DR6, JUNO).
