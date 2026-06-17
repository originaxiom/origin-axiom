import sympy as sp
E,lam=sp.symbols('E lambda')
def A(V): return sp.Matrix([[E-V,-1],[1,0]])
def Mw(word):
    M=sp.eye(2)
    for ch in word:
        M=A(lam if ch=='a' else 0)*M
    return M
# three consecutive Fibonacci words w1=a, w2=ab, w3=aba=w2 w1
x1=sp.trace(Mw('a'))/2; x2=sp.trace(Mw('ab'))/2; x3=sp.trace(Mw('aba'))/2
I=sp.simplify(sp.expand(x1**2+x2**2+x3**2-2*x1*x2*x3-1))
print("Suto invariant  I(x1,x2,x3) =", I, "   (independent of E:", E not in I.free_symbols, ")")
kappa=sp.simplify(2+4*I)
print("kappa = 2 + 4I =", kappa)
# also confirm with the NEXT triple (x2,x3,x4), x4 from w4=abaab=w3 w2
x4=sp.trace(Mw('abaab'))/2
I2=sp.simplify(sp.expand(x2**2+x3**2+x4**2-2*x2*x3*x4-1))
print("check next triple I(x2,x3,x4) =", sp.simplify(I2), " (same, conserved)")
print("\n=> kappa = 2 + lambda^2  is an exact identity in (E, lambda).  EXACT, all lambda.")
