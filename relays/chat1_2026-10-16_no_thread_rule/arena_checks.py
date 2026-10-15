"""Checks for the no-thread rule's reading (pure algebra): (1) LR and RL in the modular group's commutator subgroup, the
index of the subgroup they generate (coset enumeration in PSL(2,Z) = <S, U | S^2, U^3> and in SL(2,Z)), the commutator's trace and the
Markov traces; (2) the Higgs character chi_i(S) = chi_i(T) = i: a character, the multiplier of eta^6, and i^(#R - #L)
on a word; (3) threads by trace; (4) the
matrix-form bridge, each thread's content and primitive discriminant, the layers' deepest threads, and the powers."""
import math, itertools
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup
def mul(A, B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]], [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def inv(A): return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
L, R = [[1, 0], [1, 1]], [[1, 1], [0, 1]]
LR, RL = mul(L, R), mul(R, L)
C = mul(mul(LR, RL), mul(inv(LR), inv(RL)))
print("LR", LR, "RL", RL, "tr LR, RL, LR.RL:", LR[0][0] + LR[1][1], RL[0][0] + RL[1][1], mul(LR, RL)[0][0] + mul(LR, RL)[1][1])
print("commutator [LR, RL] =", C, "trace", C[0][0] + C[1][1], "(parabolic iff |trace| = 2)")
# PSL(2,Z) = <S, U | S^2 = U^3 = 1> with S = [[0,-1],[1,0]], U = S T (order 3 in PSL); T = S^-1 U, L = S T^-1 S^-1
F, s, u = free_group("s u")
G = FpGroup(F, [s**2, u**3])
T = s**-1 * u
Lw = s * T**-1 * s**-1
H = [Lw * T, T * Lw]                                            # LR, RL as words in s, u
ct = G.coset_enumeration(H); ct.compress(); print("index of <LR, RL> in PSL(2,Z):", len(ct.table))
# SL(2,Z) = <S, U | S^4, S^2 = U^3>, U = S T = [[0,-1],[1,1]] of order 6: its commutator subgroup has index 12
G2 = FpGroup(F, [s**4, s**2 * u**-3])
ct2 = G2.coset_enumeration(H); ct2.compress(); print("index of <LR, RL> in SL(2,Z):", len(ct2.table))
# the abelianisation: chi_i on L and R
# chi_i is a character of SL(2,Z): on the relators S^4 and S^2 U^-3 (U = S T, chi(U) = i.i = -1) it gives i^4 = 1 and
# (-1)(-1)^-3 = 1. It is the multiplier of eta^6 (weight 3): eta^6(tau + 1) = i eta^6(tau), eta^6(-1/tau) = i tau^3 eta^6.
# Checked numerically on every positive word to length 7: eta^6(g tau) / ((c tau + d)^3 eta^6(tau)) against i^(#R - #L).
import mpmath as mp
mp.mp.dps = 30
def eta6(tau): return (mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))) ** 6
tau0 = mp.mpc(0.13, 1.21)
worst, nw = 0, 0
for n in range(1, 8):
    for w in itertools.product("LR", repeat=n):
        g = [[1, 0], [0, 1]]
        for ch in w: g = mul(g, L if ch == "L" else R)
        (a, b), (c, d) = g
        val = eta6((a * tau0 + b) / (c * tau0 + d)) / ((c * tau0 + d) ** 3 * eta6(tau0))
        worst = max(worst, abs(val - mp.mpc(1j) ** (w.count("R") - w.count("L")))); nw += 1
print(f"chi_i = multiplier of eta^6; chi_i(word) = i^(#R - #L) (Rademacher's Psi) on all {nw} positive words to length 7: "
      f"max deviation {mp.nstr(worst, 3)}")
# threads (primitive cyclic words, up to rotation) by trace, both letters present, length <= 14
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
bytr = {}
for w in lyndon(16):
    if "L" not in w or "R" not in w: continue
    M = [[1, 0], [0, 1]]
    for ch in w: M = mul(M, L if ch == "L" else R)
    t = M[0][0] + M[1][1]
    bytr.setdefault(t, []).append(w)
