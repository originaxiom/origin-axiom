"""GC-5 spot-check v2 (B769 commutation) -- FORMAL symbols r3, r5 with polynomial
reduction mod (r3^2+3, r5^2-5); automorphisms act on Symbols (the safe subs).
v1 used subs on sqrt(-3) (a non-Symbol) and silently misfired -- the B1174 fence class."""
import sympy as sp
r3, r5 = sp.symbols("r3 r5")   # r3 ~ sqrt(-3), r5 ~ sqrt(5)
def red(e):
    p = sp.Poly(sp.expand(e), r3, r5)
    q = {}
    for (i, j), coef in p.terms():
        s = coef * (-3)**(i//2) * 5**(j//2)
        key = (i % 2, j % 2)
        q[key] = q.get(key, 0) + s
    return sp.expand(sum(v * r3**a * r5**b for (a, b), v in q.items()))
A = sp.Matrix([[1 + r3, 2 - r5], [r3*r5, 3 + r3 - r5]])
B = sp.Matrix([[2 - r3 + r5, 1], [r3 + 2*r5, 5 - r3*r5]])
c  = lambda M: M.applyfunc(lambda e: red(e.subs(r3, -r3)))
g5 = lambda M: M.applyfunc(lambda e: red(e.subs(r5, -r5)))
def trw(w, X, Y):
    M = sp.eye(2)
    for i in w: M = M * (X if i == 0 else Y)
    return red(sp.trace(M))
words = [[0],[1],[0,1],[1,0],[0,0,1],[0,1,1],[0,1,0,1],[1,0,0,1]]
ok = True
for name, op, sym in (("c", c, r3), ("g5", g5, r5)):
    for w in words:
        rev = w[::-1]
        t1 = trw(rev, op(A), op(B))            # (op then theta) route
        t2 = red(trw(rev, A, B).subs(sym, -sym))  # (theta then op) route
        if sp.simplify(t1 - t2) != 0:
            ok = False; print("FAIL", name, w)
print(f"theta commutes with c and with gamma5 on traces (8 words to len 4, exact): {ok}")
cg = all(sp.simplify(c(g5(A))[i,j] - g5(c(A))[i,j]) == 0 for i in range(2) for j in range(2))
inv = all(sp.simplify(c(c(A))[i,j]-A[i,j]) == 0 and sp.simplify(g5(g5(A))[i,j]-A[i,j]) == 0
          for i in range(2) for j in range(2))
print(f"c.g5 == g5.c entrywise (exact): {cg}; c^2 = g5^2 = id: {inv}")
# theta^2 = id trivially (reversal of reversal). TWO-SIDED control: inner conjugation
# (non-abelian ingredient) must FAIL to commute with theta on traces of a NON-cyclic word pair?
# tr is conjugation-invariant, so instead control against a NON-automorphism map (entrywise square):
sq = lambda M: M.applyfunc(lambda e: red(e**2))
t1 = trw([0,1], sq(A), sq(B)); t2 = red(trw([0,1], A, B)**2)
print(f"control (must be False -- entrywise-square is not a hom): {sp.simplify(t1-t2)==0}")
