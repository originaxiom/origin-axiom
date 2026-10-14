"""Audit check: the like-for-like comparison. B517's A3 used the fixed shape (S, S^2) on metallic half-ticks
S_m = [[m,1],[1,0]]. Apply to the metallic half-ticks the same criteria chat1 applied to threads:
shape (S, S+I), and B517's coefficient scan {0..3}^4 (C = c0 I + c1 S, D = d0 I + d1 S, not 0, not I)."""
import sympy as sp, mpmath as mp
mp.mp.dps = 50
x = sp.symbols('x')
def test(W, C, D):
    T = sp.Matrix(sp.BlockMatrix([[W, C], [D, W]]))
    p = sp.Poly(T.charpoly(x).as_expr(), x)
    roots = mp.polyroots([int(c) for c in p.all_coeffs()], maxsteps=200, extraprec=200)
    big = [r for r in roots if abs(r) > 1]
    pis = (len(big) == 1 and abs(mp.im(big[0])) < mp.mpf(10)**-30 and mp.re(big[0]) > 1
           and all(abs(r) < 1 for r in roots if abs(r) <= 1))
    return bool(p.is_irreducible and pis), abs(int(p.all_coeffs()[-1])) == 1, sorted([float(abs(r)) for r in roots], reverse=True)
I2 = sp.eye(2)
for m in range(1, 7):
    S = sp.Matrix([[m, 1], [1, 0]])
    a3 = test(S, S, S * S)
    s2 = test(S, S, S + I2)
    hits = []
    for c0 in range(4):
        for c1 in range(4):
            for d0 in range(4):
                for d1 in range(4):
                    C = c0 * I2 + c1 * S; D = d0 * I2 + d1 * S
                    if C in (sp.zeros(2), I2) or D in (sp.zeros(2), I2): continue
                    ok, unit, _ = test(S, C, D)
                    if ok: hits.append((c0, c1, d0, d1, unit))
    print(f"m={m}: A3 shape (S,S^2) Pisot-irr {a3[0]} mags {[round(v,4) for v in a3[2]]} | shape (S,S+I) {s2[0]} unit {s2[1]} mags {[round(v,4) for v in s2[2]]} | scan hits {len(hits)} (unit {sum(h[4] for h in hits)}): {hits[:6]}", flush=True)
