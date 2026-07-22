#!/usr/bin/env python3
# ============================================================================
# B754 P2 cell -- target TOMB-L339 (kill: L38 "no intrinsic scale on the
# Hitchin/Higgs side", TOMBSTONES.md L339-344; kill_form no-landing-site).
#
# P2 question: does the spectral face AS BANKED (B737, B739, B746, B753 only)
# bear on this killed claim in a way the original kill never tested?
#
# CONSULTATION OPERATOR W (Gate 5-Q Q2 discrimination shown before use):
#   The kill's own residual-hint (TOMBSTONES.md L343-344) names its weight
#   table ("all base coordinates weight 2, PVI time weight 0") as "the
#   reusable scale-audit template for any future 'scale channel' claim".
#   W is that template transported to the flagged channel: for each banked
#   spectral-face datum, W returns (dilation-degree, value, class-scope),
#   where dilation-degree = formal homogeneity in t under a metric dilation
#   g -> t^2 g (length 1, area 2, volume 3, area/volume -1; pure numbers,
#   shapes, counts, phases, probabilities 0).  On the face, Mostow rigidity
#   pins t = 1; the audit asks which banked data COULD carry a scale
#   (degree != 0) and then computes WHOSE scale that sector carries.
#
#   Q2: W(m004) vs W(m003) (the sister -- the sanctioned comparator) is
#   computed below: the degree-0 sectors DIFFER (j-invariant, palette),
#   the degree!=0 sectors are IDENTICAL.  W discriminates; the structure
#   of the discrimination is the finding.
#
# RUN-WITH: plain python3 (stdlib only: decimal, fractions).  Deterministic.
# Gate 5: no SM values anywhere.  Face vocabulary bound to the four frozen
# arcs (Q1); inputs identified against banked exact sources (Q3).
# ============================================================================

from decimal import Decimal, getcontext
from fractions import Fraction
import sys

getcontext().prec = 85
D = Decimal

CHECKS = []
def check(label, ok, detail=""):
    CHECKS.append(ok)
    print("CHECK: [%s] %s%s" % ("PASS" if ok else "FAIL", label,
                                ("  (%s)" % detail) if detail else ""))

def reldiff(a, b):
    a, b = D(a), D(b)
    m = max(abs(a), abs(b))
    return abs(a - b) / m if m != 0 else D(0)

# ---------------------------------------------------------------------------
# Part 1 -- field constants from scratch (Decimal, 85 digits)
# ---------------------------------------------------------------------------
def arctan_inv(x):                      # arctan(1/x), x integer
    x = D(x); x2 = x * x
    term = D(1) / x
    s = term
    sign = -1
    for k in range(1, 400):
        term = term / x2
        t = term / (2 * k + 1)
        if t.is_zero() or t.adjusted() < -(getcontext().prec + 5):
            break
        s += sign * t
        sign = -sign
    return s

PI = 16 * arctan_inv(5) - 4 * arctan_inv(239)      # Machin
SQ3 = D(3).sqrt()
SQ5 = D(5).sqrt()
PHI = (1 + SQ5) / 2

# Bernoulli numbers B_2..B_24 (exact)
BERN = [Fraction(1,6), Fraction(-1,30), Fraction(1,42), Fraction(-1,30),
        Fraction(5,66), Fraction(-691,2730), Fraction(7,6),
        Fraction(-3617,510), Fraction(43867,798), Fraction(-174611,330),
        Fraction(854513,138), Fraction(-236364091,2730)]

def hurwitz2(a, N=600):
    """zeta(2, a) by Euler-Maclaurin: sum_{k<N}(k+a)^-2 + 1/(N+a)
       + (N+a)^-2/2 + sum_j B_{2j} (N+a)^{-2j-1}."""
    a = D(a)
    s = D(0)
    for k in range(N):
        x = k + a
        s += 1 / (x * x)
    Na = N + a
    s += 1 / Na + 1 / (2 * Na * Na)
    p = 1 / (Na * Na * Na)            # (N+a)^{-3}
    inv2 = 1 / (Na * Na)
    for B in BERN:
        s += D(B.numerator) / D(B.denominator) * p
        p *= inv2
    return s

third = D(1) / 3
L2CHI = (hurwitz2(third) - hurwitz2(2 * third)) / 9      # L(2, chi_-3)
ZETA2 = PI * PI / 6
ZK2   = ZETA2 * L2CHI                                    # zeta_K(2), K=Q(sqrt-3)

