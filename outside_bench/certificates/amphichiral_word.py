#!/usr/bin/env python3
"""MEMO-108 CELL (the quine's named follow-up, run at once): THE
AMPHICHIRAL WORD MAP — memo 107 left one residue: the single external
bit (the Galois branch of omega) is convention-typed only via BANKED
amphichirality citations; the constructive upgrade is an explicit
WORD MAP phi (a -> w_a, b -> w_b) and a holomorphic intertwiner g
with   gal(rho(x)) = g rho(phi(x)) g^-1   for x in {a, b} —
exhibiting the mirror as an (outer) automorphism of the record's own
group composed with an inner conjugation: the flipped record IS the
record, rewritten.

METHOD (exact throughout): enumerate reduced words over {a,b,A,B} to
length 6; keep parabolic candidates (trace +-2, matching the
gal-targets' traces); filter pairs by the exact product-trace
condition tr(rho(w_a) rho(w_b)) = +-gal(tr(AB)) = +-(2 - conj(omega));
on survivors solve the homogeneous intertwiner system over Q(omega)
(all GL2(C) at once, nullspace method — memo 107's solver) for each
SL2 sign choice (+-gal(A), +-gal(B)).  A hit is verified exactly and
then spot-checked on longer words (the identity extends to ALL words
formally: both sides are homomorphisms of the free group, and phi
descends to the knot group because rho is faithful and
rho(phi(rel)) = g^-1 gal(rho(rel)) g = I).
TWO-OUTCOME (preregistered): FOUND in the radius — the mirror is
constructively an automorphism-plus-conjugation: the bit's two
settings yield the SAME realized record up to the record's own word
operations (convention-typing CONSTRUCTED; memo 107's residue paid);
or NOT FOUND — banks as the standing radius bound, the typing stays
banked-cited.  Gate 5 untouched.
"""
import sympy as sp
from itertools import product

omega = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-omega, 1]])
MAT = {"a": A, "b": B, "A": A.inv(), "B": B.inv()}
def gal(M): return M.applyfunc(lambda e: e.subs(sp.sqrt(3), -sp.sqrt(3)))
Ta, Tb = gal(A), gal(B)
tprod_target = sp.simplify((Ta*Tb).trace())          # = gal(tr(AB)) = 2 - conj(omega)

# ---- enumerate reduced words to length 6, matrices built incrementally
INV = {"a": "A", "A": "a", "b": "B", "B": "b"}
words = {"": sp.eye(2)}
frontier = {"": sp.eye(2)}
for L in range(6):
    nxt = {}
    for w, M in frontier.items():
        for c in "abAB":
            if w and INV[w[-1]] == c:
                continue
            nxt[w + c] = sp.Matrix(M*MAT[c])
    for w, M in nxt.items():
        words[w] = sp.Matrix([[sp.simplify(M[i, j]) for j in range(2)] for i in range(2)])
    frontier = {w: words[w] for w in nxt}
del words[""]
parab = {w: M for w, M in words.items() if sp.simplify(M.trace() - 2) == 0
         or sp.simplify(M.trace() + 2) == 0}
print(f"word pool: {len(words)} reduced words to length 6; {len(parab)} parabolic "
      f"(trace +-2) candidates")

def solve_slot(pairs):
    p, q, r_, s_ = sp.symbols('p q r s')
    g = sp.Matrix([[p, q], [r_, s_]])
    eqs = []
    for X, Y in pairs:
        E = sp.expand(g*X - Y*g)
        eqs += [E[i, j] for i in range(2) for j in range(2)]
    Mc = sp.Matrix([[sp.expand(e).coeff(v) for v in (p, q, r_, s_)] for e in eqs])
    ns = Mc.nullspace()
    for v in ns:
        gm = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
        if sp.simplify(gm.det()) != 0:
            return gm
    return None

