# THE TUBE'S OWN τ ALONG L⁶R(LR)^k, k = 1..5, TOWARD k → ∞ (THE OWNER'S "τ's k → ∞ LIMIT"; P-727, B1847 § 8, B1852; DATA-FREE; PRE-REGISTERED, AMENDED TWICE BEFORE THE AFFECTED RUNS): AN INDEPENDENT INSTRUMENT, SEALED BEFORE ITS RUN, READS THE METRIC'S OWN FIBRE MODULUS AT THE TUBE OF L⁶R(LR)^k FOR k = 1..5. AT k = 1 IT IS 0 + 6.14916(41)i: INSIDE B1847'S 6.15 ± 0.15 WITH AN ERROR ABOUT 370 TIMES SMALLER, AND WITH Re τ = 0 AS B1852 PROVED. ALONG THE FAMILY IT READS 6.14916, 6.08186, 6.06868, 6.06597 AND 6.06541, EACH WITH Re τ = 0, WHILE THE ANTI-APEX SITS AT Re ½. THE k-STEPS SHRINK BY 5.1, 4.9 AND 4.8, AND AITKEN ON k = 3, 4, 5 GIVES τ_∞ = 0 + 6.06526(57)i. SO THE METRIC'S OWN READING HAS AN ESTIMATED VALUE IN THE ONE-DEPARTURE LIMIT, WITH NO k CHOSEN. IT IS PURELY IMAGINARY, LIKE (N2)'S τ*₆ = i√5φ ≈ 3.618i, BUT ABOUT 1.68 TIMES HIGHER. WHICH CONSTRUCTION THE READ-OUT USES STAYS MAIN'S TO RULE (P-714). P1, P2, P4 AND P5 HOLD; P3 (THE CORE AT AN INTEGER LEVEL OF THE CUSP GAUGE) FAILS AT k = 2, 3 AND 4, WHICH CHANGES NOTHING ELSE. TWO AMENDMENTS, EACH COMMITTED BEFORE ITS RUN, FIXED FAILURES THAT STOPPED MEMBERS BEFORE ANY SURFACE: A SNAPPY CHECK, AND A MESH LOOKUP NOW COMPLETED BY PROPAGATION ACROSS THE FACE PAIRINGS, BITWISE IDENTICAL ON k = 1, 2 AND 5. BEFORE THE SEAL A REDUCED COPY FOUND THREE FAULTS. AMONG THEM: τ = (−E₁₂ + i)/E₂₂, THE FORMULA B1847'S SCRIPTS ALSO USE, DEPENDS ON THE CYCLE BASIS AT THE SIZE OF det E − 1, AND THE ROOT OF THE ENERGY FORM REMOVES THAT. DATA-FREE; NO COUPLING, SCALE OR RATIO OF SCALES IS COMPUTED

**On:**
- the owner's choice "τ's k → ∞ limit": the metric's own fibre modulus τ(Σ₀) at the tube, taken toward its k → ∞ limit
  with an independent instrument;
- P-727 and B1847 § 8 (Im τ(Σ₀) = 6.15 ± 0.15 at k = 1, Re unresolved), B1852 (Re τ = 0 at the k = 1 tube, by
  topology), and 66e4ed4ec ("Its value, under τ(Σ₀), is the k → ∞ limit, if it exists, which waits on P-727's
  instrument").

Main read at `d46e69cea` (S306k, B1852). This seat's branch: `ee1338c23` (sealed), `5fc903068` (amendment 1),
`3bc36d9c9` (amendment 2), `f869c637d` (the outputs). Data-free: τ is a modulus of the object, not a held-out quantity.
No coupling, scale or ratio of scales is computed, and nothing is compared with data.

**Swept first:** `VERDICT topic-sweep /P-727|τ\(Σ₀\)|k → ∞|reversing involution/ (full text): 12 of 1598 arcs on main
match (NEGATIVE 2, PROVED 10); 6 register rows match (DONE 2, QUEUED 4)`. B1846, B1847 and B1852 carry the tube's
modulus. No arc computes it beyond k = 1.

## 1. The instrument (independent of main's meshers)

`relays/chat1_2026-11-07_tau/tauinst.py`, one file; nothing in it reads a measured value.

- **Geometry.** SnapPy's developed ideal tetrahedra and face pairings; the cusp at ∞, with the maximal cusp at height 1;
  χ from the relators' exponent sums; the cusp lattice (p₁: χ = 0, the fibre's boundary; p₂: χ = 1); and the Ford
  sphere set, closed under products of floor-visible elements and checked against SnapPy's volume.