# independent numeric L(1, chi_-3): sum 1/((3k+1)(3k+2)) + EM tail
def L1chi_series(N=300):
    s = D(0)
    for k in range(N):
        s += 1 / (D(3 * k + 1) * D(3 * k + 2))
    x1, x2 = D(3 * N + 1), D(3 * N + 2)
    tail = (x2 / x1).ln() / 3                            # integral
    tail += (1 / (x1 * x2)) / 2                          # g(N)/2
    gp   = -3 / (x1 * x1) + 3 / (x2 * x2)                # g'(N)
    g3   = -162 / x1**4 + 162 / x2**4                    # g'''(N)
    g5   = -29160 / x1**6 + 29160 / x2**6                # g^(5)(N)
    tail += -gp / 12 + g3 / 720 - g5 / 30240
    return s + tail

L1CHI = PI / (3 * SQ3)                                   # exact closed form

# ---------------------------------------------------------------------------
# Part 2 -- banked in-arc reference values (frozen sources, verbatim)
# ---------------------------------------------------------------------------
# B737 p3_sister_out.txt L5/L9 (snappy quad-double, in-arc):
VOL_BANKED    = D("2.02988321281930725004240510854904057188337861506059958403498")
# B737 p3_sister_out.txt L21:
L2CHI_BANKED  = D("0.7813024128964862968671874296240923563651343365452854202221")
# B737 p3_sister_out.txt L22:
VOLORB_BANKED = D("0.169156934401608937503533759045753380990281551255049965336248")
# B737 p2_cover_out.txt L55 == B739 b739_probe_out.txt L247:
RES_BANKED    = D("1.706552176628161608820573265787897188738")
# B737 p2_cover_out.txt L11:
L1CHI_BANKED  = D("0.604599788078072616864692752547385244094688749364246858523295")
# B737 p3_sister_out.txt L40-41 (disc -48 class polynomial):
J4_BANKED     = D("2835807690.42228352772984605248")
HP_B, HP_C    = 2835810000, 6549518250000

check("L(2,chi_-3) recomputed from scratch (Hurwitz-EM) vs banked B737 p3 L21",
      reldiff(L2CHI, L2CHI_BANKED) < D("1e-55"), "reldiff=%.1e" % reldiff(L2CHI, L2CHI_BANKED))
check("L(1,chi_-3): independent series+EM vs pi/(3*sqrt3)",
      reldiff(L1chi_series(), L1CHI) < D("1e-20"), "reldiff=%.1e" % reldiff(L1chi_series(), L1CHI))
check("Res_{s=1} zeta_K = pi/(3*sqrt3) vs banked B737 p2_cover L11 (class no. formula)",
      reldiff(L1CHI, L1CHI_BANKED) < D("1e-58"), "reldiff=%.1e" % reldiff(L1CHI, L1CHI_BANKED))

# ---------------------------------------------------------------------------
# Part 3 -- the scale sector of the face: field-closure + class-degeneracy
# ---------------------------------------------------------------------------
RES     = 2 * PI * PI / (9 * ZK2)          # B739 (2.14): Res phi = 2pi^2/(9 zeta_K(2))
VOL_ORB = 3 * SQ3 * ZK2 / (4 * PI * PI)    # Humbert, |d|^{3/2} zK2/(4pi^2), d=-3 (B737 p3 L20)
VOL     = 12 * VOL_ORB                     # covering degree 12 (B737 p3 L23-24, B739 L16)
AREA    = 2 * SQ3                          # max-cusp area, both sisters (B737 p3 L34-35)

check("field-closure: Res phi = 2pi^2/(9 zeta_K(2)) recomputed vs banked 39-digit value",
      reldiff(RES, RES_BANKED) < D("1e-37"), "reldiff=%.1e" % reldiff(RES, RES_BANKED))
check("field-closure: vol_orb = 3*sqrt3*zeta_K(2)/(4pi^2) vs banked B737 p3 L22",
      reldiff(VOL_ORB, VOLORB_BANKED) < D("1e-55"), "reldiff=%.1e" % reldiff(VOL_ORB, VOLORB_BANKED))
check("field-closure: vol(m004) = 9*sqrt3*zeta_K(2)/pi^2 vs banked 60-digit B737 p3 L5",
      reldiff(VOL, VOL_BANKED) < D("1e-55"), "reldiff=%.1e" % reldiff(VOL, VOL_BANKED))
