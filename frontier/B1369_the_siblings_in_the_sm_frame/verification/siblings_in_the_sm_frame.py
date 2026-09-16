#!/usr/bin/env python3
"""B1369 -- THE SIBLINGS IN THE STANDARD-MODEL FRAME (sL-1): can a member of the figure-eight's family supply, from bulk matter with the
Standard Model unbroken, the chiral generation that m004 withholds?

The frame (B1351, B1368): a flat E6(C) connection commuting with the Standard Model has its non-abelian part in SL(2)_beta and a
character chi of H_1(M) on the two Cartan directions (Y, gamma); every bulk sector is an SL(2)_beta spin times a character chi_w.  A sector
carries a chiral index only if it is cusp-fixed on some cusp and non-unitary there.  Two lemmas decide the spin-0 half on any member:
  * one cusp: cusp-fixed <=> chi_w trivial <=> no Higgs field (B1368);
  * several cusps: cusp-fixed on cusp i <=> chi_w trivial on the peripheral subgroup P_i < H_1(M); if P_i has full rank in H_1 (x) Q,
    chi_w has finite order, the sector is unitary and vector-like.  Only a cusp with a rank-deficient peripheral image can host a
    non-unitary cusp-fixed spin-0 sector.
And the spin split (B1368): the 10 and the 5bar of SU(5) never share a spin.  So a member can give a full generation from bulk matter only
if it has a cusp with rank-deficient peripheral image.  This script:
  (A) sweeps B1186's 112 family members (SnapPy): cusps, H_1, the rank of each cusp's peripheral image in H_1 (x) Q, the SL(2,C) lift's
      traces on the meridian and longitude of each cusp (one-cusped members: Calegari's -2 on the longitude);
  (B) details m202 and s959: peripheral classes, indices, the lift's traces, the isometry group's action on the cusps;
  (C) on m202, whether the spin-1/2 half (a full 10 of SU(5) in the 78-frame; the 5bar + nu^c in the 27-frame) can be cusp-fixed on a cusp
      with the Standard Model unbroken -- the characters trivial on P_0 that keep the 22 non-SM roots of SU(6) non-trivial;
  (E) on every member with a free cusp, every isometry fixing that cusp (the combinatorial automorphisms of the canonical
      retriangulation, family_isometries.py) with its exact action on H_1(M; Q), on the free classes ann(P_c) and on the cusp torus;
      the region-swap parity: an isometry fixing the cusp and negating every free class gives N = 0 on that cusp;
  (F) the residual cusps parity leaves open, with their cusp lattices;
  (D) the verdict of the family in this frame.
Usage: python3 siblings_in_the_sm_frame.py  (about a minute)"""
import json, itertools, warnings
warnings.filterwarnings("ignore")
from fractions import Fraction as Fr
import sympy as sp
import snappy

def sm2(cm):
    """a SnapPy 2x2 cusp map as a sympy integer matrix"""
    try:
        return sp.Matrix([[int(cm[i, j]) for j in range(2)] for i in range(2)])
    except Exception:
        return sp.Matrix([[int(cm[i][j]) for j in range(2)] for i in range(2)])
def abelianise(word, gens):
    v = [0] * len(gens)
    for ch in word:
        i = gens.index(ch.lower()); v[i] += 1 if ch.islower() else -1
    return v
def peripheral_data(M):
    G = M.fundamental_group()
    gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    rank_R = R.rank() if rels else 0
    b1 = len(gens) - rank_R
    out = []
    for (mu, lam) in G.peripheral_curves():
        P = sp.Matrix([abelianise(mu, gens), abelianise(lam, gens)])
        stacked = sp.Matrix.vstack(R, P) if rels else P
        rank_P = stacked.rank() - rank_R           # rank of the peripheral image in H_1 (x) Q
        out.append((mu, lam, abelianise(mu, gens), abelianise(lam, gens), rank_P))
    return gens, rels, b1, out
def lift_traces(M):
    try:
        G = M.fundamental_group()
        res = []
        for (mu, lam) in G.peripheral_curves():
            res.append((complex(G.SL2C(mu).trace()), complex(G.SL2C(lam).trace())))
        return res
    except Exception as e:
        return None