- **Harmonic time** h, by Hejhal collocation in the cusp's Fourier–Bessel expansion (R = 10.5) at pulled-back points.
  There is no constant term, so the additive constant is the cusp gauge.
- **The level surface** {h = s mod 1}, by marching tetrahedra on an intrinsic simplicial mesh of the truncated manifold
  (cusp cross-section at height 6, two red refinements):
  - exact crossings;
  - nodes near the level snapped, then re-projected onto it;
  - 1-to-4 subdivisions, each new vertex projected onto the exact level along grad h.
- **The modulus.**
  - A cone over the cusp hole, intrinsic Delaunay flips, the cotangent Laplacian and a tree–cotree basis give the
    harmonic 1-forms and their energy matrix E.
  - τ is the root in the upper half-plane of E₂₂t² + 2E₁₂t + E₁₁, oriented by ∫α∧β and reduced.
- **Extrapolation in n:** Richardson with ratio 4 from the last two n. The error adds the distance from Aitken's
  three-point value and from the Richardson value one step earlier. Every error quoted here is an extrapolation error,
  in n (and for τ_∞ in k), at fixed cusp height 6, R = 10.5 and two refinements.
- **Exact, in integers (B1852's method):** every reversing involution J (det −1, J φ J = φ⁻¹, entries up to 14), and the
  mod-2 classes of J and φJ, the two σ-fixed fibres.

## 2. The seal, and two amendments made after it

- **Sealed at `ee1338c23`** (`prereg_sha256.txt`): the instrument, the driver `tau_k_limit.py` (pass rules C1–C8,
  predictions P1–P5, the k → ∞ estimate) and `run_chain.sh`, before any run. The runs: m004 and k = 1, 2, 3 in one
  chain and k = 4, 5 in the other, in parallel.
- **Amendment 1, `5fc903068`.** In the sealed run, k = 4 and k = 5 stopped at C3's SnapPy check ("The Dirichlet
  construction failed") before any surface. `tau_k_limit_a1.py` reads SnapPy's spectrum from isometric copies with
  randomized triangulations when that construction fails. Nothing else changes.
- **Amendment 2, `3bc36d9c9`.** The sealed mesh takes each developed vertex's horoball from a word-search lookup. In the
  sealed run k = 3 stopped there ("cusp point not found"), and under amendment 1 so did k = 4, both before any surface.
  - `tauinst_a2.py` keeps the lookup and carries its radii across the fundamental polyhedron's face pairings to the
    vertices it misses (one of 15 vertex classes on k = 3, two of 18 on k = 4): for A = ((a, b), (c, d)) taking x_b to
    x_a, r_a = r_b / |c x_b + d|. Its lookup now requires both lattice coordinates to match; the sealed assertion tested
    only the first.
  - Every vertex reached twice, or both found and reached, agrees to 10⁻⁹ (asserted).
  - On k = 1, 2 and 5 the amended mesh is bitwise identical to the sealed one (tested outside the repository on the
    meshes alone, as `prereg_a2_sha256.txt` records; the referee's independent rebuild found m004's identical too), so
    those results stand. k = 5's result is amendment 1's run (its lookup finds every vertex once the sphere set is
    closed).
- **Neither amendment touches** a pass rule, a prediction, a level, a parameter or the summary. Each was committed with
  its sha256 before its run. The stopped attempts' logs are kept (`tau_k3_attempt1_*`, `tau_k4_attempt1_*`,
  `tau_k4_attempt2_*`, `tau_k5_attempt1_*`).

