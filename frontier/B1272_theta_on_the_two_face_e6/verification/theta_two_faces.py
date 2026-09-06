#!/usr/bin/env python3
"""THE OBJECT'S MIRROR ON THE TWO-FACE E6 -- the fork's real form, decided on the lattice.

THE_STATE_2026-09-06 section 7 item 2 (JOIN 3): "does the object's theta act as an outer involution,
and with which fixed subalgebra?"  B1265-main: the fork is a rank obstruction -- D2 (inner) selects
E6(-14); E6(-26) needs an OUTER involution, "which is precisely theta".  Here theta is built from the
object and read on B1270's two-face E6.

(a) THE MIRROR, DERIVED.  The amphichirality of A = LR is conjugation by P = diag(1,-1): P R P^-1 =
    R^-1, P L P^-1 = L^-1.  Reduced mod 5 -- the golden face, <R,L> mod 5 = SL(2,F5) = 2I -- det P = -1 =
    2^2 is a SQUARE, so the mirror is INNER on 2I: conjugation by diag(3,2), an element of order 4, whose
    image h under B1270's isomorphism is a unit icosian of order 4.  Ad(h) inverts R_q and L_q; it sends
    the founding ratio g to a conjugate of g^-1 (not g^-1 itself), and the representative h' = L_q h of
    the same mirror class sends g to g^-1 exactly, hence preserves Z[g] and E6 = Z[g]^perp.  Ad(h') is
    an involution on the lattice (h'^2 = -1).

(b) THREE INVOLUTIONS ON E6, THEIR CARTAN SIGNATURES, AND THE REAL-RANK BOUND.  For an involution T of
    the E6 root datum that lifts to the Cartan involution of a real form, the T-odd part of the lattice
    Cartan is an abelian subspace of p, so  dim(odd) <= real rank.  Real ranks: E6(-78) 0, E6(-26) 2,
    E6(-14) 2, E6(2) 4, E6(6) 6; outer forms: E6(-26), E6(6).  Computed for the mirror Ad(h'), for
    quaternion conjugation (the inversion x -> xbar, which B1270 called theta), and for their ratio
    x -> h' xbar h'bar: fixed roots, two-orbits, fixed/odd ranks, the fixed root system, inner/outer.

(c) THE SO(10) x U(1) GRADINGS OF THE 27 AGAINST THE MIRROR: how many of the 27 D2-type involutions
    commute with the mirror (theta w0 = -w0 on E6).

(d) THE MIRROR'S REAL TYPE ON THE OBJECT'S OWN sl2 (exact over Q(omega)): the involutive amphichiral
    automorphisms alpha of pi_1(m004) with rho o alpha = J rhobar J^-1 (rho the Riley representation);
    J Jbar = +1 -> the mirror's real structure on sl(2,C) is sl(2,R) (reflection type, split);
    J Jbar = -1 -> su(2) (inversion type, compact).  The principal sl2 of e6 is real-split only in the
    quasi-split forms E6(6), E6(2).
"""
from __future__ import annotations
import os, sys, itertools, collections, random
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
for arc in ('B1267_spectrum_law_rebuilt', 'B1270_e6_from_the_two_faces'):
    sys.path.insert(0, os.path.join(HERE, '..', '..', arc, 'verification'))
import e6_from_the_two_faces as TF
import spectrum_law as S

REAL_RANK = {'E6(-78)': (0, 'inner'), 'E6(-26)': (2, 'outer'), 'E6(-14)': (2, 'inner'), 'E6(2)': (4, 'inner'), 'E6(6)': (6, 'outer')}
KOMPACT = {'E6(-78)': 'e6', 'E6(-26)': 'f4', 'E6(-14)': 'so(10)+u(1)', 'E6(2)': 'su(6)+su(2)', 'E6(6)': 'sp(8)'}


# ----------------------------------------------------------------------------------------- lattice tools
def real8(r):
    return [c.x for c in r] + [c.y for c in r]


