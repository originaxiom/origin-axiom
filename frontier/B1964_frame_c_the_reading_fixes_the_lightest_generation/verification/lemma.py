"""B1964, the lemma (main, 2026-11-19; exact, sympy): frame C's coupling Y_ab = sum_mn (C_a^T eps S C_b)_mn Mw_mn over the
generation blocks C = (QJ, QI, QK) (frame_mp's BLOCKS, EPS = QJ).
 L1  for S = E12 and a generic 2 x 2 Mw (four free symbols): u^H Y = 0 for u = (-i, 0, 1), and Y has rank 2 exactly
     when det Mw != 0;
 L2  for S = E21: u^H Y = 0 for u = (i, 0, 1), and the same rank statement;
 L3  the two u are orthogonal;
 L4  for the quaternion units Q in {QI, QJ, QK}: eps conj(Q) eps^T = Q, so the conjugate reading eps conj(S) eps^T of
     S = c0 QI + c1 QJ + c2 QK is c0* QI + c1* QJ + c2* QK;
 L5  c1 QJ + c2 QK with c2 = -i c1 equals 2 c1 E12, and its conjugate reading (c1* QJ + c2* QK, c2* = i c1*) equals
     -2 c1* E21  [first written -2 c1 E12; the sign corrected 2026-11-19 after the first run printed False; a scalar, the
     lemma's content unchanged];
 L6  every 3 x 3 matrix Y(S), S in the span of E12 and E21, with left null vector (-i, 0, 1) for all Mw is a multiple
     of Y(E12) (so the lemma needs the nilpotent limit exactly, and a diagonal or E21 part moves the light direction).
    python3 lemma.py > lemma_run.txt"""
import sympy as sp
I = sp.I
QI = sp.Matrix([[I, 0], [0, -I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI * QJ; EPS = QJ
BLOCKS = [QJ, QI, QK]
m = sp.symbols("m11 m12 m21 m22"); Mw = sp.Matrix([[m[0], m[1]], [m[2], m[3]]])
def Y(S):
    return sp.Matrix(3, 3, lambda a, b: sp.expand(sum((BLOCKS[a].T * EPS * S * BLOCKS[b])[i, j] * Mw[i, j] for i in range(2) for j in range(2))))
E12 = sp.Matrix([[0, 1], [0, 0]]); E21 = sp.Matrix([[0, 0], [1, 0]])
uS = sp.Matrix([-I, 0, 1]); uSt = sp.Matrix([I, 0, 1])
Y12, Y21 = Y(E12), Y(E21)
print("L1: u^H Y(E12) = %s; det Y(E12) = %s; the 2 x 2 minors' gcd: %s" % ((uS.H * Y12).applyfunc(sp.simplify).T, sp.factor(Y12.det()),
      sp.factor(sp.gcd_list([Y12.extract([0, 1], [0, 1]).det(), Y12.extract([1, 2], [1, 2]).det(), Y12.extract([0, 2], [0, 2]).det()]))))
print("L2: u^H Y(E21) = %s; det Y(E21) = %s" % ((uSt.H * Y21).applyfunc(sp.simplify).T, sp.factor(Y21.det())))
print("L3: <u_S, u_S~> = %s" % sp.simplify((uS.H * uSt)[0]))
print("L4: eps conj(Q) eps^T = Q for QI, QJ, QK: %s" % [sp.simplify(EPS * Q.conjugate() * EPS.T - Q) == sp.zeros(2) for Q in (QI, QJ, QK)])
c1 = sp.symbols("c1"); S = c1 * QJ + (-I * c1) * QK; St = EPS * S.conjugate() * EPS.T
print("L5: S = 2 c1 E12: %s; its conjugate reading = -2 conj(c1) E21: %s" % (sp.simplify(S - 2 * c1 * E12) == sp.zeros(2), sp.simplify(St + 2 * sp.conjugate(c1) * E21) == sp.zeros(2)))
a, b, d = sp.symbols("a b d")
Yg = Y(a * E12 + b * E21 + d * QI)
cond = sp.Poly(sp.expand((uS.H * Yg)[0, 0]), *m).coeffs() + sp.Poly(sp.expand((uS.H * Yg)[0, 1]), *m).coeffs() + sp.Poly(sp.expand((uS.H * Yg)[0, 2]), *m).coeffs()
print("L6: u_S^H Y(a E12 + b E21 + d QI) = 0 for every Mw requires: %s" % sp.solve(cond, [b, d], dict=True))
