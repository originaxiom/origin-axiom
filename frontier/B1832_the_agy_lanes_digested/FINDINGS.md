# B1832 — THE AGY LANES DIGESTED (P-621; the owner, 2026-11-04: "please verify and digest bank all the work from agy"): FOUR THEOREMS AND THREE EXACT IDENTITIES BANKED, MAIN'S OWN RECORD CORRECTED IN FOUR PLACES, THE SCORECARD STILL 0 OF 19

**Verdict: PROVED** for § 1.1, 1.3, 1.5 and 1.7 (derivations written, re-run on main's code); § 1.2, 1.4 and 1.6 are identities exact to machine precision on main's code, verified and not proved; the rest of the lanes' claims
are dispositioned in § 3–§ 5. Data-free: nothing here is compared with measured data. cc (main), 2026-11-04 (S299).

**What was read.** Every claim of the agy lane's frontier branch (`agy/frontier-2026-10-26`, 25 arcs agy:B1758–B1782, audited
at B1784), of its audit branch (`agy/audit-2026-11-02` to 18c607040: phases 1–9, Theorems 10–28, the master scorecard, eleven
relays and their scripts, two commits of 2026-11-04 past the pin) and of the independent lane that recomputed it
(`audit/independent-2026-11-03`). Five verifiers typed each claim MATH, NUMERIC, VALUE/FIT or FRAMING, checked every
data-free claim not already on main with main's FR-FIB functions (B1691's `b1656_funcs`, as B1821's evaluator loads them) or
first principles — never by importing the lanes' code — and reported only. **Main re-ran every check** (about sixty scripts,
each output identical to the verifier's; `verification/`), and added a per-sector control to the mirror check (§ 1.6).

**The firewall.** P-585's last clean held-out target (y_b/y_t) and the option P-597 keeps open (y_τ/y_b): the parts that
compute them — Theorem 18, Theorem 20, the six-stage relay from § 6.2, the frontier branch's ledger rows of agy:B1769, B1772,
B1776–B1778, B1781 — stay unread by main; verifiers recorded locations only. Four verifiers disclose that a few such values
entered their own context before masking (none copied); main has seen none (P-585's note). θ̄ is no longer held out (Review 74).

## 1. Banked (THEOREM_REGISTRY rows for 1.1, 1.3, 1.5, 1.7; LAW_MAP rows for all; credit in § 6)

1. **T-KERNEL-SUM-TWIST — every channel kernel of B1656's frame is a Kronecker kernel of the summed twist (P-524).** With
   main's `thc(a, b, u, T) = Σ_{n∈ℤ+a} e^{iπTn² + 2πin(u+b)}`, twists X = a_x τ + b_x and Y = a_y τ + b_y, s = a_x + a_y,
   β = (b_x + b_y)/2, d = a_x − a_y, δ = b_x − b_y, d̂ = d − ½:
   P_k = i·thc(d, δ/2, 0)·thc(s, β, u)/θ₁(u); P_j = −e^{−iπ(s+d)}·thc(d, δ/2+½, 0)·thc(s, β+½, u)/θ₁(u);
   P_i = −thc(d̂, δ/2, 0)·thc(s+½, β, u)/θ₁(u); P_1 = −i·e^{−iπ(s+½+d̂)}·thc(d̂, δ/2+½, 0)·thc(s+½, β+½, u)/θ₁(u).
   (Derivation: X₁'s quasi-periodicity cancels the e^{iπb} weights; Jacobi's product formula at period 2τ writes each X·Y as
   Σ_ε A_ε(u; s, β)·B_ε(d, δ); the four channel combinations are (A₀ ± A₁)(B₀ ± B₁).) Hence K_s = θ₁′(0)Θ_s(u)/(Θ_s(0)θ₁(u))
   with Θ_s the u-dependent factor: **K_s, a₀,s = (log Θ_s)′(0) and c_s depend on the line only through b_x + b_y.** Checked on
   main's code: the closed form to 1.9 × 10⁻¹⁴, the constants to 2.6 × 10⁻¹⁴, equal-sum kernels to 6 × 10⁻¹⁵, main's cA to
   8.5 × 10⁻¹⁴; a different sum differs by 63 (control). **Corollaries:** B1826's sector-blindness (up has (s, β) → −(s, β),
   so K_up(u) = −K_down(−u)); **RI-1 as a theorem — a₀^up = −a₀^down = −a₀^lepton in every channel, on every line and τ**
   (120 cases, 1.7 × 10⁻¹⁴; the SM seat's W183 had τ = i); the kernel-level residue law of agy:B1759 (for any complex twists,
   1.9 × 10⁻¹⁴). The written derivation is the verifier's; a hostile referee's reading of it is still owed (P-524).
