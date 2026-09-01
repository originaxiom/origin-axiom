#!/usr/bin/env python3
"""R12 blind recomputation of B1141 (THE SPIN PAYMENT).

Written BEFORE opening the arc's verification scripts/tests.
Only the claim statement of frontier/B1141_spin_payment/FINDINGS.md (lines 1-60)
was read: holonomy A,B; relator abABaBAbaB; beat(a)=a, beat(b)=b^-1 a b a^-1 b;
banked numbers: relator census (+,+)=+I,(-,-)=+I,(-,+)=(+,-)=-I; intertwiner
system rank 3 / nullspace 1; W0 conj(W0) = +A with det W0 = 1; twisted lift
needs |lambda|^2 = -1; chi beat-invariant; beat^2 = conj-by-a.

All linear algebra here is my own, exact over Q(omega), omega = exp(2 pi i/3).
"""
import sympy as sp
from sympy import I, Rational, sqrt, simplify, conjugate, Matrix, eye, zeros

w = Rational(-1, 2) + sqrt(3) * I / 2  # omega = e^{2 pi i / 3}, root of x^2+x+1
assert sp.simplify(w**2 + w + 1) == 0

A = Matrix([[1, 1], [0, 1]])
B = Matrix([[1, 0], [-w, 1]])

def S(M):
    return M.applyfunc(lambda e: sp.simplify(sp.expand(e)))

def conjM(M):
    return M.applyfunc(lambda e: sp.simplify(conjugate(sp.expand(e))))

def word_to_matrix(word, Ma, Mb):
    """word: string over a,b,A,B (A=a^-1, B=b^-1)."""
    d = {'a': Ma, 'b': Mb, 'A': Ma.inv(), 'B': Mb.inv()}
    M = eye(2)
    for ch in word:
        M = S(M * d[ch])
    return M

RELATOR = "abABaBAbaB"

print("== step 1: relator holds exactly, R(A,B) = +I ==")
R = word_to_matrix(RELATOR, A, B)
print("R(A,B) =", R.tolist())
assert R == eye(2), "relator fails"

print("\n== step 2: relator census over the four sign pairs ==")
census = {}
for ea in (1, -1):
    for eb in (1, -1):
        Rs = word_to_matrix(RELATOR, ea * A, eb * B)
        sign = "+I" if Rs == eye(2) else ("-I" if Rs == -eye(2) else "OTHER")
        census[(ea, eb)] = sign
        print(f"  R({ea:+d}A,{eb:+d}B) = {sign}")
assert census[(1, 1)] == "+I" and census[(-1, -1)] == "+I"
assert census[(1, -1)] == "-I" and census[(-1, 1)] == "-I"
print("  -> exactly TWO SL(2,C) lifts: trivial and chi(a)=chi(b)=-1")

print("\n== step 3: H1 from abelianized relator ==")
ca = RELATOR.count('a') - RELATOR.count('A')
cb = RELATOR.count('b') - RELATOR.count('B')
print(f"  abelianized relator: {ca}*a + {cb}*b = 0  -> H1 = Z (a=b generator)"
      if abs(ca) == 1 or abs(cb) == 1 else f"  {ca},{cb}")
assert (ca, cb) == (1, -1)
# Hom(H1, Z/2) = Z/2: chi(a)=chi(b), matching the census.

print("\n== step 4: the beat as automorphism ==")
BEAT = {'a': "a", 'b': "BabAb"}  # beat(b) = b^-1 a b a^-1 b
def beat_word(word):
    inv = {'a': 'A', 'b': 'B', 'A': 'a', 'B': 'b'}
    out = []
    for ch in word:
        if ch in 'ab':
            out.append(BEAT[ch])
        else:
            base = inv[ch]
            img = BEAT[base]
            out.append(''.join(inv[c] for c in reversed(img)))
    return ''.join(out)

rho_beat_a = word_to_matrix(BEAT['a'], A, B)
rho_beat_b = word_to_matrix(BEAT['b'], A, B)
print("  rho(beat(a)) =", rho_beat_a.tolist())
print("  rho(beat(b)) =", rho_beat_b.tolist())

# beat respects the relator: R(beat(a),beat(b)) must be +I (product of conjugates of R)
Rbeat = word_to_matrix(beat_word(RELATOR), A, B)
print("  R(beat(a),beat(b)) =", "+I" if Rbeat == eye(2) else Rbeat.tolist())
assert Rbeat == eye(2)

# beat^2 = conjugation by a (check on generators, at matrix level; rep is faithful mod center)
b2a = word_to_matrix(beat_word(beat_word('a')), A, B)
b2b = word_to_matrix(beat_word(beat_word('b')), A, B)
conj_a_a = A  # a a a^-1
conj_a_b = S(A * B * A.inv())
print("  beat^2(a) == a A a^-1 :", b2a == conj_a_a)
print("  beat^2(b) == a B a^-1 :", S(b2b - conj_a_b) == zeros(2))
assert b2a == conj_a_a and S(b2b - conj_a_b) == zeros(2)

