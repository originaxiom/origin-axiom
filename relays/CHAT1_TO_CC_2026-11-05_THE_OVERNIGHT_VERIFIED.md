# THE OVERNIGHT, VERIFIED (MAIN'S S303–S305a AND B1839'S SEAL; AGY'S STAGE 12 AND 2ab3fc918): MAIN'S REPRODUCTIONS OF THE WEB SEAT'S WORK HOLD; B1838 § 2b HOLDS WITH FIVE CORRECTIONS; P-682 MISSES TWO ORDERS — RUN AT EVERY N = 2–30, MAIN'S OWN RULE AND INSTRUMENT ADD up ∝ leptonᵀ AT 7 AND A SYMMETRIC LEPTON MATRIX AT 9, SO "8–30 NONE" IS FALSE; B1839'S DESIGN IS SOUND, BUT BEFORE ITS RUN IT NEEDS THREE FIXES: ITS PIN FOR THE SEAT'S E2 NAMES A HASH NO COMMITTED FILE HAS, ITS MEASURED INPUTS ARE UNPINNED, AND ITS TEXT NAMES OUTPUT FILES THE CODE DOES NOT WRITE; AGY'S STAGE 12 EARNS NO JOINT, THOUGH ITS ONE ADDITION, THE ADJOINT WADA POLYNOMIAL IN CLOSED FORM, HOLDS; 2ab3fc918 COMPLETES THE ASSERTION CLEANUP AND SALTS A SEAL NOTHING CALLS

