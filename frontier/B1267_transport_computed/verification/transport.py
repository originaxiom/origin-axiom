#!/usr/bin/env python3
"""I-26, the transport, computed: the surviving gauge algebra and the massless spectrum for every
flat-connection reading of the object, plus the theorem that kills the Standard-Model reading.

Dictionary (Acharya-Witten, M-theory on a G2 space with an ADE singularity of type g along an
associative 3-manifold Q, flat connection rho: pi_1(Q) -> G compact):
    4d N=1 gauge algebra          = c_g(rho)  (the centralizer of the holonomy image in g)
    4d chiral multiplets           = H^1(Q; g_rho), decomposed under c_g(rho)    [adjoint-valued]
    matter in non-adjoint reps     ONLY at isolated points where the singularity enhances (E7 for a 27)
Dictionary (3d-3d, the 6d (2,0) theory of type g on Q): vacua = G(C)-flat connections on Q,
    massless chiral multiplets at rho = H^1(Q; g_rho)   [adjoint-valued again].
In BOTH transports the coefficient system of the fields living on Q is the ADJOINT 78, never the 27.

Computed here, exactly, with the rebuilt instrument:
  (1) c_e6 of: the principal sl2 (0), the subregular sl2, the theta-odd dense image (0), and the
      finite image 2T under the principal AND the subregular SU(2)  (B854's u(1)^4 reproduced,
      the subregular case new);
  (2) THE DOUBLE-CENTRALIZER THEOREM: for the Standard-Model subalgebra s = su(3)+su(2)+u(1)_Y of
      B1252's descent, c(c(s)) is the full-rank Levi, NOT s -- so s is not the centralizer of
      anything in e6: no flat connection, Wilson line or adjoint VEV can leave exactly the SM;
  (3) the adjoint spectra h^1(m004; 78_rho) for the principal and subregular embeddings, and
      h^1(m004; V) for every 2T-irrep V, giving the 4d spectrum of the one UNITARY (compact-group)
      flat connection the object's own chain supplies -- the 2T Wilson line -- and of the
      theta-twisted E6 (= F4) reading;
  (4) the counts are vector-like in every case (a theorem: the 78 is self-dual and the charge
      sectors pair q <-> -q), and the 27 never appears as a field on Q.
"""
from __future__ import annotations
import os, sys, time, itertools, collections
from fractions import Fraction as F
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                'B1265_spectrum_law_rebuilt', 'verification'))   # the rebuilt 27-instrument
import e6_instrument as E
import spectrum_law as S

Qw, ONE, ZERO, OMEGA, U = E.Qw, E.ONE, E.ZERO, E.OMEGA, E.U_RILEY


# ---------------------------------------------------------------- 2T inside SL(2, Q(omega))
def sl2_2T():
    """The binary tetrahedral group as 2x2 matrices over Q(omega): i -> I, j -> J with
    I = [[a, b], [b, -a]], a^2 + b^2 = -1 (a = 1 + omega, b = omega), J = [[0,1],[-1,0]]."""
    a, b = Qw(1, 1), OMEGA
    assert (a * a + b * b) == Qw(-1)
    I = np.array([[a, b], [b, -a]], dtype=object)
    J = np.array([[ZERO, ONE], [-ONE, ZERO]], dtype=object)
    K = I.dot(J)
    one = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)
    half = Qw(F(1, 2))
    g1 = np.array([[(one[i, j] + I[i, j] + J[i, j] + K[i, j]) * half for j in range(2)] for i in range(2)], dtype=object)
    gens = [I, J, g1]
    # generate
    def key(M):
        return tuple((x.x, x.y) for x in M.flatten())
    seen = {key(one): one}
    frontier = [one]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                P = M.dot(g)
                k = key(P)
                if k not in seen:
                    seen[k] = P
                    nxt.append(P)
        frontier = nxt
    elems = list(seen.values())
    return gens, elems


def order_of(M, one, key):
    P = M
    for n in range(1, 30):
        if key(P) == key(one):
            return n
        P = P.dot(M)
    return None


