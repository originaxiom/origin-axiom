# L98 — THE ONE-ORGAN-OR-TWO STRUCTURAL FALSIFIER (sealed prereg)
# B666 cell W3-4, 2026-07-17.  Sealed BEFORE any target-grid point is
# computed; sha-256 of this file + l98_falsifier.py + l98_lib.py in
# SEALS.txt.  Design calibration (l98_design_calibration.py) ran ONLY on
# control points strictly outside the target window — the N3 precedent.

## The question (banked record)

N3 (B646, prereg 09246f08) left one-organ-or-two UNRESOLVED: on the
plateau kappa in [0.8, 1.5] the box_dim(kappa) statistic (golden word
m=1, periodic diagonalization) shows candidate peaks at 1.10 and 1.45
with margins ~1.27 sigma against a placement-jitter floor sigma_pool =
0.014337 (2-sigma bar preregistered; depth-15 gaps SHRANK).  N3's banked
recommendation: a structurally different statistic, not more depth.
This prereg registers that statistic.

## The structural move (why this is not depth-pushing)

Two facts, both in the banked record:
1. R3's mechanism-candidate says the plateau's organ is GAP-DOMINATED
   fragmentation: the exact functional g(kappa) = mst_max_edge/diam
   (banked B163 machinery) peaks at kappa = 1.2 and is UNIMODAL on the
   banked coarse grid (r3_results.json scan_mst_gap_F1597: 0.0413,
   0.0526, 0.0576, 0.0625, 0.0630*, 0.0566, 0.0503, 0.0330 on
   0.8..1.5), while the banked box_dim curve is bimodal-looking with
   its VALLEY (1.2–1.3) at g's argmax — compatible with ONE organ seen
   in negative (a single gap-notch carving two apparent flanks).
2. g and the MST gap labels are DETERMINISTIC exact functionals of the
   spectrum: no box grid, no placement, no RNG.  The N3 failure channel
   (jitter comparable to the candidate gaps) is structurally absent.
   Calibration measured: label depth-scatter < 2e-5 across depths
   12..15; labels and g invariant under 1e-10 eigenvalue perturbation
   (5 seeds); the dominant-gap label at both controls is exactly the
   Fibonacci gap-labeling value n_small/L = F_{n-2}/F_n -> 1/phi^2
   (144/377, 233/610, 377/987, 610/1597).

The remaining systematic channel is finite-size (depth) flapping; the
criterion below replaces N3's sigma bar with an exact three-depth
consistency requirement.  Every comparison in the verdict is exact
arithmetic on deterministic numbers.

## The registered statistic

Target grid (identical to N3): kappa in {0.80, 0.85, ..., 1.55} (16
points, step 0.05), golden word m=1, lambda = i*mu, mu = sqrt(2-kappa),
periodic spectra at depths d in {13, 14, 15} (L = 610, 987, 1597).

For each (kappa, d):
- g_d(kappa) = mst_max_edge / diam  (exact, deterministic);
- l1_d(kappa) = n_small/L from cutting the largest MST edge (the
  dominant-gap label), plus the degeneracy ratio e2/e1 and the top-5
  (length, label) list, recorded.

**Peak region (N3's verbatim rule, applied to g_d):** index i is
flagged iff v_i >= both existing neighbors with strict > on at least
one side; contiguous flagged runs merge into one PEAK REGION,
represented by its highest point (ties toward lower kappa).

**Depth-consistent organ:** a triple of peak regions (one per depth
13/14/15) whose representative indices agree pairwise within 1.
Triples are formed greedily by minimal pairwise representative
distance, each region used at most once; ties toward lower kappa.

**N2 := (number of depth-consistent organs) − 1.**

## THE DECISION CRITERION (verbatim; mechanical)

> **ONE-ORGAN** iff N2 = 0 (exactly one depth-consistent organ; any
> additional peak region at any depth fails depth-consistency).
> **TWO-ORGANS** iff N2 >= 1 AND some two depth-consistent organs have
> depth-14 representatives with index-gap >= 2 (N3's separation rule).
> **UNRESOLVED** iff neither: no depth-consistent organ at all, or
> extra consistent organs only at index-gap 1 (unseparated).

Under the one-organ hypothesis N2 = 0 EXACTLY (an integer identity,
not a sub-sigma comparison); under the two-organ hypothesis in its
banked mechanistic form (two gap-fragmentation structures) N2 >= 1,
provably nonzero once computed — the parity-style separation the lead
asked for.

**The mechanism tag (read only if TWO-ORGANS):** the labels
l1_14(peak A) vs l1_14(peak B): equal within 0.01 => two organs of ONE
gap regime (shape-level split); differing by > 0.01 => TWO GAP REGIMES
(the strong form; calibrated label resolution 2e-5, adjacent
phi-hierarchy labels differ by >= 0.09, separation/noise > 4000).
Degeneracy guard: if e2/e1 > 0.999 at a peak AND the rank-2 label
differs from rank-1 by > 0.01, the tag is AMBIGUOUS (calibration:
near-degenerate top pairs are mirror pairs with EQUAL labels, so this
should not trigger; declared anyway).

**Falsification scope (declared):** a ONE-ORGAN verdict falsifies the
two-organ hypothesis in its gap-mechanistic form (distinct fragmenting
structures visible to the exact gap functional).  A conceivable
two-organ structure invisible to g and to the gap labels (same gaps,
different higher-order geometry) is NOT excluded by this test; it is
excluded by nothing currently banked, and box_dim cannot see it either
(N3's floor).  This asymmetry is accepted at sealing.

**No depth-16 escape hatch:** if UNRESOLVED fires, the verdict banks as
UNRESOLVED; deeper words are out of scope (the lead's own directive).

## Runner

l98_falsifier.py --unblind runs the 16x3 grid and prints the verdict
mechanically (~10–15 min).  l98_falsifier.py --selftest runs the
decision function on synthetic unimodal/bimodal/flapping triples
(MB12: the criterion can pass AND can fail) without touching the
target window.  This cell runs ONLY --selftest; the unblinding is the
next data pass, per the campaign's sealed cell-14 scope.

## Out of scope

The a_C discriminator and the (t/V)^2 salvage (L98's other registered
items) are untouched here.  box_dim appears nowhere in the decision.
