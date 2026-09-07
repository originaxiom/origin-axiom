#!/usr/bin/env python3
"""THE SM CLOSING'S TREE-LEVEL VACUUM (B1283): D2's space on the closing whose gauge group is the Standard Model's.

B1278 found the Standard-Model vacua of the E8 theory on Y_9: a Wilson line W valued in the order-19/38 characters of
H_1(Y_9) breaks E6 to su(3) + su(2) + u(1)_Y + u(1)_beta + u(1)' (the centralizer of a generic element of the SM's
commutant SU(2)_beta . A -- B1277 (d)), keeps three complete 27s and 27bars (568 656 full-spectrum lines) and the six
flavons of the family torus u(1)^2.  B1277 computed the tree-level vacuum manifold of the E6 theory on Y_3 and found no
SM point.  Here the same one-coupling superpotential is analysed on the SM closing, where the gauge group is already the
SM's: the D-terms of the broken E6 generators are gone (their gauge bosons are massive at the closing's scale), only
the four abelian D-terms (beta, ', and the two family charges) and the SM's own constrain the light fields.

(a) THE SM-SINGLET SECTOR.  The components of the 27 that are colour singlets with T_3 = Y = 0 are N (the SO(10)
    singlet) and nu^c; with their conjugates and the six flavons S_ij these are the 18 fields whose VEVs preserve the
    SM.  Their charges under the four U(1)s (beta = the su(2)_beta Cartan, ' = the remaining direction of the E6 Cartan
    orthogonal to the SM Cartan and to beta, and the two family charges) and the cubic monomials of W among them (the
    flavon couplings S_ij N_j Nbar_i, S_ij nu^c_j nubar^c_i and the two flavon cubics; no 27^3 monomial is purely
    singlet -- the zero-sum triples of the 27 are N h_u h_d and nu h_u nu^c).
(b) THE FLAT DIRECTIONS.  F-flatness on a coordinate subspace (exact for squarefree cubics): no monomial contains two
    switched-on fields.  D-flatness under the four U(1)s: a strictly positive combination of the switched-on fields'
    charge vectors vanishes (an LP).  All maximal D- and F-flat sets of singlets are enumerated; for each, the unbroken
    abelian rank (4 minus the rank of the charge matrix) and the surviving U(1) directions, with their charges on the SM
    fields.  The question: is there a tree-level branch on which ALL four extra U(1)s are broken, leaving exactly the
    Standard Model?
(c) THE ELECTROWEAK SECTOR ON EACH BRANCH.  The mu-terms: the 27^3 monomial d_abc 27_1 27_2 27_3 gives mu_jk = lambda
    |eps_ijk| <N_i> (B1273's zero diagonal), so the doublet mass matrix on a branch is the antisymmetric-pattern
    symmetric matrix of the N VEVs; its rank counts the heavy pairs and 3 - rank the light Higgs pairs; the same N
    gives the same matrix to the colour triplets (D, Dbar) of the 10 (doublet-triplet: one light Higgs pair comes with
    one light D pair, B1276's row 4).  The nu^c VEVs' effect through nu h_u nu^c (L-H_u mixing) is recorded.
"""
from __future__ import annotations
import sys, itertools, collections, pathlib
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.optimize import linprog

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'frontier' / 'B1277_the_vacuum_manifold_of_the_closing' / 'verification'))
import vacuum_manifold as VM
from vacuum_manifold import C, R, T, F


def setup():
    wts, rep = C.load()
    triples, idx, ns = C.solve_cubic(wts, rep)
    lab, hy, wts2 = R.sm_labels(); assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = VM.descent_data()
    rootlist = list(rts.values())
    Yv = T.sm_subalgebra()[1]
    sm_cartan = [a2[0], a2[1], a1, Yv]
    orth = [a for a in rootlist if all(ip(a, x) == 0 for x in sm_cartan)]
    assert len(orth) == 2 and orth[1] == tuple(-x for x in orth[0])
    beta = orth[0]
    # u(1)': the Cartan direction orthogonal to the SM Cartan and to beta (in the coordinates of the weights, with the form ip)
    M = sp.Matrix([[sp.Rational(x) for x in v] for v in sm_cartan + [beta]])          # 5 x 6
    G = sp.Matrix([[sp.Rational(Mf[i][j]) for j in range(6)] for i in range(6)])      # the form
    ker = (M * G).nullspace()                                                          # vectors g with ip(v, g) = 0 for all five
    assert len(ker) == 1
    gamma = tuple(F(int(x.p), int(x.q)) for x in ker[0])
    return dict(wts=wts, triples=triples, lab=lab, hy=hy, rts=rts, rootlist=rootlist, ip=ip, a1=a1, a2=a2, Yv=Yv, beta=beta, gamma=gamma, sm_cartan=sm_cartan)