def simple_roots(roots, seed=3):
    rng = random.Random(seed)
    while True:
        h = [rng.randint(-97, 97) for _ in range(8)]
        ht = lambda r: sum(hh * float(v) for hh, v in zip(h, real8(r)))
        if all(abs(ht(r)) > 1e-9 for r in roots):
            break
    pos = [r for r in roots if ht(r) > 0]
    posk = {TF.key(r) for r in pos}
    return [r for r in pos if not any(TF.key(tuple(a - b for a, b in zip(r, s))) in posk
                                      for s in pos if TF.key(s) != TF.key(r))]


def root_system_type(rts):
    if not rts:
        return "empty", [], 1, []
    simple = simple_roots(rts, seed=5)
    C = [[TF.bil(a, b) for b in simple] for a in simple]
    n = len(simple)
    degs = sorted(sum(1 for x in row if x == -1) for row in C)
    det = sp.Matrix([[sp.Rational(x) for x in row] for row in C]).det()
    comp, seen = [], set()
    for i in range(n):
        if i in seen:
            continue
        stack, cc = [i], []
        while stack:
            k = stack.pop()
            if k in seen:
                continue
            seen.add(k); cc.append(k)
            stack += [j for j in range(n) if C[k][j] == -1]
        comp.append(sorted(cc))
    sizes = sorted(len(c) for c in comp)
    name = {(1,): "A1", (1, 1): "A1+A1", (1, 1, 1): "3A1", (1, 1, 1, 1): "4A1", (2,): "A2", (3,): "A3", (4,): "D4" if degs == [1, 1, 1, 3] else "A4",
            (5,): "D5" if degs == [1, 1, 1, 2, 3] else "A5", (6,): "E6" if degs == [1, 1, 1, 2, 2, 3] else "?"}.get(tuple(sizes), str(sizes))
    return name, degs, det, comp


def unit_icosian_iso():
    """B1270's isomorphism SL(2,F5) -> 2I, rebuilt: images of R, L, g and of the mirror diag(3,2)."""
    units = TF.unit_icosians()
    one = (TF.Q5(1), TF.Q5(0), TF.Q5(0), TF.Q5(0))
    key, qmul = TF.key, TF.qmul

    def m5(M):
        return tuple(x % 5 for x in M)

    def mul5(A, B):
        p, q, r, s_ = A
        t, u, v, w_ = B
        return ((p*t + q*v) % 5, (p*u + q*w_) % 5, (r*t + s_*v) % 5, (r*u + s_*w_) % 5)
    I5, R5, L5 = (1, 0, 0, 1), (1, 1, 0, 1), (1, 0, 1, 1)
    Linv5 = (1, 0, 4, 1)
    g5 = m5(tuple(-x for x in mul5(R5, Linv5)))
    ord5 = [u for u in units if TF.orders_of(u, one, key) == 5]
    iso = None
    for r in ord5:
        for l in ord5:
            img = {I5: one}
            frontier = [I5]
            good = True
            while frontier and good:
                nxt = []
                for M in frontier:
                    for g, gi in ((R5, r), (L5, l)):
                        P = mul5(M, g)
                        Q = qmul(img[M], gi)
                        if P in img:
                            if key(img[P]) != key(Q):
                                good = False
                                break
                        else:
                            img[P] = Q
                            nxt.append(P)
                    if not good:
                        break
                frontier = nxt
            if good and len(img) == 120 and len({key(v) for v in img.values()}) == 120:
                iso = img
                break
        if iso:
            break
    assert iso is not None
    P5 = (3, 0, 0, 2)                                   # diag(3,2) in SL(2,F5): conjugation by it is the mirror R -> R^-1, L -> L^-1
    assert mul5(mul5(P5, R5), (2, 0, 0, 3)) == (1, 4, 0, 1) and mul5(mul5(P5, L5), (2, 0, 0, 3)) == (1, 0, 4, 1)
    return units, one, iso, dict(R=iso[R5], L=iso[L5], g=iso[g5], h=iso[P5]), (R5, L5, g5, P5, mul5)


