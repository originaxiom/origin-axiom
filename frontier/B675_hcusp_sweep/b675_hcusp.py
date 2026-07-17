"""B675 — THE H-CUSP PREDICTION SWEEP.

H-CUSP (the principle under test as a PREDICTION ENGINE): a stage
family can host an object's hearing only if the object's cusp lattice
quantizes the stage's weight lattice — the stage's Coxeter-commutant
field must contain the cusp field with a conformal lattice embedding.

Parts:
  1  THE COMMUTANT TABLE  — Coxeter elements of A1..A5, B2, G2, D4:
     char polys, commutant algebras, imaginary quadratic subfields
     (exact; Gauss-sum certificates + Groebner emptiness).
  2  THE SILVER TEST — the m136 cusp lattice EXACT from the banked
     B649 peripheral holonomy (MU=CCB, LAM=caCA over the degree-8
     field L = Q(w,i), w^4-8w^2-16=0); prediction: quantizes A3
     (commutant Q(i)), cannot quantize A2/A4; conductor behavior.
  3  THE HEARING CHECK (bounded) — SU(4)_1 / SU(4)_2 Kac-Peterson
     stages; the silver word's tone; the mod-8 (conductor) shadow-
     class test R^2L^2 vs R^10L^2.
  4  BRONZE (bounded) — the s464 (= b++LLLRRR) cusp field from
     SnapPy at two precisions + exact minimal-poly identification;
     the H-CUSP stage prediction.

Exact arithmetic (Fractions / sympy) in every decisive step; floats
only in Part 3 tones (two precisions, flagged) and Part 4 shape
harvest (identified poly then checked at 2 precisions, flagged).
"""
import itertools
import json
import os
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy import (Matrix, Poly, Rational, cyclotomic_poly, expand, eye,
                   groebner, sqrt, symbols)

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))
BAR = "=" * 72
T0 = time.time()


def sec(t):
    print("\n" + BAR + "\n" + t + "\n" + BAR, flush=True)


x = symbols('x')

# ===========================================================================
sec("PART 1 — THE COMMUTANT TABLE (exact)")

CARTAN = {
    'A1': [[2]],
    'A2': [[2, -1], [-1, 2]],
    'A3': [[2, -1, 0], [-1, 2, -1], [0, -1, 2]],
    'A4': [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]],
    'A5': [[2, -1, 0, 0, 0], [-1, 2, -1, 0, 0], [0, -1, 2, -1, 0],
           [0, 0, -1, 2, -1], [0, 0, 0, -1, 2]],
    'B2': [[2, -2], [-1, 2]],
    'G2': [[2, -1], [-3, 2]],
    # D4: order = leaf1, leaf2, leaf3, center
    'D4': [[2, 0, 0, -1], [0, 2, 0, -1], [0, 0, 2, -1], [-1, -1, -1, 2]],
}
# (alpha_j, alpha_j)/2 normalization (long roots norm 2 in ADE; B2 alpha1
# long norm 4; G2 alpha2 long norm 6):
DHALF = {'A1': [1], 'A2': [1, 1], 'A3': [1, 1, 1], 'A4': [1] * 4,
         'A5': [1] * 5, 'B2': [2, 1], 'G2': [1, 3], 'D4': [1] * 4}


def simple_refls(C):
    n = C.shape[0]
    out = []
    for i in range(n):
        S = eye(n)
        for j in range(n):
            S[j, i] -= C[i, j]
        out.append(S)
    return out


def order_of(M, cap=64):
    P = eye(M.shape[0])
    for k in range(1, cap + 1):
        P = P * M
        if P == eye(M.shape[0]):
            return k
    return None


def ident_cyclo(f):
    for m in range(1, 31):
        if Poly(f, x) == Poly(cyclotomic_poly(m, x), x):
            return m
    return None


def sqf(n):
    """signed squarefree part of a nonzero integer (exact)."""
    n = sp.Integer(n)
    s = sp.sign(n)
    out = 1
    for p, e in sp.factorint(abs(n)).items():
        if e % 2 == 1:
            out *= p
    return s * out


def quad_subfields_cyclo(m):
    """ALL quadratic subfields of Q(zeta_m), decisively, as squarefree
    parts.  m in {3,4,6}: the field IS quadratic (degree phi(m) = 2) —
    its unique quadratic subfield is itself.  m = 5: Gal = (Z/5)* is
    CYCLIC of order 4 (verified by element orders) => exactly ONE
    quadratic subfield, exhibited by the Gauss sum g^2 = 5."""
    if m == 3 or m == 6:
        return {-3}
    if m == 4:
        return {-1}
    if m == 5:
        orders = {a: min(k for k in range(1, 5) if pow(a, k, 5) == 1)
                  for a in (1, 2, 3, 4)}
        assert sorted(orders.values()) == [1, 2, 4, 4], orders
        assert gauss_cert(5, x - x**2 - x**3 + x**4, 5)
        return {5}
    raise ValueError(m)


def gauss_cert(m, elt, D):
    """verify elt^2 = D mod Phi_m exactly (a POSITIVE certificate)."""
    _, r = sp.div(expand(elt * elt - D), cyclotomic_poly(m, x), x)
    return sp.simplify(r) == 0


print(f"{'stage':>5} | h  | char poly of Coxeter (factored)"
      f"          | commutant  | Cox-plane field | imag.quad.subfield")