# ---------------------------------------------------------------- (A) the family sweep
fam = json.load(open(__file__.rsplit('/', 4)[0] + '/frontier/B1186_family_is_112/verification/family_census.json'))
members = fam['members_B']; membersA = set(fam['members_A'])
print(f"=== (A) the family: {len(members)} members (B1186; {len(membersA)} regular-tetrahedral) ===")
rows = []; deficient = []; one_cusped_lambda = []
for name in members:
    M = snappy.Manifold(name)
    gens, rels, b1, per = peripheral_data(M)
    tr = lift_traces(M)
    ranks = [p[4] for p in per]
    rows.append((name, M.num_cusps(), str(M.homology()), b1, ranks, tr))
    for c, p in enumerate(per):
        if p[4] < b1: deficient.append((name, c, p[4], b1, str(M.homology())))
    if M.num_cusps() == 1 and tr is not None:
        one_cusped_lambda.append((name, round(tr[0][1].real, 6), round(tr[0][1].imag, 6), per[0][3]))
from collections import Counter
print(f"  cusp counts: {dict(Counter(r[1] for r in rows))}")
print(f"  free cusps -- peripheral image of rank < b_1 in H_1 (x) Q, the only cusps that can host a non-unitary cusp-fixed spin-0 sector: {len(deficient)} cusps on {len(set(d[0] for d in deficient))} members")
for d in deficient: print(f"    {d[0]:10s} cusp {d[1]}: peripheral rank {d[2]} < b_1 = {d[3]} (H_1 = {d[4]})")
candidates = sorted(set(d[0] for d in deficient))
print(f"  candidate members (a free cusp exists): {candidates}")
one = [r for r in rows if r[1] == 1]; multi = [r for r in rows if r[1] >= 2]
one_b1_1 = [r[0] for r in one if r[3] == 1]; one_b1_2 = [r[0] for r in one if r[3] >= 2]
multi_full = [r[0] for r in multi if all(k == r[3] for k in r[4])]
print(f"  one-cusped members: {len(one)}: {len(one_b1_1)} have b_1 = 1 = the peripheral rank (no free cusp); {len(one_b1_2)} have b_1 = 2 with a peripheral image of rank 1 (a free cusp): {one_b1_2}")
print(f"  multi-cusped members ({len(multi)}): {len(multi_full)} have every peripheral rank equal to b_1 (no free cusp; m202 and s959 among them: {[r[4] for r in multi if r[0] in ('m202', 's959')]}), {len(multi) - len(multi_full)} have a free cusp")
no_free = one_b1_1 + multi_full
assert len(no_free) + len(candidates) == len(members) and not set(no_free) & set(candidates)
print(f"  members without a free cusp: {len(no_free)} of {len(members)}; with a free cusp: {len(candidates)}")
print(f"  multi-cusped members: name, cusps, H_1, b_1, peripheral ranks per cusp:")
for r in multi: print(f"    {r[0]:10s} cusps {r[1]} H_1 {r[2]:>22s} b_1 {r[3]} ranks {r[4]}")
# the longitude census of the one-cusped members: is SnapPy's longitude rationally null-homologous, and what is its lifted trace?
def rationally_null(name, vec):
    M = snappy.Manifold(name); G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    return (sp.Matrix.vstack(R, sp.Matrix([vec])).rank() == R.rank()) if rels else not any(vec)
def in_lattice(R, v):
    """is the integer vector v in the Z-row space of the integer matrix R? (integer row reduction)"""
    rows = [list(map(int, R.row(i))) for i in range(R.rows)]; v = list(map(int, v)); n = len(v)
    basis = []
    for col in range(n):
        piv = None
        for r in rows:
            if r[col] != 0 and all(x == 0 for x in r[:col]):
                piv = r if piv is None else piv
        if piv is None: continue
        # Euclid on the pivot column among the rows with zeros before col
        cand = [r for r in rows if r[col] != 0 and all(x == 0 for x in r[:col])]
        while len(cand) > 1:
            cand.sort(key=lambda r: abs(r[col]))
            a = cand[0]
            for r in cand[1:]:
                q = r[col] // a[col]
                for k in range(n): r[k] -= q * a[k]
            cand = [r for r in cand if r[col] != 0]
            cand = [cand[0]] + [r for r in cand[1:]] if cand else []
            if len(cand) > 1:
                continue
        if cand:
            piv = cand[0]; basis.append(piv); rows = [r for r in rows if r is not piv]
    # reduce v
    for piv in basis:
        col = next(k for k in range(n) if piv[k] != 0)
        if v[col] % piv[col] != 0: return False
        q = v[col] // piv[col]
        for k in range(n): v[k] -= q * piv[k]
    return all(x == 0 for x in v)
