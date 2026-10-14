# Step 3a — can the thread frame split the light pair? The weights cells, with the 7/2 modes completed on the thread (chat1, 2026-10-14/15, night). Sealed before the script is committed; the run waits for the tribunal.

**Why.**
- **The owner's plan of 2026-10-14 (23:30, agreed).** Before choosing a thread, test whether the thread frame can work
  at all. Give the sectors real differences and ask whether any thread then produces the up quarks and the charged
  leptons.
- **The failure to test.** In the sealed thread frame (cell C1 below) the light pair is split too little.
  - Over the 59 admitted threads to length 8 (`lagrange_law.json`), no thread has m₁/m₂ ≤ 0.005 with m₂/m₃ in
    [0.002, 0.07].
  - The 16 admitted threads in that band have m₁/m₂ ≥ 0.0515 (LLRLRLR).
  - Those figures use the Lagrange law's mass formula (next paragraph). The data, read from the SM seat's received
    HZ2021 file: m₁/m₂ is about 0.002 for the up quarks, 0.050 for the down quarks and 0.0047 for the charged leptons.
- **A correction to the mass formula, found by this seal's pre-seal review.**
  - With K_ab = ∮⟨F_a, F_b⟩ (linear in the first slot), the basis-invariant masses are the singular values of
    K_L^{−½} Y (K_R^{−½})ᵀ.
  - The sealed thread frame and the Lagrange law used (K^{−½})ᵀ Y K^{−½}. The two agree when K and Y are real. They are
    real on every reflection-symmetric thread: one whose reversal or mirror is a rotation of it.
  - Reality is verified on the 12 threads of length ≤ 5, which include every Q0(a) thread. On the other
    reflection-symmetric threads, LLRLRLR among them, it is expected from the reflection argument, and the JSON's
    imaginary parts will confirm it.
  - 18 of the 69 words are not reflection-symmetric. Their Lagrange-law ratios are rechecked by a separate labelled post
    hoc, outside this seal.
  - This instrument uses the invariant form throughout.
- **What the frame allows** (`cells_readout.*`, committed and run before this seal; structural, no Yukawa).
  - Matter sections in ρ_R with one unit each are unique at weights −½ and 3/2, and two-dimensional at 7/2. The second
    dimension is f, the unique holomorphic 7/2 section.
  - ρ′'s holomorphic Higgs modes have dimensions 0, 0, 1, 1 and 2 at weights −3/2, ½, 5/2, 9/2 and 13/2.
  - B1644's coupling has weight k_left + k_right − ½. So among the nine cells with weights in {−½, 3/2, 7/2}, the cells
    with a unique Higgs are (3/2, 3/2), (3/2, 7/2) and (−½, 7/2), up to order.
  - **Only (3/2, 3/2) is parameter-free.** The other two have one free admixture of f per 7/2 mode.
  - (7/2, 7/2) has a two-dimensional Higgs, and the −½ pairs without 7/2 have no Higgs.
- **The half-period Higgs** (B1651) is the other route to sector differences. It waits for B1651's run (its U4 law) and
  is not tested here.

**The added hypothesis, H-ORTH (named here, not derived).** On the vacuum thread W, each one-unit 7/2 mode is completed
by removing its f-component in the weight-7/2 cycle inner product:
- F̃_b = F_b − c_b f, with c_b = ⟨F_b, f⟩_W / ⟨f, f⟩_W and ⟨X, Y⟩_W = ∮_W Σ_r X_r conj(Y_r) y^{7/2} ds;
- the cycle integral is taken as in the sealed thread frame.

That is the minimal-norm completion: c_b minimises ‖F_b − c f‖_W. F̃_b does not depend on which particular one-unit
solution is used, and Q0(d) tests that. The completion is canonical given the thread; it is still a hypothesis.

**Instrument** (`weights_cells.py`, committed after this seal and before its one run).
- **The construction is thread_frame.py's,** copied through `lagrange_law.py`: the SM seat's forms at `87cf7f551`,
  read through `git archive`, B1644's coupling with R, cycle integrals at the image of each point in the standard
  fundamental domain, the trapezoid rule at N = 256 and 384.
- **The forms:**
  - W72's F at 3/2 and h at 5/2;
  - W68's unique one-unit sections at −½. Their F₊ is R itself;
  - f, the holomorphic 7/2 section, by W68's collocation, on the line of least residual (all three were tried in
    plumbing, residuals ~10⁻⁴¹);
  - one particular one-unit section per line at 7/2, by the same collocation, normalised to coefficient 1 at its own
    unit, with f's normalised coefficient (e_i, exponent 1/8) set to zero, then H-ORTH on each thread;
  - a second particular set, with f's (v−, exponent 3/8) coefficient set to zero instead, for Q0(d) only;
  - h at 9/2 by W72's `solve_twisted`, on the line of least residual.
- **The cells,** with masses as the singular values of K_L^{−½} Y (K_R^{−½})ᵀ:
  - **C1** = (3/2, 3/2) with h at 5/2. This is the sealed thread frame, a control.
  - **C2** = (3/2, 7/2) with h at 9/2.
  - **C3** = (−½, 7/2) with h at 5/2.
