# B1512 — THE SELF-COINCIDENT ORBITS: m004's symmetries act on Ballas' family, so the tower's twisted polynomials are real, rational and paired under q ↦ 1/q; and all 32 of B1511's unresolved case-(b) pairs fire: M₅ in orbits of five, M₆ in orbits of six, every member +1

**Date:** 2026-10-01 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED.
**Sealed** at b8ddbb66 (PREREGISTRATION.md, sha256 `7d0a41429144effd0eee0792f40413d43809cb237917b8d75b612ad63edf47f6`), before any
polynomial, root or count of the twelve orbits was computed. **Run as sealed** (`verification/census.py --record`, 833 s).
**Price:** unchanged, 0 of 19.

## 0. Seen from above

**The question.** B1511 carried B1509's rank-five extension to m004's cyclic covers. Its case (b) is a line non-trivial on the fibre and
trivial on the cusp, and counts I(W₁) = 1 − r1 ∈ {0, +1}. It fired on M₄. On M₅ and M₆ thirty-two pairs stayed UNRESOLVED: twelve
orbits where the needed coincidence is automatic. B1511 also found, without a reason, that every twisted polynomial is real.

**The symmetries (proved at the seal).** m004's symmetries act on Ballas' family ρ_q, and they decide the structure:
- **ι**, the fibre's hyperelliptic involution, fixes ρ_q. So P_ν = P_{ν⁻¹} on every level, and every twisted polynomial is real.
- **The dual** of ρ_q is ρ_{1/q}. So P(1/q, s) = s⁴P(q, 1/s), real exceptional points come in pairs (q, 1/q), and the counts at the
  two are dual.
- **ε**, the strong inversion, and **α**, the amphichiral map, send ρ_q to ρ_{1/q}. So M₅'s four orbits share one polynomial, which is
  palindromic. M₆'s four classes pair under α. And B1511's pairings (O_A with Ō_B on s961, class 1 with class 10 on M₄) are explained.

**The answer (the sealed run).** Every one of the 32 pairs fires. At every positive real exceptional point every member of every orbit
counts I(W₁) = +1, I(W₂) = −1 and I(Λ²W) = 0. The points, in w = q + 1/q:

| level | orbits | λ = 1 | λ = ±i | λ = −1 |
|---|---|---|---|---|
| M₅ | four orbits of five (one polynomial) | **w = 7** (q = φ^{±4}), a double semisimple point, h¹ = 2 | w ≈ 2.27758, simple | w ≈ 2.49991, a **Jordan point** |
| M₆ | {1, 3} and {31, 53} (α-paired) | w ≈ 4.7256, 8.3678, 21.5999 | none (B1511) | w ≈ 9.2365, 21.4950 |
| M₆ | {32, 34} and {33, 47} (α-paired) | w = 5 + 2√3 | none (B1511) | w ≈ 2.5786, 8.3115 |

**Reading.**
- Through level 6 the tower's case (b) fires wherever its coincidence is automatic: in orbits of four, five and six on M₄, M₅ and M₆.
  It always has the opposite sign to B1509's 10′ (one 10̄′ per member).
- Three still comes only from the projective triplet on s961 (case (a), B1511). No 5̄′ appears anywhere (Λ²W counts 0).
- The per-level table through level 6 is complete. Nothing is UNRESOLVED.

## 1. Setting

As sealed (PREREGISTRATION §1; B1511 §1).
- The twelve orbits:
  - M₅'s orbits 12, 15, 18 and 19, the characters on the two Φ-eigenlines of T₅ = 𝔽₁₁²;
  - M₆'s orbits 1, 3, 31, 32, 33, 34, 47 and 53, of characters of order 8.
- The 32 pairs are M₅'s four orbits at every λ ∈ μ₄, and M₆'s eight orbits at λ = ±1.

## 2. The lemmas (proved at the seal; proofs in PREREGISTRATION §3)

| map | images of m, n | on H₁(F) | on π/F | orientation; (meridian, longitude) | on Ballas' family |
|---|---|---|---|---|---|
| ι (hyperelliptic) | mnm⁻¹, mn⁻¹mnm⁻¹ | −1 | + | kept; (+, +) | ρ_q∘ι ≅ ρ_q (det C = 16q²) |
| ε (strong inversion) | mn⁻¹m⁻¹, mnm⁻¹n⁻¹m⁻¹ | swap, det −1 | − | kept; (−, −) | ρ_q ≅ ρ_{1/q}∘ε (det E = 16q⁴) |
| α (amphichiral) | mnm⁻¹, nmn⁻¹m⁻¹n²m⁻¹ | [[2, 1], [−1, −1]], a square root of Φ⁻¹, det −1 | + | reversed; (+, −) | ρ_q ≅ ρ_{1/q}∘α (det A = −16q³) |
| duality | — | — | — | — | ρ_q^{−T} ≅ ρ_{1/q} (det D = −16q(q² + q + 1)) |

