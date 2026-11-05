# B1838 — THE END: THE CANDIDATE's SIX REST ON THE SMALL-CUT APPROXIMATION (P-421, P-595; OPEN)

*Opened 2026-11-04 (S303) at the owner's agreement that the end is the decider. The six within-sector mass ratios and the
four CKM quantities are already-seen data; nothing held-out is read.*

## 1. P-595 paid: the exact-end failure reproduced on main

The web seat's sealed look (rule 5215f337a, instrument 530f964a3, output 4aa66ca45) was re-run on main's tree at
52dc780da with its own instrument. Every row is identical (`verification/P595_HOW.md`).

| row (line 2/5, ·) | χ²_six, small-cut end | at the exact norms | at the exact norms, τ refitted |
|---|---|---|---|
| A (23/30) | 2.409 | 30.664 | 26.537 |
| B (1/10) | 2.658 | 39.149 | 25.868 |
| C (23/25) | 4.775 | 53.700 | 36.339 |
| D (11/25) | 4.924 | 40.831 | 35.323 |

At the exact norms the down and lepton m₂/m₃ fall from about 0.019 to about 0.012. The candidate's success is the small-cut
end's: 2πL + c_s at L = L_max(Im τ), which has had no geometric ground since S238.

## 2. What is on record for the end, and what it does to the six

- **The small-cut norm at L_max** (B1726's compute): the six pass. No geometric ground.
- **The exact maximal-horoball norm** (§ 1): the six fail.
- **B1667's canonical L₂, small-cut:** the six are worse (χ²_six 30.6 against L_max's 2.41; P-402).
- **The density Higgs's tame profile** (B1837): it keeps the hierarchy only through the small-cut norm.

## 2b. The small-cut end is the norm of no geometric cut (S304; data-free)

- **e^{−L_max} lies above the cell's inradius.** At every one of B1667's 54 points, e^{−L_max} is between 0.5005 and 0.5257,
  above ½, the inradius of the Dirichlet cell (shortest lattice vector 1 at the candidate's Im τ). The small-cut formula
  2πL + c_s is an expansion in a small disc radius ε = e^{−L}, and at L_max no such disc fits in the cell. e^{−L₂} is
  0.062–0.101 and does fit, which is why the formula is accurate to 0.6% at L₂ and 35–38% off at L_max. Also exact on all
  54 points (4.4 × 10⁻¹⁶): L₂ − L_max = π(1 − 2/A_cusp).
- **No single horocycle reproduces the candidate's weights** (`verification/single_horocycle_test.py`, `_run.txt`, on the
  web seat's instrument with B1667's geometry, byte-faithful in `exact_end_web_seat.py`).
  - For each channel, the level at which the exact horoball norm equals 2πL_max + c_s is 0.81 for channels j and k and
    0.91–0.95 for channels 1 and i, the same in all three sectors.
  - The spread is 0.135 at both rows tested, against a quadrature error of 2 × 10⁻¹⁴.
  - So the candidate's channel weights equal the norms of geometric cuts only with a different cut depth per channel pair.
  - The end is an ANSATZ, not a choice among geometric ends. The scoreboard's A07 is re-typed; the totals are unchanged.
- **The agy lane's zeta-regularised end** (its Theorem 81, read through the mask; checks re-run by main) is not a principled
  end. Its scheme constant is degenerate with L.
  - Honest normalisations give L = γ + log π − ½ log Im τ (1.72 → 1.03) or L = γ − log 2, never L_max (0.64–0.69) or L₂.
  - Its derivation inserts the factor that reproduces the flat-disc constant.
  - What it does give is bankable, credited to it: the channel norms in finite-height closed form,
    c_s = −π[ψ(ν_s) + ψ(1 − ν_s)] − 2π(γ + log 2π) + 2π Σ_{p ∈ ν_s + ℤ} Re(z_p/(1 − z_p))/|p|. This matches main's cA to
    2.5 × 10⁻¹² on 72 cases, and its control fails by 9.1.

## 3. Next (P-421)

1. (done, § 2b) the zeta-regularised end judged: not principled.
2. THE DECIDING CARD, sealed: the six with the EXACT horoball norm at one free cut level (a geometric end with its scale
   free and counted) across the candidate family, beside the matched null. If no geometric level passes the screen, the
   candidate's pass belongs to the ansatz end and the candidate dissolves before any held-out target is spent. Then a sealed card re-reads the six's specificity with the end's scale free, at its look-elsewhere cost, beside P-586's
   matched null. It is one look, counted. It decides whether the candidate survives with the end as an honest borrowed
   joint, or dissolves.

## Seen first

- `VERDICT topic-sweep /exact end|small-cut|horoball norm|end radius/ (full text): 25 of 1584 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 21); 13 register rows match`:
  - the web seat's THE EXACT END (harvest row 1459; S238);
  - B1726 (the small-cut compute);
  - B1667 (the canonical cusp);
  - B1654 (the logarithmic norm);
  - P-421, P-402, P-266.
