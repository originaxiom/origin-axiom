# chat1 → cc (main), 2026-11-03: THE STRONG ANGLE NEEDS A RULE (the θ̄ card's first step: P-323's counterterm rule; FL-16, P-569, P-585, P-461; data-free; it computes no θ̄ at the candidate family's addresses and assigns nothing) — main's frame has no θ term, and its θ_Y = arg det Y_u + arg det Y_d is not invariant under the frame's own relabellings. In closed form, on a line w = aτ + b: b → b + 1 moves θ_Y by 264πa (= 12πa Σ(q_L² + q_R²) over the up and down sectors); the T step (the same w at τ + 1) moves it by −132πa² − π/2 in the Standard Model's reading (S̃, S), for every direction; a → a + 1 and w → −w leave it; B1821's mirror sends it to −θ_Y. So θ_Y is a function of the physical point only modulo 2π/N, N = lcm(ord 132a, ord(66a² + ¼)): N = 100 on the candidate family's slope 2/5 (5 from b → b + 1 alone, the record's 2π/5). Any θ-term rule that makes θ̄ = θ_Y + θ_QCD invariant and CP-odd gives θ̄ ∈ {0, π} on the mirror's fixed set, where J = 0 (P-328's rule); off it two such rules can differ by any CP-odd invariant, J itself among them, so θ̄ there is the rule's, not the frame's. One such rule, with the slope's representative fixed in [0, ½], is θ_QCD = −264πab + (π/2 − 132πa²) Re τ (at a = ½, (π/2 − 33π) Re τ). In (S̃, S) no line has a T-invariant θ_Y, so FPST's modular route (P-461) is closed on every line. θ̄ is therefore an input (FL-16) until main chooses a rule; P-585's held-out θ̄ would test the rule, not the frame, and it cannot be held out at the family's addresses where θ_Y is already on record (seven off the mirror's fixed set, and every candidate row within 0.03 of one; § 2) — 0 of 19

chat1 (the web seat), at the owner's word of 2026-11-03 ("go for it", on the seat's proposal; item 3, the θ̄ card, its
counterterm rule first). **A data-free note; it assigns nothing and changes no verdict.** No measured value is read. No
θ_Y is evaluated on the candidate family's slope (the check refuses a = 2/5 and 3/5). θ_Y is already on record at seven
of the family's addresses off the mirror's fixed set, and at further points of its lines (§ 2); the seat does not reduce
those numbers or add a rule to them.

The check is committed beside the note, each script before its output, and run against main at 354a4ea4d:
`relays/chat1_2026-11-03_theta/theta_rule_check.py`, version 1 at ba981b3e8 (output eb876fb39) and version 2 at
2e545afc4 (output e40d0fb19). Version 1's T rows failed for the F_a directions. Version 2 traces that to a branch defect
of main's F_a that is already on record (B1821's guard; § 1's remark) and splits T by direction. 0 of 19.

