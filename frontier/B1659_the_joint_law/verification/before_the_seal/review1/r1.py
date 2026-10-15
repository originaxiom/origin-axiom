import sympy as sp, numpy as np
s=sp.symbols("s0:4"); m=sp.symbols("m0:4")
S=sp.Matrix(2,2,s); M=sp.Matrix(2,2,m)
I=sp.I
qi=sp.Matrix([[I,0],[0,-I]]); qj=sp.Matrix([[0,1],[-1,0]]); qk=qi*qj
C=[qj,qi,qk]; eps=qj
Y=sp.Matrix(3,3,lambda a,b: sum((C[a].T*eps*S*C[b]).multiply_elementwise(M))).applyfunc(sp.expand)
d=Y.det()
ell=(eps*S*M.T).trace()
print("J1 resid:",sp.expand(d-4*S.det()*M.det()*ell))
print("qk",qk)
m0,m1,m2,m3=m
A=sp.Matrix([[m0**2+m1**2+m2**2+m3**2,2*I*(m0*m2+m1*m3),-I*(m0**2+m1**2-m2**2-m3**2)],
 [2*I*(m0*m1+m2*m3),-4*m1*m2,2*(m0*m1-m2*m3)],
 [-I*(m0**2-m1**2+m2**2-m3**2),2*(m0*m2-m1*m3),-m0**2+m1**2+m2**2-m3**2]])
sub=dict(zip(m,s))
P=sp.diag(1,-1,-1)
print("J2:",(Y.adjugate()-S.det()*A-M.det()*P*A.subs(sub,simultaneous=True)).applyfunc(sp.expand)==sp.zeros(3,3))
print("J2 without P:",(Y.adjugate()-S.det()*A-M.det()*A.subs(sub,simultaneous=True)).applyfunc(sp.expand)==sp.zeros(3,3))
# row/col structure of Y
print(Y.subs({s[0]:1,s[1]:0,s[2]:0,s[3]:1}))
# irreducibility of det, remainder argument: check Y itself bilinear? degree
print(sp.factor(S.det()), sp.Poly(S.det(),*s).total_degree())
# symmetric? swap S<->M
Yt=Y.subs(dict(zip(s+m,m+s)),simultaneous=True)
print("Y(S,M) vs Y(M,S)^T/Y:",(Y-Yt).applyfunc(sp.expand), )
print("Y(S,M)=Y(M,S)?",(Y-Yt).applyfunc(sp.expand)==sp.zeros(3,3), "transpose?",(Y-Yt.T).applyfunc(sp.expand)==sp.zeros(3,3))
print(sp.simplify(Y))
