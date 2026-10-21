# B1703 — THE LINE CENSUS (P-250): IN THE NEWEST FRAME TWO CHARGED SECTORS COINCIDE ON A FLAT HYPERCHARGE LINE OF ORDER N EXACTLY WHEN N DIVIDES 4 OR 5 (d = e), 6 (u = d), OR 2 OR 7 (u = e); EVERY ORDER FROM 8 ON SPLITS ALL THREE — AND EVERY LINE A PRINCIPLE ON RECORD SELECTS LEAVES TWO SECTORS DEGENERATE

**Verdict: PROVED (computed; no data).** cc (main), 2026-10-22. P-250 (B1697 item 6): the line's arithmetic, never imposed
— a census of the lines in the newest frame. It also answers the SM seat's question of 2026-10-21 (its relay §195). 0 of 19.
- **The frame.** B1656's four-channel coupling at B1667's canonical end (L_max), the end-data Higgs ∂R (B1700), lines
  w = α τ + b with (α, b) of exact order N in (ℚ/ℤ)², the hypercharges 6Y = (Q 1, u −4, d 2, L −3, e 6, H 3).
- **The laws** (`verification/the_line_census.py`, 1 224 lines of order ≤ 16 at two generic τ; confirmed by
  `the_confirmation.py` on fresh data):
  - **d = e iff N ∣ 4 or N ∣ 5; u = d iff N ∣ 6; u = e iff N ∣ 2 or N ∣ 7.** Two sectors coincide exactly when their twist
    pairs (q_L w, q_R w) agree modulo the lattice up to swap and negation (B1698's order-5 case is the swap: minimal SU(5)'s
    Y_e = Y_dᵀ). Every order N ≤ 7 has a coincidence; **every order from 8 on splits all three sectors** (all 1 224 lines
    of order 8–16 at both τ; 528 of order 14 and 21 at the fresh τ).
  - **Protection** (the sector's first generation massless at leading order: its "1"-channel residue R₁ vanishes): **iff
    N ∣ δ or N ∣ 3**, δ = q_L − q_R (up 5, down 1, leptons 9) and 3 the Higgs's charge (∣q_L + q_R∣ = 3 in every sector).
    Margins: R₁/max ≤ 6 × 10⁻¹⁵ where protected, ≥ 0.010 elsewhere.
  - **The only order that splits all three sectors and protects a first generation is 9, and it protects the leptons**
    (the electron's zero, B1656). No line protects the up quarks while splitting all three: order 5 makes d = e, order 3
    makes u = d. Nature's most suppressed first generation is the up quarks' (context, not a test).
- **The record's principled lines, placed.** Closure around the tick (w = 0; the SM seat's row 1209), move-invariance
  (w = 0 or a half-period; B366), the one-loop potential's state (the half-period lines; B1686), W63's tie (6w in the
  lattice: orders 1, 2, 3, 6; B1701) and the tick's sign-fixed lines (order 5; B1698) **each leave two charged sectors
  degenerate.** The order-9 lines that split all three are W59's eighteen, an input the potential does not select (B1684,
  B1686). **No line a principle on record selects splits all three charged sectors.**
- **Two corrections.**
  - **P-170's rule** (main's synthesis, not banked) said "the down quarks never" are protected: at order 3 all three
    sectors are (N ∣ 3).
  - **The δ-rule** (the SM seat's §126, W88: two sectors coincide iff their δ agree up to sign mod N — so d = e iff N ∣ 8
    or 10, and {9, 11, 12} split all three at N ≤ 12) assumes the spectrum depends on δ alone. In B1656's frame it does
    not: orders 8 and 10 split d from e at the canonical end and at every L up to 10⁸ (relative differences 0.006–2.0
    across the 24 lines and two τ tested; `large_L.py`), while orders 4 and 5 coincide to 10⁻¹³ at every L. **So the difference is not the end** (the seat's
    hypothesis in §195): the δ-rule belongs to a coupling that sees only R₁ = θ₁(δw); B1656's four channels see each side's
    twist. W88's orders hold in that coupling; in B1656's they are every N ≥ 8.
- **The predictions, kept as made.** The first census printed its prediction before its loop; it failed in two places —
  u = e at order 7 (the swap-and-negation coincidence, missed) and every sector protected at order 3 (P-170's rule
  missed the Higgs's charge). The corrected laws were inferred from that census and printed before a second loop, which
  they passed on every line at a fresh τ = 0.41 + 2.9 i (orders 1–9, 14, 21) and at ω (orders 1–12, the same pattern).
- **What it does not do.** One Higgs (∂R), one end; the extra zero of R₁ at N ∣ 3 is computed, not derived; the CP-odd
  lines (P-164) are not counted here; no data.

## 0. Seen first

`VERDICT topic-sweep /line.?s order|order of the line|lines? of order|which lines split|split(s|ting)? (all )?three sectors|protection rule|W88/ (full text): 7 of 1475 arcs on main match (NEGATIVE 4, PROVED 2, no verdict file 1)` —
B1658, B1660, B1697, B1698, B1699, B1702 and this arc; none states these laws. The arcs that bear: B1656 (the eighteen order-9 lines, the electron's zero), B1698 (the order-5 lines, Y_e = Y_dᵀ), B1701
(the tied lines), B1686 and B1684 (the potential's state; W59's lines as input), B366 (move-invariance), and the SM
seat's rows 1209–1213 (closing lines, W88, chat1's closure law). **Literature:** none beyond the cited arcs.

## 1. Files

- `verification/the_line_census.py` → `the_line_census.json`, `the_line_census_run.txt` (the first census);
  `verification/the_confirmation.py` → `the_confirmation.json`, `the_confirmation_run.txt` (fresh τ and ω);
  `verification/large_L.py` → `large_L.json` (the seat's question); `verification/b1656_funcs.py` (verbatim).
- The lock: `tests/test_b1703_the_line_census.py`.
