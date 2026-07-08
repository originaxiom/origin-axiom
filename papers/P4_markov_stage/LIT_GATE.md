# Paper 4 — the literature gate (round 1: two of six hunts complete; four re-queued for the next pass)

## Hunt (e) — cat-map commutators: PARTIALLY-KNOWN (calibration excellent)

**Known, to be cited instead of claimed:**
- The 'if' direction of the commutation principle is in print VERBATIM: **Kurlberg–Rudnick,
  Duke Math. J. 103 (2000), Corollary 6** — "If A, B ∈ Γ(4,2N) commute mod 2N then their
  propagators also commute" — the basic principle behind their Hecke operators; plus
  Theorem 5 (genuine representation for suitable phases) and §4.1 (the CRT tensor
  factorization — our mod-3 × mod-5 structure's home).
- **Mezzadri, Nonlinearity 15 (2002)**: multiplicativity on the theta group for any N;
  the phase-INDEPENDENCE of commutation — the exact lemma that makes κ_q well-defined
  (to be cited at Proposition 4.0); and the assertion "the Hecke symmetries of U_N(A)
  are those U_N(B) with AB ≡ BA mod 4N" — the converse asserted by phrasing, proved
  only in the 'if' direction.
- Genuine-ness at odd level: Schur (1904/07), **Beyl, Math. Z. 191 (1986)** (Schur
  multiplier of SL(2,ℤ/m) trivial for m ≢ 0 mod 4), **Nobs–Wolfart** (the complete
  representation theory; Kloosterman 1946 the earliest genuine construction).
- Character machinery: **Howe's formula |χ(g)|² = #Fix(g)**; **Thomas, J. LMS 77 (2008)**
  (the exact character value with sign); Gurevich–Hadani (geometric Weil rep).

**Ours (scoped, honest):** the explicit N = 15 commutator table; the Q₈/SL(2,5)
commutator-image assembly; the (2,3) closure address; the ⟹ direction (quantum ⟹
classical commutation) — NOT in print; ours stands as verified-on-240-points with the
faithfulness question named.

**UPGRADE HANDED TO US (verified in-session, 25/25): |κ_q(j,l)|² = #Fix([A₁ʲ,A₂ˡ] on
(ℤ/15)²)** — Howe's formula explains every magnitude in the table (the divisors of 15
are the square roots of the fixed-point counts); the SIGN refinement is Thomas's. The
paper's §4.1 gains the magnitude law with a classical proof.

## Hunt (f) — the divisor-lattice factorization: PARTIALLY-KNOWN (with a proof gift)

**Known:** the factor-through-gcd pattern is classical and NAMED — **Cohen's "even
functions (mod r)"** (PNAS 41 (1955)): f(n) = f(gcd(n,r)), spanned by Ramanujan sums.
**Serre, Linear Representations §12.4/§13.1**: rational-valued class functions are
constant on ℚ-classes (elements generating the same cyclic subgroup) — giving a
ONE-LINE PROOF that rational-valued trace functions of powers of finite-order unitaries
factor through gcd of the exponent with the order. Gaussian periods realize the subfield
lattice classically; Gauss-sum vanishing stratified by conductor/gcd is the classical
prototype (Berndt–Evans–Williams).

**Ours:** the JOINT statement — two maps, the order-torus, the co-factorization of κ_q
AND the tier map, the 36-cell master table, the tier/subfield-lattice reading.

**UPGRADE HANDED TO US: Theorem G(ii)'s κ_q half is PROVABLE by Serre's mechanism**
(κ_q is rational-valued and a class function of the commutator, which depends on
(j mod ord, l mod ord) through powers — the ℚ-class argument applies); the tier half
should follow per-channel from the Galois-isotypic version. Draft v3 task: replace
"verified exactly on all 240 points" with the classical proof + the verification as
confirmation.

## Hunts (a)–(d) + the book gate: re-queued (next pass)

The symmetric-identity, root-criterion/reciprocal-geodesics, amphichirality, and
line-by-line book hunts did not complete this round and are re-queued; the workflow
resumes with the two completed hunts cached. §5's items (a)–(d) keep their
"could-not-locate, gate incomplete" status until then.

## Draft v3 edit list (from this gate round)

1. Proposition 4.0: cite Kurlberg–Rudnick Thm 5 + Beyl for genuine-ness; cite Mezzadri
   for phase-independence of the commutator.
2. Theorem F: cite KR Corollary 6 for ⟸; state ⟹ as ours (verified; faithfulness named).
3. §4.1: add the magnitude law |κ_q|² = #Fix with Howe/Thomas citations (verified 25/25).
4. Theorem G(ii): the Serre ℚ-class proof for κ_q; per-channel Galois-isotypic argument
   for the tier map (to be written); the 240-point check becomes confirmation.
5. §5: quantum items rewritten from SUSPENDED to the scoped form above.

---

# Round 2 (2026-07-08): ALL SIX HUNTS COMPLETE (workflow resumed; 2 cached + 4 fresh)

