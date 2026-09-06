#!/usr/bin/env python3
"""THE VACUUM MANIFOLD OF THE OBJECT'S OWN CLOSING, AND ITS WILSON LINES (L205, L204), computed from B1273's theory
and B1276's operator list.

The E8 theory on Y_3 (B1273): gauge e6 + u(1)^2 (the family torus), matter three 27s (family charges e_i), three
27bars (-e_i), six flavons S_ij (e_i - e_j), no adjoint chiral (b_1 = 0).  Superpotential (B1273/B1276, one
coupling): W = lambda [ d_abc 27_1^a 27_2^b 27_3^c + dbar 27bar_1 27bar_2 27bar_3 + sum_{i!=j} S_ij (27_j . 27bar_i)
+ S_12 S_23 S_31 + S_21 S_32 S_13 ] (the E8 bracket's three cubic pieces on the classes of Y_3; only the existence of
each monomial matters below, never its coefficient).

(a) THE NEUTRAL FIELDS: the colour-singlet, electrically neutral components of each 27 (N = the SO(10) singlet,
    nu^c, h_u^0, h_d^0, nu -- read off B1252's descent: SU(3)_c weights zero, T_3 + Y = 0), their 27bar
    conjugates, and the six flavons: 36 fields.  The 56 cubic monomials of W among them.
(b) F-FLATNESS ON COORDINATE SUBSPACES (exact rule): for a cubic W with squarefree monomials, the subspace
    "the fields of A are non-zero, all others zero" is F-flat at its generic point iff NO monomial of W contains
    two fields of A (distinct squarefree monomials are linearly independent).  D-FLATNESS by conjugate pairing
    (exact): 27_g = v, 27bar_g = conj(v) is D-flat for every v, because the holomorphic invariant I = 27_g . 27bar_g
    has dI/d(27^a) = 27bar_a = conj(27^a) (the Buccella-Derendinger-Ferrara-Savoy / Luty-Taylor criterion); the
    same for (S_ij, S_ji) and for sums of such pairs.  So the pair-directions P[X_g] = (X_g, Xbar_g) and
    Q[S_ij] = (S_ij, S_ji) are exactly D-flat, and the maximal F-flat paired branches are the maximal independent
    sets of the co-occurrence graph on the 18 pair-directions.  A Cartan-charge LP over all field-level
    independent sets lists the unpaired candidates (necessary condition only).
(c) FOR EACH MAXIMAL BRANCH: the unbroken algebra.  A paired VEV along the weight w kills the root vector E_alpha
    iff <w, alpha> != 0 (minuscule 27: E_alpha e_w != 0 iff <w,alpha^v> = -1, E_alpha e_{-w} != 0 iff +1) and the
    Cartan directions h with <h, w> != 0 mixed with the family torus t through <h,w> + <t,e_g> = 0.  So: the
    e6-part = (Cartan orthogonal to all VEV weights) + (roots orthogonal to all VEV weights), the total rank =
    8 - rank of the combined (weight, family-charge) matrix.
(d) THE WILSON LINES OF THE CLOSING.  z_L = (-1)^{2 T_3}, the centre of SU(2)_L, is an involution of E6; its
    centralizer, its joint stabilizer with the (N, nu^c) VEVs (exactly the SM), the SM's commutant in e6
    (B1269's c(s), dim 5: here identified as su(2)_beta + u(1)^2 with su(2)_beta the SU(2) of SU(6) x SU(2) pairing
    (d^c, Dbar), (L, H_d), (nu^c, S); the 10 of SU(5) -- Q, u^c, e^c -- is su(2)_beta-singlet), the sixteen
    characters of H_1(Y_3) = Z_4^2 and their h^1 by Fox calculus (exact over Q(i)), the torus elements of order
    dividing 4 that commute with the SM, and the zero-mode spectra for W = z_L o chi_j and W = (-1_beta) o chi_j.
    THEOREM: a vacuum (neutral tree-level VEVs + a flat E6 connection W) whose unbroken group contains the derived
    SM has VEVs only in N, nu^c (stabilizer SU(5)) and W valued in C(SM) = SU(2)_beta . A (A abelian); Q, u^c, e^c
    are SU(2)_beta-singlets, so their multiplicities are h^1(chi_i (x) psi_c) for characters psi_c of H_1 = Z_4^2;
    h^1 = 1 exactly for the three sign characters, so a component keeps its three generations iff psi_c = 1; W then
    acts trivially on the 10 of SU(5), whose weights every SU(5) root connects, so W commutes with SU(5): the
    unbroken group contains SU(5).  Hence no vacuum of the closing has gauge group containing the SM together
    with three generations of Q, u^c, e^c -- with or without Wilson lines, abelian or not.
(e) L204, THE OBJECT'S OWN ABELIAN LOCAL SYSTEMS: H^1(m004; C_t) != 0 exactly at t^2 - 3t + 1 = 0, i.e. at
    t = phi^{+-2} -- real, off the unit circle: no unitary abelian holonomy on the cusp carries a class.
"""
from __future__ import annotations
import os, sys, math, itertools, collections, pathlib
from fractions import Fraction as F
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for arc in ('B1267_spectrum_law_rebuilt', 'B1269_transport_computed', 'B1273_the_three_fold_closing',
            'B1275_the_cubic_made_explicit', 'B1276_the_relations_the_chain_forces'):
    sys.path.insert(0, str(ROOT / 'frontier' / arc / 'verification'))