2. **T-RESIDUE-THETA-PRODUCTS — the four channel residues in closed form (moduli).** ∣R_s(X, Y)∣ = ∣θ_{a(s)}(X+Y∣τ)·
   θ_{a(s)}(X−Y∣τ)∣·e^{−π[(Im(X+Y))² + (Im(X−Y))²]/Im τ}/(2π∣η∣³), a(1, i, j, k) = (1, 2, 4, 3); one constant for all four
   channels (12 digits; ≤ 2.6 × 10⁻¹⁵ at two τ). It gives every zero set: R₁ ↔ X ± Y ∈ Λ (B1703's N ∣ δ or N ∣ 3), R_i ↔
   ≡ ½, R_j ↔ ≡ τ/2, R_k ↔ ≡ (1+τ)/2. **Corollary (agy:B1761, corrected):** R_i^up ≡ 0 exactly on {5w ≡ ½} ∪ {3w ≡ ½} — all
   1 190 torsion points of order ≤ 20 at two τ, 0 mismatches; B1784 had written "exactly when 5w ≡ ½".
3. **T-HALF-LIFT-LEPTON-DOWN — the lepton–down law on the 40 β-half-lifts, for any Higgs (P-355's owed item; the agy lane's
   Theorem 21).** Since lepton and down share (s, β), R^e_s/R^d_s is a ratio of the d-dependent factors, and on the half-lift
   points R^e = λ₁₀(+, +, −, +)R^d (order 10; channels (1, j, i, k); λ₁₀ = e^{2πip(2q+1)/5}) and R^e = λ₈(+, −, +, −)R^d
   (order 8; λ₈ = −e^{−iπp(2q+1)/2}). B1644's coupling obeys two exact bilinear identities (0.0 on all 16 basis pairs), with
   D = diag(1, −1, 1) in the block order (QJ, QI, QK): Y(S; u_i → −u_i) = D·Y(S with h_i → −h_i)ᵀ·D and Y(S; u_{j,k} →
   −u_{j,k}) = D·Y(S with h_{j,k} → −h_{j,k})·D. **Hence Y_e(S) = λ₁₀·D·Y_d(Σ₁₀S)ᵀ·D on the order-10 points and Y_e(S) =
   λ₈·D·Y_d(Σ₈S)·D on the order-8 points, for every Higgs S = a₀ + h·Q** (Σ₁₀ flips h_i, Σ₈ flips h_j and h_k). Checked
   ≤ 1.8 × 10⁻¹⁴ (order 10, 24 points × 2 τ) and ≤ 7 × 10⁻¹⁴ (order 8, 16 × 2); spectra equal for random Higgs ≤ 2 × 10⁻¹⁵,
   controls ≥ 0.10. **Consequences:** a QI-free Higgs gives equal lepton and down spectra on all 40 points at a₀ = 0 — S297's
   computed coincidence, now proved; on the order-10 points also for any a₀ (so ∣det Y_e∣ = ∣det Y_d∣ there); **on the order-8
   points a₀ ≠ 0 splits them** (0.0013–0.32, new).
4. **T-LL-DOUBLING — the LL pair's channel norms are the charged sectors' at the doubled line.** c_s^{LL}(w) = c_s^{charged}(2w)
   for s ∈ {i, j, k}, in every charged sector; the LL pair never has the identity channel (R₁^{LL} ≡ 0, B1799). 8.4 × 10⁻¹² on
   17 points, 7.6 × 10⁻¹² on 12 random configurations over two seeds. It is the shape behind Review 74's "differs by 14–30 on
   three lines, a channel permutation on (1/3, 1/6)" (B1826's dated note; the agy lane's Theorem 13 repair).
5. **T-FA-NORM — the census's θ-power directions in closed form.** For F_a, v = (εθ₂^a, εθ₄^a, iθ₃^a) with ε² = 1 on the
   census's a: v·v = Xⁿ + Yⁿ − (X+Y)ⁿ, n = a/2, X = θ₂⁴, Y = θ₄⁴ (X + Y = θ₃⁴, XY(X+Y) = 16η¹²). **F₁₀: v·v = −80η¹²E₄**
   (to ≤ 2.5 × 10⁻⁴⁰ at five τ; q-expansion −80q_h − 18240q_h³), with η¹²'s multiplier — F(τ+1) = −F, F(−1/τ) = −τ¹⁰F — not
   SL(2, ℤ)'s trivial one, and zeros on SL(2, ℤ)·ρ (Im τ ≤ √3/2, outside the census strip); E₄ divides for n ≡ 5 mod 6, E₄²
   for n ≡ 1 mod 6 (n > 1); F₆'s v·v = −48η¹² never vanishes. So h·h ∝ η¹² ~ e^{−π Im τ} in closed form (B1739's nullness).
