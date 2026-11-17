# The seats' relations, one by one

This page takes each relation a seat has offered as a parameter-free statement and says, in plain words, what it
states, what it rests on, what main recomputed, and what would be needed before it could be set beside a measured
number. No comparison with data is made anywhere on this page. A comparison needs a rule sealed first and the
author's word (P-862, step 3).

The verdicts are those of the register's records (`verification/records/`). The page is kept current as the lanes are
read; a relation not yet read at its source is listed as pending and nothing is said about it.

## agy-002's ten relations (PR-1 to PR-10)

Source: `relays/AGY002_MASTER_CLOSURE_SYNTHESIS_2026-11-16.md` on `agy-002/closure`, section 2, read in full; each
relation traced to its gate, the gate's results, card and script text read, and recomputed on main's own code
(`verification/checks/`). The seat itself attaches "borrowed model premises" to eight of the ten; main agrees with
that labelling and adds two findings (PR-5, PR-6).

| | What it states | What it rests on | What main recomputed | Verdict |
|---|---|---|---|---|
| PR-1 | The charges of every Standard Model field satisfy 2·t + 3·d + 6Y ≡ 0 mod 6; the weights 3/5 and 2/5; one family's anomaly sums vanish on the plane of hypercharge and B − L | Nothing borrowed: an identity of the charges | The congruence for all six fields; the four anomaly sums, symbolically (`agy002_g4.py`); on main already as B1951 | **Verified.** It is the Standard Model's own structure restated. It predicts nothing new |
| PR-2 | The strong CP angle is zero and stays zero under two-loop running | Yukawa matrices Hermitian with positive determinant at the Pati–Salam scale (a parity of the left-right model); the gauge theory's own angle set to zero; one sign | That the phase of det(Y_u Y_d) does not run at one or two loops, for any Yukawa matrices: algebra, and 7e-16 on main's two-loop running with a non-zero Jarlskog invariant | **Conditional.** The invariance is unconditional; that the phase starts at zero is borrowed |
| PR-3 | sin²θ_W = 23/134 + (109/201)·α_EM/α_3 + (506/(201π))·α_EM·Δ_PS + δ, with δ between 7/10000 and 3/1000 | The left-right model's field content and breaking chain; perturbative Yukawa couplings; Δ_PS, the logarithm of the ratio of two scales, is free | The three rational coefficients exactly, from the content; the Pati–Salam stage's two-loop coefficients from the content; δ's range over the seat's 243 histories on main's own running: [0.0007265, 0.0027548], the seat's figures | **Conditional.** One free number. It is one inequality (Δ_PS ≥ 0) on three measured quantities, given the model |
| PR-4 | The ratio of the Higgs mass to the weak scale lies between 35/100 and 78/100 | The quartic's value at the Pati–Salam scale, (1/4)·g²·cos²2β, a relation borrowed from supersymmetric models; a grid of inputs whose ranges are chosen | The range over the 243 histories: [0.370482, 0.771511], the seat's figures to every digit | **Conditional.** An envelope of a chosen grid, not a prediction; and of a quantity whose measured value is known |
| PR-5 | A one-loop mass matrix on the six Higgs modes has a unique ground state, with no bit spent | A kinetic term (eigenphase over length, squared), a postulate; a "bubble" summed over the 24 points of order 5 | The seat's result as defined; then that the Higgs's Wilson line is ±3w/2 and so not a function of the point w, that the bubble changes under a lattice shift of w, and that averaged over the four lifts it is an exact multiple of the identity (`level6_higgs.py`) | **Refuted.** The ground space has dimension two: one bit, not zero |
| PR-6 | Under 3(B − L) the top row of the mixing matrix is exactly aligned at all 288 points of orders 5, 10, 15 | Unbroken SU(2)_R | That under 3(B − L) the up and down sectors have the same Wilson line, so the two matrices are one matrix (`agy002_g5.py`, C) | **Not a relation.** The equality cannot fail, for any coupling. With hypercharge, the mixing in this frame is deranged and lift-dependent |
| PR-7 | Under 3(B − L) leptons separate from down quarks (ratio above 28 at height 4; exponent ratio 3/2 at order 15) | Which charge the Wilson line carries (three choices give three answers); the single Higgs mode e_0 | The figures (28.5 and 814; the multisets over each orbit); the 3/2 is frame C's and is verified in gate 2 | **Conditional** on those choices |
| PR-8 | For even Δ the family Gramian over the 24 points is covariant under both generators and is not a multiple of the identity | The contraction with the six Higgs modes evaluated at the origin | Covariance (7e-15, 7e-14); eigenvalues 2.859, 3.069, 3.171; that for odd Δ it fails with one lift and holds with four | **Verified.** A structural fact of this frame. It is the Gramian of 24 evaluation vectors and carries no hierarchy |
| PR-9 | cos²θ_12·cos²θ_13 = 2/3 for the neutrinos, stable under running | The first column of the mixing matrix is put in by hand as one bit of a residual symmetry; masses well separated | The drift under the neutrino operator's running, to seven digits (the equation read at its source); its growth as two masses approach | **Conditional.** Nothing derives the first column from the object |
| PR-10 | No mechanism here fixes the weak scale: the mass term keeps its sign; the Casimir curve of the flat tower runs away; a second scale adds a free ratio | Scoped by the seat to the flat equal-mass tower | The sign statement (elementary); the slope as a closed negative integral (2e-16); the count of free ratios | **Verified, as scoped.** All three are negatives |

