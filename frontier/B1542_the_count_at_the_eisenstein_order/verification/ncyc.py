"""B1542 -- the library: a k-fold cyclic cover of one of sm:B1536's covers along a pulled-back character, and its classes, in
two routes.  It is sm:B1541's n45.py with the cover, the character and the order k as arguments; at (m003, d9.2, (1/5, 3/5), 0,
5) it builds sm:B1541's N_45 (control K4 checks the canonical form).

The covers read here: the 6-fold cyclic covers of m003's degree-10 covers d10.13, d10.16, d10.36 and d10.40 along the order-6
character psi = (u, kappa) = ((0, 0), 1/6) of m003 (the fibre direction), degree 60; sm:B1540 (room_60.json) read them at the
trivial character -- (n(1), n(rho)) = (3, 3), room 3, on d10.13 and d10.36; (3, 7), room 4, on d10.16 and d10.40.
  - route N: sm:B1536's route_n (Shapiro on m003 with the degree-60 permutation module rho (x) C[X]), by path, unchanged.  A class
    is a cocycle vector z (generator-major, then point, then coordinate) of that module.
  - route R: sm:B1536's route_r (the cover's own Reidemeister-Schreier presentation), by path, unchanged.  A class is a list of
    values on the Schreier generators (left cocycles).
  - transport(z): route N's class as route R's class (Shapiro: the block at the base point, along each Schreier word), so that
    both routes read the same class at the same prime.
  - the deck group Z/k: tau, the permutation of X commuting with Gamma that moves the base point along the fibre over the base
    cover's base point; its action on route N's cocycles (deck_N) and, independently, on route R's (deck_R: (h c)(gamma) =
    rho(h) c(h^-1 gamma h), with 0^h = tau(0)); the isotypic projections onto tau's eigenspaces (Lemma A's characters psi^j).
Nothing here reads a count; the structure checks are in controls.py."""
import importlib.util
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"


def _load(alias, path):
    if alias not in sys.modules:
        if str(B1536V) not in sys.path:
            sys.path.append(str(B1536V))
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


R = _load("b1542_b1536_route_r", B1536V / "route_r.py")       # allocates PARI's stack: load first
N = _load("b1542_b1536_route_n", B1536V / "route_n.py")
CL = _load("b1542_b1536_cover_lib", B1536V / "cover_lib.py")
GF = _load("b1542_b1536_gf", B1536V / "gf.py")
POP = _load("b1542_b1536_population", B1536V / "population.py")


def base_cover(state, cid):
    """(state, perms) of one of sm:B1536's covers"""
    st = CL.state(state)
    return st, dict(POP.covers(st))[cid]


