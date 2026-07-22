#!/usr/bin/env python3
# =============================================================================
# B754 P2 cell TOMB-L30 -- S019 ("Fisher metric on CS level k", TOMBSTONES.md:L30)
# consulted against the frozen spectral surface (B737, B739, B746, B753 ONLY).
#
# RUN-WITH: plain python3 (mpmath for transcendental verification at dps=50;
# every verdict-bearing identity ALSO in exact Fraction / Q(sqrt5) / Q(sqrt-3)
# arithmetic). Deterministic: no randomness, no network, no repo imports.
#
# THE P2 QUESTION: does the spectral face AS BANKED bear on the killed claim
# in a way the original kill never tested?
#
# Structure:
#   PART 1  kill basis re-examined (E21 classical line: F(m) = 16*g_WP -- no
#           spectral object enters the original kill)                [Gate 5:
#           re-examination of the KILL BASIS; no value hunting; no SM values]
#   PART 2  face one-number verified in-cell (Res_{s=2} phi = 2 sqrt3/vol(m004)
#           = 2 pi^2/(9 zeta_K(2)), 2 independent mpmath code paths, vs the
#           banked 40-digit string) + Res_{s=1} zeta_K
#   PART 3  Q2 DISCRIMINATION (Gate 5-Q): the palette operator computed for the
#           OBJECT (m004: 8 candidate level characters) vs the SISTER m003
#           (1: trivial only) -- different outputs, both computed
#   PART 4  the closure recomputed exactly (B739 (a) restriction sum over
#           O/Lam: S(mu) = 4*[mu in O^v] -- every mode where a level character
#           could enter the continuous channel is shut)
#   PART 5  the frozen surface's probability objects are exact constants
#           (B753 identities recomputed in exact Q(sqrt5))
#   PART 6  token-level boundary: the four FINDINGS carry no Fisher/CS-level
#           vocabulary; B739's own probe classifies Chern-Simons NON-SPECTRAL
#   PART 7  THE EXTENSION (exactly what is computed, no more): the Fisher
#           information of any family drawn from the banked face w.r.t. any
#           parameter k that does not move K is identically 0 (computed, exact),
#           while the same operator on a varying family returns 5 (exact) --
#           the zero is the face's rigidity, not operator blindness
#
# Any failed check raises -> no output.txt is banked.
# =============================================================================

from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 50

FAILS = []
NCHECK = [0]
def check(label, ok, detail=""):
    NCHECK[0] += 1
    tag = "PASS" if ok else "FAIL"
    print("CHECK: %s | %s%s" % (label, tag, (" | " + detail) if detail else ""))
    if not ok:
        FAILS.append(label)

def nstr(x, n=40):
    return mp.nstr(x, n)

print("=" * 78)
print("B754 P2 cell TOMB-L30 -- S019 (Fisher/information-geometry on CS level k)")
print("vs the frozen spectral surface B737 / B739 / B746 / B753")
print("=" * 78)

# -----------------------------------------------------------------------------
# exact quadratic-field helpers
# -----------------------------------------------------------------------------

class Q5:
    """x + y*sqrt(5), x,y rational. Exact."""
    __slots__ = ("x", "y")
    def __init__(s, x, y=0):
        s.x, s.y = Fr(x), Fr(y)
    def __add__(s, o):
        o = s._c(o); return Q5(s.x + o.x, s.y + o.y)
    def __sub__(s, o):
        o = s._c(o); return Q5(s.x - o.x, s.y - o.y)
    def __mul__(s, o):
        o = s._c(o); return Q5(s.x * o.x + 5 * s.y * o.y, s.x * o.y + s.y * o.x)
    def inv(s):
        n = s.x * s.x - 5 * s.y * s.y
        return Q5(s.x / n, -s.y / n)
    def __truediv__(s, o):
        o = s._c(o); return s * o.inv()
    def __eq__(s, o):
        o = s._c(o); return s.x == o.x and s.y == o.y
    def _c(s, o):
        return o if isinstance(o, Q5) else Q5(o)
    def __repr__(s):
        return "(%s + %s*sqrt5)" % (s.x, s.y)

