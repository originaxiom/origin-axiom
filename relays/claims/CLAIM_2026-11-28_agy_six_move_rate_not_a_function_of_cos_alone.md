# CLAIM CARD — the six-move slow rate is not a function of cos(pi/M) alone: at the five levels of B2015 it fits no polynomial in cos(pi/M) of degree 1 to 3

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, a3a372470d3ee9fc1e3acca2ec1bb91c322e3d42
- kind: negative
- touches: P-882 (the listening line); the law map's row LISTENING 29
- effect: refutes — LISTENING 29, as a law in cos(pi/M) alone
- scope: frame: no frame, the six-move slow rate at the five levels of B2015's R1 (mod 27, 81, 125, 343 and 625); object: whether the rate is a polynomial in c = cos(pi/M); reach: class; hypotheses: polynomials of degree 1 to 3 with real coefficients, fitted by least squares, an exact form accepted at a largest residual below 1e-10, M as B2015's run gives it for each level
- identifications: none
- definitions: the six-move slow rate r at a level is the largest eigenvalue below 6 of W = L + R + L^-1 + R^-1 + X + X^-1 on the largest orbit over the common point, as B2015 defines it (its R1), with the value its run prints in double precision; M is the number B2015's run gives for the level; c = cos(pi/M); a fit of degree d is the least-squares polynomial of degree d in c through the five values, and its residual the largest absolute difference at the five levels
- imports: none
- premises on main: B2015 (its run's values, rate_law_run.txt, copied beside the script under its own path)
- decisive script: relays/claims/rate_form/rate_form.py, SHA-256 536048e10aab4cac, depends on the standard library and numpy, run as python3 relays/claims/rate_form/rate_form.py, output SHA-256 dbc1323c20495b4b
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 fdfe1fc446bff56a
- failing control: python3 relays/claims/rate_form/rate_form.py --control
- second computation: none
- already on main?: B2015 gives the rate's value at each level it ran; no arc on main tests the rate's form in cos(pi/M)
- what would make it fail: a polynomial of degree at most 3 in cos(pi/M) through the five values with a largest residual below 1e-10
