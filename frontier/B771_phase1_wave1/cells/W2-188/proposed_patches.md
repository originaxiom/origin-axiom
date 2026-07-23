# W2-188 (H114) -- proposed patches (PATCH PROPOSAL ONLY; no banked file edited)

Source: docs/HINT_LEDGER.md:269, H114. All facts below were independently re-derived
in-sandbox in `compute.py` (output in `output.txt`) before any patch text was drafted,
per WORKING_RULES #2/#12. Six patches: one kappa-naming annotation each in the two
homes of the T-UNIQ/T-KQ language (THEOREM_REGISTRY.md, B472/FINDINGS.md), one
cross-reference fix for the "missing-4" orphan (the flagship paper, S4.1), two
annotations for the two half-chain orphans (both B471 files), and one HINT_LEDGER.md
status update for H114 itself. `cc` (the merge gate) applies these at its discretion.

---

## Patch 1 -- docs/THEOREM_REGISTRY.md (T-UNIQ row, line 14): name the kappa-language

**File:** `docs/THEOREM_REGISTRY.md`
**Line:** 14

**OLD:**
```
| T-UNIQ | tr[A_m,A_n] = 2 − (mn(n−m))²; parabolic ⟺ (m,n) = (1,2). **MECHANISM (P4 panel, verified): for ANY symmetric pair in SL(2), tr[A,B] = 2 − (M₁₂−M₂₁)² with M = AB (since BA = (AB)ᵀ) — the square is the transpose/elliptic involution; the family content is M₁₂−M₂₁ = mn(n−m). Two-line proof; significance weight moves to the Cohn identification** | B471 (+panel) | `chain_verify.py` | **GATED (P4 rounds 1–2)**: PARTIALLY-KNOWN — mechanism classical (Sarnak reciprocal geodesics; Gehring–Martin δ=0 slice; Goldman/Fricke); (1,2) instance VERBATIM in Reutenauer 2009/2019 (the Markoff morphism); books anchor to fixed trace −2, no two-parameter family. OURS: coordinate lemma, metallic parametrization, uniqueness scan (vs Schmutz Schaller 2022, Nielsen) |
```

**NEW:**
```
| T-UNIQ | tr[A_m,A_n] = 2 − (mn(n−m))²; parabolic ⟺ (m,n) = (1,2). **MECHANISM (P4 panel, verified): for ANY symmetric pair in SL(2), tr[A,B] = 2 − (M₁₂−M₂₁)² with M = AB (since BA = (AB)ᵀ) — the square is the transpose/elliptic involution; the family content is M₁₂−M₂₁ = mn(n−m). Two-line proof; significance weight moves to the Cohn identification** | B471 (+panel) | `chain_verify.py` | **GATED (P4 rounds 1–2)**: PARTIALLY-KNOWN — mechanism classical (Sarnak reciprocal geodesics; Gehring–Martin δ=0 slice; Goldman/Fricke); (1,2) instance VERBATIM in Reutenauer 2009/2019 (the Markoff morphism); books anchor to fixed trace −2, no two-parameter family. OURS: coordinate lemma, metallic parametrization, uniqueness scan (vs Schmutz Schaller 2022, Nielsen). **κ-NAMING (H114, re-verified W2-188): T-UNIQ is the κ-theorem κ(m,n) := tr[A_m,A_n] = 2−(mn(n−m))², and the banked "Fricke invariant" x²+y²+z²−xyz = κ+2 exactly (symbolic identity, re-checked). κ(1,2) = −2 is the chain's CRITICAL (cusp-closing) level-set; tr(A₁) = 3 is the letter-tower's OFF-critical seed value.** |
```

---

## Patch 2 -- docs/THEOREM_REGISTRY.md (T-KQ row, line 55): name the kappa-language

**File:** `docs/THEOREM_REGISTRY.md`
**Line:** 55

**OLD:**
```
| T-KQ | the quantum commutator table; **THE CLOSURE THEOREM [W₁²,W₂³] = I** (CRT centrality); Q₈/SL(2,5) images; κ_q(1,1) = −1 | B472 | `kq_verify.py` | **GATED (2 rounds)**: iff = corollary of published halves (⟸ KR Cor. 6/Kelmer; ⟹ Appleby 2005 odd-dim injectivity — DOWNGRADE accepted); table/Q₈×SL(2,5) assembly/closure address/divisor lattice = ours scoped; magnitude law = Howe (verified 25/25) |
```

