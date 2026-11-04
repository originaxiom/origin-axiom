"""S303 check c2 (value-free; first principles + SnapPy): the torsions of m004 that the agy lane's Stage 9 restates
(Theorem 71's ledger R3: '|tau_RS| = 4 - 2 sqrt 3 via Fox calculus').  From SnapPy's presentation of m004:
 - the Alexander polynomial by Fox calculus with the abelianisation (1-dim trivial rep), and |Delta(w)/(w-1)| at w = e^{2 pi i/3};
 - Wada's SL(2, C)-twisted torsion with the holonomy (SnapPy's SL2C lift, signs fixed so the relator maps to +I);
 - the adjoint (Ad rho, 3-dim) twisted torsion;
all at t = 1, w, -1, against the lane's 4 - 2 sqrt 3 and |Delta(w)| - 2|w - 1|."""
import cmath, itertools, math
import numpy as np
import snappy

M = snappy.Manifold("m004")
G = M.fundamental_group()
gens = G.generators(); rels = G.relators()
print("SnapPy m004: generators", gens, "relators", rels)
assert len(gens) == 2 and len(rels) == 1
r = rels[0]


def letters(w):
    out = []
    for ch in w:
        out.append((ch.lower(), 1 if ch.islower() else -1))
    return out


R = letters(r)
esum = {g: sum(e for (x, e) in R if x == g) for g in gens}
print("exponent sums of the relator:", esum)
# abelianisation: phi(g) in Z with sum_g esum[g] * phi(g) = 0 and image Z
a, b = gens
ea, eb = esum[a], esum[b]
gcd = math.gcd(ea, eb)
assert gcd == 1, "H1 should be Z"
phi = {a: eb, b: -ea}
print("abelianisation phi:", phi, "(H1 = Z)")

# holonomy lift
def _m(x):
    return np.array([[complex(x[i, j]) for j in range(2)] for i in range(2)], dtype=complex)
rho0 = {g: _m(G.SL2C(g)) for g in gens}


def ev(word, rho):
    m = np.eye(rho[gens[0]].shape[0], dtype=complex)
    for (x, e) in letters(word):
        m = m @ (rho[x] if e == 1 else np.linalg.inv(rho[x]))
    return m


Rr = ev(r, rho0)
print("SnapPy's SL2C lift: rho(relator) = %s I (deviation %.1e)" % ("+" if np.allclose(Rr, np.eye(2), atol=1e-9) else "-" if np.allclose(Rr, -np.eye(2), atol=1e-9) else "?",
      min(np.abs(Rr - np.eye(2)).max(), np.abs(Rr + np.eye(2)).max())))
rho = dict(rho0)
if np.allclose(Rr, -np.eye(2), atol=1e-9):
    odd = [g for g in gens if esum[g] % 2]
    assert odd, "no generator with odd exponent sum: the lift cannot be fixed by a sign"
    rho[odd[0]] = -rho[odd[0]]
    print("  fixed by rho(%s) -> -rho(%s); now rho(relator) = I to %.1e" % (odd[0], odd[0], np.abs(ev(r, rho) - np.eye(2)).max()))
print("  traces of the generators:", {g: complex(np.trace(rho[g])) for g in gens})


def fox(word, xj):
    """Fox derivative d word / d xj as a list of (sign, prefix_word_letters, extra_inverse) terms."""
    terms = []; prefix = []
    for (x, e) in letters(word):
        if x == xj:
            if e == 1: terms.append((1, list(prefix)))
            else: terms.append((-1, list(prefix) + [(x, -1)]))
        prefix.append((x, e))
    return terms


def Phi(lets, t, rep):
    n = rep[gens[0]].shape[0]; m = np.eye(n, dtype=complex); p = 0
    for (x, e) in lets:
        m = m @ (rep[x] if e == 1 else np.linalg.inv(rep[x])); p += e * phi[x]
    return (t ** p) * m


def wada(t, rep):
    n = rep[gens[0]].shape[0]
    num = sum(s * Phi(pre, t, rep) for (s, pre) in fox(r, a))
    den = Phi([(b, 1)], t, rep) - np.eye(n)
    num2 = sum(s * Phi(pre, t, rep) for (s, pre) in fox(r, b))
    den2 = Phi([(a, 1)], t, rep) - np.eye(n)
    d1, d2 = np.linalg.det(den), np.linalg.det(den2)
    W1 = np.linalg.det(num) / d1 if abs(d1) > 1e-9 else None
    W2 = np.linalg.det(num2) / d2 if abs(d2) > 1e-9 else None
    return W1, W2


def Ad(m):
    # adjoint action on sl2 in the basis (H, E, F)
    basis = [np.array([[1, 0], [0, -1]], dtype=complex), np.array([[0, 1], [0, 0]], dtype=complex), np.array([[0, 0], [1, 0]], dtype=complex)]
    mi = np.linalg.inv(m); cols = []
    for X in basis:
        Yv = m @ X @ mi
        cols.append([Yv[0, 0], Yv[0, 1], Yv[1, 0]])
    return np.array(cols, dtype=complex).T


triv = {g: np.eye(1, dtype=complex) for g in gens}
adr = {g: Ad(rho[g]) for g in gens}
w = cmath.exp(2j * math.pi / 3)
for name, rep in (("trivial (Delta/(t-1))", triv), ("SL(2,C) holonomy", rho), ("adjoint", adr)):
    for tn, t in (("1", 1.0 + 0j), ("w", w), ("-1", -1.0 + 0j)):
        try:
            W1, W2 = wada(t, rep)
            f = lambda W: ("%.12f" % abs(W)) if W is not None else "invalid (det Phi(x - 1) = 0)"
            print("  %-22s t = %-2s : |W| via (dr/da, b) = %s ; via (dr/db, a) = %s" % (name, tn, f(W1), f(W2)))
        except np.linalg.LinAlgError:
            print("  %-22s t = %-2s : singular (not acyclic / pole)" % (name, tn))
# Alexander polynomial itself
# Delta(t) = det Phi_triv(d r / d a) * (t - 1)/(phi... ) : report |Delta(w)| from W * |w - 1|
W1, _ = wada(w, triv)
print("|Delta(w)| = %.12f ; |w - 1| = %.12f ; |Delta(w)/(w-1)| = %.12f ; 4/sqrt3 = %.12f" % (abs(W1) * abs(w - 1), abs(w - 1), abs(W1), 4 / math.sqrt(3)))
print("lane's 4 - 2 sqrt3 = %.12f ; |Delta(w)| - 2|w - 1| = %.12f" % (4 - 2 * math.sqrt(3), abs(W1) * abs(w - 1) - 2 * abs(w - 1)))
# Kitano's closed form for the figure-eight: T(t) = t^-1 (t - 4 + t^-1)
for tn, t in (("1", 1.0 + 0j), ("w", w), ("-1", -1.0 + 0j)):
    print("  Kitano/B1836 closed form |t^-1(t - 4 + t^-1)| at t = %s: %.12f" % (tn, abs((t - 4 + 1 / t) / t)))