def integrally_null(name, vec):
    M = snappy.Manifold(name); G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    return in_lattice(R, vec) if rels else not any(vec)
lam_null = [(t[0], t[1]) for t in one_cusped_lambda if rationally_null(t[0], t[3])]
lam_int = [(t[0], t[1]) for t in one_cusped_lambda if integrally_null(t[0], t[3])]
lam_non = [(t[0], t[1]) for t in one_cusped_lambda if not rationally_null(t[0], t[3])]
print(f"  one-cusped members: SnapPy's longitude rationally null-homologous on {len(lam_null)} (lifted traces {dict(Counter(t[1] for t in lam_null))}), of which integrally null-homologous (in the commutator subgroup) on {len(lam_int)} (traces {dict(Counter(t[1] for t in lam_int))}: Calegari's -2 on every one of these); not null-homologous on {len(lam_non)} (traces {dict(Counter(t[1] for t in lam_non))}) -- on a torsion or non-null class the lift's sign is a choice")
assert all(t[1] == -2.0 for t in lam_int), "Calegari's -2 fails on an integrally null-homologous longitude"

# ---------------------------------------------------------------- (B) the siblings
print("\n=== (B) the two-cusped siblings m202 and s959 ===")
for name in ["m202", "s959"]:
    M = snappy.Manifold(name)
    gens, rels, b1, per = peripheral_data(M); tr = lift_traces(M)
    print(f"  {name}: H_1 = {M.homology()}, generators {gens}, relators {rels}")
    for c, (mu, lam, amu, alam, rk) in enumerate(per):
        idx = abs(sp.Matrix([amu, alam]).det()) if len(gens) == 2 else None
        print(f"    cusp {c}: mu = {mu} -> {amu}, lambda = {lam} -> {alam}; peripheral rank {rk}" + (f", index of P_{c} in H_1 = {idx}" if idx is not None else "") + f"; lift traces (mu, lambda) = ({tr[c][0].real:+.3f}, {tr[c][1].real:+.3f})")
    S = M.symmetry_group()
    swaps = sum(1 for iso in S.isometries() if list(iso.cusp_images()) != [0, 1])
    rot3 = [iso for iso in S.isometries() if list(iso.cusp_images()) == [0, 1] and all(abs((sm2(cm) - sp.eye(2)).det()) == 3 for cm in iso.cusp_maps())]
    print(f"    isometries: {S.order()} ({S}), cusp-swapping: {swaps}, cusp-fixing with |det(A - I)| = 3 on both cusps (the order-3 rotation of B1321): {len(rot3)}")

# ---------------------------------------------------------------- (C) m202: can the spin-1/2 half be cusp-fixed with the SM unbroken?
print("\n=== (C) m202: the spin-1/2 half on cusp 0, with the Standard Model unbroken ===")
def roots_e6():
    R = []
    for i in range(5):
        for j in range(i + 1, 5):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [Fr(0)] * 5; v[i] = Fr(si); v[j] = Fr(sj); R.append((tuple(v), Fr(0)))
    for signs in itertools.product((1, -1), repeat=5):
        if signs.count(-1) % 2 == 0:
            w = tuple(Fr(s, 2) for s in signs); R.append((w, Fr(1))); R.append((tuple(-x for x in w), Fr(-1)))
    return R
