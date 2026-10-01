"""B1378 correction (2026-10-01): own check (exact, Q(sqrt-3)) of main's B1432 finding: the web seat's TAU2 word map on the 6-fold cyclic cover of m004 is
conjugation by a^2, and B1378's substitute is not.  Presentation of the source: <a, b | a W = W b>, W = b a^-1 b^-1 a.
Cover generators (Reidemeister-Schreier, kernel of a, b -> 1 mod 6): x1 = a^6, x_{k+2} = a^k b a^-(k+1) (k = 0..4), x7 = a^5 b."""
import sympy as sp

z = sp.symbols("z")
A = sp.Matrix([[1, 1], [0, 1]])
def Bm(zz): return sp.Matrix([[1, 0], [zz, 1]])
def W(Bmat): return Bmat * A.inv() * Bmat.inv() * A
sols = [s for s in sp.solve(sp.simplify((A * W(Bm(z)) - W(Bm(z)) * Bm(z))[1, 0]), z) if sp.im(s) != 0]
zz = sols[0]
B = Bm(zz)
assert sp.simplify(A * W(B) - W(B) * B) == sp.zeros(2, 2)
gens = {1: A, 2: B}
def ev(word):
    X = sp.eye(2)
    for L in word:
        X = X * (gens[abs(L)] if L > 0 else gens[abs(L)].inv())
    return sp.simplify(X)
def base(g):
    if g == 1:
        return [1] * 6
    k = g - 2
    return [1] * k + [2] + ([] if k == 5 else [-1] * (k + 1))
X = {g: ev(base(g)) for g in range(1, 8)}
# exponent sum of every base word is 0 mod 6 (they lie in the cover's group)
assert all(sum(1 if L in (1, 2) else -1 for L in base(g)) % 6 == 0 for g in range(1, 8))
def ev_cover(word):
    Y = sp.eye(2)
    for L in word:
        Y = Y * (X[abs(L)] if L > 0 else X[abs(L)].inv())
    return sp.simplify(Y)
A2 = A ** 2
TAU2_web = {1: [1], 2: [4], 3: [5], 4: [6], 5: [7, -1], 6: [1, 2, -1], 7: [1, 3]}
TAU2_b1378 = {1: [1], 2: [4], 3: [5], 4: [6], 5: [7], 6: [1, 2, -1], 7: [1, 3, -1]}
def check(T):
    return {g: sp.simplify(ev_cover(T[g]) - A2 * X[g] * A2.inv()) == sp.zeros(2, 2) for g in range(1, 8)}
web = check(TAU2_web)
b1378 = check(TAU2_b1378)
print("holonomy parameter z =", sp.nsimplify(zz), "| source relation holds exactly")
print("web seat's TAU2 = conjugation by a^2 on every cover generator:", all(web.values()), web)
print("B1378's substitute = conjugation by a^2:", all(b1378.values()), b1378)
# the generators named in B1378's text, a^k b a^-k, have exponent sum 1: not in the cover's group
print("exponent sum of a^k b a^-k:", 1, "(not 0 mod 6)")
print("DONE")