def charges_on_27(D):
    """for each weight of the 27: (label, T_3, Y, q_beta, q_gamma, colour-singlet?)"""
    ip, wts, lab, hy = D['ip'], D['wts'], D['lab'], D['hy']
    out = []
    for i, w in enumerate(wts):
        colour = all(ip(s, w) == 0 for s in D['a2'])
        out.append(dict(i=i, lab=lab[i], t3=ip(D['a1'], w) / 2, Y=hy[i], qb=ip(D['beta'], w), qg=ip(D['gamma'], w), colour_singlet=colour))
    return out


def main():
    D = setup()
    ch = charges_on_27(D)
    e = {1: (1, 0), 2: (0, 1), 3: (-1, -1)}
    print("=== (a) the SM-singlet sector of the SM closing ===")
    sing = [c for c in ch if c['colour_singlet'] and c['t3'] == 0 and c['Y'] == 0]
    print(f"  SM singlets in the 27: {[(c['lab'], 'q_beta', str(c['qb']), 'q_gamma', str(c['qg'])) for c in sing]}")
    assert sorted(c['lab'] for c in sing) == ['S', 'nu^c']
    # the su(2)_beta doublet (nu^c, N): opposite beta charges, equal gamma charges
    qN = next(c for c in sing if c['lab'] == 'S'); qn = next(c for c in sing if c['lab'] == 'nu^c')
    print(f"  (N, nu^c): beta charges {qN['qb']}, {qn['qb']} (an su(2)_beta doublet: opposite), gamma charges {qN['qg']}, {qn['qg']} (equal)")
    # charges of the SM fields under beta and gamma (the Z' couplings), per label
    bylab = collections.defaultdict(set)
    for c in ch:
        bylab[c['lab']].add((str(c['qb']), str(c['qg'])))
    print(f"  (q_beta, q_gamma) of every SM field of the 27: { {k: sorted(v) for k, v in sorted(bylab.items())} }")
    # fields
    fields = {}                     # name -> charge vector (q_beta, q_gamma, fam1, fam2)
    kind = {}
    for g in (1, 2, 3):
        for c in sing:
            nm = {'S': 'N', 'nu^c': 'nu^c'}[c['lab']]
            fields[f"{nm}_{g}"] = (c['qb'], c['qg'], F(e[g][0]), F(e[g][1])); kind[f"{nm}_{g}"] = ('27', nm, g)
            fields[f"{nm}bar_{g}"] = (-c['qb'], -c['qg'], F(-e[g][0]), F(-e[g][1])); kind[f"{nm}bar_{g}"] = ('27bar', nm, g)
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            if i != j:
                fields[f"S_{i}{j}"] = (F(0), F(0), F(e[i][0] - e[j][0]), F(e[i][1] - e[j][1])); kind[f"S_{i}{j}"] = ('S', 'S', (i, j))
    names = list(fields)
    print(f"  fields: {len(names)} = 3 x 2 (N, nu^c) + 3 x 2 conjugates + 6 flavons")
    # monomials of W among the singlets (from the one-coupling cubic: S_ij 27_j 27bar_i restricted, and the flavon cubics)
    mons = []
    for i in (1, 2, 3):
        for j in (1, 2, 3):
            if i != j:
                for nm in ('N', 'nu^c'):
                    mons.append((f"S_{i}{j}", f"{nm}_{j}", f"{nm}bar_{i}"))
    mons += [("S_12", "S_23", "S_31"), ("S_21", "S_32", "S_13")]
    # no purely-singlet 27^3 monomial: check against the zero-sum triples of the 27
    zero_sum = {tuple(sorted(t)) for t in D['triples']}
    idxN = [c['i'] for c in sing]
    assert not any(tuple(sorted(t)) in zero_sum for t in itertools.combinations_with_replacement(idxN, 3))
    # every monomial is invariant under the four U(1)s (a control on the charges)
    for m in mons:
        tot = [sum(fields[x][k] for x in m) for k in range(4)]
        assert all(t == 0 for t in tot), (m, tot)
    print(f"  cubic monomials of W among the 18 singlets: {len(mons)} (12 flavon couplings S_ij X_j Xbar_i, 2 flavon cubics); all U(1)^4-invariant: True; no purely singlet 27^3 term: True")
    # ------------------------------------------------------------------ (b)
    print("\n=== (b) the D- and F-flat directions preserving the Standard Model ===")
    adj = collections.defaultdict(set)
    for m in mons:
        for x, y in itertools.combinations(m, 2):
            adj[x].add(y); adj[y].add(x)
    fmax = []

    def bk(Rs, Ps, Xs):
        if not Ps and not Xs:
            fmax.append(sorted(Rs)); return
        for v in list(Ps):
            nb = {u for u in names if u != v and u not in adj[v]}
            bk(Rs | {v}, Ps & nb, Xs & nb)
            Ps = Ps - {v}; Xs = Xs | {v}
    bk(set(), set(names), set())
    print(f"  maximal F-flat coordinate subspaces (independent sets of the co-occurrence graph): {len(fmax)}")

    def dflat_subsets(A):
        """all subsets of A that are D-flat under U(1)^4 with every magnitude positive (LP), maximal within A."""
        out = []
        for r in range(len(A), 0, -1):
            for B in itertools.combinations(A, r):
                if any(set(B) < set(C) for C in out):
                    continue
                M = np.array([[float(fields[x][k]) for x in B] for k in range(4)])
                res = linprog(c=np.zeros(len(B)), A_eq=M, b_eq=np.zeros(4), bounds=[(1, None)] * len(B), method='highs')
                if res.status == 0:
                    out.append(set(B))
        return out
    branches = set()
    for A in fmax:
        for B in dflat_subsets(A):
            branches.add(frozenset(B))
    # keep maximal ones
    branches = [b for b in branches if not any(b < c for c in branches)]
    rows = []
    for b in branches:
        M = sp.Matrix([[sp.Rational(fields[x][k].numerator, fields[x][k].denominator) for k in range(4)] for x in sorted(b)])
        rk = M.rank()
        surv = M.nullspace()                                                 # directions in charge space orthogonal to all VEVs
        kinds_b = collections.Counter(kind[x][1] + ('bar' if kind[x][0] == '27bar' else '') for x in b)
        paired = all((x.replace('bar', '') if 'bar' in x else x.replace('_', 'bar_')) in b for x in b if not x.startswith('S_')) and \
                 all(f"S_{x[-1]}{x[-2]}" in b for x in b if x.startswith('S_'))
        rows.append((len(b), 4 - rk, dict(kinds_b), paired, sorted(b), surv))
    rows.sort(key=lambda r: (r[1], -r[0], str(r[4])))
    print(f"  maximal D&F-flat SM-preserving branches: {len(rows)}")
    min_rank = min(r[1] for r in rows)
    for n, srank, kb, paired, b, surv in rows:
        print(f"    {n} fields, surviving extra u(1)s: {srank}, conjugate-paired: {paired}, content {kb}: {b}")
    exactly_sm = [r for r in rows if r[1] == 0]
    print(f"  branches breaking all four extra U(1)s (exactly the SM at tree level): {len(exactly_sm)}; minimal surviving abelian rank: {min_rank}")
    # the surviving U(1) on the rank-1 branches: its charges on the SM fields
    print("\n  the surviving U(1) on each minimal-rank branch, as charges on (N, nu^c, Q, u^c, d^c, L, e^c, H_u, H_d, D, Dbar) [times the family part]:")
    sm_labels = ['S', 'nu^c', 'Q', 'u^c', 'd^c', 'L', 'e^c', 'H_u', 'H_d', 'D', 'Dbar']
    lab_charge = {}
    for c in ch:
        lab_charge.setdefault(c['lab'], set()).add((c['qb'], c['qg']))
    zprimes = set()
    for n, srank, kb, paired, b, surv in rows:
        if srank != min_rank:
            continue
        for v in surv:
            v = list(v)
            # normalise: make the E6-part primitive
            v = [sp.Rational(x) for x in v]
            den = sp.ilcm(*[x.q for x in v]) if any(v) else 1
            v = [x * den for x in v]
            gcd = sp.igcd(*[int(x) for x in v if x != 0]) if any(v) else 1
            v = [int(x) // gcd for x in v]
            zq = {}
            for L in sm_labels:
                qs = {v[0] * qb + v[1] * qg for (qb, qg) in lab_charge.get(L, set())}
                zq[L] = sorted(str(q) for q in qs)
            key = (tuple(v), tuple(sorted((k, tuple(val)) for k, val in zq.items())))
            if key not in zprimes:
                zprimes.add(key)
                print(f"    branch {b}: Z' = {v[0]} beta + {v[1]} gamma + ({v[2]}, {v[3]}) family; charges {zq}")
    # ------------------------------------------------------------------ (c)
    print("\n=== (c) the electroweak sector on each branch: mu-terms from the N VEVs ===")
    light = collections.Counter()
    for n, srank, kb, paired, b, surv in rows:
        Ns = [g for g in (1, 2, 3) if f"N_{g}" in b or f"Nbar_{g}" in b]
        Nvev = {g: (sp.Symbol(f"v{g}") if g in Ns else 0) for g in (1, 2, 3)}
        Mu = sp.Matrix(3, 3, lambda j, k: 0 if j == k else Nvev[[g for g in (1, 2, 3) if g not in (j + 1, k + 1)][0]])
        rk = Mu.rank()
        light[(tuple(Ns), 3 - rk)] += 1
    print(f"  (generations with <N> != 0, light Higgs doublet pairs = light D pairs at tree level) -> number of branches: {dict(sorted(light.items()))}")
    # moduli: one complex modulus per conjugate pair (the invariant X Xbar); the E6 identification of gamma from the
    # printed charges: gamma = -(5/12) psi + (1/4) chi with psi (16: 1, 10: -2, 1: 4) and chi (10 of the 16: -1, 5bar: 3,
    # 1: -5; 5 of the 10: 2, 5bar: -2, N: 0) -- checked on every SM field
    psi = {'Q': 1, 'u^c': 1, 'e^c': 1, 'd^c': 1, 'L': 1, 'nu^c': 1, 'H_u': -2, 'D': -2, 'H_d': -2, 'Dbar': -2, 'S': 4}
    chi = {'Q': -1, 'u^c': -1, 'e^c': -1, 'd^c': 3, 'L': 3, 'nu^c': -5, 'H_u': 2, 'D': 2, 'H_d': -2, 'Dbar': -2, 'S': 0}
    gamma_ok = all(lab_charge[L] == {(next(iter(lab_charge[L]))[0], F(-5, 12) * psi[L] + F(1, 4) * chi[L])} for L in sm_labels)
    beta_ok = all(all(qb == F(psi[L] + chi[L], 4) for (qb, qg) in lab_charge[L]) for L in sm_labels)
    print(f"  E6 identification of the two extra Cartan directions on every SM field: gamma = -(5/12) psi + (1/4) chi: {gamma_ok}; beta = (psi + chi)/4: {beta_ok}")
    print(f"  so the surviving Z' on the maximal branches has E6 part -6 gamma = (5 psi - 3 chi)/2 (charges 4 on the 10 of the 16, -2 on its 5bar, 10 on nu^c and N, -8 on (H_u, D), -2 on (H_d, Dbar)), mixed with the family torus")
    moduli = {tuple(sorted(r[4])): sum(1 for x in r[4] if not ('bar' in x) and not (x.startswith('S_') and x[-1] < x[-2])) for r in rows}
    print(f"  complex moduli per branch (one per conjugate pair): {sorted(collections.Counter(moduli.values()).items())}   (3 on the three maximal branches: <N N-bar>, <nu^c nu^c-bar>, <S S>)")
    nu_branches = sum(1 for r in rows if any(x.startswith('nu^c') for x in r[4]))
    print(f"  branches with a nu^c VEV (nu h_u nu^c then mixes L with H_u at the VEV scale): {nu_branches} of {len(rows)}")
    ok = (len(exactly_sm) == 0 and min_rank == 1 and len(rows) == 9 and all(r[3] for r in rows) and gamma_ok and beta_ok
          and all(k[1] >= 1 for k in light if len(k[0]) <= 2) and all(k[1] == 0 for k in light if len(k[0]) == 3))
    return dict(rows=rows, exactly_sm=len(exactly_sm), min_rank=min_rank, light=dict(light), n_fmax=len(fmax), ok=ok, gamma_ok=gamma_ok, beta_ok=beta_ok, moduli=moduli)


if __name__ == "__main__":
    out = main()
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
