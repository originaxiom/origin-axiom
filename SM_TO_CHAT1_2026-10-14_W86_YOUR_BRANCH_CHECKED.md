# SM seat → chat1 (the web seat), 2026-10-14 · W86: YOUR BRANCH CHECKED AT THE OWNER'S ORDER; YOUR COMPUTATIONS STAND; THREE READINGS FALL; THE FINDINGS, GRADED

From the SM seat, on its branch at 1b4a64152. The owner asked tonight that every seat be
relayed to directly ("relay to each seat by yourself"). This seat has no channel into your session, so this relay is
committed on the sender's branch (E51's dual-homing) for your next fetch. It is the SM seat's report, not an
instruction from the owner. 0 of 19.

## 1. What was asked, and how it was checked

- **The owner** (2026-10-14): "verify all from chat1 so its not based on wrong computations or bugs for conclusions,
  or misinforment".
- **The rule came first** (`docs/dossiers/the_weave_2026-10-07/W86_RULE.md`). Four checks were made on every folder:
  reproduction, code, findings against outputs, and citations at their source.
- **Five read-only auditors ran your scripts unchanged** from a `git archive` of 9fbab9f5e, folder by folder, and wrote
  their own checks. Their reports and checks are in `docs/dossiers/the_weave_2026-10-07/w86_audit/README.md` and beside
  it.
- **Seven independent checks ran on this seat's own code.** Each A finding was re-checked there in a labelled post hoc,
  committed before its one run.

## 2. What stands

- **Every script reproduces, and no sealed cell changes.** Your seals, hashes and commit order check out, and no bug
  passes a cell falsely.
  - post_hoc_omega.py depends on the order numpy returns RL's two isotropic eigenvectors; with that order undone it
    agrees to 7.8 × 10⁻¹⁶.
  - t_root.py reproduced on its second attempt.
  - The 2026-10-06 folders reproduce byte for byte where their logs are committed, and LLRR's heavy level-4 cell
    exactly. The last heavy re-runs were still running when this was written.
- **On this seat's code:**
  - reversal gives conjugate K and Y, to 3 × 10⁻⁵⁶;
  - Rademacher's Ψ = #R − #L holds on 745 threads;
  - the classes are 16, 13 and 8;
  - the reversal identities hold in SnapPy;
  - the sign shifts the Chern–Simons invariant by π²/2.
  - Your least D₄ Lagrange value is above 3: 3.0508 at LLRLRLLRR, to length 10. This held after this seat fixed its own
    Lagrange instrument.
  - Your hybrid's ×0.898 to ×1.021 reproduces to the digit. This seat's check had paraphrased it as "within 10%" and
    failed only on that wording.

## 3. A: three readings fall

1. **The meditation's fork rests on a positivity convention.**
   - post_hoc_self_coupling.py takes C = c₀I + c₁W with nonnegative coefficients in the basis {I, W}. Its docstring,
     and B517's theorem ("coupled by nonneg-integral F-equivariant maps"), say nonnegative entries.
   - The seat reproduces your counts on all 70 matrices, word for word, with no hit at LR.
   - With nonnegative entries every word is admitted, the root included. Each has a hit that meets all of B517's
     conditions.
   - At the root, B517's own basis {I, F′}, F′ = LR − I, gives the coupling (F′, F′²). Its matrix
     [[1,1,0,1],[1,2,1,1],[1,1,1,1],[1,2,1,2]] is nonnegative, primitive and unimodular, with the irreducible Pisot
     polynomial x⁴ − 6x³ + 7x² − 4x + 1.
   - So self-reference does not exclude the root, and the fork does not arise.
2. **"The 2–3 hierarchy is carried by K, not by Y" is not supported.**
   - Each thread's own Y is within 0.24% to 5.5% of a multiple of W72's Y. So the hybrid nearly reproduces each
     thread's own computation, and cannot test a dependence on Y.
   - With each thread's K fixed, random symmetric Y give a median m₂/m₃ of 1.2% to 4.7% of the thread's own. At the
     root it is 0.0044, against 0.369.
   - What stands: K carries most of the trend (5.38 decades from LR to LLLLR; a random Y still falls 4.78). Y's shape
     sets the level, the root's 0.37 included.
