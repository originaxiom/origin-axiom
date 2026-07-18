# B683 / Cell L3 — the Mahler / Beilinson three-way

Numeric flagship for the arithmetic ledger. All values exact-grade
(mpmath, dps 45–70). Two-outcome, base-rate discipline: a HIT requires a
clean small rational to 20+ digits; a near-miss is a NO-HIT.

## The A-polynomial

    A(M,L) = M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4

Standard figure-eight (4_1) A-polynomial (geometric factor). On |M|=1 the
L-leading coeff is M^4, so log|lead| = 0; the two L-roots satisfy
L_+ L_- = M^4/M^4 = 1, so |L_+||L_-|=1 and the Boyd integrand is
log max(|L_+|,|L_-|) >= 0.

Root-modulus transitions (kinks) occur where c(theta)=B/M^4 crosses -2,
with c = 4cos^2(2theta) - 2cos(2theta) - 4; i.e. cos 2theta = -1/2, at
theta = pi/3, 2pi/3, 4pi/3, 5pi/3. Quadrature is subdivided there; the
integrand vanishes on (pi/3,2pi/3) and (4pi/3,5pi/3).

## The three numbers (dps 45; leg-1 confirmed to dps 70)

    m(A_41)     = 0.646131894438901028187273021447612788144483682
    Vol(4_1)/2pi= 0.323065947219450514093636510723806394072181582
    L'(E15,0)   = 0.251330433713252231374872566669336294636860391
    L(E15,2)    = 0.661475187921069742727520633979626889791045796
    Vol(4_1)    = 2.029883212819307250042405108549040571883378615...

Each of the four Boyd support-integral pieces equals Vol/2 exactly
(=1.01494160640965362502120..., residual 1.8e-71 at dps 70).

L(E15,2), L'(E15,0): newform 15.2.a.a (isogeny class 15a, curve 15a1
[1,1,1,-10,-10]); a_p by point-counting, a_p matches the newform
(a_2,a_3,a_5,a_7,a_11,a_13 = -1,-1,1,0,-4,-2); smoothed functional
equation, sign eps=+1 (rank 0; L(E15,1)=0.35015...>0). Internal check:
L'(E15,0)/L(E15,2) = 15/(4 pi^2) = 0.379954438658766642914... exact.

## The three-way test

LEG 1 — m(A_41) vs the volume:  **HIT.**
    m(A_41) / (Vol/2pi) = 2.000...   (PSLQ [m, Vol/2pi] -> [1,-2])
    m(A_41) - Vol/pi = -9.06e-72  (dps 70)
  => m(A_41) = Vol(4_1)/pi,  EXACT to 70 digits.
  This is Boyd's Borel/K_3-regulator identity: the Mahler measure computes
  the hyperbolic volume, hence (via B680) equals (3 sqrt3 / 2pi) L(chi_-3, 2)
  -- the Dirichlet L-value at s=2 of the being character.

LEG 2 — m(A_41) vs the elliptic L'(E15,0):  **NO-HIT.**
    m(A_41) / L'(E15,0)      = 2.5708462158470049992...  (not rational)
    (Vol/2pi) / L'(E15,0)    = 1.2854231079235024996...
    L'(E15,0) / (Vol/2pi)    = 0.7779539622680499793...
  PSLQ [m, L'(E15,0)] -> None; [Vol/2pi, L'(E15,0)] -> None;
  [m, L'(E15,0), pi] -> None; [m, L(E15,2)] -> None (maxcoeff 1e6).
  No clean rational multiple exists.

## Verdict

- **m(A_41) = Vol(4_1)/pi**, exact to 70 digits (PSLQ [1,-2] vs Vol/2pi;
  residual 9e-72). This is the realized Beilinson regulator.
- **m(A_41) is NOT a rational multiple of L'(E15,0)** (NO-HIT, no relation
  to coeff bound 1e6).

Structural reading: although the A-polynomial curve is isogenous to the
conductor-15 elliptic curve 15a (B674), the Mahler measure does NOT land
on the elliptic L'(E15,0) (a K_2 / weight-2 value). It lands on the
VOLUME -- the K_3 / Borel regulator of the trace field Q(sqrt-3), i.e.
the Dirichlet value L(chi_-3, 2). The knot-arithmetic bridge realized
here is volume <-> being-character, not volume <-> E15. The elliptic
isogeny and the Mahler regulator are genuinely distinct arithmetic legs.

Artifacts (this dir): mahler_a2.py (Mahler, dps 55), confirm_hp.py
(dps-70 confirmation m=Vol/pi), lfunc_e15.py (L(E15,2), L'(E15,0)),
threeway.py (ratios + PSLQ).
