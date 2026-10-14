"""Audit check: B517's coupling carried to threads, with C, D required to be non-negative INTEGER MATRICES in Z[W]
(the theorem's 'nonneg-integral maps'; chat1's own docstring: 'nonnegative entries'), instead of non-negative
COEFFICIENTS in the basis {I, W}. Exact irreducibility (sympy) + Pisot test on roots at 50 digits (mpmath)."""
import sympy as sp, mpmath as mp, json, sys
mp.mp.dps = 50
x = sp.symbols('x')

def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()

Lm = sp.Matrix([[1, 0], [1, 1]]); Rm = sp.Matrix([[1, 1], [0, 1]])
def mat(word):
    M = sp.eye(2)
    for ch in word: M = M * (Lm if ch == "L" else Rm)
    return M

def classify(W, C, D):
    T = sp.Matrix(sp.BlockMatrix([[W, C], [D, W]]))
    p = sp.Poly(T.charpoly(x).as_expr(), x)
    irr = p.is_irreducible
    roots = mp.polyroots([int(c) for c in p.all_coeffs()], maxsteps=200, extraprec=200)
    mags = sorted((abs(r) for r in roots), reverse=True)
    big = [r for r in roots if abs(r) > 1]
    pis = (len(big) == 1 and abs(mp.im(big[0])) < mp.mpf(10)**-30 and mp.re(big[0]) > 1
           and all(abs(r) < 1 for r in roots if abs(r) <= 1))
    unit = abs(int(p.all_coeffs()[-1])) == 1
    return irr, pis, unit, [float(m) for m in mags], str(p.as_expr())

I2 = sp.eye(2)
out = {}
words = ["F"] + [w for w in lyndon(8) if len(w) >= 2]
for name in words:
    W = sp.Matrix([[1, 1], [1, 0]]) if name == "F" else mat(name)
    hits_coef, hits_ent = [], []
    rng0 = range(-3, 4)
    for c1 in range(4):
        for c0 in rng0:
            C = c0 * I2 + c1 * W
            if min(C) < 0 or C == sp.zeros(2) or C == I2: continue
            for d1 in range(4):
                for d0 in rng0:
                    D = d0 * I2 + d1 * W
                    if min(D) < 0 or D == sp.zeros(2) or D == I2: continue
                    irr, pis, unit, mags, poly = classify(W, C, D)
                    if irr and pis:
                        rec = [c0, c1, d0, d1, unit]
                        hits_ent.append(rec)
                        if c0 >= 0 and d0 >= 0: hits_coef.append(rec)
    out[name] = {"trace": int(W.trace()), "coef-scan hits (c0,c1,d0,d1,unit)": hits_coef,
                 "entries-scan hits (c0,c1,d0,d1,unit)": hits_ent}
    print(name, int(W.trace()), "coef hits", len(hits_coef), "unit", sum(h[4] for h in hits_coef),
          "| entries hits", len(hits_ent), "unit", sum(h[4] for h in hits_ent),
          "| negative-c0/d0 hits:", [h for h in hits_ent if h[0] < 0 or h[2] < 0][:4], flush=True)
json.dump(out, open(sys.argv[1], "w"), indent=1)
