# B1389 PREREGISTRATION — THE FULL SPECTRUM (kill test 2): does the frame's chirality give complete, anomaly-free generations?

**Sealed 2026-09-27, before any direction-dependent spectrum or anomaly is computed. Seat: cc (the SM-derivation branch). Occasion:
the owner's "how do we continue bravely" — the second of the kill tests on the chirality mechanism (B1386, B1387, B1388). It holds
for any non-zero count N, so it does not wait on sL-8's definition question.**

## The question

On a member with a cuspidal Higgs class v, the seat's frame gives every bulk sector a chiral index.
- **Spin-0 sectors** (SL(2)_β singlets) see only the abelian Higgs field q_μ·ω_v, where q_μ = ⟨H, μ⟩ and H = aY + bγ is the Higgs
  direction in the Cartan plane of c(SM) = SL(2)_β × ℂ*² (B1368). The cuspidal character is trivial on every peripheral subgroup,
  so these sectors are cusp-fixed at every cusp. Their index is N_μ = sign(q_μ)·N(v) (B1351 (ii) with the charge sign, B1369 §4).
  If q_μ = 0 there is no Higgs field on the weight and N_μ = 0.
- **Spin-½ sectors** have index 0 at every parabolic cusp (B1372 Lemma A: the geometric Higgs field gives a doublet's two weights
  the Morse functions ±t/2).
- **The spin-1 sector** is Standard-Model-neutral.

For cube~3.24, N(v₊) = ±2: B1387's asymptotic count, which B1388 §3 identifies as minus the signed number of Higgs zeros.

**What the record has not asked.** The record has read "the spin-0 half" as the 10 of SU(5) (B1368 (F), B1369 §1.4, B1386, B1387).
- But the 27's spin-0 sector is the 15 = 10 + 5 (B1368's own census labels the 5's weights "5bar / 5"). A 5 counted with negative
  chirality has exactly a 5̄'s quantum numbers.
- If the 78's broken roots are bulk matter, its spin-0 non-Standard-Model roots are charged under the same Higgs field and are chiral
  too.

**So: for which Higgs directions H is the frame's net chiral spectrum a whole number of complete Standard-Model generations, and
anomaly-free?**

## Method (fixed now)

- **Data.** The record's own E₆ vectors, copied verbatim from B1368's `sm_connections_of_m004.py`: the 72 roots, the 27's weights,
  Y, β, γ and the ¾-weighted dot product.
- **The four frames** (what the bulk matter is):
  - **F27:** the 27 and its conjugate. C = Σ over the spin-0 weights w of the 27 of N_w·[w].
  - **F78:** the 78's broken roots (7d E₆ super-Yang–Mills). C = Σ over one root α of each ± pair among the spin-0 non-SM roots of
    N_α·[α].
  - **F27+78:** both.
  - **F133:** E₇'s adjoint, broken to E₆ × U(1)_Z by an extra Higgs component c·Z. This is the 27 with charges ⟨H, w⟩ + c, its
    conjugate, and the 78 as in F78.
- **Directions.**
  - H = (a, b) ∈ ℝ² \ 0 for F27, F78 and F27+78. For F133, (a, b, c) ∈ ℝ³.
  - The net content is constant on each open cone of the arrangement of the lines or planes ⟨H, μ⟩ (+ c) = 0.
  - In ℝ² every cone is visited exactly: one direction strictly inside each sector between consecutive critical rays, and each
    critical ray itself (reported as a boundary case).
  - In ℝ³ the cones are found by sampling the sphere: 40 000 quasi-random directions plus directions near every pairwise
    intersection of critical planes. Each distinct sign pattern is recorded.
- **Content.** For each μ with N_μ ≠ 0: |N_μ| left-handed multiplets in the representation sign(N_μ)·μ.
- **Anomalies,** exact from the weights. A generic SU(3)_c Cartan direction t and SU(2)_L Cartan direction s are used.
  - The criterion's anomalies:
    - [SU(3)]³ = Σ N_μ (t·μ)³;
    - [SU(3)]²Y = Σ N_μ (t·μ)²(Y·μ);
    - [SU(2)]²Y = Σ N_μ (s·μ)²(Y·μ);
    - Y³ = Σ N_μ (Y·μ)³;
    - grav·Y = Σ N_μ (Y·μ);
    - Witten's SU(2) anomaly: the net number of doublets is even.
  - Reported but not in the criterion: U(1)_γ's anomalies (γ³, γ²Y, γY², grav·γ, [SU(3)]²γ, [SU(2)]²γ). An anomalous abelian factor
    must be massive (B864); a Green–Schwarz term can do that for an abelian factor.