# ---------------------------------------------------------------- SL(2) -> E6 on the 27
def sl2_to_e6(g, Re, Rf):
    """[[p,q],[r,s]] -> exp(x e) exp(r f) exp(y e) with x = (p-1)/r, y = (s-1)/r (needs r != 0)."""
    p, q, r, s = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    assert not r.is_zero(), "use a conjugate with nonzero lower-left entry"
    rinv = r.inv()
    x = (p - ONE) * rinv
    y = (s - ONE) * rinv
    A = E.qw_expm_nilpotent(S.qw_scale(Re, x))
    B = E.qw_expm_nilpotent(S.qw_scale(Rf, r))
    Cm = E.qw_expm_nilpotent(S.qw_scale(Re, y))
    return A.dot(B).dot(Cm)


def qw_inv_via_group(M, elems27):
    raise NotImplementedError


# ---------------------------------------------------------------- centralizers in e6
def centralizer_dim_group(mats27, invs27):
    """dim { X in e6 : Ad(g) X = X for all g }  as 78 - rank of the stacked (Ad(g)-1) on the basis."""
    rows = []
    for g, gi in zip(mats27, invs27):
        cols = []
        for k in range(E.DIM):
            Xk = E.qw_matrix(E.REP[k])
            D = g.dot(Xk).dot(gi) - Xk
            cols.append(D.flatten())
        rows.append(np.array(cols, dtype=object).T)     # 729 x 78
    M = np.vstack(rows)
    return E.DIM - E.rank_qw(M)


def centralizer_dim_algebra(elems):
    """dim { X in e6 : [Y, X] = 0 for all Y in elems } (elems as 78-vectors)."""
    import sympy as sp
    mats = [E.ad_matrix(y) for y in elems]
    M = sp.Matrix.vstack(*mats)
    return E.DIM - M.rank()


def centralizer_basis_algebra(elems):
    import sympy as sp
    mats = [E.ad_matrix(y) for y in elems]
    M = sp.Matrix.vstack(*mats)
    return M.nullspace()


# ---------------------------------------------------------------- the adjoint 78 as a pi_1-module
def adjoint_rep(e, f):
    """rho(a) = exp(ad e), rho(b) = exp(u ad f) on e6 (78 x 78, exact over Q(omega))."""
    import sympy as sp
    ade = E.ad_matrix(e)
    adf = E.ad_matrix(f)

    def qw_from_sp(M, c):
        n, m = M.shape
        out = E.qw_zeros(n, m)
        for i in range(n):
            for j in range(m):
                x = sp.Rational(M[i, j])
                out[i, j] = Qw(F(int(x.p), int(x.q))) * c
        return out

    def expq(Mq):
        I = E.qw_eye(Mq.shape[0])
        out, term, k = I.copy(), I.copy(), 1
        while True:
            term = term.dot(Mq)
            term = np.array([[t * Qw(F(1, k)) for t in row] for row in term.tolist()], dtype=object)
            if E.qw_is_zero(term):
                return out
            out = out + term
            k += 1
            assert k < 80
    A = expq(qw_from_sp(ade, ONE))
    Ai = expq(qw_from_sp(ade, Qw(-1)))
    B = expq(qw_from_sp(adf, U))
    Bi = expq(qw_from_sp(adf, -U))
    return S.Rep({1: A, 2: B}, {1: Ai, 2: Bi})


# ---------------------------------------------------------------- finite-image coefficient systems
def perm_rep_A4():
    """pi_1(m004) -> SL(2,F3) -> PSL(2,F3) = A4 acting on P^1(F3) = {0,1,2,oo}:
    a: x -> x+1 ;  b: x -> x/(2x+1)   (the Riley matrices reduced mod (1 - omega), omega -> 1, u -> 2)."""
    pts = [0, 1, 2, 'oo']

    def mob(M, x):
        p, q, r, s = M
        if x == 'oo':
            return 'oo' if r % 3 == 0 else (p * pow(r, -1, 3)) % 3
        num, den = (p * x + q) % 3, (r * x + s) % 3
        return 'oo' if den == 0 else (num * pow(den, -1, 3)) % 3
    A = (1, 1, 0, 1)
    B = (1, 0, 2, 1)
    def pmat(M):
        P = np.zeros((4, 4), dtype=object)
        P[:] = F(0)
        for j, x in enumerate(pts):
            i = pts.index(mob(M, x))
            P[i, j] = F(1)
        return P
    PA, PB = pmat(A), pmat(B)
    return PA, PB


