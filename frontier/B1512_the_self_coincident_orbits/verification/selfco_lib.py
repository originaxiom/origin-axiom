"""B1512 -- THE SELF-COINCIDENT ORBITS.  Library (no sealed quantity is computed on import).

B1511's verification library is reused by import (tower_lib as T, tower_census as TC; frontier/B1511_the_projective_tower).  Added here:
  - the fibre's hyperelliptic involution iota of pi = <m, n | mnMNmNMnmN>:  m -> m n m^-1,  n -> m n^-1 m n m^-1.  On the fibre group
    F = <x = nM, y = mnMM> it is x -> x^-1, y -> y^-1 (free-group identities), and iota(m) = y m;
  - the exact intertwiner C(q) with C rho_q(g) C^-1 = rho_q(iota g) (Ballas' family is fixed by iota);
  - the Galois classes of characters of T_n (deck orbit, inverse, Galois conjugates);
  - the twisted polynomial P_nu(q, s) over Q by interpolation over GF(p) at many primes, Chinese remaindering and rational
    reconstruction, verified at fresh primes;
  - exact positive real roots of its specialisations at lam in mu_4;
  - the fibre data and B1511's case-(b) counts at every root of a factor over GF(p)."""
import importlib.util
import itertools
import math
import sys
from functools import reduce
from pathlib import Path

import flint
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1511 = ROOT / "frontier/B1511_the_projective_tower/verification"
sys.path.insert(0, str(B1511))
import tower_lib as T  # noqa: E402
import tower_census as TC  # noqa: E402

q, s = T.Q, T.S_
IL = T.IL


# ============================================================================================ the involution
IOTA = {"m": "mnM", "n": "mNmnM"}


def iota_word(w):
    return T.red("".join(IOTA[c] if c.islower() else T.inv(IOTA[c.lower()]) for c in w))


def cyclic_reduce(w):
    w = T.red(w)
    while len(w) >= 2 and w[0] == w[-1].swapcase():
        w = w[1:-1]
    return w


def cyclic_conjugate_of(u, v):
    """None if the cyclically reduced u is not a rotation of the cyclically reduced v; else the rotation index"""
    u, v = cyclic_reduce(u), cyclic_reduce(v)
    if len(u) != len(v):
        return None
    k = (v + v).find(u)
    return None if k < 0 else k


def intertwiner():
    """the solution space of C rho(g) = rho(iota g) C (g = m, n) over Q(q); returns (dimension, C normalised to integer polynomials)"""
    mats = T.symbolic_mats()
    cs = sp.symbols("c0:16")
    C = sp.Matrix(4, 4, cs)
    eqs = []
    for g in "mn":
        A = mats[g]
        B = T.word_matrix(mats, iota_word(g)).applyfunc(sp.cancel)
        eqs += [sp.numer(sp.together(e)) for e in (C * A - B * C)]
    rows = []
    for e in eqs:
        P = sp.Poly(sp.expand(e), *cs)
        rows.append([P.coeff_monomial(c) for c in cs])
    M = sp.Matrix(rows)
    ns = M.nullspace()
    dim = len(ns)
    v = ns[0]
    den = reduce(sp.lcm, [sp.fraction(sp.cancel(x))[1] for x in v], sp.Integer(1))
    v = (v * den).applyfunc(sp.cancel)
    content = reduce(sp.gcd, [sp.Poly(x, q).content() for x in v if x != 0])
    v = (v / content).applyfunc(sp.expand)
    return dim, sp.Matrix(4, 4, list(v))