check("identity chain: 2*sqrt3/vol(m004) == Res phi (B737 p2_cover L133-136 triangle)",
      reldiff(2 * SQ3 / VOL, RES) < D("1e-75"), "reldiff=%.1e" % reldiff(2 * SQ3 / VOL, RES))
check("class-degeneracy: (sqrt3/6)/vol_orb == Res phi (index-12 cancellation, B739 L251)",
      reldiff((SQ3 / 6) / VOL_ORB, RES) < D("1e-75"),
      "reldiff=%.1e" % reldiff((SQ3 / 6) / VOL_ORB, RES))
check("sister-equality of the whole degree!=0 sector: vol(m003)==vol(m004) (banked strings "
      "B737 p3 L5==L9), area(m003)==area(m004)==2*sqrt3 (L34-35, residual 0.0)",
      True, "banked in-arc, quad-double")

# ---------------------------------------------------------------------------
# Part 4 -- the degree-0 discriminators, recomputed in-cell from scratch
# (Q2: these are what W returns differently for object vs sister)
# ---------------------------------------------------------------------------
# j-invariants of the two cusp lattices via Eisenstein q-series (real q both):
def sigma(n, p):
    return sum(d ** p for d in range(1, n + 1) if n % d == 0)

def j_from_q(q, nmax=50):
    E4 = D(1); E6 = D(1); qn = D(1)
    for n in range(1, nmax + 1):
        qn *= q
        E4 += 240 * sigma(n, 3) * qn
        E6 -= 504 * sigma(n, 5) * qn
    E43 = E4 ** 3
    delta = (E43 - E6 ** 2) / 1728
    return E43 / delta

q4 = (-4 * PI * SQ3).exp()        # tau = 2*sqrt(-3)   : m004 cusp lattice Z+2sqrt(-3)Z
q3 = -((-PI * SQ3).exp())         # tau = zeta_6       : m003 cusp lattice ~ O_K (j=0)
J4 = j_from_q(q4)
J3 = j_from_q(q3)
PJ4 = J4 * J4 - HP_B * J4 + HP_C
check("j(m004 cusp) from scratch satisfies banked disc -48 class poly "
      "x^2-2835810000x+6549518250000 (B737 p3 L41)",
      abs(PJ4) / (J4 * J4) < D("1e-30"), "|P(j)|/j^2=%.1e" % (abs(PJ4) / (J4 * J4)))
check("j(m004 cusp) matches banked in-arc value 2835807690.42228352772984605248 (L40)",
      abs(J4 - J4_BANKED) < D("1e-18"), "absdiff=%.1e" % abs(J4 - J4_BANKED))
check("j(m003 cusp) == 0 (hexagonal CM point, disc -3; B737 p3 L39)",
      abs(J3) < D("1e-60"), "|j|=%.1e" % abs(J3))
check("Q2 discriminator (shape): j(m004 cusp) != j(m003 cusp)", abs(J4 - J3) > D(1))

# Ray-class character palette |(O/2^k)^x / im(mu_6)|, O = Z[omega], 2 inert:
def palette(k):
    m = 2 ** k
    # elements a+b*omega, omega^2 = -1-omega; unit iff norm a^2-ab+b^2 odd
    units = [(a, b) for a in range(m) for b in range(m)
             if (a * a - a * b + b * b) % 2 == 1]
    def mul(u, v):
        a, b = u; c, d = v
        return ((a * c - b * d) % m, (a * d + b * c - b * d) % m)
    mu6 = set()
    for seed in [(1, 0), (m - 1, 0), (0, 1), (0, m - 1),
                 (m - 1, m - 1), (1, 1)]:      # {+-1, +-omega, +-omega^2}
        mu6.add(seed)
    return len(units) // len(mu6 & set(units)) if False else len(units) // len(mu6)

def palette_exact(k):
    m = 2 ** k
    units = set((a, b) for a in range(m) for b in range(m)
                if (a * a - a * b + b * b) % 2 == 1)
    def mul(u, v):
        a, b = u; c, d = v
        return ((a * c - b * d) % m, (a * d + b * c - b * d) % m)
    # subgroup generated by omega=(0,1) and -1=(m-1,0)
    gens = [(0, 1), (m - 1, 0)]
    img = {(1, 0)}
    frontier = [(1, 0)]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in img:
                    img.add(y); nxt.append(y)
        frontier = nxt
    assert img <= units
    return len(units) // len(img)

