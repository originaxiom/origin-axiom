"""Park eq (32): the quantum A-polynomial of m(5_2), transcribed, and the recursion it gives
for the blocks f_j of F^+_{m(5_2)} = x^{1/2} sum_j f_j(q) x^j.
Controls: it must reproduce the printed f_2 and f_3."""
import sympy as sp
x,Q = sp.symbols('x Q')          # q = Q^2, so q^{1/2} = Q
q = Q**2

a0 = -q**9*x**7*(q**3*x+1)*(q**5*x**2-1)*(q**7*x**2-1)
a1 = (Q**11*x**2*(q*x+1)*(q**3*x+1)*(q**7*x-1)
      *(q**9*x**6+q**8*x**6-q**8*x**4-3*q**7*x**5-q**7*x**4-q**6*x**5
        +2*q**6*x**4+2*q**6*x**3+q**5*x**4-q**5*x**2-q**4*x**3-q**3*x**4
        -q**3*x**3+q**3*x**2+2*q**2*x**3+2*q**2*x**2-q*x**2-2*q*x+1))
a2 = (-q**2*(q**2*x-1)*(q**2*x+1)*(q*x**2-1)*(q**7*x**2-1)
      *(q**12*x**6+q**11*x**5-2*q**10*x**5-3*q**9*x**4+2*q**8*x**4-q**8*x**3
        +2*q**7*x**3-q**6*x**4-4*q**6*x**3-q**5*x**3-3*q**5*x**2+q**4*x**3
        +2*q**4*x**2+q**3*x-q**2*x**2-2*q**2*x+1))
a3 = (Q*(q*x**2-1)*(q*x+1)*(q**3*x+1)
      *(q**16*x**6-2*q**13*x**5-q**13*x**4+q**11*x**4+2*q**10*x**4+2*q**10*x**3
        -q**9*x**4-q**8*x**3-q**8*x**2-q**7*x**3-q**7*x**2+2*q**6*x**3+2*q**6*x**2
        +q**5*x**2-q**3*x**2-3*q**3*x-q**2*x+q+1))
a4 = (q*x+1)*(q*x**2-1)*(q**3*x**2-1)
A=[sp.expand(a0),sp.expand(a1),sp.expand(a2),sp.expand(a3),sp.expand(a4)]
DEG=[int(sp.degree(a,x)) for a in A]
print("x-degrees of a_0..a_4:",DEG)
COEF=[{int(d):sp.expand(sp.Poly(a,x).coeff_monomial(x**d)) for d in range(int(sp.degree(a,x))+1)} for a in A]
DMAX=max(DEG)
print("max x-degree:",DMAX)
# recursion: coefficient of x^{n+1/2} in sum_i a_i(x) yhat^i F  = sum_i sum_d a_{i,d} f_{n-d} q^{i(n-d+1/2)} = 0
def rec_row(n):
    """returns dict j -> coefficient (sympy in Q) for the equation at x^{n+1/2}"""
    row={}
    for i in range(5):
        for d,c in COEF[i].items():
            j=n-d
            if j<0: continue
            # q^{i(j+1/2)} = Q^{2i j + i}
            row[j]=sp.expand(row.get(j,0)+c*Q**(2*i*j+i))
    return {j:sp.cancel(v) for j,v in row.items() if sp.simplify(v)!=0}
for n in range(0,4):
    r=rec_row(n)
    print("eq at x^{%d+1/2}: involves f_j for j in %s"%(n,sorted(r)))