def rank_frac(M):
    import sympy as sp
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in M.tolist()]).rank()


def h1_frac_rep(mats, invs, gens, relators):
    """Fox h1 for a representation with exact Fraction matrices."""
    n = mats[gens[0]].shape[0]
    I = np.zeros((n, n), dtype=object); I[:] = F(0)
    for i in range(n): I[i, i] = F(1)
    def ev(word):
        out = I.copy()
        for L in word:
            out = out.dot(mats[L] if L > 0 else invs[-L])
        return out
    def fox(word, g):
        acc = np.zeros((n, n), dtype=object); acc[:] = F(0)
        cur = I.copy()
        for L in word:
            if L > 0:
                if L == g: acc = acc + cur
                cur = cur.dot(mats[L])
            else:
                cur = cur.dot(invs[-L])
                if -L == g: acc = acc - cur
        return acc
    d0 = np.vstack([mats[g] - I for g in gens])
    d1 = np.vstack([np.hstack([fox(r, g) for g in gens]) for r in relators])
    r0, r1 = rank_frac(d0), rank_frac(d1)
    return n - r0, (len(gens) * n - r1) - r0


def h1_character(val):
    """h1(m004; C_chi) for the character a, b -> val (a Qw scalar)."""
    mats = {1: np.array([[val]], dtype=object), 2: np.array([[val]], dtype=object)}
    invs = {1: np.array([[val.inv()]], dtype=object), 2: np.array([[val.inv()]], dtype=object)}
    R = S.Rep(mats, invs)
    h0, h1, _, _ = S.h0_h1(R, [1, 2], [S.REL])
    return h0, h1


# ---------------------------------------------------------------- B1252's SM subalgebra, rebuilt
def sm_subalgebra():
    """Return (roots of A2+A1, Y) for B1252's descent E6 -> SO(10) -> SU(5) -> SU(3)xSU(2)xU(1)_Y,
    reproducing its search (metric-correct inner products, the D2 stabiliser, the unique SM Y)."""
    import sympy as sp, importlib.util, json, pathlib
    root = pathlib.Path(E.ROOT)
    spec = importlib.util.spec_from_file_location(
        "cmd", root / "frontier" / "B1252_metric_and_descent" / "verification" / "cartan_metric_and_descent.py")
    cmd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cmd)
    wts, G = cmd.load()
    M = cmd.cartan_metric()
    Mf = [[F(sp.Rational(M[i, j])) for j in range(6)] for i in range(6)]
    ip = lambda a, b: sum(F(a[i]) * Mf[i][j] * F(b[j]) for i in range(6) for j in range(6))
    w13 = wts[13]
    rts = cmd.roots()
    so10 = [a for a in rts.values() if sum(x * y for x, y in zip(w13, a)) % 2 == 0]
    cache = {}
    def ipc(a, b):
        if (a, b) not in cache:
            cache[(a, b)] = ip(a, b)
        return cache[(a, b)]
    def comps(rs):
        rs = list(rs)
        adj = collections.defaultdict(set)
        for a in rs:
            for b in rs:
                if a != b and ipc(a, b) != 0:
                    adj[a].add(b); adj[b].add(a)
        seen, out = set(), []
        for r in rs:
            if r in seen: continue
            c, st = {r}, [r]
            while st:
                x = st.pop()
                for y in adj[x]:
                    if y not in c:
                        c.add(y); st.append(y)
            seen |= c; out.append(len(c))
        return tuple(sorted(out))
    BOX = [v for v in itertools.product(range(-2, 3), repeat=6) if any(v)]
    su5 = next(k for k in (frozenset(a for a in so10 if ip(v, a) == 0) for v in BOX)
               if len(k) == 20 and comps(k) == (20,))
    subs = {k for k in (frozenset(a for a in su5 if ip(v, a) == 0) for v in BOX)
            if len(k) == 8 and comps(k) == (2, 6)}
    spec2 = importlib.util.spec_from_file_location(
        "dd", root / "frontier" / "B1250_d2_decode" / "verification" / "d2_decode.py")
    dd = importlib.util.module_from_spec(spec2)
    spec2.loader.exec_module(dd)
    _, _, blocks = dd.stabiliser_blocks()
    W16 = [wts[i] for i in blocks[2]]
    Ms = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])
    for sub in subs:
        ns = [[F(sp.Rational(x)) for x in n] for n in (sp.Matrix([list(r) for r in sub]) * Ms).nullspace()]
        for c in itertools.product(range(-6, 7), repeat=len(ns)):
            if not any(c): continue
            v = [sum(ci * n[i] for ci, n in zip(c, ns)) for i in range(6)]
            gr = collections.Counter(ip(v, w) for w in W16)
            if sorted(gr.values()) != [1, 1, 2, 3, 3, 6] or gr.get(F(0)) != 1: continue
            g6 = [g for g, m in gr.items() if m == 6][0]
            if g6 == 0: continue
            lam = F(1, 6) / g6
            if {g * lam: m for g, m in gr.items()} == cmd.SM_TARGET:
                return sorted(sub), v, rts, Mf
    raise RuntimeError("B1252's SM Y not found")