def ad(h):
    hb = TF.qconj(h)
    return lambda x: TF.qmul(TF.qmul(h, x), hb)


class Lattice:
    def __init__(self):
        self.units, self.one, self.iso, self.im, self.f5 = unit_icosian_iso()
        self.roots = TF.e8_roots(self.units)
        self.rk = {TF.key(r) for r in self.roots}
        self.g = self.im['g']
        one, g = self.one, self.g
        self.e6 = [r for r in self.roots if TF.bil(r, one) == 0 and TF.bil(r, g) == 0]
        assert len(self.e6) == 72
        self.cls = {TF.key(r): (TF.bil(r, one), TF.bil(r, g)) for r in self.roots}
        counts = collections.Counter(self.cls.values())
        self.triplet = [c for c, n in counts.items() if n == 27]
        base = simple_roots(self.roots)
        assert len(base) == 8
        self.base = base
        self.Cb = sp.Matrix([[sp.Integer(TF.bil(a, b)) for b in base] for a in base])
        assert self.Cb.det() == 1
        self.Cinv = self.Cb.inv()
        self.e6span = sp.Matrix([list(self.coords(r)) for r in self.e6])
        assert self.e6span.rank() == 6

    def coords(self, r):
        v = self.Cinv * sp.Matrix([sp.Rational(TF.bil(r, b)) for b in self.base])
        return tuple(sp.Rational(x) for x in v)

    def matrix(self, f):
        return sp.Matrix([list(self.coords(f(b))) for b in self.base]).T

    def analyse(self, f, name):
        one, g = self.one, self.g
        assert all(TF.key(f(r)) in self.rk for r in self.roots), name + ": must permute the roots"
        e6k = {TF.key(r) for r in self.e6}
        assert all(TF.key(f(r)) in e6k for r in self.e6), name + ": must preserve E6"
        gimg = 'g^-1' if TF.key(f(g)) == TF.key(TF.qconj(g)) else ('g' if TF.key(f(g)) == TF.key(g) else 'other')
        fixed = [r for r in self.e6 if TF.key(f(r)) == TF.key(r)]
        orb2 = (72 - len(fixed)) // 2
        Tm = self.matrix(f)
        assert Tm * Tm == sp.eye(8), name + ": must be an involution"
        # restrict to the E6 span: ranks of (T -/+ 1) on the span
        E = self.e6span.T                                                    # 8 x 72
        odd = (Tm * E - E).rank()
        fix = (Tm * E + E).rank()
        assert odd + fix == 6
        swapped = all(self.cls[TF.key(f(r))] != self.cls[TF.key(r)] for r in self.roots if self.cls[TF.key(r)] in self.triplet)
        kept = all(self.cls[TF.key(f(r))] == self.cls[TF.key(r)] for r in self.roots if self.cls[TF.key(r)] in self.triplet)
        kind = 'outer' if swapped else ('inner' if kept else 'mixed')
        tname, degs, det, comp = root_system_type(fixed)
        allowed = [F_ for F_, (rr, io) in REAL_RANK.items() if io == kind and rr >= odd]
        print(f"  {name}:")
        print(f"    on g: {gimg};  on E6: {kind} (27 classes {'swapped with 27bar' if swapped else 'preserved'});  E6 roots fixed {len(fixed)} [{tname}: degrees {degs}, det {det}], two-orbits {orb2}")
        print(f"    Cartan signature on the E6 span: fixed {fix}, odd {odd}   ->  real rank >= {odd}:  allowed real forms {allowed}  (k = {[KOMPACT[a] for a in allowed]})")
        return dict(name=name, gimg=gimg, kind=kind, fixed=len(fixed), ftype=tname, orb2=orb2, fix=fix, odd=odd, allowed=allowed, f=f, T=Tm)