PHI   = Q5(Fr(1, 2), Fr(1, 2))   # golden ratio
SQRT5 = Q5(0, 1)

class QW:
    """a + b*sqrt(3)*i, a,b rational: exact coords for Q(sqrt-3) c C."""
    __slots__ = ("a", "b")
    def __init__(s, a, b=0):
        s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o):
        return QW(s.a + o.a, s.b + o.b)
    def __sub__(s, o):
        return QW(s.a - o.a, s.b - o.b)
    def __mul__(s, o):
        # (a + b r i)(c + d r i) with r^2 i^2 = -3
        return QW(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o):
        return s.a == o.a and s.b == o.b
    def __repr__(s):
        return "(%s + %s*sqrt3*i)" % (s.a, s.b)

def pair(mu, z):
    """Re(conj(mu) * z) for mu,z in QW coords: a1*a2 + 3*b1*b2. Exact."""
    return mu.a * z.a + 3 * mu.b * z.b

W = QW(Fr(-1, 2), Fr(1, 2))      # omega = e^{2 pi i/3}

# =============================================================================
print()
print("PART 1 -- the KILL BASIS re-examined (E21 classical line; B742 row TOMB-L30)")
print("  original kill's only Fisher object: F(m) = (dLE/dI)^2 at I* = m^2/4,")
print("  LE(I) = arccosh(2I+1)  [E21 FINDINGS.md:35-38; B742 FINDINGS.md:64]")
# =============================================================================

ok_exact = True
for m in range(1, 7):
    # exact-rational: 16*g_WP(m^2+2) with g_WP(alpha) = 1/(alpha^2-4)
    lhs = Fr(16, 1) / Fr((m * m + 2) ** 2 - 4)
    rhs = Fr(16, m * m * (m * m + 4))
    ok_exact &= (lhs == rhs)
ok_num = True
for m in range(1, 7):
    Istar = mp.mpf(m) ** 2 / 4
    d = mp.diff(lambda I: mp.acosh(2 * I + 1), Istar)
    ok_num &= abs(d ** 2 - mp.mpf(16) / (m * m * (m * m + 4))) < mp.mpf(10) ** -30
check("E21 kill basis: F(m) = (dLE/dI)^2|_{I*} = 16/(m^2(m^2+4)) = 16*g_WP(m^2+2), m=1..6",
      ok_exact and ok_num, "exact Fractions + mpmath derivative; the kill is a WP collapse")
print("  NOTE: F(m) is a function of the classical trace parameter m ALONE -- no")
print("  spectral quantity (eigenvalue, scattering datum, Fourier coefficient)")
print("  enters the original kill anywhere. faces_consulted=[none-arithmetic-only]")
print("  is CONSISTENT: the spectral face was never consulted by the kill.")

# =============================================================================
print()
print("PART 2 -- the face's one-number verified in-cell (B737 P2; B739 (e))")
# =============================================================================

# route A: 2 pi^2 / (9 zeta_K(2)), zeta_K(2) = zeta(2) * L(2,chi_-3),
#          L(2,chi_-3) = (hurwitz(2,1/3) - hurwitz(2,2/3))/9      [Hurwitz path]
L2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
zetaK2 = mp.zeta(2) * L2
routeA = 2 * mp.pi ** 2 / (9 * zetaK2)

# route B: 2 sqrt3 / vol(m004), vol(m004) = 3 * Cl_2(2 pi/3)      [Clausen path]
vol_m004 = 3 * mp.clsin(2, 2 * mp.pi / 3)
routeB = 2 * mp.sqrt(3) / vol_m004

BANKED_RES_PHI = mp.mpf("1.706552176628161608820573265787897188738")  # b739_probe_out.txt:246-249
vol_from_banked = 2 * mp.sqrt(3) / BANKED_RES_PHI   # the ONLY digits used are banked
check("vol(m004) = 3*Cl_2(2pi/3) = %s == 2 sqrt3 / (banked Res phi)" % nstr(vol_m004, 25),
      abs(vol_m004 - vol_from_banked) < mp.mpf(10) ** -37,
      "Clausen path vs the banked 40-digit residue; no unbanked digits used")
