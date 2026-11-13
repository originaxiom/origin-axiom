"""P-321 (and the last item of P-747): the agy lane's bridge note of 2026-11-07, its two halves, checked on main's own code,
exactly. The lane's code is not run; its statements were read through the mask.

HALF 1. The quaternion point tr rho([a,b]) = -2 (GENESIS GM4's input) cannot be carried by the abelian carrier Z^2: there
[a,b] = 1, so tr rho([a,b]) = 2 in every 2-dimensional representation. It CAN be carried by a carrier that is not free: the
integral Heisenberg group H3(Z) = F2/gamma3(F2) (every commutator central), through its quotient Q8 in SU(2). So narrowing to
the free group needs a premise of its own (that iterated commutators do not cancel), and the quaternion point is not that
premise. Checked: Q8's generators i, j satisfy the Heisenberg relations [[i,j],i] = [[i,j],j] = 1 and tr [i,j] = -2; the
abelian carrier gives +2; in SL(2, Z), the free group's image, [[L, R], L] is not the identity (so F2 does not factor
through H3).
HALF 2. In the finite Heisenberg group H(p) the p-dimensional irreducible with central character zeta (clock and shift,
Z X = zeta X Z) is sent by each orientation-reversing move (the swap (a,b) -> (b,a); the tick's LP (a,b) -> (ab, a)) to the
one with central character zeta^-1 = conj(zeta), since both send [a,b] to a conjugate of [a,b]^-1. So a single irreducible
sector is kept only when zeta = conj(zeta), that is at p = 2 (zeta = -1: Q8 with q_i = iZ, q_j = iX, det +1); and the pair
rho_zeta + rho_conj(zeta), of dimension 2p, is kept at every p. 'The prime is 2' needs the premise of a single irreducible
sector. Checked for p = 2, 3, 5, 7: the words, the central characters exactly (cyclotomic), and the pair's character.
Planted: a move with det +1 (L alone) keeps the central character; it must not be counted as a selector.
No data.   python3 -B the_bridge_note_on_main.py"""
import json, pathlib
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]})
    print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:160]) if detail else ""))

def comm(x, y): return x * y * x.inv() * y.inv()
I2 = sp.eye(2); iu = sp.I

# HALF 1
qi = sp.Matrix([[iu, 0], [0, -iu]]); qj = sp.Matrix([[0, 1], [-1, 0]])
c = sp.simplify(comm(qi, qj))
check("Q8: the commutator of i and j is -1, so its trace is -2", c == -I2 and c.trace() == -2, c.tolist())
check("Q8 satisfies the Heisenberg relations: [[i,j],i] = [[i,j],j] = 1", sp.simplify(comm(c, qi)) == I2 and sp.simplify(comm(c, qj)) == I2)
check("Q8 is a quaternion group: i^2 = j^2 = (ij)^2 = -1, det +1", sp.simplify(qi ** 2) == -I2 and sp.simplify(qj ** 2) == -I2 and sp.simplify((qi * qj) ** 2) == -I2 and qi.det() == 1 and qj.det() == 1)
A, B = sp.symbols("A B")
D1 = sp.diag(A, 1 / A); D2 = sp.diag(B, 1 / B)       # a 2-dimensional representation of Z^2 up to conjugacy (diagonalisable part)
check("the abelian carrier: commuting matrices have [a,b] = 1, trace +2", sp.simplify(comm(D1, D2)) == I2 and sp.simplify(comm(D1, D2).trace()) == 2)
U = sp.Matrix([[1, 1], [0, 1]]); V = sp.Matrix([[1, sp.Symbol("x")], [0, 1]])
check("the abelian carrier, its non-diagonalisable part: commuting unipotents have [a,b] = 1 too", sp.simplify(comm(U, V)) == I2)
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
t3 = comm(comm(L, R), L)
check("the free group's image in SL(2,Z): [[L,R],L] is not 1, so F2 does not factor through H3", t3 != I2, t3.tolist())

# HALF 2
def heisenberg(p):
    z = sp.exp(2 * sp.pi * iu / p)
    X = sp.zeros(p, p); Z = sp.zeros(p, p)
    for k in range(p):
        X[(k + 1) % p, k] = 1; Z[k, k] = z ** k
    return X, Z, z
def central_character(a, b, p):
    """the scalar that [a,b] acts by, when it is central"""
    cm = sp.simplify(comm(a, b))
    lam = sp.simplify(cm[0, 0])
    assert sp.simplify(cm - lam * sp.eye(p)) == sp.zeros(p, p)
    return lam
moves = {"swap (a,b) -> (b,a)": lambda a, b: (b, a), "tick's LP (a,b) -> (ab,a)": lambda a, b: (a * b, a)}
for p in (2, 3, 5, 7):
    X, Z, z = heisenberg(p)
    lam = central_character(Z, X, p)
    kept = {}
    for name, mv in moves.items():
        a2, b2 = mv(Z, X)
        lam2 = central_character(a2, b2, p)
        kept[name] = sp.simplify(lam2 - lam) == 0
        check("p = %d, %s: the central character goes to its conjugate" % (p, name), sp.simplify(lam2 - sp.conjugate(lam)) == 0, (sp.nsimplify(lam), sp.nsimplify(lam2)))
    single = all(kept.values())
    check("p = %d: a single irreducible sector is kept by both moves exactly when p = 2" % p, single == (p == 2), kept)
    pair = {sp.simplify(lam), sp.simplify(sp.conjugate(lam))}
    check("p = %d: the pair rho_zeta + rho_conj(zeta) is kept (its set of central characters is closed under conjugation)" % p,
          {sp.simplify(sp.conjugate(x)) for x in pair} == pair)
    if p == 2:
        check("p = 2: i Z and i X are Q8 in SU(2) (det +1, squares -1)", (iu * Z).det() == 1 and (iu * X).det() == 1 and sp.simplify((iu * Z) ** 2) == -sp.eye(2) and sp.simplify((iu * X) ** 2) == -sp.eye(2))
# planted: a move with det +1 (b -> ab, a fixed: the word map of L) keeps the central character, so it selects nothing
for p in (3, 5):
    X, Z, z = heisenberg(p)
    lam = central_character(Z, X, p); lam2 = central_character(Z, Z * X, p)
    check("planted: at p = %d the move (a,b) -> (a,ab) of det +1 keeps the central character (it is no selector)" % p, sp.simplify(lam2 - lam) == 0)

if __name__ == "__main__":
    json.dump({"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(HERE / "the_bridge_note_on_main.json", "w"), indent=1)