def dot(a, b): return sum(x * y for x, y in zip(a[0], b[0])) + Fr(3, 4) * a[1] * b[1]
def vec(*xs): return (tuple(Fr(x) for x in xs[:5]), Fr(xs[5]))
R = roots_e6()
sm_roots = [vec(1,-1,0,0,0,0), vec(-1,1,0,0,0,0), vec(0,1,-1,0,0,0), vec(0,-1,1,0,0,0), vec(1,0,-1,0,0,0), vec(-1,0,1,0,0,0), vec(0,0,0,1,-1,0), vec(0,0,0,-1,1,0)]
Y = vec(Fr(-1,3), Fr(-1,3), Fr(-1,3), Fr(1,2), Fr(1,2), 0); beta = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), 1); gamma = vec(Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(1,2), Fr(-5, 3))
perp = [r for r in R if dot(r, beta) == 0]; nonsm = [r for r in perp if r not in sm_roots]
doublets78 = [r for r in R if dot(r, beta) == 1]            # one weight per spin-1/2 doublet of the 78
def sm_type(w):
    col = any(dot(w, s) != 0 for s in sm_roots[:6]); wk = dot(w, sm_roots[6]) != 0
    return (col, wk, dot(Y, w))
ten = [r for r in doublets78 if (sm_type(r)[0], sm_type(r)[1], abs(sm_type(r)[2])) in [(True, True, Fr(1,6)), (True, False, Fr(2,3)), (False, False, Fr(1))] and dot(Y, r) * (1 if sm_type(r)[0] or sm_type(r)[1] else 1) is not None]
# the 10 of SU(5) inside the (2,20): pick the weights with (Q-type: colour doublet Y = 1/6), (u^c-type: colour singlet Y = -2/3), (e^c-type: (1,1) Y = 1) -- one 10 (the 10bar has opposite Y)
ten = [r for r in doublets78 if (sm_type(r) == (True, True, Fr(1,6))) or (sm_type(r) == (True, False, Fr(-2,3))) or (sm_type(r) == (False, False, Fr(1)))]
print(f"  weights of one 10 of SU(5) in the (2,20) of the 78: {len(ten)} (Q-type 6, u^c-type 3, e^c-type 1); their (Y, gamma): {sorted(set((str(dot(Y, r)), str(dot(gamma, r))) for r in ten))}")
# the character of H_1(m202) = Z^2 on a weight w: chi_w(g) = exp(2 pi i (s(g) Y_w + t(g) gamma_w)), s, t in Hom(H_1, C); cusp-fixed on cusp 0 <=> chi_w trivial on P_0
M = snappy.Manifold("m202"); gens, rels, b1, per = peripheral_data(M)
P0 = [per[0][2], per[0][3]]        # the classes of mu_0, lambda_0 in Z^2 = H_1
# unknowns: s_a, s_b, t_a, t_b (the values of s, t on the generators a, b); conditions for each p in P0 and each weight w of the 10: p.s * Y_w + p.t * gamma_w in Z
sa, sb, ta, tb = sp.symbols('s_a s_b t_a t_b')
def s_of(p): return p[0] * sa + p[1] * sb
def t_of(p): return p[0] * ta + p[1] * tb
# the three (Y, gamma) types of the 10 all have gamma = -2/3 and Y in {1/6, -2/3, 1}: conditions per p: s(p) Y + t(p) gamma in Z for the three Y
# differences give (5/6) s(p) in Z and s(p) - (2/3) t(p) in Z: s(p) in (6/5) Z, t(p) in (3/2)(s(p) - Z)
sols = []
for n1, n2 in itertools.product(range(-3, 4), repeat=2):      # s(p0) = 6 n1 / 5, s(p1) = 6 n2 / 5
    for m1, m2 in itertools.product(range(-2, 3), repeat=2):
        sp0, sp1 = sp.Rational(6 * n1, 5), sp.Rational(6 * n2, 5)
        tp0, tp1 = sp.Rational(3, 2) * (sp0 - m1), sp.Rational(3, 2) * (sp1 - m2)
        sol = sp.solve([sp.Eq(s_of(P0[0]), sp0), sp.Eq(s_of(P0[1]), sp1), sp.Eq(t_of(P0[0]), tp0), sp.Eq(t_of(P0[1]), tp1)], [sa, sb, ta, tb], dict=True)
        if not sol: continue
        S = sol[0]
        # the 10's weights are all cusp-fixed on cusp 0 by construction; check exactly
        ok10 = all(all(sp.simplify(s_of(p).subs(S) * sp.Rational(dot(Y, w).numerator, dot(Y, w).denominator) + t_of(p).subs(S) * sp.Rational(dot(gamma, w).numerator, dot(gamma, w).denominator)).q == 1 for p in P0) for w in ten)
        # the Standard Model unbroken: every one of the 22 non-SM roots must carry a non-trivial character on H_1 = <a, b>
        def char_trivial(w):
            return all(sp.simplify(sp.Rational(1) * (g_s * sp.Rational(dot(Y, w).numerator, dot(Y, w).denominator) + g_t * sp.Rational(dot(gamma, w).numerator, dot(gamma, w).denominator))).q == 1 for g_s, g_t in [(S[sa], S[ta]), (S[sb], S[tb])])
        broken = all(not char_trivial(r) for r in nonsm)
        order = 1
        vals = [S[sa], S[sb], S[ta], S[tb]]
        sols.append((n1, n2, m1, m2, ok10, broken, [str(v) for v in vals]))
