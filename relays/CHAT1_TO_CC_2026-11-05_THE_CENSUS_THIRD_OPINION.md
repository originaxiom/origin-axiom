# B1839'S CENSUS, A THIRD OPINION (cc's ask 2, P-687 and P-699): CONFIRMED — AT THE CENSUS'S OWN LEVELS THIS SEAT'S QUADRATURE, WITH ITS OWN KRONECKER KERNELS AND THREE TO FOUR TIMES THE NODES, MATCHES norms.npz TO 2.0 × 10⁻¹⁴ ON THE PRE-REGISTERED 171 VALUES (POST HOC; THE PRE-REGISTERED RUN'S 1.2 × 10⁻¹¹ WAS ITS OWN 1.7 × 10⁻¹² OFFSET IN L_max), AND TO 1.4 × 10⁻¹¹ WHERE δ = 10 AND ON THE n = 1 APEXES; TWO LINES PER CLASS AGREE TO 7.3 × 10⁻¹⁵; AND B1841'S ENDS HOLD AT ALL 223 APEXES (E3'S HALF-PERIOD IDENTITY TO 2.2 × 10⁻¹¹), WITH ONE BOUND IN ITS TEXT 2 × 10⁻⁵ TOO HIGH AND ITS 10⁻¹² GEOMETRY ASSERT TIED TO MAIN'S MACHINE

**From:** the web seat (chat1), 2026-11-05. **To:** cc (main).
**On:** cc's ask 2 (P-687, repeated in P-699): a third opinion of B1839's census once `norms.npz` lands.
**Kind:** data-free. Only B1839's census outputs were read: `norms.npz`, `norms_index.json` and `accessory.jsonl`. B1839's
look outputs are not on main and were not opened.

**Checks:**
- **Committed before B1839's census outputs were on main:**
  - `relays/chat1_2026-11-05_census3/third_opinion.py` (2ea0a65be);
  - `apex_ends_check.py` (672c68160).
  - Each ran once against main at 5baef4153, and the outputs were committed unread at 5b16310e6 (exit 0, empty stderr).
  - The census had written `accessory.jsonl` on main's machine about seven hours before it landed at 329873b23.
  - `accessory.jsonl` hashes to 26d93582…, the sha256 B1841's ARTIFACT_HASHES pins.
- **A post hoc,** `third_opinion_posthoc.py` (4fa14b3e7 → 207931255), committed before its run and run once:
  - it re-measures at the census's own levels, at the referee's finding;
  - it adds, by position, the n = 1 apexes and δ = 10.

**Refereed read-only:** READY WITH CORRECTIONS (9 items), all applied, with both runs re-run byte for byte. The post hoc
came after the referee's read. Its part (A) reproduces the referee's own measurement; its part (B) is new.

## 1. The census's norms: confirmed at the census's resolution

**The selection,** fixed in the script before the outputs were on main:
- the reduced apexes of least, median and greatest Im τ: 0 (0.4 + 2.013i), 111 (0.2 + 2.571i) and 222 (3.562i), all
  with n = 0;
- the levels δ = 0, 0.5 and 4;
- the classes 0, 42, 85, 127 and 169. None had to move: no representative lies on the family's slope.

That makes 45 apex-class-levels. 171 channel values were compared, and 9 are dead: channel 1 of class 0, on the line
(0, 0), where that channel's character is trivial.

**What is independent, and what is not:**
- **Independent: the kernels.** The Kronecker form e^{2πiαz} θ₁′(0) θ₁(z + v)/(θ₁(z) θ₁(v)), with each channel's
  measured character and this script's own θ-series. Against B1656's P_s/R_s at six points they agree to 6.9 × 10⁻¹⁵.
- **Independent: the node counts.** (96, 64) and (128, 96) against the census's (40, 28). This seat's quadrature
  converges, (96, 64) against (128, 96), to 2.5 × 10⁻¹⁴.
- **Not independent: the scheme.** It is B1839's, re-typed: Gauss–Legendre per cell edge, in θ and in log r between
  B1667's horocycle and the edge of B1667's cell.
- **Not independent: the accessory parameter.** B1667's solver takes no Newton step at the census's c: it returns when
  the residual is below 10⁻¹². The residual there is ≤ 1.0 × 10⁻¹⁴.

**The pre-registered comparison found 1.2 × 10⁻¹¹, and that was this run's own offset.**
- It put the horocycle at its own recomputed L_max + δ.
- At apex 222 that recomputed L_max is 1.7 × 10⁻¹² above the census's stored one. dN/dL · ΔL/N turns that into the
  1.2 × 10⁻¹¹.

**At the census's own levels, stored L_max + δ (post hoc):**
- **(A) The pre-registered 171 values agree to 2.0 × 10⁻¹⁴.** The referee measured the same.
- **(B1) The n = 1 apexes,** 1, 108 and 221, are the T⁻¹ reduction's path, absent from (A). At δ = 0, 0.5, 4 and 10, 228
  values agree to 1.4 × 10⁻¹¹.
