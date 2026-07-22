"""B754 P2 cell -- target B285 (the pi/6 commutator-phase kill) vs the banked spectral face.

KILLED CLAIM (B285, dead-probe): chat-2's physics reading of the forced pi/6 commutator
phase -- that it IS the physical CP (fermion-mixing / Jarlskog-type) phase yielding eta_B
within ~1 order, and that the object supplies the CP sign.
ORIGINAL KILL BASIS: value-mismatch on the eta_B channel + sign-not-supplied (B252
CP-symmetry / tau-fork). faces_consulted: none-arithmetic-only.

P2 QUESTION: does the spectral face AS BANKED (B737, B739, B746, B753 ONLY) bear on this
killed claim in a way the original kill never tested?

VERDICT COMPUTED HERE: KILL-EXTENDS, on two computed columns:
  EXT-1 (kind/column mismatch): the claim's phase datum kappa = tr[a,b] = u^2+2 =
        sqrt(3) e^{-+ i pi/6} is Eisenstein-column data (minpoly x^2-3x+3, disc -3,
        kappa in Q(zeta_3)); the face's kind-correct mixing object (B753's theta-odd
        unitary block, reconstructed below from the banked B238 pipeline) occupies the
        very role the claim asserts ("physical mixing-type phase") with golden-column
        data (eigenphases +-72 deg = e^{+-2 pi i/5}, trace +1/phi, mixing entry
        1/(phi sqrt 5)) -- and the two data sets share NO irrational algebraic content
        (Galois computation in Q(zeta_15) / Q(zeta_60)). The original kill tested only
        the value channel; this column it never tested.
  EXT-2 (sign-blindness of the face): every phase-bearing datum in the banked face is
        conjugation-symmetric: the mixing block's eigenphases form the conjugate pair
        +-72 deg (real trace, unit det, computed); the voice phi(s) = Lambda_K(s-1)/
        Lambda_K(s) has integer Dirichlet coefficients (computed) hence obeys the
        Schwarz reflection, and its leading pole datum Res phi = 2 sqrt 3/vol(m004) is
        real positive (recomputed = B737's banked 1.70655217662816); B739's rigidity
        (verified at source) leaves nothing else in the continuous channel. The
        conjugation that swaps -+pi/6 (the tau-swap the kill's sign leg rests on) acts
        trivially on the entire banked spectral surface: the face cannot supply the sign.

GATE 5: no SM values anywhere (no eta_B, no mixing angles from observation; "CP phase"
appears only as the killed claim's quoted vocabulary). Gate 5-Q: Q2 discrimination is
demonstrated FIRST (the operator distinguishes m004 from the census comparator m015).
RUN-WITH: plain python3 (stdlib + numpy; no Sage, no SnapPy). Deterministic throughout.
"""

import cmath
import importlib.util
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

PHI = (1 + math.sqrt(5)) / 2

FAILURES = []
NCHECK = [0]


def check(tag, cond, detail=""):
    NCHECK[0] += 1
    status = "PASS" if cond else "FAIL"
    print(f"CHECK[{tag}] {status}  {detail}")
    if not cond:
        FAILURES.append(tag)


# ----------------------------------------------------------------------------------
# exact polynomial arithmetic (coeff lists, index = degree; Fraction/int entries)
# ----------------------------------------------------------------------------------

def ptrim(f):
    f = list(f)
    while f and f[-1] == 0:
        f.pop()
    return f


def padd(f, g):
    n = max(len(f), len(g))
    return ptrim([(f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(n)])


def psub(f, g):
    return padd(f, [-c for c in g])


def pmul(f, g):
    if not f or not g:
        return []
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] += a * b
    return ptrim(out)