good = [s for s in sols if s[4] and s[5]]
print(f"  characters with the whole 10 cusp-fixed on cusp 0 (a grid of {len(sols)} solutions): {len(good)} keep all 22 non-SM roots non-trivial (Standard Model unbroken)")
if good:
    g = good[0]; print(f"    example: (s_a, s_b, t_a, t_b) = {g[6]} -- rational: the character has finite order (unitary), as the full rank of P_0 forces; the spin-1/2 half can be cusp-fixed on cusp 0 with the SM unbroken")
# is the character then trivial on cusp 1 as well (which would make it trivial)? P_0 + P_1 = H_1?
P1 = [per[1][2], per[1][3]]
lat = sp.Matrix([P0[0], P0[1], P1[0], P1[1]])
from sympy.matrices.normalforms import smith_normal_form
print(f"  P_0 + P_1 = H_1: index of the sum = {abs(smith_normal_form(lat.T, domain=sp.ZZ)[0, 0] * smith_normal_form(lat.T, domain=sp.ZZ)[1, 1])} (1 means the two cusps' peripheral classes generate H_1: a character trivial on both cusps is trivial)")
# the spin-0 half on m202: a spin-0 sector cusp-fixed on cusp i has chi_w trivial on P_i, hence of order dividing the index 7: unitary
print(f"  spin-0 sectors: cusp-fixed on cusp i <=> chi_w trivial on P_i (index 7) <=> chi_w^7 = 1: a unitary local system, vector-like (h^1(L) = h^1(Lbar)); the 5bar (78-frame) and the 10 (27-frame) are never chiral on m202")

# ---------------------------------------------------------------- (E) the free cusps: the isometries' exact action on H_1 and the region-swap parity
print("\n=== (E) the candidates: every isometry fixing a free cusp, its action on the cusp torus and on the free classes (canonical retriangulation) ===")
print("  lemma (fc R71's region-swap, torus action general): an isometry fixing cusp c and acting by -1 on ann(P_c) < H^1(M; Q) maps {F > 0} onto {F < 0}")
print("  for the leading cusp mode F of every harmonic 1-form with vanishing periods on P_c, so chi(d+) = chi(d-) = 0: N = 0 for every cusp-fixed spin-0 sector on c")
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family_isometries import FamilyMember
def h1_data(M):
    G = M.fundamental_group(); gens = list(G.generators()); rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    ns = R.nullspace() if rels else [sp.eye(len(gens))[:, k] for k in range(len(gens))]
    Q = sp.Matrix.hstack(*ns).T if ns else sp.zeros(0, len(gens))          # rows: a basis of Hom(H_1, Q); pi(v) = Q v
    per = G.peripheral_curves()
    P = [(Q * sp.Matrix(abelianise(mu, gens)), Q * sp.Matrix(abelianise(lam, gens))) for (mu, lam) in per]
    return Q, P