import e6_instrument as E
import spectrum_law as S
import transport as T
import three_fold_closing as TF3
import cubic_explicit as C
import relations as R


# ----------------------------------------------------------------------------------------------- descent data
def descent_data():
    sub, Y, rts, Mf = T.sm_subalgebra()
    ip = lambda a, b: sum(F(a[i]) * Mf[i][j] * F(b[j]) for i in range(6) for j in range(6))
    # sm_subalgebra returns ALL eight roots of A2 + A1.  The A1 roots are orthogonal to every root but their own
    # negative; the six remaining roots are the A2 (colour).  The sign of a1 fixes the T_3 convention (the other
    # sign is the SU(2)_L Weyl conjugate: same subgroup up to conjugation, same vacuum manifold).
    sub = [tuple(r) for r in sub]
    neg = lambda r: tuple(-x for x in r)
    a1s = [r for r in sub if all(ip(r, s) == 0 for s in sub if s != r and s != neg(r))]
    assert len(a1s) == 2 and a1s[1] == neg(a1s[0])
    a1 = a1s[0]
    a2 = [s for s in sub if s not in a1s]
    assert len(a2) == 6 and ip(a1, a1) == 2 and all(ip(s, s) == 2 for s in a2)
    assert all(ip(a1, s) == 0 for s in a2)
    # the coordinates are Dynkin labels for E.C's simple system: the metric is C^-1 and every root is integral in
    # simple-root coordinates (checked), so exp(2 pi i lambda), lambda = n/4 in simple-root coordinates, acts on the
    # weight w by i^(n . w)
    Cm = sp.Matrix(E.C)
    Ci = Cm.inv()
    assert all(sp.Rational(Mf[i][j]) == Ci[i, j] for i in range(6) for j in range(6))
    assert all(all(x.q == 1 for x in (Ci * sp.Matrix(list(r)))) for r in rts.values())
    return sub, Y, rts, Mf, ip, a1, a2


def neutral_components(wts, hy, ip, a1, a2):
    out = {}
    for i, w in enumerate(wts):
        colour = all(ip(s, w) == 0 for s in a2)
        t3 = ip(a1, w) / 2
        q = t3 + hy[i]
        if colour and q == 0:
            out[i] = (t3, hy[i])
    return out


def algebra_name(rank, nroots):
    table = {(6, 72): 'e6', (5, 40): 'so(10)+u(1)', (4, 20): 'su(5)', (5, 20): 'su(5)+u(1)', (4, 8): 'su(3)+su(2)+u(1)',
             (3, 12): 'su(4)', (4, 12): 'su(4)+u(1)', (3, 8): 'su(3)+su(2)', (3, 6): 'su(3)+u(1)', (2, 6): 'su(3)',
             (4, 24): 'so(8)', (6, 8): 'su(3)+su(2)+u(1)^3'}
    return table.get((rank, nroots), f'rank {rank}, {nroots} roots')