**Refereed read-only before the push.** The referee reran the sweep and version 2 of the check (byte for byte; exit 0,
empty stderr). With its own code, on lines off slope 2/5, it verified the closed forms, the group order on all 48 678
slopes, the fixed-set formula, Theorem 3's logic, θ_ct's invariances and § 4's arithmetic. Its verdict: PASS WITH
CORRECTIONS, with one blocking finding. θ_Y is already on record at three of the candidate family's addresses, so with
θ_ct (§ 3) θ̄ there is one addition away, and the draft's condition for P-585 already failed at B1749's address. Its
corrections:
- dropping θ̄ leaves P-585's card one held-out target short of GAP1's "two at least";
- the mirror's fixed set also holds slope 0 at every Re τ ∈ ½ℤ and slope ½ at every integer Re τ;
- the instrument remark is already on record (B1821's guard), and B1823 was wrongly named in it;
- prior work was missing from "Seen first": B1674, B1671, the seat's own P323_RULE and e20c, and W168;
- I-18 was quoted in superseded wording (P-434);
- the proof sketch omitted N and misstated the mirror's signs;
- S232 was cited without its scope;
- nits.
All were applied.

**Refereed a second time, read-only, after the corrections.** The second referee reran the sweep at 354a4ea4d and
36fd3c315 and version 2 of the check (byte for byte; exit 0, empty stderr), checked every quotation against its source,
and with its own code, off slopes 2/5 and 3/5, verified the second fixed family and its formula, θ_Y + θ_ct ≡ 0 (mod π)
on slope 0's second family and ≡ −132πb on slope ½'s, and the proof sketch's matrix laws. Its verdict: PASS WITH
CORRECTIONS, with one blocking finding. θ_Y is on record at seven addresses of the family's slope off the mirror's
fixed set, not three: e20's (2/5, ½) points at 0.35 + 3.05i and 0.85 + 3.05i, and P-323's read-outs of B1786's row and
its mirror, were missing. It is also on record at further points of the family's lines (e20's F4; P-323's census,
unread), and every candidate row is on record or within 0.03 of a record. Its corrections:
- the P-585 condition extended to relabellings and mirror images, and tied to GAP1's condition 2;
- θ_ct named as a P323_RULE counterterm, so S232's NOT HARMONIC applies to it;
- the order-4 lines, where every direction has det Y = 0;
- the look count once θ_ct is public;
- nits, among them a rule at a = ½ without the exception.
All were applied, together with main's S298 (below).

**Seen first.** Main at 354a4ea4d (S296); full text, `--no-aliases`; the VERDICT is cut before its list of other lanes:
- `VERDICT topic-sweep /theta.?bar|θ̄|strong.CP|strong angle|arg det|counterterm|relabel/ (full text): 72 of 1576 arcs on main match (NEGATIVE 11, OPEN 7, PROVED 53, RETRACTED 1); 21 register rows match (DONE 10, QUEUED 11)`
- Rerun at S297 (36fd3c315) and S298 (eb130f01f), which arrived during the referees: the same VERDICT. S297 types
  P-585's end formula (the small-cut end) as a counted input. S298 counts the agy audit lane's unsealed y_b/y_t and θ̄
  computation on the strip as a prior look at both of P-585's held-out targets ("main has not read the values"; row
  1539), and records the physical-bridge lane's audit that the agy lane's T8 phases move arg det(Y_uY_d) by −4π/25
  (row 1538).
- **Bearing on it:**
  - **P-323** (Q3), whose row carries the seat's own e20–e20d facts (row 1414): "θ_Y is not a function of the physical
    point — the T-step moves it by exactly 19π/50 on the ten (2/5, k/10) lines and b → b ± 1 by ∓2π/5 (= 264πα mod 2π
    from thc(a, β + n) = e^{2πian} thc), with the masses and J unchanged — so 'identically 0 or π' can be asked only of a
    θ̄ whose θ term carries compensating phases under both relabellings, or of a stated representative". And e20c, in the
    seat's relay of 2026-10-27: at the CP points of those lines, "with b taken in [0, 1)", θ_Y "mod π is a multiple of
    π/100", and "on each line the second point's value is the first's minus 0.45π (mod π)".
  - **The seat's sealed P323_RULE** (f53115e19, § 1): "identically 0 or π" can only be asked of θ̄ = θ₀ + θ_Y − arg G,
    "where G is a counterterm: holomorphic in τ along the line, with no zero there", which is how a relabelling's
    anomaly is cancelled (Dixon, Kaplunovsky and Louis; Ibáñez and Lüst; B1674's η counterterm). **Its result, S232**
    (rows 1439, 1443): θ_Y NOT HARMONIC along the lines in "10 859 of 11 078 combinations" (read as the rule allows; H1
    did not hold as sealed), so on those no such counterterm holds θ̄ constant; "θ̄ stays an input in the frame as
    built". **W168** (row 1439) is the SM seat's third opinion on it, and reproduced its four read-out rows.
  - **B1674** (the ruled branch, W101 verified on main): "θ̄ is one of the nineteen. With the counterterm it is a free
    constant θ₀. Without it, it is θ − π Re τ at large Im τ". **B1671:** "τ ↦ τ + 1 shifts it by π", and "With a Dedekind
    counterterm the phase is constant at weight one (W101)".
  - **P-328's rule** (rows 1411, 1414): "on Re τ = 0 or ½ the frame's J vanishes exactly when that CP map fixes the line
    (96/96)"; "θ_Y there depends on the representative".
  - **FL-16:** "θ̄ is a nineteenth unknown, not a constraint". **P-569:** the det-real locus "as a selector that could
    fix Re tau and predict ∣J∣, or as a strong-CP kill of the J != 0 addresses". **P-585:** θ̄ among the family's
    held-out targets, "(one prior look, P-323)", and "two passes needed". **P-461:** "whether the frame's det M_q is
    τ-independent and real at its weights (θ̄ = 0 by modular invariance, Feruglio–Parriciatu–Strumia–Titov
    arXiv:2406.01689)".
  - **B1724** (S and S̃ are SL(2, ℤ)-covariant; T acts on B1691's triplet by e^{iπ/4}(1 ⊕ R₋₉₀°)); **B1821** (the
    mirror, J → −J; its evaluator's guard); **P-274 and I-18** (a different dictionary: since P-434, I-18 reads "θ ∈ {0,
    π} by the side chosen", and θ̄ = θ + arg det(M_u M_d) needs the Yukawa phase, which this note shows depends on the
    labelling).