# ---- the search: pair filter by product trace, then intertwiner solves
found = None
cands = sorted(parab.items(), key=lambda kv: len(kv[0]))
for wa, Ma in cands:
    if found:
        break
    for wb, Mb in cands:
        t = sp.simplify((Ma*Mb).trace())
        if sp.simplify(t - tprod_target) != 0 and sp.simplify(t + tprod_target) != 0:
            continue
        for ea in (1, -1):
            for eb in (1, -1):
                gm = solve_slot([(Ma, ea*Ta), (Mb, eb*Tb)])
                if gm is not None:
                    found = (wa, wb, ea, eb, gm)
                    break
            if found:
                break
        if found:
            break

assert found, "NOT FOUND in radius 6 — banks as the standing bound (typing stays cited)"
wa, wb, ea, eb, gm = found
Ma, Mb = parab[wa], parab[wb]
assert sp.simplify(gm*Ma - ea*Ta*gm) == sp.zeros(2, 2)
assert sp.simplify(gm*Mb - eb*Tb*gm) == sp.zeros(2, 2)
gmi = gm.inv()
# spot-check the extension on longer words: gal(rho(w)) = +- g rho(phi(w)) g^-1
PHI = {"a": wa, "b": wb, "A": "".join(INV[c] for c in reversed(wa)),
       "B": "".join(INV[c] for c in reversed(wb))}
def rho(w):
    M = sp.eye(2)
    for c in w:
        M = M*MAT[c]
    return M
for w in ("ab", "ba", "aab", "abAB", "bbaB"):
    lhs = gal(rho(w))
    rhs = sp.simplify(gm*rho("".join(PHI[c] for c in w))*gmi)
    d1 = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
    d2 = sp.simplify(lhs + rhs) == sp.zeros(2, 2)
    assert d1 or d2, w
print(f"FOUND: phi(a) = {wa}, phi(b) = {wb} (SL2 signs {ea}, {eb});")
print(f"   intertwiner g = {sp.simplify(gm).tolist()}")
print("   verified exactly on the generators AND spot-checked on longer words")
print("   (the identity extends to ALL words: both sides are homomorphisms, and")
print("   phi descends to the knot group by faithfulness of rho).")

# ---- phi is an AUTOMORPHISM, constructively: gal is an involution, so
# rho(phi^2(x)) = h^-1 rho(x) h with h = gal(g) g; if h lies in the group
# itself, phi^2 is INNER and phi is invertible.
h = sp.simplify(gal(gm)*gm)
assert sp.simplify(h - MAT["a"]) == sp.zeros(2, 2)          # h = rho(a) EXACTLY
for w in ("a", "b", "ab", "bA"):
    lhs = rho("".join(PHI[c] for c in "".join(PHI[c2] for c2 in w)))
    rhs = sp.simplify(MAT["A"]*rho(w)*MAT["a"])             # rho(a^-1 w a)
    assert sp.simplify(lhs - rhs) == sp.zeros(2, 2) or \
           sp.simplify(lhs + rhs) == sp.zeros(2, 2), w
print("   AND phi is an AUTOMORPHISM, constructively: h = gal(g)*g = rho(a)")
print("   EXACTLY (the off-entry is conj(omega), and omega + conj(omega) = 1),")
print("   so phi^2 = conjugation by a^-1 — INNER — hence phi is invertible")
print("   (phi^-1 = phi o conj_a); verified on words.  No rigidity theorem")
print("   cited: the witness is self-contained.")

print("""
THE MIRROR IS A WORD MAP: gal(rho(x)) = g rho(phi(x)) g^-1 with phi an
explicit automorphism-by-words and g holomorphic — the Galois-flipped
record is the SAME realized record, rewritten in its own alphabet.
Memo 107's residue is PAID: the quine's one external bit is now
CONSTRUCTIVELY convention-typed — its two settings are related by the
record's own operations, so the bit carries no object content, only
the frame's anchoring choice (exactly W3's weld and B1174's c, now
with the witness in hand).  The quine story closes at full strength:
self-report complete except ONE bit; the bit is c; and c's two values
name the same world.  Gate 5 untouched.""")