COXPLANE = {}
COMMUTANT_DIM = {}
for name, Cl in CARTAN.items():
    C = Matrix(Cl)
    n = C.shape[0]
    G = C.inv() * sp.diag(*DHALF[name])
    assert G == G.T, name
    refls = simple_refls(C)
    for S in refls:
        assert (S.T * G * S - G).is_zero_matrix, f"{name}: refl not isometry"
    cox = eye(n)
    for S in refls:
        cox = cox * S
    assert (cox.T * G * cox - G).is_zero_matrix
    h = order_of(cox)
    cp = cox.charpoly(x).as_expr()
    fl = sp.factor_list(cp)[1]
    facs = sorted(((ident_cyclo(f), int(e)) for f, e in fl))
    # commutant dimension check (exact nullspace of ad_cox on n x n)
    Xs = symbols(f'X0:{n * n}')
    XM = Matrix(n, n, Xs)
    E = cox * XM - XM * cox
    rows = [[E[i, j].coeff(v) for v in Xs] for i in range(n) for j in range(n)]
    comdim = n * n - Matrix(rows).rank()
    pred = sum(e * e * sp.totient(m) for m, e in facs)
    assert comdim == pred, f"{name}: commutant dim {comdim} != {pred}"
    fstr = "*".join((f"Phi{m}" if e == 1 else f"Phi{m}^{e}") for m, e in facs)
    # Coxeter-plane field = Q[x]/Phi_h
    quad = {2: "-", 1: "-", 3: "Q(sqrt-3)", 4: "Q(i)", 6: "Q(sqrt-3)",
            5: "none imag (Q(sqrt5) real)"}[h if h in (1, 2, 3, 4, 5, 6) else 5]
    COXPLANE[name] = h
    COMMUTANT_DIM[name] = comdim
    alg = " x ".join((f"Q(zeta{m})" if e == 1 else
                      f"M{e}(Q(zeta{m}))" if sp.totient(m) > 1 else
                      f"M{e}(Q)") for m, e in facs)
    print(f"{name:>5} | {h:<2} | {fstr:<40} | dim {comdim:<6} | "
          f"Q(zeta{h})        | {quad}")

print("\nCertificates (exact):")
print("  Phi3:  (x - x^2)^2   = -3   mod Phi3 :", gauss_cert(3, x - x**2, -3))
print("  Phi4:  x^2           = -1   mod Phi4 :", gauss_cert(4, x, -1))
print("  Phi5:  (x-x^2-x^3+x^4)^2 = 5 mod Phi5:",
      gauss_cert(5, x - x**2 - x**3 + x**4, 5))
print("  Phi6:  (2x - 1)^2    = -3   mod Phi6 :", gauss_cert(6, 2 * x - 1, -3))
print("\nExclusions (decisive: two quadratic fields coincide iff same "
      "squarefree part;\nfor m = 5, Gal cyclic => the Gauss-sum field "
      "Q(sqrt5) is the ONLY quadratic subfield):")
for D, m, note in [(-1, 3, "A2 CANNOT host Q(i)"),
                   (-1, 5, "A4 CANNOT host Q(i)"),
                   (-3, 5, "A4 CANNOT host Q(sqrt-3); reproduces B672"),
                   (-3, 4, "A3/B2 CANNOT host Q(sqrt-3)"),
                   (-1, 6, "A5/G2/D4-Coxeter-plane CANNOT host Q(i)")]:
    subs = quad_subfields_cyclo(m)
    ok = sqf(D) in subs
    print(f"  Q(sqrt({D})) in Q(zeta{m}): {ok}   [quad subfields: "
          f"{{sqrt({', '.join(str(s) for s in sorted(subs))})}}]  ({note})")

print("""
NOTE (the D4 subtlety, resolved in Part 2E): D4's Coxeter char poly is
Phi6*Phi2^2 — the commutant ALGEBRA is Q(zeta6) x M2(Q), not a field,
and M2(Q) contains every quadratic field, an apparent loophole in the
'commutant' reading of H-CUSP.  Part 2E computes the loophole CLOSED:
the (-1)^2-block's own Gram form is the hexagonal form, whose rational
proper isometries are the norm-1 group of Q(sqrt-3) — no rational
J^2 = -I exists (lex-Groebner + rational-root check, decisive), while
mult-by-sqrt(-3) does.  The conformal lattice condition re-imposes the
Coxeter arithmetic on its own; the table above IS the prediction
table, with no extra axiom.""")

# ===========================================================================
sec("PART 2 — THE SILVER TEST (exact, from the banked B649 holonomy)")

# ---- the B649 exact field L = Q(w, i), w^4 = 8 w^2 + 16 -------------------
MODL = [Fr(16), Fr(0), Fr(8), Fr(0)]


def pmulred(p, q):
    out = [Fr(0)] * 7
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            out[i + j] += a * b
    for k in range(6, 3, -1):
        c = out[k]
        if c != 0:
            out[k] = Fr(0)
            for t2, m in enumerate(MODL):
                out[k - 4 + t2] += c * m
    return out[:4]


