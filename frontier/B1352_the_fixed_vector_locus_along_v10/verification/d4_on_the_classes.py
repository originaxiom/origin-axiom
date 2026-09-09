#!/usr/bin/env python3
"""B1352 stage B -- THE FULL ISOMETRY GROUP ON THE DEFORMATION CLASSES: the eight isometries of m004 (B1279's words) acting on
H^1(M; Sym^n rho) for even n <= 16 -- linearly for the four orientation-preserving ones (the inversion iota, the period-2 swap
tau, iota.tau, the identity; B1280's six signs extended to every sl2-block), and ANTILINEARLY for the four orientation-reversing
glides (rho o sigma is conjugate to the Galois-conjugate representation rho-bar, so J_sigma z = conj(g^-1 z(sigma .)) is a
conjugate-linear map of H^1 whose square is the linear action of sigma^2).  Exact over Q(zeta_12) = Q(omega, i) (sympy).

Why: Pantev-Wijnholt's d+ on a cusp-fixed weight is decided by the leading symmetry-allowed Fourier mode of the Higgs field's
radial component on the cusp torus (B1277's instrument).  The region-swap theorem uses only the inversion's parity (-1 for
iota-odd fields).  The V10 field is iota-EVEN; what decides its leading mode is the parity under the glides, which is not a
sign of a complex class but of a REAL form: J_sigma^2 = +1 on V10 makes both parities available, one per real form."""
from __future__ import annotations
import sys, itertools
import sympy as sp
from sympy import sqrt, I, Rational, Matrix, eye, zeros, simplify, nsimplify

w = Rational(-1, 2) + I * sqrt(3) / 2          # omega = e^{2 pi i / 3}
u = 1 + w                                        # the Riley root u = e^{i pi / 3}
def conj_field(x):                               # Galois conjugation of Q(omega, i): omega -> omega^2, i -> -i  (complex conjugation)
    return sp.conjugate(x)
RHO = {'a': Matrix([[1, 1], [0, 1]]), 'b': Matrix([[1, 0], [u, 1]])}
RHO['A'] = RHO['a'].inv(); RHO['B'] = RHO['b'].inv()
RHOBAR = {k: v.applyfunc(conj_field) for k, v in RHO.items()}
def ev(word, rho):
    M = eye(2)
    for c in word: M = M * rho[c]
    return M.applyfunc(simplify)
# the presentation (B1267's relator, in the letters of B1279's word search: a w b^-1 w^-1, w = b A B a)
W = 'bABa'; REL = 'a' + W + 'B' + ''.join({'a':'A','A':'a','b':'B','B':'b'}[c] for c in reversed(W))
assert ev(REL, RHO) == eye(2), "relator"
ISOS = {  # B1279: cusp map (s_mu, s_lam), translation (b_mu, b_lam), the substitution, orientation
    'id':      ((1, 1), (0, 0), {'a': 'a', 'b': 'b'}, +1),
    'tau':     ((1, 1), (0, Rational(1, 2)), {'a': 'b', 'b': 'a'}, +1),
    'iota':    ((-1, -1), (0, 0), {'a': 'A', 'b': 'B'}, +1),
    'iota.tau':((-1, -1), (0, Rational(1, 2)), {'a': 'B', 'b': 'A'}, +1),
    'g1':      ((-1, 1), (Rational(1, 2), Rational(1, 4)), {'a': 'A', 'b': 'bAB'}, -1),
    'g2':      ((-1, 1), (Rational(1, 2), Rational(3, 4)), {'a': 'A', 'b': 'BAb'}, -1),
    'g3':      ((1, -1), (Rational(1, 2), Rational(1, 4)), {'a': 'a', 'b': 'baB'}, -1),
    'g4':      ((1, -1), (Rational(1, 2), Rational(3, 4)), {'a': 'a', 'b': 'Bab'}, -1),
}
INVL = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
def subst(word, s):
    out = ''
    for c in word:
        if c in 'ab': out += s[c]
        else: out += ''.join(INVL[d] for d in reversed(s[INVL[c]]))
    return out
def reduce(wd):
    out = []
    for c in wd:
        if out and out[-1] == INVL[c]: out.pop()
        else: out.append(c)
    return ''.join(out)

def intertwiner(s, orient):
    """g with rho(sigma(x)) = g R(x) g^-1 for x = a, b, R = rho (orientation +) or rho-bar (orientation -); solved linearly, normalised."""
    R = RHO if orient > 0 else RHOBAR
    g = Matrix(2, 2, sp.symbols('g0:4'))
    eqs = []
    for x in 'ab':
        lhs = ev(reduce(subst(x, s)), RHO) * g; rhs = g * R[x]
        eqs += list((lhs - rhs).applyfunc(sp.expand))
    sol = sp.linsolve(eqs, list(g))
    sol = list(sol)[0]
    free = [t for t in sol.free_symbols]
    assert len(free) == 1, (s, sol)
    gm = Matrix(2, 2, [e.subs({free[0]: 1}) for e in sol]).applyfunc(simplify)
    det = simplify(gm.det()); assert det != 0
    gm = (gm / sp.sqrt(det)).applyfunc(simplify)     # det 1
    for x in 'ab':
        assert (ev(reduce(subst(x, s)), RHO) - gm * R[x] * gm.inv()).applyfunc(simplify) == zeros(2, 2), ("intertwiner", s, x)
    return gm