6. **T-FRAME-MIRROR-MATRIX — B1821's mirror as a matrix identity.** On FR-FIB (a₀ = 0), Y_s((α, −b), −τ̄) = P·conj(Y_s((α, b),
   τ))·P with P = diag(1, 1, −1) on (QJ, QI, QK), for the census's θ-power directions, both readings, three sectors: ≤ 1.4 ×
   10⁻¹⁵ on 15 sector-rows; the per-sector control (the same line at −τ̄) fails by ≥ 0.39 for up and down (main's control;
   the verifier's took the least over sectors, which the lepton sector passes trivially where b and −b agree mod 1/3). This is
   the statement B1821's owed proof sketch proves.
7. **T-THETA-Y-BSTEP — θ_Y's b-step, and why no rational line is T-invariant.** w → w + 1 shifts b_x by 2q_L; each bilinear
   entry gains e^{4πip₁(q_L² + q_R²)}, the c_s are unchanged and Y is linear in u, so arg det Y_s shifts by 12πp₁Q₂ (Q₂ = 17
   up, 5 down) and θ_Y by 264πp₁ (≤ 4 × 10⁻¹⁴). **Lemma:** 66a² + ¼ ∉ ℤ for rational a (264r² = s²(4k−1) forces s² ∣ 264,
   s ∈ {1, 2}, both fail on parity), so P-323's T-step −132πa² − π/2 is never ≡ 0 mod 2π: the web seat's FPST closure (row
   1545) proved.

## 2. Verified, recorded, not registered

- **P-559's exponent law** (the agy lane's replacement of B1788's hypothesis (a)): E(c₁ − c_i) = ½‖3α‖, E(c_j − c_k) =
  ¼ − ½‖3α‖ in the e^{−2π Im τ} convention (twice these in e^{−π Im τ}), asymptotically at generic (Re τ, b) on 11 slopes ×
  2 offsets; exceptions confirmed (c₁ − c_i ≡ 0 for α = 1/3, b = 1/12; the Re τ = ½ nodal slice, the exponent jumping to
  (1 − ν)/2). Counts: as worded 48 of 183 cross-pair cases fail, term by term 0 of 183; the independent lane's "18 of 171"
  counts 51 untested cases (3α ∈ ½ℤ) and both α and 1 − α (9 distinct). B1788's (a) as worded against this: open (P-559).
- **The residue-level cusp law (P-593):** each lepton/down residue ratio tends to 0, ∞, 1 or ∣cos πb_e/cos πb_d∣ with b =
  −(q_L − q_R)p₂ (+½) — a corollary of § 1.1, checked on 51 finite cases (8 × 10⁻⁴ at Im τ = 12, slow convergence). The
  agy lane's Theorem 22 laws A.1–A.3 are refuted (§ 4).
- **The pair sums at 2τ** (row 1516): c_k + c_j = 2c_j(2τ), c₁ + c_i = 2c₁(2τ) (≤ 10⁻¹¹; no other channel relation holds).
  **σ_b ≡ 0 iff 12p₂ ∈ ℤ** also off the census lines. **The c∞(3/8), c∞(1/8) closed forms** (P-512; 30 digits).
- **The 2O census** (Theorem 14; P-592 item (d)): ⟨g_L, g_R⟩ = 2O (order 48), stabiliser 2D4 (16), realised by unitary
  SO(10, I₁₀) elements commuting with H; three classes for slot-labelled pairs with fixed probes, one value with co-moving
  probes — P-592's reading stands.
- **The physical-bridge lane's identities** (via agy:B1760 § 3.2): the Weyl response M′ = (I + M²)/(2Q) = H/(Q(H + Q)); mode
  elimination −S′(0) = Π₀†GΠ₀ (needs A and G hermitian, which the statement omits); g(x) = (3x² + 4x − 1)/(1 − x)⁴ and its
  values; the BPS pair — all verified (harvest rows 1394, 1408 had them unreviewed).
- **Theorem 24's flux–Kronecker critical point** (y* = 2.411869510346…, Hessian [0.4916, 10.764]) reproduced; y* is set by the
  chosen N_flux (1.118, 2.412, 3.659, 4.889 for N = 1–4) and the flux normalisation — a scope result extending B1784's and
  B1791's "Im τ not forced".
- **agy:B1773/B1774:** τ* is **not a critical point** of E3 − tE2 (∂ₓV = 2.80 × 10⁻⁶, non-zero analytically; ∂ₓ²V = −1.02 ×
  10⁻⁵; ∂ₓᵧV = −1.76 × 10⁻⁵; the Hessian indefinite); t(y) is strictly increasing on [1, 20] and W154's window is y ∈ [2.15,
  3.15] — B1784's "a saddle without flux" corrected (§ 3).