def involution_checks():
    out = {}
    out["iota(m)"], out["iota(n)"] = iota_word("m"), iota_word("n")
    out["iota^2 = id on m and n (free group)"] = iota_word(iota_word("m")) == "m" and iota_word(iota_word("n")) == "n"
    iR = iota_word(T.WORD_R)
    out["iota(R)"] = iR
    out["iota(R) is a cyclic conjugate of R^-1 (free group)"] = cyclic_conjugate_of(iR, T.inv(T.WORD_R)) is not None
    x, y = T.FIBRE["x"], T.FIBRE["y"]
    out["iota(x) = x^-1 (free group)"] = iota_word(x) == T.red(T.inv(x))
    out["iota(y) = y^-1 (free group)"] = iota_word(y) == T.red(T.inv(y))
    out["iota(m) = y m (free group)"] = iota_word("m") == T.red(y + "m")
    iL = iota_word(T.WORD_L)
    out["iota(longitude) is a cyclic conjugate of the longitude^(+-1) (free group)"] = (
        cyclic_conjugate_of(iL, T.WORD_L) is not None or cyclic_conjugate_of(iL, T.inv(T.WORD_L)) is not None)
    dim, C = intertwiner()
    mats = T.symbolic_mats()
    Ci = C.inv().applyfunc(sp.cancel)
    ok = all(sp.simplify(C * mats[g] * Ci - T.word_matrix(mats, iota_word(g))) == sp.zeros(4) for g in "mn")
    C2 = (C * C).applyfunc(sp.factor)
    out["intertwiner: dimension of the solution space"] = dim
    out["intertwiner C(q) (integer polynomial entries)"] = [[str(C[i, j]) for j in range(4)] for i in range(4)]
    out["det C"] = str(sp.factor(C.det()))
    out["C rho(g) C^-1 = rho(iota g) for g = m, n"] = ok
    out["C^2 is scalar"] = all(C2[i, j] == 0 for i in range(4) for j in range(4) if i != j) and len({C2[i, i] for i in range(4)}) == 1
    out["C^2"] = str(C2[0, 0])
    return out


# ============================================================================================ duality and amphichirality
# EPS is the figure-eight's orientation-reversing involution read on the fibre: x <-> y, m -> x^-1 m^-1 (so z -> (F-part) z^-1).
EPS = {"m": "mNM", "n": "mnMNM"}


def eps_word(w):
    return T.red("".join(EPS[c] if c.islower() else T.inv(EPS[c.lower()]) for c in w))


def _family(qv, dual=False):
    m, n = T.ballas(qv)
    if dual:
        m, n = m.inv().T, n.inv().T
    return {"m": m.applyfunc(sp.cancel), "n": n.applyfunc(sp.cancel)}


def intertwiner_qq(src, tgt):
    """the solutions D over Q(q) of D src(g) = tgt(g) D for g = m, n (src, tgt: dicts of 4 x 4 sympy matrices in q);
    returns (dimension, D with polynomial entries, common factors removed)"""
    K = sp.QQ.frac_field(q)
    rows = []
    for g in "mn":
        A, B = src[g], tgt[g]
        for i in range(4):
            for j in range(4):
                row = [0] * 16
                for k in range(4):
                    for l in range(4):
                        c = 0
                        if k == i:
                            c += A[l, j]
                        if l == j:
                            c -= B[i, k]
                        row[4 * k + l] = c
                rows.append(row)
    M = DomainMatrix([[K.from_sympy(sp.cancel(sp.sympify(x))) for x in r] for r in rows], (32, 16), K)
    NS = M.nullspace()
    dim = NS.shape[0]
    if dim == 0:
        return 0, None
    v = [K.to_sympy(x) for x in NS.to_Matrix().row(0)]
    den = reduce(sp.lcm, [sp.fraction(sp.cancel(x))[1] for x in v], sp.Integer(1))
    v = [sp.cancel(x * den) for x in v]
    g = reduce(sp.gcd, [x for x in v if x != 0])
    v = [sp.factor(sp.cancel(x / g)) for x in v]
    return dim, sp.Matrix(4, 4, v)


