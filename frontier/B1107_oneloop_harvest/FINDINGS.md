# B1107 — the one-loop Ruelle identity HARVESTED: the whole chain reproduces from a fresh spectrum, to fifteen significant figures

**Status: banked (frontier). Verdict PROVED (two-bench: the audit seat's chain
B8100→B8104→B8112 with B8113's three residues as scope, re-derived here from
scratch). Harvest arc (integrate-don't-merge). Gate 5 untouched. Lock
`tests/test_b1107_b1108_harvest.py` (fast JSON core; OA_SLOW full re-run).**
Run: `python3 frontier/B1107_oneloop_harvest/b1107_verify.py` (~2 min; fresh
SnapPy spectrum + mpmath cross-check).

## THE IDENTITY (the audit seat's B8112, now two-bench)

For the one-dimensional SO(2) characters σ_k, the Ruelle product at s = k is
exactly the Giombi–Maloney–Yin factor: **R(k, σ_k) = ∏_{[γ] prime} (1 − q_γ^k)**,
q_γ = e^{−ℓ_γ + iθ_γ} — so the AdS₃ boundary-graviton one-loop product
**Z_geod = ∏_{n≥2} |R(n, σ_n)|^{−2} is an infinite tower of one-dimensional
Ruelle zetas**, and no single finite Pfaff torsion ρ(m) can equal it; Pfaff
Thm 1.2 supplies the TAIL via the torsion-ratio limit. The unwind is a clean
substitution (abelian M ⟹ 1×1 determinants) — verified here NOT by restating it:
σ_k was built by diagonalizing actual rotation matrices and powering the extracted
eigenvalue (500 random trials, max error 1.19×10⁻¹⁵; on m004's real data
2.22×10⁻¹⁶), and every definition was quote-checked against the LIVE Pfaff paper
(arXiv:1206.0228) — no misquotes anywhere in the chain.

## The numbers, from scratch (this bench's own spectrum fetch, cutoff 5.5)

- **log Z_geod = −0.27297717083840395** vs banked −0.2729771708384004 —
  agreement **3.6×10⁻¹⁵ (~15 significant figures)**.
- The two summation orders agree to **8.166×10⁻¹⁴** (theirs: 8.2×10⁻¹⁴) — and an
  mpmath 50-digit cross-check (a method NOT in their arc) shows the orders agree
  to 1.16×10⁻⁴⁰, **proving the float-64 gap is pure roundoff**, not a hidden bug.
- The cutoff-instability table reproduces (<5×10⁻⁷, print-rounding); the
  n = 2-vs-tail instability ratio: **201.8×** (theirs ~202×) — the abscissa
  residue (B8113 residue 3) is real on this bench too.
- B8113's S(2)/S(3) increments reproduce exactly at their cutoffs and were
  **extended two steps**: at 5.0→5.5 the S(2) step drops to +0.0447 (below the
  previous +0.0504) — nothing banked is contradicted (B8113 claims nothing beyond
  its cutoffs), but the next extension must account for this datum.

## The three residues (B8113, carried verbatim as this harvest's scope)

(1) the cusp continuous spectrum outside the assembly; (2) the
torsion-to-determinant identification NOT claimed; (3) the n = 2 factor outside
Pfaff's absolute-convergence abscissa. THE ROAD VI.2/VI.3 carry all three.

## One defect found by this verification (documentation, non-blocking; relayed)

**B8100's FINDINGS/verdict prose states "cutoff 5.5 (134 classes, 1221 geodesics)"
— those are the cutoff-5.0 counts.** The true 5.5 spectrum is **214 classes, 2819
geodesics** (reproduced on three fresh fetches, cross-checked against the `4_1`
name). The COMPUTATION used the right spectrum (log Z reproduces to 15 digits);
only the descriptive count is stale. One-line fix relayed to the owning band.