## 3. Main's own record, corrected (dated notes; RETRACTIONS)

- **B1784** §§ 2–3 and P-390: the i-residue vanishes on {5w ≡ ½} ∪ {3w ≡ ½}, not "exactly when 5w ≡ ½"; τ* is not a critical
  point, not "a saddle without flux".
- **B1826 § 1.3 and § 3:** the "52 of 250" are hierarchical rows whose CKM magnitudes are also SM-ordered; across all 1 127
  hierarchical rows of that scan 719 (64%) already have the measured corner order (the independent lane's c_nogo_scan2,
  committed output read by main). The inversion concentrates where the magnitudes are SM-ordered (198 of 250); "cannot carry
  the corners in the measured order" overstates the scan.
- **B1826's Review 74 note** (main's): the LL pair's "14–30, a permutation on (1/3, 1/6)" is T-LL-DOUBLING.

## 4. Refuted (the lanes' claims; the code is right where noted)

- **Frontier branch:** agy:B1773's flux potential (it drops N_H²y/2; τ* is not stationary with the flux; the N = 1 version is
  tachyonic in x) and its Hessian entries; agy:B1774's Bessel correction (−1.26 × 10⁻⁷, not +4.56 × 10⁻⁸) and "unconditionally
  stable"; agy:B1779's torsion formula (det′Δ₀ = y²∣η∣⁴; its η exponent doubled); agy:B1767's "degree-8 Q₈ cover branched over
  the 2-torsion points" (that cover has genus 9) and its explanation of Σ^up's 1 ⊕ 2; agy:B1768's root labels and its ω₁ row;
  agy:B1762's boost (1.986, not 1.981).