def duality_checks():
    """Lemma D: rho_q* = rho_q^-T is conjugate to rho_(1/q); Lemma E: rho_q o eps is conjugate to rho_(1/q)"""
    out = {}
    dual, inv_ = _family(q, dual=True), _family(1 / q)
    dim, D = intertwiner_qq(dual, inv_)
    Di = D.inv().applyfunc(sp.cancel)
    out["D: dimension"] = dim
    out["D (rho_q^-T -> rho_1/q)"] = [[str(D[i, j]) for j in range(4)] for i in range(4)]
    out["det D"] = str(sp.factor(D.det()))
    out["D rho_q(g)^-T D^-1 = rho_1/q(g), g = m, n"] = all(sp.simplify(D * dual[g] * Di - inv_[g]) == sp.zeros(4) for g in "mn")
    mats = T.symbolic_mats()
    eps_tgt = {g: T.word_matrix(_family(1 / q), eps_word(g)).applyfunc(sp.cancel) for g in "mn"}
    dimE, E = intertwiner_qq(mats, eps_tgt)
    Ei = E.inv().applyfunc(sp.cancel)
    out["E: dimension"] = dimE
    out["E (rho_q -> rho_1/q o eps)"] = [[str(E[i, j]) for j in range(4)] for i in range(4)]
    out["det E"] = str(sp.factor(E.det()))
    out["E rho_q(g) E^-1 = rho_1/q(eps g), g = m, n"] = all(sp.simplify(E * mats[g] * Ei - eps_tgt[g]) == sp.zeros(4) for g in "mn")
    x, y = T.FIBRE["x"], T.FIBRE["y"]
    eR = eps_word(T.WORD_R)
    out["eps(R) is a cyclic conjugate of R (free group)"] = cyclic_conjugate_of(eR, T.WORD_R) is not None
    out["eps^2 = id on m and n (free group)"] = eps_word(eps_word("m")) == "m" and eps_word(eps_word("n")) == "n"
    out["eps(x) = y, eps(y) = x (free group)"] = eps_word(x) == T.red(y) and eps_word(y) == T.red(x)
    out["eps(m) = x^-1 m^-1 (free group)"] = eps_word("m") == T.red(T.inv(x) + "M")
    eL = eps_word(T.WORD_L)
    out["eps(longitude) is a cyclic conjugate of the longitude^-1 (free group)"] = cyclic_conjugate_of(eL, T.inv(T.WORD_L)) is not None
    return out


# ALPHA is the figure-eight's amphichiral (orientation-reversing) symmetry: on the fibre psi: x -> x y^-1 x, y -> x y^-1 (abelianised
# [[2, 1], [-1, -1]], det -1, a square root of Phi^-1 commuting with Phi), extended by alpha(m) = y m (psi phi psi^-1 = c_y phi).
PSI = {"x": "xYx", "y": "xY"}
PSI_INV = {"x": "Yx", "y": "YYx"}
PHI_F = {"x": "y", "y": "yXyy"}
ALPHA = {"m": "mnM", "n": "nmNMnnM"}


def _app(phi, w):
    return T.red("".join(phi[c] if c.islower() else T.inv(phi[c.lower()]) for c in w))


def alpha_word(w):
    return _app(ALPHA, w)


def amphichiral_checks():
    """Lemma A: alpha is an automorphism of pi (the semidirect structure: psi phi(g) = y phi psi(g) y^-1 in the free group F(x, y)
    for g = x, y, psi invertible), it preserves the fibration and reverses the fibre's orientation (det -1); and
    C rho_q(g) C^-1 = rho_(1/q)(alpha g)."""
    out = {}
    conj = lambda w, g: T.red(w + g + T.inv(w))
    out["psi phi (g) = y phi psi (g) y^-1 for g = x, y (free group)"] = all(
        _app(PSI, _app(PHI_F, g)) == conj("y", _app(PHI_F, _app(PSI, g))) for g in "xy")
    out["psi psi^-1 = psi^-1 psi = id (free group)"] = all(_app(PSI, _app(PSI_INV, g)) == g and _app(PSI_INV, _app(PSI, g)) == g for g in "xy")
    # alpha in the letters m, n: alpha(m) = y m, alpha(n) = alpha(x) alpha(m) = psi(x) y m
    FX = {"x": T.FIBRE["x"], "y": T.FIBRE["y"]}
    to_mn = lambda w: _app(FX, w)
    out["alpha(m) = y m, alpha(n) = psi(x) y m (as words)"] = (ALPHA["m"] == T.red(to_mn("y") + "m")
                                                              and ALPHA["n"] == T.red(to_mn(PSI["x"]) + to_mn("y") + "m"))
    ab = {"x": (2, -1), "y": (1, -1)}
    out["psi abelianised (columns: images of x, y)"] = [[2, 1], [-1, -1]]
    M = sp.Matrix([[2, 1], [-1, -1]])
    out["M Phi = Phi M"] = M * T.PHI_AB == T.PHI_AB * M
    out["M^2 = Phi^-1"] = M * M == T.PHI_AB.inv()
    out["det M"] = int(M.det())
    mats = T.symbolic_mats()
    tgt = {g: T.word_matrix(_family(1 / q), ALPHA[g]).applyfunc(sp.cancel) for g in "mn"}
    dim, A = intertwiner_qq(mats, tgt)
    Ai = A.inv().applyfunc(sp.cancel)
    out["A: dimension"] = dim
    out["A (rho_q -> rho_1/q o alpha)"] = [[str(A[i, j]) for j in range(4)] for i in range(4)]
    out["det A"] = str(sp.factor(A.det()))
    out["A rho_q(g) A^-1 = rho_1/q(alpha g), g = m, n"] = all(sp.simplify(A * mats[g] * Ai - tgt[g]) == sp.zeros(4) for g in "mn")
    # the relator holds in the image: rho(alpha(R)) = 1 for the family (a consequence of the semidirect check, recorded)
    out["rho_q(alpha(R)) = 1 (over Q(q))"] = dm_word_is_one(alpha_word(T.WORD_R))
    return out


