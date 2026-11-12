# Independent recomputation of B1895 Part A (reader B, Review 80). Own code; no arc code imported.
import itertools
N = 5
def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
def tp(A): return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))
def pw(A, r):
    R = ((1,0),(0,1))
    for _ in range(r): R = mm(R, A)
    return R
I = ((1,0),(0,1)); J = ((0,1),(1,0))
L = ((1,0),(1,1)); Rr = ((1,1),(0,1))
G = [((a,b),(c,d)) for a in range(N) for b in range(N) for c in range(N) for d in range(N) if (a*d-b*c) % N == 1]
print("SL2 mod 5 size", len(G))
def rowv(v, A): return tuple(sum(v[k]*A[k][j] for k in range(2)) % N for j in range(2))
def colv(A, u): return tuple(sum(A[i][k]*u[k] for k in range(2)) % N for i in range(2))
def ln(w): return frozenset(((k*w[0]) % N, (k*w[1]) % N) for k in range(1, N))
vecs = [(a,b) for a in range(N) for b in range(N) if (a,b) != (0,0)]
LINES = sorted({ln(w) for w in vecs}, key=lambda s: min(s))
def rep(l): return min(l)
def keptrow(v, A): return ln(rowv(v, A)) == ln(v)
def keptcol(A, u): return ln(colv(A, u)) == ln(u)
def seat_word(seq):
    W = I
    for k, r in enumerate(seq): W = mm(W, pw(L if k % 2 == 0 else Rr, r))
    return W
def second_word(seq):
    W = I
    for k, r in enumerate(seq): W = mm(W, pw(Rr if k % 2 == 0 else L, r))
    return W
seqs = [s for n in (2, 4) for s in itertools.product(range(1, 7), repeat=n)]
print("sequences", len(seqs))
Ws = {s: seat_word(s) for s in seqs}
print("matrices reached", len(set(Ws.values())), "all of SL2:", set(Ws.values()) == set(G))
swapc = lambda A: mm(mm(J, A), J)
print("A1 word equality second == J W J on all:", all(second_word(s) == swapc(Ws[s]) for s in seqs))
v = (1, 3); m2 = (1, 2)
ann = lambda v: {ln(u) for u in vecs if (v[0]*u[0] + v[1]*u[1]) % N == 0}
print("annihilated by (1,3):", [rep(l) for l in ann(v)], "own line?", ann(v) == {ln(v)})
print("(2,1) in line of (1,3)?", (2,1) in ln(v), "J(2,1) =", colv(J, (2,1)))
dw = sum(swapc(Ws[s]) != tp(Ws[s]) for s in seqs)
dt = sum(keptcol(swapc(Ws[s]), m2) != keptcol(tp(Ws[s]), m2) for s in seqs)
print("A2 swapped word != transposed word on", dw, "; tests differ on", dt)
# also: second word (actual) vs transpose of seat word
print("   actual second word != W^T on", sum(second_word(s) != tp(Ws[s]) for s in seqs))
ground = mm(L, Rr); print("ground", ground, "symmetric", tp(ground) == ground, "swap", swapc(ground), "second ground R.L", mm(Rr, L))
print("row (1,3)*ground", rowv(v, ground))
for l in LINES:
    w = rep(l); (u,) = ann(w)
    a4 = sum(keptrow(w, g) == keptcol(g, min(u)) for g in G)
    a7b = sum(keptrow(w, g) == keptcol(tp(g), w) for g in G)
    selfann = ann(w) == {l}
    ctrl = sum(keptrow(w, g) == keptcol(swapc(g), colv(J, w)) for g in G)
    print("line", w, "self-annihilating", selfann, "A4", a4, "row=col-of-transpose", a7b, "recipe(swapped mark on swapped matrix) agree", ctrl)
S = ((0, N-1), (1, 0))
print("lines S keeps (rows):", [rep(l) for l in LINES if keptrow(rep(l), S)], " (columns):", [rep(l) for l in LINES if keptcol(S, rep(l))])
print("A5", sum(keptrow(v, g) == keptcol(swapc(g), m2) for g in G))
# A7 reversed: second word on reversed == J W^T J ?
print("A7 second word on reversed == J W^T J on all:", all(second_word(s[::-1]) == swapc(tp(Ws[s])) for s in seqs))
# odd length sanity (not claimed by arc)
odd = [s for s in itertools.product(range(1, 7), repeat=3)]
print("   odd length 3: second word on reversed == J W^T J:", sum(second_word(s[::-1]) == swapc(tp(seat_word(s))) for s in odd), "of", len(odd), "; == W^T:", sum(second_word(s[::-1]) == tp(seat_word(s)) for s in odd))
# E12 of B1881 with own code: lengths 2,4,6 runs to 6
agree = rev = rot = 0; tot = 0
for n in (2, 4, 6):
    for s in itertools.product(range(1, 7), repeat=n):
        tot += 1
        a = keptrow(v, seat_word(s))
        agree += a == keptcol(second_word(s), m2)
        rev += a != keptcol(second_word(s[::-1]), m2)
        rot += a != keptcol(second_word(s[1:] + s[:1]), m2)
print("E12 total", tot, "agree", agree, "differ vs reversed", rev, "differ vs rotated", rot)
# P L P = R
print("J L J == R:", mm(mm(J, L), J) == Rr)