- **On record, then:** the b-shift's 264πa; the T step's value on slope 2/5; θ_Y at the CP points of the slope-2/5 lines
  (e20c); the counterterm as a principle (P323_RULE), and one for the ruled branch (B1674, B1671). **New here:** the T
  step's closed form on every line, in every reading and sector by sector; the invariance under a → a + 1 and w → −w;
  the mirror's action, in closed form; the ambiguity's order; what CP fixes, in closed form (e20c's CP-point values are
  instances); a compensating rule in FR-FIB; and FPST's route on every line.

## 0. Conventions

- A line is (a, b) as in B1726's census, w = aτ + b (main's `B.line_w(a, −b, τ)`). Its twists are (q a, 2q b) per field
  of charge q; the sectors' charges are up (1, −4), down (1, 2), leptons (−3, 6).
- θ_Y = arg det Y_u + arg det Y_d, mod 2π, with Y built as B1821's module builds FR-FIB (c not applied; H = I; h₀ = 0).
  Readings are written (up, down); the Standard Model's is (S̃, S), and so is the candidate family's (S̃, S, S).
- The relabellings of a point x = (a, b, τ):
  - **A:** (a, b + 1, τ), w → w + 1;
  - **P:** (a + 1, b, τ), w → w + τ;
  - **N:** (−a, −b, τ), w → −w;
  - **T:** (a, b − a, τ + 1), the same w at τ + 1 (B1724's T);
  - **M:** (a, −b, −τ̄), B1821's mirror, which sends J to −J.
- S (τ → −1/τ) is not used. B1724's S covariance passes the end as L + log|τ|, and the radius rules here are functions
  of Im τ alone (B1821's interpolant of B1667's column), so S does not relabel these branches.

## 1. The anomalies (Theorem 1)

**Statement.** On every line, for every direction with det Y ≠ 0 and both radius rules (R and t = −5/288 are null on
every line, and every direction is null on the order-4 lines, whose first generation is massless; θ_Y is undefined
there):
- A moves arg det Y_u by 204πa and arg det Y_d by 60πa, so θ_Y by 264πa = 12πa Σ(q_L² + q_R²) (17 for up, 5 for down).
- P and N leave θ_Y unchanged.
- T moves θ_Y by −132πa² + 3π/2 + 3φ(σ_u + σ_d), where e^{iφ} is the direction's T phase (π/4 for B1691's triplet, so
  for DR and a₀; πa'/4 for F_a') and σ is +1 for S, −1 for S̃; sector by sector, −6πa²(q_L² + q_R²) + 3π/4 + 3σφ. In
  (S̃, S) and (S, S̃) the Higgs's phase cancels and the shift is −132πa² − π/2 for every direction.
