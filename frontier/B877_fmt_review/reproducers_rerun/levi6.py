import os
import io, contextlib, sympy as sp
from sympy.polys.matrices import DomainMatrix
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'B854_centralizer_exact', 'e6_centralizer.py')).read(),'b854','exec'), globals())
print("rebuilt", flush=True)
t, rho = sp.symbols('t rho'); G = {n: sp.Matrix(ADS[n]) for n in ns}
def restrict(M, Nb):
    NT = Nb.T; return (NT*Nb).inv() * (NT*(M*Nb))
p = DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ).charpoly()
P = sp.Poly([sp.Rational(c) for c in p], t)
r = sp.div(P, sp.gcd(P, P.diff(t)))[0]
facs = [f for f,_ in sp.factor_list(r)[1] if f.degree() > 1]
D14=DomainMatrix.from_Matrix(G[14]).convert_to(sp.QQ)
mx=max(f.degree() for f in facs)
pows=[sp.eye(78)]; acc=DomainMatrix.eye(78, sp.QQ)
for k in range(1,mx+1): acc=acc*D14; pows.append(acc.to_Matrix())
mu = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)
print("mu coefficient factorizations:", {str(c): sp.factorint(abs(c)) for c in mu.all_coeffs()}, flush=True)
print("mu real roots:", [sp.nstr if 0 else str(sp.N(rt,25)) for rt in sp.real_roots(mu)], flush=True)
for f in facs:
    cs=f.all_coeffs()[::-1]; Pf=sp.zeros(78,78)
    for k,c in enumerate(cs):
        if c: Pf += sp.Rational(c)*pows[k]
    Nb=sp.Matrix.hstack(*Pf.nullspace()); d=Nb.shape[1]
    if d not in (12,36): continue
    R8, R16 = restrict(G[8],Nb), restrict(G[16],Nb)
    det = sp.Poly((R8 + rho*R16).det(method='berkowitz'), rho)
    k = d//3
    q, rem = sp.div(det, mu**k)
    print(f"block {d}: det degree {det.degree()};  det == c*mu^{k}: {rem == 0 and q.degree()==0}", flush=True)
    if rem != 0 or q.degree()!=0:
        fl = sp.factor_list(det)[1]
        print("   factorization degrees:", [(g.degree(), m) for g,m in fl], flush=True)
        print("   mu multiplicity:", next((m for g,m in fl if sp.div(sp.Poly(g,rho),mu)[1]==0 or sp.Poly(g,rho).as_expr().equals(mu.as_expr())), 0), flush=True)
print("DONE", flush=True)
