import sympy as sp
I=sp.I
QI=sp.Matrix([[I,0],[0,-I]]); QJ=sp.Matrix([[0,1],[-1,0]]); QK=QI*QJ; EPS=QJ
BL=[QJ,QI,QK]
m00,m01,m10,m11=sp.symbols('m00 m01 m10 m11')
t00,t01,t10,t11=sp.symbols('t00 t01 t10 t11')
M=sp.Matrix([[m00,m01],[m10,m11]]); T=sp.Matrix([[t00,t01],[t10,t11]])
Y=sp.zeros(3,3)
for a,Ca in enumerate(BL):
    for b,Cb in enumerate(BL):
        A=Ca.T*EPS*T*Cb
        Y[a,b]=sp.expand(sum(A[i,j]*M[i,j] for i in range(2) for j in range(2)))
for pos in (t00,t01,t10,t11):
    print("== big entry", pos)
    # linear coefficient of pos in each Y entry
    co=[[sp.expand(Y[a,b].coeff(pos)) for b in range(3)] for a in range(3)]
    for row in co: print("   ", row)
    # quadratic coefficient of pos^2 in each 2x2 minor
    qs=[]
    for r in [(0,1),(0,2),(1,2)]:
        for c in [(0,1),(0,2),(1,2)]:
            mnr=sp.expand(Y.extract(list(r),list(c)).det())
            qs.append(sp.factor(sp.expand(mnr).coeff(pos,2)))
    print("   pos^2 coefficients of the minors:", qs)