def part_ab(L):
    im = L.im
    R_q, L_q, g, h = im['R'], im['L'], im['g'], im['h']
    one = L.one
    key, qmul, qconj = TF.key, TF.qmul, TF.qconj
    assert TF.orders_of(h, one, key) == 4
    inv = lambda x: qconj(x)                                                  # units: x^-1 = xbar
    Ah = ad(h)
    assert key(Ah(R_q)) == key(inv(R_q)) and key(Ah(L_q)) == key(inv(L_q)), "Ad(h) must invert R and L"
    conj_of_ginv = key(Ah(g)) == key(inv(g))
    hp = qmul(L_q, h)
    assert key(qmul(hp, hp)) == key(tuple(-c for c in one))                  # h'^2 = -1
    Ahp = ad(hp)
    assert key(Ahp(g)) == key(inv(g)), "the representative h' = L h must send g to g^-1"
    assert key(Ahp(L_q)) == key(inv(L_q))
    print(f"  the mirror P = diag(1,-1) reduces mod 5 to diag(3,2) (det P = -1 = 2^2, a square): INNER on 2I, of order 4;")
    print(f"  its image h (order {TF.orders_of(h, one, key)}) inverts R_q and L_q: True;  Ad(h) g = g^-1: {conj_of_ginv} (it is a conjugate of g^-1);")
    print(f"  the representative h' = L_q h of the same mirror class has h'^2 = -1, sends g -> g^-1 and L -> L^-1: True")
    res = {}
    res['mirror'] = L.analyse(Ahp, "the mirror Ad(h') (the object's amphichirality on the golden face, preserving Z[g])")
    res['inversion'] = L.analyse(qconj, "quaternion conjugation x -> xbar (the inversion; B1270's 'theta')")
    res['ratio'] = L.analyse(lambda x: Ahp(qconj(x)), "their ratio x -> h' xbar h'bar")
    # the mirror's fixed roots on all of E8 (context)
    fixed8 = [r for r in L.roots if key(Ahp(r)) == key(r)]
    t8 = root_system_type(fixed8)
    print(f"  (context) roots of E8 fixed by the mirror: {len(fixed8)} [{t8[0]}]")
    ok = (res['mirror']['kind'] == 'outer' and res['mirror']['gimg'] == 'g^-1'
          and res['inversion']['kind'] == 'outer' and res['ratio']['kind'] == 'inner' and res['ratio']['gimg'] == 'g')
    return ok, res


def part_c(L, res):
    one, g = L.one, L.g
    GA2 = sp.Matrix([[sp.Integer(TF.bil(a, b)) for b in (one, g)] for a in (one, g)])
    GA2inv = GA2.inv()
    c_one, c_g = sp.Matrix(list(L.coords(one))), sp.Matrix(list(L.coords(g)))

    def e6_part(r):
        pr = GA2inv * sp.Matrix([sp.Integer(TF.bil(r, one)), sp.Integer(TF.bil(r, g))])
        return sp.Matrix(list(L.coords(r))) - pr[0] * c_one - pr[1] * c_g
    c0 = L.triplet[0]
    class_roots = [r for r in L.roots if L.cls[TF.key(r)] == c0]
    assert len(class_roots) == 27
    out = {}
    for nm in ('mirror', 'inversion', 'ratio'):
        Tm = res[nm]['T']
        n_anti = n_fix = 0
        for r0 in class_roots:
            p = e6_part(r0)
            img = Tm * p
            n_anti += (img == -p)
            n_fix += (img == p)
        out[nm] = (n_anti, n_fix)
        print(f"  {nm}: SO(10)xU(1) gradings D2(w0) of the 27 that commute with it: {n_anti + n_fix} of 27  (theta w0 = -w0: {n_anti}; theta w0 = +w0: {n_fix})")
        if nm == 'mirror':
            comp = [r0 for r0 in class_roots if Tm * e6_part(r0) == -e6_part(r0)]
            prs = collections.Counter(TF.bil(a, b) for a, b in itertools.combinations(comp, 2))
            sm = tuple(sum(c[i] for c in [tuple(e6_part(r0)) for r0 in comp]) for i in range(8))
            print(f"    the {len(comp)} mirror-compatible weights: mutual E8 pairings {dict(prs)}; sum of their E6 parts = {sm}  (zero <=> a zero-sum triple: one of the cubic's 45)")
    return True, out


