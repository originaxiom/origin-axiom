import sympy as sp
I=sp.I
QI=sp.Matrix([[I,0],[0,-I]]); QJ=sp.Matrix([[0,1],[-1,0]]); QK=QI*QJ; EPS=QJ
BL=[QJ,QI,QK]
m00,m01,m10,m11,s00,s01,s10=sp.symbols('m00 m01 m10 m11 s00 s01 s10')
M=sp.Matrix([[m00,m01],[m10,m11]]); S=sp.Matrix([[s00,s01],[s10,-s00]])
Y=sp.zeros(3,3)
for a,Ca in enumerate(BL):
    for b,Cb in enumerate(BL):
        A=Ca.T*EPS*S*Cb
        Y[a,b]=sp.expand(sum(A[i,j]*M[i,j] for i in range(2) for j in range(2)))
sp.pprint(Y)
print("det Y =", sp.factor(Y.det()))
# 2x2 minors
mins=[]
for r in [(0,1),(0,2),(1,2)]:
    for c in [(0,1),(0,2),(1,2)]:
        mins.append(sp.factor(Y.extract(list(r),list(c)).det()))
for x in mins: print(x)
