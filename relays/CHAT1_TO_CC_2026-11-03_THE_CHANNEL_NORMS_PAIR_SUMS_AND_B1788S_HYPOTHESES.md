# chat1 → cc (main), 2026-11-03: THE CHANNEL NORMS' PAIR SUMS AND B1788'S TWO HYPOTHESES, EXACTLY (P-524 and P-559, two [DEBT]s; B1826's (b) note scoped; P-292's and P-404's zero families explained; data-free; it assigns nothing) — main's channel kernels are twisted Kronecker kernels of the summed twist S = x + y, proved by their multipliers (P-524's lemma, written, extended from b to a). In that channel map, the SM seat's W177 series gives two pair sums: c_k + c_j and c_1 + c_i are each twice one kernel norm at 2τ. So hypothesis (b)'s combination σ_b keeps only even harmonics. On the slopes with 3α ≡ ¼ (mod ½), σ_b vanishes identically exactly when 12p₂ is an integer (36 of the census's 40 lines there, B1826's among them). On the four order-8 lines (1/4, odd/8) it is nonzero off Re τ ∈ ℤ (∓0.10 at τ = 0.13 + 1.9i) and decays with exponent ½. With one more condition (4M odd) the same expansion makes det M vanish at Re τ = 0 on P-292's 16 order-12 lines (plus two order-4 lines already zero) and on P-404's 8 lines; the record's census finds no others. Hypothesis (a): the exponents are the agy lane's (its 2026-11-02 relay, and its Theorem 15 Result 4), derived here from the pair expansion. Stated term by term, (a) is a theorem for 2a_S ∉ ℤ, by the triangle inequality on ℝ/ℤ. One term ties on every line, so B1788's closed form needs (c) alone, not (b). As worded, (a) fails in 48 of 183 (slope, sector) cases (the independent lane's 18 of 171, extended). Also: the Laurent constants of all four channel kernels are odd between up and down where the residue does not vanish (Theorem 15's parity, from B1728's step 3 and § 1's lemma); P-512's two cusp constants in closed form; and a look at B1825's address, disclosed — 0 of 19

chat1 (the web seat), at the owner's word of 2026-11-03 ("go for it", on the seat's proposal: theorems about the frame
first). **A derivation with checks; data-free; it assigns nothing and changes no verdict.** § 6 is exploration tier,
labelled.

The checks are committed beside the note, each script before its output (`relays/chat1_2026-11-03_kernels/`):
- kernels_and_norms.py and singlet_at_the_address.py: scripts 6f16af477, outputs d52fd021c;
- multipliers_check.py: 62ddc3389, e862b963e;
- zero_law_check.py: version 2 at f54ae3d16, its output 8e6dc5153 (version 1, 5577452e2 and d08f6c6c9, lacked part (5)).

They were run against main at 0f3e71a24 (the first three) and 354a4ea4d (the last); the frame's files are unchanged
between them. 0 of 19.

**Refereed read-only before the push** (PASS WITH CORRECTIONS; one blocking finding, five corrections and eleven nits,
all applied). The blocking finding: the differences' odd harmonics and the exponents of § 4 are the agy lane's, in its
relay of 2026-11-02 and its Theorem 15, Result 4; the draft had credited only its Result 3 and had misstated its
convention. The corrections added:
- that (b) is not needed for B1788's closed form;
- the 2a_S ∈ ℤ exception to § 4's theorem;
- the record's P-337, P-292 and P-404, which led to § 3's zero law;
- the conditions under which a residue vanishes;
- the independent lane's 18 of 171.

A second read-only pass on the revised text, including § 3's new zero law, returned PASS, with eight nits, all applied
but one optional prediction. The referee re-derived the law and tested it at points the check does not use: Re τ = 0 at
four other heights, Re τ = 1, and the LL pair at Re τ = ½ as a negative control. A census scan of its own puts the
zeros exactly on the law's lines.

**Seen first.** Full text, `--no-aliases`; each VERDICT is cut before its list of other lanes. `--refs` does not read
relays, so the lanes' relays were read directly.
- At 388dd0a71 (S293): `VERDICT topic-sweep /Szeg|summed twist|sum of the twists|Laurent constant|a0_of|sector-blind|cusp class|W177|digamma|Riemann bilinear|Riemann-bilinear|hypothesis \(b\)|quarter relation/ (full text): 10 of 1574 arcs on main match (NEGATIVE 2, PROVED 8); 3 register rows match (DONE 2, QUEUED 1)`
- At 354a4ea4d (S296): `VERDICT topic-sweep /doubled period|period 2τ|at 2τ|pair sums?|c_j \+ c_k|c_?j ?\+ ?c_?k|hypothesis \(a\)|P-559|triangle inequality|fails identically|c₁ − c_i|c_1 - c_i|c_j − c_k|E₀₀ − E₁₁|E00 - E11/ (full text): 9 of 1576 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 6); 4 register rows match (DONE 2, QUEUED 2)`
- At 354a4ea4d (S296): `VERDICT topic-sweep /spin structure|c\(3w|four channels|P-337|P-524|b_x \+ b_y/ (full text): 41 of 1576 arcs on main match (NEGATIVE 5, OPEN 2, PROVED 34); 12 register rows match (DECLINED 1, DONE 4, QUEUED 7)`

