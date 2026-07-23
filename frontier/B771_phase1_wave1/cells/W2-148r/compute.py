#!/usr/bin/env python3
"""W2-148r -- level-27 mu_infinity re-derivation under the PROVEN normalization.

(B771 Phase-1 Wave 2; prereg addendum PREREG_WAVE2.md, sealed 486ea7c8.)

HISTORY THIS CELL MUST RESOLVE (read from the artifacts, restated for the record):
  - Wave-1 OI-148 computed an exact 9-vs-27 discrepancy for the B415/T1 registered
    level-27 prediction gauss_norm_at_level(3) = 3^3 = 27, but was VERIFY-REFUTED
    (upheld=false): its "x12 clearing" y = 12v was justified by the y-cubic's linear
    coefficient being -3 -- which is TAUTOLOGICAL given the already-banked
    e2(v) = -1/48 (any N gives linear coefficient -N^2/48; N=12 is the unique
    positive solution of -N^2/48 = -3, so the "match" was circular), and it ignored
    B399's own negative D-sweep (identify_1215_triple.py Method 2: v=(X+Yc1+Zc2)/D,
    D in {12,...,1152} INCLUDING 12, |X|,|Y|,|Z| <= 400, over the Q(zeta9)+ basis
    {1, c1=2cos(2pi/9), c2=2cos(4pi/9)}: "NO small form found" for any cell).
  - Wave-1 OI-031 then PROVED the true normalization (upheld=true, adversarially
    verified): the level-1215 triple values are v_c = cos(2*pi*k/27)/6 exactly
    (classes c=121,256,391 <-> k=10,19,1), the cubic is Chebyshev,
    t^3 - t/48 - cos(2pi/9)/864, i.e. u=12t satisfies u^3 - 3u - 2cos(2pi/9) = 0
    with roots u = 2cos(2pi k/27) -- the zeta27 rung of the trisection tower.

THIS CELL (per the sealed Wave-2 criterion):
  (1) FIRST establish what the mu_inf/B415 prediction's OBJECT is under the proven
      normalization;
  (2) address the verifier's circularity findings and B399's negative D-sweep
      EXPLICITLY (computed, not asserted);
  (3) compute the discriminating fact exactly, in-cell, from the raw banked
      residues AND independent symbolic + high-precision routes;
  (4) two-outcome verdict: prediction confirmed at level 27 => RESOLVED-A /
      refuted with the correct comparison established => RESOLVED-B.
      Named failure mode: forcing the old N=12 story. (The N=12 clearing is used
      below ONLY because it is now a THEOREM -- v_c = (zeta27^k + zeta27^-k)/12,
      re-proven in-cell from the raw 20-prime data + exact cyclotomics -- not
      because the old cell chose it.)

THE PREDICTION OBJECT (established before any comparison is made):
  B413 (level 9, exact, banked): the tower-measure's innovation orbit at level 9
  is {(1+c_m)/12 : m in {1,4,7}}, c_m = zeta9^m + zeta9^-m, and the order-3
  character resolvent satisfies
        12*L(chi_1) = zeta9 + zeta9^4 + zeta9^7 + 3*zeta9^8  in Z[zeta9],
        |12*L(chi_1)|^2 = 9      (exact; re-derived symbolically below).
  B415/T1 (t1_continuum.py, the REGISTERED prediction): if the flat/Gauss-sum
  property persists, gauss_norm_at_level(k) = |12*L(chi_1)|^2 = 3^k at rung 3^k;
  at level 27 (k=3) the registered prediction is 27. T1's own level-27 "check"
  used an ad hoc orbit guess (orbit_m=[1,4,7] at N=27) and (1+c)-shaped values --
  neither matches any banked object: the REAL level-27 innovation is the B399
  1215-rung triple (mean-zero: no "1+"; additive orbit k in {1,10,19}, i.e.
  k == 1 mod 9, NOT a {1,4,7} guess).
  Under the proven normalization, the like-for-like level-27 object is therefore:
        12*L(chi) = sum_j chi(class_j) * 12*v_{class_j}
                  = the Z/3 resolvent of {zeta27^k + zeta27^-k : k=1,10,19},
  the exact parallel of B413's level-9 resolvent of {1+c_m} (both are resolvents
  of the ALGEBRAIC-INTEGER forms 12v of the raw tower values v; the 12 is the
  tower's own constant -- the frozen 1/12 line at the same rung, the seam
  constant, the (1+c)/12 normalizer -- and, decisively, 12v is an algebraic
  integer while v is not: proven below).

Everything below is exact (sympy polynomials over Q, exact F_p arithmetic on the
raw banked residues) plus an independent mpmath high-precision twin at two
working precisions. No step uses the old OI-148 justification.
"""
import json
import math
import os
import time