# ----------------------------------------------------------------------------------------------- (a)-(c)
def parts_abc(wts, triples, lab, hy, ip, a1, a2, rts):
    neutral = neutral_components(wts, hy, ip, a1, a2)
    names = {i: {'S': 'N', 'nu^c': 'nu^c', 'H_u': 'h_u0', 'H_d': 'h_d0', 'L': 'nu'}[lab[i]] for i in neutral}
    print(f"  neutral colour-singlet components of the 27 (T_3, Y): { {names[i]: (str(neutral[i][0]), str(neutral[i][1])) for i in neutral} }")
    assert sorted(names.values()) == ['N', 'h_d0', 'h_u0', 'nu', 'nu^c']
    inv = {v: k for k, v in names.items()}
    gens = (1, 2, 3)
    fields = []                                   # (name, kind, generation, weight index or None, family charge)
    e = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}       # the weights of the 3 of SU(3)_fam in a basis of its torus
    for g in gens:
        for nm, wi in inv.items():
            fields.append((f"{nm}_{g}", '27', g, wi, e[g]))
        for nm, wi in inv.items():
            fields.append((f"{nm}bar_{g}", '27bar', g, wi, tuple(-x for x in e[g])))
    for i in gens:
        for j in gens:
            if i != j:
                fields.append((f"S_{i}{j}", 'S', (i, j), None, tuple(x - y for x, y in zip(e[i], e[j]))))
    fid = {f[0]: k for k, f in enumerate(fields)}
    print(f"  fields: {len(fields)} = 3 x 5 (27) + 3 x 5 (27bar) + 6 (flavons)")
    zero_sum = {tuple(sorted(t)) for t in triples}
    mons = []
    neut = list(inv.values())
    for (a, b, c) in itertools.combinations(neut, 3):
        if tuple(sorted((a, b, c))) in zero_sum:
            for (i, j, k) in itertools.permutations(gens):
                mons.append((f"{names[a]}_{i}", f"{names[b]}_{j}", f"{names[c]}_{k}"))
                mons.append((f"{names[a]}bar_{i}", f"{names[b]}bar_{j}", f"{names[c]}bar_{k}"))
    for i in gens:
        for j in gens:
            if i != j:
                for nm in inv:
                    mons.append((f"S_{i}{j}", f"{nm}_{j}", f"{nm}bar_{i}"))
    mons.append(("S_12", "S_23", "S_31")); mons.append(("S_21", "S_32", "S_13"))
    kinds = collections.Counter()
    for m in mons:
        if m[0].startswith('S_') and m[1].startswith('S_'):
            kinds['S S S'] += 1
        elif m[0].startswith('S_'):
            kinds['S 27 27bar'] += 1
        elif 'bar' in m[0]:
            kinds['27bar^3'] += 1
        else:
            kinds['27^3'] += 1
    cubic_neutral = sorted({tuple(sorted(names[x] for x in t)) for t in itertools.combinations(neut, 3) if tuple(sorted(t)) in zero_sum})
    print(f"  cubic monomials of W among the neutral fields: {len(mons)} = {dict(kinds)}")
    print(f"  the neutral zero-sum triples of the 27: {cubic_neutral}  (the mu-term N h_u h_d and the Dirac term nu h_u nu^c)")
    assert cubic_neutral == [('N', 'h_d0', 'h_u0'), ('h_u0', 'nu', 'nu^c')] and len(mons) == 56
    # ------------------------------------------------------------ F-flat coordinate subspaces
    adj = collections.defaultdict(set)
    for m in mons:
        for x, y in itertools.combinations(m, 2):
            adj[x].add(y); adj[y].add(x)
    pairs = []
    for g in gens:
        for nm in inv:
            pairs.append((f"P[{nm}_{g}]", (f"{nm}_{g}", f"{nm}bar_{g}"), 'rank' if nm in ('N', 'nu^c') else 'ew'))
    for (i, j) in ((1, 2), (2, 3), (1, 3)):
        pairs.append((f"Q[S_{i}{j}]", (f"S_{i}{j}", f"S_{j}{i}"), 'flavon'))
    ok_pair = {p[0]: not (p[1][1] in adj[p[1][0]]) for p in pairs}
    assert all(ok_pair.values())
    compat = {}
    for p, q in itertools.combinations(pairs, 2):
        compat[(p[0], q[0])] = compat[(q[0], p[0])] = not any(y in adj[x] for x in p[1] for y in q[1])
    P = [p[0] for p in pairs]
    maximal = []

    def bk(Rset, Pset, Xset):
        if not Pset and not Xset:
            maximal.append(sorted(Rset)); return
        for v in list(Pset):
            nb = {u for u in P if u != v and compat[(u, v)]}
            bk(Rset | {v}, Pset & nb, Xset & nb)
            Pset = Pset - {v}; Xset = Xset | {v}
    bk(set(), set(P), set())
    pinfo = {p[0]: p for p in pairs}
    wvec = {i: [F(x) for x in wts[i]] for i in range(27)}
    rootlist = list(rts.values())

    def unbroken(won_names, flavon_names):
        """won_names: 27 fields switched on (paired with their conjugates); flavon_names: S_ij switched on (paired)."""
        widx = [fid[x] for x in won_names]
        weights = [wvec[fields[k][3]] for k in widx]
        fam_w = [fields[k][4] for k in widx]
        fam_s = [fields[fid[x]][4] for x in flavon_names]
        Mw = sp.Matrix([[sp.Rational(x) for x in w] for w in weights]) if weights else sp.zeros(0, 6)
        rank_w = Mw.rank() if weights else 0
        kept_roots = [a for a in rootlist if all(ip(w, a) == 0 for w in weights)]
        rows = [[sp.Rational(x) for x in w] + [sp.Rational(x) for x in f] for w, f in zip(weights, fam_w)]
        rows += [[sp.Integer(0)] * 6 + [sp.Rational(x) for x in f] for f in fam_s]
        rank_c = sp.Matrix(rows).rank() if rows else 0
        return 6 - rank_w, kept_roots, 8 - rank_c

    print(f"\n  maximal F-flat paired branches: {len(maximal)}")
    rows = []
    for br in maximal:
        kinds_b = collections.Counter(pinfo[p][2] for p in br)
        won = [pinfo[p][1][0] for p in br if pinfo[p][2] != 'flavon']
        fl = [pinfo[p][1][0] for p in br if pinfo[p][2] == 'flavon']
        crank, kroots, total_rank = unbroken(won, fl)
        rows.append((len(br), dict(kinds_b), crank, kroots, total_rank, br))
    rows.sort(key=lambda r: (-r[0], str(r[5])))
    both = 0
    depth = []
    for n, kb, crank, kroots, trank, br in rows:
        nm = algebra_name(crank, len(kroots))
        has_rank = kb.get('rank', 0) > 0
        has_ew = kb.get('ew', 0) > 0
        both += has_rank and has_ew
        depth.append((crank, len(kroots)))
        print(f"    {n} pairs {kb}: e6-part {nm} (dim {crank + len(kroots)}), unbroken rank {trank} of 8 "
              f"({trank - crank} extra u(1) mixed with the family torus); rank-reducing {'yes' if has_rank else 'no'}, electroweak {'yes' if has_ew else 'no'}: {br}")
    print(f"  branches containing BOTH a rank-reducing VEV (N or nu^c) and an electroweak VEV (h_u0, h_d0, nu): {both} of {len(rows)}")
    per_weight = collections.Counter()
    for _, kb, _, _, _, br in rows:
        for nm in ('N', 'nu^c'):
            per_weight[(nm, sum(1 for p in br if p.startswith(f'P[{nm}_')))] += 1
    print(f"  (weight, generations carrying it in a maximal branch) -> count: {dict(sorted(per_weight.items()))}")
    sub_n = unbroken(['N_1'], [])
    sub_nn = unbroken(['N_1', 'nu^c_1'], [])
    sub_all = unbroken(['N_1', 'nu^c_1', 'h_u0_1', 'h_d0_1', 'nu_1'], [])
    print(f"  sub-branches of one generation: <N> -> {algebra_name(sub_n[0], len(sub_n[1]))}, rank {sub_n[2]}; "
          f"<N>,<nu^c> -> {algebra_name(sub_nn[0], len(sub_nn[1]))}, rank {sub_nn[2]}; all five -> {algebra_name(sub_all[0], len(sub_all[1]))}, rank {sub_all[2]}")
    sm_point = any(cr == 4 and len(kr) == 8 for cr, kr in depth)
    print(f"  a maximal branch with e6-part su(3)+su(2)+u(1): {sm_point}   (the SM is not a point of the tree-level manifold)")
    # ------------------------------------------------------------ Cartan-LP scan of field-level independent sets
    from scipy.optimize import linprog
    Fs = [f[0] for f in fields]
    charge = {}
    for f in fields:
        nm, kind, g, wi, fam = f
        if kind == '27':
            charge[nm] = [float(x) for x in wvec[wi]] + [float(x) for x in fam]
        elif kind == '27bar':
            charge[nm] = [-float(x) for x in wvec[wi]] + [float(x) for x in fam]
        else:
            charge[nm] = [0.0] * 6 + [float(x) for x in fam]
    fmax = []

    def bk2(Rs, Ps, Xs):
        if not Ps and not Xs:
            fmax.append(sorted(Rs)); return
        for v in list(Ps):
            nb = {u for u in Fs if u != v and u not in adj[v]}
            bk2(Rs | {v}, Ps & nb, Xs & nb)
            Ps = Ps - {v}; Xs = Xs | {v}
    bk2(set(), set(Fs), set())
    partner = {}
    for p in pairs:
        partner[p[1][0]] = p[1][1]; partner[p[1][1]] = p[1][0]
    unpaired = []
    for A in fmax:
        M = np.array([charge[x] for x in A]).T
        res = linprog(c=np.zeros(len(A)), A_eq=M, b_eq=np.zeros(8), bounds=[(1, None)] * len(A), method='highs')
        if res.status == 0 and not all(partner[x] in A for x in A):
            unpaired.append(A)
    print(f"  field-level maximal F-flat sets: {len(fmax)}; Cartan-D-feasible with all magnitudes positive and NOT conjugate-paired: {len(unpaired)}   (no unpaired branch passes even the Cartan test)")
    for A in unpaired[:3]:
        print(f"     e.g. {A}")
    return {'maximal': len(maximal), 'both': both, 'per_weight': dict(per_weight), 'depth': depth, 'sm_point': sm_point,
            'sub': (sub_n, sub_nn, sub_all), 'unpaired': unpaired, 'neutral_idx': inv, 'names': names, 'fields': fields, 'e': e}