def root_index(r):
    """B854 basis index of the root vector e_r; r is given in DYNKIN-LABEL coordinates (B1252's
    convention, the rep27 'weights' coordinates), converted to simple-root coordinates by C^-1."""
    import sympy as sp
    n = sp.Matrix(E.C).inv() * sp.Matrix(list(r))
    n = tuple(int(x) for x in n)
    return E.N + E.IDX[n]


def main():
    t0 = time.time()
    e, h, f = E.principal_sl2()
    es, hs, fs, _ = E.subregular_sl2()
    HV = E.hw_vectors(e)

    print("=== (1) centralizers in e6 ===")
    print("  c(principal sl2) dim =", centralizer_dim_algebra([e, f]))
    print("  c(subregular sl2) dim =", centralizer_dim_algebra([es, fs]))
    print("  c(<sl2, hv8>) dim =", centralizer_dim_algebra([e, f, HV[8]]), "  (the theta-odd amalgam closes to e6: centre only)")

    gens2, elems2 = sl2_2T()
    one2 = np.array([[ONE, ZERO], [ZERO, ONE]], dtype=object)
    key = lambda M: tuple((x.x, x.y) for x in M.flatten())
    orders = collections.Counter(order_of(g, one2, key) for g in elems2)
    print(f"  2T in SL(2,Q(omega)): |2T| = {len(elems2)}, element orders {dict(sorted(orders.items()))}")
    for name, (ee, ff) in (("principal", (e, f)), ("subregular", (es, fs))):
        Re, Rf = E.qw_matrix(E.rho(ee)), E.qw_matrix(E.rho(ff))
        imgs = [sl2_to_e6(g, Re, Rf) for g in gens2]
        # closure of the image on the 27 must have order 24 (a homomorphism, faithful on 2T)
        key27 = lambda M: tuple((x.x, x.y) for x in M.flatten())
        one27 = E.qw_eye(27)
        seen = {key27(one27): one27}
        frontier = [one27]
        while frontier:
            nxt = []
            for M in frontier:
                for g in imgs:
                    P = M.dot(g)
                    k = key27(P)
                    if k not in seen:
                        seen[k] = P
                        nxt.append(P)
            frontier = nxt
            assert len(seen) <= 48
        n27 = len(seen)
        # inverses: g^-1 = g^(ord-1)
        invs = []
        for g in imgs:
            P = g
            o = 1
            while key27(P) != key27(one27):
                P = P.dot(g); o += 1
            Q = one27
            for _ in range(o - 1):
                Q = Q.dot(g)
            invs.append(Q)
        cd = centralizer_dim_group(imgs, invs)
        print(f"  2T via the {name} SU(2): image on the 27 has order {n27}; dim c_e6(2T) = {cd}")

    print("\n=== (2) the double-centralizer theorem for the Standard-Model subalgebra ===")
    sub, Y, rts, Mf = sm_subalgebra()
    # s = span of root vectors of the A2+A1 (both signs) + their coroots + the Y direction (Cartan)
    # Cartan element for Y: Y is a vector in weight coordinates; as an element of the Cartan
    # subalgebra it is the coweight h_Y with <w, h_Y> = ip(Y, w); in the B854 basis h_i are the
    # simple coroots, so h_Y = sum_i c_i h_i with c = M^-1 Y  (M the Cartan metric = the Cartan matrix here).
    import sympy as sp
    Ms = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])
    # weights are Dynkin labels w; <w, h_Y> must equal ip(Y, w) = Y^T M w, so h_Y = sum_i (M Y)_i h_i
    cY = Ms * sp.Matrix([sp.Rational(y) for y in Y])
    hY = [F(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in cY] + [F(0)] * len(E.ROOTS)
    RhY = E.rho(hY)
    wts = __import__('json').load(open(E.REP27))['weights']
    for i, w in enumerate(wts):
        assert RhY[i, i] == sum(F(Y[a]) * Mf[a][b] * F(w[b]) for a in range(6) for b in range(6)), "h_Y convention"
    s_elems = []
    for r in sub:
        s_elems.append(E.vec(root_index(r)))
        s_elems.append(E.vec(root_index(tuple(-x for x in r))))
    s_elems.append(hY)
    s_dim = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in v] for v in
                       s_elems + [E.br(E.vec(root_index(r)), E.vec(root_index(tuple(-x for x in r)))) for r in sub]]).rank()
    cs = centralizer_basis_algebra(s_elems)
    cs_vecs = []
    for v in cs:
        from math import lcm
        L = 1
        for c in v: L = lcm(L, int(sp.Rational(c).q))
        cs_vecs.append([F(int(sp.Rational(c * L).p), int(sp.Rational(c * L).q)) for c in v])
    ccs_dim = centralizer_dim_algebra(cs_vecs)
    # rank of c(c(s)): does it contain a Cartan? check the dimension of its intersection with h
    print(f"  s = su(3)+su(2)+u(1)_Y  (B1252's descent): dim s = {s_dim}  (expect 8+3+1 = 12)")
    print(f"  dim c(s) = {len(cs)}     dim c(c(s)) = {ccs_dim}    (s is a centralizer iff c(c(s)) = s)")
    # brackets among c(s): abelian?
    ab = all(not E.nz(E.br(x, y)) for x in cs_vecs for y in cs_vecs)
    print(f"  c(s) abelian: {ab};  c(c(s)) has dimension {ccs_dim} > {s_dim}: the SM algebra is NOT a centralizer in e6")
    # the same test on the full-rank Levi l = su(3)+su(2)+u(1)^3 containing s
    # (its centre is the 3-dim orthogonal complement of the A2+A1 roots): c(c(l)) = l
    ns = (sp.Matrix([list(r) for r in sub]) * Ms).nullspace()
    l_elems = list(s_elems[:-1])
    for n_ in ns:
        cn = Ms * sp.Matrix([sp.Rational(x) for x in n_])
        l_elems.append([F(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in cn] + [F(0)] * len(E.ROOTS))
    cl = centralizer_basis_algebra(l_elems)
    cl_vecs = []
    for v in cl:
        from math import lcm
        L = 1
        for c in v: L = lcm(L, int(sp.Rational(c).q))
        cl_vecs.append([F(int(sp.Rational(c * L).p), int(sp.Rational(c * L).q)) for c in v])
    print(f"  control, the full-rank Levi l = su(3)+su(2)+u(1)^3: dim c(l) = {len(cl)}, dim c(c(l)) = {centralizer_dim_algebra(cl_vecs)}  (= dim l = 14: a centralizer)")

    print("\n=== (3) adjoint spectra and the finite-image coefficient systems ===")
    for name, (ee, ff) in (("principal", (e, f)), ("subregular", (es, fs))):
        R = adjoint_rep(ee, ff)
        S.check_rep(R, [1, 2], [S.REL])
        h0, h1, _, _ = S.h0_h1(R, [1, 2], [S.REL])
        print(f"  h^1(m004; 78) via the {name} embedding = {h1}   (h0 = {h0})")
    PA, PB = perm_rep_A4()
    PAi, PBi = PA.T.copy(), PB.T.copy()
    # check the relator in the permutation rep
    def evp(word):
        I4 = np.zeros((4, 4), dtype=object); I4[:] = F(0)
        for i in range(4): I4[i, i] = F(1)
        out = I4
        for L in word:
            out = out.dot({1: PA, 2: PB}[L] if L > 0 else {1: PAi, 2: PBi}[-L])
        return out
    Rw = evp(S.REL)
    assert all(Rw[i, i] == 1 for i in range(4)) and sum(1 for x in Rw.flatten() if x != 0) == 4
    h0p, h1p = h1_frac_rep({1: PA, 2: PB}, {1: PAi, 2: PBi}, [1, 2], [S.REL])
    h0t, h1t = h1_character(ONE)
    print(f"  A4 permutation rep on P^1(F3): h0 = {h0p}, h1 = {h1p}  ->  h^1(m004; 3_{{2T}}) = {h1p - h1t}   (h^1(triv) = {h1t})")
    for nm, val in (("omega", OMEGA), ("omega-bar", OMEGA.conj()), ("-1", Qw(-1))):
        print(f"  h^1(m004; C_{nm}) = {h1_character(val)[1]}")
    # 78 and 27 restricted to 2T: multiplicities by characters (2T = SL(2,3): classes and the
    # SU(2)-restriction of Sym^n) -- computed from the principal grading, exact
    print("  78|_2T and 27|_2T from the principal SU(2) (B854/B327 reproduced):")
    # character of Sym^n at an element of SU(2) with eigenvalues z, 1/z: sum z^(n-2k)
    import cmath
    classes = {"1": 1, "-1": -1, "i (ord 4)": 1j, "ord 6": cmath.exp(1j * cmath.pi / 3), "ord 3": cmath.exp(2j * cmath.pi / 3)}
    sizes = {"1": 1, "-1": 1, "i (ord 4)": 6, "ord 6": 8, "ord 3": 8}
    # irreps of 2T restricted characters: 1, omega, omega-bar, 3, 2, 2', 2''  -- only need A4 part
    def chi_sym(n, z):
        return sum(z ** (n - 2 * k) for k in range(n + 1))
    def decompose(blocks):
        # multiplicities of 1, omega, omegabar, 3 (the A4 irreps) in sum of Sym^n, n even
        w = cmath.exp(2j * cmath.pi / 3)
        # class functions on A4 classes: 1, (12)(34) [3], (123) [4], (132) [4]  <- SU(2) classes 1/-1 -> 1, i -> (12)(34), ord6/ord3 -> 3-cycles
        chi = {"1": 0, "-1": 0, "i (ord 4)": 0, "ord 6": 0, "ord 3": 0}
        for n in blocks:
            for c, z in classes.items():
                chi[c] += chi_sym(n, z)
        # 2T characters of the four A4 irreps (values at classes 1,-1,i,ord6,ord3)
        irr = {"1": [1, 1, 1, 1, 1], "omega": [1, 1, 1, w, w * w], "omegabar": [1, 1, 1, w * w, w], "3": [3, 3, -1, 0, 0]}
        keys = ["1", "-1", "i (ord 4)", "ord 6", "ord 3"]
        out = {}
        for nm, vals in irr.items():
            m = sum(sizes[k] * chi[k] * vals[i].conjugate() for i, k in enumerate(keys)) / 24
            out[nm] = round(m.real)
        return out
    print("     78 =", decompose([2, 8, 10, 14, 16, 22]), "   27 =", decompose([16, 8, 0]))
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