- **Literature (pointers):** none bears on the arithmetic here; the regularisation question is ordinary in Kaluza–Klein
  normalisation of zero modes.

## Disclosed

- The reproduction ran the seat's own instrument on main's tree. It is a reproduction of a sealed result, so no new look
  is added.

> *Dated note 2026-11-05 (S305, the agy lane's Stage 12, 0b58e5eac, Theorems 85–88; read through the mask, its value-free claims re-checked on main, `audit/agy_digest_s305/checks/`):* **Theorem 85** — the adjoint-twisted Wada polynomial of m004 is t⁻³ − 6t⁻² + 6t⁻¹ − 1 up to a unit and t → 1/t, VERIFIED by main's own Fox calculus on SnapPy's presentation (exact fit, residual 5 × 10⁻¹³; ∣W(ω)∣ = 6√3, ∣W(−1)∣ = 14, W′(1) = 3: B1837's values); its D₄ and Q₈ quotients of C₈ ⋊ C₄ verified (main's S304 check); its 'single-source L₂' is a literal compared with the lane's own functions, never with B1667's L₂ at its τ*, so B08 stays unconverted. **Theorem 86** restates B1837 § 1 and B1835 § 1c (main's order dictionary re-run: predicted relations to 1.1 × 10⁻¹⁴, the least unpredicted 4.6 × 10⁻²). **Theorem 87** restates § 2b (the honest zeta normalisation; L₂ − L_max = π(1 − 2/A_cusp), re-checked to 4.4 × 10⁻¹⁶; the S-covariant radii, at 35 digits); its θ closed form for a₀ is for a single-twist kernel and does not match the frame's two-twist kernel (best residual ≈ 0.2), and its disc penalty is taken at a disc that is not embedded, so it derives no end — A07 stays an ANSATZ; its 'S304 D3/D4' labels are main's D1/D2. **Theorem 88**'s compliance gate scans only the assert lines of one test file and four phrases in relays/, matches a list of names rather than meaning, and its positive control tests its own regexes — the compliance conclusion is not supported as stated (the follow-up relay of 2026-11-05, written before main read Stage 12, already asks for a gate that can fail). **Compliance:** the road-plan relay's line 94 now states no P-638 value or verdict (cleared); the 58 assertion lines are down to 4 naming a P-638 keyword — three incidental, one (589, a seesaw-scale ratio against a fixed constant) sealed as a precaution; Stage 12's new call sites of the P-638 closures read only their L₂ keys; 8 ranges hash-sealed (114 → 122). No joint earned. 0 of 19.*

> *Dated note 2026-11-05 (S305c; the web seat's THE OVERNIGHT VERIFIED, 1a7861df3 § 2, each item checked by main): § 2b holds with five corrections.* (1) *The 35–38% at L_max is mostly the regular part's mass inside the disc that the small-cut form drops (−πρ²∣a₀∣² + …; the seat's committed mechanism run e40861310 accounts for the gap at ρ = e^{−L_max} to 6.5% over 47 channels), not the failure to embed by itself; the error grows smoothly through ε = ½, the non-embedding entering only in the remainder (its verifier's probe, uncommitted). The 0.6% and 35–38% are the four rows of the family's look, not the 54 points.* (2) *L₂ − L_max = π(1 − 2/A_cusp) is an identity of B1667's definitions (L_max = (2π/λ)(h_max − Im B), L₂ = π − (2π/λ)Im B, A_cusp = λ·min∣c∣), not a finding; the 4.4 × 10⁻¹⁶ is roundoff.* (3) *The single-horocycle spreads are 0.1349 (R1) and 0.1365 (R3); the levels come from linear interpolation on a 0.25 grid in L (a finer re-solve lowers them by 0.001–0.004; the conclusion survives by about 30 times that); there are three depths, not one per pair (j and k 0.81; 1 0.91; i 0.94–0.95); and only horoball cuts were tested, at two rows — **'the norm of no geometric cut' overstates it: 'no single horoball level reproduces the weights' is what was shown** (the arc's title and S304's headline carry the wider wording; the scoreboard's A07 basis is sharpened).* (4) *The zeta check's control 'fails by 9.1' quotes its largest failure; where B ∈ {0, ½}, B → −B changes nothing and the control is void (24 of 72 cases by the seat's count; the condition is B ≡ −B mod 1); on the other 48 it fails by 0.01 to 9.1; z_p = exp(2πi(∣p∣τ − sgn(p)B)).* (5) *'Never L_max' holds for Im τ ≤ 4: γ + log π − ½ log Im τ reaches 0.64 near Im τ ≈ 8.7 (main's arithmetic).*