def cusp_map_method(M, c, i, Q, P, isos):
    """the earlier instrument: the induced action on H_1 (x) Q inferred from SnapPy's cusp maps, possible only when the peripheral classes span H_1"""
    b1 = Q.rows
    Pi = sp.Matrix.hstack(P[i][0], P[i][1]); ann = Pi.T.nullspace()
    out = []
    for iso in isos:
        if list(iso.cusp_images())[i] != i: continue
        perm = list(iso.cusp_images()); maps = [sm2(cm) for cm in iso.cusp_maps()]
        Ai = maps[i]
        typ = "I" if Ai == sp.eye(2) else ("-I" if Ai == -sp.eye(2) else (f"order-{[k for k in (2,3,4,6) if (Ai**k) == sp.eye(2)][0]}" if any((Ai**k) == sp.eye(2) for k in (2,3,4,6)) else "?"))
        gstar = None
        for conv in (0, 1):
            src = []; dst = []
            for j in range(c):
                A = maps[j] if conv == 0 else maps[j].T
                mu_j, lam_j = P[j]; k = perm[j]; mu_k, lam_k = P[k]
                src += [mu_j, lam_j]; dst += [A[0, 0] * mu_k + A[1, 0] * lam_k, A[0, 1] * mu_k + A[1, 1] * lam_k]
            Src = sp.Matrix.hstack(*src); Dst = sp.Matrix.hstack(*dst)
            if sp.Matrix.vstack(Src, Dst).rank() == Src.rank():
                cols = []
                for kcol in range(Src.cols):
                    trial = cols + [kcol]
                    if Src[:, trial].rank() == len(trial): cols = trial
                    if len(cols) == b1: break
                gst = Dst[:, cols] * Src[:, cols].inv()
                if (gst * Src - Dst) == sp.zeros(b1, Src.cols) and gst.det() in (1, -1):
                    gstar = gst; break
        if gstar is None:
            out.append((typ, "undetermined")); continue
        act = [gstar.T * f for f in ann]
        neg = all((a + f) == sp.zeros(b1, 1) for a, f in zip(act, ann)); pos = all((a - f) == sp.zeros(b1, 1) for a, f in zip(act, ann))
        out.append((typ, "negated" if neg else ("fixed" if pos else "mixed")))
    return out
def reduce_tau(t):
    t = complex(t)
    if t.imag < 0: t = -t.conjugate()
    for _ in range(500):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12: t = -1 / t
        else: break
    return t
parity_rows = []; residual = []; cross_checks = 0
rank_by_name = {r[0]: r[4] for r in rows}
for name in candidates:
    FM = FamilyMember(name)
    M = FM.M; c = FM.num_cusps
    assert FM.b1 == [r for r in rows if r[0] == name][0][3], f"{name}: b_1 disagrees with SnapPy's fundamental group"
    my_ranks = [FM.cusp[k]['rankP'] for k in range(c)]
    assert my_ranks == rank_by_name[name], f"{name}: peripheral ranks {my_ranks} differ from SnapPy's {rank_by_name[name]} (cusp numbering)"
    S = M.symmetry_group(); isos = S.isometries()
    assert len(FM.auts) == S.order(), f"{name}: {len(FM.auts)} automorphisms vs |Isom| = {S.order()}"
    Q, P = h1_data(M)
    spans_all = sp.Matrix.hstack(*[v for pair in P for v in pair]).rank() == FM.b1
    print(f"  {name}: cusps {c}, b_1 {FM.b1}, ranks {my_ranks}, |Isom| {S.order()} = |Aut(canonical retriangulation)| {len(FM.auts)}, tetrahedra {FM.n}, peripheral classes span H_1: {spans_all}")
    verdicts = []
    for k in range(c):
        if FM.cusp[k]['free'] == 0: continue
        fixers, closed_general, closed_pmI = FM.analyse_cusp(k)
        summary = sorted(Counter((r['torus'], r['on_free'], r['orientation']) for r in fixers).items())
        # cross-check against the cusp-map inference where it applies
        note = ""
        if spans_all:
            old = cusp_map_method(M, c, k, Q, P, isos)
            mine = sorted((r['torus'].replace(" (det -1)", ""), r['on_free']) for r in fixers)
            agree = sorted(old) == mine
            cross_checks += 1
            note = f"; cusp-map inference agrees: {agree}"
            assert agree, f"{name} cusp {k}: cusp-map inference {sorted(old)} vs direct {mine}"
        # the -1 eigenspace of the fixers on ann(P_c): the sub-family of Higgs classes closed by parity
        ann = FM.cusp[k]['ann']; d = len(ann)
        neg_dims = []
        for r in fixers:
            Amat = r['A']
            annM = sp.Matrix.hstack(*ann)
            # action on ann in the basis ann: solve annM X = A^T annM
            X = (annM.T * annM).inv() * annM.T * (Amat.T * annM)
            neg_dims.append(d - (X + sp.eye(d)).rank())
        verdict = "N = 0 by parity (an isometry fixes the cusp and negates every free class)" if closed_general else "parity silent on some free class: the partition must be computed"
        if not closed_general: residual.append((name, k, d, max(neg_dims)))
        verdicts.append((k, d, len(fixers), summary, closed_general, closed_pmI, max(neg_dims), verdict))
        print(f"    free cusp {k} (free classes {d}), isometries fixing it {len(fixers)}: {summary}{note}")
        print(f"      largest -1-eigenspace of a fixer on the free classes: {max(neg_dims)} of {d} -> {verdict}" + ("" if closed_general == closed_pmI else " (closed only by the general lemma: the closing isometry's torus action is not +-I)"))
    parity_rows.append((name, c, FM.b1, my_ranks, S.order(), verdicts))
