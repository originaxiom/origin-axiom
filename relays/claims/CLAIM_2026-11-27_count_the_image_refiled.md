# CLAIM CARD — frame A's map to the six descends through none of its five named choices; joint image dimension 5

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: negative
- touches: P-612, P-418, P-355; A01, A02, A03, A04, A07, A09, A10
- effect: conditions — A01, A02, A03, A04, A07, A09, A10: their price under T-COUNT-THE-IMAGE is the image, not one row
  each. The offset (A03) has 10 images, the ends (A07) 7, the A04 menu 3 and c (A10) 5; the continuous choices' joint
  image has dimension 5. D = c^2 descends through A01, A07 and A04 on the base line wherever D is defined. No joint is
  earned or removed.
- scope: frame: frame A, the record's candidate, through main's frozen-row instrument (B1842) at the reading
  (S~, S, S), a0 = 0, H = I, read only as ratios of its own singular values; object: whether the six and D are constant
  under each of c, the 2/5 class (slope and offset), the end norm, tau and the Higgs direction, and the size of each
  choice's image; reach: single; hypotheses:
  - the three moduli 0.21 + 2.97i, -0.33 + 3.08i and 0.44 + 3.02i stand in for the strip, and 3.0i serves for the
    mirror plant only; B1841's own tau is not used;
  - continuous images are local Jacobian ranks at those points, not global images;
  - a mass ratio below 1e-12 counts as a zero, and logs of a zero are undefined;
  - finite-difference steps 1e-3 and 5e-4; rank threshold 1e-4; CONSTANT below 1e-8, NON-CONSTANT above 1e-5
- identifications: none
- definitions:
  - **The six and D.**
    - The six are ln(m1/m2) and ln(m2/m3) for up, down and lepton, from the singular values m3 >= m2 >= m1 of
      Y_sector.
    - Y_sector is B1726's coupling with B1838's exact twisted channel norms over B1667's cell, cut at the horoball level
      L_h(tau). The up sector is read with S~ = eps conj(S) eps^T; down and lepton with S.
    - c multiplies the lepton m2/m3 by c and divides its m1/m3 by c (B1789 sec. 1).
    - D = c^2 R2 R1, with R2 = (m2/m3)_e / (m2/m3)_d and R1 = (m1/m3)_d / (m1/m3)_e.
  - **The base row:** line (2/5, 4/5), end E4 (L_h = L_2 - pi/2), Higgs DR, c = 3.
  - **The choices' menus:**
    - c in {1, 2, 3, 4, 5};
    - the 2/5 offsets b = k/10 (ten lines), and all 99 lines (j/10, k/10) other than (0, 0);
    - the ends E1 = L_2, E2 = ln 2, E3 = L_max, E4, delta = inf (each channel weight 1), and the small-cut norm
      2 pi L + c_s at L_max and at L_2;
    - the Higgs menu R, DR, D^2R (B1691), and C^3 about DR (6 real directions);
    - tau in (Re tau, Im tau);
    - jointly, all ten continuous parameters: Re tau, Im tau, the end level, the Higgs (6 real) and ln c.
  - **Descend and image.** A choice descends on an output if the output's spread over its menu is below 1e-8. Its image
    is the number of distinct output vectors at 1e-5, or, for a continuous choice, the rank of the Jacobian.
  - **The plants:**
    - PL1: D scales as c^2;
    - PL2: one down channel weight times (1 + 1e-4) must register;
    - PL3: the Higgs scale and phase are null;
    - PL4: the mirror (a, b) to (a, -b) at Re tau = 0;
    - PL5: the T-law (tau, (a, b)) to (tau + 1, (a, b - a)) at delta = inf;
    - PL6: c leaves the quark four unchanged.
- imports: none
- premises on main:
  - B1842 (the frozen-row instrument, P-688), B1838, B1726, B1723, B1691, B1667;
  - B1840 (the closed list of ends E1 to E4), B1789 (c and D);
  - B1232 (T-COUNT-THE-IMAGE), P-355 (the d = e identity), B1834 (P-418's scoreboard), B1831 (row 237).
  - The void run is kept on record. SM-R612 (relays/sm_r612/run.py, SHA-256 a0ae72658d25a97e) was void by its own rule:
    PL5 failed, 0.87 to 1.8, from logs of numerical-zero masses. The decisive run is the re-sealed SM-R612b
    (relays/sm_r612b/run.py, SHA-256 0d0edb642ce9dcbb), sealed after the void run's results were known.
- decisive script: relays/claims/sm_refile/r612_decisive.py, SHA-256 f5c608bdbe74874d, depends on the standard library,
  numpy and mpmath, run as python3 relays/claims/sm_refile/r612_decisive.py, output SHA-256 4b7db5aeb3901109, heavy
- decisive lines: 47 lines marked "DECISIVE:", SHA-256 dfca11fd69493eb2
- failing control: python3 relays/claims/sm_refile/r612_control.py
- second computation: none
- already on main?: `grep -il "count the image" frontier/*/FINDINGS.md` on main finds B1232 only, the retired P^3 case.
  B1831's reader table, row 237, says the lemma was never applied to the input count. The closest arc is B1232.
- what would make it fail: any one of these refutes it:
  - any named choice registering CONSTANT on the six;
  - a discrete menu's image smaller than its size, other than through the sign pair or the mirror;
  - a joint rank other than 5;
  - D differing from c^2 at a defined point of the base line under tau, the end or the Higgs;
  - any plant outside its sealed bound (PL2 not registering, or PL5 failing on its defined outputs), which voids the run