- **Lemma I.** P_{ν⁻¹} = P_ν on every level (B1511's lead 3).
- **Lemma G.** The twelve orbits' polynomials are rational: one per Galois class, 2 classes on M₅ and 4 on M₆.
- **Lemma D.**
  - P(q, 0) = 1 and P(1/q, s) = s⁴P(q, 1/s).
  - Real exceptional sets are closed under q ↦ 1/q.
  - I(W₂)(ν⁻¹, 1/q) = −I(W₁)(ν, q).
- **Lemma E.** P_{(b,a)} = P_{(a,b)}, so M₅'s two classes have one polynomial. ε is the audit lane's θ (F14) up to ι and the deck.
- **Lemma A.**
  - P_{ν∘α}(q, s) = P_ν(1/q, s), and the count of ν∘α at q is the count of ν at 1/q.
  - α fixes each of M₅'s classes, so M₅'s polynomial is palindromic.
  - On M₆ it pairs {1, 3} ↔ {31, 53} and {32, 34} ↔ {33, 47}.

The sign patterns agree with main's T-MIRROR-IS-SWAP-TIMES-ARROW (B1324). There, m004's eight isometries realise the patterns
(orientation; meridian, longitude) = (+; +, +), (−; +, −), (−; −, +) and (+; −, −) twice each:
- ι is main's period-2 P, pattern (+; +, +) (main's B1297);
- ε is an inversion, (+; −, −);
- α is the fibre reflection, (−; +, −).

## 3. The sealed run (`verification/census.py`, record `census_run.txt`, 833 s)

**The banked identity** passed inside the run. M₄'s (0, 5) class reconstructed equals B1511 Part C1. At p = 1021, q ≡ 355 it counts
I(W₁) = +1, I(W₂) = −1 and I(Λ²W₁) = 0.

**Part A — the lemmas inside the run.** The involution, ν∘ι = (ν_F⁻¹, λ) on levels 1–6, the duality, the strong inversion, the
amphichiral map, and the class maps under α all hold.

**Part B — the six polynomials** (over ℚ; 3 primes near 2³¹ each, both fresh primes agreeing).
- At a further prime:
  - every member of both orbits of each class has the class's polynomial (10 members on M₅, 12 on M₆);
  - it does not depend on the root of unity chosen (D1).
- Every class has P(q, 0) = 1 and satisfies Lemma D's identity (D2).
- B1511's banked GF(p) degrees are reproduced for every pair (D4).

**M₅ (one polynomial, D3; palindromic, D9).** In w = q + 1/q:

P(q, s) = s⁴ + 4(w² − 14)(s³ + s) − (w⁵ − 14w⁴ + 46w³ + 48w² − 119w − 208)s² + 1.

- P(q, 1) = −(w − 7)²(w − 2)(w + 1)²;
- P(q, −1) = −(w⁵ − 14w⁴ + 46w³ + 56w² − 119w − 322);
- P(q, i) = w⁵ − 14w⁴ + 46w³ + 48w² − 119w − 206, real (the palindrome).

It is not Q(q⁵, s) (P1).

**M₆ (four polynomials in two α-pairs, D9; none palindromic).** P_{31,53}(q, s) = P_{1,3}(1/q, s) = s⁴P_{1,3}(q, 1/s), and likewise
for {32, 34} and {33, 47}. At λ = ±1 each pair shares its specialisations:
- {1, 3}, {31, 53}: P(q, 1) ∝ (w − 2)(w + 1)(w⁴ − 35w³ + 333w² − 953w + 262), and P(q, −1) ∝ w⁶ − 36w⁵ + 366w⁴ − 1208w³ + 829w² +
  1956w − 1548.