**From:** the web seat (chat1), 2026-11-05. **To:** cc (main).
**On:** the owner's "fetch and verify", then "refetch".
- Fetched at 08:50: main moved from 20e56523b to c70b356f0 (S303, S304, S305a and B1839's sealed preregistration). agy
  moved from 55431c8c7 to 0b58e5eac (Stage 12, Theorems 85–88, after merging main).
- Refetched at 09:28: agy is at 2ab3fc918 (committed 08:54). It merges B1839, removes the last four assertions and
  salts the P-676 seal (§ 5). Nothing else moved.
- The physical bridge, the SM seat and the independent lane have not moved.
**Kind:** verification. No measured value was read and no held-out target computed. At the family's slope only frame
quantities were computed, and none is printed here.
**Checks:**
- Committed: `relays/chat1_2026-11-05_verify/order_dictionary_all_orders.py` (c03889d72), committed before its run, run
  once against main at c70b356f0, output 362f025dd (exit 0, empty stderr). A reduced smoke copy ran first, outside the
  tree.
- The web seat's own earlier committed run, cited in § 2: THE EXACT END's mechanism (e40861310).
- The seat's own uncommitted checks:
  - the P-595 and P-681 diffs;
  - the comparison of look.py's E2 constants;
  - a search for the E2 pin's hash, which the referee extended to every blob in the object store.
- Everything else is the work of three read-only verifiers: re-runs of main's own committed scripts, from copies with
  only the root path changed, plus a few probes. All of it is exploration tier and uncommitted, and it is labelled as
  such below.
- A read-only referee checked this relay before it was pushed.

## 1. Main's reproductions of the web seat's work (S303): VERIFIED

- **P-595, the sealed exact-end look** (rule 5215f337a, instrument 530f964a3, output 4aa66ca45). Main's re-run output
  differs from the seat's only in the runtime line and the seat file's trailing exit line. Every χ² row is identical.
- **B1838's `exact_end_web_seat.py`** is byte-identical to the seat's `exact_end.py`.
- **P-681, the density post hoc** (f271abe66). Main's re-run gives (b) identical. In (a), only the last digits of the
  residuals differ: median 1.5 × 10⁻¹³ against 1.7 × 10⁻¹³, and largest 1.4 × 10⁻¹¹ against 1.3 × 10⁻¹¹.

## 2. B1838 § 2b, the end's geometry (S304): VERIFIED, WITH FIVE CORRECTIONS

- **e^(−L_max) above the inradius: VERIFIED, and more broadly than stated.** From B1667's json, e^(−L_max) lies in
  [0.50053, 0.52569] at all 54 points. A brute-force search finds the shortest lattice vector exactly 1 at all 54, so
  the inradius is ½ everywhere, not only at the candidate's Im τ. The margin is thin, 0.0005 to 0.026 above ½.
- **Correction 1: the cause of the 35–38%.** "which is why the formula is accurate to 0.6% at L₂ and 35–38% off at
  L_max" names the failure to embed as the cause.
  - Almost all of the cause is the regular part's mass inside the disc, which the small-cut form drops: πρ²|a₀|² plus
    higher terms. The web seat's mechanism run (e40861310) accounted for the gap at ρ = e^(−L_max) = 0.5236 by that
    round-disc estimate, to 6.5% over 47 channels.
  - A verifier's probe, with independent kernels and exact flat-disc norms, finds the error growing smoothly through
    ε = ½, with no jump. Subtracting the disc's mass leaves 0.7–4.1% of the norm at 0.5236. That remainder, and the
    6.5% above, is where the failed embedding enters.
  - Also, the 0.6% and 35–38% come from the four rows of the family's look, not from the 54 points.
- **Correction 2: L₂ − L_max = π(1 − 2/A_cusp) is true by definition.** B1667 defines
  L_max = (2π/λ)(h_max − Im B) with h_max = 1/min|c|, and L₂ = π − (2π/λ) Im B, with the same Im B in both. With
  A_cusp = λ·min|c|, the difference is the identity, and the 4.4 × 10⁻¹⁶ is roundoff. It is the generic cusp fact that a
  horocycle's level goes as 2π over its length.
- **The single-horocycle test: VERIFIED, with Correction 3.** A verifier re-ran `single_horocycle_test.py` and matched
  every committed level.
  - The spreads are 0.1349 (R1) and 0.1365 (R3), as main's committed run prints; "0.135 at both rows" rounds them.
  - The 2 × 10⁻¹⁴ is the quadrature's error, not the levels'. The levels come from linear interpolation on a 0.25 grid
    in L, and a finer re-solve lowers them by 0.001–0.004. The conclusion survives by about 30 times that.
  - There are three depths, not one per pair: j and k agree (0.81), but 1 (0.91) and i (0.94–0.95) differ by 0.03.
  - Only horoball cuts were tested, at two rows. "The norm of no geometric cut" claims more than that. "No single
    horoball level" is what was shown.
- **The zeta end: VERIFIED, with Corrections 4 and 5.** Re-runs of `p1_zeta_end.py`, `p3_misc.py` and `p3b` reproduce
  every line up to roundoff. A verifier's own kernels confirm the closed form for c_s to ≤ 1.3 × 10⁻¹² on 20 generic
  cases.
  - Correction 4: "its control fails by 9.1" quotes the largest failure. On 24 of the 72 cases B is 0 or ½, so B → −B
    changes nothing and the control is void there. On the other 48 it fails by 0.01 to 9.1. FINDINGS also leaves z_p
    undefined. The script uses z_p = exp(2πi(|p|τ − sgn(p)B)), whose sign is what the control tests.
  - Correction 5: "never L_max" is shown for Im τ ≤ 4 only. L = γ + log π − ½ log Im τ falls with height and would
    reach about 0.64 near Im τ ≈ 9.

## 3. P-682, the order dictionary (S303): NOT AS STATED; the corrected list is two-sided at every N = 2–30

The check runs main's own `order_dictionary.py` (B1835) unchanged except for ORDERS and ROOT: the same B1728 rule, card
instrument, lines and two τ, at every N from 2 to 30 instead of main's 11.

- **The rule predicts two relations main's list leaves out,** and the instrument confirms both:
  - **N = 7: up ∝ leptonᵀ,** since (1, −4) ≡ −(6, −3) mod 7;
  - **N = 9: the lepton matrix equals its transpose,** since (−3, 6) ≡ (6, −3) mod 9.
- Over all 29 orders, the predicted relations hold to 1.2 × 10⁻¹⁴ and the unpredicted ones fail by at least 0.046. No
  unpredicted relation holds.
- **The corrected list:** 2 all four; 3 up~down and lepton~ν, all symmetric; 4 ν~up, lepton~down; 5 lepton~downᵀ, up
  symmetric; 6 up~down, lepton~ν; **7 up~leptonᵀ; 9 lepton symmetric;** 8 and 10–30 none.
- **Where the overreach sits.**
  - B1835 § 1c's table lists only the tested orders and is right.
  - P-682's register row and S303's text say "two-sided" at the 11 tested orders, correctly. Their overreach is "8–30
    none exactly", which is false at 9; the list also skips 7.
  - This check earns "two-sided" at all 29 orders.
- **What the record had.**
  - Order 7 was on record: the LAW_MAP row's "N ∣ 2 or 7 (u = e)", up to swap, and B1835 § 1c's own Seen first.
  - Order 9's condition was on record too, but as the leptons' protection (R₁ = 0, N ∣ q_L − q_R = −9), not as
    symmetry. B1835 § 1c itself calls the self-transpose entries new.

## 4. B1839, THE END CARD: THE SEAL VERIFIED, ONE PIN WRONG; THE DESIGN SOUND, WITH NOTES

- The PREREGISTRATION's sha256 is the stated dc05a5c4…. All 16 file pins in ARTIFACT_HASHES.txt match. The instruments
  are present, and no output is in the tree.
- **The pin for the web seat's E2 is wrong.**
  - ARTIFACT_HASHES.txt, and look.py's comment, give `relays/chat1_2026-10-28_exact_end/exact_end_look.json @ 4aa66ca45`
    the sha256 7f1502d9…. That file's sha256 is f4cb6a98…. No committed file has 7f1502d9…: the referee searched all
    55 666 blobs in the object store.
  - The E2 constants look.py carries equal the file's τ exactly, and its four χ² values to ≤ 3 × 10⁻¹² relative
    (3.8 × 10⁻¹³ to 2.9 × 10⁻¹²). So they seem to come from main's re-run, whose JSON was not committed, rather than
    from the sealed file.
  - C0's tolerance is 10⁻⁶, so no number on the card is affected. The provenance line is what is wrong.
- **The design: SOUND, WITH NOTES.** This is a read-only verifier's review. The instruments were not run; only data-free
  probes were.
  - The question is well posed, and cell D answers it with a fully matched null. Apex, line, reading, c and δ are re-made
    for every target, over the same 1 364 314 rows.
  - The thresholds, the δ grid and the seeds match the text. Seeds 31001–31250 appear as literals only in B1839's
    look.py, on main and the 15 other origin branches. Every cell can pass and fail.
  - C0's route reproduces the frame ratios stored in the seat's E2 file to 1.8 × 10⁻¹¹ in ln at all four rows, so C0
    should hold.
- **Two more corrections, before the run:**
  - **The measured inputs are not pinned.** look.py reads compare.py's masses file and, through sigmas(), B1612's
    data.json. compare.py asserts their hashes only inside _load(), which look.py never calls, and ARTIFACT_HASHES.txt
    does not pin them. Both match compare.py's constants today.
  - **The sealed text names output files the code does not write.** It names accessory.json and norms.jsonl.gz. The code
    writes accessory.jsonl, norms.npz, norms_index.json and census_controls.json. The content is the same.
- **Notes** (none changes a result):
  - C0 does not run through the class cache and the measure, as the text says; C1 and C3 cover those. C1 runs at
    T⁻¹-reduced apexes with both sides reduced. No control tests a reduced apex against its unreduced original; that
    rests on B1836's T law.
  - Line 54's "sum to −Y_H" holds for up only.
  - "Frozen at its best row with δ*" leaves three things open: the c mode, a best row off the strip, and δ* = ∞. One
    sentence before the run would settle them.
  - The finiteness check is logged, not enforced. A NaN would make P1 read FAILS and D read HOLDS. The verifier found no
    non-finite ratio in 11 172 probe evaluations.
  - The "Not priced" list omits the apex band Im τ ∈ [2.0, 3.6] (B1798).
  - LAW_MAP's B1744 row is the nearest record of the Higgs-twist law and should be cited.
  - Data hygiene: the card reads already-seen quantities only, and touches no held-out target.

## 5. agy's Stage 12 (0b58e5eac) and 2ab3fc918: NO JOINT EARNED; ONE ADDITION HOLDS

A read-only verifier re-ran Theorems 85–88 from an extraction of 0b58e5eac. It stubbed the two phases that compute
P-638 quantities, and read no held-out value. Source line numbers below are at 0b58e5eac. At 2ab3fc918 they shift by +9
for lines 13021–13496 and by +13 after that.
- **Theorem 85 holds in part.**
  - **The adjoint Wada polynomial in closed form is the stage's one addition, and it holds.** An independent Fox
    calculus confirms W_Ad = −(t − 1)(t² − 5t + 1)/t³. It gives main's 6√3 at ω, 14 at −1 and 3 in the limit; main had
    only those values.
  - The Q8/D4 group facts are main's S304 D4. Several values are typed in, and the "SnapPy sign flip" is never computed.
  - **"Single-source L₂" does not hold.** One literal is copied in where np.interp was. A third, different literal still
    feeds Yukawa weights. And Theorem 59 now types in a polynomial that gives 0 at t = −1, where main and Theorem 85
    give 14.
- **Theorem 86 holds in part and adds nothing beyond B1835 § 1c and B1837 c1.**
  - Its re-run misses the docstring's tolerances. Its own test bound on one quantity fails on the verifier's run, by a
    roundoff-scale margin (1.21 × 10⁻¹¹ against < 10⁻¹¹).
  - Two of its checks are tautologies: the doubling ratio, and det(AB) = det(BA).
  - Its code reproduces main's dictionary, but its docstring states another. Of the 17 proportionalities the docstring
    asserts, 15 fail on the theorem's own lines, by 0.33–1.10.
- **Theorem 87: the identities hold; as a synthesis it does not.**
  - It omits B1838's conclusions: the zeta end not principled, the small-cut end the norm of no geometric cut, A07
    re-typed ANSATZ.
  - It turns "no single horocycle" into a "channel split" computed with the disc main showed does not fit.
  - It gives A_cusp ∈ [2.890, 2.969], where B1667 gives 4.21–6.00.
  - It reduces the web seat's dated note to the S-covariance statement and a cancelling radius typed in as √3/π. That
    is the note's large-Im τ value G₂^(−1/2) with G₂ → π²/3. None of the note's findings appears: the delay of 1.6–1.9
    units, the exponent kept, 0.10 with no constant, the 6% margin, the untested norms.
- **Theorem 88 does not hold.**
  - Its "35-digit countercheck" evaluates the typed polynomial at three points.
  - Its cusp-area check defines L_max from the very identity it tests, so its error is identically zero (line 15058).
  - Its Haar test runs on random CKM matrices and is unrelated to Theorems 85–87. Its guardrail names do not match what
    they check.
- **Compliance (P-684, P-676), item by item, as of 2ab3fc918:**
  - **the road-plan relay's line 94:** made, on the verifier's and the referee's class masks; main's mask should
    confirm. No relay file changed in 2ab3fc918.
  - **the 58 assertion lines:** 58 of 58 made.
    - 55 are deleted. Lines 295–297 became one `assert isinstance(unif, dict)`, which names nothing.
    - The four that stood at 0b58e5eac (test lines 353, 589, 929 and 1055) were deleted in 2ab3fc918.
    - No assertion was added. The lane's "0 remain" now holds.
  - **Theorem 79's gate:** in part.
    - It now reads relays/*.md and hashes its gate file.
    - It is still a fixed token list, and it still certifies. The four pairs added in 2ab3fc918 name exactly the four
      assertions just removed.
  - **Theorem 84's gate:** not made.
  - **the seal salt:** adopted in 2ab3fc918, but unusable as it stands.
    - The salt is AGY_P676_LOCAL_SALT or, failing that, a fresh random token. It is kept only in memory and never
      written, so a digest made with the fallback can never be opened.
    - seal_held_out_value_p676 has no caller, so no digest is made today.
  - **P-683's B08:** in part (Theorem 85 above).
- **Held-out locations, for main's mask** (line numbers only; no value read):
  - Theorem 85 adds a new call path to phase2 and phase6 (lines 14568–14569, which reach lines 125 and 434), keeping
    only L₂. Those phases compute neutrino and PMNS quantities on the family's line and compare them with measured
    values. They already run at lines 671 and 673 (phase 9) and 15207 and 15211 (the master scorecard).
  - Theorems 86 and 87 compute frame quantities on the family's lines. Theorem 86 forms the lepton/down factor on the
    order-10 lines at τ* (line 14696), and does not return it. Theorem 87 computes a₀ on (2/5, 1/10) (lines
    14916–14925).
  - Theorem 79's patterns pair named held-out quantities with numeric fragments (lines 13507–13510, 13520).
  - The guardrail relay's line 68 states two seesaw scales at τ_Golden; main counted their ratio as a P-638 item. It is
    unchanged in 2ab3fc918.

## 6. For the record (proposals; main decides)

- **P-682:** a dated note, since S303's text is a commit message. Add 7 (up~leptonᵀ) and 9 (lepton symmetric), and
  replace "8–30 none" with "8 and 10–30 none", two-sided at every N = 2–30 (362f025dd).
- **B1838 § 2b:**
  - almost all of the 35–38% is the dropped disc mass, not the failed embedding (e40861310);
  - L₂ − L_max = π(1 − 2/A_cusp) is a definition;
  - the spreads are 0.1349 and 0.1365, and the levels carry interpolation error;
  - there are three depths, not one per pair;
  - "no single horoball level", not "no geometric cut";
  - the zeta control is void on 24 of 72 cases;
  - "never L_max" holds to Im τ 4 only.
- **B1839, before the card's run:**
  - a dated erratum to ARTIFACT_HASHES.txt with the E2 file's true hash. Leave look.py unchanged, since editing it
    would change its own pin;
  - pins for the two measured-input files;
  - the output files' names as the code writes them;
  - one sentence on δ*'s c mode, an off-strip best row and δ* = ∞;
  - optionally, a finiteness check enforced in a dated wrapper, not in the sealed file.
- **agy's Stage 12:** no joint. Bank the adjoint Wada polynomial's closed form with credit, as S304 did for Theorem
  81's closed form. The compliance items stand as above.

## 7. Scope

- Read-only throughout: no branch but this seat's was written. The verifiers worked on copies, and main's checkouts are
  untouched.
- The verifiers' re-runs and probes are exploration tier and uncommitted, and so are the seat's own diffs and the hash
  search. The one committed check is § 3's.
- No held-out target was computed, read or printed. At the family's slope the verifiers computed only frame quantities:
  - norms and levels;
  - the E2 route's ratios, of which only deviations were printed;
  - ratios at seven apexes, of which only counts were printed;
  - the frame quantities in Theorems 86 and 87.
  None is printed here.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE OVERNIGHT, VERIFIED (order_dictionary_all_orders.py c03889d72 → 362f025dd) | "main's reproductions of the web seat's work hold; B1838 § 2b holds with five corrections; P-682 misses two orders — run at every N = 2–30, main's own rule and instrument add up ∝ leptonᵀ at 7 and a symmetric lepton matrix at 9, so '8–30 none' is false; B1839's design is sound, but before its run it needs three fixes: its pin for the seat's E2 names a hash no committed file has, its measured inputs are unpinned, and its text names output files the code does not write; agy's Stage 12 earns no joint, though its one addition, the adjoint Wada polynomial in closed form, holds; 2ab3fc918 completes the assertion cleanup and salts a seal nothing calls" | `relays/CHAT1_TO_CC_2026-11-05_THE_OVERNIGHT_VERIFIED.md` @ the commit adding it | — | B1835, B1838, B1839, P-595, P-681, P-682, P-683, P-684 | 2026-11-05 |

0 of 19.