def part_d():
    """Exact over Q(omega) with the corpus's Qw arithmetic (E.Qw): no symbolic blow-up."""
    import numpy as np
    import e6_instrument as E
    Qw, ONE, ZERO, OMEGA = E.Qw, E.ONE, E.ZERO, E.OMEGA
    u = complex(0.5, 3 ** 0.5 / 2)
    A = np.array([[1, 1], [0, 1]], dtype=complex)
    B = np.array([[1, 0], [u, 1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    mats = {1: A, -1: np.linalg.inv(A), 2: B, -2: np.linalg.inv(B)}

    def ev(word, m=mats):
        M = I2.copy()
        for Lt in word:
            M = M @ m[Lt]
        return M

    def reduced_words(maxlen):
        out = [()]
        for n in range(1, maxlen + 1):
            for wd in itertools.product((1, -1, 2, -2), repeat=n):
                if all(wd[i] != -wd[i + 1] for i in range(n - 1)):
                    out.append(wd)
        return out
    words = reduced_words(6)
    parab = [wd for wd in words if abs(np.trace(ev(wd)) - 2) < 1e-9]
    t_ab_bar = np.conj(np.trace(A @ B))
    hits = []
    for wa in parab:
        Ma = ev(wa)
        for wb in parab:
            Mb = ev(wb)
            if abs(np.trace(Ma @ Mb) - t_ab_bar) > 1e-9:
                continue
            sub = {1: Ma, -1: np.linalg.inv(Ma), 2: Mb, -2: np.linalg.inv(Mb)}
            if np.allclose(ev(S.REL, sub), I2, atol=1e-9):
                hits.append((wa, wb))
    # exact arithmetic over Q(omega): 2x2 matrices as tuples of Qw
    U = E.U_RILEY
    Ae = ((ONE, ONE), (ZERO, ONE)); Be = ((ONE, ZERO), (U, ONE))

    def mm(X, Y):
        return tuple(tuple(sum((X[i][k] * Y[k][j] for k in range(2)), ZERO) for j in range(2)) for i in range(2))

    def minv(X):                                    # det = 1 for all words in SL(2)
        (a, b), (c, d) = X
        return ((d, -b), (-c, a))

    def cw(z):                                      # omega -> omegabar = -1 - omega
        return Qw(z.x - z.y, -z.y)

    def mconj(X):
        return tuple(tuple(cw(z) for z in row) for row in X)
    me = {1: Ae, -1: minv(Ae), 2: Be, -2: minv(Be)}

    def eve(word, m=me):
        M = ((ONE, ZERO), (ZERO, ONE))
        for Lt in word:
            M = mm(M, m[Lt])
        return M
    ident = ((ONE, ZERO), (ZERO, ONE))
    om = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
    tosp = lambda z: sp.Rational(z.x) + sp.Rational(z.y) * om
    types = collections.Counter()
    shown = 0
    n_invol = 0
    n_inner = 0
    n_sym = 0
    # numeric evaluation for the D-check
    def evn(word):
        return ev(word)
    short = [wd for wd in words if len(wd) <= 6]
    rho_short = [(wd, evn(wd)) for wd in short]
    for wa, wb in hits:
        Ma, Mb = eve(wa), eve(wb)
        sub = {1: Ma, -1: minv(Ma), 2: Mb, -2: minv(Mb)}
        assert eve(S.REL, sub) == ident, "exact relator check"
        j = sp.symbols('j0:4')
        J = sp.Matrix(2, 2, j)
        Mas = sp.Matrix(2, 2, [tosp(z) for row in Ma for z in row])
        Mbs = sp.Matrix(2, 2, [tosp(z) for row in Mb for z in row])
        Abar = sp.Matrix(2, 2, [tosp(z) for row in mconj(Ae) for z in row])
        Bbar = sp.Matrix(2, 2, [tosp(z) for row in mconj(Be) for z in row])
        eqs = list(J * Abar - Mas * J) + list(J * Bbar - Mbs * J)
        sol = list(sp.linsolve([sp.expand(e) for e in eqs], j))[0]
        free = [s_ for s_ in j if any(s_ in sp.sympify(x).free_symbols for x in sol)]
        assert len(free) == 1, free
        Jm = sp.Matrix(2, 2, [sp.expand(x.subs(free[0], 1)) for x in sol])
        Jbar = Jm.applyfunc(lambda z: sp.expand(sp.conjugate(z)))
        JJ = (Jm * Jbar).applyfunc(sp.expand)
        if JJ[0, 1] == 0 and JJ[1, 0] == 0 and sp.expand(JJ[0, 0] - JJ[1, 1]) == 0:
            n_invol += 1
            lam = sp.nsimplify(JJ[0, 0])
            ty = 'sl(2,R) [reflection type, split]' if lam > 0 else 'su(2) [inversion type, compact]'
            types[ty] += 1
            if shown < 4:
                print(f"    involutive alpha: a -> {wa}, b -> {wb};  J Jbar = ({lam}) I  ->  {ty}")
                shown += 1
            continue
        # alpha^2 is conjugation by D = J Jbar: is D in the image (inner), or a symmetry outside it?
        Dn = np.array([[complex(sp.N(JJ[i, k], 30)) for k in range(2)] for i in range(2)])
        Dn = Dn / np.sqrt(np.linalg.det(Dn))
        inner = any(np.allclose(Dn, M, atol=1e-7) or np.allclose(Dn, -M, atol=1e-7) for wd, M in rho_short)
        if inner:
            n_inner += 1
        else:
            n_sym += 1
            if shown < 6:
                D2 = Dn @ Dn
                print(f"    alpha: a -> {wa}, b -> {wb};  alpha^2 = Ad(D) with D not in rho(pi_1) (words <= 6);  tr D = {np.trace(Dn):.6f}, D^2 = +-1: {np.allclose(D2, np.eye(2), atol=1e-7) or np.allclose(D2, -np.eye(2), atol=1e-7)}")
                shown += 1
    print(f"  words of length <= 6: {len(words)}; parabolic: {len(parab)}; endomorphisms with rho o alpha ~ rhobar: {len(hits)}")
    print(f"  of these: involutive (J Jbar scalar): {n_invol};  alpha^2 inner (D in rho(pi_1)): {n_inner};  alpha^2 = Ad(D) with D outside the image (the mirror's square is a symmetry, the mirror has order 4): {n_sym}")
    print(f"  real types of the involutive mirrors on the object's own sl(2,C): {dict(types) if types else 'none found -- no involutive mirror among words <= 6'}")
    return len(hits) > 0, (types, n_invol, n_inner, n_sym)


if __name__ == "__main__":
    ok = True
    print("=== (a)+(b) the mirror derived from P = diag(1,-1), and the three involutions on E6 with their Cartan signatures ===")
    L = Lattice()
    okab, res = part_ab(L)
    ok &= okab
    print("\n=== (c) the SO(10) x U(1) gradings of the 27 against each involution ===")
    okc, gr = part_c(L, res)
    ok &= okc
    print("\n=== (d) the mirror's real type on the object's own sl2 (Riley representation, exact over Q(omega)) ===")
    okd, types = part_d()
    ok &= okd
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