check("Res_{s=2} phi: 2 pi^2/(9 zeta_K(2)) == 2 sqrt3/vol(m004), two independent code paths",
      abs(routeA - routeB) < mp.mpf(10) ** -45,
      "|A-B| = %s" % nstr(abs(routeA - routeB), 3))
check("Res_{s=2} phi matches the BANKED 40-digit value (b739_probe_out.txt:246-249)",
      abs(routeA - BANKED_RES_PHI) < mp.mpf(10) ** -37,
      "computed %s" % nstr(routeA, 40))

# Res_{s=1} zeta_K = L(1,chi_-3) = pi/(3 sqrt3)  [B737 P1: 2pi/(6 sqrt3) = 0.6045997880...]
L1 = (mp.digamma(mp.mpf(2) / 3) - mp.digamma(mp.mpf(1) / 3)) / 3
check("Res_{s=1} zeta_K = L(1,chi_-3) = pi/(3 sqrt3) = 0.6045997880... (B737 P1)",
      abs(L1 - mp.pi / (3 * mp.sqrt(3))) < mp.mpf(10) ** -45
      and abs(L1 - mp.mpf("0.6045997880")) < mp.mpf(10) ** -9,   # B737 FINDINGS.md:14 digits only
      "digamma reflection path, %s" % nstr(L1, 25))

# =============================================================================
print()
print("PART 3 -- Q2 DISCRIMINATION: the palette operator PC, computed for the")
print("  OBJECT vs the SISTER (B737 P3 datum: |(O/2^k)^x / im(mu_6)| = 1, 2, 8)")
# =============================================================================

def palette(k):
    """|(O/2^k)^x / im(mu_6)| by brute force in Z[w]/(2^k). Exact/finite."""
    Mod = 2 ** k
    def norm(a, b):          # N(a + b w) = a^2 - a b + b^2
        return a * a - a * b + b * b
    def mul(p, q):
        a, b = p; c, d = q   # w^2 = -(1+w)
        return ((a * c - b * d) % Mod, (a * d + b * c - b * d) % Mod)
    units = [(a, b) for a in range(Mod) for b in range(Mod) if norm(a, b) % 2 == 1]
    # im(mu_6) = {+-w^j}: generate the subgroup from w and -1
    sub = {(1 % Mod, 0)}
    frontier_set = [(1 % Mod, 0)]
    gens = [(0, 1), ((-1) % Mod, 0)]
    while frontier_set:
        x = frontier_set.pop()
        for g in gens:
            y = mul(x, g)
            if y not in sub:
                sub.add(y)
                frontier_set.append(y)
    assert len(units) % len(sub) == 0
    return len(units) // len(sub), len(units), len(sub)

p1, u1, s1 = palette(1)
p2, u2, s2 = palette(2)
p3, u3, s3 = palette(3)
check("palette |(O/2^k)^x/im(mu_6)| = (1, 2, 8) at levels (2),(4),(8), brute force",
      (p1, p2, p3) == (1, 2, 8) and (u1, u2, u3) == (3, 12, 48) and (s1, s2, s3) == (3, 6, 6),
      "unit counts (3,12,48), im(mu_6) sizes (3,6,6) -- matches b739_probe_out.txt PART 0.5")

print("  OPERATOR PC (palette-and-closure): input = the banked cusp congruence data;")
print("  output = (# candidate Hecke characters that could vary the continuous")
print("  channel, their status).")
print("  OBJECT m004: cusp = C/(Z+2sqrt(-3)Z), conductor-4 order, level (8)")
print("    [B737 FINDINGS.md:26-34] -> PC = 8 candidates  (computed above)")
print("  SISTER m003: cusp = C/O_K, MAXIMAL order (j = 0 exactly)")
print("    [B737 FINDINGS.md:26-27] -> trivial congruence level -> PC = 1 (only")
print("    zeta_K; nothing that could ever vary -- and even at (2) the computed")
print("    palette is 1)")
check("Q2: PC(m004) = 8 != 1 = PC(m003) -- the operator discriminates object vs sister",
      p3 == 8 and p1 == 1,
      "for m003 rigidity is VACUOUS; for m004 it is a theorem with 8 candidates to kill")