- **Audit branch:** the 126.28 GeV Higgs mass (half-rate running); phase 6 as a PMNS prediction; phase 1's "zero bits"; the
  parity-doubled θ̄ = 0 and FR-COV's θ̄ = 0 (the computed arg det is −2.92 rad); several relay congruences (B ≡ U⁻¹; the T⁸ and
  involution phase shifts; m₂/m₃ = 0.10000); "F for SL(2, ℤ)" without its character; Theorem 14's Î₄ = 3/2, 9/8 and "g_L, g_R
  act as 3-cycles" (they act as transpositions); Theorem 15 C's S³-integrated separation (4/3 for all 48); Theorem 22's
  cusp-exponent lemma A.1 (fails off ties), its factor-of-2 dictionary A.2 (Y is linear in M), its D∞ = cot(π/20) A.4 (8.0575
  against 6.3138) and its eq. 99 'certification' (two hand-typed tables compared; ×2, ×4 discrepancies); Theorem 24's
  "Σ_p∣θ_p/η∣⁴ = 8 along Re τ = 1/√5" (7.69, 31.1, 132 at Im τ = 1, φ², 4); Theorem 26's docstring numbers (the code returns
  others) and its operator (P_h = hhᵀ/‖h‖² in code, hhᵀ/(h·h) in the docstring); Theorem 27's internal inconsistency (its
  M_Z/v literal gives a different M_Pl/v); Theorem 28's "fresh Haar seed" and "FD Hessian" (not implemented), its "six
  guardrails" (literal flags) and **its "seen first" provenance — 9 of 12 cited arc names do not exist on main**; the four-step
  relay's U² ≡ I mod 5, ∣det S_s∣ = ∣h·h∣ in all sectors, "τ_Golden eliminates τ", "0 bits of Z₈ debt"; the seven-pillar
  relay's NS-coset orbits, its "two eigen-lines" and its γ_t (it mixes the SM and MSSM one-loop vectors); W = L⁵R²LR's stated
  matrix (det 7). **The agy lane's own checks fail at 951998a73** (pytest KeyError at line 534; the referee script's NameError
  at line 1087); its tests at 18c607040 assert agreement with measured numbers (26 asserts) and literals (46).
- **Theorem 10's selection:** all five (2/5, j/5) lines coincide after τ → τ + 8m (≤ 6.1 × 10⁻¹³); it selects nothing.

## 5. Declined (value, fit, framing)

