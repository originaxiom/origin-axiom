# Extra independent checks (reader B, Review 80). Own code.
import itertools
import sympy as sp
N = 5
def mm(A, B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
def tp(A): return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))
def pw(A, r):
    R = ((1,0),(0,1))
    for _ in range(r): R = mm(R, A)
    return R
I = ((1,0),(0,1)); J = ((0,1),(1,0)); L = ((1,0),(1,1)); Rr = ((1,1),(0,1))
seqs = [s for n in (2, 4) for s in itertools.product(range(1, 7), repeat=n)]
def word(seq, a, b):
    W = I
    for k, r in enumerate(seq): W = mm(W, pw(a if k % 2 == 0 else b, r))
    return W
# 1. the second convention's letters are the transposes of the seat's letters, in the same order
print("L^T == R:", tp(L) == Rr, " R^T == L:", tp(Rr) == L, " JLJ == L^T:", mm(mm(J, L), J) == tp(L), " JRJ == R^T:", mm(mm(J, Rr), J) == tp(Rr))
lettertr = sum(word(s, Rr, L) == word(s, tp(L), tp(Rr)) for s in seqs)
print("second word == seat letters each transposed, order kept:", lettertr, "of", len(seqs))
# 2. reversal closure for a mark that does not annihilate its own line, e.g. (1,1), on the 1332 sequences
def ln(w): return frozenset(((k*w[0]) % N, (k*w[1]) % N) for k in range(1, N))
def rowv(v, A): return tuple(sum(v[k]*A[k][j] for k in range(2)) % N for j in range(2))
for c in [(1,1), (1,0), (0,1), (1,4), (1,3), (1,2)]:
    d = sum((ln(rowv(c, word(s, L, Rr))) == ln(c)) != (ln(rowv(c, word(s[::-1], L, Rr))) == ln(c)) for s in seqs)
    print("mark", c, ": seat test differs between a sequence and its reversal on", d, "of", len(seqs))
# 3. the lock's exact apex of (6) closed by one period, [6,1,1,1]: 2 sqrt30 / 3 ?
def ppcf(period):
    p, q, r, s = 1, 0, 0, 1
    for a in period: p, q, r, s = p*a + q, p, r*a + s, r
    return (-(s - p) + sp.sqrt((s - p)**2 + 4*r*q)) / (2*r)
def heights(seq):
    n = len(seq)
    return [sp.nsimplify(sp.radsimp((seq[i] + 1/ppcf([seq[(i+1+k) % n] for k in range(n)]) + 1/ppcf([seq[(i-1-k) % n] for k in range(n)])) / 2)) for i in range(n)]
h = [sp.simplify((6 if i == 0 else 1) * 0 + x) for i, x in enumerate(heights([6, 1, 1, 1]))]
top = max(h, key=lambda e: sp.N(e, 30))
print("apex of [6,1,1,1]:", sp.N(top, 12), "equals 2 sqrt30/3:", sp.simplify(top - 2*sp.sqrt(30)/3) == 0)
own6 = sp.Rational(5, 2) + sp.sqrt(5)/2
print("percent above own value of (6):", sp.N((top - own6)/own6*100, 6))