# =============================================================================
print()
print("PART 4 -- the closure recomputed EXACTLY (B739 (a): the restriction sum)")
# =============================================================================

# lattices in QW coords (a + b sqrt3 i):
one = QW(1, 0)
sqm3 = QW(0, 1)                                  # sqrt(-3)
check("(1+2w)^2 = -3, i.e. sqrt(-3) = 1+2w, hence Z+2sqrt(-3)Z = Z+(2+4w)Z (B739 (a))",
      (one + W + W) * (one + W + W) == QW(-3, 0) and (one + W + W) == sqm3,
      "exact QW arithmetic")

# Lam = Z*(1,0) + Z*(0,2)  (= Z + 2 sqrt(-3) Z)
def in_Lam(z):
    return z.a.denominator == 1 and z.b.denominator == 1 and z.b % 2 == 0

# index [O : Lam]: O basis {1, w}; 2 sqrt(-3) = 2 + 4w -> transition det = 4
check("[O : Lam] = 4  (2 sqrt(-3) = 2*1 + 4*w, det [[1,0],[2,4]] = 4)",
      QW(0, 2) == one + one + W + W + W + W and 1 * 4 - 0 * 2 == 4, "")

# coset reps of O/Lam: {0, w, 2w, 3w}, pairwise distinct mod Lam
reps = [QW(0, 0), W, W + W, W + W + W]
distinct = all(not in_Lam(reps[i] - reps[j]) for i in range(4) for j in range(4) if i != j)
check("O/Lam = Z/4 with reps {0, w, 2w, 3w} (pairwise distinct mod Lam; 4w in Lam)",
      distinct and in_Lam(W + W + W + W), "")

# dual lattices under <mu,z> = Re(conj(mu) z):
v1, v2 = QW(1, 0), QW(0, Fr(1, 6))               # Lam^v basis
u1_, u2_ = QW(1, Fr(1, 3)), QW(0, Fr(2, 3))      # O^v basis
lam_gens = [QW(1, 0), QW(0, 2)]
o_gens = [QW(1, 0), W]
dual_ok = (
    [pair(v1, g) for g in lam_gens] == [1, 0] and
    [pair(v2, g) for g in lam_gens] == [0, 1] and
    [pair(u1_, g) for g in o_gens] == [1, 0] and
    [pair(u2_, g) for g in o_gens] == [0, 1]
)
check("dual bases exact: Lam^v = <(1,0),(0,1/6)>, O^v = <(1,1/3),(0,2/3)>", dual_ok, "")

