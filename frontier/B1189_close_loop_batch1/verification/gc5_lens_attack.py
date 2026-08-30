"""INSTRUMENT lens attack on GC-5.
A) Is the v1 'inner-conjugation control' (cited in evidence as part of the two-sided
   control) mathematically valid?  With a CORRECT c, trace conjugation-invariance
   predicts tr(inner(c(B))) == tr(c(inner(B))) -> True, i.e. the control CANNOT
   discriminate; its printed False could only be the subs bug.
B) BITE control for the entrywise c/g5 commutation leg (the leg whose only cited
   control was the buggy v1 run): a deliberately non-commuting pair
   (c = flip r3) vs (swap r3<->r5) must FAIL entrywise commutation.
C) BITE control for the trace-identity leg with a multiplicative-but-not-additive
   map (e -> e with r3 -> r3*r5)? keep to the swap map on traces as well.
All exact sympy, formal symbols reduced mod (r3^2+3, r5^2-5)."""
import sympy as sp
r3, r5 = sp.symbols("r3 r5")
def red(e):
    p = sp.Poly(sp.expand(e), r3, r5)
    q = {}
    for (i, j), coef in p.terms():
        s = coef * (-3)**(i//2) * 5**(j//2)
        q[(i % 2, j % 2)] = q.get((i % 2, j % 2), 0) + s
    return sp.expand(sum(v * r3**a * r5**b for (a, b), v in q.items()))
A = sp.Matrix([[1 + r3, 2 - r5], [r3*r5, 3 + r3 - r5]])
B = sp.Matrix([[2 - r3 + r5, 1], [r3 + 2*r5, 5 - r3*r5]])
c  = lambda M: M.applyfunc(lambda e: red(e.subs(r3, -r3)))

# A) correct-c version of the v1 control
Ainv = A.inv()
inner = lambda M: (A * M * Ainv).applyfunc(lambda e: red(sp.cancel(e)))
lhs = red(sp.cancel(sp.trace(inner(c(B)))))
rhs = red(sp.cancel(sp.trace(c(inner(B)))))
print(f"A) v1-control with CORRECT c -- tr(inner(c(B))) == tr(c(inner(B))): {sp.simplify(lhs-rhs)==0}  (True => v1 control was constitutionally unable to discriminate; its False was the bug)")

# B) genuine BITE for entrywise commutation: c vs swap(r3<->r5)
swap = lambda M: M.applyfunc(lambda e: red(e.subs({r3: r5, r5: r3}, simultaneous=True)))
comm = all(sp.simplify(c(swap(A))[i,j] - swap(c(A))[i,j]) == 0 for i in range(2) for j in range(2))
print(f"B) BITE entrywise: c commutes with swap(r3,r5): {comm}  (must be False)")

# C) same non-commuting pair detected on the trace module too?
def trw(w, X, Y):
    M = sp.eye(2)
    for i in w: M = M * (X if i == 0 else Y)
    return red(sp.trace(M))
t1 = trw([0,1], c(swap(A)), c(swap(B)))
t2 = trw([0,1], swap(c(A)), swap(c(B)))
print(f"C) BITE on traces: tr_ab under c.swap vs swap.c equal: {sp.simplify(t1-t2)==0}  (must be False)")