## Hunt (a) — the symmetric-pair identity: PARTIALLY-KNOWN
The identity is the coordinate form of classical facts in three clothings: **Sarnak,
Reciprocal geodesics (Clay Proc. 7, 2007)** — symmetric ⟺ S₀-conjugation inverts, giving
[A,B] = M(Mᵀ)⁻¹ = −(MS₀)² and the 2−(square) form in two lines; **Gehring–Martin (J.
Anal. Math. 63, 1994)** — the δ = 0 slice of their commutator calculus (hunter VERIFIED
numerically: sin²θ = 4(n−m)²/((m²+4)(n²+4)) reproduces (mn(n−m))²); **Goldman/Fricke** —
direct substitution into κ. **And the (1,2) instance is in print VERBATIM: Reutenauer's
Markoff morphism μ(x) = [[2,1],[1,1]], μ(y) = [[5,2],[2,1]] = our (A₁, A₂), parabolic
commutator computed via Fricke (Integers 9 (2009); OUP book 2019, Thm 3.1.1).** Ours:
the coordinate lemma AS a lemma, the metallic parametrization, the uniqueness scan —
positioned against Schmutz Schaller (2022), Nielsen's theorem, D.E. Martin (2025).

## Hunt (c) — the root criterion: PARTIALLY-KNOWN (criterion EXACTLY known)
**Northshield, Square roots of 2×2 matrices (Contemp. Math. 517, 2010), eq. (7)**: the
criterion + formula X = (B−I)/t — identical content; cite, do not claim. O'Sullivan
(arXiv:2408.14405, §8.3) exhibits the det −1 root of R^tL^t. Latimer–MacDuffee applies
verbatim for the classification; Sarnak's reciprocal-geodesic count is the same
correspondence in negative-Pell form; which t give h⁺(t²+4) = 1 is the Yokoi problem
(Yokoi; Biró). The equivalence "family = locus ⟺ h⁺ = 1" found nowhere stated (immediate
corollary; claim assembly only). Hunter re-verified the criterion exhaustively (108
matrices, 0 mismatches).

## Hunt (d) — amphichirality: PARTIALLY-KNOWN (criterion known, closed case)
**Tian–Wang–Wang (arXiv:2406.13241, 2024), Lemma 3.1 + Thm 3.5**: the FULL criterion —
both mechanisms, sufficiency-not-necessity, the commuting det −1 element subsuming the
root — for closed Sol torus bundles; proof transplants verbatim. **Baake–Roberts (J.
Phys. A 30, 1997, Props. 3–5)**: rev·swap ⟺ conjugate-to-inverse, exactly. **Floyd–
Hatcher (1982, p. 268)**: symmetry group = GL(2,ℤ)-normalizer of the monodromy.
Morimoto: the unoriented classification (plain conjugacy-to-±inverse ignores
orientation — the trap our bridge lemma avoids). Sakuma (1985): the closed-case root
mechanism. Gieseking m = 1 classical. Ours: the punctured word-criterion statement, the
strictness witnesses, the tables.

## Hunt (e) refinement — the ⟹ DIRECTION IS A FOLKLORE COROLLARY (downgrade, accepted)
**Appleby (J. Math. Phys. 46, 052107 (2005))**: the projective Weil representation is
injective in odd dimension — so [W_A, W_B] = I ⟹ W_{[A,B]} scalar ⟹ [A,B] ≡ I mod N.
With Kelmer's multiplicativity mod odd N, the FULL iff of Theorem F(ii) is a corollary
of published results (stated verbatim nowhere that the hunters could find). Our
240-point check becomes CONFIRMATION, not claim. This demotes v3's Theorem F(ii)
scoping; v4 carries the correction.

## Hunt (f) refinement — the two-variable even-function class is DEFINITIONAL
McCarthy's book (1986, after Cohen): (r,s)-even functions f(a,b) = f(gcd(a,r), gcd(b,s))
— the joint factorization PATTERN is a definition in print, not just the one-variable
class. Coste–Gannon/Bantay supply the Galois-channel equivariance wholesale. Ours
remains: the specific instance (two cat maps, κ_q + tier jointly, the 36-cell table).

## Book gate — PARTIALLY-KNOWN, position confirmed
The three monographs anchor everything to the single fixed commutator (trace −2, Cohn
one-parameter families; Aigner Thm 4.8). No two-parameter commutator formula, no R^mL^m
family, no square-root theme, in the books or the 2019–2026 citing sweep (Gyoda–
Maruyama–Sato 2024 still one-parameter). "Metallic" as a name appears only for physics
transfer matrices (Wang–Grimm–Schreiber). RESIDUAL: no page-level access to Aigner 2013
/ Reutenauer 2018 full texts (chapter-level + citing-paper evidence only) — the residual
uncertainty statement goes in the paper's §5 verbatim.

## Draft v4 edit list (all applied)
1. Lemma 2.2: provenance paragraph (Sarnak mechanism, Gehring–Martin slice, Goldman).
2. Theorem A remarks + Theorem B: Reutenauer's morphism = the pair, verbatim; uniqueness
   positioned against Schmutz Schaller/Nielsen/Martin.
3. Theorem D: "classical (Northshield eq. 7)"; O'Sullivan; proof kept for completeness.
4. Theorem D′: Latimer–MacDuffee/Sarnak/Yokoi–Biró citations; assembly-only claim.
5. Lemma 3.3: Tian–Wang–Wang + Baake–Roberts + Floyd–Hatcher provenance; Sakuma at E″.
6. Theorem F(ii): the iff = corollary of Appleby injectivity + Kelmer multiplicativity;
   240-point check = confirmation. §5 quantum block updated to match.
7. §5 items (a)–(d): final verdicts with the residual-uncertainty statement.