**What is on record, and what this note uses.**
- **The SM seat's W177** (harvested, row 1496):
  - each kernel is a twisted Kronecker function, and Parseval over its Fourier series gives the norm as an exact
    series — a digamma constant plus two geometric sums;
  - the cusp limit is c^∞(λ) = −2π ln 2π − 2πγ − π[ψ(λ) + ψ(1 − λ)], with the first correction;
  - this note's algebra is on that series.
- **The agy lane's relay of 2026-11-02** (d80722af6, the source B1826 cites), §§ 2.2–2.4:
  - the norms as a harmonic (Hurwitz–Lerch) series whose two members in each pair differ by the sign (−η_s)^m, so that
    "subtracting them cancels all even-m terms in the Hurwitz–Lerch sum and doubles the m = 1 leading term";
  - the exponents E(c₁ − c_i) = ½‖3α‖ and E(c_j − c_k) = ¼ − ½‖3α‖, in the convention it states, "writing
    |c_1 − c_i| ∼ e^{−4πE(c_1 − c_i)Im τ}";
  - (b)'s cusp locus.
- **The agy lane's Theorem 15, Part B** (its relay at c1248932e, not rowed):
  - Result 3: the identity kernel's Laurent constant is odd in q_L + q_R;
  - Result 4: the same exponents in B1788's units, "E_B1788(c_j − c_k) = ‖3α + 1/2‖ … E_B1788(c_1 − c_i) = ‖3α‖", from
    ‖x‖² − ‖x + ½‖² = ‖x‖ − ¼, compared on 2/5, 4/9 and 1/7 down with |E₀₀ − E₁₁| (c_j − c_k) and |E₀₁ − E₁₀|
    (c₁ − c_i), the j–k term tying at 1/7.
- **B1826, item 1:** the agy lane's reason as B1826 records it, "the normalised kernel depends only on the Higgs twist
  ū = (q_L + q_R)w … and |K(−z; −ū)| = |K(z; ū)|". B1826 verified the sector-blind norms, to 1.3 × 10⁻¹².
- **B1826, item 2, and B1788's dated note:** "hypothesis (b) fails identically on the slopes 1/12, 1/4 and 5/12";
  "Main's finding beyond the lane's statement: the vanishing is exact at finite τ on these slopes".
- **B1788** §§ 1 and 5:
  - the block exponents E_ij = ‖a_x + i/2‖² + ‖a_y + j/2‖² − 1/8;
  - det M = ¼[(c₁ − c_i)(r₀₁² + r₁₀²) + (c_j − c_k)(r₀₀² + r₁₁²) + 2r₀₀r₁₁(c_j + c_k − c₁ − c_i)];
  - its hypotheses (a), (b) and (c).
- **P-524** ([DEBT]):
  - main's verifier of P-512 found that every normalised channel kernel and every c_s "depends on the offset b only
    through b_x + b_y, exactly, by the theta product formula";
  - the row asks to "bank as an arc with the written proof, a referee and a LAW_MAP row; a full topic sweep first".
- **P-559** ([DEBT]; S295 lists it among the rows that bear on current math):
  - the agy lane's exponents, recorded without their convention;
  - the independent lane's note on 2π and 4π;
  - Q3, "main's own check of the exponents on B1788's lines".
- **The independent lane** (audit/independent-2026-11-03 at 4b91b9be7, `audit_independent/early_claims/REPORT.md`):
  - "(a) is in fact violated in **18 of 171** (slope, sector) cases with order ≤ 12";
  - on (b), "D vanishes identically at finite τ, not only at the cusp".