## 3. Three faults found before the seal, and a note on B1847's formula

A reduced copy of the driver (no tube level, no anti-apex of k ≥ 2) was smoke-run outside the repository. It found
three faults in this seat's development code, all fixed before the sha256 was recorded.

1. **The subdivision's midpoint key.** One projected midpoint was shared per (frame, vertex pair). On a frame whose faces
   are glued to each other, the same surface edge sits at two places in that frame, so one copy received the other's
   midpoint. The two sides of an edge then disagreed in length by up to a factor 6.5, and the moduli at n ≥ 1 on the
   σ-fixed levels blew up (det E ~ 10²⁷¹). The key now includes the unprojected midpoint, rounded to 10⁻⁸.
2. **Needles.** Nodes just outside the 10⁻⁶ snapping band made triangles with edges near 10⁻⁶ beside edges near 10⁻⁴.
   Their near-straight angles are set by the rounding of the lengths. The band is now per node: max(10⁻⁶, 10⁻² × the
   largest |Δh| on the node's mesh edges), so no crossing falls within 1 % of an edge's end. On m004's σ-level the
   shortest n = 0 edge went from 1.6 × 10⁻⁶ to 3.2 × 10⁻⁴.
3. **The modulus formula.** τ = (−E₁₂ + i)/E₂₂ depends on the order of the two cycles at the size of det E − 1. A
   10⁻¹³ shift of s (or 10⁻¹² perturbations of the lengths) reordered the tree–cotree cycles, and the n = 1 modulus at
   k = 1's s = ½ moved from −0.5 + 1.58247i to 0.49807 + 1.58858i: the same E with its cycles swapped. The root of the
   energy form, τ = (−E₁₂ + i√det E)/E₂₂, is covariant under a change of basis (E ↦ AEAᵀ moves it by A's Möbius map) and
   equals the old formula when det E = 1. After the change, eight perturbations give one reduced τ, and the convergence
   in n became monotone with ratios near 4.

**For main (B1847).** `stage_b_modulus.py:327`, `stage_c_general.py:274`, `stage_e_gamma.py:343` and
`stage_a_control.py` (lines 208 and 318) compute τ = complex(−E12/E22, 1/E22).
- That reading depends on the cycle basis at the size of det E − 1.
- At the tube, § 8 records det E − 1 near −1.6 % ("the 1–2 % det E systematic near s = 0"), so the basis-dependent
  part there is of that order. That is at s = 0 exactly, where § 8 says its meshers degenerate. Its readings just off
  s = 0 carry −0.6 % to −2 %, and its result is their s → 0 limit. The root changes Im τ by a factor √det E or its
  inverse, at most about 1 % there (0.06), inside the ± 0.15.
- With main's fixed geometric basis the reading is deterministic, and the covariant root would remove that part.
- Limits taken as det E → 1 are the same under either formula.

## 4. Results

Every pass rule holds for every member:
- C1, C2, C4, C5 and C8 on m004;
- C2, C3, C4, C6, C7 and C8 on k = 1;
- C2, C3 and C4 on k = 2..5.

Every final run's exit code is 0, and its stderr holds only plink's missing-tkinter warning (the four stopped attempts
exit 1 with tracebacks). The moduli are R4 values, with the errors of § 1. At the σ-fixed levels the real parts sit on
0 and ½ at every n to within 3 × 10⁻⁹.

**The controls.**
- **m004.** τ(Σ_¼) = i at every n, to 10⁻¹³. The mesh carries the square torus's two symmetries (m004's
  triangulation is preserved by its isometries), and the covariant root keeps them. τ(Σ₀) = ½ + 1.124381(27)i, against
  B1847's 1.12438.
- **k = 1.** τ(Σ_½) = ½ + 1.590345(42)i, against B1847's 1.5904. τ(Σ_¼) = 0.372179(23) + 1.008503(69)i, against
  −0.3722 + 1.0085i (the mirror, as disclosed).
- **The other checks.**
  - B1295's coefficient reads 4.2609826349.
  - Every Ford volume is within 2.6 × 10⁻⁶ (relative) of SnapPy's.
  - Hejhal's residuals are at most 9.7 × 10⁻¹¹, and the paired faces agree to 1.2 × 10⁻¹¹ or better.
  - h is constant on every core to 1.6 × 10⁻¹¹.

**The members.** The tube is the σ-fixed level through the systole; the anti-apex is σ's other fixed level, s₀ + ½.

| k | systole's real length (= SnapPy's) | core level s₀ (cusp gauge) | \|dθ\| on the core | reversing involutions | τ at the tube | τ at the anti-apex |
|---|---|---|---|---|---|---|
| 1 | 0.18486980 | 0 | 0.041999 | 4, opposite classes | 0 + 6.14916(41)i | ½ + 1.59035(4)i |
| 2 | 0.18519963 | 0.534940 | 0.026548 | 4, opposite | 0 + 6.08186(42)i | ½ + 0.96047(3)i |
| 3 | 0.18521766 | 0.755893 | 0.019516 | 2, opposite | 0 + 6.06868(42)i | ½ + 1.20896(2)i |
| 4 | 0.18521832 | 0.072840 | 0.015484 | 2, opposite | 0 + 6.06597(42)i | ½ + 1.08763(3)i |
| 5 | 0.18521828 | 0 | 0.012852 | 2, opposite | 0 + 6.06541(42)i | ½ + 1.14157(3)i |