- **Threads:** every Lyndon word of length 2–8 (69).
- **Admission,** per cell, as in the Lagrange law: y_max ≤ 3, and the cell's ratios agree between N = 256 and 384 to
  10⁻⁵ relative. For C3 only m₂/m₃ is used, because of S1. A cell whose K is not numerically positive definite at either
  N is not admitted on that thread.
- **The JSON keeps every thread's K_L, K_R and Y per cell at N = 384,** and the largest imaginary parts.
- **The run waits for the tribunal.** The script runs once, after main banks THE FRAME TRIBUNAL (P-136), unless the
  owner says otherwise.

**Controls (Q0)** — holds if all hold:
- (a) C1 reproduces `lagrange_law.json`'s m₂/m₃ and m₁/m₃ to 10⁻⁶ relative on LR, LLR, LLRR, LLRLR and LLLR, all
  reflection-symmetric;
- (b) every solve has residual < 10⁻²⁰, and h at 5/2 matches W72's banked coefficients to 10⁻²⁵. "R equals the −½
  section F₊" is an identity (the same call), reported, not a control;
- (c) every integrand of the three cells and the three norms is invariant under 20 random modular moves to 10⁻⁹
  relative (thread_frame.py's test, floored at 10⁻¹² of the largest value at each point);
- (d) on the root, the completed K_R, Y₂ and Y₃ from the two particular sets agree to 10⁻¹⁰ relative. The arithmetic
  identity ⟨F̃_b, f⟩ = 0 is reported, not counted;
- (e) on LLRLRR, a thread that is not reflection-symmetric, every cell's masses are unchanged, to 10⁻⁸ of m₃, under five
  random changes of mode basis. For C2 and C3 the change is unitary on the left and phases on the right. For C1 it is the
  same unitary on both sides.

**A void clause, fixed now.** If (c) fails for an integrand of C2 or C3, that cell's S rows are void: reported, not
scored. An invariance failure would mean the cell's multipliers do not match, so its numbers would not be cycle integrals
of anything.

| | prediction | prior |
|---|---|---|
| Q0 | the controls hold | 88% |
| **S1** (an instrument check on C3) | rank 2 on every admitted thread: m₁/m₃ < 10⁻¹⁰. Reason: the left mode F₊ at −½ is R, and G(R, F, R) = (R·R)F = 0 since R is isotropic. Only numerics can fail it. It is the isotropy behind B1649's zero, returning whenever R is a matter mode | 97% |
| **S2** (the main cell, C2) | some admitted thread has m₁/m₂ ≤ 0.005 with m₂/m₃ in [0.002, 0.07]. C1 has none (under the Lagrange law's formula) | 25% |
| S3 (C2) | among C2's admitted threads in that band, the least m₁/m₂ is below 0.0515, C1's value on the reflection-symmetric LLRLRLR. If C2 has no thread in the band, S3 fails | 50% |
| S4 (C3) | some admitted thread has C3's m₂/m₃ in [0.002, 0.07] (with m₁ = 0) | 70% |
| S5 (C2) | the root LR has the largest m₂/m₃ of C2's admitted threads | 70% |

**Read-outs (no prior).**
- Per thread and cell: both ratios, m₁/m₂, the K conditions, |c_b|, the matrices and their imaginary parts.
- Spearman(y_max, ln m₂/m₃) per cell.
- The root's values per cell, and each cell's threads in the band.
- C1's least m₁/m₂ in the band under the invariant formula.
- The nearest admitted (thread, cell) to each sector's two ratios, over C1 and C2 (C3 has m₁ = 0). This is a read-out
  only: no sector is assigned.

**What a result means, fenced.**
- **If S2 fails,** no thread in the weights route splits the light pair as the up quarks and leptons need, at rank 3 and
  given H-ORTH.
  - What remains: the Higgs's locus (B1651, after its run), other representations, or a rank-2 cell such as C3, whose
    first generation is massless at leading order and needs a lift (B1649, P-128).
- **If S2 holds,** the frame survives this check, and a sealed sector-assignment test follows. A hit is not an
  assignment.
- **S1** would place the isotropy behind B1649's zero inside the thread frame: a massless generation returns whenever R is
  one of the matter modes.
- **Not tested:** H-ORTH's derivation; the half-period loci; other representations; mixing; CP; which thread.
- No value. **0 of 19.**

**Disclosed: seen before the seal.**
- `cells_readout.*`, committed and run before this seal, and a scratch run of the same calls before that.
- Plumbing in scratch, no coupling and no mass:
  - f builds at 7/2 on each of the three lines with residual ~10⁻⁴¹, normalised on e_i, lowest exponent 1/8;
  - the −½ sections build, and h at 9/2 builds on each of the three lines, with residuals of order 10⁻⁴¹;
  - the three particular one-unit 7/2 sections build with residuals of 6.4, 2.9 and 4.3·10⁻⁴¹ and a zero coefficient
    at (e_i, 1/8).
- C1's band figures come from `lagrange_law.json` (the sealed Lagrange law's output).
- **A read-only pre-seal review** read the draft and found:
  - the mass formula (taken above);
  - an unguarded crash path;
  - no stored matrices;
  - two controls that were identities;
  - minor wording.

  It computed no C2 or C3 quantity. Its algebra checks used random matrices and banked JSON only.
- No C2 or C3 number has been computed.

chat1, 2026-10-15.