print("\n== step 5: intertwiner system W*conj(rho(g)) - rho(beat(g))*W = 0, g in {a,b} ==")
w11, w12, w21, w22 = sp.symbols('w11 w12 w21 w22')
W = Matrix([[w11, w12], [w21, w22]])
eqs = []
for g, target in (('a', rho_beat_a), ('b', rho_beat_b)):
    Mg = {'a': A, 'b': B}[g]
    E = S(W * conjM(Mg) - target * W)
    eqs += [E[i, j] for i in range(2) for j in range(2)]
Msys, _ = sp.linear_eq_to_matrix(eqs, [w11, w12, w21, w22])
Msys = S(Msys)
rk = Msys.rank()
ns = Msys.nullspace()
print(f"  system: {Msys.shape[0]} equations x 4 unknowns; RANK = {rk}, NULLSPACE dim = {len(ns)}")
assert rk == 3 and len(ns) == 1

print("\n== step 6: base intertwiner W0, det normalization, the self-consistent square ==")
v = ns[0]
W0 = S(Matrix([[v[0], v[1]], [v[2], v[3]]]))
d = sp.simplify(W0.det())
print("  raw nullspace W:", W0.tolist(), " det =", d)
# normalize det to 1: W0 -> W0 / mu with mu^2 = det
mu = sp.simplify(sp.sqrt(d))
W0 = S(W0 / mu)
print("  det-normalized W0 =", W0.tolist(), " det =", sp.simplify(W0.det()))
assert sp.simplify(W0.det() - 1) == 0

chk1 = S(W0 * conjM(A) * W0.inv())
chk2 = S(W0 * conjM(B) * W0.inv())
print("  W0 conj(A) W0^-1 == +rho(beat(a)):", S(chk1 - rho_beat_a) == zeros(2))
print("  W0 conj(B) W0^-1 == +rho(beat(b)):", S(chk2 - rho_beat_b) == zeros(2))
sq = S(W0 * conjM(W0))
print("  W0 conj(W0) =", sq.tolist())
target_plus = sq == A
target_minus = sq == -A
print("  W0 conj(W0) == +A:", target_plus, " == -A:", target_minus)
assert S(chk1 - rho_beat_a) == zeros(2) and S(chk2 - rho_beat_b) == zeros(2)
assert target_plus or target_minus
SIGN = +1 if target_plus else -1
print(f"  -> the untwisted-lift square closes with sign {SIGN:+d}")

print("\n== step 7: scaling argument -- the general beat implementation is lambda*W0 ==")
lam = sp.symbols('lam')
# (lam W0) conj(lam W0) = lam conj(lam) W0 conj(W0) = |lam|^2 * (SIGN*A)
# untwisted extension needs (lam W0) conj(lam W0) = rho(a)   = +A -> |lam|^2 = SIGN
# twisted  extension needs (lam W0) conj(lam W0) = rho'(a)   = -A -> |lam|^2 = -SIGN
print(f"  untwisted: |lambda|^2 = {SIGN:+d}  ->", "SOLVABLE" if SIGN == 1 else "IMPOSSIBLE")
print(f"  twisted:   |lambda|^2 = {-SIGN:+d}  ->", "SOLVABLE" if SIGN == -1 else "IMPOSSIBLE")

print("\n== step 8: the twisted lift satisfies the SAME intertwiner equations ==")
# chi(a)=chi(b)=-1; chi(w) = (-1)^len(w). beat(a) len 1, beat(b) len 5 -> chi(beat(g))=chi(g).
chi = lambda word: (-1) ** len(word)
print("  len(beat(a)) =", len(BEAT['a']), " len(beat(b)) =", len(BEAT['b']),
      " both odd:", len(BEAT['a']) % 2 == 1 and len(BEAT['b']) % 2 == 1)
# twisted rep rho'(g) = chi(g) rho(g). Its intertwiner eq:
#   W conj(rho'(g)) - rho'(beat(g)) W = chi(g) [W conj(rho(g)) - chi(beat(g))/chi(g) rho(beat(g)) W]
# equals chi(g) * (untwisted eq) iff chi(beat(g)) = chi(g). Verify by direct construction:
Ap, Bp = -A, -B
rho_p_beat_a = word_to_matrix(BEAT['a'], Ap, Bp)   # image of beat(a) under twisted rep
rho_p_beat_b = word_to_matrix(BEAT['b'], Ap, Bp)
eqs_t = []
for Mg, target in ((Ap, rho_p_beat_a), (Bp, rho_p_beat_b)):
    E = S(W * conjM(Mg) - target * W)
    eqs_t += [E[i, j] for i in range(2) for j in range(2)]