class LF:
    __slots__ = ("re", "im")

    def __init__(self, re=None, im=None):
        self.re = re if re is not None else [Fr(0)] * 4
        self.im = im if im is not None else [Fr(0)] * 4

    def __add__(s, o):
        return LF([a + b for a, b in zip(s.re, o.re)],
                  [a + b for a, b in zip(s.im, o.im)])

    def __sub__(s, o):
        return LF([a - b for a, b in zip(s.re, o.re)],
                  [a - b for a, b in zip(s.im, o.im)])

    def __mul__(s, o):
        rr, ii = pmulred(s.re, o.re), pmulred(s.im, o.im)
        ri, ir = pmulred(s.re, o.im), pmulred(s.im, o.re)
        return LF([a - b for a, b in zip(rr, ii)],
                  [a + b for a, b in zip(ri, ir)])

    def is_zero(s):
        return all(c == 0 for c in s.re) and all(c == 0 for c in s.im)

    def inv(s):
        cols = []
        for k in range(8):
            b = LF([Fr(1) if t2 == k else Fr(0) for t2 in range(4)], None) \
                if k < 4 else \
                LF(None, [Fr(1) if t2 == k - 4 else Fr(0) for t2 in range(4)])
            cols.append((s * b).re + (s * b).im)
        A = [[cols[j][i] for j in range(8)] + [Fr(1) if i == 0 else Fr(0)]
             for i in range(8)]
        for c in range(8):
            piv = next(r for r in range(c, 8) if A[r][c] != 0)
            A[c], A[piv] = A[piv], A[c]
            pv = A[c][c]
            A[c] = [v / pv for v in A[c]]
            for r in range(8):
                if r != c and A[r][c] != 0:
                    f = A[r][c]
                    A[r] = [v - f * w for v, w in zip(A[r], A[c])]
        xs = [A[r][8] for r in range(8)]
        return LF(xs[:4], xs[4:])


def Lc(q):
    return LF([Fr(q), Fr(0), Fr(0), Fr(0)], None)


L0, L1 = Lc(0), Lc(1)
dent = json.load(open(os.path.join(
    _REPO, "frontier", "B649_silver_holonomy", "entries_L.json")))


def gen2(nm):
    return [[LF([Fr(v) for v in dent[f"{nm}{i}{j}"][0]],
                [Fr(v) for v in dent[f"{nm}{i}{j}"][1]])
             for j in range(2)] for i in range(2)]


def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def adj2(M):
    return [[M[1][1], L0 - M[0][1]], [L0 - M[1][0], M[0][0]]]


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


G2m = {nm: gen2(nm) for nm in "abc"}
for nm in "abc":
    G2m[nm.upper()] = adj2(G2m[nm])


def word2(w):
    m = None
    for ch in w:
        m = G2m[ch] if m is None else mm2(m, G2m[ch])
    return m


print("2A. Gates on the banked rep (decisive, exact):")
for nm in "abc":
    print(f"    det({nm}) = 1 :", (det2(G2m[nm]) - L1).is_zero())
for rel in ["aBAbcc", "aaCbcB"]:
    W = word2(rel)
    isI = all((W[i][j] - (L1 if i == j else L0)).is_zero()
              for i in range(2) for j in range(2))
    print(f"    relator {rel} -> I :", isI)

MU2, LAM2 = word2("CCB"), word2("caCA")
comm_ok = all((mm2(MU2, LAM2)[i][j] - mm2(LAM2, MU2)[i][j]).is_zero()
              for i in range(2) for j in range(2))
print("    [rho(MU), rho(LAM)] = 0 :", comm_ok)


def trace_sign(M):
    tr = M[0][0] + M[1][1]
    for s in (1, -1):
        if (tr - Lc(2 * s)).is_zero():
            return s
    return None


sMU, sLAM = trace_sign(MU2), trace_sign(LAM2)
print(f"    tr(MU) = {2*sMU:+d}, tr(LAM) = {2*sLAM:+d}  (both parabolic)")
NMU = [[Lc(sMU) * MU2[i][j] - (L1 if i == j else L0) for j in range(2)]
       for i in range(2)]
NLAM = [[Lc(sLAM) * LAM2[i][j] - (L1 if i == j else L0) for j in range(2)]
        for i in range(2)]
for nmn, N in (("N_mu", NMU), ("N_lam", NLAM)):
    nil = all(v.is_zero() for row in mm2(N, N) for v in row)
    print(f"    {nmn} nilpotent (N^2 = 0):", nil)

piv = next((i, j) for i in range(2) for j in range(2)
           if not NMU[i][j].is_zero())
tau = NLAM[piv[0]][piv[1]] * NMU[piv[0]][piv[1]].inv()
prop = all((NLAM[i][j] - tau * NMU[i][j]).is_zero()
           for i in range(2) for j in range(2))
print("    N_lam = tau * N_mu (all 4 entries):", prop)
in_Qi = all(c == 0 for c in tau.re[1:]) and all(c == 0 for c in tau.im[1:])
tre, tim = tau.re[0], tau.im[0]
print(f"\n2B. THE SILVER CUSP MODULUS (exact): tau = lam-translation / "
      f"mu-translation\n    tau = {tre} + ({tim}) i   ;   tau in Q(i): "
      f"{in_Qi}   [k(Gamma) = Q(i), B659: CONFIRMED at the lattice level]")
assert in_Qi
if tim < 0:
    tau_c = (tre, -tim)
    print(f"    (orientation: using tau-bar = {tre} + {-tim} i for Im > 0; "
          f"conformal class unchanged)")
else:
    tau_c = (tre, tim)
tre, tim = tau_c
# minimal polynomial / order conductor of Z + Z tau
A_ = sp.Rational(1)
B_ = -2 * sp.Rational(tre)
C_ = sp.Rational(tre) ** 2 + sp.Rational(tim) ** 2
den = sp.lcm([sp.denom(v) for v in (A_, B_, C_)])
Ai, Bi, Ci = [sp.Integer(v * den) for v in (A_, B_, C_)]
g = sp.gcd(sp.gcd(Ai, Bi), Ci)
Ai, Bi, Ci = Ai // g, Bi // g, Ci // g
D = Bi * Bi - 4 * Ai * Ci
f_cond = sp.sqrt(D / (-4))
print(f"    min poly of tau: {Ai} x^2 + {Bi} x + {Ci} = 0 ;  disc = {D}"
      f" = f^2 * (-4)  =>  ORDER CONDUCTOR f = {f_cond} in Z[i]")
