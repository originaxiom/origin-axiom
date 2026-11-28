# CLAIM CARD — P-632: on B1813's s-family the Farey operator's fastest-growing mode picks no interior locus: it is constant at s = 0 (λ₁ = 2) and, at s = 0.1, 0.2, …, 0.9, positive and strictly decreasing on [0, 1], so largest at the parabolic point; λ₁ falls strictly over s = 0, 0.1, …, 0.9, 0.95, to 1.0203 at s = 0.95 (the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 0a89dddd2fa84dda59eb6c77ebd3b114f78050db
- kind: negative
- touches: P-632, P-713, P-441, P-468, P-629
- effect: conditions — P-632: on B1813's s-family, the fastest-growing mode picks no locus on [0, 1] at s = 0,
  0.1, ..., 0.9, 0.95; P-713, P-441 and P-468 keep their negatives; the route through a dynamics for τ is not
  taken (P-629)
- scope: frame: B1813's s-family, through the L↔R-symmetric part F_s of its word-by-word operator; object: the leading
  eigenvalue λ₁(s) and eigenfunction h_s of F_s on [0, 1]; reach: class; hypotheses: s = 0, 0.1, ..., 0.9 and 0.95;
  collocation at N = 64, 128 and 256 Chebyshev nodes; h_s read on a grid of 2001 points; the next eigenvalues read at
  N = 128 and printed to 4 decimals. The decisive verdict also asks that those print below 1; they belong to the
  discretisation (the largest is 0.9998 or 0.9999 at N = 128 and approaches 1 as N grows, the edge of the continuous
  spectrum [0, 1]), so their staying below 1 is not a spectral gap and is not claimed as one
- identifications: F_s is the L↔R-symmetric part of B1813's word-by-word operator L_s (the old card's reading,
  carried by p632_modes.py's docstring)
- definitions: (F_s f)(x) = (1 + x)^(−2s) [f(x/(1 + x)) + f(1/(1 + x))] for f on [0, 1]; λ₁(s) is its leading
  eigenvalue and h_s its eigenfunction; "picks no interior locus" means h_s has no interior extremum: it is constant
  or strictly monotone on [0, 1]; x = 0 is the parabolic point, the cusp. Z_n(s) is the sum, over the 2ⁿ − 2 words of
  n letters L = [[1, 1], [0, 1]] and R = [[1, 0], [1, 1]] that hold both letters, of λ_w^(−2s), λ_w the larger
  eigenvalue of the word's product; Z₁₈/Z₁₇ approximates λ₁(s). h_s's mass on [0, 0.05] is ∫₀^0.05 h_s / ∫₀¹ h_s.
- imports: none for the computation. The old card also cites Prellberg (J. Phys. A 36, 2455, 2003) for the
  continuous spectrum [0, 1], Hofbauer–Keller quasi-compactness and Yuri's weak Gibbs property; this card does not
  rest on them.
- premises on main: B852 (the Farey pressure and its method), B1813 (the s-family), P-713 (the transition places no
  τ), P-441 and P-468 (the critical line), P-629 (the symmetric points)
- decisive script: relays/chat1_2026-11-25_p632/card_p632.py, SHA-256 b6ca05f7aff26875, depends on the standard library
  and numpy, run as python3 relays/chat1_2026-11-25_p632/card_p632.py, output SHA-256 9299ced9fe51bd4a
- decisive lines: 15 lines marked "DECISIVE:", SHA-256 081f0339be415c96
- failing control: python3 relays/chat1_2026-11-25_p632/card_p632.py --control
- second computation: none that shares no code. Within the sealed p632_modes.py, λ₁ is computed at three N (agreeing
  to about 1e-13 at N = 128 and 256 for s ≤ 0.9) and by the word sums Z₁₈/Z₁₇ (within 7e-5 at s = 0.25 and 6.3e-4 at
  s = 0.5). The old card's referee computed λ₁ by inducing on the Gauss map, not committed. The decisive script runs
  the sealed p632_modes.py (SHA-256 e5d9879e6a3dda93, at 718935fa0; the decisive script's docstring names 8fadd3f3e,
  where an earlier version stands, by mistake) unchanged.
- already on main?: topic_sweep.py "instability spectrum|Farey operator|fastest-growing" at 68b04c69d: no arc, one
  register row (P-632); the old card's sweep found B852 the nearest, which computes the leading eigenvalue only
- what would make it fail: a leading eigenfunction of F_s, at s = 0.1, ..., 0.9, with an interior extremum; or values
  that differ from the sealed output. The control applies the same
  check to the second eigenfunction at s = 0.5 in place of the first: it changes sign, and the check fails.