def psi_exponents(st, perms, u, kappa):
    """the state's character psi = (u, kappa) on the cover's Schreier generators (route_r.PCover), as exponents of a primitive
    Nroot-th root, and Nroot, via sm:B1536's own character (Base.character)"""
    from cypari import pari
    cus, L, Nroot, _ = POP.characters(st, perms)
    p = GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    B = N.Base(st, GF.GF(p, Nroot))
    psi = B.character(u, kappa)
    cov = R.PCover(st["G"], perms)
    r = int(pari.lift(pari.znprimroot(p) ** ((p - 1) // Nroot)))
    table = {pow(r, e, p): e for e in range(Nroot)}
    exps = []
    for w in cov.sword:
        v = 1
        for c in w:
            x = int(psi[c.lower()])
            v = v * (x if c.islower() else pow(x, -1, p)) % p
        exps.append(table[v])
    return cov, exps, Nroot


def build(state, cid, u, kappa, k):
    """the k-fold cyclic cover of (state, cid) along psi = (u, kappa) restricted to it: (state, perms, fibre map point -> (base
    point, i mod k), the deck permutation tau (i -> i + 1)).  Asserts that psi restricts to a character of order exactly k."""
    st, perms0 = base_cover(state, cid)
    cov0, exps, Nroot = psi_exponents(st, perms0, u, kappa)
    assert Nroot % k == 0, "the root order does not carry the order k"
    q = Nroot // k
    assert all(e % q == 0 for e in exps), "psi is not of order dividing k on the cover"
    step = {sg: (e // q) % k for sg, e in zip(cov0.sgens, exps)}
    g = k
    for s in step.values():
        g = gcd(g, s)
    assert g == 1, "psi does not have order exactly k on the cover"
    idx, pts = {(0, 0): 0}, [(0, 0)]
    for (x, i) in pts:
        for gen in cov0.gens:
            key = (cov0.P[gen][x], (i + step.get((x, gen), 0)) % k)
            if key not in idx:
                idx[key] = len(pts)
                pts.append(key)
    assert len(pts) == k * cov0.d, "the cyclic cover is not connected of degree k d"
    perms = {gen: [idx[(cov0.P[gen][x], (i + step.get((x, gen), 0)) % k)] for (x, i) in pts] for gen in cov0.gens}
    tau = [idx[(x, (i + 1) % k)] for (x, i) in pts]
    for gen in cov0.gens:                                 # tau commutes with Gamma
        assert all(perms[gen][tau[j]] == tau[perms[gen][j]] for j in range(len(pts)))
    tk = list(range(len(pts)))                            # tau has order exactly k
    for m in range(1, k + 1):
        tk = [tau[j] for j in tk]
        assert (tk == list(range(len(pts)))) == (m == k), "tau does not have order exactly k"
    assert CL.check_cover(st["G"], perms), "the cyclic cover is not a cover"
    return st, perms, pts, tau


def route_n_setup(st, perms):
    """route N at the trivial character: (Base, perm arrays, chi = 1, class space (mod, Zb, R, BP), cusps with 'trivial')"""
    cus, L, Nroot, _ = POP.characters(st, perms)
    p = GF.primes_1_mod(Nroot, N.P_BOUND, 1)[0]
    B = N.Base(st, GF.GF(p, Nroot))
    chi = B.character((Fr(0), Fr(0)), Fr(0))
    pa = N.perm_arrays(st["G"], perms)
    mod, Zb, Rm, BP = N.class_space(B, pa, chi)
    cusps = [dict(c, trivial=True) for c in cus]
    return B, pa, chi, (mod, Zb, Rm, BP), cusps


def deck_N(z, tau, ngens, e=4):
    """tau on route N's cocycle vector: the block at point x moves to the block at tau(x), for every generator"""
    d = len(tau)
    D = d * e
    out = np.zeros_like(z)
    for gi in range(ngens):
        for x in range(d):
            out[gi * D + tau[x] * e:gi * D + (tau[x] + 1) * e] = z[gi * D + x * e:gi * D + (x + 1) * e]
    return out


def zeta(p, k):
    """a primitive k-th root of unity mod p (p = 1 mod k): order exactly k, checked at every prime divisor of k"""
    assert (p - 1) % k == 0
    primes = [q for q in range(2, k + 1) if k % q == 0 and all(q % r for r in range(2, q))]
    for a in range(2, p):
        z = pow(a, (p - 1) // k, p)
        if all(pow(z, k // q, p) != 1 for q in primes):
            return z
    raise ValueError((p, k))


def project(z, deck, j, p, k):
    """the isotypic projection onto deck's eigenvalue zeta(p, k)^j: (1/k) sum_i zeta^(-j i) deck^i z"""
    zt = zeta(p, k)
    out = np.zeros_like(z)
    cur = z % p
    for i in range(k):
        out = (out + pow(zt, (-j * i) % k, p) * cur) % p
        cur = deck(cur) % p
    return out * pow(k, -1, p) % p


def transport(z, st, perms, cov, B, e=4):
    """route N's cocycle z (left cocycles of rho (x) C[X] on Gamma = pi_1 of the state) as route R's values on the cover's Schreier
    generators: c(w) = (z(w)) at the base point's block, z(w) = sum over letters of prefix z(letter) (left cocycles).
    The block of M_prefix z_g at the base point is rho(prefix) z_g[block 0^prefix]."""
    p = B.p
    gens = list(st["G"].gens)
    d = len(perms[gens[0]])
    D = d * e
    zg = {g: z[gi * D:(gi + 1) * D] for gi, g in enumerate(gens)}
    rho = {g: np.asarray(B.rho[g], dtype=np.int64) % p for g in gens}
    rinv = {g: R.RS.minv(rho[g], p) for g in gens}
    inv = {g: [0] * d for g in gens}
    for g in gens:
        for x, y in enumerate(perms[g]):
            inv[g][y] = x
    out = []
    for w in cov.sword:
        val = np.zeros(e, dtype=np.int64)
        Pre = np.eye(e, dtype=np.int64)
        x = 0                                           # 0^prefix
        for c in w:
            g = c.lower()
            if c.islower():
                val = (val + R.mm(Pre, zg[g][x * e:(x + 1) * e].reshape(-1, 1), p).ravel()) % p
                Pre = R.mm(Pre, rho[g], p)
                x = perms[g][x]
            else:
                Pre = R.mm(Pre, rinv[g], p)
                x = inv[g][x]
                val = (val - R.mm(Pre, zg[g][x * e:(x + 1) * e].reshape(-1, 1), p).ravel()) % p
        assert x == 0
        out.append(val)
    return out


def path_word(perms, gens, target):
    """a word h (in the generators, positive letters only) with 0^h = target (breadth first)"""
    prev = {0: None}
    order = [0]
    for x in order:
        for g in gens:
            y = perms[g][x]
            if y not in prev:
                prev[y] = (x, g)
                order.append(y)
    w, y = [], target
    while prev[y] is not None:
        x, g = prev[y]
        w.append(g)
        y = x
    return "".join(reversed(w))


def deck_R_matrix(cov, rho, tau, p, e=4):
    """route R's own deck action on cocycle vectors (values on the Schreier generators, generator-major): with h a word, 0^h =
    tau(0), (h c)(s_j) = rho(h) c(h^-1 s_j h), the conjugate rewritten into Schreier generators (route_r.fox on the lifted
    module).  Returns the (ng e) x (ng e) matrix T with (T c)[j] = sum_k K_jk c[k]."""
    gens = list(cov.gens)
    h = path_word({g: cov.P[g] for g in gens}, gens, tau[0])
    hinv = CL.inv_word(h)
    mod = R.lift(cov, rho, p)
    rh = R.base_word(rho, h, p)
    ng = len(cov.sgens)
    T = np.zeros((ng * e, ng * e), dtype=np.int64)
    for j, w in enumerate(cov.sword):
        rw, end = cov.rewrite(0, hinv + w + h)
        assert end == 0
        K = R.fox(mod, rw, ng)                        # e x (ng e): c(word) = K c
        T[j * e:(j + 1) * e, :] = R.mm(rh, K, p)
    return T