import sympy as sp
import mpmath as mp

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
B399 = os.path.normpath(os.path.join(HERE, "..", "..", "..", "B399_wall_scale"))


def log(msg=""):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)


FAIL = []          # any failed gate lands here; verdict logic sees it


def gate(ok, label):
    log(f"  gate [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        FAIL.append(label)


# ===========================================================================
# STEP 0 -- raw data + structural gates, re-derived in-cell (not cited)
# ===========================================================================
log("STEP 0: load the 20-prime raw residue data (B399_wall_scale) and re-derive "
    "the structural gates in-cell")
FILES = ["singles_1215.json", "singles_1215_p3.json", "singles_1215_p456.json",
         "singles_1215_p7_10.json", "singles_1215_p11_20.json",
         "singles_1215_p14_20.json"]
DATA = {}
for f in FILES:
    DATA.update(json.load(open(os.path.join(B399, f))))
PRIMES = sorted(int(p) for p in DATA)
gate(len(PRIMES) == 20, f"20 banked primes loaded ({PRIMES[0]}..{PRIMES[-1]})")

CLASSES = (121, 256, 391)      # the triple's classes mod 405 (translation +135)
TRIPLE = {}                    # p -> {class: value mod p}
for p in PRIMES:
    cells = {int(a): int(v) % p for a, v in DATA[str(p)].items()}
    ok = len(cells) == 24 and all(a % 45 == 31 for a in cells)
    inv12 = pow(12, p - 2, p)
    line = [a for a, v in cells.items() if v == inv12]
    trip = [a for a in cells if a not in line]
    ok &= len(line) == 12 and len(trip) == 12
    byc = {}
    for a in trip:
        byc.setdefault(a % 405, set()).add(cells[a])
    ok &= sorted(byc) == list(CLASSES) and all(len(v) == 1 for v in byc.values())
    if not ok:
        gate(False, f"structure at p={p}")
        continue
    TRIPLE[p] = {c: byc[c].pop() for c in CLASSES}
gate(len(TRIPLE) == 20, "all 20 primes: 24 cells, mod-45=31, 12x(1/12) line, "
                        "triple constant on classes {121,256,391} mod 405")

# e1, e2 re-derived from the raw residues (e2 = -1/48 is the only banked input
# the OLD cell leaned on; we re-prove it here and then NEVER use it to justify
# the normalization)
ok1 = ok2 = True
for p in PRIMES:
    v1, v2, v3 = (TRIPLE[p][c] for c in CLASSES)
    ok1 &= (v1 + v2 + v3) % p == 0
    ok2 &= (v1 * v2 + v1 * v3 + v2 * v3) % p == (-pow(48, p - 2, p)) % p
gate(ok1, "e1 = 0 mod all 20 primes (triple sums to zero)")
gate(ok2, "e2 = -1/48 mod all 20 primes")

# ===========================================================================
# STEP 1 -- THE NORMALIZATION IS A THEOREM (re-proven in-cell, three routes)
# ===========================================================================
log("")
log("STEP 1: re-prove the OI-031 normalization in-cell: v_c = (z^k + z^-k)/12, "
    "z = zeta27, k in {1,10,19}")

# --- 1a. exact symbolic: in Q[z]/Phi_27, prod_{k}(t - (z^k+z^-k)/12) closes ---
z, t = sp.symbols('z t')
PHI27 = sp.Poly(z**18 + z**9 + 1, z, domain=sp.QQ)


def red27(expr):
    """reduce a polynomial in z modulo Phi_27 (exact, over Q)."""
    return sp.Poly(sp.expand(expr), z, domain=sp.QQ).rem(PHI27).as_expr()


KS = (1, 10, 19)
y_of = {k: z**k + z**(27 - k) for k in KS}          # 12*v as z-polynomials
prod_poly = sp.expand(sp.prod(t - y_of[k] / 12 for k in KS))
prod_poly = sp.Poly(prod_poly, t)
coefs = {d: red27(prod_poly.coeff_monomial(t**d)) for d in range(3)}
c9 = z**3 + z**24                                    # 2cos(2pi/9) as a z-poly
ok_e1 = sp.simplify(coefs[2]) == 0
ok_e2 = sp.simplify(coefs[1] + sp.Rational(1, 48)) == 0
ok_e3 = sp.simplify(red27(sp.expand((coefs[0]) * 1728 + c9))) == 0
gate(ok_e1, "symbolic: e1(v) = 0 exactly in Q[z]/Phi_27")
gate(ok_e2, "symbolic: e2(v) = -1/48 exactly")
gate(ok_e3, "symbolic: e3(v) = (z^3+z^-3)/1728 = 2cos(2pi/9)/1728 = cos(2pi/9)/864 "
            "exactly -- the triple cubic is t^3 - t/48 - cos(2pi/9)/864, "
            "u=12t: u^3 - 3u - 2cos(2pi/9), Chebyshev trisection")

# --- 1b. the same, prime-by-prime on the RAW residues (deterministic embedding)
def primitive_root(p):          # identical algorithm to the data engine's
    fac, n, d = [], p - 1, 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    g = 2
    while True:
        if all(pow(g, (p - 1) // f, p) != 1 for f in fac):
            return g
        g += 1


ASSIGN = {}                     # p -> {class: k} bijection actually observed
ok_coh = ok_match = True
for p in PRIMES:
    g = primitive_root(p)
    z27 = pow(g, (p - 1) // 27, p)
    z9 = pow(g, (p - 1) // 9, p)
    ok_coh &= pow(z27, 3, p) == z9          # ladder coherence z27^3 = z9
    roots = {k: (pow(z27, k, p) + pow(z27, 27 - k, p)) % p for k in KS}
    vals = {c: (12 * TRIPLE[p][c]) % p for c in CLASSES}
    inv = {}
    for c in CLASSES:
        hits = [k for k in KS if roots[k] == vals[c]]
        if len(hits) != 1:
            ok_match = False
            break
        inv[c] = hits[0]
    else:
        ok_match &= sorted(inv.values()) == sorted(KS)
        ASSIGN[p] = inv
gate(ok_coh, "F_p embedding coherence: z27^3 = z9 for the deterministic "
             "primitive-root embedding, all 20 primes")
gate(ok_match, "F_p: the multiset {12*v_c mod p} EQUALS {z27^k + z27^-k : "
               "k=1,10,19} mod p, with a unique class<->k bijection, all 20 primes")
assigns = {tuple(sorted(a.items())) for a in ASSIGN.values()}
gate(len(assigns) == 1, f"the class->k assignment is IDENTICAL across all 20 "
                        f"primes: {ASSIGN[PRIMES[0]]}")
CK = ASSIGN[PRIMES[0]]          # e.g. {121: 10, 256: 19, 391: 1}

# --- 1c. mpmath twin at two precisions (the archimedean embedding) -----------
prec_agree = []
for dps in (50, 100):
    mp.mp.dps = dps
    dev = max(abs(mp.cos(2 * mp.pi * CK[c] / 27) / 6
                  - mp.cos(2 * mp.pi * CK[c] / 27) / 6) for c in CLASSES)  # identity twin
    # the real content at this precision: the cubic actually vanishes on the roots
    e3v = mp.cos(2 * mp.pi / 9) / 864
    resid = max(abs(u**3 - u / mp.mpf(48) - e3v)
                for u in [mp.cos(2 * mp.pi * k / 27) / 6 for k in KS])
    prec_agree.append(resid)
gate(all(r < mp.mpf(10) ** (-(d - 5)) for r, d in zip(prec_agree, (50, 100))),
     f"mpmath twin (dps=50,100): cos(2pi k/27)/6 satisfies t^3 - t/48 - cos(2pi/9)/864 "
     f"to full working precision (residuals {prec_agree[0]}, {prec_agree[1]})")

# --- 1d. integrality: x12 is the canonical clearing, not a choice ------------
x = sp.symbols('x')
mp_y = sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / 27), x)      # integer-primitive
mp_v = sp.minimal_polynomial(sp.cos(2 * sp.pi / 27) / 6, x)
py, pv = sp.Poly(mp_y, x), sp.Poly(mp_v, x)
gate(py.degree() == 9 and py.LC() == 1,
     f"y = 2cos(2pi/27) IS an algebraic integer: minpoly monic integer, degree 9 "
     f"({sp.factor(mp_y)!s:.60s}...)")
gate(pv.degree() == 9 and pv.LC() != 1,
     f"v = cos(2pi/27)/6 is NOT an algebraic integer (primitive minpoly has "
     f"leading coefficient {pv.LC()} != 1): multiplying by 12 is the clearing "
     f"to the ring of integers of Q(zeta27)+, exactly parallel to level 9's "
     f"v=(1+c)/12 -> 12v = 1+c in Z[zeta9]")

# ===========================================================================
# STEP 2 -- the verifier's circularity findings, addressed head-on
# ===========================================================================
log("")
log("STEP 2: the Wave-1 verifier's findings, addressed by computation")

# (2.i) the old justification WAS circular -- reproduce the tautology explicitly
N = sp.symbols('N', positive=True)
lin_coeff = sp.expand((N**2) * sp.Rational(-1, 48))   # linear coeff of (Nv)-cubic
sols = sp.solve(sp.Eq(lin_coeff, -3), N)
gate(sols == [12], "confirmed the verifier: given e2(v)=-1/48, the y=N*v cubic has "
                   "linear coefficient -N^2/48 for EVERY N; '-3' selects N=12 "
                   "tautologically. The old cell's 'forced' was circular. The new "
                   "derivation NEVER uses this; N=12 now comes from the proven "
                   "root form (STEP 1) alone.")

# (2.ii) the verifier's counterfactual N = 12*sqrt(3) (which would rescale the
# norm to 27) is NOT an available normalization in the object's own field:
# sqrt(3) is not in Q(zeta27). Proof, computed: (Z/27)* is cyclic (2 is a
# primitive root mod 27), so Q(zeta27) has a UNIQUE quadratic subfield; that
# subfield is Q(sqrt(-3)) (witness: (z^9 - z^18)^2 = -3 exactly mod Phi_27);
# Q(sqrt(3)) != Q(sqrt(-3)) (real vs imaginary). Hence sqrt(3)*y is outside the
# field for nonzero y, and no Z-integral normalization inside Q(zeta27)+ can
# turn the resolvent norm 9 into 27.
ord2 = 1
a = 2 % 27
while a != 1:
    a = a * 2 % 27
    ord2 += 1
gate(ord2 == 18, "2 is a primitive root mod 27 (order 18) => (Z/27)* cyclic => "
                 "Q(zeta27) has a UNIQUE quadratic subfield")
w = z**9 - z**18
gate(sp.simplify(red27(sp.expand(w**2 + 3))) == 0,
     "(z^9 - z^18)^2 = -3 exactly in Q[z]/Phi_27: the unique quadratic subfield "
     "is Q(sqrt(-3)); sqrt(3) is NOT in Q(zeta27), so the counterfactual "
     "N=12*sqrt(3) clearing exits the object's value field entirely -- it is "
     "not a competing normalization")

# ===========================================================================
# STEP 3 -- B399's negative D-sweep, reconciled (it was a wrong-FIELD negative)
# ===========================================================================
log("")
log("STEP 3: the B399 negative D-sweep (identify_1215_triple.py Method 2), "
    "reconciled with the proven form")
# The sweep hunted v = (X + Y*c1 + Z*c2)/D with c1,c2 = 2cos(2pi/9), 2cos(4pi/9)
# -- i.e. INSIDE Q(zeta9)+, degree 3 over Q -- for D in {12,...,1152}, |X,Y,Z|<=400.
# The proven value v = (z^k+z^-k)/12 has degree 9 over Q (STEP 1d): it cannot lie
# in a degree-3 field at ANY coefficient height or denominator. The sweep's
# "NO small form found" is IMPLIED by the true form; it never tested (and cannot
# refute) the denominator 12 -- it refutes only zeta9+-numerators over 12.
gate(py.degree() == 9, "deg_Q(2cos(2pi/27)) = 9; [Q(zeta9)+:Q] = 3; 9 > 3 => "
                       "v is in NO (X+Y*c1+Z*c2)/D form at any height: the "
                       "D-sweep negative is exactly what the proven form predicts")
# sharper, computed: the relative trace of y to Q(zeta9)+ is ZERO (e1 = 0 is
# precisely Tr_{Q(zeta27)+/Q(zeta9)+}(y) = 0), so the sweep's target was
# literally trace-orthogonal to the field it searched.
tr_rel = red27(sum(y_of[k] for k in KS))
gate(sp.simplify(tr_rel) == 0, "Tr_{Q(zeta27)+/Q(zeta9)+}(y) = y_1+y_10+y_19 = 0: "
                               "the swept field sees the triple only through its "
                               "(vanishing) relative trace")

# ===========================================================================
# STEP 4 -- the level-9 anchor, re-derived exactly (the prediction's base case)
# ===========================================================================
log("")
log("STEP 4: the B413 level-9 anchor re-derived in-cell (exact)")
PHI9 = sp.Poly(z**6 + z**3 + 1, z, domain=sp.QQ)


def red9(expr):
    return sp.Poly(sp.expand(expr), z, domain=sp.QQ).rem(PHI9).as_expr()


# level-9 innovation values: (1 + c_m)/12, m in {1,4,7} (the additive orbit
# m == 1 mod 3, exponents -(1+3j) mod 9 in {8,5,2}); resolvent with
# omega = zeta9^3 and zeta9^6 (z stands for zeta9 here):
anchor = {}
for wexp in (3, 6):
    om = z**wexp
    expr = sum(om**j * (1 + z**(1 + 3 * j) + z**(9 - ((1 + 3 * j) % 9)))
               for j in range(3))
    anchor[wexp] = red9(sp.expand(expr))
# banked B413 form: zeta9 + zeta9^4 + zeta9^7 + 3 zeta9^8
banked = red9(z + z**4 + z**7 + 3 * z**8)
ok_anchor_form = sp.simplify(anchor[3] - banked) == 0
gate(ok_anchor_form, f"12*L(chi_1) at level 9 (omega=zeta9^3 pairing) = "
                     f"{sp.simplify(anchor[3])} = banked zeta9+zeta9^4+zeta9^7+3*zeta9^8 "
                     f"(they are equal mod Phi_9: the banked 4-term form simplifies "
                     f"to 3*zeta9^8 = 3*zeta9^-1)")
# norms: |a|^2 computed exactly as a * conj(a), conj: z -> z^8 (=z^-1)
def norm9_sq(expr):
    conj = red9(sp.expand(expr.subs(z, z**8)))
    return sp.simplify(red9(sp.expand(expr * conj)))


n9 = {wexp: norm9_sq(anchor[wexp]) for wexp in (3, 6)}
gate(n9[3] == 9 and n9[6] == 9,
     f"|12*L(chi_1)|^2 = {n9[3]} and |12*L(chi_2)|^2 = {n9[6]} at level 9 (exact; "
     f"the anchor 9 = 3^2 numerically -- note it is ALSO |3*zeta|^2, the two "
     f"readings coincide at the anchor and CANNOT be distinguished there)")

# ===========================================================================
# STEP 5 -- THE DISCRIMINATING FACT: the level-27 resolvent, exact, three routes
# ===========================================================================
log("")
log("STEP 5: the level-27 resolvent under the proven normalization -- exact")

# --- 5a. symbolic in Q[z]/Phi_27: 12L = 3 * (a 27th root of unity) ----------
resolv = {}
for wexp in (9, 18):                     # omega = z^9 or z^18 (the two pairings)
    om = z**wexp
    expr = sum(om**j * (z**(1 + 9 * j) + z**(27 - ((1 + 9 * j) % 27)))
               for j in range(3))
    resolv[wexp] = sp.simplify(red27(sp.expand(expr)))
# equality mod Phi_27 (3*z^26 itself reduces: z^26 = z^8*z^18 == z^8*(-z^9-1))
eq9 = sp.simplify(red27(sp.expand(resolv[9] - 3 * z**26))) == 0
eq18 = sp.simplify(red27(sp.expand(resolv[18] - 3 * z))) == 0
gate(eq9 and eq18,
     f"symbolic: sum_j omega^j (z^(1+9j) + z^-(1+9j)) = {resolv[9]} (omega=z^9) "
     f"and {resolv[18]} (omega=z^18): the resolvent is EXACTLY 3*zeta27^-+1 -- "
     f"three times a PURE 27th root of unity, not a primitive-conductor Gauss sum")


def norm27_sq(expr):
    conj = red27(sp.expand(expr.subs(z, z**26)))
    return sp.simplify(red27(sp.expand(expr * conj)))


n27 = {wexp: norm27_sq(resolv[wexp]) for wexp in (9, 18)}
gate(n27[9] == 9 and n27[18] == 9,
     f"symbolic: |12*L|^2 = {n27[9]} (both pairings) at level 27 -- EXACT")

# --- 5b. the SAME resolvent computed from the RAW banked residues -----------
# chi is the order-3 character on the +135 translation: chi(121+135i) = omega^i.
ok_raw = True
tset = set()
for p in PRIMES:
    g = primitive_root(p)
    z27p = pow(g, (p - 1) // 27, p)
    omp = pow(z27p, 9, p)
    L12 = sum(pow(omp, i, p) * 12 * TRIPLE[p][c] for i, c in enumerate(CLASSES)) % p
    L12bar = sum(pow(omp, -i, p) * 12 * TRIPLE[p][c] for i, c in enumerate(CLASSES)) % p
    ok_raw &= (L12 * L12bar - 9) % p == 0
    hits = [tt for tt in range(27) if (L12 - 3 * pow(z27p, tt, p)) % p == 0]
    tset.add(tuple(hits))
gate(ok_raw, "RAW DATA: 12L * conj(12L) = 9 mod ALL 20 primes, computed from the "
             "banked residues themselves (not from the closed form)")
gate(len(tset) == 1 and len(next(iter(tset))) == 1,
     f"RAW DATA: 12L = 3 * zeta27^t mod every prime with the SAME t = "
     f"{next(iter(tset))[0]} across all 20 primes (phase, embedding-consistent)")

# --- 5c. mpmath twin, two precisions ----------------------------------------
mp_ok = True
for dps in (50, 100):
    mp.mp.dps = dps
    om = mp.e ** (2j * mp.pi / 3)
    L12m = sum(om**j * 2 * mp.cos(2 * mp.pi * (1 + 9 * j) / 27) for j in range(3))
    mp_ok &= abs(abs(L12m) ** 2 - 9) < mp.mpf(10) ** (-(dps - 5))
    mp_ok &= abs(L12m - 3 * mp.e ** (-2j * mp.pi / 27)) < mp.mpf(10) ** (-(dps - 5))
gate(mp_ok, "mpmath twin (dps=50,100): |12L|^2 = 9 and 12L = 3*exp(-2pi i/27) to "
            "full working precision (independent archimedean arithmetic)")

# --- 5d. the character table completed (what 'flat' means now) ---------------
# trivial character: L(chi_0) = sum v = e1 = 0 (STEP 0/1). Nontrivial: |L| = 3/12 = 1/4.
log("  character table of the level-27 innovation triple (exact): "
    "L(chi_0) = 0 (mean-zero innovation; the rung's mass 1 sits entirely on the "
    "frozen 1/12 line), |L(chi_1)| = |L(chi_2)| = 3/12 = 1/4")

# ===========================================================================
# STEP 6 -- the general-rung freeze lemma (bonus, conditional)
# ===========================================================================
log("")
log("STEP 6: the freeze generalizes -- symbolic check at rungs 3^k, k=2..7")
ok_all = True
for k in range(2, 8):
    m = 3 ** (k - 1)
    PHIk = sp.Poly(z**(2 * m) + z**m + 1, z, domain=sp.QQ)
    expr = sum((z**m)**j * (z**(1 + m * j) + z**(3 * m - ((1 + m * j) % (3 * m))))
               for j in range(3))
    diff = sp.expand(expr - 3 * z**(3 * m - 1))
    r = sp.Poly(diff, z, domain=sp.QQ).rem(PHIk).as_expr()
    ok_all &= sp.simplify(r) == 0
gate(ok_all, "for every rung 3^k, k=2..7: the resolvent of the additive orbit "
             "{1, 1+3^(k-1), 1+2*3^(k-1)} is EXACTLY 3*zeta_{3^k}^-1 -- "
             "|12L|^2 = 9 FROZEN at every rung (conditional on the orbit "
             "persisting as the additive triple; proven from data at k=2,3)")

# ===========================================================================
# VERDICT
# ===========================================================================
log("")
log("=" * 77)
PREDICTED = 27          # t1_continuum.py gauss_norm_at_level(3) = 3**3, registered
COMPUTED = int(n27[9])  # exact
log("THE COMPARISON (prediction object established in STEP 4/5, normalization "
    "proven in STEP 1):")
log(f"  registered B415/T1 prediction at level 27:  |12*L(chi_1)|^2 = 3^3 = {PREDICTED}")
log(f"  exact value under the proven normalization: |12*L(chi_1)|^2 = {COMPUTED}")
log(f"  level-9 anchor (re-derived):                |12*L(chi_1)|^2 = 9")
log("")
if FAIL:
    verdict = "UNRESOLVED"
    log(f"GATES FAILED ({len(FAIL)}): " + "; ".join(FAIL))
elif COMPUTED == PREDICTED:
    verdict = "RESOLVED-A"
else:
    verdict = "RESOLVED-B"
    log("RESOLVED-B: the registered 3^k growth prediction is REFUTED at level 27 "
        "with the correct comparison now established on a PROVEN normalization:")
    log("  12L = 3*zeta_{3^k}^-1 exactly (k=2 AND k=3, from raw data + symbolic + "
        "mpmath): the resolvent norm FREEZES at 9; it never was a growing "
        "primitive Gauss sum -- the anchor's 9 = 3^2 was |3*zeta|^2 in disguise.")
    log("  What survives of B415's mu_inf characterization: the measure-level flat "
        "magnitude |L(chi)| = 1/4 = the B413 mass DOES persist at level 27 "
        "(9/144 = 1/16 = (1/4)^2) on the nontrivial characters; what dies is the "
        "3^k Gauss-NORM growth (which would have needed |L| = 3^(k/2)/12, i.e. "
        "0.433 at k=3, contradicting flatness). The two readings coincide at the "
        "level-9 anchor and are separated for the first time here.")
log("")
log(f"VERDICT: {verdict}")

out = dict(
    cell="W2-148r",
    verdict=verdict,
    normalization="v_c = (zeta27^k + zeta27^-k)/12, classes {121,256,391} -> k "
                  f"{CK} -- re-proven in-cell (symbolic Q[z]/Phi_27 + all-20-prime "
                  "F_p multiset match + mpmath dps 50/100 + integrality: 12v is an "
                  "algebraic integer, v is not)",
    prediction_object="|12*L(chi)|^2, the Z/3-resolvent norm of the algebraic-"
                      "integer forms 12v of the innovation triple (level-9 anchor "
                      "re-derived: banked zeta9+zeta9^4+zeta9^7+3*zeta9^8 = "
                      "3*zeta9^-1, norm 9)",
    registered_prediction=PREDICTED,
    computed_exact=COMPUTED,
    resolvent_closed_form="12L = 3*zeta27^(-+1) symbolically; = 3*zeta27^t, "
                          f"t={next(iter(tset))[0]}, mod all 20 primes from raw data",
    circularity_addressed="old N=12-from-'-3' shown tautological (solve(-N^2/48=-3) "
                          "= [12]); counterfactual N=12*sqrt3 excluded: Q(zeta27) "
                          "has the unique quadratic subfield Q(sqrt-3) "
                          "((z^9-z^18)^2=-3, 2 primitive root mod 27)",
    d_sweep_reconciled="identify_1215_triple.py Method 2 swept Q(zeta9)+ numerators "
                       "over D (12 included); deg(2cos(2pi/27))=9 > 3 = "
                       "[Q(zeta9)+:Q] and the relative trace of y vanishes: the "
                       "negative is implied by the proven form and never tested "
                       "the denominator 12",
    freeze_lemma="resolvent = 3*zeta_{3^k}^-1 for k=2..7 symbolically (conditional "
                 "on the additive orbit persisting; data-proven at k=2,3)",
    flat_magnitude_survives="|L(chi_nontrivial)| = 1/4 at level 27 (= B413 mass); "
                            "L(chi_0) = 0 (mean-zero innovation)",
    gates_failed=FAIL,
)
with open(os.path.join(HERE, "output.json"), "w") as fh:
    json.dump(out, fh, indent=1)
log("wrote output.json")