**NEW:**
```
| T-KQ | the quantum commutator table; **THE CLOSURE THEOREM [W₁²,W₂³] = I** (CRT centrality); Q₈/SL(2,5) images; κ_q(1,1) = −1 | B472 | `kq_verify.py` | **GATED (2 rounds)**: iff = corollary of published halves (⟸ KR Cor. 6/Kelmer; ⟹ Appleby 2005 odd-dim injectivity — DOWNGRADE accepted); table/Q₈×SL(2,5) assembly/closure address/divisor lattice = ours scoped; magnitude law = Howe (verified 25/25). **κ-NAMING (H114, re-verified W2-188): κ_q is the quantum-stage counterpart of the classical κ; the 36-cell divisor-lattice census (paper S4.3, gx=gcd(j,20)×gy=gcd(l,12)) was re-derived from scratch (240/240 points, two primes 61/421, pure-integer CRT cross-check) — clean, no missing or mismatched cell at gx=4 or gy=4; see paper S4.1 patch for the specific j=4-row cross-reference this census motivates.** |
```

---

## Patch 3 -- frontier/B472_quantum_commutator/FINDINGS.md (lines 61-63): close the H114 pointer

**File:** `frontier/B472_quantum_commutator/FINDINGS.md`
**Lines:** 61-63

**OLD:**
```
3. **The κ-naming pass** (seat-2): the uniqueness theorem is a κ-theorem; the towers are
   κ-level-sets (chain κ = −2, letter-tower κ = 3 = tr A₁); the banked "Fricke invariant"
   = κ + 2. One documentation session; H114.
```

**NEW:**
```
3. **The κ-naming pass** (seat-2): the uniqueness theorem is a κ-theorem; the towers are
   κ-level-sets (chain κ = −2, letter-tower κ = 3 = tr A₁); the banked "Fricke invariant"
   = κ + 2. One documentation session; H114. **RUN (W2-188, frontier/B771_phase1_wave1/
   cells/W2-188/): the identity Fricke-invariant = κ+2 and both level-set readings
   re-verified symbolically (sympy, exact); the pass's three named orphans (the
   missing-4 operator-order census, the half-chain 3-phase quasi-invariant, the
   silent-word field shadows) were located and re-derived in-sandbox — see the B471
   patches below and the paper S4.1 patch.**
```

---

## Patch 4 -- frontier/B471_chain_verification/CHAIN_SCOUT_FINDINGS.md (lines 56-60): de-orphan both W3 items

**File:** `frontier/B471_chain_verification/CHAIN_SCOUT_FINDINGS.md`
**Lines:** 56-60

**OLD:**
```
- OBSERVATION (plainly, small-number caution): silent-word fields read sqrt3 (n=2),
  sqrt35 = sqrt5*sqrt7 (n=5); n=3 breathing word at sqrt10 (the May class-number-2 field).
  Real shadows of the program's imaginary fields surfacing on the half-chain. NOT built upon.
- OBSERVATION: the half-chain's cubic is NOT conserved but is a 3-PHASE QUASI-INVARIANT
  (constant on two of three Pisano phases: 13; 29,29; 1133; 40325,40325; ...). Open.
```