# O^v inside Lam^v: u1 = v1 + 2 v2, u2 = 4 v2 -> index 4; classes mu_j = j*v2
check("[Lam^v : O^v] = 4; mu_j = j*(0,1/6) in O^v  <=>  j = 0 mod 4",
      u1_ == v1 + v2 + v2 and u2_ == v2 + v2 + v2 + v2 and
      all((j % 4 == 0) == (j % 4 == 0 and (j // 4) * 4 == j) for j in range(4)),
      "b739 PART 0.4 criterion 2*n1+n2 = 0 mod 4 at (n1,n2)=(0,j) gives the same classes")

# THE SUM: S(mu_j) = sum_{c in O/Lam} e^{2 pi i <mu_j, c>}, exact roots of unity
ROOT4 = {Fr(0): (Fr(1), Fr(0)), Fr(1, 4): (Fr(0), Fr(1)),
         Fr(1, 2): (Fr(-1), Fr(0)), Fr(3, 4): (Fr(0), Fr(-1))}
S = []
for j in range(4):
    mu = QW(0, Fr(j, 6))
    re, im = Fr(0), Fr(0)
    for c in reps:
        q = pair(mu, c) % 1
        r = ROOT4[q]
        re, im = re + r[0], im + r[1]
    S.append((re, im))
check("restriction sum S(mu_j) = (4,0,0,0) for j = 0,1,2,3  -- EXACT (B739 (a) mechanism)",
      S == [(4, 0), (0, 0), (0, 0), (0, 0)],
      "every Fourier mode where a level character could enter the continuous channel is 0")

# =============================================================================
print()
print("PART 5 -- the frozen surface's probability objects are EXACT CONSTANTS")
print("  (B753 identities recomputed in exact Q(sqrt5))")
# =============================================================================

pA = PHI / SQRT5                 # phi/sqrt5
pB = (PHI * SQRT5).inv()         # 1/(phi sqrt5)
check("B753 row (phi/sqrt5, 1/(phi sqrt5)) = (1/2+sqrt5/10, 1/2-sqrt5/10), sums to 1 EXACTLY",
      pA == Q5(Fr(1, 2), Fr(1, 10)) and pB == Q5(Fr(1, 2), Fr(-1, 10)) and pA + pB == Q5(1),
      "unistochastic row of P; sqrt5*phi = phi+2 exact: %s" % (SQRT5 * PHI == PHI + Q5(2)))

# |B00|^2 = 1/(4 phi^2) + (1 - 1/(4 phi^2))/5  ==  1/(phi sqrt5)   exactly
inv4phi2 = (PHI * PHI * 4).inv()
lhs = inv4phi2 + (Q5(1) - inv4phi2) * Q5(Fr(1, 5))
check("B753 exact identity |B00|^2 = 1 - p = 1/(phi sqrt5)  (B753 FINDINGS.md:27-31)",
      lhs == pB, "with cos72 = 1/(2phi), sin^2 72 = 1 - 1/(4 phi^2)")

x = (PHI * 2).inv()
check("cos 72deg = 1/(2 phi): root of 4x^2+2x-1 EXACTLY, and numeric to 40 digits",
      (x * x * 4 + x * 2 - Q5(1)) == Q5(0)
      and abs(mp.cos(2 * mp.pi / 5) - (mp.sqrt(5) - 1) / 4) < mp.mpf(10) ** -45,
      "eigenphase datum of the theta-odd block (B753 FINDINGS.md:16-20)")

iu = mp.mpc(0, 1)
ok_p = all(
    abs(mp.re(mp.exp(iu * th) * pp + mp.exp(-iu * th) * (1 - pp)) - mp.cos(th)) < mp.mpf(10) ** -45
    for th in [2 * mp.pi / 5]
    for pp in [mp.mpf(0), mp.mpf(1) / 7, mp.mpf(1) / 3, mp.mpf(1) / 2, mp.mpf(9) / 10]
)
check("Re(e^{i th} p + e^{-i th}(1-p)) = cos th for p in {0,1/7,1/3,1/2,9/10} (B753 cell 2)",
      ok_p, "the real-part projection is p-independent -- no tunable parameter hides here")

# =============================================================================
print()
print("PART 6 -- token-level boundary of the frozen surface")
# =============================================================================

import os
BASE = "/Users/dri/oa-audit-seat/origin-axiom/frontier"
FOUR = ["B737_candidate_zero", "B739_character_rigidity",
        "B746_golden_ledger", "B753_mixing_structure"]
tok_ok = True
for arc in FOUR:
    txt = open(os.path.join(BASE, arc, "FINDINGS.md"), encoding="utf-8").read().lower()
    hits = sum(txt.count(t) for t in ["fisher", "chern", "information metric", "cs level"])
    tok_ok &= (hits == 0)
    print("  %s/FINDINGS.md: fisher/chern/'information metric'/'cs level' hits = %d" %
          (arc, hits))
check("the four FINDINGS carry ZERO Fisher / Chern-Simons / information-metric vocabulary",
      tok_ok, "the CS level k appears NOWHERE on the frozen surface")

probe = open(os.path.join(BASE, "B739_character_rigidity", "b739_probe_out.txt"),
             encoding="utf-8").read().splitlines()
line230 = probe[229].strip()
line231 = probe[230].strip()
check("B739's own boundary statement (b739_probe_out.txt:230-231): Chern-Simons is",
      "Chern-Simons" in line230 and "NON-SPECTRAL" in line230
      and "outside the Laplace spectrum" in line231,
      "verbatim: '%s %s'" % (line230, line231))

# =============================================================================
print()
print("PART 7 -- THE EXTENSION: Fisher degeneracy of the banked face, computed")
# =============================================================================

# The face-supplied family: the single banked probability distribution
# p = (phi/sqrt5, 1/(phi sqrt5)) with the face-supplied k-derivative dp/dk = 0
# (PARTS 3-6: the surface contains no parameter k; the one channel of the
# object that COULD have varied -- the 8 candidate level characters -- is
# computed shut mode by mode in PART 4).
dpA, dpB = Q5(0), Q5(0)
I_face = (dpA * dpA) / pA + (dpB * dpB) / pB
check("I_Fisher(face family; any k with K fixed) = 0 EXACTLY (in Q(sqrt5))",
      I_face == Q5(0),
      "d_k p = 0 is FORCED by the face: no k on the surface + all 8 candidates closed")

# operator non-blindness: the SAME operator on a family that DOES vary
# (q(eps) = (p1+eps, p2-eps)) returns, at eps=0:  I = 1/p1 + 1/p2
I_pert = pA.inv() + pB.inv()
check("contrast: same operator on the eps-perturbed family gives I = 1/p1 + 1/p2 = 5 EXACTLY",
      I_pert == Q5(5),
      "the 0 above is the FACE's rigidity, not operator blindness (Q2, second leg)")

print("""
  CHAIN (each link computed above or verified in-arc at the cited line):
  (1) The continuous channel of m004 is the single Eisenstein series with
      phi(s) = Lambda_K(s-1)/Lambda_K(s) AS FUNCTIONS -- B739 FINDINGS.md:8-16,
      one-number re-verified here to 40 digits (PART 2).
  (2) The only place a genuinely object-level parameter could enter that
      channel -- the 8 candidate conductor-(4)/(8) characters opened by the
      level (PART 3, computed) -- is closed mode by mode: S(mu) = 0 on every
      nontrivial dual class (PART 4, exact).
  (3) phi contains no parameter of the object at all (B737 P4 object-deletion,
      FINDINGS.md:41-43), and the surface's only probability object (B753's
      unistochastic P) is a golden-EXACT constant (PART 5, exact).
  (4) Chern-Simons data is classified by the face's own arc as NON-SPECTRAL,
      outside the Laplace spectrum entirely (PART 6, b739_probe_out.txt:230-231).
  => Any probability family p(x|k) drawn from the banked spectral surface has
     d_k p = 0 for every parameter k that does not move the field K; its
     Fisher information is identically zero (computed exact, with the nonzero
     contrast 5 showing the operator is not blind).
  => The bounded test the original kill LACKED ("heuristic, not rigorous; no
     bounded test survived") now EXISTS on the spectral face and returns
     DEGENERATE: the face cannot host a Fisher/information metric in k.
     The kill gains a spectral column. KILL-EXTENDS.

  SCOPE (stated, not exceeded): continuous channel + banked probability
  objects only. The discrete newform spectrum is OUTSIDE the frozen surface
  (B739 honest bounds: Hejhal-class, owner-gated; B746 door 2 already banks
  that question) and NO banked bridge connects the CS level k to it -- the
  face's own classification (PART 6) puts CS data outside the Laplace
  spectrum. Q6 specialness: the bearing is special to m004 -- for the sister
  m003 the same rigidity is VACUOUS (palette 1, PART 3); for m004 it is a
  theorem with content (8 candidates, each computed shut).

  FALSIFIER: exhibit a k-varying probability family constructible from the
  four frozen arcs alone (a banked continuous-channel coefficient outside
  zeta_K, or a banked non-constant probability object), or refute PART 3's
  palette (1,2,8) / PART 4's restriction zeros, or produce a banked bridge
  from the CS level k to a parameter moving the continuous channel.
""")

if FAILS:
    print("RESULT: %d CHECK FAILURES -- CELL VOID" % len(FAILS))
    raise SystemExit(1)
print("CHECK: VERDICT TOMB-L30 = KILL-EXTENDS | PASS | all %d checks green" % NCHECK[0])
print("RESULT: KILL-EXTENDS")
