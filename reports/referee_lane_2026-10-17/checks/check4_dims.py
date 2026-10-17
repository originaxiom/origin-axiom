"""Check 4: Theorem 9(3): dim M_k(rho) for rho = chi_eta^21 (x) rho_u at k = -1/2, 3/2, ..., 27/2.
Method: f in M_k(rho) <=> F = eta^3 f in M_{k+3/2}(rho_u) with the (theta3^2+theta4^2)-component vanishing at the cusp.
M_K(rho_u) = vector-valued forms (F1,F2,F3), F_i degree-K polynomials in X=theta2^2, Y=theta3^2, Z=theta4^2 mod Y^2 = X^2+Z^2,
with F(tau+1) = rho_u(t) F and F(-1/tau) = rho_u(s) tau^K F."""
import sympy as sp
X, Y, Z = sp.symbols('X Y Z')
I = sp.I

def basis(K):
    return [X**a * Y**b * Z**c for b in (0, 1) for a in range(K - b + 1) for c in [K - b - a]]

def reduce_poly(p):
    # reduce modulo Y^2 -> X^2 + Z^2
    p = sp.expand(p)
    while True:
        q = sp.expand(p.subs(Y**2, X**2 + Z**2))
        q = sp.expand(sp.Poly(q, Y).as_expr())
        # substitute all even powers of Y
        q2 = sp.expand(q)
        changed = False
        for term in sp.Add.make_args(q2):
            pw = sp.degree(term, Y)
            if pw >= 2:
                changed = True
        if not changed: return q2
        # generic reduction: replace Y^n by Y^(n mod 2) * (X^2+Z^2)^(n//2)
        q3 = 0
        for term in sp.Add.make_args(q2):
            pw = sp.degree(term, Y)
            q3 += term / Y**pw * Y**(pw % 2) * (X**2 + Z**2)**(pw // 2)
        p = sp.expand(q3)
        if all(sp.degree(t, Y) < 2 for t in sp.Add.make_args(p)): return p

def dims(K):
    B = basis(K); n = len(B)
    cs = sp.symbols(f'c0:{3*n}')
    F = [sum(cs[i*n + j] * B[j] for j in range(n)) for i in range(3)]
    def T(p): return p.subs({X: I*X, Y: Z, Z: Y}, simultaneous=True)
    def S(p): return (-I)**K * p.subs({X: Z, Z: X}, simultaneous=True)
    eqs = [T(F[0]) - I*F[0], T(F[1]) - F[2], T(F[2]) - F[1],
           S(F[0]) + I*F[2], S(F[1]) + I*F[1], S(F[2]) + I*F[0]]
    rows = []
    for e in eqs:
        e = reduce_poly(e)
        P = sp.Poly(e, X, Y, Z)
        for mon, coeff in P.terms():
            rows.append([sp.expand(coeff).coeff(c) for c in cs])
    M = sp.Matrix(rows)
    null = M.nullspace()
    dimK = len(null)
    # constant-term functional on F2 + F3 at X=0, Y=1, Z=1
    vals = []
    for v in null:
        sub = {cs[i]: v[i] for i in range(3*n)}
        ct = (F[1] + F[2]).subs(sub).subs({X: 0, Y: 1, Z: 1})
        vals.append(sp.simplify(ct))
    r = 1 if any(val != 0 for val in vals) else 0
    return dimK, dimK - r

for K in range(1, 16, 2):
    dK, dk = dims(K)
    print(f"K = k+3/2 = {K:2d} (k = {K-3/2:5.1f}): dim M_K(rho_u) = {dK},  dim M_k(rho) = {dk}")
print("paper: 0,0,1,1,2,2,3,3 at k = -1/2, 3/2, ..., 27/2")