**NEW:**
```
- OBSERVATION (plainly, small-number caution): silent-word fields read sqrt3 (n=2),
  sqrt35 = sqrt5*sqrt7 (n=5); n=3 breathing word at sqrt10 (the May class-number-2 field).
  Real shadows of the program's imaginary fields surfacing on the half-chain. NOT built upon.
  **DE-ORPHANED (H114/W2-188): re-derived from scratch (exact integer arithmetic on
  s_{n+1}=s_n s_{n-1}, s0=X_2, s1=X_1); all three values reproduced exactly on the nose
  (n=2 disc=12 -> sqrt3; n=5 disc=20160 -> sqrt35; n=3 metallic-disc=40 -> sqrt10).
  Mechanism named: silent words (det s_n = +1) carry the cover-form disc v_n^2-4;
  breathing words (det s_n = -1) carry the metallic-form disc v_n^2+4; dets follow the
  exact period-3 pattern (-,-,+) from n=0. Still NOT built upon (no further structure
  claimed); the mechanism is now attached, not floating. compute.py in
  frontier/B771_phase1_wave1/cells/W2-188/.**
- OBSERVATION: the half-chain's cubic is NOT conserved but is a 3-PHASE QUASI-INVARIANT
  (constant on two of three Pisano phases: 13; 29,29; 1133; 40325,40325; ...). Open.
  **DE-ORPHANED (H114/W2-188): re-derived exactly; the quoted sequence reproduced
  digit-for-digit. Mechanism named precisely: grouping consecutive cubic values
  x^2+y^2+z^2-xyz (x,y,z = 3 consecutive half-chain traces) into blocks of 3
  (indices 3k,3k+1,3k+2), the LAST TWO entries of every block coincide exactly
  (verified k=0..3) while the first differs -- i.e. two of the three phases within
  each period-3 block agree, not two of three residues mod 3 globally (the cubic
  is genuinely unbounded block-to-block: 13,1133,4.3e11,... on the first phase).
  "Open" still stands for WHY the tail-pair coincidence holds (no proof attempted
  here, only the exact re-derivation and the precise restatement of what "3-phase"
  means). compute.py in frontier/B771_phase1_wave1/cells/W2-188/.**
```

---

## Patch 5 -- frontier/B471_chain_verification/FINDINGS.md (lines 46-50): confirm the banked summary line

**File:** `frontier/B471_chain_verification/FINDINGS.md`
**Lines:** 46-50

**OLD:**
```
- The half-chain: the twisted Fricke law v_{n+1} = v_n v_{n−1} − det(s_{n−1})·v_{n−2}
  (**the breath is the sign in the composition law**) and the field-form selection:
  breathing words (det −1) carry the metallic form v²+4; silent words (det +1) the cover
  form v²−4 — BR-N riding the word tower. Half-chain discs confirm their small-number
  notes (5, 8, 40 → √10, 20160 → √35) — noted, not built upon.
```

**NEW:**
```
- The half-chain: the twisted Fricke law v_{n+1} = v_n v_{n−1} − det(s_{n−1})·v_{n−2}
  (**the breath is the sign in the composition law**) and the field-form selection:
  breathing words (det −1) carry the metallic form v²+4; silent words (det +1) the cover
  form v²−4 — BR-N riding the word tower. Half-chain discs confirm their small-number
  notes (5, 8, 40 → √10, 20160 → √35) — noted, not built upon. **RE-VERIFIED (H114/
  W2-188): the composition law and both field-form claims hold exactly on a fresh
  from-scratch build (n=0..8); κ-naming cross-reference: this v²∓4 pair is the
  half-chain's own two κ-level-sets (κ=∓4 in the trace-discriminant sense), the
  det-parity playing the same role here that critical/off-critical κ plays for the
  full chain (T-UNIQ). No new claim beyond the confirmation.**
```

---

## Patch 6 -- papers/P4_markov_stage/DRAFT_v8.md (lines 414-426): the missing-4 cross-reference

**File:** `papers/P4_markov_stage/DRAFT_v8.md`
**Lines:** 414-426

**OLD:**
```
### 4.1 The commutator table

tr[W₁ʲ, W₂ˡ], 1 ≤ j, l ≤ 5 (exact in ℚ(ζ₆₀); verified in three independent lifts —
the commutators are lift-independent by Proposition 4.0):

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |
```