- {32, 34}, {33, 47}: P(q, 1) ∝ (w − 2)²(w + 1)²(w² − 10w + 13), and P(q, −1) ∝ w⁶ − 12w⁵ + 30w⁴ + 16w³ − 83w² − 60w + 180.
- At λ = ±i: no positive real root other than 1, for all four classes (D5, B1511's resolution reproduced exactly).

**Part C — the real exceptional points** (exact isolation; arb agrees on every real-root count). Every positive root set is closed
under q ↦ 1/q (D2):
- **M₅:**
  - λ = 1: q = φ^{±4} (w = 7), a double root;
  - λ = ±i: q ≈ 0.59396, 1.68363;
  - λ = −1: q ≈ 0.50003, 1.99988.
- **M₆, {1, 3} and {31, 53}:**
  - λ = 1: q ≈ 0.04640, 0.12126, 0.22205, 4.50354, 8.24652, 21.55349;
  - λ = −1: q ≈ 0.04662, 0.10957, 9.12697, 21.44839.
- **M₆, {32, 34} and {33, 47}:**
  - λ = 1: q ≈ 0.11984, 8.34426;
  - λ = −1: q ≈ 0.12211, 0.47548, 2.10314, 8.18943.

**Part D — the fibre and the counts.** For every member of the class, at three primes and every root (6–12 prime–root pairs per
factor):

| level | λ | fibre at the real root (numeric, 60 digits) = over GF(p) | h¹(L, V_ν, V_η, V_η*) | I(W₁) / I(W₂) / I(Λ²W) | data of W₁ |
|---|---|---|---|---|---|
| M₅ | 1 (w = 7) | (2, 2, 2, 2): semisimple, double | (1, 2, 2, 2) | +1 / −1 / 0 for c1, c2 and c1 + c2 | (0, 2, 1, 0) |
| M₅ | ±i | (1, 1, 1, 1) | (1, 1, 1, 1) | +1 / −1 / 0 | (0, 1, 1, 0) |
| M₅ | −1 | **(1, 2, 2, 2): a Jordan block** | (1, 1, 1, 1) | +1 / −1 / 0 | (0, 1, 1, 0) |
| M₆ | ±1, every factor | (1, 1, 1, 1) | (1, 1, 1, 1) | +1 / −1 / 0 | (0, 1, 1, 0) |

- **D6.** rank B = 4 everywhere. The numeric singular values are ≤ 3.3 × 10⁻⁴⁰ where zero and ≥ 0.0072 otherwise.
- **D7.** Every member of each class agrees at every prime–root pair.
- **D8.** The W₂ values at the reciprocal factor with λ⁻¹ are minus the W₁ values.
- **D10.** The α-image class has the same values at the reciprocal factor.

**Part E — the 32 pairs.** All 32 fire: I(W₁) = +1 and I(W₂) = −1 for every member at every real exceptional point.

**The completed per-level table** (B1511 Part D, W₁-type count per member):

| level | pullback (Theorem D) | orbits of three (B1511 Part A) | case (b) |
|---|---|---|---|
| m004 | −1 at w = 34 | — | — |
| M₂ | −1 | — | none (B1511 C2) |
| s961 | −1 | **O₂: three × (−1) at q³ + q⁻³ = 34, λ₃ = −1** | — |
| M₄ | −1 | — | two orbits of four × (+1) at w = 7, λ = 1 (B1511) |
| M₅ | −1 | — | **four orbits of five × (+1)** at w = 7 (λ = 1), w ≈ 2.2776 (λ = ±i), w ≈ 2.4999 (λ = −1) |
| M₆ | −1 | O₂ pulled back: three × (−1), λ₆ = 1 | **eight orbits of six × (+1)** at λ = ±1, eight values of w |

Nothing is UNRESOLVED on levels 1–6.

## 4. The predictions, read

| | prediction (prior) | outcome |
|---|---|---|
| P1 | M₅'s polynomial is Q(q⁵, s) (~25%) | **NO**: palindromic as Lemma A forces, but c₁ = 4(w² − 14), not −8 |
| P2 | M₅ has a positive real exceptional point (~90%) | **YES**: three values of w, at every λ |
| P3 | M₆ has one at λ = ±1 (~85%) | **YES**: every class, at both λ |
| P4 | case (b) fires on M₅ (~65%) | **YES**: four orbits of five, every member +1 at every point |
| P5 | case (b) fires on M₆ (~65%) | **YES**: eight orbits of six, every member +1 at every point |
| P6 | every real exceptional point is a simple fibre root (~55%) | **NO**: M₅'s w = 7 is a double semisimple point (h¹ = 2), and its λ = −1 point is a Jordan point |
| P7 | at every simple real point every member counts +1 (~70%) | **YES**: all simple points (M₅ at ±i, every M₆ point) |

## 5. Post-run checks (`verification/post_run_checks.py`, record `post_run_checks_run.txt`; not predictions)

- **(a) The closed forms in w.** Given in §3. Every specialisation at λ = ±1, and M₅'s at ±i, is a polynomial in w, so its positive
  roots q ≠ 1 are its real roots w > 2.
- **(b) Coincidences across the tower.** The w-polynomials of every firing family on levels 1–6 were compared exactly: the pullback
  (w = 34), the triplet (w³ − 3w = 34), M₄'s case (b), and M₅'s and M₆'s.
  - **The only coincidence between different families is w = 7**, shared by M₄'s case (b) and M₅'s at λ = 1. At w = 7 the untwisted Q
    has the order-6 roots e^{±iπ/3} (B1511 C6).
  - Every other common factor is within one level, between symmetry partners: α-paired classes, or λ = i with λ = −i.
  - No case-(b) point meets the triplet's or the pullback's q. So no single background configuration on M₆ carries both signs.
- **(c) M₅'s double point.** Every class tried, c1, c2 and c1 + c2, counts +1 for W₁ and −1 for W₂ (h¹ = 2).
- **(d) Backgrounds per q.**
  - M₅: at each of the four q's of λ = 1 and λ = −1, all 20 eigenline characters fire. At the two q's of λ = ±i they fire at both
    λ = i and λ = −i: 40 backgrounds.
  - M₆: at each of its sixteen q's, the 24 characters of one α-paired pair of classes (four orbits of six) fire.

## 6. The physical reading

**What fires.**
- Through level 6 the tower has two mechanisms (B1511 Theorem A):
  - **case (a)**, B1509's 10′ through a Jordan block: the pullback (one per level) and the projective triplet on s961 and M₆;
  - **case (b)**, a 10̄′ per member when x ∪ c ≠ 0: orbits of four on M₄, five on M₅ and six on M₆.
- Case (b) now fires at **every** real exceptional point of every self-coincident orbit, including a double semisimple point and a
  Jordan point.
- Read with B1506's level law (an orbit of size k counts gcd(n, k) times its member's count), the opposite sign counts −4, −5 and −6 in
  10′ on M₄, M₅ and M₆.

