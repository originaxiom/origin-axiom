# B1656 — THE ELECTRON'S ZERO: preregistration

cc (main), 2026-10-15. **No data.** 0 of 19. The second arc of C (P-151), after B1654. It bears on the parent's
clause 7 (split the down quarks from the charged leptons), on P-128 and on P-129.

## 0. Seen first

`VERDICT topic-sweep /twisted (channel|szeg|norm)|electron.{0,20}(zero|massless)|lepton.{0,20}(zero|massless)|9.torsion|omega.fixed|order.3 rotation/: 8 of 1427 arcs on main match (NEGATIVE 1, PROVED 7)`
at the seal (B1042, B1291, B1292, B1302, B1320, B1321, B1654, B931); the design's sweep (13 of 1426, with 10 other lanes) also
matched B1435, B1490, B928, B1294 and B1453, all read. None of the arcs on main states an electron zero. The matches are
ω-fixed or 9-torsion points in other settings (B1042, B1291, B1292, B1302, B1320, B1321, B1435, B1490, B928, B931), the chirality
bit (B1294), a harvest (B1453) and B1654. The nearest fact on record is B1653's U7 read-out, which found the leptons' triplet
isotropic on W59's lines. By the null quaternion that is R₁(leptons) = 0, seen there without the norms and without its
consequence for the mass.

**The nearest prior statements, which this arc builds on:**
- The SM seat's W59, its PH2 (its dossier's NOTE, about lines 4758–4779), and the register's P-100. These already give
  the twist arithmetic on these same 18 lines: "the quarks in ninths, the leptons in thirds"; "d^c and e^c see
  different twists"; "a discrete d–e split appears, if the Higgs's term dominates". P-100 notes that the underlying
  fact is the Standard Model's Z₆ (6Y ≡ colour triality mod 3).
- Main's own superseded B1653 draft (`frontier/B1653_*/design_v1/B1653_PREREGISTRATION_v1.md`, line 79) said "the
  electron massless at leading order", in the reading that dropped R₁.
- The SM seat's NOTE (about line 5259) records the literature fact "electron massless at τ = i" (a rank-one
  charged-lepton matrix), in another construction.

What this arc adds to them is the consequence under the canonical end condition: D_sector = (c₁ − c_⊥)R₁², and
R₁(leptons) = 0 because δ_e = −9w lies in the lattice. The sweep's lane hits were not all read; the ones above were.