**What this comes to.** Of the ten, two are verified identities of known structure (PR-1, PR-8), one is a verified
set of negatives (PR-10), one is refuted (PR-5), one is not a relation (PR-6), and five are conditional on the
left-right model's content, parities and scales, which are borrowed and not derived from the object (PR-2, PR-3,
PR-4, PR-7, PR-9). None of the ten removes a free number from the count. Three state something that could be set
beside data once a rule is sealed: PR-3 (one inequality), PR-4 (an envelope) and PR-9 (one equality), each on its
premises.

**What a sealed rule would have to fix, before any look.** For PR-3: the scale at which the three couplings are
taken, the scheme, the treatment of δ, and what counts as failure given that Δ_PS is free. For PR-4: nothing can be
sealed while the grid's ranges are chosen; the envelope moves with them. For PR-9: which data set, which ordering,
and the statement that the premise (the first column) is itself unearned. Main drafts no rule here; that is the
author's call under P-862.

## agy-exp's seven relations (UR-1 to UR-7)

Source: the three result notes of its campaign X-RELATIONS on `agy/self-consistent-loop-2026-11-11`, each read in
full (the consolidated atlas is in the third), the text of its second script for the exponent rule, and its own page
of premises of 2026-11-17 (`relays/AGY_EXP_ONE_PAGE_PREMISES_UR1_TO_UR7_AND_THREE_FAMILIES_2026-11-17.md`), which says
of each relation what it borrows and what it leaves free. Main agrees with that page. Its later campaigns revise
some of the numbers; they are not yet read at their source, and where a later version exists this is said.

| | What it states | What it rests on | What main recomputed | Verdict |
|---|---|---|---|---|
| UR-1 | sin²θ_W − (23/134 + (109/201)·α_EM/α_3) vanishes at one loop for any number of families, and lies between 3129 and 4693 per million at two loops over 1320 histories | A single-step model; a unified coupling typed in as an area, or a volume times an area; a running span typed in as (45/π)·Vol or a stop at an integer 1/α_3; the 44 points of a fourfold cover | The one-loop part exactly (B1956) | **One-loop part verified; the corridor conditional and superseded.** The single step's one-loop relation is already refuted on the record (B915); the later version adds a Pati–Salam stage with a free Δ_PS (PR-3 above) |
| UR-2 | The quartic stays positive in every history, and √(2λ) at the bottom lies between 0.2899 and 1.1329 | A boundary value λ = g²/5; the same typed-in coupling and span | Nothing of the envelope. Its running at this date carried −24·λ²·Tr_Y for −48 and the exchanged mixed products, both verified wrong on main at the primary source and repaired by the seat later | **Conditional and superseded in its numbers.** An envelope of a quantity whose measured value is known |
| UR-3 | At order 5 the lepton's singular values equal the down quark's; exponent gap ratios {39/31, 5/3} | The seat's overlap: a supplied ansatz with a cut-off, not frame C | The exponent arithmetic from the seat's stated rule (`agyexp_ur345.py`): the ratios and the equality of the exponents at every point | **Arithmetic verified; the relation conditional** on the ansatz. Its infrared envelope touches a ratio held out here: not compared |
| UR-4 | At order 15 the lepton's singular values are the down quark's at 6w; gap ratios {39/31, 5/3} against {15/11, 15/8, 431/190, 15} | The same ansatz | The same arithmetic: both sets, the identity through 6w, and that 3w fails | **Arithmetic verified; conditional.** On main's frame C the law is through 3α (B1949): the two frames differ |
| UR-5 | At order 10 no multiplier relates the two sectors; gap ratios {10/7, 31/5} against {29/26, 10/3} | The same ansatz | The same arithmetic: no multiplier c in 0..9; both sets | **Arithmetic verified; conditional** |
| UR-6 | The phase of the determinant of a doubled 6 × 6 state (each point with its reflection) is zero before and after the running | The doubling itself; the gauge theory's own angle set to zero | Read in the script: the overlap at (a, −b) is the conjugate of the overlap at (a, b) up to a factor that cancels between up and down. On main: a determinant's phase does not run at one or two loops | **Conditional.** Two elementary facts and two premises. Its own control shows the overlap is not a function of the point on the torus (a lattice vector changes the phase by 4π/5) |
| UR-7 | A seesaw operator built from the overlap is covariant, obeys the same order-15-to-5 identity, and has corridors for its two ratios | The Majorana matrix is the seat's own operator, with two free ratios or a typed-in weight 1/(4π) | Nothing beyond the exponent arithmetic it shares with UR-4 | **Conditional; not recomputed** |

**What this comes to.** The exact arithmetic the seat reports for its own rule is right wherever main has re-entered
it. None of the seven is a statement about the object alone: each sits inside a supplied model, with a typed-in
coupling, span, boundary value, ansatz or doubling, and the seat's page of premises says so in its own words. None
removes a free number. Its page also states that the three chiral families of its last campaign are an input: the
index equals the flux put in, and 0, 1, 2, 6 and −3 are not excluded.

**Still to do for this lane:** the later campaigns' versions of these relations (X-UNIFY to X-FOUNDATION), read at
their result notes; the physical lane's fifteen defects in X-APEX (all held by the seat) and its six further findings
on X-FOUNDATION, each by reading the cited lines.