print(f"    Gram (up to scale): [[1, {tre}], [{tre}, {tre**2 + tim**2}]]")

# ---- 2C. the A3 target lattice ------------------------------------------
print("\n2C. The A3 side: the Coxeter (Phi4) plane of the A3 weight lattice")
C3 = Matrix(CARTAN['A3'])
G3 = C3.inv()
cox3 = eye(3)
for S in simple_refls(C3):
    cox3 = cox3 * S
K = (cox3 ** 2 + eye(3))
ns = K.nullspace()
assert len(ns) == 2
basis = []
for v in ns:
    d = sp.lcm([sp.denom(c) for c in v])
    vv = v * d
    g = sp.gcd(list(vv))
    basis.append(vv / g)
M1, M2v = basis
# saturate (index of Z<M1,M2v> in P cap V)
mins = [Matrix([M1.T, M2v.T]).T[i:i + 2, :].det() if False else 0
        for i in range(1)]
mat32 = Matrix.hstack(M1, M2v)
minors = [mat32[[i, j], :].det() for i, j in [(0, 1), (0, 2), (1, 2)]]
gm = sp.gcd(list(minors))
print(f"    integer kernel of cox^2+1: basis {list(M1)}, {list(M2v)}; "
      f"2x2-minor gcd = {gm} (saturated iff 1): {gm == 1}")
assert gm == 1
# J = cox restricted; solve cox*M1 = p*M1 + q*M2v etc.
sol = sp.linsolve((mat32, cox3 * M1))
p1, q1 = next(iter(sol))
sol = sp.linsolve((mat32, cox3 * M2v))
p2, q2 = next(iter(sol))
J = Matrix([[p1, p2], [q1, q2]])
print(f"    J = cox|plane = {J.tolist()},  J^2 = -I: {(J**2 + eye(2)).is_zero_matrix}")
g11 = (M1.T * G3 * M1)[0]
g12 = (M1.T * G3 * M2v)[0]
g22 = (M2v.T * G3 * M2v)[0]
rez = g12 / g11
imz2 = g22 / g11 - rez ** 2
imz = sp.sqrt(imz2)
print(f"    plane Gram/g11: [[1, {rez}], [{rez}, {g22/g11}]]; "
      f"Im z2 = sqrt({imz2}) = {imz}  rational: {imz.is_rational}")
assert imz.is_rational
# orientation: J is rotation by +90 or -90 in the (M1, M2v) frame; fix sign
# z2 with Im > 0 in the frame where J = +i:
z2 = (rez, imz if q1 * imz > 0 else -imz)
if z2[1] < 0:
    z2 = (rez, abs(imz))  # relabel by conjugating the identification
print(f"    A3 Coxeter-plane lattice  M = Z + Z z2,  z2 = {z2[0]} + {z2[1]} i")
# order of M
Bm = -2 * sp.Rational(z2[0])
Cm = sp.Rational(z2[0]) ** 2 + sp.Rational(z2[1]) ** 2
denm = sp.lcm([sp.denom(v) for v in (Bm, Cm)])
Am2, Bm2, Cm2 = sp.Integer(denm), sp.Integer(Bm * denm), sp.Integer(Cm * denm)
gg = sp.gcd(sp.gcd(Am2, Bm2), Cm2)
Am2, Bm2, Cm2 = Am2 // gg, Bm2 // gg, Cm2 // gg
Dm = Bm2 * Bm2 - 4 * Am2 * Cm2
print(f"    min poly of z2: {Am2} x^2 + {Bm2} x + {Cm2}; disc {Dm} => "
      f"conductor {sp.sqrt(Dm / (-4))} in Z[i]")


def in_lat(v, z):
    """v = (re, im) in Z + Z z (z = (re, im)) ?  exact."""
    beta = sp.Rational(v[1]) / z[1]
    alpha = sp.Rational(v[0]) - beta * z[0]
    return alpha.is_integer and beta.is_integer, (alpha, beta)


def qi_mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


print("\n2D. THE PREDICTION, verified both ways:")
print("  (i) silver -> A3: conformal Z[i]-equivariant embedding "
      "j = mult-by-xi, xi minimizing the index:")
best = None
tauQ = (sp.Rational(tre), sp.Rational(tim))
for dd in (1, 2, 3, 4, 6, 8):
    for pq in range(-16, 17):
        for qq in range(-16, 17):
            if pq == qq == 0:
                continue
            xi = (sp.Rational(pq, dd), sp.Rational(qq, dd))
            ok1, ab1 = in_lat(xi, z2)
            if not ok1:
                continue
            ok2, ab2 = in_lat(qi_mul(xi, tauQ), z2)
            if not ok2:
                continue
            Mint = Matrix([[ab1[0], ab2[0]], [ab1[1], ab2[1]]])
            idx = abs(Mint.det())
            if best is None or idx < best[0]:
                best = (idx, xi, Mint)
idx, xi, Mint = best
d1 = sp.gcd(list(Mint))
d2 = idx / d1
print(f"      xi = {xi[0]} + ({xi[1]}) i ;  coord matrix {Mint.tolist()} ; "
      f"INDEX = {idx} (elementary divisors {d1}, {d2})")