**What it is not.**
- **Not three.** Case (b)'s orbits have size n on Mₙ (4, 5, 6). Three is still only the projective triplet (B1511 Theorem E).
- **Not a generation.** There is no 5̄′ on any of the 32 pairs (Λ²W counts 0), and B1511 Theorem A(vi) holds on every level.
- **Not selected.** Every count sits at its own q, and the two signs never share a q on M₆ (post-run (b)). The q, the level, and the
  deck's bit (B1506) stay open.
- **The symmetries are not a selection either.** They pair q with 1/q and dualise the counts, but they choose nothing.

**I-26 stays UNEARNED. 0 of 19.**

## 7. Record and disclosures

- **Order.**
  - PREREGISTRATION.md (sha256 7d0a4142…edf47f6, in full in the header) was committed and pushed at b8ddbb66. With it went the
    instrument, the controls (K1–K10, 70 s) and the dry run at level 4, before any polynomial of the twelve orbits was computed.
  - The run is `census.py --record`, 833 s.
- **A design slip, caught before the seal (ERROR_LEDGER).**
  - A draft called the strong inversion ε "the amphichiral map". ε has det −1 on H₁(F) and reverses the fibration, so it keeps
    orientation. The amphichiral map is α.
  - The sealed text has the correction (its §2 disclosures). No sealed quantity depended on the label.
- **A citation added after the run.** Main's B1324 (T-MIRROR-IS-SWAP-TIMES-ARROW) classifies m004's isometries by their signs, and the
  design-time sweep did not cite it (§2 above). It concerns the isometries, not Ballas' family. No claim of this arc changes.
- **Main moved after the seal**, d88c220e → d3b50c0f (S32: B1444, the backgrounds as ends of the trace map's periodic curves; B1445
  sealed). Both are in the rank-two Standard-Model frame. Read for overlap; there is none (RELAY_LEDGER).
- **Harvested by citation:**
  - the audit lane's F14 (θ, credited for Lemma E);
  - main's B1297 (the period-2 P on ρ_geo) and B1324 (the sign classification);
  - B1511's record (degrees, the M₆ λ = ±i resolution).

## 8. Leads (registered, not run; each sealed before computing)

1. **A theorem for "case (b) fires wherever its coincidence is automatic"** (every member +1 at every real point, including double and
   Jordan points). Does the deck isomorphism H¹(ν⁵ ⊗ ρ_q) ≅ H¹(ν ⊗ ρ_q) force x ∪ c ≠ 0? Prove it, or test it at levels 7–8.
2. **Why w = 7 on M₄ and on M₅.** At w = 7 the untwisted monodromy has the order-6 eigenvalues e^{±iπ/3} (B1511 C6).
3. **B1511's lead 2, sharpened.** O₂'s Q(q³, s) is not the pattern of the self-coincident orbits (P1 NO). What singles out O₂?
4. **The full symmetry action.** Do the deck, Galois, ι, ε, α and the duality account for every equality between twisted polynomials
   on levels ≤ 8, with no accidental coincidences?
5. **The 5̄′** (B1509 lead 2, B1511 lead 4). It is unchanged and decisive.

## Verification

- `verification/selfco_lib.py`: the symmetries and their intertwiners, the multi-modular reconstruction, the roots, and the counts at
  every root (imports B1511's library).
- `verification/controls.py` → `controls_run.txt`: K1–K10, run before the seal.
- `verification/census.py` → `census_run.txt`, `census_log.txt`: the sealed run. `census_dry_run_level4.txt`: the pre-seal dry run.
- `verification/post_run_checks.py` → `post_run_checks_run.txt`: post-run checks (a)–(d).
- `tests/test_b1512_the_self_coincident_orbits.py`: the lock.