- **The tube's convergence in n is the same for every member.**
  - The n-steps shrink by 2.5, 3.35 and 3.84.
  - det E − 1 falls from 3.4–3.5 × 10⁻² at n = 0 to 2.1–2.2 × 10⁻⁴ at n = 4.
  - Richardson and Aitken agree to 1.1 × 10⁻⁴.
- **The k-differences are much steadier than the values.** The two the estimate uses settle to about 10⁻⁶ in n:
  k = 4 → 5 reads 0.000563 at both n = 3 and 4, and k = 3 → 4 reads 0.002708 and 0.002706 (k = 2 → 3 moves by
  1.1 × 10⁻⁵). So the ±4.2 × 10⁻⁴ on each value is almost all the shared extrapolation in n.
- **C3's SnapPy side** needed amendment 1's randomized copies on k = 4 (twelve copies) and k = 5 (three). The
  randomizations are unseeded, so a rerun draws a different number; only the length is compared.

## 5. The predictions, as sealed

- **P1 holds.** k = 1's Im τ(Σ₀) = 6.14916(41) lies inside B1847 § 8's 6.15 ± 0.15, with an error about 370 times
  smaller.
- **P2 holds for every member.** The tube's reduced Re τ is 0, and the anti-apex's |Re τ| is ½, at every n to 3 × 10⁻⁹:
  B1852's real part at k = 1, and the same split at k = 2..5.
- **P3 fails.** The core's level is an integer in the cusp gauge only for k = 1 and 5. For k = 2, 3 and 4 it is
  0.534940, 0.755893 and 0.072840.
  - The prediction carried k = 1's gauge to every member, and that was the error. The tube level is σ-fixed all the
    same: σ maps the unique systole to itself, and h ∘ σ = −h + c then forces 2·h(core) ≡ c (mod 1). In the cusp gauge
    c vanishes only for some members.
  - The driver used s₀ = h(core) mod 1 throughout, so nothing else depends on P3.
- **P4 holds.** The tube's k-steps are 0.067298, 0.013177, 0.002706 and 0.000562, each smaller than the last, and the
  last is 0.009 % of Im τ₅.
- **P5 holds.** For k = 2..5, every reversing involution puts the two fibres in opposite classes (4, 2, 2 and 2 of them),
  as B1852's even-run pattern says for words with one even run. C8 reproduced B1852's table for m004 (12, both ≢ I)
  and k = 1 (4, opposite).

## 6. The k → ∞ estimate

