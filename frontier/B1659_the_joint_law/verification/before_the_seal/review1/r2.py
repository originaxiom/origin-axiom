import sympy as sp
I=sp.I
p0,p1,q0,q1=sp.symbols("p0 p1 q0 q1")
m0,m1,m2,m3=p0*q0,p0*q1,p1*q0,p1*q1
A=sp.Matrix([[m0**2+m1**2+m2**2+m3**2,2*I*(m0*m2+m1*m3),-I*(m0**2+m1**2-m2**2-m3**2)],
 [2*I*(m0*m1+m2*m3),-4*m1*m2,2*(m0*m1-m2*m3)],
 [-I*(m0**2-m1**2+m2**2-m3**2),2*(m0*m2-m1*m3),-m0**2+m1**2+m2**2-m3**2]])
pt=sp.Matrix([p0**2+p1**2,2*I*p0*p1,-I*(p0**2-p1**2)]);qt=sp.Matrix([q0**2+q1**2,2*I*q0*q1,-I*(q0**2-q1**2)])
print((A-qt*pt.T).applyfunc(sp.expand)==sp.zeros(3,3), (A-pt*qt.T).applyfunc(sp.expand)==sp.zeros(3,3))