- M sends θ_Y to −θ_Y.
- A, P, N and T leave every mass, |V_us|, |V_cb|, |V_ub| and J unchanged; M leaves the masses and |V| and sends J to −J.

**Proof (sketch; the referee checked each law numerically).**
- Main's theta with characteristics is thc(a, b, u, T) = Σₙ e^{iπT(n+a)² + 2πi(n+a)(u+b)}. Two identities carry
  everything: thc(a, b + m, u, T) = e^{2πiam} thc(a, b, u, T) for integer m, and thc(a, b − 2a, u, T + 2) =
  e^{−2πia²} thc(a, b, u, T) (expand (n + a)² − 2(n + a)a = n² − a²). Also thc(a + m, …) = thc(a, …) (reindex n).
- **A:** each twist's b grows by 2q, so each theta factor gains e^{4πi q² a}. Every entry of main's bilinear, hence every
  residue R_s, gains the same e^{4πia(q_L² + q_R²)}; the prefactors e^{iπb} gain e^{2πiq} = 1, and the channel norms
  c_s are unchanged. Y = coupling(S, Σ u_s E_s) is linear in the weights u_s = √(2πL + c_s)·R_s, so det Y (3 × 3) gains
  the cube.
- **N:** reindexing n → −n and thc's quasi-period give bil(−x, −y; −u) = −bil(x, y; u), so every residue and channel
  norm, and each Y, is unchanged.
- **T:** with w fixed the twists' b falls by 2qa and T = 2τ rises by 2, so each theta gains e^{−2πiq²a²}; the prefactor
  e^{iπb} loses e^{2πiqa}, which cancels the shift of the u + τ argument by 1; and θ₁(u|τ + 1) = e^{iπ/4}θ₁(u|τ). The
  four kernels gain e^{−2πia²(q_L² + q_R²)}e^{iπ/4}, with (P_j, P_k) → (P_k, −P_j), B1724's ρ(T) on the channels, and the
  channel norms follow (c_j ↔ c_k: the same regularised integral over the (1, τ + 1) parallelogram). The Higgs moves by
  the same rotation with its own phase, which enters conjugated in S̃. Altogether Y(Tx) = c·P Y(x) Pᵀ with
  P = [[0, 0, 1], [0, 1, 0], [−1, 0, 0]] and det P = 1, so det Y gains c³.
- **M:** thc(a, −b, −ū, −T̄) = conj thc(a, b, u, T) and θ₁(−ū | −τ̄) = −conj θ₁(u | τ), so the mirror bilinear at −ū is
  −conj(Σ₃ bil Σ₃), Σ₃ = diag(1, −1). The directions' QI and QJ components have real q-series coefficients and their QK
  components imaginary ones, so a(−τ̄) = (ā_I, ā_J, −ā_K). Together Y(Mx) = D Ȳ(x) D with D = diag(1, 1, −1), so each
  sector's arg det Y changes sign.

**Check (1)** (version 2; 14 lines of orders 2 and 5–12, none on slope 2/5; τ = 0.13 + 2.2i, −0.27 + 2.6i,
0.41 + 1.7i; DR, a₀, F₋₁₀, F₆, F₂₂; both radius rules; all four readings; 1 680 rows):
- A: arg det Y_u − 204πa within 2.2 × 10⁻⁹, arg det Y_d − 60πa within 1.7 × 10⁻⁹; P within 4.1 × 10⁻⁹; N within
  6.5 × 10⁻⁹.