closed = [(r[0], v[0]) for r in parity_rows for v in r[5] if v[4]]
closed_pmI = [(r[0], v[0]) for r in parity_rows for v in r[5] if v[5]]
silent = [(r[0], v[0]) for r in parity_rows for v in r[5] if not v[4]]
print(f"  free cusps: {len(closed) + len(silent)}; closed by parity: {len(closed)} (of which {len(closed_pmI)} already by an isometry acting on the torus by +-I, R71's form; {len(closed) - len(closed_pmI)} need the general lemma); parity silent: {len(silent)}: {silent}")
print(f"  cross-checks of the direct action against the cusp-map inference: {cross_checks} cusps, all agree")

# ---------------------------------------------------------------- (F) the residual: the cusps parity leaves open
print("\n=== (F) the residual free cusps: the fixers' -1-eigenspaces and the cusp lattices ===")
for (name, k, d, negdim) in residual:
    M = snappy.Manifold(name); tau = reduce_tau(M.cusp_info()[k]['modulus'])
    shortest_unique = abs(abs(tau) - 1) > 1e-9
    print(f"  {name} cusp {k}: free classes {d}, a fixer negates a subspace of dimension {negdim} (the Higgs classes there are closed; the rest open); reduced cusp modulus {tau.real:+.6f} {tau.imag:+.6f}i, |tau| = {abs(tau):.6f}: shortest dual vector unique: {shortest_unique}")
print("  on a cusp whose lattice has a unique shortest dual vector, a harmonic form's leading cusp mode is cos(2 pi k.x + phase) when its coefficient is non-zero: an annular partition, N = 0;")
print("  whether that coefficient vanishes is the harmonic form's cusp expansion, not computed here -- the residual of sL-1.")

# ---------------------------------------------------------------- (D) the verdict
print("\n=== (D) the family in the Standard-Model frame ===")
print(f"  members without a free cusp: {len(no_free)} of {len(members)} ({len(one_b1_1)} one-cusped with b_1 = 1; {len(multi_full)} multi-cusped with full peripheral ranks, m202 and s959 among them):")
print("    every cusp-fixed spin-0 sector is unitary, its Higgs field vanishes, N = 0; with the spin split (the 10 and the 5bar never share a spin) no full generation from bulk matter with the Standard Model unbroken, for every flat connection.")
print(f"  members with a free cusp: {len(candidates)}, carrying {len(closed) + len(silent)} free cusps: parity closes {len(closed)} (the exact action of the isometries on H_1); {len(silent)} remain: {silent} -- the residual of sL-1.")
print(f"  members fully closed (no free cusp, or every free cusp closed by parity): {len(members) - len(set(n for n, k in silent))} of {len(members)}; members with an open cusp: {sorted(set(n for n, k in silent))}")
print("DONE")