- **As sealed** (Aitken's Δ² on k = 3, 4, 5; the two steps share a sign and shrink): **τ_∞ = 0 + 6.06526(57)i.** The error
  is |τ_∞ − τ₅| = 0.00015 plus the largest member error, 0.00042.
- **The steps shrink roughly geometrically:** ratios 5.11, 4.87 and 4.81 from k = 1 → 2 on, still drifting. The real part is 0 at every k, so the
  limit's is 0.
- **Every member from k = 2 on reads within 0.017 of τ_∞, and k = 4 and 5 within 0.0008.**

**The anti-apex (secondary) alternates with k's parity.**
- Odd k: 1.590, 1.209, 1.142 for k = 1, 3, 5. Even k: 0.960, 1.088 for k = 2, 4.
- Its two k-steps over 3, 4, 5 have opposite signs, so, as sealed, no limit is stated.
- The odd values fall and the even ones rise, both toward the neighbourhood of m004's σ-level ½ + 1.12438i, as the
  anti-apex fibre plausibly sinks into the (LR)^k block. That is an observation, not a sealed claim; nothing computed
  here shows the mechanism.

## 7. What this does for the goal

- **Under the metric's own reading, τ now has an estimate of its one-departure value.** 66e4ed4ec named the k → ∞
  limit as the value that reading needs. Its sealed estimate (Aitken on k = 3, 4, 5) is τ_∞ = 0 + 6.06526(57)i, with
  no k chosen; no member at k = ∞ is computed. This seat's k = 1 value (the member P-727 banked at 6.15 ± 0.15) is its
  first term, 0.084 above it.
- **It is purely imaginary, like (N2)'s value, but not equal to it.** (N2)'s τ*₆ = i√5φ ≈ 3.618i lies on the same axis
  at about 0.60 of this height. At k = 1, B1847 § 8 found the metric's reading about 1.7 times the Teichmüller apex at
  the tube (3.65).
- **What stays chosen for τ:**
  - the construction itself: (N2)'s Teichmüller reading, the pleated or the tetrahedron reading, or the metric's own
    τ(Σ₀) (P-714's four; main's to rule);
  - point or weight on closed members;
  - the family, the one-departure history with reading (ii)'s run of 6.
- **The line and the scale are untouched.** No coupling, scale or ratio of scales is computed.

## 8. What this asks of main (owed, not done here)

1. **Harvest the row** and move the pin to this relay's commit.
2. **The modulus formula in B1847's scripts** (§ 3). The covariant root removes the cycle-basis part of § 8's "1–2 %
   det E systematic near s = 0"; the rest is the mesh's. This seat's k = 1 value sits inside B1847's band, so nothing
   in B1847's result moves. Main may still want the root for any later reading near the tube.
3. **P-714.** The metric's own reading now has an estimated value in the one-departure limit. Which of the four readings the
   read-out uses is still main's to rule; this relay does not choose.
4. **B1852's pattern.** Its exact classes hold for four more words here (k = 2..5), and the numerics put the tube at
   Re 0 in each. Whether that suffices to state the pattern for the family, or a proof from the cyclic word is needed,
   is main's call.
5. **Main's suggested next work** for this seat (whether R2's exact block is a ratio of two scales) is not taken up
   here. The owner's choice was τ's k → ∞ limit.

## Not claimed

- That the metric's own τ is the read-out's τ, or that it replaces (N2). The construction stays a choice (P-714).
- That the k → ∞ limit exists as a theorem. It is estimated from five members, with the stated error, and the steps'
  geometric ratio is observed, not derived.
- Any closed form for τ_∞, or any limit for the anti-apex.
- Anything about the line or the scale. No coupling, scale or ratio of scales is computed; nothing is compared with data.
- That B1847's numbers are wrong. Its controls agree with this instrument's to the stated tolerances, and its k = 1 band
  holds this seat's value.

## Disclosures