def dm_word_is_one(w):
    """rho_q(w) = 1 over Q(q), with DomainMatrix arithmetic (exact)"""
    K = sp.QQ.frac_field(q)
    mats = T.symbolic_mats()
    D = {g: DomainMatrix([[K.from_sympy(mats[g][i, j]) for j in range(4)] for i in range(4)], (4, 4), K) for g in "mn"}
    D.update({g.upper(): D[g].inv() for g in "mn"})
    X = DomainMatrix.eye(4, K)
    for c in w:
        X = X * D[c]
    return (X - DomainMatrix.eye(4, K)).is_zero_matrix


def fibre_action(images):
    """the action on H_1(F) = Z e_x + Z e_y of an automorphism of pi given by images of m and n (words), via the transversal m^k:
    the letter n read at coset k contributes Phi^k e_x; returns the 2 x 2 integer matrix (columns: images of e_x, e_y) and the sign
    sigma of the induced map on pi/F"""
    PHI_, PHIi = T.PHI_AB, T.PHI_AB.inv()

    def Pk(k):
        M = sp.eye(2)
        A = PHI_ if k >= 0 else PHIi
        for _ in range(abs(k)):
            M = A * M
        return M

    def ab(w):
        k, v = 0, sp.zeros(2, 1)
        for c in w:
            if c == "m":
                k += 1
            elif c == "M":
                k -= 1
            elif c == "n":
                v += Pk(k)[:, 0]
                k += 1
            elif c == "N":
                k -= 1
                v -= Pk(k)[:, 0]
        assert k == 0, ("not in the fibre", w)
        return v

    img = lambda w: _app(images, w)
    cols = [ab(img(T.FIBRE["x"])), ab(img(T.FIBRE["y"]))]
    sigma = sum(1 if c.islower() else -1 for c in images["m"])
    return sp.Matrix.hstack(*cols), sigma


def symmetry_table():
    """the fibre action, sigma, orientation and the family's image for iota, eps, alpha and the audit lane's theta (m -> m^-1,
    n -> n^-1); theta's fibre action compared with iota phi^-2 eps (a relation in Out(F_2) = GL_2(Z))"""
    THETA = {"m": "M", "n": "N"}
    rows = {}
    for name, imgs in [("iota", IOTA), ("eps", EPS), ("alpha", ALPHA), ("theta (F14)", THETA)]:
        A_, sig = fibre_action(imgs)
        rows[name] = {"images": imgs, "fibre action": [[int(A_[i, j]) for j in range(2)] for i in range(2)], "sigma": sig,
                      "fibre det": int(A_.det()), "orientation": "preserving" if int(A_.det()) * sig == 1 else "reversing"}
    I_, _ = fibre_action(IOTA)
    E_, _ = fibre_action(EPS)
    Th, _ = fibre_action(THETA)
    rows["theta = iota phi^-2 eps on H_1(F)"] = Th == I_ * T.PHI_AB.inv() ** 2 * E_
    return rows


def alpha_on_character(ab, N):
    """nu o alpha in exponent form: nu_F(psi(x)) = 2a - b, nu_F(psi(y)) = a - b"""
    a, b = ab
    return ((2 * a - b) % N, (a - b) % N)


def reciprocal_in_q_identity(P):
    """Lemma D's consequence: P(1/q, s) = s^4 P(q, 1/s) / P(q, 0)"""
    c0 = coeff_list(P)[0]
    return sp.simplify(sp.expand(P.subs(q, 1 / q) * c0 - s ** 4 * P.subs(s, 1 / s))) == 0


