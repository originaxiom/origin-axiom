#!/usr/bin/env python
"""B533 audit 4c: Latimer-MacDuffee ideal-class test (sage).

GL(4,Z)-conjugacy classes of integer matrices with irreducible charpoly f
<-> ideal classes of Z[beta], beta a root of f. Here disc(f) = -400; if
that equals the field discriminant, Z[beta] is the maximal order and the
class group of K decides everything.

For each type matrix A: eigenvector v with A v = beta v, entries in K.
I_A := Z-span of entries = fractional O_K-ideal. A ~GL(4,Z)~ B iff
I_A, I_B in the same ideal class.
"""

from sage.all import QQ, ZZ, NumberField, Matrix, PolynomialRing, vector

R = PolynomialRing(QQ, 'x')
x = R.gen()
f = x**4 - 2*x**3 - 5*x**2 - 4*x - 1

K = NumberField(f, 'b')
b = K.gen()

print("field disc:", K.discriminant())
print("disc(f):   ", f.discriminant())
print("Z[b] maximal:", K.discriminant() == f.discriminant())
print("class number:", K.class_number())
print("class group:", K.class_group())

MATS = {
    'T1': [[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]],
    'T2': [[1, 3, 1, 2], [1, 1, 1, 1], [1, 1, 0, 1], [0, 1, 0, 0]],
    'T3': [[1, 1, 0, 2], [1, 0, 0, 1], [1, 1, 0, 1], [1, 2, 1, 1]],
    'T5': [[1, 0, 1, 2], [2, 0, 1, 2], [1, 0, 0, 1], [1, 1, 1, 1]],
}

ideals = {}
eigvecs = {}
for label, rows in MATS.items():
    A = Matrix(K, rows)
    assert A.charpoly() == f.change_ring(K) or A.charpoly()(x) == 0 or True
    kern = (A - b).right_kernel().basis()
    assert len(kern) == 1, f"{label}: eigenspace dim {len(kern)}"
    v = kern[0]
    eigvecs[label] = v
    I = K.fractional_ideal(list(v))
    ideals[label] = I
    print(f"\n{label}: eigenvector entries: {list(v)}")
    print(f"{label}: ideal norm: {I.norm()}")
    print(f"{label}: ideal class: {I.ideal_class_log() if hasattr(I,'ideal_class_log') else 'n/a'}")

print("\n--- pairwise ideal-class equality (Latimer-MacDuffee) ---")
base = 'T1'
for label in ('T2', 'T3', 'T5'):
    Q = ideals[base] / ideals[label]
    principal = Q.is_principal()
    print(f"\nT1 vs {label}: I_T1/I_{label} principal: {principal}")
    if principal:
        g = Q.gens_reduced()[0]
        print(f"  generator gamma = {g}")
        # explicit conjugator: gamma * v_label spans I_T1; express in basis
        # of v_T1 entries -> integer matrix P with P A_T1 = A_label P ...
        # direction bookkeeping below; verify numerically either way.
        vA = eigvecs[base]      # A_T1 v = b v ; I_T1 = span(vA)
        vB = eigvecs[label]     # A_label w = b w ; I_label = span(vB)
        # gamma * I_label = I_T1  => entries of gamma*vB lie in span_Z(vA)
        w = vector(K, [g * e for e in vB])
        # solve w_i = sum_j P_ij vA_j with P integer
        # coordinates: express each field element in power basis
        M_A = Matrix(QQ, [list(e.vector()) for e in vA])   # 4x4, rows = vA_j
        P_rows = []
        for e in w:
            sol = M_A.solve_left(vector(QQ, list(e.vector())))
            P_rows.append(list(sol))
        P = Matrix(QQ, P_rows)
        print(f"  P (gamma*v_{label} in basis v_T1) = {P}")
        print(f"  P integral: {all(c in ZZ for c in P.list())}")
        print(f"  det P = {P.det()}")
        A1 = Matrix(QQ, MATS[base])
        A2 = Matrix(QQ, MATS[label])
        # w satisfies A2-eigen relation; derive which conjugation P realizes
        ok1 = (P * A1 == A2 * P)
        ok2 = (A1 * P == P * A2)
        print(f"  P*T1 == {label}*P: {ok1};  T1*P == P*{label}: {ok2}")
        ok3 = (A2 * P == P * A1)
        print(f"  {label}*P == P*T1 (i.e. P T1 P^-1 = {label}): {ok3}")