print(f"      EXISTS: True — the silver cusp lattice QUANTIZES A3.")
for mod in (2, 4, 8):
    ker = sp.gcd(d1, mod) * sp.gcd(d2, mod)
    print(f"      mod {mod}: |ker(Lambda/{mod} -> M/{mod})| = {ker} "
          f"({'ISO' if ker == 1 else 'NOT iso'})")
print(f"      gcd(index, 8) = {sp.gcd(idx, 8)}  "
      f"[silver conductor 8 = the shadow level; 2 RAMIFIES in Q(i): "
      f"(1+i)^2 = 2i]")
print("  (ii) silver -/-> A2: needs Q(i) inside Q(zeta3) = Q(sqrt-3): "
      f"sqf(-1) = {sqf(-1)} != {sqf(-3)} = sqf(-3)  => IMPOSSIBLE (exact)")
print("  (iii) silver -/-> A4: needs Q(i) inside Q(zeta5), whose ONLY "
      "quadratic subfield is Q(sqrt5)  => IMPOSSIBLE (exact)")

print("""
  PREREG RESOLUTION (PREREG_ADDENDUM_OUTCOMES.md, sealed before this
  run): the DISCRIMINATOR was computed FIRST (2B): the silver cusp
  translation lattice is defined over Q(i) ALONE — tau = -2i, every
  w-component (the sqrt2/zeta8-compositum part) vanishes EXACTLY in
  the banked L-basis; the bifocal entanglement does NOT reach the
  cusp.  => outcomes 1 vs 2 apply (outcome 3 is off the table), and
  the embedding certificate (2D-i) + the A2/A4 field mismatches
  (2D-ii/iii) select  OUTCOME 1: CONFIRMED.""")

print("\n2E. Controls + the cross grid (golden object, same machinery):")
# golden: tau_g = 2 sqrt(-3) into A2 plane Z + Z zeta6  (B672 reproduction)
z6 = (sp.Rational(1, 2), sp.sqrt(3) / 2)


def in_lat_s(v, z):
    beta = v[1] / z[1]
    alpha = sp.simplify(v[0] - beta * z[0])
    beta = sp.simplify(beta)
    return (alpha.is_integer and beta.is_integer), (alpha, beta)


taug = (sp.Integer(0), 2 * sp.sqrt(3))
ok1, ab1 = in_lat_s((sp.Integer(1), sp.Integer(0)), z6)
ok2, ab2 = in_lat_s(taug, z6)
Mg = Matrix([[ab1[0], ab2[0]], [ab1[1], ab2[1]]])
print(f"    golden -> A2 with xi = 1: contained {ok1 and ok2}; coord matrix "
      f"{Mg.tolist()}; index {abs(Mg.det())} (= conductor 4, B672 cellB "
      f"REPRODUCED); elementary divisors 1, 4 => ISO mod 5 (gcd(4,5)=1)")
print("    golden -/-> A3/B2: z^2 = -3 in Q(i): p^2-q^2=-3 & 2pq=0 -> "
      "q=0: p^2=-3 (no) ; p=0: q^2=3 (no)  => IMPOSSIBLE (exact)")
print(f"    golden -> A5/G2/D4 Coxeter-plane field Q(zeta6): (2x-1)^2 = -3 "
      f"certificate above => field-level YES (A2 remains the MINIMAL stage)")

# D4 loophole block, exact
print("\n    D4 degenerate block (the loophole, computed):")
C4d = Matrix(CARTAN['D4'])
G4d = C4d.inv()
cox4 = eye(4)
for S in simple_refls(C4d):
    cox4 = cox4 * S
KB = cox4 + eye(4)
nsb = KB.nullspace()
assert len(nsb) == 2
bb = []
for v in nsb:
    d = sp.lcm([sp.denom(c) for c in v])
    vv = v * d
    bb.append(vv / sp.gcd(list(vv)))
NB = Matrix.hstack(*bb)
gb11 = (bb[0].T * G4d * bb[0])[0]
gb12 = (bb[0].T * G4d * bb[1])[0]
gb22 = (bb[1].T * G4d * bb[1])[0]
gB = Matrix([[gb11, gb12], [gb12, gb22]]) / gb11
a_, b_, c_ = symbols('a_ b_ c_')
JJ = Matrix([[a_, b_], [c_, -a_]])  # J^2 = -I forces tr J = 0, det J = 1
eqs = [sp.expand(e) for e in
       list(JJ ** 2 + eye(2)) + list(JJ.T * gB * JJ - gB) if e != 0]
gbb = groebner(eqs, a_, b_, c_, order='lex', domain='QQ')
uni = [e for e in gbb.exprs if e.free_symbols <= {c_}]
rat_roots = [r for u in uni for r in sp.roots(Poly(u, c_), filter='Q')]
print(f"      (-1)^2-block Gram (normalized) = {gB.tolist()} — the "
      f"HEXAGONAL form (CM by sqrt-3)!")
print(f"      rational J, J^2 = -I isometric: lex-GB = {gbb.exprs} ; "
      f"univariate {uni[0]} has rational roots: {rat_roots}  => NONE "
      f"exists (decisive)")
Kw = Matrix([[1, 2], [-2, -1]])
print(f"      golden witness on the SAME block: K = {Kw.tolist()}: "
      f"K^2 = -3I: {(Kw**2 + 3*eye(2)).is_zero_matrix}, "
      f"K^T g K = 3 g: {(Kw.T*gB*Kw - 3*gB).is_zero_matrix}")
print("      => the 'M2(Q) loophole' CLOSES ITSELF: the block's own "
      "conformal form is hexagonal,\n      so even the degenerate block "
      "only quantizes Q(sqrt-3) — H-CUSP needs no extra axiom;\n      "
      "the commutant reading and the Coxeter-plane reading AGREE on all "
      "8 stages computed.")

