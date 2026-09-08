# B1305 — SLICE B: THE QUANTUM-FACE LINE (cloud memos 174–182 + the relay of 2026-09-08): DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-08 (night) · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1305 (iii), pulled forward because a received relay
outranks the queue · **Cloud pinned:** `origin/outside-bench` @ `792918b7` (worktree `oa-audit-seat/cloud-seat-792918b7`) · **Read in full
before this seal:** memos 174 (THE_FIRST_MEASUREMENT), 177 (THE_CEFF_SCALING_LAW, with addenda 1–7), 180 (THE_VERIFICATION_LEDGER), the relay
`CLOUD_TO_CC_2026-09-08_Q1_THE_QUANTUM_FACE.md`, `certificates/trefoil_ends.py`; the heads of 175, 176 (its retraction note), 178, 179, 181,
182; Gukov–Manolescu arXiv:1904.06057v2 located and quoted from the text (pp. 6, 7, 52, 68, 72–73: the positive-trefoil sentence, eq. (13),
the trefoil's range p/r ∉ [0, 6], eq. (166), eq. (175) with F₀, the definition of c, condition (177), c = −1/16 "experimentally", the range
(−4, 0), Table 10); the abstracts of Armond–Dasbach arXiv:1106.3948 (head and tail depend only on the reduced checkerboard graphs),
Garoufalidis–Lê arXiv:1112.3905 (stability for alternating links), Gukov–Jagadale arXiv:2308.05360, HJNP arXiv:2508.10087. **Seat certificates
re-run in the pinned worktree before this seal (receipts in `verification/sliceB/`, RC=0 unless stated):** `trefoil_ends.py` (3₁: bottom
±(q;q)_∞, top 1, windows 13–14; 4₁: (q;q)_∞ at both ends, window 15), `table10_control.py`, `mock_theta_ceff.py` (χ₀ → 0.1999996, F₀ →
0.1428569), `colored_jones_validate.py`, `ceff_scaling_law.py`, `xi_recursion_fast.py`; `park_52_blocks.py` **RC=1** — it reads an untracked
scratch file (`/tmp/k52/ahat.py`) that exists only on the seat's machine: the seat's own stuck item, and an E57-shaped certificate.

## 0. The rules' lines and the view from above

- `already_banked.py "colored Jones" "head and tail" "mock theta" "c_eff" "Zhat" "surgery formula" "chirality-odd"`: run at the seal (line in
  the receipt); main's own quantum-face work is B685/B690/B697/B800 (Habiro ring, the being-hand asymmetry, GSWZ's Φ·τΦ) and B1190/GC-6
  (the σ bridge's 6-vs-1). `absence_sweep.py "head and tail"` and `"colored Jones tail"`: run at the seal.
- **The view from above.** Q1 of the fresh-eyes register asked what the Vol ≠ 0 face says about chirality. The cloud's answer is a
  mechanism, not a number: the two ENDS of the colored Jones polynomial are swapped by the mirror, so their difference is a mirror-odd
  invariant, and on an amphichiral knot it must vanish — the ends coincide. That is B1227's theorem in a FOURTH value group (formal
  q-series with constant term ±1, under quotient: the head/tail ratio is 2-torsion, so ±1, for amphichiral knots), and it is why this
  face, like the other three, reads "2 or nothing" on m004. The literature already has the mechanism (Armond–Dasbach 2011: head and
  tail from the reduced checkerboard graphs; the mirror swaps the graphs); the cloud's contribution is the reading and the computation.
  What the cloud did NOT produce is a generation count on this face — Q1's other half stays open. The second thing the relay carries is
  a correction of GC-6's reading of the σ gap (6 = 1 + 5, the 1 universal) and the quantitative ceiling c_eff < 1 on the figure-eight's
  Ẑ at every convergent slope: the σ bridge's target 6 is unreachable on this route, by the cloud's numbers, which this slice checks
  where main's code can and records as the seat's where it cannot. **Nothing here moves the chirality bit; it closes Q1's chirality half,
  sharpens the invariant's name, and prices Phase 3's DESIGN.**

## 1. Pre-registered questions — predictions before the scripts exist; PASS and FAIL both reachable

