#!/usr/bin/env python3
"""THE SIX-FOLD CLOSING'S WILSON LINES -- does B1277's theorem survive on the first hyperbolic closing that carries the
three characters?  (The three faces at once: Y_6 is hyperbolic (the geometric face: volume != 0, an exponential
sector), 3 | 6 so the family holonomy descends with the Klein image and the three sign characters (the arithmetic
face), and its torsion joins the two ends: |H_1(Y_6)| = |Delta(-1)| |Delta(omega)|^2 |Delta(-omega)|^2 = 5 . 16 . 4 = 320,
the golden determinant 5 and the Eisenstein 16 in one group.)

For n in {3, 6} (n = 3 is the control that must reproduce B1277):
(a) pi_1(Y_n) by Reidemeister-Schreier (B1274), H_1 by Smith normal form with transforms, Fox's formula
    |H_1(Y_n)| = prod_{zeta^n = 1, zeta != 1} |Delta(zeta)| as a check, Delta = t^2 - 3t + 1.
(b) ALL characters psi of H_1(Y_n) (as exponent vectors on the presentation's generators) and h^1(Y_n; psi) by Fox
    calculus: a numeric sweep (mpmath, 40 digits, singular-value gaps reported) and an EXACT confirmation over the
    cyclotomic field Q(zeta_m) (Gaussian elimination modulo Phi_m) of every character with h^1 > 0 and of controls.
(c) the three family characters chi_i: the descended 3_rho (B1273/B1274; the Klein four-group image) split into its
    three sign characters, located inside the character group; h^1(chi_i) = 1 each.
(d) the three-generation alphabet K3 = {psi : sum_i h^1(chi_i psi) >= 3}.  A flat E6 connection W commuting with
    the SM acts on the weight w of the 27 by the character psi_w = <lambda, w>, and the multiplicity of the component
    c of the three 27s is sum_i h^1(chi_i psi_c).  Three generations of Q, u^c, e^c require psi_Q, psi_u, psi_e in K3.
    If K3 = {1}: W is trivial on the 10 of SU(5), so (B1277) it commutes with SU(5) and the theorem stands on Y_n.
    Otherwise (e): enumerate every SM-commuting W (Hom(P/Q_SM, H_1^) exactly, through the Smith form of the SM-root
    lattice), its spectrum, whether it breaks SU(5), and whether three generations of Q, u^c, d^c, L, e^c survive.
"""
from __future__ import annotations
import os, sys, math, itertools, collections, pathlib
from fractions import Fraction as F
import numpy as np
import sympy as sp
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for arc in ('B1267_spectrum_law_rebuilt', 'B1268_cusped_net_chirality_bound', 'B1269_transport_computed',
            'B1273_the_three_fold_closing', 'B1274_the_tower_and_its_doubles', 'B1275_the_cubic_made_explicit',
            'B1276_the_relations_the_chain_forces', 'B1277_the_vacuum_manifold_of_the_closing'):
    sys.path.insert(0, str(ROOT / 'frontier' / arc / 'verification'))
import e6_instrument as E
import spectrum_law as S
import three_fold_closing as Y3
import tower_and_doubles as TW
import cubic_explicit as C
import relations as R
import vacuum_manifold as VM

mp.mp.dps = 40


# ------------------------------------------------------------------------------------------------ (a) H_1 by Smith
def relation_matrix(gens, rels):
    M = sp.zeros(len(rels), len(gens))
    for i, r in enumerate(rels):
        for L in r:
            M[i, abs(L) - 1] += (1 if L > 0 else -1)
    return M


def smith_with_transforms(M):
    """U M V = D (sympy 1.14's smith_normal_decomp; the convention is asserted)."""
    from sympy.matrices.normalforms import smith_normal_decomp
    D, U, V = smith_normal_decomp(M, domain=sp.ZZ)
    D, U, V = sp.Matrix(D), sp.Matrix(U), sp.Matrix(V)
    assert U * M * V == D, "Smith convention"
    assert abs(U.det()) == 1 and abs(V.det()) == 1
    return D, U, V


