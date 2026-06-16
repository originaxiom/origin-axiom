"""ROUTE toward DERIVING k=4-m(o-3): structural probe of the exponent mechanism.

We have the EXACT figure-eight families:
  o=3 SL3: [A,B] = (unit) mu^4   (k=4)
  o=4 SL3: [A,B] = mu^3          (k=3)   [r1_fig_sl3_o4_proof.py]
mu = A^-m t. Question: WHERE does the exponent come from algebraically?

Hypothesis from B154: k = A-polynomial slope; order-determined. Structural attempt:
The longitude [A,B] with B=A^-2 t A t^-1 (m=1) is [A,B]=A B A^-1 B^-1. Expand in t,A.
The meridian mu=A^-1 t. We want [A,B] as a word in mu and A, then use A^o=I to collapse.

[A,B] = A B A^-1 B^-1 = A (A^-2 t A t^-1) A^-1 (t A^-1 t^-1 A^2)
      = A^-1 t A t^-1 A^-1 t A^-1 t^-1 A^2.
Write t = A mu (since mu=A^-1 t => t = A mu). Substitute and collapse using A^o=I; count the net power
of mu and the residual A-power (which must be I for [A,B]=c mu^k since mu,A don't commute generally...).
Actually [A,B]=c mu^k is a SPECIAL identity on the variety, not a free-group identity. So the exponent
emerges from the IDEAL, not from free reduction. We probe: express [A,B] mu^-1 and see how many factors of
mu are 'absorbed' before hitting a scalar, ON the variety, symbolically.
"""
import sympy as sp

def fig_family_o4_sl3():
    I=sp.I
    q,t22=sp.symbols("q t22")
    t11=I*t22; t00=(1+I)*t22; p=I*q; r=(1+I)*q-I*t22**2
    t=sp.Matrix([[t00,1,1],[p,t11,1],[q,r,t22]])
    A=sp.diag(1,I,-I)
    return A,t,(q,t22)

A,t,params=fig_family_o4_sl3()
Ai=sp.diag(1,-sp.I,sp.I); A2=sp.diag(1,-1,-1)
# verify on variety
S=sp.expand(t*A2*t*A-Ai*t*A*t)
print("o=4 SL3 family on variety:", all(sp.simplify(S[r,c])==0 for r in range(3) for c in range(3)))
mu=sp.expand(Ai*t)
det=sp.cancel(t.det()); u=t.adjugate()
B=sp.expand(A2*t*A*u)/det
Bi=sp.expand(t*Ai*u)/det*A2
comm=sp.Matrix(3,3,lambda r,c: sp.cancel((A*B*Ai*Bi)[r,c]))
# Track: comm * mu^-j -- when does it become scalar*I? (mu^-1 = adj(mu)/det mu)
detmu=sp.cancel(mu.det()); umu=mu.adjugate()
print("\nComputing comm * mu^-j for j=0..5 and testing scalar:")
cur=comm
for j in range(0,6):
    # is cur a scalar matrix?
    is_scalar = all(sp.simplify(cur[r,c])==0 for r in range(3) for c in range(3) if r!=c) and \
                sp.simplify(cur[0,0]-cur[1,1])==0 and sp.simplify(cur[1,1]-cur[2,2])==0
    print(f"  comm*mu^-{j} scalar? {is_scalar}" + (f"  diag={sp.simplify(cur[0,0])}" if is_scalar else ""))
    cur=sp.Matrix(3,3,lambda r,c: sp.cancel((cur*umu)[r,c])/detmu)
print("\n=> the smallest j with comm*mu^-j scalar IS k (here should be 3).")
