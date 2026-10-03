#!/usr/bin/env python3
"""B1530 -- route E's states: the groups, the exact holonomies, the four, and the characters.  Nothing sealed is computed on
import.

- group(sign, word): sm:B1527's family_lib.word_group (Gamma = F x| <t>, F = <a, b>, the cusp <abAB, t'>, t' = t for + and abt
  for -), with the characters of F that phi fixes (family_lib.torsion_characters).
- m135_sl2(): the exact holonomy of m135 = -LLRR in PGL(2, Q(i)), as sm:B1529's post_run_exact_m135.exact_sl2 reads it (the
  60-digit point, conjugated so the cusp's fixed point p0 goes to infinity, a(p0) to 0 and b(p0) to 1, each generator divided by
  its largest entry; the relators checked there in exact arithmetic).
- eisenstein_sl2(sign, word): the same reading over Q(omega), for m004 = +LR (its cusp field is Q(sqrt -3)).
- four(g): H -> g H g* / |det g| on Hermitian H = [[x1, x3 + i x4], [x3 - i x4, x2]], in the coordinates (x1, x2, x3, x4), as
  sm:B1529's post_run_exact_m135.four; |det g| is the square root of a rational and lies in Q(zeta_24) here.
- nu(sign, u, kappa_turn): the character with nu(a) = e^{2 pi i u_a}, nu(b) = e^{2 pi i u_b}, nu(t') = e^{2 pi i kappa_turn}."""
import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_lib as E  # noqa: E402

ROOT = HERE.parents[2]
B1527 = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
B1529 = ROOT / "frontier" / "B1529_the_eigenvalue_one_locus" / "verification"
DEN_MAX = 10 ** 9
READ_TOL = mp.mpf(10) ** -50


def load(where, name, alias):
    """a module by path, registered under alias (sm:B1527's modules import each other by bare name, so their directory goes on
    sys.path)"""
    if alias in sys.modules:
        return sys.modules[alias]
    if str(where) not in sys.path:
        sys.path.append(str(where))
    spec = importlib.util.spec_from_file_location(alias, where / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[alias] = mod
    spec.loader.exec_module(mod)
    return mod


def family():
    return load(B1527, "family_lib", "family_lib")


def group(sign, word):
    FL = family()
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    return E.Group(G.gens, G.rels, G.cusp, G.name), img, chars, D


def tprime(sign):
    return "t" if sign == "+" else "abt"


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] != c and out[-1].lower() == c.lower():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def phi_prime(sign, img):
    """t' g t'^-1 as a word in a, b: phi for +, (ab) phi(g) (ab)^-1 for -"""
    if sign == "+":
        return dict(img)
    return {g: free_reduce("ab" + img[g] + "BA") for g in "ab"}


# ============================================================================================ exact holonomies
def m135_sl2():
    P = load(B1529, "post_run_exact_m135", "b1529_post_run_exact_m135")
    g2 = P.exact_sl2()
    return {g: [[E.from_z8(x) for x in row] for row in g2[g]] for g in "abt"}


def _read_eisenstein(x):
    """x = p + q omega, p, q rational"""
    q = Fraction(mp.nstr(2 * mp.im(x) / mp.sqrt(3), 58, min_fixed=-200, max_fixed=200)).limit_denominator(DEN_MAX)
    p = Fraction(mp.nstr(mp.re(x) + mp.mpf(q.numerator) / q.denominator / 2, 58, min_fixed=-200,
                         max_fixed=200)).limit_denominator(DEN_MAX)
    om = mp.mpc(-0.5, mp.sqrt(3) / 2)
    val = mp.mpf(p.numerator) / p.denominator + mp.mpf(q.numerator) / q.denominator * om
    assert abs(val - x) < READ_TOL, (x, p, q)
    return E.K.of(p) + E.K.of(q) * E.OMEGA