- **Development before the seal** (outside the repository):
  - the instrument was built on m004 (s = ¼, 0) and on L⁶RLR at s = ½ and ¼;
  - L⁶RLR's core (χ, h on its axis, |dθ|) was computed;
  - the control levels' series were seen under the final instrument (m004 at s = 0 and ¼ to n = 3; k = 1 at s = ¼ to
    n = 3 and at s = ½ to n = 2), and the faults were fixed until they agreed with main.

  So C5 and C6 test agreement with B1847, not a blind prediction. No tube level of any member, and no anti-apex of
  k = 2..5, was extracted before the seal.
- **Read before the predictions:** B1847's numbers, including 6.15 ± 0.15, and B1852's result, table and even-run
  pattern. P1, P2 and P5 lean on them by design.
- **Seen before each amendment's seal.**
  - *Amendment 1:*
    - k = 4's and k = 5's lines up to the SnapPy stop;
    - SnapPy's shortest real lengths for k = 1..5, from a test of the fallback outside the repository;
    - m004's complete results and k = 1's log as far as it had run.

    `tau_k_limit_a1.py` was written after k = 4's stop. Its "k = 5 failed the same way" came from that SnapPy-only
    test, and the record and the commit follow both stops.
  - *Amendment 2:*
    - k = 3's and k = 4's lines up to the mesh stop (h on the core included);
    - k = 1's, k = 2's and m004's complete results;
    - k = 5's amendment-1 run up to its tube level at n = 3.
  - No amendment changes a pass rule, a prediction or the summary.
- **Orientation.** This instrument's orientation is the mirror of main's at s = ¼, so |Re τ| is what is compared.
- **Main's code was read, not run:** B1847's `stage_*` scripts, for the formula note only. B1847's and B1852's findings
  were read through this seat's mask.

**Refereed read-only:** READY WITH CORRECTIONS (3 errors, 15 suggestions). The errors and suggestions 1–14 are
applied; suggestion 15 concerns future runs only. The referee rebuilt the meshes with both instruments and found m004,
k = 1, 2 and 5 byte-identical, and recomputed every extrapolation to 10⁻⁹.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE TUBE'S OWN τ ALONG L⁶R(LR)^k, k = 1..5, TOWARD k → ∞ (the owner's "τ's k → ∞ limit"; P-727, B1847 § 8, B1852; data-free; pre-registered, amended twice before the affected runs) | "An independent instrument, sealed before its run, reads the metric's own fibre modulus at the tube of L⁶R(LR)^k for k = 1..5. At k = 1 it is 0 + 6.14916(41)i: inside B1847's 6.15 ± 0.15 with an error about 370 times smaller, and with Re τ = 0 as B1852 proved. Along the family it reads 6.14916, 6.08186, 6.06868, 6.06597 and 6.06541, each with Re τ = 0, while the anti-apex sits at Re ½. The k-steps shrink by 5.1, 4.9 and 4.8, and Aitken on k = 3, 4, 5 gives τ_∞ = 0 + 6.06526(57)i. So the metric's own reading has an estimated value in the one-departure limit, with no k chosen. It is purely imaginary, like (N2)'s τ*₆ = i√5φ ≈ 3.618i, but about 1.68 times higher. Which construction the read-out uses stays main's to rule (P-714). P1, P2, P4 and P5 hold; P3 (the core at an integer level of the cusp gauge) fails at k = 2, 3 and 4, which changes nothing else. Two amendments, each committed before its run, fixed failures that stopped members before any surface: a SnapPy check, and a mesh lookup now completed by propagation across the face pairings, bitwise identical on k = 1, 2 and 5. Before the seal a reduced copy found three faults. Among them: τ = (−E₁₂ + i)/E₂₂, the formula B1847's scripts also use, depends on the cycle basis at the size of det E − 1, and the root of the energy form removes that. Data-free; no coupling, scale or ratio of scales is computed" | `relays/CHAT1_TO_CC_2026-11-07_THE_TUBES_TAU_TOWARD_K_INFINITY.md` @ the commit adding it | — | P-727, P-714, B1846, B1847, B1852, B1295 | 2026-11-07 |

0 of 19.