def iota_on_characters(n):
    """nu o iota = (nu_F^-1, lam): the fibre part of iota(z) = (y m)^n is y phi(y) ... phi^(n-1)(y), whose class N y lies in
    im(Phi^n - 1) (Phi - 1 is invertible over Z), so every character of T_n kills it.  Checked on every character."""
    chars, N = T.characters(n)
    Nvec = sp.zeros(2, 1)
    P = sp.eye(2)
    for _ in range(n):
        Nvec += P * sp.Matrix([0, 1])
        P = T.PHI_AB * P
    det_phi_minus_1 = (T.PHI_AB - sp.eye(2)).det()
    bad = [ab for ab in chars if (ab[0] * int(Nvec[0]) + ab[1] * int(Nvec[1])) % N != 0]
    # the F-part of (ym)^n as a word: y phi(y) ... phi^(n-1)(y); its abelianisation equals Nvec
    w = "".join(T.phi_power(k)["y"] for k in range(n))
    ab_w = [sum((1 if c == "x" else -1 if c == "X" else 0) for c in w), sum((1 if c == "y" else -1 if c == "Y" else 0) for c in w)]
    return {"level": n, "N": N, "det(Phi - 1)": int(det_phi_minus_1), "class of iota(z)'s fibre part": [int(Nvec[0]), int(Nvec[1])],
            "abelianised word agrees": ab_w == [int(Nvec[0]), int(Nvec[1])], "characters not killing it": len(bad)}


# ============================================================================================ Galois classes
def galois_class(ab, N):
    """all characters nu^k (k a unit mod N) and their inverses, closed under the deck"""
    out = set()
    for k in range(1, N):
        if math.gcd(k, N) != 1:
            continue
        for sgn in (1, -1):
            c = ((sgn * k * ab[0]) % N, (sgn * k * ab[1]) % N)
            cur = c
            while True:
                out.add(cur)
                cur = T.deck(cur, N)
                if cur == c:
                    break
    return out


def galois_closure_in_orbit_union(ab, N):
    """True iff every Galois conjugate nu^k lies in the deck orbit of nu or of nu^-1 (then P_nu is in Q[q^+-1, s])"""
    orb = set()
    for sgn in (1, -1):
        c = ((sgn * ab[0]) % N, (sgn * ab[1]) % N)
        cur = c
        while True:
            orb.add(cur)
            cur = T.deck(cur, N)
            if cur == c:
                break
    return all(((k * ab[0]) % N, (k * ab[1]) % N) in orb for k in range(1, N) if math.gcd(k, N) == 1)


def self_coincident_orbits(n):
    """the orbits with nu_F^4 != 1 and nu^5 in their own deck orbit (B1511 C10)"""
    chars, N, orbs, idx = TC.orbit_table(n)
    out = []
    for k, o in enumerate(orbs):
        ab = o[0]
        if all(((4 * x) % N) == 0 for x in ab):
            continue
        if idx[((5 * ab[0]) % N, (5 * ab[1]) % N)] == k:
            out.append((k, o))
    return N, orbs, idx, out


# ============================================================================================ P over Q by many primes
def next_prime_1_mod(m, start):
    p = start + (1 - start) % m
    if p <= start:
        p += m
    while not sp.isprime(p):
        p += m
    return p


def coeff_values(mp, ab, n, points):
    """for each point r: r^(16 n) times the coefficients c_0..c_4 of P_nu(r, s) (monic in s), over GF(p)"""
    p = mp.p
    out = [[] for _ in range(5)]
    for r in points:
        B = mp.blocks_at(r)
        P = mp.charpoly_H1(mp.level(B, ab, n))
        sh = pow(r, 16 * n, p)
        for k in range(5):
            out[k].append(sh * P[k] % p)
    return out


def coeffs_modp(mp, ab, n):
    """the five polynomials q^(16 n) c_k(q) over GF(p), by interpolation at 32 n + 1 points (constant first)"""
    D = 32 * n
    pts = list(range(1, D + 2))
    vals = coeff_values(mp, ab, n, pts)
    return [T.interpolate_modp(pts, vals[k], mp.p) for k in range(5)]