**Q1 — the two ends, re-derived with main's own code** (`b1305_ends.py`). J_n(4₁) from GM eq. (166) (Habiro form, coded independently);
J_n(3₁) by TWO formulas — Habiro's cyclotomic expansion (as the certificate) and the Rosso–Jones/Morton torus-knot formula for T(2,3) —
cross-checked against each other at n = 2, 3, 4 and against the Jones polynomial J₂(3ʳ₁) = q⁻¹ + q⁻³ − q⁻⁴. Predictions: (a) the two
trefoil formulas agree exactly for n ≤ 4; (b) at matched parity the trefoil's bottom end stabilises to ±(q;q)_∞ and its top end to the
trivial series (windows ≥ 12 at n = 13, 15), and 4₁'s two ends both to (q;q)_∞ (window ≥ 14 at n = 15, 16); (c) the mirror 3ˡ₁ (q ↦ q⁻¹)
has the ends swapped; (d) **the B1227 reading:** the head/tail ratio R(K) = top-end series / bottom-end series (normalised to constant
term +1) satisfies R(K*) = R(K)⁻¹, hence R² = 1 for an amphichiral knot: predicted R(4₁) = 1 exactly on the stable window and R(3ʳ₁) =
1/(q;q)_∞ (the partition generating function), R(3ˡ₁) = (q;q)_∞. PASS = (a)–(d); FAIL = any end differs from the cloud's or R(4₁) ≠ 1.

**Q2 — Gukov–Manolescu's constant c, and what exactly is mirror-odd** (`b1305_blocks.py`, using the cloud's Ξ generator as a data source in
the pinned worktree and main's own check on its output). GM define c by "the lowest powers of q in the coefficients f_m(q) of x^{m/2} have
exponents of the order of c·m²" (p. 72) and state c = +1/24 (3ʳ₁), −1/24 (3ˡ₁), −1/16 (4₁, "experimentally"). The relay calls c "the
chirality-odd invariant on this face". **Prediction (the precision point):** for 4₁ the blocks Ξ_k are PALINDROMIC — lowest exponent
−⌊(k−1)²/4⌋ and highest +⌊(k−1)²/4⌋ for every k ≤ 20 — so c_low = −1/16 and c_high = +1/16 and the mirror-odd combination (c_low + c_high)/2
is **0**, as B1227 requires of an amphichiral knot; for the trefoils GM's Thm 1.3 blocks are single monomials, so c_low = c_high = ±1/24 and
the odd combination IS c. So: **the chirality-odd invariant is the CENTRE of the block's exponent range; the WIDTH (c_high − c_low)/2 —
1/16 for 4₁, 0 for torus knots — is mirror-even and is what feeds c_edge and the c_eff ceiling.** "c is the chirality-odd invariant" is
exact for torus knots and not in general (4₁ has c = −1/16 ≠ 0 while amphichiral). PASS = palindromic 4₁ blocks for all k ≤ 20 and the
trefoil's monomial blocks at ±(2k−1)²/24 + O(k); FAIL = a non-palindromic 4₁ block (then the framing question is reopened, not settled).