Mt, _ = sp.linear_eq_to_matrix(eqs_t, [w11, w12, w21, w22])
Mt = S(Mt)
rkt = Mt.rank(); nst = Mt.nullspace()
same_line = False
if len(nst) == 1:
    u = nst[0]
    # proportional to v (the untwisted nullspace vector)?
    same_line = all(sp.simplify(u[i] * v[j] - u[j] * v[i]) == 0
                    for i in range(4) for j in range(i + 1, 4))
print(f"  twisted system: rank = {rkt}, nullspace dim = {len(nst)}, same line as W0: {same_line}")
assert rkt == 3 and len(nst) == 1 and same_line
# so the twisted lift's only candidate implementations are lambda*W0 too, and its square
# needs |lambda|^2 = -1: the twisted lift is KILLED. Exactly one lift closes the beat.

print("\n== step 9: chi beat-invariance, random-word check + parity argument ==")
import random
random.seed(12341141)
inv = {'a': 'A', 'b': 'B', 'A': 'a', 'B': 'b'}
ok = 0
for _ in range(50):
    wrd = ''.join(random.choice('abAB') for _ in range(random.randint(1, 12)))
    bw = beat_word(wrd)
    if (len(wrd) % 2) == (len(bw) % 2):
        ok += 1
print(f"  length parity preserved on {ok}/50 random free words")
assert ok == 50
# general argument: beat maps each letter to an odd-length word, so length parity is preserved;
# chi(w) = (-1)^len(w) on reduced or unreduced words (free reduction removes letters in pairs).

print("\n== step 10: CONTROLS (planted positives / could-have-failed) ==")
# (C1) wrong automorphism: replace beat(b) -> b. The intertwiner system should NOT have
#      nullspace 1 with a working square (rank should be 4, or square fails).
eqs_c = []
for Mg, target in ((A, A), (B, B)):
    E = S(W * conjM(Mg) - target * W)
    eqs_c += [E[i, j] for i in range(2) for j in range(2)]
Mc, _ = sp.linear_eq_to_matrix(eqs_c, [w11, w12, w21, w22])
rkc = S(Mc).rank()
print(f"  C1 fake beat (identity automorphism): rank = {rkc} (nullspace {4-rkc})",
      "-> rank-3 result is falsifiable" if rkc != 3 else "!! control failed")
assert rkc == 4

# (C2) the sign of the square is not forced to +: planted positive for '-' outcome.
#      Toy antilinear extension: G = trivial group rep, beat = id, sigma^2 = 1, W = [[0,1],[-1,0]]:
Wc = Matrix([[0, 1], [-1, 0]])
sq_c = S(Wc * conjM(Wc))
print("  C2 planted W with W conj(W) = -I exists:", sq_c == -eye(2),
      "(so a '-' square is achievable in principle; m004's '+' is a fact, not a tautology)")
assert sq_c == -eye(2)

# (C3) decision procedure symmetry: if the banked claim had been inverted (twisted selected),
#      the same code would report it. Run the full decision on both lifts:
def lift_extends(eps_a, eps_b):
    La, Lb = eps_a * A, eps_b * B
    ta = word_to_matrix(BEAT['a'], La, Lb)
    tb = word_to_matrix(BEAT['b'], La, Lb)
    es = []
    for Mg, tg in ((La, ta), (Lb, tb)):
        E = S(W * conjM(Mg) - tg * W)
        es += [E[i, j] for i in range(2) for j in range(2)]
    Mx, _ = sp.linear_eq_to_matrix(es, [w11, w12, w21, w22])
    nsx = S(Mx).nullspace()
    if len(nsx) != 1:
        return f"intertwiner dim {len(nsx)}"
    vv = nsx[0]
    Wx = Matrix([[vv[0], vv[1]], [vv[2], vv[3]]])
    dd = sp.simplify(Wx.det())
    Wx = S(Wx / sp.sqrt(dd))
    sqx = S(Wx * conjM(Wx))
    # need (lam Wx) conj(lam Wx) = eps_a * A  for some lam: sqx = s*A -> need |lam|^2 * s = eps_a
    s = sp.simplify(sqx[0, 0] / A[0, 0])
    if S(sqx - s * A) != zeros(2):
        return "square not proportional to A"
    need = sp.simplify(eps_a / s)
    return "EXTENDS (|lambda|^2 = %s)" % need if need == 1 else \
           "KILLED (|lambda|^2 = %s impossible)" % need

for ea, eb in ((1, 1), (-1, -1)):
    print(f"  lift (chi(a),chi(b)) = ({ea:+d},{eb:+d}):", lift_extends(ea, eb))

print("\nALL BLIND CHECKS PASSED")