**NEW:**
```
### 4.1 The commutator table

tr[W₁ʲ, W₂ˡ], 1 ≤ j, l ≤ 5 (exact in ℚ(ζ₆₀); verified in three independent lifts —
the commutators are lift-independent by Proposition 4.0). **Row j=4 is IDENTICAL to
row j=2 in this 5×5 sample; this is a computed coincidence of the divisor-lattice
census of S4.3, not a duplication: rows j=2 and j=4 are the DISTINCT lattice points
gx=gcd(2,20)=2 and gx=gcd(4,20)=4 (ord(W₁)=20), which merely agree on VALUE (not on
tier — see S4.3) at every gy = gcd(l,12) sampled here (l=1..5, i.e. gy∈{1,2,3,4,1}).
They first diverge in tier at gy=12 (l=12): (gx=2,gy=12) is "dark", (gx=4,gy=12) is
"qrs". Re-derived exactly, both primes, all 240 points, W2-188.**

|      | l=1 | l=2 | l=3 | l=4 | l=5 |
|------|-----|-----|-----|-----|-----|
| j=1  | −1  | 3   | −5  | 3   | −1  |
| j=2  | 3   | 3   | 15  | 3   | 3   |
| j=3  | −1  | 3   | −5  | 3   | −1  |
| j=4  | 3   | 3   | 15  | 3   | 3   |
| j=5  | −5  | 15  | −5  | 15  | −5  |
```

---

## Patch 7 -- docs/HINT_LEDGER.md (line 269): close H114

**File:** `docs/HINT_LEDGER.md`
**Line:** 269

**OLD (the row's STATUS/RESOLUTION/CONSEQUENCE columns, the fifth/sixth/seventh
pipe-fields of the row; full row given for exact match):**
```
| H114 | (both seats, 2026-07-08) THE κ-NAMING PASS: the banked "Fricke invariant" = κ + 2; T-UNIQ is a κ-theorem (κ(m,n) = 2 − (mn(n−m))²); the towers are κ-level-sets (chain κ = −2 critical, letter-tower κ = 3 = tr A₁ off-critical); the "interacting register" was probed all saga under the name "chain". Naming collision #6 — at the door itself. | TASK | 2026-07-08 | OPEN | — | One documentation session: annotate the banked files with the κ-language; convert the negative laundering law to its positive face (C5, the laundering group). Orphans to de-orphan in the same pass: the missing-4 in the operator-order census; the half-chain 3-phase quasi-invariant; the silent-word field shadows (√3, √35). |
```

**NEW:**
```
| H114 | (both seats, 2026-07-08) THE κ-NAMING PASS: the banked "Fricke invariant" = κ + 2; T-UNIQ is a κ-theorem (κ(m,n) = 2 − (mn(n−m))²); the towers are κ-level-sets (chain κ = −2 critical, letter-tower κ = 3 = tr A₁ off-critical); the "interacting register" was probed all saga under the name "chain". Naming collision #6 — at the door itself. | TASK | 2026-07-08 | **CHECKED → W2-188 (patch proposal, B771 Phase-1 Wave-2)** | — | One documentation session: annotate the banked files with the κ-language; convert the negative laundering law to its positive face (C5, the laundering group). Orphans to de-orphan in the same pass: the missing-4 in the operator-order census; the half-chain 3-phase quasi-invariant; the silent-word field shadows (√3, √35). **All four sub-items re-derived in-sandbox and located (W2-188/compute.py): the naming identity + both level-sets (sympy, exact); the missing-4 census resolved to the S4.3 36-cell divisor-lattice table (paper, re-verified 240/240 points, 2 primes) with the j=4/j=2 row coincidence in S4.1 now cross-referenced; the half-chain 3-phase quasi-invariant reproduced digit-for-digit with its block mechanism named; the silent-word shadows (√3 at n=2, √35 at n=5, √10 at n=3 breathing) reproduced exactly. The C5 "laundering group" positive-face reframe is NOT attempted here (out of this cell's located scope; no source file was found defining a "negative laundering law" convertible to "C5" — named as a residual, not silently dropped).** |
```

---

## Residual (named, not silently dropped)

The H114 hint also asks to "convert the negative laundering law to its positive face
(C5, the laundering group)." A repo-wide search (`grep -rn "laundering"`) turns up the
*phenomenon* described repeatedly (composition "does not launder — it escalates",
B470/RFZ; "the level sees only the interaction mod 15", B472) but no prior artifact
named literally "the laundering group" or "C5" in this sense. This sub-item is a
NEW naming/definition task, not a de-orphaning of an existing computed object — it is
out of this cell's scope (H114 lists it in the same sentence as the Fricke-invariant
annotation, not among the three explicitly enumerated orphans that follow). Recorded
here so it is not silently absorbed into "pass completed."