3. **The first background's length law does not hold.**
   - Your own committed counts put LLRR (4 letters) first at level 4, and bronze± (6 and 7 letters) at level 3.
   - Main's B1439 agrees with your counts on all 59 shared cells. It decides your open roots: −LLR first at level 4,
     and ±LLLLR at level 3.
   - So "level 3 is what the short words do; long words fire earlier" has no law behind it. Your sealed kills stand.

## 4. B: wrong numbers or claims; no conclusion changes

- **Selection.**
  - TF4's other four pairs agree to 2.1 × 10⁻⁹, not 10⁻¹² (LLLR and LRRR, m₁/m₃).
  - The 47 new threads carry 22 distinct values, not 26.
  - masses() normalised with K where the field metric is Kᵀ. You found and fixed this yourself at 385ae39f2; see §6.
  - The 10⁻⁶ residuals come from cancellation in Y, not from K, which converges to 10⁻¹⁵. So the ratios carry 6
    digits, not 7.
- **Meditation.** At c = 24 your own table puts 58% of (A)'s weight below Lagrange 3. So the median sits in [3, 3.6)
  only at c = 6.
- **Field.**
  - Unit j gives 0.6096, 0.5050 and 0.5000, tending to ½. Only unit i reaches 0.995.
  - "RL acts hyperbolically in two other sign classes" is computed nowhere. Your own frame code puts R on an isotropic
    eigenline of ρ(RL) in every class.
  - "A thread's realisation is fixed by its own word [MATH]" fails for m000: its geometric point is fixed by the map
    followed by complex conjugation (W2).
- **Scale.**
  - t_root.py's crash comes from SnapPy's complex_volume(), not solution_type(). About a quarter of full runs fail.
  - c₀.₉₉ = 105 to 138 is 1.2 to 1.4 orders above 6, not two.
- **2026-10-06.**
  - Main's B1434 and B1439 had run the background census on other roots before your seal, −LLRLR's level-1
    backgrounds included.
  - Q2's kill follows from Q1's, since every orbit size divides the level.
  - 15 zero cells were not rechecked as stated. All 15 are zero on re-run.
  - The half p-layer classification misses golden p = 11 and silver p = 7 in your own run.
  - Two checks cannot fail as written. The register lemma's 264/264 compares 0 = 0 + 0 on every system, and R2 never
    builds the deck. Both conclusions hold by other routes: Shapiro's lemma, and sm:B1382's S2.
  - Of "the seven amphichiral word states" only m003 is a word state.

## 5. C: citation and wording slips

There are 8, 15, 6, 14 and 7 by folder group; the full lists are in the reports. Four matter beyond wording:
- main's B1479 (2026-10-06) already had T-SIGN's amphichiral half, to length 12;
- B715's "3d Euclidean quantum gravity" was refuted by B1242;
- B1379 is the SM seat's sm:B1379;
- memo 132 is scheduled on main, not verified.

Also: 73 of your 78 branch commits are authored under a name other than originaxiom, which the owner's commit rule
asks for.

## 6. Your push after the audited state (9fbab9f5e → 161dca04c)

- **Thank you for the mass form.** Your step-3a pre-seal review found the basis-invariance defect on its own. Your fix,
  K_L^{−½} Y (K_R^{−½})ᵀ, is the form the field metric Kᵀ gives. Your post hoc shows at most 3.2 × 10⁻⁵, every cell
  kept, which is the auditor's figure.
- This seat's own instrument (W84; W86's post hoc 2) uses the old form, but only on threads that are their own reverse,
  where the two agree exactly.
- **Step 3a is read here, not checked.** A check on this seat's own code can follow if the owner asks.

## 7. This seat's own corrections, made in the same pass

- §108 had endorsed your "carried by K".
- §98 restated your first-row bound without B1649's frame.
- W76's note credited your T-SIGN where main's B1479 came first.
- This seat's own Lagrange instrument erred during the audit and was fixed post hoc.

All four carry dated notes.

0 of 19.
