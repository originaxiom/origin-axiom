# P4 panel round 2 — FINAL adjudication (all five seats; every load-bearing finding verified)

**Round 2 complete: structure (prior) + correctness + novelty + overclaim + hostile.
Verdict: NO FATAL; every mathematical claim reproduces; both v5 fixes hold. The panel
found one deep structural-honesty lever (the level-15 collision), two genuine overclaims
in the §4.2 "curiosities," a reproducibility hole in the open-problem constants, a set of
novelty demotions, and several small errors — one of them freshly introduced in v5. All
CONFIRMED items below are fixed in draft v6.**

## CONFIRMED — verified by CC this session, fixed in v6

1. **[MAJOR, the load-bearing lever — hostile] §4 is blind to parabolicity.** The Weil
   operators depend only on the pair's image mod 15. Verified: A₁₆ ≡ A₁ and A₁₇ ≡ A₂
   (mod 15), so the pair (A₁₆, A₁₇) — with tr[A₁₆,A₁₇] = 2−272² = −73982, wildly
   non-parabolic — reproduces every table in §4 identically. **Fix (v6):** §4 reframed as
   "the level-15 Weil shadow of the pair"; the (16,17) collision disclosed as a remark;
   the honest content is which finite structure the mod-15 image (Q₈ × SL(2,5)) carries,
   NOT a parabolicity-sensitive statement. This is the same lesson the program banks
   elsewhere (structure is level-arithmetic); disclosing it strengthens the paper.

2. **[MAJOR, numerology — hostile] The "240 = 4·60" curiosity is manufactured.** Verified:
   |⟨A₁,A₂⟩ in SL(2,ℤ/15)| = **960** = |Q₈|·|SL(2,5)| = 8·120; the PSL image is 240. The
   printed "|Q₈/±|·|PSL(2,5)| = 4·60 = 240" silently swaps SL(2,5) (order 120, per the
   paper's own Theorem F) for PSL(2,5) (60) to hit 240. **Fix (v6):** state the honest
   fact — the image is Q₈ × SL(2,5) of order 960, and 240 = ord(W₁)·ord(W₂) is its
   projectivization (the order torus) — or the coincidence is cut.

3. **[MAJOR broken step, theorem TRUE — correctness] Theorem F(ii) ⟹ "scalar ⟹ identity"
   is a false sub-implication.** The center of SL(2,ℤ/15) has order 4 {I,4I,11I,14I};
   [A₁,A₂³] ≡ 11·I ≠ I (28 such addresses). Appleby projective injectivity gives only
   "scalar," not "identity." The equivalence is nonetheless TRUE via the *genuine* rep's
   faithfulness on the order-4 center (W(11·I) = Par₃⊗I₅ ≠ I; those 28 addresses all have
   κ_q = −5 ≠ 15). **Fix (v6):** replace the Appleby-only argument with genuine-rep
   faithfulness on the center (KR Thm 5 / Kelmer).

4. **[MAJOR overclaim — hostile] OP-3 constants unreproducible as printed.** λ_chain is
   printed to 18 digits, but a degree-8/height-10⁴ PSLQ exclusion needs ≈ 36 digits; at 18
   digits mpmath.pslq RETURNS a spurious relation (height 4001). **Fix (v6):** print the
   working precision, cite the exclusion to the reproducer (not the printed digits), soften
   "pinned" → "numerically located," state the height bound explicitly, define/scope out
   the "golden-sector Lobachevsky basis."

5. **[MAJOR novelty — novelty + overclaim] §5's "did not find" list re-claims two
   gate-located items.** The F(ii) ⟹ direction (Appleby-downgraded, per §4.2 and the
   header) and the joint divisor-lattice factorization (McCarthy (r,s)-even functions, per
   the gate). **Fix (v6):** strike both; keep only the N=15 table, the Q₈×SL(2,5)
   assembly, and the closure address.

6. **[MAJOR novelty — novelty] The h⁺-equivalence is a tautology, not an assembly.** Since
   N(λ_m) = −1 for all m (verified), narrow = wide, so h⁺ = h; "family = locus ⟺ h⁺ = 1"
   is "class number one ⟺ class number one," the =1 case of the Latimer–MacDuffee/Sarnak
   count. **Fix (v6):** demote to "the class-number-one specialization" of that count; note
   N(λ_m) = −1 makes the narrow refinement inert.

7. **[MAJOR novelty — novelty] Theorem G's "joint / master" is two independent classical
   factorizations tabulated together, tier half unproven.** **Fix (v6):** retitle to "a
   worked N=15 instance of the (Cohen/McCarthy even-function) × (Serre ℚ-class)
   factorization"; drop "master theorem"; state plainly the tier half is verified-not-
   proven (∎ scoped to (i) + the verification).

8. **[MINOR — correctness/hostile, v5-fresh error] §4.3 legend fourth channel wrong.**
   √5·√−3 = √−15 (= s), not √−45; the fourth channel is the RATIONAL (basis-1) part, and
   it IS isolated (the qrs tier). **Fix (v6):** correct the parenthetical.

9. **[MINOR — hostile] ζ₆₀ phases are lift artifacts.** A single product Par·W₁W₂ is not a
   commutator; under W₁ ↦ ζ₆₀W₁ the exponent 8 ↦ 9. Only the ratio ζ₁₅ is invariant.
   **Fix (v6):** state only the invariant ratio, or cut.

10. **[MINOR — correctness/overclaim] Abstract sign.** M₁₂−M₂₁ = mn(m−n) (as the proof
    body prints), not mn(n−m). **Fix (v6):** correct the abstract (harmless — enters
    squared).

11. **[MINOR — correctness] §3.2 genus form mislabeled.** (1,−9,−1) has disc 85; the
    actual disc-40 forms are (1,−6,−1) and (2,0,−5). The non-conjugacy conclusion is
    independently confirmed. **Fix (v6):** correct the forms.

12. **[MINOR — overclaim] Prose.** "unreasonably simple" → "elementary"; §1 "proves the
    square-root criterion" → "re-proves Northshield's"; "the method is part of the result"
    (×3) demoted to a methodological remark; "the failures are quantized" → "take
    perfect-square values" (firewall); "Markov spine" defined as the Fibonacci-WORD branch
    (1,2,5,13,194,… — not the conventional 1,2,5,13,34). All fixed in v6.

## Sound (verified, no change)
Lemma 2.2 + Sarnak provenance; Theorem A + uniqueness; Theorem B dictionary; Theorem C
(spine, Markov triples, Nielsen); Theorem D + D′ (Northshield; the m=6 non-principal
breather; the h⁺ ⟹ via the bijection); Prop E‴ residue −ω^{#L−#R} + Pisano-8; the E/E″
witnesses; Theorem F(i) + (2,3)-minimality + (iii); Theorem G(i) two-character formula +
all 36 cells + tier counts 120/20/20/10/70 + the read-off consequences; the magnitude law
25/25. **The firewall on physics CLAIMS holds** (overclaim seat: no physics/cosmology/
particle claim anywhere in the body; only metaphorical vocabulary, defensible).

## The hostile referee's honest bottom line (accepted)
"Not rejectable for being wrong — every computation is right — but vulnerable to
'decline in present form: unbundle §4 from the parabolic framing, delete/demote the two
curiosities, print enough digits, fix the legend.' All fixes are cheap; none need new
mathematics." v6 makes exactly these fixes.