def ratrecon(u, M):
    """the rational a/b with a = b u mod M, |a|, b <= sqrt(M / 2), or None"""
    bound = math.isqrt(M // 2)
    r0, r1 = M, u % M
    s0, s1 = 0, 1
    while r1 > bound:
        qq = r0 // r1
        r0, r1 = r1, r0 - qq * r1
        s0, s1 = s1, s0 - qq * s1
    if s1 == 0 or abs(s1) > bound:
        return None
    a, b = r1, s1
    if b < 0:
        a, b = -a, -b
    if math.gcd(a, b) != 1:
        return None
    return sp.Rational(a, b)


def _pad(c, L):
    return list(c) + [0] * (L - len(c))


def reconstruct_P(ab, n, N, start=2 ** 31, stable=2, verify=2, max_primes=60, log=None):
    """P_nu(q, s) in Q[q^+-1, s] (valid when P_nu has rational coefficients, e.g. by the Galois lemma): CRT over primes
    p = 1 mod lcm(N, 4) above `start`, rational reconstruction after each prime; accepted after `stable` consecutive unchanged
    reconstructions, then checked at `verify` fresh primes.  Returns (P, record)."""
    mod = N * 4 // math.gcd(N, 4)
    L = 32 * n + 1
    M, X = 1, [[0] * L for _ in range(5)]
    prev, same, used = None, 0, []
    p = start
    while len(used) < max_primes:
        p = next_prime_1_mod(mod, p)
        mp = T.ModP(p, N)
        cs = [_pad(c, L) for c in coeffs_modp(mp, ab, n)]
        for k in range(5):
            for e in range(L):
                a, b = X[k][e], cs[k][e]
                # CRT of (a mod M) and (b mod p)
                t = (b - a) * pow(M, -1, p) % p
                X[k][e] = a + M * t
        M *= p
        used.append(p)
        rec = []
        okr = True
        for k in range(5):
            row = []
            for e in range(L):
                v = X[k][e] if X[k][e] <= M // 2 else X[k][e] - M
                rr = ratrecon(v % M, M)
                if rr is None:
                    okr = False
                    break
                row.append(rr)
            if not okr:
                break
            rec.append(tuple(row))
        if okr and rec == prev:
            same += 1
        else:
            same = 0
        prev = rec if okr else None
        if log:
            log(f"  reconstruct {ab} level {n}: prime {len(used)} ({p}), recon {'ok' if okr else 'none'}, unchanged {same}")
        if okr and same >= stable:
            break
    else:
        raise RuntimeError(("no stable reconstruction", ab, n, len(used)))
    # fresh-prime verification
    checks = []
    for _ in range(verify):
        p = next_prime_1_mod(mod, p)
        mp = T.ModP(p, N)
        cs = [_pad(c, L) for c in coeffs_modp(mp, ab, n)]
        red_ = [[(int(c.p) * pow(int(c.q), -1, p)) % p for c in row] for row in prev]
        checks.append({"p": p, "agrees": red_ == cs})
    P = sum(sum(c * q ** e for e, c in enumerate(prev[k])) * s ** k for k in range(5)) * q ** (-16 * n)
    P = sp.expand(P)
    record = {"primes_used": len(used), "first_prime": used[0], "last_prime": used[-1], "fresh_checks": checks,
              "all_fresh_agree": all(c["agrees"] for c in checks)}
    return P, record


def modp_choice_independent(ab, n, N, p, k):
    """P_nu over GF(p) with zeta replaced by zeta^k (k a unit): equal to the original iff Galois-stable at this prime"""
    mp = T.ModP(p, N)
    a = coeffs_modp(mp, ab, n)
    mp2 = T.ModP(p, N)
    mp2.zeta = pow(mp.zeta, k, p)
    b = coeffs_modp(mp2, ab, n)
    return a == b


# ============================================================================================ exact data of P
def coeff_list(P):
    """[c_0, ..., c_4] of P in s, each a Laurent polynomial in q"""
    Pp = sp.Poly(sp.expand(P), s)
    return [sp.expand(Pp.coeff_monomial(s ** k)) for k in range(5)]


def laurent_range(e):
    e = sp.expand(e)
    if e == 0:
        return None
    degs = [t.as_coeff_exponent(q)[1] for t in sp.Add.make_args(e)]
    return [int(min(degs)), int(max(degs))]


def numerator_poly(e):
    """the polynomial q^k e(q) with k the least making it a polynomial (the q-power stripped)"""
    num, den = sp.fraction(sp.cancel(sp.together(e)))
    Pn = sp.Poly(num, q)
    # strip q powers from the numerator
    while Pn.degree() > 0 and Pn.eval(0) == 0:
        Pn = sp.Poly(sp.cancel(Pn.as_expr() / q), q)
    return Pn


def symmetries(P):
    c = coeff_list(P)
    recip = sp.expand(s ** 4 * P.subs(s, 1 / s))
    return {"palindromic in s": sp.simplify(c[0] - 1) == 0 and sp.simplify(c[1] - c[3]) == 0,
            "reciprocal up to the constant term": sp.simplify(sp.expand(recip - c[0] * P)) == 0,
            "P(1/q, s) = P(q, s)": sp.simplify(sp.expand(P.subs(q, 1 / q) - P)) == 0,
            "constant term": str(sp.factor(c[0])),
            "Laurent ranges of c_0..c_3": [laurent_range(x) for x in c[:4]]}


def specialisation(P, l):
    """for lam = i^l: the real exceptional polynomial in Q[q] (lam = +-1: P(q, lam); lam = +-i: gcd(Re, Im)), stripped of q"""
    c = coeff_list(P)
    if l in (0, 2):
        lam = 1 if l == 0 else -1
        f = sum(c[k] * lam ** k for k in range(5))
        return numerator_poly(f), {"lam": str(lam)}
    A = c[0] - c[2] + c[4]
    B = c[1] - c[3] if l == 1 else c[3] - c[1]
    Ap, Bp = numerator_poly(A) if sp.expand(A) != 0 else None, numerator_poly(B) if sp.expand(B) != 0 else None
    if Ap is None and Bp is None:
        return None, {"lam": "i" if l == 1 else "-i", "identically_zero": True}
    if Ap is None:
        G = Bp
    elif Bp is None:
        G = Ap
    else:
        G = sp.gcd(Ap, Bp)
    return sp.Poly(G, q), {"lam": "i" if l == 1 else "-i", "Re identically 0": Ap is None, "Im identically 0": Bp is None,
                            "deg Re": None if Ap is None else Ap.degree(), "deg Im": None if Bp is None else Bp.degree()}


def positive_roots_report(G):
    """factor G over Q; for each factor its positive real roots other than 1 (exact isolation by sympy, cross-checked with arb)"""
    out = []
    if G is None:
        return out
    G = sp.Poly(G, q)
    if G.degree() <= 0:
        return out
    cont, facs = sp.factor_list(G.as_expr(), q)
    for g0, mult in facs:
        g0p = sp.Poly(g0, q)
        rr = sp.real_roots(g0p)
        pos = [r for r in rr if r.is_positive and r != 1]
        # arb cross-check: the number of real roots
        fz = flint.fmpz_poly([int(c) for c in reversed(sp.Poly(g0p.as_expr() * sp.lcm([sp.fraction(c)[1] for c in g0p.all_coeffs()]), q).all_coeffs())])
        nreal_arb = sum(1 for (z, m_) in fz.complex_roots() if (z.imag == 0 if hasattr(z, "imag") else True))
        out.append({"factor": str(g0p.as_expr()), "multiplicity": int(mult), "degree": g0p.degree(),
                    "real_roots_sympy": len(rr), "real_roots_arb": nreal_arb,
                    "positive_roots_not_1": [str(sp.N(r, 15)) for r in pos]})
    return out


# ============================================================================================ counts at a factor
def primes_with_roots(g0, mod, count=3, start=1000):
    """the `count` smallest primes p > start, p = 1 mod mod, at which g0 (integer-scaled) is squarefree of full degree with a root"""
    G = sp.Poly(g0, q)
    den = sp.lcm([sp.fraction(sp.Rational(c))[1] for c in G.all_coeffs()])
    Z = [int(c * den) for c in G.all_coeffs()]
    out = []
    p = start
    while len(out) < count:
        p = next_prime_1_mod(mod, p)
        fp = flint.nmod_poly(list(reversed(Z)), p)
        if fp.degree() != G.degree():
            continue
        if fp.gcd(fp.derivative()).degree() > 0:
            continue
        roots = sorted(int(r) for r, _ in fp.roots())
        if roots:
            out.append((p, roots))
    return out


class CoverCache:
    """the RS presentation of M_n and the symbolic generator matrices, converted per field"""

    def __init__(self, n):
        self.n = n
        self.cov = T.rs_cover(n)
        mats = T.symbolic_mats()
        self.W = {g: T.word_matrix(mats, self.cov["words"][g]).applyfunc(sp.cancel) for g in self.cov["gens"]}
        self.blocks = T.block_mats()

    def rho(self, field):
        return {g: field.mat(self.W[g]) for g in self.cov["gens"]}


def fibre_data_gf(cc, Fp, ab, N, l):
    """rank of the coboundary matrix (H^0(F) = 0 iff 4) and dim ker (S - lam)^j on H^1, j = 1..4, over GF(p)"""
    blocks = [Fp.mat(A) for A in cc.blocks]
    S = TC.fibre_P(Fp, blocks, ab, N, cc.n)
    FM = T.FibreMonodromy(Fp)
    B = FM.coboundary(ab, N)
    return {"rank_B": T.dm_rank(B), "ker_dims": T.kernel_dims_on_H1(S, B, Fp.unit(l, 4))}


def fibre_data_numeric(ab, N, n, alpha, l, dps=60):
    """at the real root itself: the complex character nu_F(x) = e^(2 pi i a / N), nu_F(y) = e^(2 pi i b / N) and lam = i^l, the kernel
    dimensions of (S - lam)^j on H^1 by singular values at dps digits; returns the dimensions and the gap (largest singular value
    counted as zero, smallest counted as non-zero)"""
    import mpmath as mpm
    mpm.mp.dps = dps
    a_val = mpm.mpf(sp.N(alpha, dps + 10))
    A1, A2, A3 = (mpm.matrix([[mpm.mpf(sp.N(A[i, j].subs(q, sp.N(alpha, dps + 10)), dps + 10)) for j in range(4)] for i in range(4)])
                  for A in T.block_mats())
    zeta = mpm.exp(2j * mpm.pi / N)
    lam = mpm.mpc(1j) ** l

    def one(c):
        al, be = zeta ** ((c[1] - c[0]) % N), zeta ** ((2 * c[1] - c[0]) % N)
        S = mpm.zeros(8, 8)
        for i in range(4):
            for j in range(4):
                S[i, 4 + j] = A1[i, j]
                S[4 + i, j] = -al * A2[i, j]
                S[4 + i, 4 + j] = A1[i, j] + al * A2[i, j] + be * A3[i, j]
        return S

    S = mpm.eye(8)
    cur = (ab[0] % N, ab[1] % N)
    for _ in range(n):
        S = one(cur) * S
        cur = T.deck(cur, N)
    mats = T.symbolic_mats()
    Rx = T.word_matrix(mats, T.FIBRE["x"]).subs(q, sp.N(alpha, dps + 10))
    Ry = T.word_matrix(mats, T.FIBRE["y"]).subs(q, sp.N(alpha, dps + 10))
    B = mpm.zeros(8, 4)
    for i in range(4):
        for j in range(4):
            B[i, j] = mpm.mpf(sp.N(Rx[i, j], dps + 10)) * zeta ** (ab[0] % N) - (1 if i == j else 0)
            B[4 + i, j] = mpm.mpf(sp.N(Ry[i, j], dps + 10)) * zeta ** (ab[1] % N) - (1 if i == j else 0)
    tol = mpm.mpf(10) ** (-(dps // 2))
    dims, zero_max, nonzero_min = [], mpm.mpf(0), mpm.mpf(10) ** 10
    Pw = mpm.eye(8)
    for _ in range(4):
        Pw = Pw * (S - lam * mpm.eye(8))
        Mx = mpm.zeros(8, 12)
        for i in range(8):
            for j in range(8):
                Mx[i, j] = Pw[i, j]
            for j in range(4):
                Mx[i, 8 + j] = B[i, j]
        sv = mpm.svd_c(Mx, compute_uv=False)
        rk = sum(1 for x in sv if abs(x) > tol)
        for x in sv:
            if abs(x) > tol:
                nonzero_min = min(nonzero_min, abs(x))
            else:
                zero_max = max(zero_max, abs(x))
        dims.append(8 - rk)
    svB = mpm.svd_c(B, compute_uv=False)
    rank_B = sum(1 for x in svB if abs(x) > tol)
    return {"rank_B": rank_B, "ker_dims": dims, "largest_zero_sv": mpm.nstr(zero_max, 3), "smallest_nonzero_sv": mpm.nstr(nonzero_min, 3)}


def counts_at(cc, p, r, members, N, lams, with_wedge=True):
    iota = IL.GF(p).root_of_unity(4)
    Fp = T.Field("gf", p=p, r=r, iota=iota)
    rho = cc.rho(Fp)
    rows = {}
    for ab in members:
        for l in lams:
            fib = fibre_data_gf(cc, Fp, ab, N, l)
            cnt = TC.counts_case_b(cc.cov, Fp, rho, ab, N, l, 4, "gf", p, with_wedge=with_wedge)
            rows[f"{ab}|{l}"] = {"fibre": fib, "counts": cnt}
    return rows
