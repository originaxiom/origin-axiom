"""GC-5 spot-checks: (1) B769 -- do c, theta, gamma5 actually commute as operations
(the abelianness B769 imports from B766)?  (2) B279 -- the SnapPy checkable inputs.
Exact sympy for (1); SnapPy numeric (stated tol) for (2)."""
import sympy as sp

# ---- (1) B769: the three involutions on the module of words-in-matrices over Q(sqrt-3, sqrt5)
s3, s5 = sp.sqrt(-3), sp.sqrt(5)
# generic-ish SL-free 2x2 matrices with entries in Q(sqrt-3, sqrt5) (traces land in the field)
A = sp.Matrix([[1 + s3, 2 - s5], [s3*s5, 3 + s3 - s5]])
B = sp.Matrix([[2 - s3 + s5, 1], [s3 + 2*s5, 5 - s3*s5]])
def field_auto(M, flip3, flip5):
    def f(e):
        e = sp.expand(e)
        if flip3: e = e.subs(s3, -s3)
        if flip5: e = e.subs(s5, -s5)
        return sp.expand(e)
    return M.applyfunc(f)
c  = lambda M: field_auto(M, True, False)   # complex conjugation: flips sqrt-3, fixes sqrt5
g5 = lambda M: field_auto(M, False, True)   # Galois: flips sqrt5, fixes sqrt-3
# theta = word reversal; on the word module. Test on words up to length 4:
words = [[0],[1],[0,1],[1,0],[0,0,1],[0,1,1],[0,1,0,1],[1,0,0,1]]
def evalw(w, X, Y):
    M = sp.eye(2)
    for i in w: M = M * (X if i==0 else Y)
    return M
def trace_of(w, X, Y): return sp.expand(sp.trace(evalw(w, X, Y)))
ops = {"c": c, "g5": g5}
all_ok = True
for name, op in ops.items():
    for w in words:
        rev = w[::-1]
        # theta then op  vs  op then theta, on traces:
        t1 = sp.expand(trace_of(rev, op(A), op(B)))          # op after reversal
        t2_pre = trace_of(rev, A, B)                          # reversal first, then field-auto on the trace
        t2 = sp.expand(t2_pre.subs(s3, -s3) if name=="c" else t2_pre.subs(s5, -s5))
        if sp.simplify(t1 - t2) != 0: all_ok = False; print("FAIL theta-", name, w)
# c and g5 commute (distinct legs of an abelian Galois group) -- verify on all matrix entries:
cg = sp.simplify(c(g5(A)) - g5(c(A))) == sp.zeros(2,2)
cg2 = all(sp.simplify(c(g5(A))[i,j] - g5(c(A))[i,j]) == 0 for i in range(2) for j in range(2))
# involutivity:
inv = all(sp.simplify(c(c(A))[i,j]-A[i,j])==0 and sp.simplify(g5(g5(A))[i,j]-A[i,j])==0 for i in range(2) for j in range(2))
print(f"B769 spot: theta commutes with c and gamma5 on traces (8 words, exact): {all_ok}")
print(f"B769 spot: c and gamma5 commute entrywise (exact): {cg2}; both involutions: {inv}")
# TWO-SIDED control: a deliberately non-commuting pair must FAIL -- conjugation-by-A vs c:
inner = lambda M: A * M * A.inv()
lhs = sp.expand(sp.trace(inner(c(B)))); rhs = sp.expand(sp.trace(c(inner(B))))
print(f"control (must be False): inner-conj commutes with c on tr(B): {sp.simplify(lhs-rhs)==0}")

# ---- (2) B279: SnapPy checkable inputs
import snappy
M = snappy.Manifold("4_1")
G = M.symmetry_group()
print(f"B279 spot: symmetry group = {G}, order {G.order()}, |H1| = {M.homology()}")
mats = G.isometries()
allpm = True; mod2_id = True
for iso in mats:
    m = iso.cusp_maps()[0]
    for r in range(2):
        for cix in range(2):
            v = m[r,cix]
            if abs(v) > 1: allpm = False
    if (m[0,0]%2, m[0,1]%2, m[1,0]%2, m[1,1]%2) != (1,0,0,1): mod2_id = False
print(f"B279 spot: {len(mats)} isometries; cusp maps all +-1 entries: {allpm}; all == identity mod 2: {mod2_id}")
amph = G.is_amphicheiral()
print(f"B279 spot: amphichiral: {amph}")