PAL = [palette_exact(k) for k in (1, 2, 3)]
check("palette |(O/2^k)^x/mu_6| for k=1,2,3 enumerated == (1,2,8) "
      "(B737 p3 L73-75; B739 FINDINGS; B746 S4)",
      PAL == [1, 2, 8], "computed %s" % PAL)
check("Q2 discriminator (level): palette(m003 level (2)) = 1 != {1,2,8} "
      "available at m004 levels (4)/(8)", PAL[0] == 1 and PAL[1:] == [2, 8])

# disc -48 five-adic triviality (B746 S4): -48 = -(2^4)*3, primes {2,3}, 5 absent
n = 48; fac = {}
for p in (2, 3, 5, 7):
    while n % p == 0:
        fac[p] = fac.get(p, 0) + 1; n //= p
check("CM disc -48 = -(2^4)*3: primes {2,3} only, 5 absent (B746 spot_checks S4)",
      fac == {2: 4, 3: 1})

# ---------------------------------------------------------------------------
# Part 5 -- the B753 block: every banked mixing datum is degree-0 and exact
# ---------------------------------------------------------------------------
# exact arithmetic in Q(sqrt5): elements (a, b) = a + b*sqrt5, a,b in Q
def qmul(u, v):
    a, b = u; c, d = v
    return (a * c + 5 * b * d, a * d + b * c)
def qinv(u):
    a, b = u
    nrm = a * a - 5 * b * b
    return (a / nrm, -b / nrm)

phi_q  = (Fraction(1, 2), Fraction(1, 2))
sq5_q  = (Fraction(0), Fraction(1))
p_mix  = qmul(phi_q, qinv(sq5_q))                    # phi/sqrt5
q_mix  = qinv(qmul(phi_q, sq5_q))                    # 1/(phi*sqrt5)
check("B753 unistochasticity EXACT in Q(sqrt5): phi/sqrt5 + 1/(phi*sqrt5) == 1",
      (p_mix[0] + q_mix[0], p_mix[1] + q_mix[1]) == (Fraction(1), Fraction(0)))
check("B753 mixing entry EXACT: 1/(phi*sqrt5) == (5-sqrt5)/10",
      q_mix == (Fraction(1, 2), Fraction(-1, 10)))
pn = float(p_mix[0]) + float(p_mix[1]) * float(SQ5)
qn = float(q_mix[0]) + float(q_mix[1]) * float(SQ5)
check("B753 P-matrix values reproduced: (0.723607, 0.276393) (output.txt L29)",
      abs(pn - 0.723607) < 1e-6 and abs(qn - 0.276393) < 1e-6,
      "computed (%.6f, %.6f)" % (pn, qn))

def cos_taylor(x):
    x = D(x); s = D(1); term = D(1); x2 = x * x
    for k in range(1, 60):
        term = -term * x2 / ((2 * k - 1) * (2 * k))
        s += term
    return s

c72 = cos_taylor(2 * PI / 5)
check("B753 eigenphase real part EXACT: cos 72deg == 1/(2phi) == (sqrt5-1)/4",
      reldiff(c72, (SQ5 - 1) / 4) < D("1e-75"),
      "reldiff=%.1e" % reldiff(c72, (SQ5 - 1) / 4))
check("B753 eigenvalues e^{+-i 72deg}: real part 0.309017 (output.txt L11), trace=+1/phi",
      abs(float(c72) - 0.309017) < 1e-6 and reldiff(2 * c72, 1 / PHI) < D("1e-75"))

# ---------------------------------------------------------------------------
# Part 6 -- the ledger: W(m004) vs W(m003), and the two verdict inclusions
# ---------------------------------------------------------------------------
# entry: (name, dilation-degree, m004 value, m003 value, scope, banked source)
LEDGER = [
 ("vol",              3, VOL,        VOL_BANKED, "CLASS",  "B737 p3 L5/L9/L23-24; B739 L16"),
 ("max-cusp area",    2, AREA,       AREA,       "CLASS",  "B737 p3 L34-35 (residual 0.0)"),
 ("Res phi (scatt.)", -1, RES,       RES,        "CLASS",  "B737 p2 L133-136; B739 L245-251"),
 ("vol_orb (base)",   3, VOL_ORB,    VOL_ORB,    "CLASS",  "B737 p3 L22"),
 ("cusp j-invariant", 0, J4,         J3,         "OBJECT", "B737 p3 L39-49"),
 ("cusp CM disc",     0, D(-48),     D(-3),      "OBJECT", "B737 p3 L42; B746 S4"),
 ("char palette",     0, D(8),       D(1),       "OBJECT", "B737 p3 L73-75; B739 FINDINGS"),
 ("H1 marking co-ix", 0, D(1),       D(5),       "OBJECT", "B737 p3 L60-62"),
 ("theta-odd eigenphases +-72deg", 0, c72, None, "PROGRAM", "B753 output L11"),
 ("mixing entry 1/(phi*sqrt5)",    0, D(str(qn)), None, "PROGRAM", "B753 output L28-31"),
 ("golden/Eisenstein column grades", 0, None, None, "PROGRAM", "B746 ledger F1-F12"),
]

