# B1656 — THE ELECTRON'S ZERO: on W59's eighteen Higgs lines at τ = ω the charged leptons' first generation stays exactly massless under every channel weight, because q_L − q_e = −9 = −3q_H and W59's lines have 3w fixed by the order-3 move, so 9w lies in the lattice and R₁(leptons) = θ₁(−9w) = 0; the quarks are lifted, by three values in a 3-cycle

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.
- Sealed `27e7e7482` (sha256 c4cfc3c0) before the run. The output was committed unread at `ad26e995d` (one run, 277 s,
  exit 0; the instrument unchanged since the seal, sha256 8abe8b53).
- No data. **0 of 19.**
- POINT_REGISTER P-151, the second arc of C (after B1654). It bears on the parent's clause 7 (split the down quarks from
  the charged leptons), P-128 and P-129.

## 0. Seen first

As sealed: `VERDICT topic-sweep /twisted (channel|szeg|norm)|electron.{0,20}(zero|massless)|lepton.{0,20}(zero|massless)|9.torsion|omega.fixed|order.3 rotation/: 8 of 1427 arcs on main match (NEGATIVE 1, PROVED 7)`;
the design's sweep (13 of 1426) also matched B1435, B1490, B928, B1294 and B1453, all read. None states an electron zero.
The nearest fact on record is B1653's U7 read-out (the leptons' triplet isotropic on W59's lines), which by the null
quaternion is R₁(leptons) = 0, seen there without the norms. **Read before the seal:** the SM seat's W59 (the eighteen
lines), W87 (the untwisted norms in closed form) and its reading of which hypercharge lines split the sectors (order 9,
W59's, splits all three). **Literature:** Szegő kernels with characteristics; flat line bundles on an elliptic curve.

## 0b. Disclosed

In full in the preregistration's §0b. In brief: main's exploration saw the values the cells read (through equivalent
kernels for E1, E2 and E5(d)); two passes of read-only reviewing agents before the seal (the first found E1's missing
πε²∣a₀∣² term, decisive; the second MIX3, E0's exact gates, E2's threshold, the blindness ledger and the priors), their
scripts beside the seal with their absolute paths made relative before the seal; the number moved from B1655 (main's
audit took it); main's later, untwisted exploration of the symmetric point (P-153) changed no cell.

## 1. The sealed run (`verification/the_electrons_zero.py`, unchanged; `.json`, `_run.txt`)

**E0, plumbing** (not void): route A's bilinear against B1653's mpmath bilinear 5.2 × 10⁻¹⁵; the null quaternion
8.6 × 10⁻¹⁶; B1653's residue formula 5.6 × 10⁻¹⁵; the arithmetic exact — on all 18 lines 9w lies in the lattice and 3w
is ω-fixed, the lines' exact order is 9, the three non-fixed lines have 9w in the lattice and 3w not fixed, W59's set is
invariant in the minus convention and not in the plus, the exact lines match the float lines.

| cell | prediction | prior | result |
|---|---|---|---|
| **E1**, the universal log, four channels | norms agree across ε = 10⁻³…10⁻⁵ to < 10⁻⁹; the residue-2 control drifts by 6π·log 10 | 95% | **HOLDS:** 1.3 × 10⁻¹¹; control in [1 − 2 × 10⁻¹⁴, 1 + 1.2 × 10⁻¹²] |
| **E2**, two routes | A and B agree < 5 × 10⁻⁹ in three cases | 90% | **HOLDS:** 2.8 × 10⁻¹⁰ |
| **E3**, the equal norms | c_i = c_j = c_k (< 10⁻¹⁰); the gap c₁ − c_⊥ the same in every sector and line (< 10⁻⁹), ∣gap∣ > 1; D_sector = (c₁ − c_⊥)R₁² (< 10⁻¹⁰∣R∣²) | 97% | **HOLDS:** 2.4 × 10⁻¹²; gap −5.806896 (spread 1.2 × 10⁻¹²); 3.9 × 10⁻¹³ |
| **E4**, the electron's zero | ∣R₁(lep)∣/∣R∣ < 10⁻¹², ∣D_lep∣/∣R∣² < 10⁻¹⁰ on all 18 lines; quarks ∣R₁∣/∣R∣ > 0.1, ∣D∣/∣R∣² > 0.5 | 95% | **HOLDS:** 4.6 × 10⁻¹⁵ and 5.0 × 10⁻¹³; quarks at least 0.421 and 1.031 |
| **E5**, the controls bite | (a) generic τ lifts the leptons > 0.1; (b) non-fixed lines: R₁ = 0 yet D > 0.1; (c) fictitious leptons (−3, 5) lifted > 0.1; (d) the pair (−2, 5): equal norms, R₁ > 0.1, D > 0.5 | 93% | **HOLDS:** (a) 3.081; (b) R₁ ≤ 3.2 × 10⁻¹⁶, D 2.921; (c) 3.229, 2.853, 4.513; (d) c_⊥ spread ≤ 1.8 × 10⁻¹², R₁ ≥ 0.421, D ≥ 1.031 |
| **E6**, the masses | leptons σ₃/σ₁ < 10⁻¹² (an identity); quarks lifted, L·σ₃/σ₁ converging within 2%, and the lift law within 2% | 90% | **HOLDS:** 1.2 × 10⁻¹⁵; convergence 1.6 × 10⁻³; the lift law 5.4 × 10⁻⁴; quark m₁/m₃ at L = 40 from 2.4 × 10⁻⁴ to 1.0 × 10⁻² over the five Higgs fields |

**E7, read-outs** (line (1/9, 1/9)): c₁ = −3.575627, c_⊥ = 2.231269 in every sector (the leptons' c₁ undefined, since
R₁ = 0); ∣a₀∣ = 2.428651 on the ⊥ channels. **The quarks' lifts on the 18 lines** (∣D∣/∣R∣², up and down): (2.7416,
1.0312) on six lines, (2.4629, 2.7416) on six, (1.0312, 2.4629) on six — down's value on one class is up's on the next,
a 3-cycle; the leptons 0 on all eighteen.

