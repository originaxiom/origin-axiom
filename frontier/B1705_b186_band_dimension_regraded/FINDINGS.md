# B1705 — B186'S BAND DIMENSION RE-GRADED (Review 67, R66-4): THE BAND'S SPECTRUM IS REAL AND WAS BOX-COUNTED IN TWO DIMENSIONS ON NOISE; COUNTED ON THE LINE IT IS BLAS-INDEPENDENT, AND B186'S ORDERING STANDS BY 0.11–0.12

**Verdict: PROVED (a targeted correction that sharpens; no data).** cc (main), 2026-10-22, at Review 67 (R66-4, carried
from R65-9 and R64-10). 0 of 19.
- **The defect.** B186's C2 compares the box-counting dimension of the off-axis spectrum (λ = 2i) with the κ = 2 band's
  (λ = 0). At λ = 0 the operator is Hermitian, so its spectrum is real; the lock computed it with the general solver and
  counted boxes in two dimensions after rescaling each coordinate to unit range — the imaginary parts, ≈ 10⁻¹⁵, were
  scaled up to fill the square. The band's value therefore counted noise, and it moved with the BLAS thread count
  (golden 0.903 / 0.928, silver 0.847 / 0.792 at default / single-threaded), which is why the lock failed every
  single-threaded suite since Review 64.
- **The re-grade** (`verification/regrade.py`, each setting in its own process): counted on the line, the band's
  dimension is **0.9385 (golden, depth 12) and 0.8830 (silver, depth 6) at both settings, to 10⁻¹²** (the same from the
  real parts and from eigvalsh), against the off-axis **0.8272 and 0.7646**, which never depended on the setting. **The
  ordering stands by 0.11–0.12** (> the lock's 0.04).
- **Done.** B186's lock counts the band on the line (`tests/test_b186_hyperbolicity_certification.py`, with a dated
  comment); B186's FINDINGS carries a dated note: its printed band values (1.10, 0.85) measured partly noise; its claim
  (off-axis below band) stands. Not a retraction.

## 0. Seen first

`VERDICT topic-sweep /box.?count|box dimension|band.?s (box )?dimension|hyperbolicity certification|BLAS/ (full text): 6 of 1477 arcs on main match (OPEN 1, PROVED 5)` —
B186 itself, and the arcs that cite its box count; the defect was diagnosed at Review 64 (§5b: "ill-conditioned"; R64-10) and
carried; this arc finds its cause. **Literature:** none.

## 1. Files

- `verification/regrade.py` → `regrade.json`, `regrade_run.txt`.
- The lock: `tests/test_b1705_b186_band_dimension_regraded.py`; B186's own lock repaired.
