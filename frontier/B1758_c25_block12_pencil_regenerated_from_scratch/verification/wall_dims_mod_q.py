"""B1758 (main's re-banking): main's audit, the exact tie to B892's wall -- over GF(q) for q = 40123, 40493, 40583, 40693, dim z(x1) = 46 and, where gamma^2 = e(rho_q) and a^2 = -det14(rho_q) have roots, dim z(x1, gamma x14 - a x16) = 14 against the controls (a wrong a; a generic y: 12). Written by main's read-only auditor, carried with the B854 path made repository-relative.
"""
"""Exact GF(q) check that B1758's e(rho), det14(rho) define B892's wall: dim z(x1, y*) = 14 for y* = gamma x14 - a x16
with gamma^2 = e(rho_q), a^2 = -det14(rho_q); controls: wrong a, generic y."""
import io, contextlib, random
import sympy as sp

import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B854 = str(ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py")
src = open(B854).read()
src = src.replace("for _ in range(4000):", "for _ in range(0):").split("# ---------------------------------------------------------------- VERIFY closure")[0]
env = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "b854", "exec"), env)   # original averaging (slow path) kept, Jacobi loop skipped
br, hvec, evec, ROOTS, DIM, N, INV = (env[k] for k in ("br", "hvec", "evec", "ROOTS", "DIM", "N", "INV"))
basis = [hvec(j) if j < N else evec(ROOTS[j - N]) for j in range(DIM)]
AD = {n: [[None] * DIM for _ in range(DIM)] for n in (8, 14, 16)}
for n in (8, 14, 16):
    for j in range(DIM):
        col = br(INV[n], basis[j])
        for i in range(DIM):
            AD[n][i][j] = col[i]

def rank_mod(rows, q):
    M = [r[:] for r in rows]; rk = 0; ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] % q), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = pow(M[rk][c], -1, q)
        M[rk] = [x * inv % q for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] % q:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk

def red(fr, q):
    return fr.numerator % q * pow(fr.denominator % q, -1, q) % q

rho = sp.Symbol("rho")
MU = 500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197
det14_x = sp.Rational(9084997258444800000, 28561)*rho**2 + sp.Rational(77253378048000, 2197)*rho + sp.Rational(461060812800, 169)
e_x = -sp.Rational(752150557025548369920000, 4826809)*rho**2 + sp.Rational(159895951748628480000, 371293)*rho + sp.Rational(82022486586163200, 28561)
random.seed(1)
for q in (40123, 40493, 40583, 40693):
    Aq = {n: [[red(AD[n][i][j], q) for j in range(DIM)] for i in range(DIM)] for n in AD}
    for rq in sorted(int(z) % q for z in sp.Poly(MU, rho, modulus=q).ground_roots()):
        x1 = [[(Aq[8][i][j] + rq * Aq[16][i][j]) % q for j in range(DIM)] for i in range(DIM)]
        eq = sp.Rational(e_x.subs(rho, rq)); dq = sp.Rational(det14_x.subs(rho, rq))
        eq = eq.p % q * pow(eq.q % q, -1, q) % q; dq = dq.p % q * pow(dq.q % q, -1, q) % q
        gs = [g for g in range(1, q) if g * g % q == eq]
        as_ = [a for a in range(1, q) if a * a % q == (-dq) % q]
        k1 = DIM - rank_mod(x1, q)
        line = f"q={q} rho_q={rq}: dim z(x1)={k1}; gamma^2=e: {gs[:1]}; a^2=-det14: {as_[:2]}"
        if gs and as_:
            g, a = gs[0], as_[0]
            def nul(ycoef14, ycoef16):
                y = [[(ycoef14 * Aq[14][i][j] - ycoef16 * Aq[16][i][j]) % q for j in range(DIM)] for i in range(DIM)]
                return DIM - rank_mod(x1 + y, q)
            abad = next(b for b in range(2, q) if (b * b + dq) % q)   # a with a^2 != -det14
            line += f" | z(x1,y*)={nul(g, a)}  z(x1, g x14 + a x16)={nul(g, (-a) % q)}  ctrl wrong-a={nul(g, abad)}  ctrl generic={nul(1, random.randrange(2, q))}"
        print(line, flush=True)