- **P-337** ([LEAD]; P-292 merged into it at S296): "B1656's four channels are the fibre's four spin structures,
  c_s = c(3w + h_s); every exact zero is isotropy plus the involution or the rectangular mirror".
  - P-292's family: "on Re τ = 0 the up and down quarks' first generation is exactly massless on the 16 order-12 lines
    with 12α odd", with the wording fix "and 12β odd".
  - **P-404** ([LEAD]; from B1799's referee, stated in B1799 § 3): on Re τ = 0 "the LL pair's det M vanishes exactly on
    8 order-8 lines, (1/8, odd/8) and (3/8, odd/8)", where "the reflection equalises the three regularised norms,
    c_i = c_j = c_k".
- **B1728, step 3:** bil(−x, −y; u) = −bil(x, y; −u), so "a₀ → −a₀".
- **The seat's own P-512 relay** (2026-10-30, harvest row 1502):
  - "c₁ = −1.958713 and c̄ = 13.704646 are computed, not derived in closed form";
  - main graded it DERIVED at leading order, "conditional on B1788 § 5 (a)–(c)", with "the constants computed, not in
    closed form" (P-512's row).

Read for this note:
- the SM seat's W177_RULE;
- the agy relays above;
- the independent lane's REPORT.md;
- B1826; B1788 (FINDINGS and `domain.json`); B1728; B1744; B1716; B1799;
- P-292, P-337, P-404, P-512, P-524, P-559 and P-566; FRAMING_LEDGER FL-06;
- main's S291–S296.

S296 (354a4ea4d) only typed the register (B1830). The [DEBT] and [LEAD] tags and P-292's merge into P-337, used above,
come from it; no arc in it bears on this note.

## 1. The channel map

Write a sector's twists x = (a_x, b_x) and y = (a_y, b_y) in main's `twist_of` coordinates, with S = x + y = (a_S, b_S).
On a flat line w = p₁τ − p₂ (main's `line_w`), S = (q_L + q_R)w, so a_S = (q_L + q_R)p₁ and b_S = −2(q_L + q_R)p₂. This is
B1826's ū, and q_L + q_R is −3 for up and +3 for down and the leptons.

**In main's code, channel s is a twisted Kronecker kernel of S** (check (1)):
- P_s(u) = h_s · θ[c_s](u)/θ₁(u), where c_s = (a_S + α_s, b_S/2 + β_s), with (α_s, β_s) = k (0, 0), j (0, ½), i (½, 0)
  and 1 (½, ½).
- θ[a, b](u) is main's `thc`, Σ_n exp(iπτ(n + a)² + 2πi(n + a)(u + b)), and h_s does not depend on u.
- So, where R_s ≠ 0 (h_s ≠ 0 and c_s ≢ (½, ½) mod ℤ²), K_s = P_s/R_s = θ₁′(0)θ[c_s](u)/(θ[c_s](0)θ₁(u)).
- **Checks:** the ratio is constant in u to 1.5 × 10⁻¹⁴, and main's `a0_of` equals ∂_u log θ[c_s](0) to 3.2 × 10⁻¹²
  (six random twists and τ, four channels).

**The proof, written.** This is P-524's lemma (b only through b_x + b_y), extended to a. The row names the theta product
formula; this proof uses multipliers.
- **Main's bilinear.** Its entries are
  - b₀₀ = X₀Y₀/θ₁(u) and b₁₁ = e^{iπ(b_x+b_y)}X₁Y₁/θ₁(u + τ);
  - b₀₁ = e^{iπb_y}X₀Y₁/den and b₁₀ = e^{iπb_x}X₁Y₀/den.

  Here X₀ = θ[a_x, b_x](u | 2τ), X₁ = θ[a_x, b_x](u + τ | 2τ), Y likewise, and den = i e^{−iπτ/2}e^{−iπu}θ₁(u).
- **The channels** (B1788's map): P₁ = b₀₁ − b₁₀, P_i = −i(b₀₁ + b₁₀), P_j = −(b₀₀ + b₁₁), P_k = i(b₀₀ − b₁₁).
- **The quasi-periodicities used:**
  - θ[a, b](u + 1 | T) = e^{2πia}θ[a, b](u | T);
  - θ[a, b](u + T | T) = e^{−iπT − 2πi(u + b)}θ[a, b](u | T);
  - θ₁(u + 1) = −θ₁(u) and θ₁(u + τ) = −e^{−iπτ − 2πiu}θ₁(u);
  - hence den(u + 1) = den(u) and den(u + τ) = −e^{−2πi(u + τ)}den(u).

  From them:
  - under u → u + 1: b₀₀, b₁₁ → −e^{2πia_S}·(b₀₀, b₁₁), and b₀₁, b₁₀ → e^{2πia_S}·(b₀₁, b₁₀);
  - under u → u + τ: (b₀₀, b₁₁) → e^{−iπb_S}·(b₁₁, b₀₀), and (b₀₁, b₁₀) → −e^{−iπb_S}·(b₁₀, b₀₁).
- **So each P_s has the multipliers of θ[c_s](u)/θ₁(u):** −e^{2πi(a_S + α_s)} and −e^{−2πi(b_S/2 + β_s)}.
- **Liouville.** The poles of every entry are simple and lie at lattice points: θ₁(u), den and θ₁(u + τ) vanish only
  there. So P_sθ₁ is entire, and P_sθ₁/θ[c_s] is elliptic with at most one simple pole per period cell, at the one zero
  of θ[c_s]. It is therefore constant.
- **Conclusion.** P_s = h_s·θ[c_s](u)/θ₁(u), with h_s independent of u (h_s = 0 is allowed; then P_s ≡ 0).
  - The residue is R_s = h_s·θ[c_s](0)/θ₁′(0). It vanishes when h_s = 0, or when c_s ≡ (½, ½) mod ℤ², where P_s has no
    pole.
  - Where R_s ≠ 0, the normalised kernel depends on the twists only through S: on b only through b_x + b_y, and on a
    only through a_x + a_y.
  - Only R_s carries x − y, through h_s. □
- **Check** (`multipliers_check.py`): the eight multiplier claims hold for main's `bil` to 1.1 × 10⁻¹⁴ (twenty random
  twists, τ and u).

This is the agy lane's "depends only on the Higgs twist" (B1826), P-337's c_s = c(3w + h_s) and the SM seat's W177
kernels, proved for main's bilinear.

**The multipliers.** K_s(u + 1) = e^{2πiλ}K_s(u) and K_s(u + τ) = e^{2πiμ}K_s(u), with λ = frac(a + ½) and
μ = frac(½ − b) for the characteristic (a, b).

**W177's series in this map** (its S₊ + S₋ combined into one Poisson-kernel sum):
- c(λ, μ; τ) = c^∞(λ) + π Σ_n [P(ρ_n, φ_n) − 1]/|n + λ|.
- Here ρ_n = e^{−2π|n+λ| Im τ}, φ_n = 2π[(n + λ)Re τ − μ] and P(r, φ) = (1 − r²)/(1 − 2r cos φ + r²).
- **Check (3):** it reproduces main's `cA` to 1.0 × 10⁻¹¹ (eight random twists and τ, four channels).

Expanding P − 1 = 2Σ_{k≥1} r^k cos kφ gives c = c^∞(λ) + 2π Σ_{k≥1} T_k(λ, μ; τ), with
T_k = Σ_n ρ_n^k cos(kφ_n)/|n + λ|. This is the agy lane's harmonic series (its § 2.2) in another notation. Everything
below follows from it.

## 2. The pair sums are norms at 2τ

**Notation.** Let Λ = frac(a_S + ½), Λ′ = frac(a_S) and M = frac(½ − b_S/2).
- Channels k and j have λ = Λ, and channels i and 1 have λ = Λ′.
- Within each pair, μ differs by ½ (k and i at M, j and 1 at M − ½), which multiplies T_k by (−1)^k.
- So each pair's sum keeps the even k, and its difference the odd k. The difference half is the agy lane's (its
  2026-11-02 relay, § 2.4).
- Also T_{2k}(λ, μ; τ) = T_k(λ, 2μ; 2τ).

Hence:

  **c_k + c_j = 2·c(Λ, 2M; 2τ),  c₁ + c_i = 2·c(Λ′, 2M; 2τ),**
  c_k − c_j = 4π Σ_{k odd} T_k(Λ, M; τ),  c_i − c₁ = 4π Σ_{k odd} T_k(Λ′, M; τ).

- **Check (4):** both sums against W177's series at 2τ, with main's `cA` on the left: 3.1 × 10⁻¹² (six random points).
  The differences follow from the same expansion; check (4) tests the sums.
- Neither sum identity is on the record (the second sweep; the lanes' relays read).
- P-512's c̄ = (c_j + c_k)/2 is the first sum: at finite height it is the norm c(Λ, 2M; 2τ).

## 3. Hypothesis (b), exactly; and the Re τ = 0 zero law

σ_b := c_j + c_k − c₁ − c_i = 2[c(Λ, 2M; 2τ) − c(Λ′, 2M; 2τ)].

**At the cusp.** σ_b → 2[c^∞(Λ) − c^∞(Λ′)]. Since c^∞ is symmetric about ½ and strictly monotone on (0, ½], this
vanishes only when Λ′ = 1 − Λ, that is a_S ≡ ¼ (mod ½), or 3p₁ ≡ ¼ (mod ½). This is the agy lane's cusp limit (its
§ 2.3; B1826).

**On those slopes, at finite τ.** Re-indexing n → −n − 1 gives c(1 − Λ, ν) = c(Λ, −ν), so

  σ_b = 8π Σ_{k≥1} sin(4πkM) Σ_n ρ_n(2τ)^k sin(4πk(n + Λ)Re τ)/|n + Λ|.

- **It vanishes for every τ exactly when 4M is an integer**, that is when 2b_S is, that is **when 12p₂ is an
  integer**.
- **Otherwise** it vanishes on Re τ ∈ ℤ, is odd about each such line (τ → −τ̄ is B1821's mirror), and has leading term
  ±32π sin(4πM) sin(π Re τ) e^{−π Im τ} (+ for Λ = ¼, − for Λ = ¾). So it decays with exponent ½ (B1788's convention).

**Check (5)** (main's `cA`, at τ = 0.13 + 1.9i, 0.31 + 2.6i, 2.2i and 0.5 + 2.2i):
- On five of B1826's seven lines — (1/12, 0), (1/12, 1/12), (5/12, 1/3), (1/4, 0), (1/4, 1/2) — σ_b ≤ 6 × 10⁻¹² in
  modulus.
- On (1/4, 1/8), (1/4, 3/8), (1/4, 5/8) and (1/4, 7/8) it is ∓0.102, ∓0.024, 6 × 10⁻¹² (at Re τ = 0) and ∓0.100, in the
  same order of τ.
- The closed form matches main's σ_b to 5.9 × 10⁻¹²; the fitted exponent is 0.5000; the mirror holds to 2.3 × 10⁻¹²;
  and the three sectors agree to 6 × 10⁻¹².

**The census.** It has 266 lines of order ≤ 12 (B1825's reach), counted up to w → −w.
- Forty lie on these slopes. 36 of them have 12p₂ an integer, B1826's seven among them.
- The four that do not are the order-8 lines (1/4, 1/8), (1/4, 3/8), (1/4, 5/8) and (1/4, 7/8).
- On those four, the down and lepton sectors are among B1788's excluded line-sectors (a theta constant vanishes); the up
  sector is in its domain.

**So:**
- B1826's "the vanishing is exact at finite τ on these slopes" holds on the lines with 12p₂ an integer, and this is its
  reason. It fails on the other four. The independent lane's "vanishes identically at finite τ" over-reaches the same
  way.
- On those four, σ_b's cusp limit is still zero, so (b) fails there too. **That does not touch B1788's closed form.** By
  § 4, a difference term always reaches E₀₀ + E₁₁ by itself, so E(det M) = E₀₀ + E₁₁ needs only (c), with or without
  (b).
- A wording main may want for B1788's dated note: "(b) fails at the cusp on the slopes with 3α ≡ ¼ (mod ½); at finite τ,
  σ_b vanishes identically there exactly when 12p₂ is an integer (36 of the census's 40 lines on these slopes); on the
  order-8 lines (1/4, odd/8) it is nonzero off Re τ ∈ ℤ, with exponent ½. (b) is not needed for the closed form: with
  (a) stated term by term, one difference term always reaches E₀₀ + E₁₁ (§ 4), so E(det M) = E₀₀ + E₁₁ rests on (c)
  alone."

**The Re τ = 0 zero law (P-292 and P-404, explained).**

*Why it holds.*
- At Re τ = 0, φ_n = −2πμ for every n, so T_k(λ, μ) = cos(2πkμ)·Σ_n ρ_n^k/|n + λ|.
- The odd-harmonic differences of § 2 then carry cos(2πkM) for odd k. These all vanish exactly when 4M is odd: c₁ = c_i
  and c_j = c_k.
- 4M odd also makes 4M an integer, so on the slopes above σ_b ≡ 0.
- Then c₁ = c_i = c_j = c_k: the two pair equalities and σ_b = 0 give 2c_j = 2c_i. This is P-337's isotropy.
- All three terms of det M vanish, at every Im τ and either radius (L cancels in each difference).
- For the quark sectors (|q_L + q_R| = 3) the two conditions read **12p₁ odd and 12p₂ odd**.
- For the lepton doublet pair LL (q_L = q_R = −3, so R₁ = 0 and det M ∝ (c_j − c_k)(r₀₀² + r₁₁²) +
  2r₀₀r₁₁(c_j + c_k − 2c_i)) they read **24p₁ odd and 24p₂ odd**. The same conditions give c_j = c_k and
  c_j + c_k = 2c_i, that is c_i = c_j = c_k, as P-404 says.

*Check* (`zero_law_check.py`, version 2):
- **The lines.** In the census, 18 lines meet the quark condition: P-292's 16 of order 12, and two of order 4,
  (1/4, 1/4) and (1/4, 3/4). Exactly 8 meet the LL condition: P-404's (1/8, odd/8) and (3/8, odd/8).
- **The quark sectors at Re τ = 0** (Im τ 2.2 and 3.1, up and down, all 18 lines):
  - |D|/Σ|R_s|² ≤ 1.8 × 10⁻¹³, with main's D = Σ_s c_s R_s² (B1716);
  - |c₁ − c_i| ≤ 8.5 × 10⁻¹⁴, |c_j − c_k| ≤ 1.6 × 10⁻¹², |σ_b| ≤ 6.1 × 10⁻¹².
- **At Re τ = 0.13** the 16 order-12 lines are lifted (least 3.4 × 10⁻²). The two order-4 lines keep B1716's zeros at
  every τ.
- **The leptons** on these lines have D ≈ 0 at both Re τ (≤ 3.1 × 10⁻¹³). That is B1716's zero (−3w of exact order 4,
  6w of order 2), at every τ, not this law.
- **The LL pair** on P-404's 8 lines:
  - at Re τ = 0, |D|/Σ|R_s|² ≤ 1.8 × 10⁻¹³ and |c_j − c_k|, |c_j + c_k − 2c_i| ≤ 5.9 × 10⁻¹²;
  - at Re τ = 0.13 it is lifted (least 3.8 × 10⁻²).
- **Controls at Re τ = 0:**
  - (1/12, 0), the slope with 4M even: c₁ − c_i = c_j − c_k = 1.6 and D ≠ 0;
  - (1/7, 1/12), 4M odd off the slope: the differences vanish, σ_b = 48.6 and D ≠ 0.

So P-337's rectangular-mirror zeros of these two families follow from the pair expansion.
- **The quarks.** The conditions are P-292's (12α and 12β odd; here 12p₁ and 12p₂ odd), now derived.
- **LL.** 24p₁ and 24p₂ odd, which give exactly P-404's 8 lines.
- **The converse is the record's census:** that no other census line has the zero (P-292's row: "no other order and no
  other sector has such a zero in the census"; B1799 for LL). The derivation and the check give the "if" direction.
- P-404's other families (Re τ = ½; isolated points) are not treated here.

## 4. Hypothesis (a), exactly (P-559)

**The exponents.**
- From § 2, the leading terms of c_k − c_j and c_i − c₁ are the k = 1 terms at the nearest n.
- In B1788's convention (a modulus ∝ e^{−E·2π Im τ}):
  - **E(c_j − c_k) = ‖a_S + ½‖ = ½ − ‖a_S‖**;
  - **E(c₁ − c_i) = ‖a_S‖**, with a_S = (q_L + q_R)p₁.
- These are generic: they fail where the leading cosine vanishes (special Re τ) and where 2a_S is an integer (W177's
  integer-λ case, which has a term linear in Im τ).
- **Check (6a)** (W177's series at 40 digits, Re τ 0.17, Im τ 6 → 7), three sectors each, with the prediction:

| line | E(c_k − c_j) fitted (predicted) | E(c_i − c₁) fitted (predicted) |
|---|---|---|
| (2/5, 0) | 0.3000 (3/10) | 0.2000 (1/5) |
| (1/7, 1/7) | 0.0716 (1/14) | 0.4291 (3/7) |
| (4/9, 1/3) | 0.1667 (1/6) | 0.3333 (1/3) |
| (1/8, 3/8) | 0.1250 (1/8) | 0.3750 (3/8) |
| (3/10, 1/5) | 0.4000 (2/5) | 0.1000 (1/10) |

**These are the agy lane's exponents.**
- Its 2026-11-02 relay gives ‖3α‖/2 and 1/4 − ‖3α‖/2 for |q_L + q_R| = 3, in the convention it states,
  e^{−E·4π Im τ}. P-559's row records them without that convention.
- The independent lane's note on 2π and 4π is about the lane's account of B1788's anomalies, which set these
  4π-convention values against B1788's 2π-convention numbers.
- Its Theorem 15, Result 4, gives them in B1788's units and compares them term by term on 2/5, 4/9 and 1/7 down.
- **New here:** the comparison below on every slope and sector, with the tie rule.

**What B1788's det M needs, term by term.**
- From B1788's E_ij, E₀₀ + E₁₁ = E₀₁ + E₁₀. Write d_x = ‖q_L p₁‖ and d_y = ‖q_R p₁‖. Then |E₀₀ − E₁₁| = |d_x + d_y − ½|
  and |E₀₁ − E₁₀| = |d_x − d_y|.
- The term (c_j − c_k)(r₀₀² + r₁₁²) stays at or above E₀₀ + E₁₁ iff E(c_j − c_k) ≥ |E₀₀ − E₁₁|.
- The term (c₁ − c_i)(r₀₁² + r₁₀²) stays at or above it iff E(c₁ − c_i) ≥ |E₀₁ − E₁₀|.

**Both always hold (for 2a_S ∉ ℤ).**
- ‖a_x + a_y‖ ≥ |‖a_x‖ − ‖a_y‖| is the reverse triangle inequality for the distance to ℤ.
- ½ − ‖a_x + a_y‖ ≥ |½ − ‖a_x‖ − ‖a_y‖| follows from the triangle inequality when d_x + d_y ≤ ½. When d_x + d_y > ½, it
  follows from ‖a_x + a_y‖ ≤ 1 − d_x − d_y, which holds in both sign cases.
- **The ties:**
  - the j–k term ties when a_x and a_y, taken in (−½, ½], have the same sign;
  - the 1–i term ties when they have opposite signs;
  - both tie when one of them is 0 or ½.
- **Check (6b)**, over every slope in (0, ½] with denominator ≤ 20, three sectors, 2a_S not an integer (183 cases):
  - both minimum margins are 0;
  - the j–k term ties in 95 cases, the 1–i term in 95, both in 7, neither in 0.

**So (a), stated term by term, is a theorem for 2a_S ∉ ℤ.**
- **Where 2a_S is an integer,** the difference whose λ is an integer (c_i − c₁ when a_S ∈ ℤ, c_k − c_j when
  a_S ∈ ½ + ℤ) grows linearly in Im τ (W177's integer-λ term), and its bound is 0. Its term still sits at exponent
  E₀₀ + E₁₁, with a factor Im τ.
- **(c) carries the closed form.** On every line one difference term ties at E₀₀ + E₁₁. So B1788's leading order, with or
  without (b), rests on (c), "no cancellation among tied tropical terms", on every line. This note does not test (c).
- **As worded,** "c_j − c_k and c₁ − c_i decay at least at rate |E₀₀ − E₁₁|" compares c₁ − c_i with the other pair's
  rate.
  - It fails in 48 of the 183 cases; the list is in the output.
  - On the slopes with denominator ≤ 12 they reduce to nine: 2/5 up, 2/7 down, 3/8 up, 3/10 down and leptons, 3/11 down,
    and 4/11 in all three sectors.
  - With their mirrors 1 − α, these are exactly the independent lane's 18. Its 171 also counts α = 0 once per N and the
    cases with 2a_S an integer. The 48 extend its count to denominator 20.
- **Against B1788's failing classes.** The 48 overlap B1788's 32 failing m₂/m₃ classes (`domain.json`) only in part: 3/10
  down and leptons, 4/13 down, 4/15 down, 5/14 down and 7/20 down are in both. The seat draws nothing from that.

## 5. The parity of the Laurent constants (Theorem 15's Result 3, all four channels)

**The proof.**
- By § 1, where R_s ≠ 0, K_s depends on the twists only through c_s(S).
- S → −S sends c_s to −c_s modulo ℤ², since α_s and β_s lie in {0, ½}. K is unchanged when its characteristic moves by
  ℤ², because the factor cancels in θ[c](u)/θ[c](0).
- And θ[−c](u) = θ[c](−u). With θ₁ odd, this gives **K_s(u; −S) = −K_s(−u; S)**.
- So a₀ is odd in S, while |a₀|² and the norms are even. B1826 records the modulus form, |K(−z; −ū)| = |K(z; ū)|; this
  is the signed form.
- On a flat line, S(up) = −3w = −S(down) = −S(lepton). Hence a₀(up) = −a₀(down) = −a₀(lepton) in every channel where
  the residue does not vanish.
- On main, this is B1728's step 3 composed with B1826's "depends only on the Higgs twist ū".

**Check (2).** On (3/8, 3/8) at B1825's τ, on (1/7, 0) and on (2/9, 1/3):
- |a₀(up) + a₀(down)| ≤ 2.5 × 10⁻¹⁴ and |a₀(lepton) − a₀(down)| ≤ 5.2 × 10⁻¹⁴, with |a₀| up to 7.3;
- the shared norms agree to 3.6 × 10⁻¹²;
- step 3 as used holds to 1.7 × 10⁻¹⁴.

**Reading (labelled).**
- The kernels see ū alone. So their Laurent constants are odd in the sign of q_L + q_R — FL-06's and P-566's first
  candidate, "the Higgs's hypercharge sign" — and their norms are even.
- Whether the Higgs's singlet component takes a Laurent constant is not derived. B1744's twisted residue quaternion is
  even (H_u = H_d), so a rule would have to say why the singlet reads the constant and not the residue.
- S291 found the odd singlet to be the adjugate reading (P-583). This is an object-side quantity with that oddness, not
  a reading of it.

## 6. A look at B1825's address, disclosed (exploration tier, labelled)

**The look.** An unpushed draft of this note added a singlet a₀I to the Higgs at B1825's least-χ²_ten address
((3/8, 3/8), DR, L₂, S̃ for up and down) and compared one value, |V_ub|/|V_td| = 0.444, with nature's corner ratio
(about 0.43). That is a look at a function of the four. The address itself was chosen with the ten (run.json's least
χ²_ten), so the look is post hoc there too.

**What the committed check shows** (`singlet_at_the_address.py`; a₀ = c·√(h·h) over main's twelve phases; no singlet
gives 11.280):

| family | non-null phases | ∣V_ub∣/∣V_td∣ | below 1 |
|---|---|---|---|
| odd (up −a₀, down +a₀; main's opposite-sign family) | 10 | 0.152–1.214 | 9 |
| even (both +a₀) | 10 | 5.04–19.39 | 0 |
| up only | 10 | 0.472–1.409 | 5 |
| down only | 10 | 0.735–1.118 | 7 |
| a quarter turn between the sectors (up ia₀, down a₀) | 8 | 0.449–1.095 | 7 |

- At that address every family that differs between the sectors puts the ratio below 1 at half or more of its non-null
  phases (the odd one at 9 of 10), and the even family at none. So the address responds to any difference between the
  sectors, and does not test the parity's sign.
- The look earns nothing. It touched seen data, so it counts for any card it informs (PRACTICES, the two tiers).

## 7. P-512's two cusp constants, in closed form

**The cusp classes.** On slope 1/8 in the down sector (a_S = 3/8), channels 1 and i sit in the cusp class λ = 3/8 and
channels j and k in λ = 7/8. On slope 3/8 the classes swap (check (7), at Im τ 10).

**The constants.** By W177's c^∞ and Gauss's digamma theorem:
- c₁ = c^∞(3/8) = 2π[ln(8/π) − √2 ln(1 + √2)] = −1.95871280146;
- c̄ = c^∞(1/8) = 2π[ln(8/π) + √2 ln(1 + √2)] = 13.7046458862.

The digamma value, Gauss's sum and the closed form agree to 14 digits.

**P-512's x.** x = (2πL + c₁)/(2πL + c̄) = (L + ln(8/π) − √2 ln(1 + √2))/(L + ln(8/π) + √2 ln(1 + √2)):
- 0.117311322 at L_max and 0.442730295 at L₂ (P-512's 0.1173113 and 0.4427303);
- x > 0 iff L > √2 ln(1 + √2) − ln(8/π) = 0.311738824;
- x = ¼ at L = (5√2 ln(1 + √2) − 3 ln(8/π))/3 = 1.14270581.

This closes the gap the seat's P-512 relay left open.

## 8. What it does not show

- No measured value is read, and no frame point is chosen (§ 6's look aside, disclosed).
- The pair-sum identities rest on W177's series and are checked against main's `cA`. They are not derived independently
  of W177.
- § 4's exponents are generic (§ 4 names the exceptions). The note does not test hypothesis (c), on which B1788's leading
  order now rests on every line.
- § 3's zero law covers P-292's and P-404's Re τ = 0 families only.
- § 5 is a parity of the matter's kernels. Its use for the Higgs's singlet needs a rule that is not here.

## Proposals (main's to take or leave)

- **P-524 (a [DEBT]):** § 1's written proof, for the arc main's row asks for (b and a).
- **B1788's dated note and B1826's item 2:** scope them as in § 3, and record that (b) is not needed (§ 4).
- **P-559:**
  - the agy lane's exponents (its Result 4) hold, derived from § 2's expansion and checked on B1788's lines (§ 4; P-559's
    Q3);
  - (a), stated term by term, is a theorem for 2a_S ∉ ℤ;
  - as worded it fails in 48 of 183 cases (the independent lane's 18 of 171, extended), so its open part becomes (c).
- **P-512:** its constants in closed form (§ 7). Its condition on B1788 § 5 reduces to (c): (a) term by term is a theorem
  (§ 4), and (b) holds at the cusp on the slopes 1/8 and 3/8, since 3α = 3/8 and 9/8 are not ≡ ¼ (mod ½) (§ 3).
- **P-337 (with P-292 and P-404):** the Re τ = 0 zero law of § 3, for these two families.
- **FL-06 / P-566:** the Laurent constants are odd in the Higgs's hypercharge sign in all four channels (§ 5), a fact on
  the object's side for the first candidate.
- **LOOK_LEDGER:** § 6's look.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE CHANNEL NORMS' PAIR SUMS AND B1788'S TWO HYPOTHESES, EXACTLY (scripts 6f16af477, 62ddc3389 and f54ae3d16; outputs d52fd021c, e862b963e and 8e6dc5153) | "c_k + c_j and c_1 + c_i are each twice one kernel norm at 2τ" | `relays/CHAT1_TO_CC_2026-11-03_THE_CHANNEL_NORMS_PAIR_SUMS_AND_B1788S_HYPOTHESES.md` @ the commit adding it | — | P-524, B1788, B1826, P-559, P-512, P-337, P-404, B1799, P-566, FL-06 | 2026-11-03 |

0 of 19.