def eisenstein_sl2(sign, word):
    mp.mp.dps = 60
    FL = family()
    A, B, Tm, _ = FL.hyperbolic_sl2(sign, word)
    M = {"a": A, "b": B, "t": Tm}
    lm = FL.sl2_word("abAB", M)
    p0 = (lm[0, 0] - lm[1, 1]) / (2 * lm[1, 0])

    def mob(g, z):
        return (g[0, 0] * z + g[0, 1]) / (g[1, 0] * z + g[1, 1])
    p1, p2 = mob(A, p0), mob(B, p0)
    Cm = mp.matrix([[p2 - p0, -p1 * (p2 - p0)], [p2 - p1, -p0 * (p2 - p1)]])
    Ci = mp.inverse(Cm)
    out = {}
    for g in "abt":
        gp = Cm * M[g] * Ci
        piv = max(((i, j) for i in range(2) for j in range(2)), key=lambda ij: abs(gp[ij]))
        gq = gp / gp[piv]
        out[g] = [[_read_eisenstein(gq[i, j]) for j in range(2)] for i in range(2)]
    return out


def is_scalar2(X_):
    return X_[0][1].is_zero() and X_[1][0].is_zero() and X_[0][0] == X_[1][1]


def check_sl2(G, g2):
    """the relators are scalars in PGL(2), the cusp generators commute and are parabolic"""
    mod = E.Module(["a", "b", "t"], g2)
    out = {}
    for r in G.rels:
        out["relator " + r + " scalar"] = is_scalar2(mod.word(r))
    P1, P2 = mod.word(G.cusp[0]), mod.word(G.cusp[1])
    out["cusp generators commute"] = all((E.mmul(P1, P2)[i][j] == E.mmul(P2, P1)[i][j]) for i in range(2) for j in range(2))
    for name, X_ in (("l", P1), ("t'", P2)):
        tr = X_[0][0] + X_[1][1]
        det = X_[0][0] * X_[1][1] - X_[0][1] * X_[1][0]
        out[name + " parabolic"] = (tr * tr == det * 4) and not is_scalar2(X_)
    return out


# ============================================================================================ the four
_HERM = [E.mat([[1, 0], [0, 0]]), E.mat([[0, 0], [0, 1]]), E.mat([[0, 1], [1, 0]]),
         [[E.ZERO, E.I_UNIT], [-E.I_UNIT, E.ZERO]]]


def four(g):
    """H -> g H g* / |det g| in the coordinates (x1, x2, x3, x4) of H = [[x1, x3 + i x4], [x3 - i x4, x2]]"""
    gs = [[g[j][i].conj() for j in range(2)] for i in range(2)]
    d = g[0][0] * g[1][1] - g[0][1] * g[1][0]
    nrm = (d * d.conj()).rational()
    assert nrm is not None and nrm > 0
    absdet = E.sqrt_rational(nrm)
    half = E.K.of(Fraction(1, 2))
    cols = []
    for H in _HERM:
        Hn = E.mmul(E.mmul(g, H), gs)
        z = Hn[0][1]
        re = (z + z.conj()) * half
        im = (z - z.conj()) / (E.I_UNIT * 2)
        cols.append([Hn[0][0], Hn[1][1], re, im])
    return [[cols[j][i] / absdet for j in range(4)] for i in range(4)]


def four_module(g2):
    return E.Module(["a", "b", "t"], {g: four(g2[g]) for g in "abt"})


def power_t(g2, n):
    """the holonomy of the n-fold cyclic level: a, b kept, t -> t^n"""
    T = E.eye(2)
    for _ in range(n):
        T = E.mmul(T, g2["t"])
    return {"a": g2["a"], "b": g2["b"], "t": T}


# ============================================================================================ characters
def nu(sign, u, kappa_turn=0):
    """nu(a) = e^{2 pi i u_a}, nu(b) = e^{2 pi i u_b}, nu(t') = e^{2 pi i kappa_turn} (all of order dividing 24); nu(t) is
    nu(t') for + and nu(t') / (nu(a) nu(b)) for - (t' = abt)"""
    na, nb = E.root_of_unity(Fraction(u[0])), E.root_of_unity(Fraction(u[1]))
    k = E.root_of_unity(Fraction(kappa_turn))
    lam = k if sign == "+" else k / (na * nb)
    return {"a": na, "b": nb, "t": lam}


def power_char(ch, m):
    out = {}
    for g, v in ch.items():
        x = E.ONE
        for _ in range(m % 24):
            x = x * v
        out[g] = x
    return out