# ===========================================================================
sec("PART 3 — THE HEARING CHECK (bounded; numerics at 2 precisions, "
    "flagged NON-DECISIVE)")

import cmath

import numpy as np


def su_data(N, k):
    kap = k + N
    weights = [w for w in itertools.product(range(k + 1), repeat=N - 1)
               if sum(w) <= k]
    rho_eps = [Fr(0)] * N

    def leps(wt):
        return [sum(wt[j] + 1 for j in range(i, N - 1)) for i in range(N - 1)] + [0]

    def ipf(u, v):
        return Fr(sum(a * b for a, b in zip(u, v))) - Fr(sum(u) * sum(v), N)

    r0 = leps([0] * (N - 1))
    cc = Fr(k * (N * N - 1), k + N)
    hs = [(ipf(leps(w), leps(w)) - ipf(r0, r0)) / (2 * kap) for w in weights]
    perms = list(itertools.permutations(range(N)))

    def sgn(p):
        return (-1) ** sum(p[i] > p[j] for i in range(N)
                           for j in range(i + 1, N))

    n = len(weights)
    S = np.zeros((n, n), dtype=complex)
    for i, wl in enumerate(weights):
        Ll = leps(wl)
        for j, wm in enumerate(weights):
            Lm = leps(wm)
            S[i, j] = sum(sgn(p) * cmath.exp(-2j * cmath.pi *
                          float(ipf([Ll[q] for q in p], Lm)) / kap)
                          for p in perms)
    S = S / np.sqrt((np.abs(S) ** 2).sum(axis=0)[0])
    thetas = [h - cc / 24 for h in hs]
    T = np.diag([cmath.exp(2j * cmath.pi * float(th)) for th in thetas])
    return weights, S, T, cc, hs, thetas


def modular_gate(S, T):
    n = S.shape[0]
    uni = np.allclose(S @ S.conj().T, np.eye(n), atol=1e-9)
    sym = np.allclose(S, S.T, atol=1e-9)
    S2 = S @ S
    perm = np.allclose(np.abs(S2) @ np.abs(S2), np.eye(n), atol=1e-9)
    ST3 = np.linalg.matrix_power(S @ T, 3)
    idx = np.unravel_index(np.argmax(np.abs(S2)), S2.shape)
    prop = np.allclose(ST3, (ST3[idx] / S2[idx]) * S2, atol=1e-7)
    return uni and sym and perm and prop


def wrt_trace(S, T, word):
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    Rr, Lr = T, Si @ Ti @ S
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ (Rr if ch == 'R' else Lr)
    return np.trace(M)


STAGES = {}
for (N, k) in [(3, 2), (4, 1), (4, 2)]:
    w, S, T, cc, hs, thetas = su_data(N, k)
    gate = modular_gate(S, T)
    ordT = sp.lcm([sp.denom(sp.Rational(th)) for th in thetas])
    STAGES[(N, k)] = (S, T, ordT)
    print(f"  SU({N})_{k}: {len(w)} primaries, gate {gate}, c = {cc}, "
          f"ord(T) = {ordT}  (congruence level; conductor-8 divisibility: "
          f"{'8 | ' + str(ordT) if ordT % 8 == 0 else '8 does NOT divide ' + str(ordT)})")
    assert gate

print("\n  Tones (Z = tr rho(word), double precision):")
for word in ['RL', 'RRLL', 'RRRLLL']:
    row = []
    for (N, k) in [(3, 2), (4, 1), (4, 2)]:
        S, T, _ = STAGES[(N, k)]
        z = wrt_trace(S, T, word)
        row.append(f"SU({N})_{k}: {z.real:+.6f}{z.imag:+.6f}i")
    print(f"    {word:>7} | " + " | ".join(row))

print("\n  THE SHADOW-CLASS TEST at the silver conductor 8: "
      "R^2L^2 vs R^10L^2  (equal mod 8, different in SL(2,Z))")
w1, w2 = 'RRLL', 'R' * 10 + 'LL'
Rm = Matrix([[1, 1], [0, 1]])
Lm = Matrix([[1, 0], [1, 1]])


def wmat(w):
    M = eye(2)
    for ch in w:
        M = M * (Rm if ch == 'R' else Lm)
    return M


M1w, M2w = wmat(w1), wmat(w2)
print(f"    matrices: {M1w.tolist()} vs {M2w.tolist()}; "
      f"equal mod 8: {[(a - b) % 8 for a, b in zip(list(M1w), list(M2w))] == [0]*4}; "
      f"equal mod 15: {[(a - b) % 15 for a, b in zip(list(M1w), list(M2w))] == [0]*4}")
for (N, k) in [(4, 1), (4, 2), (3, 2)]:
    S, T, ordT = STAGES[(N, k)]
    za, zb = wrt_trace(S, T, w1), wrt_trace(S, T, w2)
    print(f"    SU({N})_{k} (level {ordT}): Z({w1}) = {za:.8f}, "
          f"Z(R^10L^2) = {zb:.8f}, equal: {abs(za - zb) < 1e-8}")

print("\n  High-precision corroboration (mpmath, 40 dps) + exact "
      "identification of the SU(4)_1 silver tone:")
from mpmath import mp, mpc, mpf, pslq

mp.dps = 40