- **Generations.** Classify the net content by Standard-Model quantum numbers (colour 3 / 3̄ / 1, weak 2 / 1, Y). It is "n complete
  generations" if it equals n·(Q + u^c + e^c + d^c + L), plus any SM singlets, for an integer n ≠ 0, with nothing else SM-charged.

## BANKED IDENTITY:

Before any direction is read, the pipeline must reproduce:
- B1368's census:
  - the 27 by SL(2)_β spin: 15 + 12;
  - the 78's roots by spin: 30 + 40 + 2;
  - the 27's spin-0 content: Q-type 6, u^c-type 3, e^c-type 1, D-type 3, H-type 2;
  - the 22 non-SM spin-0 roots, with six distinct (Y·α, γ·α) pairs.
- B1366's singlet line: the two SM singlets of the 27 have equal non-zero γ-charges.
- Controls:
  - every weight of the 27 at index +1 is SM-anomaly-free;
  - one generation (Q, u^c, e^c, d^c, L) is anomaly-free;
  - a lone 10 has [SU(3)]³ ≠ 0.

If any of these fails, the run stops and nothing below is read.

## PRIOR ART:

The design-time bank grep, `scripts/checks/already_banked.py`, was run on three queries:
- "anomaly chiral spectrum Higgs direction cusp";
- "anomaly free generation 10 5bar spin-0";
- "chiral 5 from the 78 anomalous".

The relevant record:
- B864: over a chiral generation, hypercharge is the unique gaugeable abelian direction.
- B1374 (the class's index): spin-0 sectors carry no class index; one anomaly-free generation on t12839 comes from the doublet sectors.
  That is a different index.
- B1368 (the frame theorem, proved on m004, where spin-0 sectors cannot be chiral at all).
- B1369 §2.4: the 10's sign pattern is uniform only when the γ-component dominates.
- B1372's Lemma A.
- A sweep of this branch and origin/main for the spin-0 5 read as a 5̄ ("negative chirality", "anti-chiral", "(1,15)", "5 of the 15",
  "15 = 10 + 5") finds none.

No arc computes the frame's net chiral spectrum per Higgs direction on a cuspidal member.

## The outcomes (fixed now)

**Per frame:**
- **PASS:** some open cone, not merely a critical ray, gives an SM-anomaly-free net content equal to n ≠ 0 complete generations,
  with no chiral SM-charged exotic.
- **FAIL:** no cone does.

**Overall:**
- **POSITIVE** if F27+78 or F133 passes. These are the bulk contents that include the gauge multiplet's own broken roots, which 7d E₆
  super-Yang–Mills always carries.
- **MIXED** if only F27 or F78 passes.
- **NEGATIVE** if no frame passes.

**Consequences, fixed in advance:**
- *F27 passes.* B1368's frame theorem ("one half of every generation is never chiral") is scoped to members without a cuspidal
  class. On a cuspidal member the 27's spin-0 sector alone carries whole generations, n = |N| per member in the passing cones. For
  cube~3.24 that is two in the frame, conditional on sL-8.
- *F27 fails.* The 27-frame reading of B1386/B1387 is closed.
- *F78, F27+78 and F133 all fail.*
  - The bulk that 7d E₆ super-Yang–Mills actually carries is anomalous in every direction, and non-abelian anomalies have no
    Green–Schwarz cure.
  - So the frame is consistent only if something outside it cancels them: the completion, or anomaly inflow at the cusps. That is
    registered as a lead.
  - The 27-frame's generations are then physical only with the 78's charged roots removed or paired.
- *Any fuller frame passes.* POSITIVE for that frame, with its cones reported.

## Declared prior

- **F27 PASS, about 85%.** Along γ the 10 and the 5 of the 15 should carry opposite charges (U(1)_η: −2 and +4 in the standard
  normalisation), giving 10 + 5̄. The risk is the record's γ normalisation.
- **F78 FAIL, about 85%.** The 35's non-SM roots should give a lone 5 or 5̄, or an exotic.
- **F27+78 FAIL, about 75%.**
- **F133 FAIL, about 70%.**
- **Overall MIXED, about 55%.**

## Fence

The seat's frame, the spin-0/spin-½ split as the record has it:
- Pantev–Wijnholt on the cusped 3-manifold;
- B1351 (ii) per sector;
- B1372's Lemma A for doublets.

N(v) is any non-zero count. The pattern multiplies N, so the definition question (sL-8) does not enter.

The four frames are the record's readings. Which one is physical is not decided here. Generations in the frame are not generations
in nature: no physics is crossed.