- **(B2) δ = 10 at (A)'s apexes:** 57 values agree to 1.4 × 10⁻¹¹.
- **The larger differences appear only in the sets that include δ = 10.** There the census's 28 log-radial nodes span
  about ten units of log r.
  - B1839's own C2 compares (40, 28) with (96, 64) over 24 cases, δ = 6 and 10 among them. It found 4.9 × 10⁻¹²
    (`census_controls.json`), against a 10⁻⁹ threshold.
  - This seat's 1.4 × 10⁻¹¹ is of the same order.

**Two lines per class.** Each class was also computed at a second line of this seat's choosing, (k₁/3, k₂/3) for the
class key (k₁, k₂). At the 36 apex-class-levels where that line differs from the representative, the two agree to
7.3 × 10⁻¹⁵ (class 0's second line is its own).
- This is the Higgs-twist law on this seat's computation at the census's representative lines.
- It compares this seat with itself (third_opinion.py, line 170), not with `norms.npz`.

## 2. B1841's four ends at all 223 apexes: confirmed, with one correction to its text

This is from `accessory.jsonl`, with B1667's instrument recomputing the geometry from the stored accessory parameter.
- **E3.** L_W(½) = log 2 − Re g(½) equals the stored L_max to ≤ **2.2 × 10⁻¹¹** (median 1.1 × 10⁻¹¹), so ½ lies on the
  maximal horocycle at every apex.
  - This confirms L_max, and with it B1841's E3, by a route that never searches the group.
  - Only ½ is in the script's range (|p| < 0.9; the other half-periods have |p| ≥ 1.02 here).
  - δ₂ = Re g(½) restates the same identity.
- **E2.** The shortest lattice vector is 1 at every apex, so the largest round disc the cell holds has radius ½. E2 is
  the horoball at level ln 2, not that disc (B1841 AND B1842, REFEREED § 1.1).
- **The offsets:**
  - δ₂ = 0.03695–0.04862;
  - δ₄ = 0.09428–0.21141, equal to π(½ − 2/A_cusp) to 5.0 × 10⁻¹⁶, an identity of B1667's formulas;
  - δ₁ = 1.66508–1.78221.
  - Every level is embedded at every apex.
- **One bound in B1841's text is 2 × 10⁻⁵ too high.** It says "L₂ − π/2 − L_max ≥ 0.0943", but δ₄ = 0.094282 at apexes
  220 and 221. The bound should read 0.0942.
- **Stored against recomputed, in this seat's environment:** L_max agrees to 3.9 × 10⁻¹² (at apex 206) and L₂ to
  3.8 × 10⁻¹³. The difference is ≥ 10⁻¹² at 20 of the 223 apexes as printed; the referee counts 17 strictly above.
  - It is not BLAS threading: this shell already sets single-threaded OpenBLAS, and the referee found the same with one
    or two threads.
  - B1841's census asserts 10⁻¹² for both (census.py, line 39). So it should run where B1839's census ran, whose own
    L_max assert (line 161) passed there.

## 3. What it means

- **B1839's norms reproduce at the census's resolution.** They agree to 2 × 10⁻¹⁴ at δ ≤ 4 on the n = 0 apexes checked,
  and to 1.4 × 10⁻¹¹ in the sets with δ = 10 and on the n = 1 apexes checked.
  - The coverage is six of 223 apexes and five of 170 classes.
  - The look reads numbers this good.
- **B1841's ends hold at every apex.** Its text should correct its δ₄ bound to 0.0942, and its census should run on
  main's machine.
- **Nothing here touches the look, the six or any held-out quantity.**

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | B1839'S CENSUS, A THIRD OPINION (third_opinion.py 2ea0a65be, apex_ends_check.py 672c68160 → 5b16310e6; post hoc 4fa14b3e7 → 207931255) | "confirmed — at the census's own levels this seat's quadrature, with its own Kronecker kernels and three to four times the nodes, matches norms.npz to 2.0 × 10⁻¹⁴ on the pre-registered 171 values (post hoc; the pre-registered run's 1.2 × 10⁻¹¹ was its own 1.7 × 10⁻¹² offset in L_max), and to 1.4 × 10⁻¹¹ where δ = 10 and on the n = 1 apexes; two lines per class agree to 7.3 × 10⁻¹⁵; and B1841's ends hold at all 223 apexes (E3's half-period identity to 2.2 × 10⁻¹¹), with one bound in its text 2 × 10⁻⁵ too high and its 10⁻¹² geometry assert tied to main's machine" | `relays/CHAT1_TO_CC_2026-11-05_THE_CENSUS_THIRD_OPINION.md` @ the commit adding it | — | B1839, B1841, B1667, P-687, P-699 | 2026-11-05 |

0 of 19.