def alexander_order(n):
    t = sp.symbols('t')
    Delta = t ** 2 - 3 * t + 1
    prod = 1
    for k in range(1, n):
        z = sp.exp(2 * sp.pi * sp.I * k / n)
        prod *= Delta.subs(t, z)
    return int(round(abs(complex(sp.N(prod, 30)))))


def characters(D, V, m, with_coords=False):
    """All a in (Z/m)^g with R a = 0 mod m, from D c = 0, a = V c.  Returns a list of tuples (and, optionally, the
    group coordinates: c restricted to the non-trivial cyclic factors, with their moduli -- the character group as
    (+) Z/d_j, addition coordinatewise)."""
    g = V.shape[0]
    ranges, coord_axes, moduli = [], [], []
    for j in range(g):
        d = int(D[j, j]) if j < D.shape[0] and j < D.shape[1] else 0
        gcd = math.gcd(d, m) if d != 0 else m
        step = m // gcd
        ranges.append([step * i for i in range(gcd)])
        if gcd > 1:
            coord_axes.append(j); moduli.append(gcd)
    out, coords = [], []
    Vi = [[int(V[i, j]) for j in range(g)] for i in range(g)]
    for c in itertools.product(*ranges):
        a = tuple(sum(Vi[i][j] * c[j] for j in range(g)) % m for i in range(g))
        out.append(a)
        coords.append(tuple((c[j] // (m // moduli[k])) % moduli[k] for k, j in enumerate(coord_axes)))
    if with_coords:
        return out, coords, moduli
    return out


# ------------------------------------------------------------------------------------------------ (b) h^1 by Fox
def fox_scalar(word, g, psi, psi_inv):
    acc, cur = 0, 1
    for L in word:
        if L > 0:
            if L == g:
                acc = acc + cur
            cur = cur * psi[L]
        else:
            cur = cur * psi_inv[-L]
            if -L == g:
                acc = acc - cur
    return acc


def h1_numeric(gens, rels, a, m):
    zeta = mp.exp(2 * mp.pi * 1j / m)
    psi = {g: zeta ** a[g - 1] for g in gens}
    psi_inv = {g: zeta ** ((m - a[g - 1]) % m) for g in gens}
    d1 = mp.matrix([[fox_scalar(r, g, psi, psi_inv) for g in gens] for r in rels])
    sv = mp.svd_c(d1, compute_uv=False)
    sv = sorted([abs(x) for x in sv], reverse=True)
    tol = mp.mpf('1e-25')
    r1 = sum(1 for x in sv if x > tol)
    gap_hi = max([x for x in sv if x <= tol], default=mp.mpf(0))
    gap_lo = min([x for x in sv if x > tol], default=mp.mpf(1))
    r0 = 0 if all(x == 0 for x in a) else 1
    return (len(gens) - r1) - r0, 1 - r0, float(gap_lo), float(gap_hi)


class Cyc:
    """Elements of Q(zeta_m) as polynomials modulo Phi_m, exact."""
    x = sp.symbols('x')

    def __init__(self, poly, Phi):
        self.Phi = Phi
        self.p = sp.rem(sp.Poly(poly, Cyc.x, domain='QQ'), Phi)

    def __add__(self, o):
        return Cyc(self.p + o.p, self.Phi)

    def __sub__(self, o):
        return Cyc(self.p - o.p, self.Phi)

    def __mul__(self, o):
        return Cyc(self.p * o.p, self.Phi)

    def is_zero(self):
        return self.p.is_zero

    def inv(self):
        return Cyc(sp.invert(self.p, self.Phi), self.Phi)


def rank_cyc(rows):
    A = [list(r) for r in rows]
    n, mcols = len(A), len(A[0])
    r = 0
    for c in range(mcols):
        piv = next((i for i in range(r, n) if not A[i][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(n):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
        if r == n:
            break
    return r


def h1_exact(gens, rels, a, m):
    Phi = sp.Poly(sp.cyclotomic_poly(m, Cyc.x), Cyc.x, domain='QQ')
    z = lambda k: Cyc(Cyc.x ** (k % m), Phi)
    psi = {g: z(a[g - 1]) for g in gens}
    psi_inv = {g: z(m - a[g - 1]) for g in gens}
    one, zero = z(0), Cyc(0, Phi)

    def fox(word, g):
        acc, cur = zero, one
        for L in word:
            if L > 0:
                if L == g:
                    acc = acc + cur
                cur = cur * psi[L]
            else:
                cur = cur * psi_inv[-L]
                if -L == g:
                    acc = acc - cur
        return acc
    d1 = [[fox(r, g) for g in gens] for r in rels]
    r1 = rank_cyc(d1)
    r0 = 0 if all(x == 0 for x in a) else 1
    return (len(gens) - r1) - r0


# ------------------------------------------------------------------------------------------------ (c) the family characters
def family_characters(n, gens, m):
    surj, order_of, one = Y3.surjections_2T()
    found = set()
    for (X, Y) in surj:
        rep = TW.rep_on_cover(X, Y, n, Y3.ad3)
        # the image: {1, A, B, AB}; label the generators' images
        keys = {}
        one3 = E.qw_eye(3)
        elems = {Y3.key(one3): one3}
        frontier = [one3]
        while frontier:
            nxt = []
            for Mm in frontier:
                for g in gens:
                    P = Mm.dot(rep.M[g])
                    k = Y3.key(P)
                    if k not in elems:
                        elems[k] = P; nxt.append(P)
            frontier = nxt
        assert len(elems) == 4, len(elems)
        nontriv = [k for k in elems if k != Y3.key(one3)]
        A, B = nontriv[0], nontriv[1]
        # the three sign characters of V4: values on the generator images
        def sign_char(k, cA, cB):
            if k == Y3.key(one3):
                return 1
            if k == A:
                return cA
            if k == B:
                return cB
            return cA * cB
        chis = []
        for cA, cB in ((1, -1), (-1, 1), (-1, -1)):
            a = tuple(0 if sign_char(Y3.key(rep.M[g]), cA, cB) == 1 else m // 2 for g in gens)
            chis.append(a)
        found.add(frozenset(chis))
    assert len(found) == 1, f"the character triple depends on the surjection: {len(found)} triples"
    return sorted(next(iter(found)))


# ------------------------------------------------------------------------------------------------ (e) the Wilson lines
def wilson_search(n, gens, m, chars, h1, chis, wts, lab, sm_roots, enumerate_w=True):
    N = len(chars)
    idx = {a: i for i, a in enumerate(chars)}
    zero = tuple([0] * len(gens))
    add = lambda x, y: tuple((p + q) % m for p, q in zip(x, y))
    mult = lambda x, k: tuple((k * p) % m for p in x)
    h1v = np.array([h1[a] for a in chars], dtype=np.int64)
    chi_idx = [idx[c] for c in chis]
    # gen_count(psi) = sum_i h^1(chi_i psi)
    ADD = None
    G = np.zeros(N, dtype=np.int64)
    for i, a in enumerate(chars):
        G[i] = sum(h1[add(c, a)] for c in chis)
    K3 = [chars[i] for i in range(N) if G[i] >= 3]
    K2 = [chars[i] for i in range(N) if G[i] == 2]
    K1 = [chars[i] for i in range(N) if G[i] == 1]
    print(f"  generation counts sum_i h^1(chi_i psi) over the {N} characters: {dict(sorted(collections.Counter(G.tolist()).items()))}; "
          f"three-generation alphabet K3: {len(K3)} {'(only the trivial character)' if K3 == [zero] else ''}; two-generation alphabet K2: {len(K2)}")
    if not enumerate_w:
        return K3, K2, None
    # tables
    ADD = np.zeros((N, N), dtype=np.int32)
    for i, a in enumerate(chars):
        for j, b in enumerate(chars):
            ADD[i, j] = idx[add(a, b)]
    SCAL = np.zeros((m, N), dtype=np.int32)
    for k in range(m):
        for i, a in enumerate(chars):
            SCAL[k, i] = idx[mult(a, k)]
    # P/Q_SM through the Smith form of the SM-root lattice
    Rm = sp.Matrix([list(a) for a in sm_roots])
    D, U, V = smith_with_transforms(Rm)
    dprime = [int(D[j, j]) for j in range(min(D.shape))]
    rank = sum(1 for d in dprime if d != 0)
    VT = V.T
    coeff = {i: [int(x) % m for x in (VT * sp.Matrix(list(wts[i])))] for i in range(27)}
    tors = [[idx[a] for a in chars if mult(a, d) == zero] for d in dprime[:rank]]
    print(f"  SM-root lattice in P: invariant factors {dprime[:rank]} (rank {rank}); W <-> nu in (H_1^)^6 with d'_j nu_j = 0 for j <= {rank}: "
          f"{[len(t) for t in tors]} torsion choices x {N}^{6 - rank} free")
    comp = {l: next(i for i in range(27) if lab[i] == l) for l in ('Q', 'u^c', 'd^c', 'L', 'e^c')}
    ar = np.arange(N, dtype=np.int32)
    zero_i = idx[zero]

    def psi_w(i, nu_fixed, free_axis):
        acc = np.full(N, zero_i, dtype=np.int32) if free_axis is not None else zero_i
        for j in range(6):
            c = coeff[i][j]
            if c == 0:
                continue
            if j == free_axis:
                acc = ADD[acc, SCAL[c, ar]]
            else:
                acc = ADD[acc, SCAL[c, nu_fixed[j]]]
        return acc
    free_axes = list(range(rank, 6))
    assert len(free_axes) == 3
    total = 0
    full3 = 0
    best = -1
    best_count = 0
    examples = []
    su5_kept_full = 0
    for tor in itertools.product(*tors):
        for n4 in range(N):
            for n5 in range(N):
                nu = list(tor) + [n4, n5, None]
                total += N
                pq = psi_w(comp['Q'], nu, 5); pu = psi_w(comp['u^c'], nu, 5); pe = psi_w(comp['e^c'], nu, 5)
                pd = psi_w(comp['d^c'], nu, 5); pl = psi_w(comp['L'], nu, 5)
                gmin = np.minimum.reduce([G[pq], G[pu], G[pe], G[pd], G[pl]])
                broken = ~((pq == pu) & (pu == pe))
                full3 += int(np.sum((gmin >= 3) & broken))
                su5_kept_full += int(np.sum((gmin >= 3) & ~broken))
                bm = gmin[broken]
                if bm.size:
                    mx = int(bm.max())
                    if mx > best:
                        best, best_count, examples = mx, 0, []
                    if mx == best:
                        sel = np.where(broken & (gmin == mx))[0]
                        best_count += int(sel.size)
                        for n6 in sel[:2]:
                            if len(examples) < 6:
                                examples.append(list(tor) + [n4, n5, int(n6)])
    print(f"  SM-commuting Wilson lines enumerated: {total}; SU(5)-breaking with three generations of Q, u^c, d^c, L, e^c: {full3}; "
          f"SU(5)-preserving with three generations of all five: {su5_kept_full}")
    print(f"  the best SU(5)-breaking Wilson lines keep min(generations of Q, u^c, d^c, L, e^c) = {best}, achieved by {best_count} of them; examples (spectrum by label, summed over the three 27s):")
    seen = set()
    for nu in examples:
        spec = collections.Counter()
        for i in range(27):
            acc = zero_i
            for j in range(6):
                c = coeff[i][j]
                if c:
                    acc = ADD[acc, SCAL[c, nu[j]]]
            spec[lab[i]] += int(G[acc])
        key = tuple(sorted(spec.items()))
        if key in seen:
            continue
        seen.add(key)
        print(f"     {dict(sorted(spec.items()))}")
    return K3, K2, dict(total=total, full3=full3, best=best, best_count=best_count, su5_kept_full=su5_kept_full)


# ------------------------------------------------------------------------------------------------ (e') the K3 search
def wilson_search_k3(n, gens, m, chars, coords, moduli, h1, chis, wts, lab, sm_roots, rts, ip, wN, wnc):
    """When the three-generation alphabet is non-trivial and |H_1|^3 is out of reach: W is determined by the characters
    of Q, u^c and L (the three weights are a basis of P/Q_SM when the 3 x 3 coefficient matrix is invertible modulo
    every d_j), so the SM-commuting lines with three generations of Q, u^c, L are the triples in K3^3; the rest of the
    27's characters follow, and d^c, e^c, SU(5)-breaking and the unbroken roots are read off."""
    N = len(chars)
    cidx = {c: i for i, c in enumerate(coords)}
    add = lambda x, y: tuple((p + q) % d for p, q, d in zip(x, y, moduli))
    smul = lambda x, k: tuple((k * p) % d for p, d in zip(x, moduli))
    a2c = {a: c for a, c in zip(chars, coords)}
    chic = [a2c[c] for c in chis]
    zero = tuple([0] * len(moduli))
    key = lambda c: sum(c[k] * int(np.prod(moduli[:k])) for k in range(len(moduli)))
    G = np.zeros(N, dtype=np.int64)
    for a, c in zip(chars, coords):
        G[key(c)] = sum(h1[chars[cidx[add(ch, c)]]] for ch in chic)
    K3 = [c for c in coords if G[key(c)] >= 3]
    # the SM-root lattice and the coefficient rows
    Rm = sp.Matrix([list(a) for a in sm_roots])
    D, U, V = smith_with_transforms(Rm)
    dprime = [int(D[j, j]) for j in range(min(D.shape))]
    rank = sum(1 for d in dprime if d != 0)
    assert all(d == 1 for d in dprime[:rank]), dprime
    free = list(range(rank, 6))
    VT = V.T
    coeff = {i: [int(x) for x in (VT * sp.Matrix(list(wts[i])))] for i in range(27)}
    rcoeff = {a: [int(x) for x in (VT * sp.Matrix(list(a)))] for a in rts.values()}
    comp = {l: next(i for i in range(27) if lab[i] == l) for l in ('Q', 'u^c', 'd^c', 'L', 'e^c', 'H_u', 'H_d', 'D', 'Dbar', 'S', 'nu^c')}
    Cm = sp.Matrix([[coeff[comp[l]][j] for j in free] for l in ('Q', 'u^c', 'L')])
    det = int(Cm.det())
    print(f"  the characters of Q, u^c, L determine W: coefficient matrix det = {det}, invertible modulo every d_j: {all(math.gcd(det, d) == 1 for d in moduli)}")
    assert all(math.gcd(det, d) == 1 for d in moduli)
    adj = Cm.adjugate()
    # solve nu = C^-1 psi coordinatewise (each coordinate modulo its own d)
    K = len(K3)
    Kc = np.array(K3, dtype=np.int64)                      # K x ncoord
    ncoord = len(moduli)
    mods = np.array(moduli, dtype=np.int64)
    # all triples (psi_Q, psi_u, psi_L)
    iQ, iu, iL = np.meshgrid(np.arange(K), np.arange(K), np.arange(K), indexing='ij')
    iQ, iu, iL = iQ.ravel(), iu.ravel(), iL.ravel()
    psi = [Kc[iQ], Kc[iu], Kc[iL]]                          # each (T, ncoord)
    nu = []
    for j in range(3):
        acc = np.zeros_like(psi[0])
        for k in range(3):
            acc = acc + int(adj[j, k]) * psi[k]
        # divide by det: multiply by the inverse of det modulo each modulus
        inv = np.array([pow(det % int(d), -1, int(d)) for d in moduli], dtype=np.int64)
        nu.append((acc % mods) * inv % mods)
    def psi_of(coef):
        acc = np.zeros_like(psi[0])
        for j, f in enumerate(free):
            if coef[f]:
                acc = acc + coef[f] * nu[j]
        return acc % mods
    def Gof(arr):
        k = np.zeros(arr.shape[0], dtype=np.int64)
        for t in range(ncoord):
            k += arr[:, t] * int(np.prod(moduli[:t]))
        return G[k]
    pQ, pu, pL = psi_of(coeff[comp['Q']]), psi_of(coeff[comp['u^c']]), psi_of(coeff[comp['L']])
    assert np.array_equal(pQ, psi[0]) and np.array_equal(pu, psi[1]) and np.array_equal(pL, psi[2])
    pd, pe = psi_of(coeff[comp['d^c']]), psi_of(coeff[comp['e^c']])
    three = (Gof(pd) >= 3) & (Gof(pe) >= 3)
    broken = ~(np.all(pQ == pu, axis=1) & np.all(pu == pe, axis=1))
    sel = np.where(three & broken)[0]
    print(f"  Wilson lines with three generations of Q, u^c, L (K3^3 = {K}^3 = {len(iQ)}): with three generations of d^c and e^c as well: {int(three.sum())}; of those breaking SU(5): {len(sel)}")
    # the survivors: spectra, unbroken roots at the (N, nu^c) point, adjoint chirals
    specs = collections.Counter()
    groups = collections.Counter()
    orders = collections.Counter()
    images = collections.Counter()
    order_of = lambda c: max([d // math.gcd(int(x), d) for x, d in zip(c, moduli)] + [1])
    root_list = list(rts.values())
    su5_roots = [a for a in root_list if ip(a, wN) == 0 and ip(a, wnc) == 0]
    examples = []
    sm_vacua = 0            # SU(5) broken, three generations of the five, <N> and <nu^c> available, H_u and H_d present
    full_spectrum = 0       # all 81 states of the three 27s survive
    bad_kept = 0
    for t in sel:
        nut = [tuple(int(x) for x in nu[j][t]) for j in range(3)]
        def psi_c(coef):
            acc = zero
            for j, f in enumerate(free):
                if coef[f]:
                    acc = add(acc, smul(nut[j], coef[f]))
            return acc
        spec = collections.Counter()
        comp_chars = {}
        for i in range(27):
            pc = psi_c(coeff[i])
            comp_chars[i] = pc
            spec[lab[i]] += int(G[key(pc)])
        vac = spec['S'] >= 1 and spec['nu^c'] >= 1 and spec['H_u'] >= 1 and spec['H_d'] >= 1
        kept = [a for a in su5_roots if psi_c(rcoeff[a]) == zero]
        adjch = sum(int(h1[chars[cidx[psi_c(rcoeff[a])]]]) for a in root_list)
        specs[tuple(sorted(spec.items()))] += 1
        if vac:
            sm_vacua += 1
            groups[(len(kept), adjch)] += 1
            bad_kept += (len(kept) != 8)
            if sum(spec.values()) == 81:
                full_spectrum += 1
                # the image of W in the character group: the subgroup generated by the 27 component characters
                gen = set([zero])
                frontier = [zero]
                basis = list({comp_chars[i] for i in range(27)})
                while frontier:
                    nxt = []
                    for x in frontier:
                        for b in basis:
                            y = add(x, b)
                            if y not in gen:
                                gen.add(y); nxt.append(y)
                    frontier = nxt
                images[len(gen)] += 1
                orders[(order_of(comp_chars[comp['Q']]), order_of(comp_chars[comp['u^c']]), order_of(comp_chars[comp['e^c']]))] += 1
                if len(examples) < 3:
                    examples.append((dict(sorted(spec.items())), len(kept), adjch, nut, len(gen)))
    print(f"  of these, SM VACUA (SU(5) broken, three generations of Q, u^c, d^c, L, e^c, <N> and <nu^c> available, H_u and H_d present): {sm_vacua}; "
          f"with the FULL spectrum of the three 27s (81 states, nothing projected): {full_spectrum}")
    print(f"  distinct spectra (by label, summed over the three 27s) among the SU(5)-breaking three-generation lines: {len(specs)}")
    for sp_, cnt in sorted(specs.items(), key=lambda kv: -kv[1])[:6]:
        print(f"     x{cnt}: {dict(sp_)}")
    print(f"  SM vacua: (roots of SU(5) kept at the <N>,<nu^c> point, e6-adjoint chirals from the broken roots) -> count: {dict(groups)}; lines with kept != 8: {bad_kept}   (8 kept = exactly the SM's roots)")
    print(f"  full-spectrum vacua: order of the Wilson line's image in the character group -> count: {dict(images)}; (order of psi_Q, psi_u, psi_e) -> count: {dict(orders)}")
    return K3, dict(total=len(iQ), three=int(three.sum()), full3=len(sel), specs=len(specs), groups=dict(groups), examples=examples,
                    sm_vacua=sm_vacua, full_spectrum=full_spectrum, bad_kept=bad_kept, images=dict(images))


# ------------------------------------------------------------------------------------------------ main
def closing(n, wts, lab, sm_roots, exact_controls=3, enumerate_w=True, dps=40, extra=None):
    print(f"\n=== Y_{n}: the {n}-fold cyclic branched cover of the object ===")
    mp.mp.dps = dps
    gens, rels = TW.presentation(n, branched=True)
    Rm = relation_matrix(gens, rels)
    D, U, V = smith_with_transforms(Rm)
    inv = [int(D[j, j]) for j in range(min(D.shape))]
    tors = sorted(d for d in inv if d not in (0, 1))
    free = len(gens) - sum(1 for d in inv if d != 0)
    order = 1
    for d in tors:
        order *= d
    m = 1
    for d in tors:
        m = m * d // math.gcd(m, d)
    fox_order = alexander_order(n)
    print(f"  presentation: {len(gens)} generators, {len(rels)} relators; H_1 = {' + '.join(f'Z/{d}' for d in tors) or '0'} (free rank {free}), order {order}; "
          f"Fox's prod |Delta(zeta)| = {fox_order}: {order == fox_order}; exponent m = {m}")
    assert free == 0 and order == fox_order
    chars, coords, moduli = characters(D, V, m, with_coords=True)
    assert len(chars) == order and len(set(chars)) == order and len(set(coords)) == order
    # the relators are killed (sanity)
    for a in chars[:50]:
        for r in rels:
            assert sum((1 if L > 0 else -1) * a[abs(L) - 1] for L in r) % m == 0
    # (b) the sweep
    h1 = {}
    gaps = []
    t0 = __import__('time').time()
    for a in chars:
        h, h0, lo, hi = h1_numeric(gens, rels, a, m)
        h1[a] = h
        gaps.append((lo, hi))
    worst_hi = max(g[1] for g in gaps)
    worst_lo = min(g[0] for g in gaps)
    dist = collections.Counter(h1.values())
    print(f"  h^1(Y_{n}; psi) over all {len(chars)} characters (numeric, 40 digits): {dict(sorted(dist.items()))}; "
          f"smallest accepted singular value {worst_lo:.3e}, largest rejected {worst_hi:.3e}  ({__import__('time').time() - t0:.0f} s)")
    # exact confirmation of every character with h^1 > 0 and of a few zeros
    pos = [a for a in chars if h1[a] > 0]
    zeros = [a for a in chars if h1[a] == 0][:exact_controls]
    for a in pos + zeros:
        he = h1_exact(gens, rels, a, m)
        assert he == h1[a], (a, he, h1[a])
    print(f"  exact over Q(zeta_{m}): the {len(pos)} characters with h^1 > 0 and {len(zeros)} zero controls confirmed")
    # orders of the characters with h^1 > 0
    def order_of(a):
        o = 1
        for x in a:
            o = max(o, m // math.gcd(x, m))
        return o
    print(f"  characters with h^1 > 0: {[(order_of(a), h1[a]) for a in pos]}  (order, h^1)")
    # (c) the family characters
    chis = family_characters(n, gens, m)
    assert all(h1[c] == 1 for c in chis), [h1[c] for c in chis]
    add = lambda x, y: tuple((p + q) % m for p, q in zip(x, y))
    prod3 = add(add(chis[0], chis[1]), chis[2])
    print(f"  the three family characters chi_i (the descended 3_rho, Klein image, same for all 48 surjections): h^1 = {[h1[c] for c in chis]}, orders {[order_of(c) for c in chis]}, chi_1 chi_2 chi_3 trivial: {all(x == 0 for x in prod3)}")
    only_family = set(pos) == set(chis)
    print(f"  the characters with h^1 > 0 are EXACTLY the three family characters: {only_family}")
    if not only_family:
        extra_cls = [a for a in pos if a not in chis]
        orders_extra = collections.Counter(order_of(a) for a in extra_cls)
        closed = all(add(a, c) in set(pos) for a in extra_cls for c in chis)
        pairs = sum(1 for a in extra_cls for c in chis if add(a, c) in set(pos))
        print(f"  the extra classes: {len(extra_cls)} characters of orders {dict(orders_extra)}; the set of h^1 > 0 characters is closed under multiplication by the family characters: {closed} "
              f"({pairs} of {3 * len(extra_cls)} products land in it)")
    # (d), (e)
    K3, K2, results = wilson_search(n, gens, m, chars, h1, chis, wts, lab, sm_roots, enumerate_w=enumerate_w)
    k3_search = None
    if K3 == [tuple([0] * len(gens))]:
        print(f"  => on Y_{n}: three generations of Q, u^c, e^c force W trivial on the 10 of SU(5); W commutes with SU(5) (B1277 (d)); NO Standard-Model vacuum with three generations, with or without Wilson lines")
    elif extra is not None:
        rts, ip, wN, wnc = extra
        K3c, k3_search = wilson_search_k3(n, gens, m, chars, coords, moduli, h1, chis, wts, lab, sm_roots, rts, ip, wN, wnc)
        if k3_search['full3'] > 0:
            print(f"  => on Y_{n}: the three-generation alphabet is NON-TRIVIAL; {k3_search['full3']} SM-commuting Wilson lines break SU(5) with three generations of Q, u^c, d^c, L, e^c, "
                  f"{k3_search['sm_vacua']} of them SM vacua (VEVs and both Higgs doublets available), {k3_search['full_spectrum']} keeping all 81 states of the three 27s -- vector-like (B1260)")
        else:
            print(f"  => on Y_{n}: the alphabet is non-trivial but no Wilson line with three generations of Q, u^c, L also keeps three of d^c, e^c and breaks SU(5)")
    return dict(tors=tors, order=order, m=m, dist=dict(dist), pos=pos, chis=chis, only_family=only_family, K3=K3, K2=K2, results=results, k3_search=k3_search)


def main():
    wts, rep = C.load()
    lab, hy, wts2 = R.sm_labels()
    assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = VM.descent_data()
    sm_roots = sorted(set(a2) | {a1, tuple(-x for x in a1)})
    iN = next(i for i in range(27) if lab[i] == 'S'); inc = next(i for i in range(27) if lab[i] == 'nu^c')
    wN, wnc = [F(x) for x in wts[iN]], [F(x) for x in wts[inc]]
    ns = [int(x) for x in sys.argv[1:]] or [3, 6]
    out = {}
    for n in ns:
        out[n] = closing(n, wts, lab, sm_roots, enumerate_w=(n <= 6), dps=(40 if n <= 9 else 30), extra=(rts, ip, wN, wnc))
    ok = True
    if 3 in out:
        c3 = out[3]['tors'] == [4, 4] and out[3]['only_family'] and out[3]['K3'] == [tuple([0] * 4)] and out[3]['results']['full3'] == 0 and out[3]['results']['best'] == 2
        print(f"\n  Y_3 control reproduces B1277 (H_1 = Z/4 + Z/4, only the three sign characters carry h^1, K3 trivial, best SU(5)-breaking spectrum two generations): {c3}")
        ok = ok and c3
    if 6 in out:
        c6 = out[6]['order'] == 320 and out[6]['K3'] == [tuple([0] * 7)] and out[6]['results']['full3'] == 0
        print(f"  Y_6: |H_1| = {out[6]['order']} = {' + '.join(f'Z/{d}' for d in out[6]['tors'])}; h^1 distribution {out[6]['dist']}; only the family characters carry h^1: {out[6]['only_family']}; K3 trivial and no SU(5)-breaking three-generation Wilson line: {c6}")
        ok = ok and c6
    for n in ns:
        if n not in (3, 6):
            triv = out[n]['K3'] == [tuple([0] * (n + 1))]
            ks = out[n]['k3_search']
            print(f"  Y_{n}: |H_1| = {out[n]['order']} = {' + '.join(f'Z/{d}' for d in out[n]['tors'])}; h^1 distribution {out[n]['dist']}; K3 trivial: {triv}"
                  + (f"; SU(5)-breaking three-generation Wilson lines: {ks['full3']}, SM vacua {ks['sm_vacua']}, full-spectrum {ks['full_spectrum']}, all with exactly the SM's roots kept: {ks['bad_kept'] == 0}" if ks else ""))
            ok = ok and (triv or (ks is not None and ks['bad_kept'] == 0))
    return ok


if __name__ == "__main__":
    print("=== the six-fold closing's Wilson lines: H_1(Y_n), every character's h^1 (numeric sweep + exact cyclotomic confirmation), the family characters, the three-generation alphabet ===")
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