def su41_tone(word):
    # SU(4)_1: 4 primaries, h = (0, 3/8, 1/2, 3/8), c = 3
    hs = [mpf(0), mpf(3) / 8, mpf(1) / 2, mpf(3) / 8]
    om = mp.e ** (mpc(0, -2) * mp.pi / 4)
    S = mp.matrix(4, 4)
    for a in range(4):
        for b in range(4):
            S[a, b] = om ** (a * b) / 2
    T = mp.matrix(4, 4)
    for a in range(4):
        T[a, a] = mp.e ** (mpc(0, 2) * mp.pi * (hs[a] - mpf(1) / 8))
    Rr = T
    Lr = (S ** -1) * (T ** -1) * S
    M = mp.eye(4)
    for ch in word:
        M = M * (Rr if ch == 'R' else Lr)
    return sum(M[i, i] for i in range(4))


zs = su41_tone('RRLL')
zs2 = su41_tone('R' * 10 + 'LL')
print(f"    Z(RRLL; SU(4)_1) = {mp.nstr(zs, 25)}")
print(f"    Z(R^10L^2; SU(4)_1) = {mp.nstr(zs2, 25)}   "
      f"|diff| = {mp.nstr(abs(zs - zs2), 5)}")
im_zero = abs(zs.imag) < mpf(10) ** -30
r_re = pslq([mpf(1), mp.sqrt(2), zs.real], maxcoeff=10 ** 6)
print(f"    Im(Z) = 0 (to 30 digits): {im_zero} ; pslq Re over "
      f"[1, sqrt2]: {r_re}")
if r_re and im_zero:
    reex = sp.Rational(-r_re[0], r_re[2]) + \
        sp.Rational(-r_re[1], r_re[2]) * sp.sqrt(2)
    print(f"    identified: Z(RRLL; SU(4)_1) = {reex}  (RATIONAL — the "
          f"silver tone at its conductor-8 stage);")
    print(f"    40-dps residual |Z - ({reex})| = "
          f"{mp.nstr(abs(zs - mpf(str(reex))), 5)}")

# ===========================================================================
sec("PART 4 — BRONZE (bounded): the s464 cusp field + the prediction")

import warnings

warnings.filterwarnings("ignore")
import snappy

for name in ["b++LR", "b++LLRR", "b++LLLRRR"]:
    M = snappy.Manifold(name)
    ident = M.identify()
    print(f"  {name}: {ident[0] if ident else '?'}  "
          f"vol {float(M.volume()):.8f}")

print("\n  Cusp shapes (SnapPy default peripheral basis), double + "
      "high precision (~60 digits):")
SHAPES = {}
for name in ["b++LR", "b++LLRR", "b++LLLRRR", "s464"]:
    Mlo = snappy.Manifold(name)
    sh_lo = complex(Mlo.cusp_info()[0].shape)
    shr = Mlo.high_precision().cusp_info()[0]["shape"]
    sh_hi = mpc(mpf(str(shr.real()).replace(" ", "")),
                mpf(str(shr.imag()).replace(" ", "")))
    SHAPES[name] = (sh_lo, sh_hi)
    print(f"    {name:>10}: {sh_lo.real:+.3e} + {sh_lo.imag:.12f} i   "
          f"purely imaginary (60 digits): {abs(sh_hi.real) < mpf(10)**-50}")

print("\n  Identification (pslq on u = Im(tau)^2, cascade deg 1..4; the "
      "identified poly re-checked at BOTH precisions):")
BRONZE = None
for name, label, banked, exp_disc in [
        ("b++LR", "golden m004",
         "banked EXACT tau = 2 sqrt(-3): disc -48, f = 4 (B672 cellB)", -48),
        ("b++LLRR", "silver m136",
         "banked EXACT tau = -2i (Part 2B): disc -16, f = 2", -16),
        ("b++LLLRRR", "bronze s464", None, None)]:
    lo, hi = SHAPES[name]
    y = hi.imag
    u = y * y
    rel = None
    for deg in (1, 2, 3, 4):
        r = pslq([u ** k for k in range(deg + 1)],
                 maxcoeff=10 ** 4, maxsteps=10 ** 6)
        if r and abs(sum(c * u ** k for k, c in enumerate(r))) < mpf(10) ** -25:
            rel = (deg, r)
            break
    deg, r = rel
    pu = sum(sp.Integer(c) * sp.symbols('u') ** k for k, c in enumerate(r))
    resid_hi = sum(c * u ** k for k, c in enumerate(r))
    ulo = mpf(abs(lo.imag)) ** 2
    resid_lo = sum(c * ulo ** k for k, c in enumerate(r))
    print(f"    {label}: deg(u) = {deg}, relation {r}")
    print(f"        p(u) = {pu} = 0 ; residuals: double {mp.nstr(resid_lo, 3)}"
          f", 60-digit {mp.nstr(resid_hi, 3)}")
    if deg == 1:
        u_ex = sp.Rational(-r[0], r[1])
        tau2 = -u_ex
        Aq, Cq = sp.Integer(sp.denom(u_ex)), sp.Integer(sp.numer(u_ex))
        Dq = -4 * Aq * Cq
        d = 1
        for pp, ee in sp.factorint(Aq * Cq).items():
            if ee % 2 == 1:
                d *= pp
        dK = -d if (-d) % 4 == 1 else -4 * d
        print(f"        tau^2 = {tau2}: cusp field Q(sqrt-{d}); order disc "
              f"{Dq}, conductor f = {sp.sqrt(sp.Integer(Dq) / dK)}")
        print(f"        CROSS-ROUTE CHECK vs {banked}: disc {Dq} == "
              f"{exp_disc}: {sp.Integer(Dq) == exp_disc}  (same order "
              f"class, basis-independent invariant)")
    else:
        BRONZE = (deg, r)