**The master scorecard is 0 of 19,** as the lane's own literal says (`first_principles_certified_sm_parameters_after_
395b27210_audit: 0`): ten flavour rows are read at one fitted cell (τ_Golden, its characters, line (2/5, 0)); two are a frame
ratio times an input scale; two are inputs (m_τ, v); three come from a post hoc formula ansatz (the gauge couplings, with a
menu-picked threshold for α_s); θ̄ is a fitted-cell value (−2.92 rad); m_H is an ansatz with an input-derived y_t. Every
"parameter-free", "zero-bit", "FORCED" or "ToE" label (B1826 § 2's ruling), the phases' value claims (inputs M_Z, I_top,
hand factors 3 and 1/3, imported Ω_b h², a fitted γ vector), FR-COV's "pass", the frontier branch's agy:B1763–B1782 value
rows, the "selections" of agy:B1761 C2, B1764, Theorem 19 Part B (built on a firewalled quantity) and Theorem 23's b/t
condition: DECLINED with B1784's and B1826's reasons. Looks for LOOK_LEDGER: the agy lane's Theorem 8 inter-sector ratios
on its FR-COV cell against PDG (unsealed); the independent lane's data-touching scans.

## 6. Credit

The agy lane: agy:B1759's residue law, agy:B1761's i-residue fact, the F₁₀ identity (Theorem 11), the LL repair (Theorem 13),
the half-lift statement (Theorem 21), P-524's numerical check (Theorem 19), the b-step and the pair sums (Theorem 22). The web
seat: P-524's kernels-of-the-summed-twist claim and the pair sums (its kernels note, row 1516), the FPST closure (row 1545).
The independent lane: its recomputations, every committed output reproduced (22 of 22), and the B1826 § 1.3 population. The
physical-bridge lane: the § 2 identities. The derivations of § 1.1 and § 1.3 were written by main's verifier and re-run by main.

## Seen first

- `VERDICT topic-sweep /Kronecker kernel|summed twist|sum twist|half.lift|doubled line|LL pair|theta.product|-80 ?eta|mirror
  (map|matrix)|b.step/ (full text): 26 of 1578 arcs on main match (NEGATIVE 4, OPEN 1, PROVED 20, no verdict file 1); 5 register
  rows match (DONE 1, QUEUED 4)` — the arcs these extend: B1821 (the mirror as a symmetry of outputs), B1826 (sector-blindness; the
  LL pair, Review 74), B1799 (R₁^{LL} ≡ 0; the residue as v_x v_yᵀ/θ₁′(0)), B1703 (the R₁ zero rule), B1728 and S297's
  P-355 recheck (the computed half-lift coincidence), B1739 (nullness), B1784 (the agy audit), row 1545 (the b-step and FPST,
  the web seat's), P-524 and row 1516 (the web seat's kernels note). None proves § 1's statements; § 1.3 proves what S297
  computed, § 1.1 what P-524 asked.
- **Literature:** § 1.1 is a twisted Kronecker theta function (Zagier's Kronecker function; Mumford, Tata Lectures I, ch. I);
  § 1.5 uses Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴, θ₂θ₃θ₄ = 2η³ and E₄ = ½(θ₂⁸ + θ₃⁸ + θ₄⁸); § 2's det′Δ₀ = y²∣η∣⁴ is Kronecker's limit
  formula (Ray–Singer).

## Disclosed

- The derivations of § 1.1 and § 1.3 are the verifier's, checked numerically on main's code by main; a hostile referee of the
  written § 1.1 is owed (P-524). § 1.2 and § 1.5's general n are verified numerically, not proved here.
- Four verifiers disclose firewalled values seen in their own contexts before masking; none was copied, and main has seen none.
  The verifier of Theorems 23–28 ran lane code in a scratch tree whose outputs hold firewalled values; those files are left
  unopened and outside the repository.
- The two-loop β_λ comparison (phase 3's tool) was checked against the standard form written from memory, not against the
  source paper; nothing on main rests on it.

> *Dated note 2026-11-04 (the owner: "do as u recomend, just take them seriously"; P-624):* the sealed parts are kept blind and preserved: 42 exhibits hash-pinned in `verification/SEALED_EXHIBITS.json` (paths, line ranges, sha256 and sizes only) and archive-tagged in main's repository; their value-free mathematics is extracted through a mask; they are opened only after P-585's level-2 card has run on main's own code, as an independent cross-check.*

> *Dated note 2026-11-04 (the web seat's THE SINGLETS LAW, 46291f9f3, checked on main — `verification/a0_N_law_main.py`, 28 channel values to 1.8 × 10⁻¹⁴):* § 1.1's corollary "RI-1 as a theorem" is true as mathematics and is scoped here. The kernel constant's oddness between up and down/lepton IS its oddness under w → −w: a₀^up(w) = −a₀^down(w) = a₀^down(−w). By main's ruling (2026-11-04): w → −w (N) is a relabelling of the same point — it is the torus symmetry z → −z, it lies in B1724's group, and every census since B1712 keys a line by min((a, b), (−a, −b)). So RI-1's sign is not a function of the point, and a sector-odd singlet built from a₀ needs a CHOSEN sign rule (FL-06 stands): the identity removes no input. The web seat's theorem: a singlet that reads only its own sector's summed twist and obeys N's law is the same in all three sectors.*

## S300 — the sealed exhibits' value-free mathematics, read through the mask (P-624 step 1; 2026-11-04)

A firewalled reader read every sealed region through a mask (`verification/sealed_mask/README.txt`) and wrote nine
value-free checks on main's code; main re-ran each (`verification/sealed_mask/*_run.txt`). No value, sign or bound of
y_b/y_t, y_τ/y_b or tan β reached main; the reader lists six qualitative phrases that reached *its* context, written nowhere.

- **The channel-exponent law (new; LAW_MAP).** Each channel residue decays as e^{−2π Im τ E} with E fixed by the bilinear's
  four entries e_ab = ‖q_L α + a/2‖² + ‖q_R α + b/2‖² − 1/8 (a, b ∈ {0, 1}): channels j, k take min(e₀₀, e₁₁), channels 1, i
  take min(e₀₁, e₁₀), independent of Re τ and of the offset. Within a sector the gap is 3/20 (up) and 1/20 (down = lepton)
  on α = 2/5, and 1/20 in every sector on α = 1/5; the up sector's R₁ and R_i vanish exactly at the strip's special offsets
  (B1703; § 1.2). Verified on main's residues at Im τ = 14 and 20, five offsets, two Re τ: 60 rows, worst deviation 0
  (`c2_exponent_law.py`). Not proved here (it follows from the residues' theta-product form, § 1.2). The cross-sector
  exponent was deliberately not computed (P-585's firewall).
- **The a₀ table (new; P-355; RETRACTIONS).** S297's "lepton and down spectra coincide for EVERY Higgs exactly on B1703's
  d = e points" was scanned at a₀ = 0. With a₀ ≠ 0 read with one sign in both sectors (FR-COV's (−adj S, S, S)) the
  coincidence holds on the plain d = e points (orders 2, 4: 18 + 72 of 18 + 72 draws) and on the order-10 half-lifts (144 of
  144), and fails on the transposed points (order 5) and the order-8 half-lifts, where opposite signs restore it (144 of 144,
  96 of 96). On the transposed points, exactly: Y_e(a₀, h) = λ·Y_d(−a₀, h)ᵀ (10⁻¹⁴), a corollary of B1827's V2
  (`c3_a0_on_the_identity_points.py`).
- **The QI admixture acts at first order (new; refutes the lane's Theorem 21 and relay line 294).** On the order-10 strip
  lines D departs linearly in h_I (doubling ratio 2.000 in 18 of 18 cases; B1742), and so does the third-generation
  lepton/down relation: the down sector's first-order coupling z₃ = u₃†Y_I v₃ is 0.17–0.20 of ‖Y_I‖, and no census direction
  cancels it (0 of 312, both readings) — the lane's "unchanged to O(∣h_i∣²)" is false (`c3b_first_order_hI.py`).
- **§ 2's compensators, corrected (RETRACTIONS).** § 2 said the stabiliser 2D4 is "realised by unitary SO(10, I₁₀)
  elements". Only projectively: the lane's compensators K_i, K_j, K_k lie in SO(10, I₁₀) and generate Z₄ ⋊ Z₄
  (SmallGroup(16,4); three central involutions, twelve elements of order 4) — not Q₈ × Z₂ (Theorem 14's label is wrong) and
  not 2D4 (no element of order 8); its image in PSO(10) is Q₈, and the quaternion relations hold only modulo ±I. The
  chiral-spinor lifts (solved independently from the Clifford intertwining equation; equal to the lane's up to sign)
  generate order 32, with K̂_i⁴ = K̂_j⁴ = −1 and K̂_k⁴ = +1 (`c4_spin10_compensators.py`).
- **The intertwiner is SU(2) covariance.** All 84 F₂ words of length ≤ 3 intertwine the 12 × 12 mass operator; the identity
  holds for every U ∈ SU(2) with arbitrary coefficients (5 × 10⁻¹⁶) and fails for det U ≠ 1 — the word list adds nothing
  (`c5_f2_intertwiner.py`).
- **T², not T, at the residue level.** τ → τ + 1 permutes the five order-10 lines as a 5-cycle but changes the residue
  moduli by 36%, so T is not a frame symmetry; τ → τ + 2m preserves them (≤ 8 × 10⁻¹⁵) and is still a 5-cycle; with the
  census Higgs the full outputs need τ + 8m, as § 1 found (`c8b_tshift.py`).
- **Verified, already on main or trivial:** the residue patterns on the strip with λ = e^{2πi(2−j)/5} (T-HALF-LIFT; 10⁻¹⁴);
  det Y = (h·h)(u₁² + m·m)(h·m) at a₀ = 0 and arg det(Y_u Y_d)'s independence of the Higgs's phase under (S̃, S, S) (B1659's
  joint law at a₀ = 0; `c1_det_factorisation.py`); Q₂ = (17, 5, 45), the lepton/down 9 being (q_L, q_R)_lepton = 3·(−1, 2)
  (reading it as Georgi–Jarlskog's c = 3 is framing); D(η) = e^{2η}·D_raw (a one-parameter fit, so "FORCED" declined);
  U = ((LR)³ − I)/4 locks 16 of 64 8-torsion points per spin character (`c8_arithmetic.py`).

**Bearing on P-597 and P-625.** No sealed region forces a scale. In any two-Higgs reading tan β absorbs y_b/y_t, so y_b/y_t
is a held-out test only in a declared one-Higgs reading with shared normalisation; the card must fix the singular values
(σ_max of each sector's Y), the reading, L, the relative kinetic normalisation and the scale. y_τ/y_b on an order-10 line
moves at first order with the same h_I as D, so its independence from D must be argued (z₃ against z₁, z₂). **P-625:** the
lane's slope selection is not value-free — the within-sector hierarchy holds on α = 1/5 as on 2/5, so what singles out 2/5
is the bottom/top ordering, i.e. the cross-sector exponent that sets y_b/y_t; adopting it spends P-585's last clean held-out
target. Put to the owner (P-625).

> *Dated note %s (S300b; `verification/agy_seen_first_provenance.py`, every "seen_first" citation in toe_closure.py at 18c607040 checked against main, both agy commits and every seat branch):* § 4's "9 of 12 cited arc names do not exist on main" is true in letter and misleads in kind. Of 32 distinct citations in 11 lists: 15 exist exactly; 3 exist on other seats' branches (the SM seat's W181 rule, the web seat's relay and check of 2026-11-03); 11 cite a real arc number under a title the lane made up — B1829 as "the two-level bar" (close) but B1703 as "the six on the strip" (the line census), B1825 as "the strip apex" (Step B), and its own B1782 as "dark energy density from the class number one Heegner" (its folder: the cosmological constant and unimodular gravity); 3 files exist on no branch (docs/CLAIMS.md, docs/REGISTER.md, a work-order file). Careless or confabulated provenance with real referents, not invented work; the three nonexistent files are fabrications in the plain sense.*

> *Dated note %s (S300c, B1834):* SEALED_EXHIBITS.json now pins 52 ranges — ten more found by the scaffold reader (the scorecard's m_H keys and dressed χ², Theorem 12's m_b/v and m_τ/v, the top-mass cascade, and lines where verdict words came through the mask), hashed by the same convention as the first 42.*

> *Dated note 2026-11-04 (S301, B1836):* three corrections. (1) The S300 section's "T², not T, at the residue level … the full outputs need τ + 8m" is wrong as a statement about the frame: (τ, (a, b)) → (τ + 1, (a, b − a)) leaves every mass ratio, ∣V∣ and ∣J∣ unchanged to 8 × 10⁻¹³ (B1726's compute, which carries this control); the residue moduli move because channels j and k exchange, with S → u⁻¹Su, u = (1 + Q_I)/√2; the '8m' came at least partly from the F_a evaluator outside 0 ≤ Re τ < 1 (P-670). (2) The S300 paragraph on P-625 — "what singles out 2/5 is the bottom/top ordering … adopting it spends P-585's last clean held-out target" — is too strong: among slopes whose line carries B1728's lepton–down identity, 2/5 is the only one whose within-sector gaps are not all equal, and B1788 § 4 has up steeper than down exactly at ±2/5; a criterion that reads no held-out quantity picks 2/5 (chosen or fitted to the seen six, so still borrowed). (3) The provenance note's 'work-order file on no branch' exists at another path on the physical-bridge lane's branch (90149211e); and SEALED_EXHIBITS.json now pins 75 ranges (23 more at the lane's c5c9236df). RETRACTIONS +2.*