## 2. What it shows

- **The electron's zero is arithmetic.** With the dictionary's charges (6Y: L −3, e^c 6, H 3), the leptons' twist
  difference is q_L − q_e = −9 = −3q_H, and on W59's lines 3w is fixed by the order-3 move, so 9w lies in the lattice and
  θ₁(−9w) = 0: R₁(leptons) = 0, and with the equal norms at ω (E3) the leptons' D vanishes. The first generation of the
  charged leptons stays massless at this order **for every Higgs field and every channel weight** on these lines. The
  controls show each ingredient is needed: off ω (E5a), off the ω-fixed lines (E5b: R₁ = 0 but the norms unequal),
  with other charges (E5c), and with R₁ ≠ 0 at equal norms (E5d), the leptons are lifted.
  On these lines R₁(leptons) vanishes at every τ, not only at ω, since 9w is a lattice point whatever τ is (the SM
  seat's W89 read-out); what is special to ω is the equal norms, which make D_lep vanish with it.
- **The quarks are lifted**, and the size is one canonical function per sector: D_sector = (c₁ − c_⊥)R₁² with one gap
  (−5.8069) for every sector and line. Up and down differ on every line, so **this frame splits the down quarks from the
  charged leptons** (the parent's clause 7) and up from down, at τ = ω on W59's lines.
- **The L-independent numbers** are the ratios across sectors on a line: up : down = 2.7416 : 1.0312, 2.4629 : 2.7416 or
  1.0312 : 2.4629, depending on the line's class, and leptons 0. They are the first structural numbers of this frame;
  the masses still carry L and the Higgs's direction (E6's lift law).
- **Context, not a test** (as the preregistration said): in nature the electron is lighter, relative to its generation's
  heaviest, than the down quark, and heavier than the up quark. Here, at this order, the electron is the lightest of the
  three (exactly zero). So the electron's mass, in this frame, must come from beyond this order or from elsewhere —
  B1657's Higgs defect, a second-order term, or another line.

## 3. What it does not show

Which end condition is physical; whether τ = ω and W59's lines are nature's (both stated inputs); any mass value; the
second generation; the neutrinos (a Dirac pairing L–ν^c has δ = −3w and is lifted, D = 2.90, the reviewer's unsealed
computation, not a cell); any comparison with data; the interacting weave (one fibre at ω, the field held fixed).

## 3b. Verified on an independent seat

The SM seat's W89 (rule 0e301c52a, script f71da8733, output 6fb4eabb7) checked every claim here on its own code before
main's run landed — twisted norms by W87's polar quadrature with the argument reduced modulo the lattice, residues from
W85's 60-digit series, the arithmetic in exact rationals — and found the same numbers to every printed digit: the gap
−5.806896, the leptons' R₁ ≤ 2.1 × 10⁻⁵⁹, the quarks' three classes 1.031150, 2.462927, 2.741626. Harvest row 1192.

## 4. Credit

The SM seat: W59 (the lines and τ = ω), C0 (the boundary class), W87, its hypercharge-lines reading, and W89, the
independent check. Main's two
read-only reviewing agents: the first found E1's missing term; the second MIX3, E0's exact gates and an honest ledger.

## 5. Next

B1657 (the symmetric point: two isotropic vacua, two laws), in review before its seal: with the Higgs on an isotropic
line its conjugate law makes the lifted light mass ∣d_v∣ = ∣D_sector∣/(2πL∣R∣²), so this arc's three values become
cross-sector mass ratios at fixed L and Higgs direction; and the Higgs's own defect is the candidate source of the
electron's mass.