def symn(g, n):
    """Sym^n(g) on the basis x^{n-j} y^j, the substitution x -> g00 x + g10 y, y -> g01 x + g11 y (g acting on (x, y) as a column)."""
    x, y = sp.symbols('x y')
    X = g[0, 0] * x + g[0, 1] * y; Y = g[1, 0] * x + g[1, 1] * y
    cols = []
    for j in range(n + 1):
        pol = sp.Poly(sp.expand(X ** (n - j) * Y ** j), x, y)
        cols.append([simplify(pol.coeff_monomial(x ** (n - k) * y ** k)) for k in range(n + 1)])
    return Matrix(cols).T

def cocycle_data(n, rho):
    """Z^1(F_2; Sym^n rho) restricted to the relator: the Fox matrix; returns (S = {x: Sym^n rho(x)}, kernel basis of the relator's Fox map, coboundary matrix)."""
    S = {k: symn(v, n) for k, v in rho.items()}
    d = n + 1
    # Fox derivative of the relator wrt a and b in the representation (left convention)
    def fox(word, gen):
        acc = zeros(d, d); cur = eye(d)
        for c in word:
            if c == gen: acc += cur
            if c == INVL[gen]:
                cur = cur * S[c]; acc -= cur; continue
            cur = cur * S[c]
        return acc
    Fa, Fb = fox(REL, 'a'), fox(REL, 'b')
    J = Fa.row_join(Fb).applyfunc(simplify)          # d x 2d
    ker = J.nullspace()
    cob = (S['a'] - eye(d)).col_join(S['b'] - eye(d))  # 2d x d
    return S, ker, cob

def transport(z, s, orient, gsym, n, S):
    """(J_sigma z): x -> gsym^-1 z(sigma(x)) for orientation +, conj(gsym^-1 z(sigma(x))) for orientation -; z given by its values on a, b."""
    d = n + 1
    za, zb = z[:d, :], z[d:, :]
    def val(word):
        acc = zeros(d, 1); cur = eye(d)
        for c in word:
            if c in 'ab':
                acc += cur * (za if c == 'a' else zb); cur = cur * S[c]
            else:
                cur = cur * S[c]; acc -= cur * (za if c == 'A' else zb)
        return acc
    out = []
    for x in 'ab':
        v = gsym.inv() * val(reduce(subst(x, s)))
        out.append(v.applyfunc(conj_field) if orient < 0 else v)
    return out[0].col_join(out[1]).applyfunc(simplify)

def main(ns=(2, 4, 6, 8, 10, 12, 14, 16)):
    G = {name: intertwiner(s, o) for name, (_, _, s, o) in ISOS.items()}
    print("intertwiners found for all eight isometries (rho o sigma = g rho g^-1 for the four orientation-preserving, = g rho-bar g^-1 for the four glides)")
    table = {}
    for n in ns:
        S, ker, cob = cocycle_data(n, RHO)
        rB = cob.rank(); h1 = len(ker) - rB
        # a non-coboundary cocycle
        z = next(k for k in ker if cob.row_join(k).rank() > rB)
        row = {}
        for name, (cm, b, s, o) in ISOS.items():
            gs = symn(G[name], n)
            zz = transport(z, s, o, gs, n, S)
            # zz = eps z + coboundary?  solve zz - eps z in image(cob) for eps in {+1, -1}; else report the matrix (h1 = 1 => a scalar; antilinear: a phase)
            eps = None
            for e in (1, -1):
                if cob.row_join(zz - e * z).rank() == rB: eps = e; break
            if eps is None:
                # general scalar c with zz = c z mod B^1: project
                Mfull = cob.row_join(z)
                sol = sp.linsolve((Mfull, zz))
                c = simplify(list(sol)[0][-1]) if sol else None
                eps = c
            row[name] = eps
        table[n] = (h1, row)
        print(f"  n = {n:2d}: h1 = {h1};  " + "  ".join(f"{k}: {row[k]}" for k in ISOS))
    # the squares of the glides on the class space: (J_sigma)^2 acts as sigma^2, which lies in the Klein four-group
    print("\nfor each glide, sigma^2 as a substitution and its class in the Klein four-group {id, tau, iota, iota.tau}:")
    for name in ('g1', 'g2', 'g3', 'g4'):
        s = ISOS[name][2]
        s2 = {x: reduce(subst(s[x], s)) for x in 'ab'}
        print(f"  {name}^2: a -> {s2['a']}, b -> {s2['b']}")
    return table

if __name__ == "__main__":
    ns = tuple(int(a) for a in sys.argv[1:]) or (2, 4, 6, 8, 10, 12, 14, 16)
    main(ns)