**Q3 — the two mock-theta growth rates with an own estimator** (`b1305_mock_theta.py`). F₀(q) = Σ q^{n²}/(q^{n+1};q)_n (GM eq. 175; GJ's
Σ(2,3,7)) and χ₀(q) = Σ qⁿ/(q^{n+1};q)_n (GJ's Σ(2,3,5)), 20 000 coefficients each, exact integers; the first coefficients must match GM
eq. (175)'s printed 1, 1, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 1, 3 and the receipt's χ₀ 1, 1, 1, 2, 1, 3, 2, 3, 3, 5, 3, 6; then a three-parameter fit
log a_n = A√n + B log n + C on the last half, c_eff = 3A²/(2π²), calibrated on 1/(q;q)_∞ (must give 1 ± 0.001) and on the Rogers–Ramanujan
G(q) (must give 2/5 ± 0.001). Predictions: **c_eff(F₀) = 1/7 ± 0.0005, c_eff(χ₀) = 1/5 ± 0.0005, B = −½ ± 0.01.** The relay's "6 = 1 + 5"
is then recorded as: the bare growth rates are 1/5 and 1/7 (verified here), and the "+1" is GJ's half-index prefactor q^{−1/24}-type
factor as the cloud reads GJ's eq. (55) — GJ was read at abstract level here, so that split is REGISTERED as the seat's reading, not
verified. PASS/FAIL per number.

**Q4 — the cloud's Ẑ assembly against Gukov–Manolescu (seat scripts, not re-derived here):** Table 10 (nine −1/r series), eq. (13), eq. (175),
c = −1/16 with the range (−4, 0), the Legendre law and sup c_eff = 1 — all VERIFIED as the seat's computations by the re-runs above;
GM's printed statements verified in the paper's text here. The assembly itself (recursion (171)–(172) + Thm 1.2) is NOT re-implemented in
this slice: it is Phase 3's DESIGN work (v3.1 §6), where GM is read in full and the surgery formula re-derived with main's code. Recorded
as the seat's, with its own verification ledger (memo 180: eleven of thirteen GM inputs checked on their bench; no error found in GM).

**Q5 — dispositions without computation:** memo 176 §5–7 SUPERSEDED-BY-SEAT (the Legendre law of memo 177 replaces the tangent; the Gelfond
and Lehmer sections retracted by the seat); memo 179's calculator and memo 182's Park R-matrix check VERIFIED as scripts by re-run
(`colored_jones_validate.py` RC=0); memo 182's `park_52_blocks.py` VERIFIED-DIFFERS (script: an untracked scratch dependency; the seat's stuck
normalisation between Park's F⁺ and GM's Ξ is registered as its open item, not ours); memo 178 (GC-6 substituted η⁻¹; the substitute is the
object) REGISTERED against B1190/GC-6 with the 6 = 1 + 5 reading — B1190's row gains a dated note, no verdict change on main (the σ bridge
was already O3 obstructed, B1064).

**Q6 — the sense census, re-pre-registered with a meta-exclusion list** (`b1305_sense_census.py --exclude`): exclude `frontier/B1305_*/`,
`docs/HARVEST_LEDGER.md`, `docs/CAMPAIGN_STATUS.md`, `docs/RELAY_LEDGER.md`, `docs/FRESH_EYES_2026-09.md` (the surfaces that quote seats about
gaps). Prediction on main at HEAD: `logarithmic` returns to FALSE COMFORT (occurrences 10 ± 2, technical 0), `non-semisimple` stays FALSE
COMFORT, `Chern-Simons` stays genuine (≥ 40 %), `character` stays FALSE COMFORT — the two-sided control PASSES. If PASS: ADOPT as a checks
script with `--selftest` (the two-sided control with the exclusion list + the three planted controls), WORKING_RULES' ABSENCE RULE gains its
second half, PRACTICES the note, the cloud credited (memo 172). FAIL = the control still fails (then NOT ADOPTED, reason recorded, no third try
without a new idea).

**Q7 — registrations:** FRESH_EYES Q1 → "chirality half CLOSED by computation (cloud + main): the ends; the count half OPEN"; Q6 → mechanism
verified on the quantum face; Q10 → the access answer recorded and the per-seat source-fetch check added to Phase 4 (1); the FOURTH regime
of B1227 (formal q-series ends) registered on the theorem row as a hint-level note (the value group is not a group of numbers; stated as
the head/tail ratio being 2-torsion); RELAY_LEDGER row → BANKED (B1305); HARVEST_LEDGER rows for memos 174–182 and the relay; B1190's dated
note; hint rows; the held reply to the cloud drafted (owner: all sends hold).

## 2. Priors

Q1 (a)–(d): 90 % (the formulas are classical; the risk is a convention slip in the torus-knot formula, which the n ≤ 4 cross-check catches).
Q2 palindromic 4₁ blocks: 85 %. Q3: 90 %. Q6 after exclusion: 80 %. Expected verdict: **VERIFIED (the ends, the growth rates, the seat's
assembly by re-run) + VERIFIED-DIFFERS on one framing (what is mirror-odd: the centre, not c) + ADOPTED (the sense census, second try under
a new pre-registration) + REGISTERED (the fourth regime; GC-6's re-reading; the seat's stuck item).**

## 3. Method, controls, discipline

Own code for Q1–Q3 and Q6; the cloud's scripts re-run in the pinned worktree with their receipts; every prediction asserted with PASS and FAIL
branches; pytest's own rc; quotations located in GM's text before use (E68); seat credited by memo and pin; no grade lowered without a
computation; loose relay files never at root; the cloud's own retractions respected as its dispositions. Out of scope: re-implementing the
surgery assembly (Phase 3), 5₂'s F_K, the Park/GM normalisation, any σ claim, any generation count on this face.
