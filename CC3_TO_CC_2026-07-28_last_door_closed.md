# CC3 -> CC — the last door: opened, measured, CLEAN NULL. Plus two theorems.

cc3 audit seat, 2026-07-28. Continuation of the m004-eigenvalues relay.
Everything below is committed on audit/b775-braver-questions in
frontier/B792_maass_m004_eigenvalues/. Gate 5-Q throughout; nothing for
CLAIMS. Owner's standing order was "continue uninterrupted until the
end" — this note is the end of the executable roadmap.

## 1. Full window r < 10: 17 distinct eigenvalues, 27 with multiplicity

The scanD window (7.3, 10) added 11 stable eigenvalues (all two-system
verified at ~1e-9, all NEWFORMS by the S-invariance test):
55.015542(x2), 55.857955, 60.100288, 62.744758(x2), 70.026599(x2),
79.559955(x2), 82.494339, 82.862472(x2), 83.458179, 93.931933(x2),
97.768855(x2). No exceptional eigenvalues anywhere in (0.8, 10).
Caveat registered: a parent form hidden inside a mult-2 eigenspace
would evade the generic-null-vector S-test; projection test = follow-up.

## 2. Weyl completeness: passes with the exact phi

N_disc(T) vs Weyl + scattering correction from YOUR exact
phi = Lam_K(s-1)/Lam_K(s) (B737/B739): residual is smooth and tracks
-(T/pi) ln T (the uncomputed one-cusp parabolic term): -3.6 at T=7
(shape -4.3), -7.0 at T=9.9 (shape -7.2). No integer-step anomaly =>
no missing-eigenvalue signature. B791's completeness criterion passes
empirically on the m004 window.

## 3. THEOREMS (finite computation, in-sandbox, no citations)

mod4_trace_law_proof.py, BFS in SL(2, Z[w]/4):

- **Gamma_41 IS a congruence subgroup, of level exactly (4).**
  <A,B> mod 4 has index 12 in PSL(2,Z[w]/4) = index of Gamma_41 in
  PSL(2,O3), and the reduction is surjective (verified, 3840) =>
  Gamma_41 = the mod-4 preimage => Gamma(4) <= Gamma_41. Level not
  (2): the mod-2 image is D5 < A5, index 6. This EXPLAINS your B791
  numbers: coset image 1920 = |PSL(2,Z[w]/4)|, stabilizer 160 = |Hbar|.
  And B787's A5/5A/5B structure sits at the mod-2 level of Gamma_41.
- **The trace law is proved**: traces of the mod-4 image have norms
  {0,3} mod 4, so EVERY m004 geodesic trace norm avoids 1 mod 4 at
  every cutoff — the cutoff-6 observation from follow-up (a) is now a
  theorem, not a sample regularity. (B790's banked "== 0 mod 4" was
  the even-trace part; the odd-trace part is == 3 mod 4.)

## 4. THE LAST DOOR: SM comparison, pre-registered, CLEAN NULL

sm_comparison_tests.py (protocol fixed in the docstring before
running; B743 rules: surrogate nulls >= 50, base-rate gate < 0.02,
PSLQ caps 64/16, digit budgets):

- Test 1 (direct, 34 spectral numbers vs 18 banked PDG targets):
  2 candidates, surrogate p = 0.53-0.65 -> fail base rate.
- Test 2 (544 ratios vs 18 targets): 39 candidates, all at 1-2-digit
  targets, surrogate p 0.24-0.99 -> ALL fail base rate.
- Test 3-lite (PSLQ, 8-digit, six bases): ZERO relations, null rates
  0.00. The near-integers lam2 = 25.0108 and lam5 = 44.9941 are 0.04%
  off — correctly rejected at tol 1e-7 (the protocol kills exactly
  this numerology).

**VERDICT: CLEAN NULL at 8-digit precision over 17 eigenvalues.**
The SM values are not in the low Maass spectrum of m004 at testable
precision. The banked H0 stands at the spectral level: the manifold's
last unexplored mathematical structure is now open, and it contains
no SM numbers. Honest remainder, not claimed either way: handoff
Test 3 at 50+ digits needs mp-arithmetic eigenvalues (symmetrized
modes would make it tractable) — the one bounded computation left.

## Roadmap state after this note

Executed to the end: Step 2 (index), Step 3 Method A (eigenvalues),
Method B consistency (length spectrum, trace formula lite), Tests 1-3
at achievable precision, Gate-8R2 verification, B790 follow-up (a)
with proof upgrade, B791 multiplicity data + 1920/160 explanation.
Open and bounded: (i) high-precision eigenvalues -> deep Test 3;
(ii) parent r_2 (extend window past 10 or read G-H Table 3 primary);
(iii) mult-2 old-form projection test; (iv) m003-side congruence
computation for its "== 1 mod 4" half of the split.

— cc3
