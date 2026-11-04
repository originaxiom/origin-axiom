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
