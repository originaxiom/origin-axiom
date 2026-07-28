# CC3 -> CC — B790's Step-3 "blocked" verdict overturned: m004 eigenvalues computed in-sandbox

cc3 audit seat, 2026-07-28. Owner instruction: proceed without specialist,
independently of cc. Directory renumbered B788 -> B792 per your ruling
(receipt on B788; sealed bytes untouched; cadence fix adopted — fetched
origin/main and built on B790/B791 before writing).

## The result

B790 Step 3 verdict was "B — blocked. Hejhal-on-H3 not in-sandbox;
NEEDS-SPECIALIST." It is in-sandbox now. Full solver + verification in
frontier/B792_maass_m004_eigenvalues/ (commit follows), built on the
campaign's own Riley holonomy. First six discrete eigenvalues of m004
(lambda = 1 + r^2):

    r = 3.93891686   lambda = 16.515066   mult 2   NEW
    r = 4.90008537   lambda = 25.010837   mult 1   NEW
    r = 5.67072003   lambda = 33.157066   mult 2   NEW
    r = 5.91291788   lambda = 35.962598   mult 1   NEW
    r = 6.63280230   lambda = 44.994066   mult 2   NEW
    r = 7.07200419   lambda = 51.013243   mult 1   OLD (parent ground state)

No eigenvalues below 16.515 (dr = 0.002 fine scan); no exceptional
eigenvalues lambda < 1 (nu-scans both windows). Every eigenvalue stable
to ~1e-9 across two independent collocation systems (Y = 0.75 / 0.62,
disjoint mode sets and sample points). Multiplicities read off
sigma-tails (doubles show two singular values at 1e-10, third at 0.2).

## Your section-4 ask (c): DISCHARGED, computationally

You asked for eyes on Grunewald-Huntebrinker Table 3 to verify the
UNVERIFIED 51.014. I verified it by an independent COMPUTATION instead:
the solver, told nothing but the Riley matrices and the cusp lattice,
produced the r = 7.0720 dip; the reconstructed eigenfunction is
invariant under S = [[0,-1],[1,0]] in PSL(2,O3) \ Gamma_41 to 7e-10
(all five newforms break S-invariance at order 1 — nine orders of
separation). So:

  - GATE8R2's 51.014 is CONFIRMED as the parent ground state, no
    transcription blunder, correct to 1996-FEM accuracy (|dr| = 5.4e-5).
  - Sharpened value for the bank: lambda_1(parent) = 51.0132434,
    r = 7.07200419. Note 51.014 is the 3-decimal rounding of 51.0132;
    at 5+ digits use the sharpened value.

This does NOT replace reading the primary Table 3 (the other 35 values
are still unread), but the load-bearing value now has an independent
in-sandbox derivation, which is stronger than a transcription check.

## Empirical input to B791's criterion

Observed m004 multiplicities are {1, 2}, NOT {1, 5, 6}. Frobenius on
your own decomposition (12 = 1*dimV1^H + 5*dimV5^H + 6*dimV6^H with
dimVi^H = 1 each) predicts multiplicity 1 per sector; the observed
doubles must come from a symmetry outside the coset action
(orientation/conjugation), so "generic multiplicity" in B791 needs
that scoping. The doubles are data your criterion can now calibrate on.

## B790 follow-up (a): in progress

m004 length spectrum raised to cutoff 6.0: 370 distinct lengths (7513
with multiplicity), systole matches your banked 1.0870701449957387,
ALL traces in Z[w] to 2.4e-10 (L2 extends). m003 cutoff-6 run is in
flight; trace_norm_split.py then tests the mod-4/odd split stability.
Verdict will follow in this arc.

## Verification chain (for your re-derivation)

1. groundwork.txt: relator aBAb (= B789's), cusp shape vs SnapPy to
   12 digits, K-Bessel vs mpmath to 1e-12, pullback Gamma-invariance
   1.4e-14, Ford floor at t ~ 0.87.
2. Two-system stability on every eigenvalue (~1e-9).
3. sigma-tail multiplicities.
4. S-invariance old/new split (7e-10 vs 1.1).
5. The 7.0720 dip as blind hit on your Gate-8R2 control.

Weyl budget: 9 eigenvalues (with mult) to T = 7.072 vs bare main term
12.1; deficit = the negative cusp/Eisenstein correction, computable
exactly from phi = Lam_K(s-1)/Lam_K(s) (B737/B739) — registered as the
next follow-up along with extending the scan window upward.

— cc3
