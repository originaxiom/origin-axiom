"""Audit check: the root W = LR has commutant Z[W] = Z[F'] with F' = W - I = [[0,1],[1,1]] (F'^2 = W), i.e. B517's own
ring Z[phi]. Run B517's coefficient scan {0..3}^4 in B517's own basis {I, F'} (C = c0 I + c1 F', D = d0 I + d1 F'),
with the thread W on the diagonal, as chat1's S3 does but in this basis."""
import sympy as sp, mpmath as mp
mp.mp.dps = 50
x = sp.symbols('x')
W = sp.Matrix([[1, 1], [1, 2]]); Fp = W - sp.eye(2); I2 = sp.eye(2)
assert Fp * Fp == W
hits = []
for c0 in range(4):
    for c1 in range(4):
        for d0 in range(4):
            for d1 in range(4):
                C = c0 * I2 + c1 * Fp; D = d0 * I2 + d1 * Fp
                if C in (sp.zeros(2), I2) or D in (sp.zeros(2), I2): continue
                T = sp.Matrix(sp.BlockMatrix([[W, C], [D, W]]))
                p = sp.Poly(T.charpoly(x).as_expr(), x)
                if not p.is_irreducible: continue
                r = mp.polyroots([int(c) for c in p.all_coeffs()], maxsteps=200, extraprec=200)
                big = [z for z in r if abs(z) > 1]
                if len(big) == 1 and abs(mp.im(big[0])) < 1e-30 and mp.re(big[0]) > 1 and all(abs(z) < 1 for z in r if abs(z) <= 1):
                    hits.append(((c0, c1, d0, d1), str(p.as_expr()), abs(int(p.all_coeffs()[-1])) == 1))
print("root LR, B517 basis {I, F'}: hits", len(hits))
for h in hits: print(" ", h)