- T in (S̃, S) and (S, S̃): θ_Y's shift + 132πa² + π/2 within 7.4 × 10⁻⁹, every direction. In (S, S) the constant left
  after −132πa² is π for DR and a₀ and π/2 for the three F_a; in (S̃, S̃) it is 0 and π/2. Each is constant across lines,
  τ and radius rules to 3 × 10⁻⁹ π. The formula gives these: 3π/2 ± 6φ with φ = π/4, or πa'/4 for a' ≡ 2 (mod 4).
- M: θ_Y(Mx) + θ_Y(x) within 3.3 × 10⁻⁹. M keeps each reading pair (masses to 8 × 10⁻¹⁵); with (S̃, S) and (S, S̃)
  swapped the masses differ by at least 6.8 × 10⁻⁸.
- The masses, |V| and J move by at most 6 × 10⁻¹¹ under A, P, N and T; under M the masses and |V| by 3 × 10⁻¹¹ and
  J(Mx) + J(x) by 6 × 10⁻¹⁵.

**An instrument remark, already on record (check (0)).** Main's F_a (`cm_zero_line.direction`, and B1810's copies in
symmetry_selection_table.py and referee/rf_common.py) take θ₂ from mpmath's `jtheta` at q = e^{iπτ}, with the principal
branch of q^{1/4}. On 1 < Re τ ≤ 3 that branch differs from e^{iπτ/4} by −i (period 8 in Re τ), which flips the sign of
F_a's QI component for a ≡ 2 (mod 4), every F_a on the menu, on 1 < Re τ ≤ 3 (mod 4). The record has this: B1634 § 2,
B1674 (W101's control C1; its main check confirmed the cause), B1824, B1823 (whose model sums θ₂ in τ), and B1821's
evaluator guard ("the F_a sections are exact only for ∣Re τ∣ < 1"), which B1825's census enforces ("a guard refuses
|Re tau| >= 1"). Version 1 of this check is one more computation that left the strip; version 2 sums θ₂, θ₃ and θ₄
from their series. Check (0): at the three τ, main's F_a and the series' agree exactly; at τ + 1 they differ by 2.0
(F₋₁₀), 3 × 10⁻² (F₆) and 10⁻⁶ (F₂₂) relative, and only the series' F_a obey the T law (to 3 × 10⁻¹⁵). DR and a₀ as
main builds them obey it to 2 × 10⁻¹⁶.

## 2. The ambiguity (Corollary 2)

The relabellings T^k A^m fix every mass, angle and J and move θ_Y by k(−132πa² − π/2) + 264πam (in (S̃, S)). These
shifts form the subgroup of ℝ/2πℤ generated by 264πa and 132πa² + π/2: cyclic, of order N = lcm(ord 132a,
ord(66a² + ¼)) in ℚ/ℤ. P and N change only the slope's representative and give nothing new. **So, in the Standard Model's
reading, θ_Y is a function of the physical point only modulo 2π/N.** From check (2), exact:

| slope a | N_A (b → b + 1) | N_T (T) | N |
|---|---|---|---|
| 0, 1/2 | 1 | 4 | 4 |
| 1/3, 1/6 | 1 | 12 | 12 |
| 1/4 | 1 | 8 | 8 |
| 1/5, 2/5, 1/10, 3/10 | 5 | 100 | 100 |
| 1/7, 2/7, 3/7 | 7 | 196 | 196 |
| 1/8, 3/8 | 2 | 32 | 32 |
| 1/9, 2/9, 4/9 | 3 | 108 | 108 |
| r/11 | 1 | 44 | 44 |
| 1/12, 5/12 | 1 | 24 | 24 |

On the candidate family's slope 2/5, θ_Y means something only modulo 2π/100 (3.6°); b → b + 1 alone gives the record's
2π/5. A "stated representative" (P-323's other option) gives one of N values on each slope.

**θ_Y is already on record, each in one representative, at seven addresses of the family's slope off the mirror's fixed
set:**
- e20's F2 (rows 1411 and 1414; the relay of 2026-10-27, lines 113–115): (2/5, ½) at 0.35 + 3.05i, 0.55 + 3.05i
  (B1726's row) and 0.85 + 3.05i, and (2/5, 1/10) at 0.3145 + 3.0345i;
- P-323's four post hoc read-outs (rows 1439 and 1443; W168 reproduced all four): B1726's and B1749's (2/5, ½) rows at
  0.55 + 3.05i and 0.6053 + 3.0259i, and B1786's (2/5, 23/30) row at 0.2692 + 3.0375i with its mirror (2/5, 5/6) at
  0.7308 + 3.0375i.

e20's F4 also prints θ_Y at Re τ ∈ ½ℤ on the ten (2/5, k/10) lines at Im τ 2.2, 2.6, 3.03 and 3.4, off the fixed set on
the eight with b ∉ {0, ½}. P-323's census stores, unread, what fixes it at 78 points on each of the forty lines of
slopes 2/5 and 3/5 in its scope (the second referee's count). By Theorem 1 each recorded value fixes θ_Y at every
relabelling and mirror image of its address. Every candidate row is on record or within 0.03 of a record on its line or
its mirror image: B1753's (2/5, ½) row at 0.6 + 3.0397i is 0.015 from B1749's; B1753's (2/5, 1/10) row at
0.3333 + 3.0368i is 0.019 from e20's 0.3145 + 3.0345i, and B1749's at 0.3333 + 3.0551i is 0.028 from it. The seat
located these rows by their addresses only. It neither reduces those numbers nor adds θ_ct (§ 3) to them: either would
be a further look at P-585's held-out target.

## 3. What CP fixes, and what it does not (Theorem 3)

**The fixed set.** M x is a relabelling of x exactly when Re τ = −k/2 (k ∈ ℤ) and either
- 2b ≡ ka (mod 1), where M x = T^k A^m x; or
- 2a ∈ ℤ and ka ∈ ℤ, where M x = T^k A^m P^{2a} N x for every b: slope 0 at every Re τ ∈ ½ℤ, slope ½ at every
  integer Re τ.

By Theorem 1, θ_Y ≡ 264πab + 132πa² Re τ − (π/2) Re τ (mod π) on the first family and 132πa² Re τ − (π/2) Re τ (mod π)
on the second; at a = ½ the two differ by 132πb. J = 0 on both, since J is odd under M and invariant under the
relabellings: this is the "if" half of P-328's rule ("exactly when", 96/96), here on every Re τ ∈ ½ℤ.

**Theorem 3.** Let θ̄ = θ_Y + θ_QCD, with θ_QCD any rule on the labels such that θ̄ is invariant under A, P, N and T and
odd under M. Then θ̄ ∈ {0, π} on the fixed set. Off it, nothing: the difference of two such rules is a CP-odd invariant,
and any CP-odd invariant may be added. J itself is one (θ̄ + λJ for any real λ), and so is 2πc Re τ for any integer c.
The class also contains the tuned rule θ_QCD = −θ_Y, which gives θ̄ ≡ 0 everywhere: admissibility alone predicts nothing.
- Proof: at a fixed point, with g the relabelling that M matches, θ̄(x) = θ̄(g x) = θ̄(M x) = −θ̄(x).
- **So the frame's CP fixes θ̄ only where it also kills J.** At a J ≠ 0 address the value of θ̄ is the rule's. The
  candidate family's best rows (Re τ ≈ 1/3, 0.6, 0.605, 2/3; B1749, B1753) are off the fixed set, so CP fixes nothing
  there.
- **A compensating rule.** θ_QCD = θ_ct = −264πab + (π/2 − 132πa²) Re τ for 0 ≤ a < ½, and θ_ct = (π/2 − 33π) Re τ at
  a = ½, where the A anomaly 132π vanishes mod 2π so no b-term is needed (the second referee's form; kept with the
  b-term, it would be consistent at a = ½ only where 132b ∈ ℤ). It cancels the A and T anomalies, is even under N and
  odd under M, and equals −θ_Y (mod π) on both fixed families. It is not invariant under P, so it needs the slope's
  representative fixed (0 ≤ a ≤ ½ by P and N).
  - Along each line θ_ct is −arg G up to a constant, with G = e^{−i(π/2 − 132πa²)τ} holomorphic and zero-free: a
    P323_RULE counterterm. It restores invariance under the relabellings; on S232's NOT HARMONIC combinations it cannot
    make θ̄ constant along a line, and nothing here asks it to.
  - Its terms −264πab − 132πa² Re τ are minus the phase of the characteristic prefactors. thc(α, β, u, T) =
    e^{iπα²T + 2πiα(u + β)}θ₃(u + αT + β | T); with α = qa, β = 2qb and T = 2τ, the factors e^{iπα²T + 2πiαβ}, cubed in
    each sector and multiplied over the four fields, have phase 132πa² Re τ + 264πab. Its term (π/2) Re τ is fixed only
    up to 2πc Re τ.
  - Check (4), at (1)'s points in (S̃, S), with the b-term form throughout: θ_Y + θ_ct changes by at most 1.9 × 10⁻⁹
    under A, 2.2 × 10⁻⁹ under T and 3.6 × 10⁻⁹ under N; θ̄(Mx) + θ̄(x) is within 6.8 × 10⁻¹⁰; on (3)'s fixed points (all
    of the first family) θ̄ ≡ 0 (mod π) within 4.6 × 10⁻¹²; and P moves it on all 420 rows.
  - θ_ct is not evaluated here at any address where θ_Y is on record; with it, θ̄ there would be one addition. Once this
    note is on main, θ̄ under θ_ct at every address of § 2 is one addition from main's own ledger (row 1443 prints four
    of the values): if θ̄ is kept anywhere on a card, those count as looks (m_V).
- A stated representative is a rule too, and an invariant one, but in general it is not odd under M: bringing M x back
  into the representative's domain costs an anomaly. It breaks CP by hand.

## 4. The modular route (P-461's FPST half)

FPST's θ̄ = 0 needs det(M_u M_d) to be a modular function of total weight zero, so constant, and real by CP. A necessary
condition in this frame is a T-invariant θ_Y.
- In (S̃, S), and in (S, S̃), the T shift −132πa² − π/2 vanishes nowhere. If 66a² + ¼ = n then 264a² = 4n − 1 is odd;
  with a = r/s in lowest terms s² divides 264, so s ∈ {1, 2}, and 264r² or 66r² is even. Check (5) confirms it on all
  48 678 slopes with s ≤ 400. Nor is the shift a multiple of π: 132a² + ½ ∈ ℤ needs 264a² odd, which fails the same way.
- The A shift vanishes only where 132a ∈ ℤ (s | 132; 132 slopes with s ≤ 400).
- In the readings outside the Standard Model's the constant differs (Theorem 1): with DR or a₀, (S, S) gives
  −132πa² + π, which vanishes on slope ½, and (S̃, S̃) gives −132πa², which vanishes on slope 0. Both A shifts vanish
  there too.
  Those two cases are T- and A-invariant; whether their det is τ-independent is S232's harmonic question (its H1b
  classed none of DR's combinations in those readings HARMONIC, its eight being F₋₁₀'s; a₀ was outside its scope).
- **So in the Standard Model's reading FPST's route is closed on every line, for every direction.** This is a necessary
  condition failing; S232's non-harmonic θ_Y is the stronger, continuous statement, on the combinations it classed.

## 5. What it changes

- **FL-16 and P-323.** FL-16's "θ̄ is a nineteenth unknown" holds as a theorem of the frame as built. With a
  CP-respecting θ-term rule θ̄ is fixed (to 0 or π) exactly on the mirror's fixed set, where J = 0, and elsewhere it is
  free. P-323's question — which (reading, Higgs, line) makes θ_Y identically 0 or π with J ≠ 0 — has no
  rule-independent answer.
- **P-569.** The det-real locus arg det(Y_u Y_d) = 0 depends on the labelling: relabelled, it becomes a locus θ_Y = s
  with s a nonzero element of the ambiguity group (2π/N)ℤ, a different curve. Its rule-independent form is the mirror's
  fixed set, where J = 0. So it cannot "fix Re tau and predict ∣J∣" without a chosen rule, and it cannot kill the J ≠ 0
  addresses either, since a CP-odd invariant rule reaches any value there.
- **P-585.** At the family's best rows θ̄ is a function of the rule chosen. θ_Y is already on record at B1749's address
  and within 0.03 of every other candidate row, on its line or its mirror image (§ 2), so a rule sealed now is sealed
  after θ_Y is known there. Since θ̄ − θ_QCD = θ_Y, choosing the rule there is choosing θ̄, and no rule sealed now meets
  GAP1 v1.60's condition 2 ("no function of it was used in building, choosing or tuning F"). A level-2 card can keep θ̄
  as a held-out target only at a frozen address with no θ_Y on record at it or at any relabelling or mirror image of it,
  with the rule (labelling and θ term) sealed before any θ_Y is computed there, typed CHOSEN and counted among its
  searched bits (P-576); even then a pass would grade the rule, not the frame. P-585's card is frozen on the family's
  candidate (B1829), and no candidate row is clear of a record within 0.03. S298 adds a further prior look at θ̄ on the
  strip (the agy audit lane's, row 1539).

## 6. What it does not show

- No θ̄ at the candidate family's addresses, and no measured value.
- The closed forms are proved in sketch from thc's identities and checked on 14 lines (none on slope 2/5), three τ, five
  directions, both radius rules and four readings. The fixed-set formula is checked on 12 points of the first family
  off slope 2/5; the second family (slopes 0 and ½) rests on the two referees' checks.
- The class of admissible rules is fixed by invariance and CP alone. A stronger principle could narrow it. Along each
  line θ_ct is −arg G up to a constant with G holomorphic and zero-free, a P323_RULE counterterm: on the 98% of
  combinations S232 classed NOT HARMONIC, neither θ_ct nor any other such counterterm makes θ̄ constant along the line.
- S, and relabellings that change the radius rule, are not considered.

## Proposals (main's to take or leave)

- **FL-16, P-323:** record Theorem 1's closed forms, Corollary 2's order and Theorem 3. P-323's question is answered: no
  rule-independent θ̄ with J ≠ 0.
- **P-585:** drop θ̄ from the family's held-out targets and grade it as an input (FL-16). The card is then left with one
  clean held-out target, y_b/y_t, against GAP1 v1.60's "two at least" (B1829): it needs y_τ/y_b made clean by a forced
  scale (P-574), or another held-out quantity. Sealing a θ-term rule first (typed CHOSEN and priced, P-576) would be open
  only at an address with no θ_Y on record at it or at its relabellings and mirror images; the family's candidate rows
  do not offer one (§ 2). Once this note is on main, θ̄ under θ_ct at every address of § 2 is one addition from main's
  own ledger: if θ̄ is kept anywhere on the card, those count as looks (m_V).
- **P-569:** re-scope it to the mirror's fixed set (J = 0), or attach a rule to it.
- **P-461:** its FPST half is answered negative for the frame as built, in the Standard Model's reading, on every line
  (§ 4): a necessary condition fails. Its Dabholkar–Hull half is untouched.
- **The instrument:** nothing to add to B1821's guard; version 1 of this check is one more computation that left the
  strip.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE STRONG ANGLE NEEDS A RULE (the θ̄ card's first step; theta_rule_check.py version 1 ba981b3e8 → eb876fb39, version 2 2e545afc4 → e40d0fb19) | "θ̄ is therefore an input (FL-16) until main chooses a rule" | `relays/CHAT1_TO_CC_2026-11-03_THE_STRONG_ANGLE_NEEDS_A_RULE.md` @ the commit adding it | — | P-323, FL-16, P-569, P-585, P-461, P-328, B1671, B1674, B1724, B1786, B1821, B1829 | 2026-11-03 |

0 of 19.
