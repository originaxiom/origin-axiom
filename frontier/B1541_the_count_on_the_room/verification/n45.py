"""B1541 -- the library: the cover N_45 and its classes, in two routes.

N_45 is the 5-fold cyclic cover of m003's degree-9 cover d9.2 along the order-5 character chi pulled back from m003's Z/5
torsion (u = (1/5, 3/5), kappa = 0); (n(1), n(rho)) = (4, 18) at its trivial character (the golden covers dossier's section 7,
to be banked as sm:B1540).  Its classes at the trivial character, H^1(N_45; rho) (dimension 23), are read here in two routes:
  - route N: sm:B1536's route_n (Shapiro on m003 with the degree-45 permutation module rho (x) C[X]), by path, unchanged.  A class
    is a cocycle vector z (generator-major, then point, then coordinate) of that module.
  - route R: sm:B1536's route_r (N_45's own Reidemeister-Schreier presentation), by path, unchanged.  A class is a list of
    values on the Schreier generators (left cocycles).
  - transport(z): route N's class as route R's class (Shapiro: the block at the base point, along each Schreier word), so that
    both routes read the same class at the same prime.
  - the deck group Z/5: tau, the permutation of X commuting with Gamma that moves the base point along the fibre over d9.2's
    base point; its action on route N's cocycles (deck_N) and, independently, on route R's (deck_R: (h c)(gamma) =
    rho(h) c(h^-1 gamma h), with 0^h = tau(0)); the isotypic projections onto tau's eigenspaces (Lemma A's characters chi^j).
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


R = _load("b1541_b1536_route_r", B1536V / "route_r.py")       # allocates PARI's stack: load first
N = _load("b1541_b1536_route_n", B1536V / "route_n.py")
CL = _load("b1541_b1536_cover_lib", B1536V / "cover_lib.py")
GF = _load("b1541_b1536_gf", B1536V / "gf.py")
POP = _load("b1541_b1536_population", B1536V / "population.py")
U0 = (Fr(1, 5), Fr(3, 5))


def d92():
    """(state, d9.2's perms)"""
    st = CL.state("m003")
    return st, dict(POP.covers(st))["d9.2"]


def chi_exponents(st, perms):
    """the order-5 character chi on d9.2's Schreier generators (route_r.PCover), as exponents of a primitive Nroot-th root,
    and Nroot, via sm:B1536's own character (Base.character at u = U0, kappa = 0)"""
    from cypari import pari
    cus, L, Nroot, _ = POP.characters(st, perms)
    p = GF.primes_1_mod(Nroot, 1 << 31, 1)[0]
    B = N.Base(st, GF.GF(p, Nroot))
    chi = B.character(U0, Fr(0))
    cov = R.PCover(st["G"], perms)
    r = int(pari.lift(pari.znprimroot(p) ** ((p - 1) // Nroot)))
    table = {pow(r, e, p): e for e in range(Nroot)}
    exps = []
    for w in cov.sword:
        v = 1
        for c in w:
            x = int(chi[c.lower()])
            v = v * (x if c.islower() else pow(x, -1, p)) % p
        exps.append(table[v])
    return cov, exps, Nroot


def build():
    """N_45: (state, perms, fibre map point -> (d9.2 point, k mod 5), the deck permutation tau (k -> k + 1))"""
    st, perms9 = d92()
    cov9, exps, Nroot = chi_exponents(st, perms9)
    k5 = Nroot // 5
    assert all(e % k5 == 0 for e in exps), "chi is not of order dividing 5 on d9.2"
    step = {sg: (e // k5) % 5 for sg, e in zip(cov9.sgens, exps)}
    assert any(step.values()), "chi is trivial on d9.2"
    idx, pts = {(0, 0): 0}, [(0, 0)]
    for (x, k) in pts:
        for g in cov9.gens:
            key = (cov9.P[g][x], (k + step.get((x, g), 0)) % 5)
            if key not in idx:
                idx[key] = len(pts)
                pts.append(key)
    assert len(pts) == 5 * cov9.d, "N_45 is not connected of degree 45"
    perms = {g: [idx[(cov9.P[g][x], (k + step.get((x, g), 0)) % 5)] for (x, k) in pts] for g in cov9.gens}
    tau = [idx[(x, (k + 1) % 5)] for (x, k) in pts]
    for g in cov9.gens:                                   # tau commutes with Gamma, and has order 5
        assert all(perms[g][tau[i]] == tau[perms[g][i]] for i in range(len(pts)))
    t5 = list(range(len(pts)))
    for _ in range(5):
        t5 = [tau[i] for i in t5]
    assert t5 == list(range(len(pts))) and tau[0] != 0
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


def zeta5(p):
    """a primitive 5th root of unity mod p (p = 1 mod 5)"""
    for a in range(2, p):
        z = pow(a, (p - 1) // 5, p)
        if z != 1:
            return z
    raise ValueError(p)


def project(z, deck, j, p):
    """the isotypic projection onto deck's eigenvalue zeta5(p)^j: (1/5) sum_k zeta^(-jk) deck^k z"""
    zt = zeta5(p)
    out = np.zeros_like(z)
    cur = z % p
    for k in range(5):
        out = (out + pow(zt, (-j * k) % 5, p) * cur) % p
        cur = deck(cur) % p
    return out * pow(5, -1, p) % p


def transport(z, st, perms, cov, B, e=4):
    """route N's cocycle z (left cocycles of rho (x) C[X] on Gamma = pi_1 m003) as route R's values on N_45's Schreier
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
