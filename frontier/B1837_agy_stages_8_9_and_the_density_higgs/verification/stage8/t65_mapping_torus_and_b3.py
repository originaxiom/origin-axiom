"""S302 check of the lane's Theorem 65 (value-free parts, main's side):
(a) the monodromy facts: A = LR = [[2,1],[1,1]], tr 3, |det(I - A)| = 1, eigenvalues phi^{+-2}; A^3, tr, |det(I - A^3)|;
(b) SnapPy: m004 = b++LR; its 3-fold cyclic cover is the bundle of A^3 (b++LRLRLR), volume 3 Vol(m004), and
    Vol(m004) = 2 Cl_2(pi/3);
(c) |b_3| = 11 - (2/3) n_f with n_f = 2 N_gen = 6 -> 7 (an SM input: N_c = 3, N_gen = 3);
(d) the 'collapse' a*V - b3*ln T - b3*k*V == b3*(V - ln T) holds identically iff a = b3*(k + 1), i.e. it is a constraint
    on the posited integers (B22's a and B23's k), not a derivation: list the (a, k) it allows for b3 = 7.
No SM value enters."""
from fractions import Fraction as F
import numpy as np
import mpmath as mp
import sympy as sp
import snappy

dev = []
A = np.array([[2, 1], [1, 1]]); A3 = A @ A @ A; I2 = np.eye(2, dtype=int)
phi = (1 + 5 ** 0.5) / 2
facts = {"tr A": int(np.trace(A)), "|det(I-A)|": abs(round(np.linalg.det(I2 - A))), "A^3": A3.tolist(),
         "tr A^3": int(np.trace(A3)), "|det(I-A^3)|": abs(round(np.linalg.det(I2 - A3)))}
ev = np.sort(np.linalg.eigvals(A.astype(float)))
dev.append(("eigenvalues vs phi^-2, phi^2", max(abs(ev[0] - phi ** -2), abs(ev[1] - phi ** 2))))
print("monodromy facts:", facts)

M = snappy.Manifold("m004"); B = snappy.Manifold("b++LR")
print("m004 isometric to b++LR:", M.is_isometric_to(B))
covs = M.covers(3, cover_type="cyclic")
print("number of 3-fold cyclic covers of m004:", len(covs))
C3 = covs[0]
print("cyclic 3-cover isometric to b++LRLRLR (bundle of A^3):", C3.is_isometric_to(snappy.Manifold("b++LRLRLR")),
      "; tetrahedra:", C3.num_tetrahedra(), "; H1:", C3.homology())
dev.append(("Vol(M3) - 3 Vol(m004)", abs(float(C3.volume()) - 3 * float(M.volume()))))
mp.mp.dps = 30
cl2 = mp.clsin(2, mp.pi / 3)
dev.append(("Vol(m004) - 2 Cl2(pi/3)", abs(float(M.volume()) - 2 * float(cl2))))

nf = 2 * 3
b3 = F(11) - F(2, 3) * nf
print("|b3| = 11 - (2/3)*n_f, n_f = 6:", b3, "; = 11 - (4/3)*N_gen at N_gen = 3:", F(11) - F(4, 3) * 3)

a, k, b, V, T = sp.symbols("a k b V T")
expr = sp.expand(a * V - b * sp.log(T) - b * k * V - b * (V - sp.log(T)))
print("lhs - rhs =", sp.factor(expr), " -> identity iff a = b*(k + 1)")
print("with b3 = 7 the allowed (B22 integer a, B23 integer k):", [(7 * (kk + 1), kk) for kk in range(0, 5)])
print("the lane's pair (21, 2) is one of them: 21 = 7*(2+1):", 21 == 7 * (2 + 1))
bad = [d for d in dev if d[1] > 1e-9]
print("deviations > 1e-9:", bad if bad else "none", "; max dev", max(d[1] for d in dev))