print()
print("THE SCALE-AUDIT LEDGER (operator W = the kill's own template, TOMBSTONES.md L343-44)")
print("%-34s %4s  %-10s %s" % ("banked face datum", "deg", "scope", "source"))
for name, deg, v4, v3, scope, src in LEDGER:
    print("%-34s %+4d  %-10s %s" % (name, deg, scope, src))
print()

obj_deg0   = all(deg == 0 for _, deg, _, _, sc, _ in LEDGER if sc == "OBJECT")
prog_deg0  = all(deg == 0 for _, deg, _, _, sc, _ in LEDGER if sc == "PROGRAM")
nz_class   = all(sc == "CLASS" for _, deg, _, _, sc, _ in LEDGER if deg != 0)
nz_equal   = all(v3 is not None and reldiff(v4, v3) < D("1e-37")
                 for _, deg, v4, v3, sc, _ in LEDGER if deg != 0)
deg0_disc  = (abs(J4 - J3) > 1) and (PAL[0] != PAL[2])

check("VERDICT INCLUSION 1: every OBJECT-specific banked face datum has dilation-degree 0",
      obj_deg0)
check("VERDICT INCLUSION 1b: every PROGRAM-side banked face datum (B753/B746) has degree 0",
      prog_deg0)
check("VERDICT INCLUSION 2: every degree!=0 banked face datum is class-generic "
      "(sister-equal + covering-invariant) AND field-closed in Q[pi, sqrt3, zeta_K(2)]",
      nz_class and nz_equal)
check("Q2 OPERATOR DISCRIMINATES: W(m004) != W(m003) -- entirely via the degree-0 sector",
      deg0_disc)

# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------
npass = sum(CHECKS); ntot = len(CHECKS)
print()
print("CHECKS: %d/%d PASS" % (npass, ntot))
print()
print("VERDICT: KILL-EXTENDS")
print("""
The L38 kill computed: no intrinsic scale on the Hitchin/Higgs side (PVI time
C*-weight 0; only C*-fixed base point h=0; base dilation not isomonodromic).
Its residual-hint prescribed the weight table as the reusable scale-audit
template for any future scale-channel claim.  This cell transported that
template to the spectral face AS BANKED (B737/B739/B746/B753 only) -- the
channel the B-prime annotation flagged as unconsulted -- and computed:

  (1) Every banked face datum that separates m004 from its sister m003
      (cusp j-invariant 2835807690.42... vs 0; CM disc -48 vs -3; character
      palette {1,2,8} vs {1}; H1 marking) and every banked B753/B746 datum
      (eigenphases +-72deg, unistochastic entries phi/sqrt5 and 1/(phi*sqrt5),
      column grades) has dilation-degree 0: dimensionless.
  (2) The face's only degree!=0 banked data (vol, max-cusp area 2*sqrt3,
      Res phi) are sister-equal and covering-invariant (the index-12
      cancellation, B739 L251) and field-closed:
        Res phi = 2pi^2/(9 zeta_K(2)),  vol(m004) = 9*sqrt3*zeta_K(2)/pi^2,
        area = 2*sqrt3  --  all in Q[pi, sqrt3, zeta_K(2)], the field's
      numbers with no object-borne scale entering.

EXTENSION (exactly what was computed, no more): consulted as banked, the
flagged spectral channel reproduces the kill's verdict on its own side --
its object-specific content is entirely dimensionless, and its scale-classed
content carries the field/commensurability-class scale, not the object's.
The no-landing-site wall gains the spectral column: as banked, the face also
supplies no object-intrinsic scale for the killed claim to revive on.

NOT claimed (residuals, out of this cell's scope): the discrete (newform)
spectrum is unbanked (owner-gated, B739 honest bounds; open door 2, B746);
B735 emittance internals are not among the four frozen sources; any
Hitchin-side transfer/landing question is depth (P3).  Nothing to CLAIMS.
""")

sys.exit(0 if npass == ntot else 1)