**Read before the seal:**
- B1653 (the twisted pairing: P_s = N_s e^{2πiAu}θ_s(u + ū)/θ₁(u); R_s = κ c_s θ_s(ū)θ_s(δ)/θ₁′(0), c = (−i, −1, −1, i);
  the null quaternion R₁² + R·R = 0; ū = w_x + w_y and δ = w_x − w_y; the hypercharges in units of 6Y as a stated
  dictionary input; W59's lines as holonomy phases);
- B1654 (the boundary class's norm; the canonical end condition; D = Σ c_s R_s²);
- the SM seat's W59–W61 (the lines, the charges, the selected vacua) and C0;
- B1653's U7 read-out ("at W59's Higgs lines at ω: up and down non-isotropic, leptons isotropic").

**Literature.** No source was read for this arc beyond those that B1642–B1654 cite (theta functions and Jacobi's
identities, Whittaker–Watson §21). The twisted Szegő kernels' form is B1653's U1. The fixed points of z ↦ ωz on the
hexagonal torus (0 and ±(ω − 1)/3) are derived here by hand, and checked exactly in E0.

**Main's own earlier note.** Main's S127 design notes (`audit/drafts/s127/P128_DESIGN_NOTES.md` §6, firewalled, not on
the record) observed by hand that δ_lep = −9w lies in the lattice, so that the leptons are not lifted (a d–e split).
That was in the triplet reading of the superseded first design of B1653. This arc is that observation's first test,
now with the full null quaternion and the canonical end condition.

## 0b. Disclosed

**Main's exploration before the seal** (`verification/before_the_seal/`, scripts with their saved outputs):
- **`twisted_D_explore`, `twisted_D_lines`.** At τ = ω, on all 18 W59 Higgs lines, with route A as it then was (no a₀
  term, ε = 10⁻⁵ only), D_sector/|R|²:
  - leptons ≤ 5.1 × 10⁻¹³;
  - quarks in {1.0312, 2.4629, 2.7416}, cycling between up and down;
  - the half-period and 3-torsion lines give 0 in every sector;
  - the generic τ = 0.13+1.07i gives the leptons 3.08.
- **The channel norms of the quark sectors at ω on W59's lines:** c_i = c_j = c_k = 2.231269 and c₁ = −3.575627. For the
  leptons R₁ = 0, and c₁ is undefined (P₁ ≡ 0).
- **`controls_explore`** (output now saved).
  - On the 9-torsion lines (1/9, 2/9) and (1/9, 0), whose 3w is not ω-fixed, the leptons' R₁ ≈ 10⁻¹⁶, the imaginary
    norms split (−2.78, −2.78, 22.6) and the lift is 2.92.
  - The fictitious charges (−3, 5) give R₁ = 0.36|R| and D = 3.23.
  - The third line it tried, (4/9, 1/9), is ω-fixed and therefore not a control. The instrument's third line is
    (2/9, 1/9); see below.
- **A smoke test of the functions**, and unit tests of the revision's new pieces on unsealed inputs: the line
  arithmetic, the corrected norm on the line (5/9, 8/9), and the lift law with another seed.

**One pass of a read-only reviewing agent** (`verification/before_the_seal/review/`, scripts and a README; the draft it
read is kept as `design_v1/`). It found:
- **DECISIVE.** E1 could not hold as first sealed. The twisted kernels are not odd: K_s = 1/z + a₀ + a₁z + …, with
  |a₀| = 2.43 on W59's lines. So the cut-off integral misses the disc's πε²|a₀|², and drifts by 1.85 × 10⁻⁵ across
  ε = 10⁻³ … 10⁻⁵, against 10⁻⁹. Its control failed likewise.
  - Route A now restores that term (a₀ from a circle mean). E1 then holds with margins of 70× and 8 × 10⁵.
  - B1654's N1 passed only because the Szegő kernels are odd.
  - At ω the identity channel's a₀ and a₁ vanish (< 10⁻¹³) by rotation invariance, so the identity channel shows no
    ε-drift.
- **MAJOR.**
  - E5(c)'s pair (−3, 5) breaks q_L + q_R = 3, so it breaks both conditions at once. The pair (−2, 5), added as E5(d),
    keeps ū = 3w and equal norms and isolates R₁ ≠ 0.
  - §1.3's "the leptons' charges are integer multiples of the Higgs's" was false as a cause: the neutrino pair
    (−3, 0) satisfies it and is lifted (D = 2.90). The criterion is 9 | q_L − q_R.
  - The hand of w was an unstated input: with w = ψ₁τ + ψ₂ the same 18 pairs are non-fixed and the leptons are lifted.
    The minus convention is pinned by W59's set being invariant under the induced order-3 action, now checked in E0.
- **MINOR.**
  - E6's lepton half is an identity (det M′ = D/4), and is now labelled so. E6 gains the lift law,
    L·σ₃/σ₁ → |D|·|l_S(M_R)|/(8πσ₁²σ₂), with det Y(S, M) = det(M)·l_S(M).
  - E0 gains the exact line arithmetic.
  - E2's margin was 11× because of route A's old bias; it is now larger.
  - E5(a) and E6 used three lines of one ū class; they now mix in a b = 2/9 line.
- **TEXT.** These disclosures; §1.2's "a common b"; the four-channel premise stated; the identification of the massless
  lepton state with the electron; the Literature line.

**A second pass of a read-only reviewing agent** (`verification/before_the_seal/review2/`) found no decisive or major
defect and verified every fix. Its minor findings, all taken:
- **MIX3 did not mix.** The 18 lines are three classes of six under rotation and mirror, and (5/9, 5/9) mirrors
  (4/9, 4/9). MIX3 is now (1/9, 1/9), (4/9, 4/9) and (2/9, 2/9), one line of each class.
- **E0 gains three gates:** the lines' exact order 9, the plus convention's non-invariance, and the exact lines'
  match with the float lines.
- **E2's threshold falls from 10⁻⁷ to 5 × 10⁻⁹,** so E2 becomes a second guard on the a₀ term.
- **The blindness ledger is restated, and the nearest prior statements are cited.**
- **Text:** "pinned" becomes "supported"; the neutrino's D = 2.90 is the reviewer's unsealed computation; the lift is
  "proportional to D/L", with an S-dependent factor.

**What has been seen, cell by cell, after two review passes.** Every K_s depends only on (ū modulo the lattice, up
to sign, and τ), so other lines of the same class reproduce the sealed numbers.
- **E0, E3, E4.** Seen: the gates, perp spread 2.4 × 10⁻¹², gap −5.806896, D = (c₁ − c_⊥)R₁² to 3.9 × 10⁻¹³, lepton
  R₁ ≤ 4.6 × 10⁻¹⁵, quark D ≥ 1.031.
- **E1.** Seen through equivalent kernels: the corrected spread 1.35 × 10⁻¹¹ and control 8 × 10⁻¹³ on the same ū
  classes.
- **E2.** Seen through equivalent kernels: route B at n = 32 about 5 × 10⁻¹⁰ from route A.
- **E5.** (b) 2.9210 and (c) 3.2289, 2.8532, 3.2289. (d) is seen through equivalent kernels: {1.0312, 2.4629, 2.7416} by
  class.
- **E6.** The lift law on other lines and seeds; the tail risk by Monte Carlo (about 0.5% that one of the 30 sealed draws
  fails a 2% clause). Unseen only through the seed-1655 draws.

The thresholds were set with all of this in view.

**After the second review (2026-10-15).** The arc's number moved from B1655 to B1656: main's audit of its own negatives
(the owner's ruling on P-152) took B1655 and landed first. Main then explored the symmetric point at ω in the untwisted
fibre frame (POINT_REGISTER P-153, firewalled): a Higgs in M on an isotropic eigenline of the order-3 move gives rank one,
and the two light masses are the isotropy defects of the Higgs and of the zero-mode triplet. That exploration used the
untwisted triplet and a Higgs in M, not this arc's twisted channels on W59's lines. No cell, threshold or line of the
instrument was changed after it.

**Read before the seal, after the second review (2026-10-15, from the SM seat's branch at 37a5c5924):** W87, which proves
B1654's untwisted channel norms in closed form, c_r = −2π ln((π/2)∣θ_r(0)∣²), and D(τ) = −θ₃⁴h(λ)/(4πη⁶) (main checked
D against B1654's stored values, 1.3 × 10⁻¹⁴); and its reading of which flat hypercharge lines split the sectors (up and
down differ by 6w, down and the leptons by 4w; a line of order dividing 6 gives V = 1, of order 4 ties the down quarks to
the leptons; order 9, W59's, splits all three). Both are consistent with this arc's design; neither changed a cell. And
B1655's rule (E89): if a cell here fails, its failure is reported as the failure of the guess it encodes, and the arc's
finding is stated beside it.

## 1. The setting, and what follows by hand

- **The premises are B1654's P1–P4, with four channels.** The Higgs is S ∈ M₂(ℂ) = span{1, i, j, k}. Each unit's pairing
  P_s is a channel. Its boundary class is the conjugate twisted Szegő kernel K̄_s, K_s = P_s/R_s, cut at one end radius.
  The vacuum factorises, and the canonical end condition equalises the four channels' canonical amplitudes.
  - **The identity unit as a fourth channel is a new premise relative to B1654**, where R₁ = 0. The quarks' lift
    depends on it entirely (D = (c₁ − c_⊥)R₁²).
  - The electron's zero does not, because its R₁ = 0.
- **Stated inputs, not derived:**
  - the hypercharge dictionary (Q 1, u^c −4, d^c 2, L −3, e^c 6, H 3, in units of 6Y);
  - a flat hypercharge line w = ψ₁τ − ψ₂ (B1653);
  - τ = ω;
  - W59's Higgs lines (ψ₁, ψ₂) ∈ {(b + i/3, b + j/3) : b ∈ {1/9, 2/9}, i, j ∈ {0, 1, 2}}, the SM seat's selection.
    Within a line ψ₁ and ψ₂ share the same b.
  - **The line's orientation, w = ψ₁τ − ψ₂** (B1653's reviewer's finding). With w = ψ₁τ + ψ₂ the same 18 pairs would
    all be non-fixed, and the leptons would be lifted (E5(b)'s case). The minus convention is pinned by consistency:
    W59's set is invariant under the order-3 action it induces on (ψ₁, ψ₂), and is not in the plus convention (E0). This
    supports B1653's convention (its holonomy-cycle pairing); it restates rather than proves it, and it presupposes that
    W59's selection is ω-symmetric.
  - **An identification:** the lepton sector's massless state is the electron.
- **The sectors.** A field of charge q sees qw. For a sector (left, right), ū = (q_L + q_R)w and δ = (q_L − q_R)w.
  - Hypercharge conservation gives q_L + q_R = ±3 = ±q_H for every sector, so ū = ±3w, the Higgs's twist.
  - δ is 5w (up), −w (down) and −9w (leptons).

**What follows:**
1. **The cancellation.** u_s = √(2πL + c_s)·R_s, so u·u = 2πL(R₁² + R·R) + D = D, with D_sector = Σ_s c_s R_s². The log
   cancels because the residue quaternion is null (B1653).
2. **On W59's lines the Higgs's twist is ω-fixed.**
   - 3w = (3ψ₁)ω − 3ψ₂ with 3ψ ∈ (1/3 or 2/3) + ℤ, which is ±(ω − 1)/3 modulo the lattice. Those are the fixed points of
     z ↦ ωz.
   - The rotation then maps each imaginary channel's kernel to another's (it permutes i, j, k, as in B1654 §1.7) and
     fixes the identity channel, with ū fixed and the disc about 0 preserved.
   - So c_i = c_j = c_k =: c_⊥ in every sector, and **D_sector = c₁R₁² + c_⊥(R·R) = (c₁ − c_⊥)·R₁²**.
3. **The electron's zero.**
   - R₁ ∝ θ₁(ū)θ₁(δ). On W59's lines 9w lies in the lattice, since 9ψ ∈ ℤ, and θ₁ vanishes on the lattice.
   - So R₁(leptons) ∝ θ₁(−9w) = 0, while θ₁(ū) ≠ 0.
   - So D_lep = 0, u_lep ∝ R_lep is null, and the lepton coupling has rank ≤ 2 for every Higgs S and every L.
   - **The electron stays massless at this order.** The cause is the hypercharge arithmetic:
     q_L − q_e = −9 = −3q_H, and 3w is 3-torsion, so 9w lies in the lattice.
   - The criterion, for a line of exact order 9, is that 9 divides q_L − q_R. The quarks' 5 and −1 do not.
   - The neutrino pair (L, ν^c) = (−3, 0) does not either (−3), so a Dirac neutrino would be lifted, even though its
     charges are integer multiples of the Higgs's.
4. **The quarks.** 5w and −w are not in the lattice, so R₁(up) and R₁(down) ≠ 0. Then D_q = (c₁ − c_⊥)R₁(q)² ≠ 0, and
   the first generation is lifted, proportionally to D/L with an S-dependent factor (E6's lift law), for generic S.
5. **Both conditions are needed.**
   - With 9w in the lattice but 3w not ω-fixed, R₁(lep) = 0 still, but the imaginary norms split and D_lep ≠ 0.
   - With a fictitious pair that keeps q_L + q_R = 3 but whose difference is not a multiple of 9, such as (−2, 5),
     R₁ ≠ 0 with the norms still equal, and D ≠ 0.
   - At a generic τ there is no rotation, and D_lep ≠ 0.

## 2. The instrument

`verification/the_electrons_zero.py`, one run. It writes `the_electrons_zero.json` and `_run.txt` beside itself, after
every cell.
- **Route A.** numpy theta series, polar quadrature about 0 with s = log r, cut at ε. It restores the disc's constant
  term πε²|a₀|², with a₀ the circle mean of K_s − 1/z at radius 0.05.
- **Route B.** B1653's mpmath bilinear and product Gauss–Legendre over P, with 1/|z|², 2Re(a₀/z̄) and 2Re(a₁z/z̄)
  subtracted and restored analytically. The twisted kernels are not odd, so a₀ ≠ 0.
- **The coupling with channel weights.** M′ = Σ_s u_s E_s, with {E_s} dual to the unit pairings; Y_ab is B1644's coupling
  of M′ with the generations' blocks.
- **Points.** The 18 lines are W59's. The generic control is τ = 0.13+1.07i. The non-fixed lines are (1/9, 2/9),
  (1/9, 0) and (2/9, 1/9). MIX3 is three W59 lines, (1/9, 1/9), (4/9, 4/9) and (2/9, 2/9) (two with b = 1/9, one with
  b = 2/9). The 18 lines are three independent classes of six under rotation and mirror, which is why the quark
  |D|/|R|² takes exactly three values; MIX3 holds one line of each class.

## 3. The cells

| cell | prediction | prior |
|---|---|---|
| **E0**, plumbing (void if any fails) | route A's bilinear against B1653's mpmath bilinear < 10⁻¹¹ relative (two lines, three sectors, two points); the null quaternion < 10⁻¹²; B1653's residue formula R_s ∝ c_s θ_s(ū)θ_s(δ) (ratios to R_i) < 10⁻¹⁰ at five lines, two τ and three sectors; **the arithmetic, exact:** on all 18 lines 9w lies in the lattice, 3w does not (exact order 9) and 3w is ω-fixed; on the three non-fixed lines 9w lies in the lattice and 3w is not fixed; W59's set is invariant under the order-3 action in the minus convention and not in the plus convention; the exact lines match the float lines the cells use | 99% |
| **E1**, the universal log, four channels | with the disc's πε²\|a₀\|² restored, every channel's norm agrees across ε = 10⁻³, 10⁻⁴, 10⁻⁵ to < 10⁻⁹ (a W59 line at ω and at the generic τ, all sectors). **Control:** the residue-2 kernel drifts by 6π·log 10 per decade, to 10⁻⁶ relative | 95% |
| **E2**, two routes | routes A and B (n = 32) agree to < 5 × 10⁻⁹ on every channel of three cases: up on a W59 line at ω, leptons on a non-fixed line at ω, down at W59's phases (1/9, 1/9) at the generic τ | 90% |
| **E3**, the equal norms | on all 18 lines, every sector: c_i = c_j = c_k (spread < 10⁻¹⁰); the gap c₁ − c_⊥ is the same in every sector and on every line (spread < 10⁻⁹) and \|gap\| > 1; D_sector = (c₁ − c_⊥)R₁² to < 10⁻¹⁰\|R\|² | 97% |
| **E4**, the electron's zero | on all 18 lines: \|R₁(lep)\|/\|R\| < 10⁻¹² and \|D_lep\|/\|R\|² < 10⁻¹⁰; the quarks: \|R₁\|/\|R\| > 0.1 and \|D\|/\|R\|² > 0.5 | 95% |
| **E5**, the controls bite | (a) at the generic τ, \|D_lep\|/\|R\|² > 0.1 on MIX3; (b) on the three non-fixed 9-torsion lines at ω, \|R₁(lep)\|/\|R\| < 10⁻¹² yet \|D_lep\|/\|R\|² > 0.1 (equal norms are needed); (c) fictitious leptons (−3, 5) on MIX3, \|D\|/\|R\|² > 0.1 (charges matter); (d) **R₁ isolated:** the pair (−2, 5) (q_L + q_R = 3, so ū = 3w and the norms stay equal; q_L − q_R = −7) on MIX3: c_⊥ spread < 10⁻¹⁰, \|R₁\|/\|R\| > 0.1 and \|D\|/\|R\|² > 0.5 | 93% |
| **E6**, the masses | for five seeded random Higgs fields S ∈ M₂(ℂ), on MIX3: the lepton coupling with canonical weights has σ₃/σ₁ < 10⁻¹² at L ∈ {40, 640, 2560} (an identity: det M′ = D/4, a consistency check); the quarks have σ₃/σ₁ > 10⁻⁶ at L = 40, L·σ₃/σ₁ converges (2560 against 640 within 2%), and **the lift law** holds: L·σ₃/σ₁ at L = 2560 equals \|D\|·\|l_S(M_R)\|/(8πσ₁²σ₂) within 2%, with det Y(S, M) = det(M)·l_S(M), M_R the residue matrix and σ₁ ≥ σ₂ the nonzero singular values of Y(S, M_R) | 90% |
| **E7**, read-outs | the channel norms and \|a₀\| per sector on the line (1/9, 1/9) (the leptons' c₁ undefined, since R₁ = 0); the three quark values of \|D\|/\|R\|² and their cycle | — |

**What could fail, and what a failure would say:**
- **E3** fails if the rotation argument is wrong: the norms unequal, or the gap sector-dependent.
- **E4** fails if the lepton R₁ is not zero (the residue formula or the arithmetic is wrong), or if a quark sector has
  no lift.
- **E5(b)** fails if equal norms are not needed: then the electron's zero would come from R₁ alone.
- **E5(c)** fails if the charges do not matter. **E5(d)** fails if R₁ ≠ 0 alone does not lift the sector when the norms
  are equal.
- **E6** fails if the coupling's lift does not follow D: the lift law.

## 4. What it will not show

- which end condition is physical;
- whether τ = ω and W59's lines are nature's (both are stated inputs);
- any mass value: the quark lifts carry the end datum L and the Higgs's direction;
- the second generation;
- the neutrinos (a Dirac pairing with L − ν^c = −3 has δ = −3w, not in the lattice, so it is lifted: D = 2.90, the
  reviewer's unsealed computation; not a cell);
- a comparison with data.

Context, not a test: in nature the electron is lighter, relative to its generation's heaviest, than the down quark, and
heavier than the up quark.

0 of 19.