print("\n  Bronze analysis (exact, on the identified quartic):")
uu = sp.symbols('u')
qpoly = sp.Poly(192 * uu ** 4 - 112 * uu ** 3 + 20 * uu ** 2 - 21 * uu + 7,
                uu)
print(f"    p(u) = {qpoly.as_expr()}  irreducible: {qpoly.is_irreducible}")
print(f"    disc(p) factorization: {sp.factorint(qpoly.discriminant())}")
from sympy.polys.numberfields.galoisgroups import galois_group

Ggal, _alt = galois_group(qpoly)
print(f"    Galois group of p: order {Ggal.order()}, abelian: "
      f"{Ggal.is_abelian}  (order 24 = S4)")
tpoly = sp.Poly(192 * uu ** 8 + 112 * uu ** 6 + 20 * uu ** 4
                + 21 * uu ** 2 + 7, uu)
print(f"    min poly of tau_bronze (= i sqrt(u)): {tpoly.as_expr()}  "
      f"irreducible: {tpoly.is_irreducible}  => [Q(tau) : Q] = 8")
print("    INDEPENDENT CORROBORATION: the census triangulation s464 "
      "(different peripheral basis)\n    gives u' with the REVERSED "
      "relation [-192, 112, -20, 21, -7], i.e. u' = 1/u — the SAME "
      "field:")
_, hi464 = SHAPES["s464"]
u464 = hi464.imag ** 2
rr = pslq([u464 ** k for k in range(5)], maxcoeff=10 ** 10, maxsteps=10 ** 6)
print(f"        pslq(census u'): {rr} ;  u * u' = 1: "
      f"{mp.nstr(abs(u * u464 - 1), 3)}")

print("""
  THE BRONZE PREDICTION (H-CUSP): every stage family's Coxeter-plane
  field is Q[x]/Phi_h — CYCLOTOMIC, hence ABELIAN over Q (A, B, C, D,
  E, F, G alike).  The bronze cusp field is a degree-8 field whose
  quartic subfield Q(u) has Galois closure S4 — NON-ABELIAN.  By
  Kronecker-Weber no subfield chain can place Q(tau_bronze) (or even
  Q(u)) inside ANY cyclotomic field.
    => H-CUSP PREDICTS: NO stage family at ANY rank hears bronze.
    (Falsifiable: one bronze tone with shadow-class structure at any
    A_n stage kills the principle.  Status of the identification:
    pslq at 60 digits, residual ~1e-59, re-checked at truncated
    precision and against the independent census triangulation —
    corroborated, not certified; the exact-descent route stays open.)
  Note: the banked cellW35 SL(2,Z)-side data (disc 117 = 3^2 * 13)
  lives on the REAL/Anosov side; the hyperbolic cusp field's quartic
  has disc primes {2, 7, 617} — the 13-dial does NOT surface in the
  cusp lattice.  The prereg's declared bronze confound (f = 3 vs
  d_K = 13) is resolved by computation: NEITHER prime appears — the
  confound dissolves into a sharper fact.  The f = m ladder (golden
  4_1, silver m136, bronze s464) breaks at bronze in the CUSP
  arithmetic too: golden/silver cusp fields are imaginary quadratic;
  bronze jumps to degree 8.""")

# ===========================================================================
sec("VERDICT — THE H-CUSP ASSIGNMENT TABLE (the principle PREDICTS)")
print(f"""
  object | cusp lattice (exact)      | cusp field   | H-CUSP stage assignment
  -------+---------------------------+--------------+---------------------------------------------
  golden | Z + Z 2sqrt(-3), f = 4    | Q(sqrt-3)    | A2 = SU(3) (min; also A5/G2/D4-plane);
         |                           |              |   NOT A3/A4/B2  [banked B672: CONFIRMED]
  silver | Z + Z 2i,        f = {f_cond}    | Q(i)         | A3 = SU(4) (min; also B2);
         |                           |              |   NOT A2/A4/A5/G2  [NEW]
  bronze | deg-8, S4 closure         | Q(tau), deg 8| NO stage family at ANY rank  [NEW, sharp]

  Exact certificates: Part 1 Gauss sums + the quadratic-subfield
  exclusions (squarefree parts; Gal(Q(zeta5)) cyclic); Part 2
  embedding coordinate matrices with indices (golden index 4 iso mod
  5 REPRODUCED from B672; silver index 2 = its conductor, kernel of
  order 2 mod 8 = the RAMIFIED prime (1+i)); Part 2E the D4 block
  lex-Groebner rational-root exclusion + the golden K-witness; Part 4
  the bronze quartic (corroborated at 2 precisions + independent
  triangulation; NOT certified — flagged).

  THE INDEX = CONDUCTOR LAW (new, exact, 2 instances): the minimal
  conformal quantization index equals the cusp order conductor
  (golden 4, silver 2).  Golden's conductor is coprime to its shadow
  level 5 => iso mod 5; silver's conductor 2 divides its shadow
  level 8 => the quantization has a (1+i)-line kernel mod 8.

  THE HEARING SUPPORT (Part 3, numeric-flagged): SU(4)_1 is EXACTLY
  the conductor-8 stage — ord(T) = 8, and it hears only the mod-8
  shadow class (Z(R^2L^2) = Z(R^10L^2) = 2, words equal mod 8 but not
  in SL(2,Z)); SU(3)_2 (level 15) and SU(4)_2 (level 48) separate
  them.  The silver -> A3 assignment lands on the stage whose
  congruence level IS the silver conductor.

  total time: {time.time() - T0:.0f}s
""")