# ----------------------------------------------------------------------------------------------- (d)
def fox_scalar(word, g, psi):
    acc, cur = sp.Integer(0), sp.Integer(1)
    for L in word:
        if L > 0:
            if L == g:
                acc += cur
            cur = cur * psi[L]
        else:
            cur = cur / psi[-L]
            if -L == g:
                acc -= cur
    return sp.expand(acc)


def h1_character(gens, rels, psi):
    d1 = sp.Matrix([[fox_scalar(r, g, psi) for g in gens] for r in rels])
    d0 = sp.Matrix([[psi[g] - 1] for g in gens])
    r1 = d1.rank(simplify=True)
    r0 = d0.rank(simplify=True)
    return (len(gens) - r1) - r0, 1 - r0


def part_d(wts, lab, hy, ip, a1, a2, rts, info):
    I = sp.I
    # (d1) z_L = (-1)^{2 T_3} on the 27
    two_t3 = [int(ip(a1, w)) for w in wts]
    assert all(t in (-1, 0, 1) for t in two_t3)
    zL = [(-1) ** (t % 2) for t in two_t3]
    sixY = [int(6 * hy[i]) for i in range(27)]
    print(f"  z_L = (-1)^(2T_3) on the 27: {zL.count(1)} (+1), {zL.count(-1)} (-1); equals (-1)^(6Y) on every component: {all(zL[i] == (-1) ** (sixY[i] % 2) for i in range(27))}")
    rootlist = list(rts.values())
    even = [a for a in rootlist if int(ip(a1, a)) % 2 == 0]
    print(f"  centralizer of z_L in e6: Cartan 6 + {len(even)} roots = dim {6 + len(even)}   (an involution of type A1 A5 iff 38)")
    # (d2) joint stabilizer with the (N, nu^c) paired VEVs
    inv = info['neutral_idx']
    wN, wnc = [F(x) for x in wts[inv['N']]], [F(x) for x in wts[inv['nu^c']]]
    joint = [a for a in even if ip(a, wN) == 0 and ip(a, wnc) == 0]
    sm_roots = set(a2) | {a1, tuple(-x for x in a1)}
    crank = 6 - sp.Matrix([list(map(sp.Rational, wN)), list(map(sp.Rational, wnc))]).rank()
    print(f"  joint stabilizer of z_L and <N>, <nu^c>: Cartan {crank} + {len(joint)} roots; the roots are exactly the SM's (colour A2 + weak A1): {set(joint) == sm_roots}")
    # the SM's commutant c(s) (B1269: dim 5): the Cartan directions orthogonal to colour and T_3 (3) plus the roots
    # orthogonal to the whole SM Cartan (colour A2, T_3, Y): two, +-beta, an su(2)_beta commuting with the SM
    Yv = T.sm_subalgebra()[1]
    sm_cartan = [a2[0], a2[1], a1, Yv]
    orth = [a for a in rootlist if all(ip(a, x) == 0 for x in sm_cartan)]
    assert len(orth) == 2 and orth[1] == tuple(-x for x in orth[0])
    beta = orth[0]
    wkeys = {tuple(F(x) for x in w): i for i, w in enumerate(wts)}
    doublets = []
    for i, w in enumerate(wts):
        up = tuple(F(x) + F(y) for x, y in zip(w, beta))
        if up in wkeys:
            doublets.append((lab[i], lab[wkeys[up]]))
    singlets = sorted(collections.Counter(lab[i] for i in range(27) if all(tuple(F(x) + s * F(y) for x, y in zip(wts[i], beta)) not in wkeys for s in (1, -1))).items())
    print(f"  the SM's commutant in e6: u(1)^3 (Cartan orthogonal to colour and T_3) + {len(orth)} roots +-beta = su(2)_beta + u(1)^2, dim 5 (B1269's c(s));")
    print(f"     su(2)_beta doublets in the 27: {sorted(collections.Counter(doublets).items())}; singlets: {singlets}")
    assert sorted(collections.Counter(doublets).items()) == [(('L', 'H_d'), 2), (('d^c', 'Dbar'), 3), (('nu^c', 'S'), 1)] or \
           sorted(collections.Counter(tuple(sorted(d)) for d in doublets).items()) == [(('Dbar', 'd^c'), 3), (('H_d', 'L'), 2), (('S', 'nu^c'), 1)]
    assert singlets == [('D', 3), ('H_u', 2), ('Q', 6), ('e^c', 1), ('u^c', 3)]
    # every root of SU(5) (the stabilizer of <N>, <nu^c>) connects two weights of the 10 = {Q, u^c, e^c}: an element
    # trivial on the 10 commutes with SU(5)
    su5 = [a for a in rootlist if ip(a, wN) == 0 and ip(a, wnc) == 0]
    ten = {tuple(F(x) for x in wts[i]) for i in range(27) if lab[i] in ('Q', 'u^c', 'e^c')}
    connects = all(any(tuple(x + F(y) for x, y in zip(w, a)) in ten for w in ten) for a in su5)
    print(f"  SU(5) = stabilizer of <N>,<nu^c>: {len(su5)} roots, every one connecting two weights of the 10 (Q, u^c, e^c): {connects}  -> trivial on the 10 => commutes with SU(5)")
    assert len(su5) == 20 and connects
    # (d3) the sixteen characters of H_1(Y_3) = Z_4^2 and their h^1 (exact over Q(i))
    gens, rels = TF3.branched_cover_presentation()
    chars = []
    for ex in itertools.product(range(4), repeat=len(gens)):
        psi = {g: I ** ex[k] for k, g in enumerate(gens)}
        if all(sp.expand(sp.prod([psi[abs(L)] ** (1 if L > 0 else -1) for L in r]) - 1) == 0 for r in rels):
            chars.append(ex)
    assert len(chars) == 16, len(chars)
    h1 = {}
    orders = {}
    for ex in chars:
        psi = {g: I ** ex[k] for k, g in enumerate(gens)}
        h1[ex] = h1_character(gens, rels, psi)
        orders[ex] = max([4 // math.gcd(e_, 4) for e_ in ex] + [1])
    byorder = collections.defaultdict(list)
    for ex in chars:
        byorder[orders[ex]].append((ex, h1[ex]))
    for o in sorted(byorder):
        print(f"  characters of order {o}: {len(byorder[o])}; (h^1, h^0) values: {dict(collections.Counter(v for _, v in byorder[o]))}")
    signs = [ex for ex in chars if orders[ex] == 2]
    assert len(signs) == 3 and all(h1[ex] == (1, 0) for ex in signs)
    assert all(h1[ex] == (0, 0) for ex in chars if orders[ex] == 4) and h1[(0,) * len(gens)] == (0, 1)
    add = lambda x, y: tuple((a + b) % 4 for a, b in zip(x, y))
    keep3 = [psi for psi in chars if all(h1[add(chi, psi)][0] == 1 for chi in signs)]
    print(f"  characters psi with h^1(chi_i psi) = 1 for all three sign characters chi_i: {keep3}   (only the trivial one)")
    assert keep3 == [(0,) * len(gens)]
    # (d4) the torus elements of order | 4 commuting with the SM; those trivial on the SM matter
    Cm = sp.Matrix(E.C)
    Ci = Cm.inv()
    ten_idx = [i for i in range(27) if lab[i] in ('Q', 'u^c', 'e^c')]
    assert len(ten_idx) == 10
    commuting, trivial_on_ten = [], []
    for n in itertools.product(range(4), repeat=6):
        if all(sum(ni * ai for ni, ai in zip(n, a)) % 4 == 0 for a in sm_roots):
            commuting.append(n)
            if all(sum(ni * wi for ni, wi in zip(n, wts[i])) % 4 == 0 for i in ten_idx):
                trivial_on_ten.append(n)
    nb = tuple(int(x) for x in (Ci * sp.Matrix(list(beta))))
    beta_torus = sorted({tuple((k * x) % 4 for x in nb) for k in range(4)})
    print(f"  torus elements t = exp(2 pi i n/4) (n in simple-root coordinates) with t^4 = 1 commuting with the SM: {len(commuting)}; "
          f"trivial on the 10 (Q, u^c, e^c): {len(trivial_on_ten)}, all of them exp(2 pi i k beta^v/4) in SU(2)_beta's torus: {sorted(trivial_on_ten) == beta_torus}")
    assert sorted(trivial_on_ten) == beta_torus and len(beta_torus) == 4
    m = Ci * sp.Matrix(list(a1))
    nzL = tuple(int(2 * x) % 4 for x in m)
    acts = [(-1) ** (((sum(ni * wi for ni, wi in zip(nzL, wts[i])) % 4) // 2) % 2) for i in range(27)]
    print(f"  z_L = exp(2 pi i n/4) with n = {nzL}: acts as (-1)^(2T_3) on the 27: {acts == zL}; z_L commutes with the SM: {nzL in commuting}")
    assert acts == zL and nzL in commuting
    # (d5) the spectrum for W = z_L o chi_j (j = 1): m(c, i) = h^1(chi_i (x) chi_j^{[2T_3 odd]})
    chi = {1: signs[0], 2: signs[1], 3: signs[2]}
    j = 1
    spec = {}
    for i in (1, 2, 3):
        for c in range(27):
            psi_c = chi[j] if zL[c] == -1 else (0,) * len(gens)
            spec[(i, lab[c], c)] = h1[add(chi[i], psi_c)][0]
    by_gen = {i: collections.Counter() for i in (1, 2, 3)}
    for (i, l, c), mult in spec.items():
        by_gen[i][l] += mult
    print(f"  Wilson line W = z_L o chi_{j}: surviving components of 27_i (multiplicity-summed by SM label):")
    for i in (1, 2, 3):
        print(f"     27_{i}: total {sum(by_gen[i].values())} of 27; {dict(sorted(by_gen[i].items()))}")
    lost = {i: 27 - sum(by_gen[i].values()) for i in (1, 2, 3)}
    adj_chirals = sum(h1[chi[j]][0] for a in rootlist if int(ip(a1, a)) % 2 == 1)
    print(f"  lost states per generation: {lost} (the SU(2)_L doublets Q, L, H_u, H_d of generation {j}); "
          f"e6-adjoint chirals from the z_L-odd roots: {adj_chirals} (the (2,20) of SU(2) x SU(6), vector-like); flavons: 6 (unchanged)")
    assert lost == {1: 12, 2: 0, 3: 0} and adj_chirals == 40
    # the other involution: -1 in SU(2)_beta, W = (-1_beta) o chi_j: commutes with SU(6) > SU(5), keeps the 10
    zB = [(-1) ** (int(ip(beta, w)) % 2) for w in wts]
    assert zB.count(-1) == 12
    by_gen_b = {i: collections.Counter() for i in (1, 2, 3)}
    for i in (1, 2, 3):
        for c in range(27):
            psi_c = chi[j] if zB[c] == -1 else (0,) * len(gens)
            by_gen_b[i][lab[c]] += h1[add(chi[i], psi_c)][0]
    lost_b = {i: 27 - sum(by_gen_b[i].values()) for i in (1, 2, 3)}
    joint_b = [a for a in rootlist if int(ip(beta, a)) % 2 == 0 and ip(a, wN) == 0 and ip(a, wnc) == 0]
    print(f"  Wilson line W = (-1_beta) o chi_{j}: lost states per generation {lost_b} (the su(2)_beta doublets d^c, Dbar, L, H_d, nu^c, S of generation {j}); "
          f"Q, u^c, e^c keep three generations; joint stabilizer with <N>,<nu^c>: {len(joint_b)} roots = SU(5) (not the SM)")
    assert lost_b == {1: 12, 2: 0, 3: 0} and len(joint_b) == 20
    print("  THEOREM: SM unbroken => VEVs in {N, nu^c} (stabilizer SU(5)) and W in C(SM) = SU(2)_beta . A; Q, u^c, e^c are SU(2)_beta-singlets, so three generations of them")
    print("           => their characters are trivial => W is trivial on the 10 => W commutes with SU(5) => the unbroken group contains SU(5).  No SM vacuum with three generations on Y_3.")
    return {'zL': zL, 'even': len(even), 'joint_ok': set(joint) == sm_roots, 'commuting': len(commuting), 'lost': lost, 'adj': adj_chirals, 'crank': crank, 'orth': len(orth), 'lost_b': lost_b, 'joint_b': len(joint_b), 'connects': connects}


# ----------------------------------------------------------------------------------------------- (e)
def part_e():
    t = sp.symbols('t')
    psi = {1: t, 2: t}
    fa, fb = [sp.factor(sp.together(fox_scalar(S.REL, g, psi))) for g in (1, 2)]
    print(f"  m004, abelian local system a, b -> t: Fox row (dR/da, dR/db) = ({fa}, {fb})")
    roots_a = set(sp.solve(sp.numer(sp.together(fa)), t))
    roots_b = set(sp.solve(sp.numer(sp.together(fb)), t))
    common = sorted(roots_a & roots_b, key=lambda x: float(x))
    phi = (1 + sp.sqrt(5)) / 2
    golden = sorted([sp.radsimp(sp.expand(phi ** 2)), sp.radsimp(phi ** -2)], key=lambda x: float(x))
    ok = len(common) == 2 and all(sp.simplify(x - y) == 0 for x, y in zip(common, golden))
    print(f"  H^1(m004; C_t) != 0 (t != 1) iff both Fox derivatives vanish iff t in {common} = phi^(+-2): {ok}; "
          f"|t| = 1 for none of them: {all(abs(float(x)) != 1 for x in common)}; (t - phi^2)(t - phi^-2) = {sp.expand(sp.radsimp((t - golden[0]) * (t - golden[1])))}")
    return ok


def main():
    wts, rep = C.load()
    triples, idx, ns = C.solve_cubic(wts, rep)
    lab, hy, wts2 = R.sm_labels()
    assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = descent_data()
    print("\n=== (a)-(c) the tree-level vacuum manifold ===")
    info = parts_abc(wts, triples, lab, hy, ip, a1, a2, rts)
    print("\n=== (d) the Wilson lines of the closing ===")
    d = part_d(wts, lab, hy, ip, a1, a2, rts, info)
    print("\n=== (e) L204: the object's abelian local systems ===")
    e_ok = part_e()
    ok = (info['maximal'] == 9 and info['both'] == 9 and not info['sm_point']
          and info['per_weight'].get(('N', 1)) == 9 and info['per_weight'].get(('N', 2), 0) == 0
          and (3, 12) in info['depth'] and info['sub'][1][0] == 4 and len(info['sub'][1][1]) == 20
          and d['even'] == 32 and d['joint_ok'] and d['crank'] == 4 and d['orth'] == 2 and d['connects'] and d['joint_b'] == 20 and d['lost_b'] == {1: 12, 2: 0, 3: 0} and len(info['unpaired']) == 0 and d['lost'] == {1: 12, 2: 0, 3: 0} and d['adj'] == 40 and e_ok)
    return ok


if __name__ == "__main__":
    print("=== the vacuum manifold of the object's closing, and its Wilson lines (neutral fields, exact F-flat rule, paired D-flatness, Fox calculus over Q(i)) ===")
    ok = main()
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