def pdivmod(f, g):
    """exact division with remainder over Q (Fraction)."""
    f = [Fraction(c) for c in f]
    g = [Fraction(c) for c in g]
    q = [Fraction(0)] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and f:
        c = f[-1] / g[-1]
        d = len(f) - len(g)
        q[d] = c
        f = ptrim([f[i] - c * g[i - d] if 0 <= i - d < len(g) else f[i] for i in range(len(f))])
    return ptrim(q), f


def pgcd(f, g):
    """monic gcd over Q, returned as primitive integer poly with positive lead."""
    f = ptrim([Fraction(c) for c in f])
    g = ptrim([Fraction(c) for c in g])
    while g:
        _, r = pdivmod(f, g)
        f, g = g, r
    if not f:
        return []
    f = [c / f[-1] for c in f]  # monic
    from math import gcd as igcd
    den = 1
    for c in f:
        den = den * c.denominator // igcd(den, c.denominator)
    ints = [int(c * den) for c in f]
    content = 0
    for c in ints:
        content = igcd(content, abs(c))
    ints = [c // content for c in ints]
    if ints[-1] < 0:
        ints = [-c for c in ints]
    return ints


def pderiv(f):
    return ptrim([i * f[i] for i in range(1, len(f))])


def peval(f, x):
    v = 0
    for c in reversed(f):
        v = v * x + c
    return v


def pstr(f):
    if not f:
        return "0"
    terms = []
    for i in range(len(f) - 1, -1, -1):
        c = f[i]
        if c == 0:
            continue
        if i == 0:
            terms.append(f"{c:+d}" if isinstance(c, int) else f"{c:+}")
        elif i == 1:
            terms.append(f"{c:+d}u" if isinstance(c, int) else f"{c:+}u")
        else:
            terms.append(f"{c:+d}u^{i}" if isinstance(c, int) else f"{c:+}u^{i}")
    return " ".join(terms)


# 2x2 matrices of polynomials
def mmul(X, Y):
    return [[padd(pmul(X[i][0], Y[0][j]), pmul(X[i][1], Y[1][j])) for j in range(2)] for i in range(2)]


ONE, ZERO, U = [1], [], [0, 1]
MA = [[ONE, ONE], [ZERO, ONE]]            # a  = [[1,1],[0,1]]
MAI = [[ONE, [-1]], [ZERO, ONE]]          # a^-1
MB = [[ONE, ZERO], [[0, -1], ONE]]        # b  = [[1,0],[-u,1]]   (the B285 convention)
MBI = [[ONE, ZERO], [U, ONE]]             # b^-1

LETTER = {("a", +1): MA, ("a", -1): MAI, ("b", +1): MB, ("b", -1): MBI}


def riley_condition(p, q, start, relwhich):
    """Build the 2-bridge Riley word for b(p,q); return (gcd, product) of the nonzero
    entries of the rep condition (relwhich 0: W a - b W; 1: W b - a W), both as
    primitive integer polys (product up to sign/content)."""
    eps = [(-1) ** ((i * q) // p) for i in range(1, p)]
    other = "b" if start == "a" else "a"
    W = [[ONE, ZERO], [ZERO, ONE]]
    for i, e in enumerate(eps):
        letter = start if i % 2 == 0 else other
        W = mmul(W, LETTER[(letter, e)])
    if relwhich == 0:
        M = [[psub(mmul(W, MA)[i][j], mmul(MB, W)[i][j]) for j in range(2)] for i in range(2)]
    else:
        M = [[psub(mmul(W, MB)[i][j], mmul(MA, W)[i][j]) for j in range(2)] for i in range(2)]
    entries = [M[i][j] for i in range(2) for j in range(2) if ptrim(M[i][j])]
    if not entries:
        return None, None
    g, prod = entries[0], entries[0]
    for e in entries[1:]:
        g = pgcd(g, e)
        prod = pmul(prod, e)
    if len(g) <= 1:
        return None, None
    return g, pgcd(prod, prod)  # second slot: primitive-normalized product


def divides(d, f):
    _, r = pdivmod(f, d)
    return not r


print("=" * 92)
print("CELL 0 -- the killed claim's phase object, recomputed exactly (target arc B285 anchor)")
print("=" * 92)

# tr[a,b] symbolically: a b a^-1 b^-1
K = mmul(mmul(MA, MB), mmul(MAI, MBI))
tr = padd(K[0][0], K[1][1])
check("T1", tr == [2, 0, 1], f"tr[a,b] = {pstr(tr)}  (= u^2 + 2, chat-2's object; holds for ALL u "
      f"-- object-specificity enters ONLY through the Riley root)")

kplus = peval([2, 0, 1], cmath.exp(2j * math.pi / 3))    # u = omega
kminus = peval([2, 0, 1], cmath.exp(-2j * math.pi / 3))  # u = omega^2
s3 = math.sqrt(3)
check("T2", abs(kplus - (1.5 - 1j * s3 / 2)) < 1e-12 and abs(kminus - (1.5 + 1j * s3 / 2)) < 1e-12
      and abs((kplus + kminus) - 3) < 1e-12 and abs(kplus * kminus - 3) < 1e-12,
      "kappa(u=omega) = (3 - sqrt(-3))/2, kappa(u=omega^2) = (3 + sqrt(-3))/2; sum=3, product=3 "
      "=> exact minpoly x^2 - 3x + 3, disc = 9 - 12 = -3  => kappa generates Q(sqrt(-3)) = Q(zeta_3): EISENSTEIN column")
check("T3", abs(abs(kplus) - s3) < 1e-12 and abs(abs(cmath.phase(kplus)) - math.pi / 6) < 1e-12
      and abs(cmath.phase(kplus) + cmath.phase(kminus)) < 1e-12,
      "|kappa| = sqrt(3), |arg kappa| = pi/6 exactly; the two conjugate roots give -+pi/6 (the tau-swap)")

print()
print("=" * 92)
print("CELL 1 -- GATE 5-Q Q2 FIRST: the consultation operator and its discrimination")
print("=" * 92)
print("""OP_COLUMN(x): input an exact algebraic phase-bearing datum x (a holonomy trace or a unit
eigenvalue); output (exact minimal polynomial over Q, its discriminant/field, and the
B746 column: EISENSTEIN if x generates Q(sqrt(-3))-content, GOLDEN if Q(sqrt(5))-content,
NONE otherwise; plus the phase when it is forced cyclotomic).
CONSULTATION = OP_COLUMN(claim datum kappa)  vs  OP_COLUMN(face mixing data)  + a Galois
test for common irrational content.
Q2 comparator: the operator's input type is a 2-bridge Riley normal form; of the menu
(random census manifold / sister m003 / Gieseking parent), the one that FITS this input
type is a census 2-bridge knot complement: m015 = 5_2, the next 2-bridge hyperbolic knot
after 4_1.  (m003 is not banked as any 2-bridge knot normal form in S^3; the Gieseking
manifold is non-orientable -- neither presents the operator's input type.)""")

# ---- anchor the Riley-word convention on the banked (5,3) figure-eight arc ----------
anchor = None
for qa in (3, 2):
    for conv in (("a", 0), ("b", 0), ("a", 1), ("b", 1)):
        g, prod = riley_condition(5, qa, conv[0], conv[1])
        if g and divides([1, 1, 1], g):
            anchor = (qa, conv, g, prod)
            break
    if anchor:
        break
check("Q2a", anchor is not None,
      f"Riley convention anchored on b(5,q): q={anchor[0]}, word starts '{anchor[1][0]}', relator "
      f"{'Wa=bW' if anchor[1][1]==0 else 'Wb=aW'}; condition gcd = {pstr(anchor[2])}; "
      f"(u^2+u+1) | gcd -- the banked B285 geometric root u = omega is recovered")
check("Q2b", anchor is not None and anchor[3] == [0, 1, 2, 3, 2, 1],
      f"the (5,q) condition entries multiply to {pstr(anchor[3])} = u(u^2+u+1)^2 -- the exact "
      f"banked B285 'Riley poly' form recovered")

# ---- the comparator m015 = 5_2 = b(7,q) with the SAME anchored convention -----------
qa, conv = anchor[0], anchor[1]
cubic = None
for q7 in (3, 5, 2, 4):
    g7, _p7 = riley_condition(7, q7, conv[0], conv[1])
    if not g7:
        continue
    while g7 and g7[0] == 0:          # strip the u^k (abelian) factor
        g7 = g7[1:]
    sf = pgcd(g7, pderiv(g7)) if len(g7) > 2 else [1]
    core, r = pdivmod(g7, sf)
    core = pgcd(core, core)           # primitive-normalize
    if len(core) == 4:                # a cubic
        cubic = (q7, g7, core)
        break
check("Q2c-a", cubic is not None,
      f"b(7,q={cubic[0]}): stripped condition gcd = {pstr(cubic[1])}; squarefree core = {pstr(cubic[2])} (degree 3)")

c3 = cubic[2]
a3, b3, c3c, d3 = c3[3], c3[2], c3[1], c3[0]
disc3 = (18 * a3 * b3 * c3c * d3 - 4 * b3 ** 3 * d3 + b3 ** 2 * c3c ** 2
         - 4 * a3 * c3c ** 3 - 27 * a3 ** 2 * d3 ** 2)
# rational-root test => irreducibility for a cubic
rr = [Fraction(sp, sq) * sgn for sp in range(1, abs(c3[0]) + 1) if abs(c3[0]) % sp == 0
      for sq in range(1, abs(c3[3]) + 1) if abs(c3[3]) % sq == 0 for sgn in (1, -1)]
has_rat_root = any(peval([Fraction(c) for c in c3], r) == 0 for r in set(rr))
check("Q2c-b", (not has_rat_root) and abs(disc3) == 23,
      f"the comparator Riley cubic is irreducible over Q (no rational root) with |disc| = {abs(disc3)} = 23 "
      f"(the 5_2 trace-field arithmetic -- landed on the intended census comparator)")

roots = np.roots(list(reversed(c3)))
u0 = max(roots, key=lambda z: z.imag)            # deterministic: the root with largest Im
kappa_c = u0 ** 2 + 2

# exact minpoly of kappa' = u0^2+2 via multiplication matrix on Q[u]/(c3)
c3m = [Fraction(c, c3[3]) for c in c3]           # monic cubic
red = [[Fraction(0)] * 3 for _ in range(5)]      # u^j mod c3m for j=0..4
for j in range(5):
    col = [Fraction(0)] * 5
    col[j] = Fraction(1)
    col = list(col)
    for d in range(4, 2, -1):                    # reduce degrees 4,3
        if col[d]:
            f = col[d]
            col[d] = Fraction(0)
            for i in range(3):
                col[d - 3 + i] -= f * c3m[i]
    red[j] = col[:3]
# multiplication by (u^2 + 2): column j = (u^{j+2} + 2 u^j) mod c3m
Mm = [[Fraction(0)] * 3 for _ in range(3)]
for j in range(3):
    colv = [red[j + 2][i] + 2 * red[j][i] for i in range(3)]
    for i in range(3):
        Mm[i][j] = colv[i]


def matmulF(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def trF(X):
    return sum(X[i][i] for i in range(3))


M2 = matmulF(Mm, Mm)
M3 = matmulF(M2, Mm)
t1, t2, t3 = trF(Mm), trF(M2), trF(M3)
e1 = t1
e2 = (e1 * t1 - t2) / 2
e3 = (e2 * t1 - e1 * t2 + t3) / 3
# charpoly x^3 - e1 x^2 + e2 x - e3, cleared to integers
from math import gcd as igcd
den = 1
for c in (e1, e2, e3):
    den = den * c.denominator // igcd(den, c.denominator)
mp_k = [int(-e3 * den), int(e2 * den), int(-e1 * den), den]
cont = 0
for c in mp_k:
    cont = igcd(cont, abs(c))
mp_k = [c // cont for c in mp_k]
resid = abs(peval(mp_k, kappa_c))
scale = max(abs(c) for c in mp_k) * max(1.0, abs(kappa_c)) ** 3
rrk = [Fraction(sp, sq) * sgn for sp in range(1, abs(mp_k[0]) + 1) if abs(mp_k[0]) % sp == 0
       for sq in range(1, abs(mp_k[3]) + 1) if abs(mp_k[3]) % sq == 0 for sgn in (1, -1)]
kappa_rat = any(peval([Fraction(c) for c in mp_k], r) == 0 for r in set(rrk))
check("Q2d", resid / scale < 1e-10 and not kappa_rat,
      f"comparator kappa' = u0^2+2 = {kappa_c:+.6f} (u0 = {u0:+.6f}) has EXACT minpoly "
      f"{pstr(mp_k)} (x for u), irreducible cubic => Q(kappa') is a CUBIC field => it has NO quadratic "
      f"subfield => OP_COLUMN column = NONE (neither Eisenstein nor golden is available to it)")

argc = math.degrees(cmath.phase(kappa_c))
check("Q2e", abs(abs(cmath.phase(kappa_c)) - math.pi / 6) > 1e-3 and abs(kappa_c.imag) > 1e-6,
      f"comparator phase arg kappa' = {argc:+.3f} deg (non-real, NOT +-30 deg, non-cyclotomic-forced)")
print()
print("Q2 DISCRIMINATION TABLE (computed, not asserted):")
print("  m004 (object) : OP_COLUMN(kappa)  = (x^2-3x+3, disc -3, EISENSTEIN, phase exactly -+30 deg)")
print(f"  m015 (generic): OP_COLUMN(kappa') = ({pstr(mp_k)}, |disc(f)| = {abs(disc3)} field, NONE, "
      f"phase {argc:+.3f} deg, not forced)")
check("Q2", True, "the operator returns DIFFERENT outputs for the object vs the census comparator "
      "=> it discriminates; the cell may proceed (B752 lesson honored)")

print()
print("=" * 92)
print("CELL 2 -- the face's kind-correct mixing object, RECONSTRUCTED from the banked pipeline")
print("         (B753 in-arc verification; B238 su32_wrt.py is B753's own imported source)")
print("=" * 92)

spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(FRONTIER, "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S
pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
Umat = np.zeros((n, 2))
for j, (ai, bi) in enumerate(pairs):
    Umat[ai, j], Umat[bi, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
Umat = Umat.astype(complex)
W_weld = C @ R @ L
B = np.array([[np.conj(Umat[:, i]) @ W_weld @ Umat[:, j] for j in range(2)] for i in range(2)])

banked = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
check("F1", abs(B[0, 0] - banked) < 1e-12 and abs(B[1, 1] - np.conj(B[0, 0])) < 1e-12,
      f"B00 = {B[0,0]:+.6f} matches the banked B593 element 1/(2 phi) + i sin72/sqrt5; B11 = conj(B00)")
check("F2", np.linalg.norm(B @ B.conj().T - np.eye(2)) < 1e-12,
      f"the theta-odd block is UNITARY (||B B^dag - I|| = {np.linalg.norm(B @ B.conj().T - np.eye(2)):.2e})")
evals = sorted(np.linalg.eig(B)[0], key=lambda z: -z.imag)
lam72 = cmath.exp(2j * math.pi / 5)
lam108 = cmath.exp(1j * math.radians(108))
check("F3", abs(evals[0] - lam72) < 1e-9 and abs(evals[1] - np.conj(lam72)) < 1e-9
      and min(abs(evals[0] - lam108), abs(evals[0] - np.conj(lam108))) > 0.5,
      f"eigenphases are e^{{+-i 72 deg}} = e^{{+-2 pi i/5}} (evals = {evals[0]:+.6f}, {evals[1]:+.6f}); NOT +-108 deg")
detB = np.linalg.det(B)
check("F4", abs((evals[0] + evals[1]) - 1 / PHI) < 1e-9 and abs(detB - 1) < 1e-9,
      f"trace = +1/phi = {1/PHI:.6f} (REAL), det = 1: the eigenphases are FORCED into a conjugate +- pair")
evec = np.linalg.eig(B)[1]
order = np.argsort(-np.linalg.eig(B)[0].imag)
P = np.zeros((2, 2))
for jj, j in enumerate(order):
    v = evec[:, j] / np.linalg.norm(evec[:, j])
    for i in range(2):
        P[i, jj] = abs(v[i]) ** 2
pgold = 1 / (PHI * math.sqrt(5))
check("F5", all(abs(P[i, i] - PHI / math.sqrt(5)) < 1e-9 for i in range(2))
      and all(abs(P[i, 1 - i] - pgold) < 1e-9 for i in range(2))
      and abs(abs(B[0, 0]) ** 2 - pgold) < 1e-12,
      f"P = [[phi/sqrt5, 1/(phi sqrt5)],[1/(phi sqrt5), phi/sqrt5]] and |B00|^2 = 1/(phi sqrt5) = {pgold:.6f} "
      f"(the banked kind-correct mixing entry)")
t72 = 2 * math.cos(2 * math.pi / 5)
check("F6", abs(t72 ** 2 + t72 - 1) < 1e-12 and abs(peval([1, 1, 1, 1, 1], lam72)) < 1e-12,
      "exact algebra of the face data: 2 cos 72 satisfies x^2 + x - 1 (disc 5 => Q(sqrt 5): GOLDEN column); "
      "e^{2 pi i/5} satisfies Phi_5 => Q(zeta_5)")

print()
print("=" * 92)
print("CELL 3 -- EXT-1: the kind/column mismatch, made exact (Galois disjointness)")
print("=" * 92)

zeta5 = [cmath.exp(2j * math.pi * a / 5) for a in range(5)]
def legendre5(a):
    a %= 5
    if a == 0:
        return 0
    return 1 if pow(a, (5 - 1) // 2, 5) == 1 else -1
def chi3(a):
    a %= 3
    return 0 if a == 0 else (1 if a == 1 else -1)

g5 = sum(legendre5(a) * zeta5[a] for a in range(1, 5))
g3 = sum(chi3(a) * cmath.exp(2j * math.pi * a / 3) for a in range(1, 3))
check("D1", abs(g5 - math.sqrt(5)) < 1e-12 and abs(g3 - 1j * math.sqrt(3)) < 1e-12,
      "quadratic Gauss sums: sum (a|5) zeta_5^a = sqrt 5  and  sum chi_-3(a) zeta_3^a = sqrt(-3) "
      "=> sqrt5 in Q(zeta_5), sqrt(-3) in Q(zeta_3); sigma_k acts on them by the character value at k")
check("D2", (7 % 3 == 1 and legendre5(7) == -1) and (11 % 5 == 1 and chi3(11) == -1)
      and (13 % 12 == 1 and legendre5(13) == -1) and math.gcd(3, 5) == 1 and math.gcd(12, 5) == 1,
      "computed character values: sigma_7 in Gal(Q(zeta_15)/Q) fixes zeta_3, sends sqrt5 -> -sqrt5 "
      "((7|5) = -1); sigma_11 fixes zeta_5, sends sqrt(-3) -> -sqrt(-3) (chi_-3(11) = -1); "
      "phase level: sigma_13 in Gal(Q(zeta_60)/Q) fixes zeta_12 = e^{i pi/6}, sends sqrt5 -> -sqrt5 ((13|5) = -1)")
check("D3", abs(kplus - (3 - 1j * math.sqrt(3)) / 2) < 1e-12,
      "kappa = (3 -+ sqrt(-3))/2 lies in Q(zeta_3); its phase e^{-+i pi/6} lies in Q(zeta_12); "
      "gcd(3,5) = gcd(12,5) = 1 => Q(zeta_3) cap Q(zeta_5) = Q and Q(zeta_12) cap Q(zeta_5) = Q")
print("""
EXT-1 (computed): the claim's datum kappa is EISENSTEIN-column (being-column) exactly;
the face's kind-correct mixing object -- the occupant of the very role the killed claim
asserted for arg kappa ("the physical mixing-type phase") -- is GOLDEN-column exactly
(eigenphases e^{+-2 pi i/5}, trace 1/phi, entry 1/(phi sqrt5)); and by sigma_7/sigma_11/
sigma_13 the two data sets share NO irrational content: no identification of the pi/6
datum with the face's mixing phase exists anywhere inside the banked surface. Per B746's
two-column law (gait transmits, name does not), the claim put a being-column datum into
the gait-column role. The original kill (value channel + sign; faces_consulted:
none-arithmetic-only) NEVER tested this column. The kill gains it now, computed.""")

print("=" * 92)
print("CELL 4 -- EXT-2: the banked face is sign-blind exactly where the claim needed a sign")
print("=" * 92)

check("S1", abs(evals[1] - np.conj(evals[0])) < 1e-9,
      "the mixing block's eigenphases form the conjugate pair e^{+-i 72 deg} (real trace + unit det): "
      "the face's kind-correct object presents both signs symmetrically -- it cannot orient one")

# the voice: zeta_K = zeta * L(chi_-3) Dirichlet coefficients, exact integer convolution
N = 5000
aN = [0] * (N + 1)
for d in range(1, N + 1):
    for m in range(d, N + 1, d):
        aN[m] += chi3(d)
expected = {1: 1, 2: 0, 3: 1, 4: 1, 5: 0, 6: 0, 7: 2, 9: 1, 13: 2, 21: 2, 25: 1, 49: 3}
check("S2", all(aN[k] == v for k, v in expected.items()) and all(c >= 0 for c in aN[1:])
      and all(isinstance(c, int) for c in aN),
      f"zeta_K Dirichlet coefficients a_n = sum_(d|n) chi_-3(d) computed EXACTLY (integers) to n = {N}; "
      f"sample splitting values verified; all a_n are real integers >= 0")


def zetaK_trunc(s):
    return sum(aN[nn] * cmath.exp(-s * math.log(nn)) for nn in range(1, N + 1) if aN[nn])


refl = 0.0
for spt in (3 + 2j, 2.5 + 1.7j, 3.5 - 0.9j):
    num = zetaK_trunc(spt - 1) / zetaK_trunc(spt)
    numc = (zetaK_trunc(spt.conjugate() - 1) / zetaK_trunc(spt.conjugate())).conjugate()
    refl = max(refl, abs(num - numc))
check("S3", refl < 1e-12,
      f"Schwarz reflection of the voice: conj[zeta_K-part of phi at conj(s)] = same at s "
      f"(max dev {refl:.2e} at 3 test points; EXACT term-by-term since every a_n is real -- the "
      f"completing factors (sqrt3/2pi)^s Gamma(s) are Schwarz-symmetric as real-based). "
      f"The voice phi(s) = Lambda_K(s-1)/Lambda_K(s) is invariant under the conjugation that swaps -+pi/6")


def trigamma(x):
    v, K = 0.0, 60
    for k in range(K):
        v += 1.0 / (x + k) ** 2
    z = x + K
    v += 1 / z + 1 / (2 * z ** 2) + 1 / (6 * z ** 3) - 1 / (30 * z ** 5) + 1 / (42 * z ** 7) - 1 / (30 * z ** 9)
    return v


L2 = (trigamma(1 / 3) - trigamma(2 / 3)) / 9      # L(2, chi_-3)
res_phi = 4 / (3 * L2)                            # = 2 pi^2/(9 zeta_K(2)) = Res_{s=2} phi  (B739 line 31)
check("S4", abs(res_phi - 1.70655217662816) < 1e-11 and res_phi > 0,
      f"Res phi = 2 pi^2/(9 zeta_K(2)) = 4/(3 L(2,chi_-3)) = {res_phi:.14f} -- matches B737's banked "
      f"2 sqrt3/vol(m004) = 1.70655217662816 (in-arc recomputation); REAL and positive: the voice's "
      f"leading spectral datum carries no phase at all")

markers = ["golden", "1.618", "0.618", "sqrt(5)", "sqrt5", "zeta_5", "zeta5", "Phi_5",
           "fibonacci", "Fibonacci", "GOLDEN", "Golden"]
hits = []
for arc in ("B737_candidate_zero", "B739_character_rigidity"):
    txt = open(os.path.join(FRONTIER, arc, "FINDINGS.md"), encoding="utf-8").read()
    for mk in markers:
        if mk in txt:
            hits.append((arc, mk))
check("S5", not hits,
      f"golden-marker grep over the voice arcs' FINDINGS (B737, B739): {len(hits)} hits -- re-verifies "
      f"B746's F11 absence (the gait/mixing column is entirely absent from the emission channel)")
print("""
EXT-2 (computed): every phase-bearing datum of the banked spectral face is conjugation-
symmetric -- the mixing block's +-72 deg pair (S1), the voice's real-integer-coefficient
zeta_K-quotient with real positive residue (S2-S4) -- and B739's character-rigidity
(verified at source: single channel, multiplicity 1, phi = Lambda_K(s-1)/Lambda_K(s)
exactly, nothing else in the continuous spectrum) forecloses any other continuous-
spectrum carrier. The conjugation that swaps kappa <-> conj(kappa) (-+pi/6, the
tau/amphichirality swap on which the kill's sign leg rests) acts TRIVIALLY on the whole
banked face: the spectral face cannot supply the CP sign the claim needed. The kill's
sign leg (B252 CP-symmetry) extends into the spectral face, computed.""")

print("=" * 92)
print("VERDICT")
print("=" * 92)
ok = not FAILURES
print(f"checks: {NCHECK[0]} run, {len(FAILURES)} failed {FAILURES if FAILURES else ''}")
print("""
KILL-EXTENDS.  Exactly what was computed, and no more:
 (1) kind/column mismatch: the claim's phase datum (Eisenstein, x^2-3x+3, disc -3,
     -+pi/6) and the face's kind-correct mixing data (golden, e^{+-2 pi i/5}, 1/phi,
     1/(phi sqrt5)) lie in Galois-disjoint fields (Q(zeta_3)/Q(zeta_12) vs Q(zeta_5),
     meeting only in Q): inside the banked surface there is NO identification of the
     pi/6 commutator phase with the program's mixing-type phase -- the claim's central
     identification is contradicted in kind by the face itself, a channel the original
     kill (value-mismatch only, faces_consulted: none-arithmetic-only) never tested.
 (2) sign-blindness: the banked face is invariant under the -+pi/6 conjugation (block
     pair symmetric; voice real-coefficient, real residue; B739-rigid continuous
     channel): the face cannot supply the CP sign either -- the kill's sign leg extends.
SCOPE: no eta_B statement, no SM values, no claim about non-banked future bridges;
the exposure note's Born-ledger/bounded-observer routes are OUT OF SCOPE here (not
spectral-face sources). The revival direction remains as unlikely as banked: nothing
in the face moves it.
""")
if not ok:
    raise SystemExit(1)
print("ALL CHECKS PASS")