print("threads by trace (t: count, D = t^2 - 4, Psi values):")
for t in range(3, 13):
    ws = bytr.get(t, [])
    print(f"  t={t:2d} D={t*t-4:4d}: {len(ws)} threads  {ws[:6]}  Psi={sorted(set(w.count('R') - w.count('L') for w in ws))}")
# (4) how a trace layer sits in the classical sums by discriminant. A matrix [[a,b],[c,d]] of trace t gives the form
# Q = [c, d - a, -b] of discriminant t^2 - 4, and back by [[(t - B)/2, -C], [A, (t + B)/2]]: the classes of forms of
# discriminant t^2 - 4, primitive or not, are the classes of elements of trace t, primitive threads and powers alike.
def word_matrix(w):
    M = [[1, 0], [0, 1]]
    for ch in w: M = mul(M, L if ch == "L" else R)
    return M
def height(w):   # the record's height: sqrt(tr^2 - 4) / (2 min over rotations of min(|B|, |C|))
    t = sum(word_matrix(w)[i][i] for i in range(2))
    m = min(min(abs(word_matrix(w[k:] + w[:k])[0][1]), abs(word_matrix(w[k:] + w[:k])[1][0])) for k in range(len(w)))
    return math.sqrt(t * t - 4) / (2 * m)
bytr20 = {}
for w in lyndon(19):
    if "L" in w and "R" in w:
        M = word_matrix(w); bytr20.setdefault(M[0][0] + M[1][1], []).append(w)
print("each thread's form, its content f and primitive discriminant (t^2 - 4)/f^2; the round trip; the layer's length:")
ok = True
for t in range(3, 13):
    rows = []
    for w in bytr20[t]:
        (a, b), (c, d) = word_matrix(w)
        A_, B_, C_ = c, d - a, -b
        ok &= (B_ * B_ - 4 * A_ * C_ == t * t - 4) and [[(t - B_) // 2, -C_], [A_, (t + B_) // 2]] == [[a, b], [c, d]]
        f = math.gcd(math.gcd(A_, B_), C_)
        rows.append(f"{w}:f={f},D'={(t*t-4)//(f*f)}" if f > 1 else w)
    hs = {w: height(w) for w in bytr20[t]}
    deep = max(hs, key=hs.get)
    top = [w for w in hs if abs(hs[w] - hs[deep]) < 1e-12]
    assert sorted(top) == sorted({"L" * (t - 2) + "R", "L" + "R" * (t - 2)}), top     # the deepest pair is unique
    print(f"  t={t:2d} length 2 arccosh(t/2) = {2*math.acosh(t/2):.4f}; imprimitive forms: {[r for r in rows if ':' in r]}; "
          f"deepest {deep} (and its mirror) at height {hs[deep]:.3f}, sqrt(t^2-4)/2 = {math.sqrt(t*t-4)/2:.3f}")
print("round trip matrix <-> form exact on every thread to t = 12:", ok)
def chebyshev_tr(t0, k):   # tr(g^k) from tr g
    a, b = 2, t0
    for _ in range(k - 1): a, b = b, t0 * b - a
    return b
print("powers of threads with trace <= 20 (in the classical sum at D = t^2 - 4, not in the trace layer):")
for t0 in range(3, 21):
    for w in bytr20.get(t0, []):
        for k in range(2, 6):
            tk = chebyshev_tr(t0, k)
            if tk <= 20: print(f"  ({w})^{k}: trace {tk}")
print("layer sizes to t = 20 (primitive threads):", {t: len(bytr20.get(t, [])) for t in range(3, 21)})
def prim_disc(w):
    (a, b), (c, d) = word_matrix(w); f = math.gcd(math.gcd(c, d - a), b); t = a + d
    return (t * t - 4) // (f * f)
mins = {t: min(prim_disc(w) for w in bytr20[t]) for t in range(3, 21)}
alld = [prim_disc(w) for t in range(3, 21) for w in bytr20[t]]
print("smallest primitive discriminant per layer to t = 20:", mins)
print("each primitive discriminant in one layer only (to t = 20):",
      all(len({t for t in range(3, 21) for w in bytr20[t] if prim_disc(w) == D}) == 1 for D in set(alld)))
