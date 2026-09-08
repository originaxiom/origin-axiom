#!/usr/bin/env python3
"""THE TRIPLET'S PROTECTION (B1300, part b): why no Wilson line of Y_9 splits the doublets from the triplets -- the exact
structural model of B1278's enumeration, in seconds, and the theorem behind the count.

B1278 proved that the characters psi of H_1(Y_9) = (Z/76)^2 with h^1(Y_9; psi) = 1 are exactly ((C_1 u C_2) x V_4) minus
the identity, where C_1, C_2 are two cyclic subgroups of order 19 of the 19-part (Z/19)^2 and V_4 = {1, chi_1, chi_2, chi_3}
is the group of the three family characters (order 2).  Every other character has h^1 = 0.  A component c of the 27 on
which the SM-commuting Wilson line W acts by the character psi_c survives in generation g iff h^1(chi_g psi_c) = 1, so its
multiplicity is m(c) = #{g : chi_g psi_c in the support}: 3 if the 19-part of psi_c is a non-trivial element of C_1 u C_2;
3 if psi_c = 1; 2 if psi_c is a family character (that generation is projected); 0 if its 19-part lies outside C_1 u C_2.
W is determined by the characters (psi_Q, psi_u, psi_L) (B1278: the weights of Q, u^c, L are a Z-basis of P/Q_SM), and
every other component's character is the corresponding integer combination -- the coefficients are the weights of the
27 modulo the SM roots, read off B1278's Smith form (free coordinates 3, 4, 5) and re-derived here from the eight cubic
couplings of the 27 (Q Q D, u^c e^c D, d^c nu^c D, Q L Dbar, u^c d^c Dbar, Q u^c H_u, Q d^c H_d, L e^c H_d, L nu^c H_u,
N H_u H_d, N D Dbar).  Everything B1278 and B1300(a) counted follows from this model with no Fox calculus at all, and
the model is where the theorem lives:

    THE TRIPLET'S PROTECTION.  w_D = -2 w_Q modulo the SM roots (the diquark coupling Q Q D), so psi_D = psi_Q^-2.
    Three generations of Q put psi_Q in the alphabet K3 = {1} u ((C_1 u C_2) minus 1) x V_4, whose elements have order
    1, 19 or 38; the square of such a character has odd order (1 or 19) and lies in the same C_a, so psi_D is again in
    K3 and never a family character: D survives in all three generations on EVERY three-generation line.  The family
    group is 2-torsion and D's weight is twice a weight: the Wilson line cannot see D with the family characters, which
    are the only characters that project anything.

Run with --verify-weights to re-derive the coordinate table from B1278's own loaders (about two minutes).
"""
from __future__ import annotations
import sys, time, collections, itertools, pathlib
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]

LABELS = ('Q', 'u^c', 'd^c', 'L', 'e^c', 'H_u', 'H_d', 'D', 'Dbar', 'S', 'nu^c')
# the weights of the 27 modulo the SM roots: B1278's Smith-form coordinates (free coordinates 3, 4, 5 of V^T w), one row
# per SM multiplet (all members of a multiplet agree, as they must); 'S' is the SO(10) singlet N
SMITH_COORDS = {'Q': (-1, 0, 0), 'u^c': (-1, 0, 1), 'd^c': (0, 1, -1), 'L': (0, 1, 0), 'e^c': (-1, 0, -1),
                'H_u': (2, 0, -1), 'H_d': (1, -1, 1), 'D': (2, 0, 0), 'Dbar': (1, -1, 0), 'S': (-3, 1, 0), 'nu^c': (-2, -1, 1)}
# the cubic couplings of the 27 (zero-sum weight triples), each a relation among the multiplets' weights
CUBICS = [('Q', 'Q', 'D'), ('u^c', 'e^c', 'D'), ('d^c', 'nu^c', 'D'), ('Q', 'L', 'Dbar'), ('u^c', 'd^c', 'Dbar'),
          ('Q', 'u^c', 'H_u'), ('Q', 'd^c', 'H_d'), ('L', 'e^c', 'H_d'), ('L', 'nu^c', 'H_u'), ('S', 'H_u', 'H_d'), ('S', 'D', 'Dbar')]
# B1278's counts on Y_9 and B1300(a)'s histogram (the pipeline's re-enumeration), to be reproduced by the model
B1278 = dict(k3=145, k2=3, three_gen=758593, su5_broken=737568, sm_vacua=706464, full=568656)
B1300A_HIST = {(2, 2, 3, 3): 1296, (2, 3, 3, 2): 1296, (2, 3, 3, 3): 27648, (3, 2, 3, 2): 864, (3, 2, 3, 3): 27216, (3, 3, 3, 2): 27216, (3, 3, 3, 3): 620928}
P19 = 19


def qul_basis():
    """Express every multiplet's weight (mod SM roots) in the Z-basis (w_Q, w_u^c, w_L); check the cubic relations."""
    B = sp.Matrix([SMITH_COORDS['Q'], SMITH_COORDS['u^c'], SMITH_COORDS['L']]).T          # columns = basis vectors
    assert abs(B.det()) == 1, "Q, u^c, L are a Z-basis of P/Q_SM (B1278: coefficient determinant 1)"
    Binv = B.inv()
    expr = {l: tuple(int(v) for v in (Binv * sp.Matrix(SMITH_COORDS[l]))) for l in LABELS}
    for tri in CUBICS:
        s = tuple(sum(SMITH_COORDS[l][k] for l in tri) for k in range(3))
        assert s == (0, 0, 0), (tri, s)
    return expr


def multiplicity(c19, s2):
    """m(c) for a character with 19-part c19 (shape (...,2), entries mod 19) and 2-part s2 (shape (...,2), entries mod 2)."""
    on_axis = (c19[..., 0] == 0) | (c19[..., 1] == 0)
    nonzero19 = (c19[..., 0] != 0) | (c19[..., 1] != 0)
    s_zero = (s2[..., 0] == 0) & (s2[..., 1] == 0)
    m = np.zeros(c19.shape[:-1], dtype=np.int64)
    m[nonzero19 & on_axis] = 3
    m[~nonzero19 & s_zero] = 3
    m[~nonzero19 & ~s_zero] = 2
    return m


def alphabet():
    """K3 in the model: the identity and (c, s), c a non-zero element of one of the two axes of F_19^2, s in V_4."""
    els = [(0, 0, 0, 0)]
    for s in itertools.product(range(2), repeat=2):
        for t in range(1, P19):
            els.append((t, 0) + s)
            els.append((0, t) + s)
    arr = np.array(els, dtype=np.int64)
    assert len(arr) == 145 and len({tuple(x) for x in els}) == 145
    return arr


def enumerate_lines(expr):
    """All lines (psi_Q, psi_u, psi_L) in K3^3, every multiplet's multiplicity, and B1278's classes."""
    K = alphabet(); n = len(K)
    iQ, iu, iL = np.meshgrid(np.arange(n), np.arange(n), np.arange(n), indexing='ij')
    q, u, l = K[iQ.ravel()], K[iu.ravel()], K[iL.ravel()]
    N = q.shape[0]
    chars, mult = {}, {}
    for lab in LABELS:
        a, b, c = expr[lab]
        x = a * q + b * u + c * l
        x19 = x[:, :2] % P19; x2 = x[:, 2:] % 2
        chars[lab] = np.concatenate([x19, x2], axis=1)
        mult[lab] = multiplicity(x19, x2)
    three = (mult['d^c'] == 3) & (mult['e^c'] == 3)                                   # Q, u^c, L are 3 by construction
    assert (mult['Q'] == 3).all() and (mult['u^c'] == 3).all() and (mult['L'] == 3).all()
    same = lambda A, B: (chars[A] == chars[B]).all(axis=1)
    broken = ~(same('Q', 'u^c') & same('u^c', 'e^c'))
    vac = (mult['S'] >= 1) & (mult['nu^c'] >= 1) & (mult['H_u'] >= 1) & (mult['H_d'] >= 1)
    sm = three & broken & vac
    full = sm & np.all(np.stack([mult[l] == 3 for l in LABELS]), axis=0)
    return dict(n_lines=N, chars=chars, mult=mult, three=three, broken=broken, sm=sm, full=full, q=q, u=u, l=l)


def verify_against_pipeline():
    """Re-derive SMITH_COORDS from B1278's loaders and Smith form (about two minutes)."""
    sys.path.insert(0, str(ROOT / 'frontier' / 'B1278_the_six_fold_closing' / 'verification'))
    from six_fold_closing import C, R, VM, smith_with_transforms
    wts, rep = C.load(); lab, hy, wts2 = R.sm_labels(); assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = VM.descent_data()
    sm_roots = sorted(set(a2) | {a1, tuple(-x for x in a1)})
    Rm = sp.Matrix([list(a) for a in sm_roots]); D, U, V = smith_with_transforms(Rm)
    dprime = [int(D[j, j]) for j in range(min(D.shape))]; rank = sum(1 for d in dprime if d != 0)
    assert dprime[:rank] == [1] * rank and rank == 3
    free = list(range(rank, 6)); VT = V.T
    table = {}
    for i in range(27):
        co = tuple(int(v) for v in (VT * sp.Matrix(list(wts[i]))))
        key = tuple(co[j] for j in free)
        assert table.setdefault(lab[i], key) == key, ("multiplet members disagree mod SM roots", lab[i])
    ok = all(table[l] == SMITH_COORDS[l] for l in LABELS) and set(table) == set(LABELS)
    return ok, table


def main(verify_weights=False):
    t0 = time.time()
    expr = qul_basis()
    print("=== the weights of the 27 modulo the SM roots, in the basis (w_Q, w_u^c, w_L) ===")
    for l in LABELS:
        print(f"  {l:5s}  Smith coords {SMITH_COORDS[l]!s:14s}  = {expr[l][0]:+d} w_Q {expr[l][1]:+d} w_u^c {expr[l][2]:+d} w_L")
    print(f"  the {len(CUBICS)} cubic couplings of the 27 are zero-sum triples: True")
    even = [l for l in LABELS if all(v % 2 == 0 for v in expr[l])]
    print(f"  multiplets whose weight is TWICE a weight (all coefficients even): {even}   (w_D = -2 w_Q: the diquark coupling Q Q D)")
    out = dict(expr=expr, twice=even)

    print("\n=== the model of the character support: ((C_1 u C_2) x V_4) minus 1 in (Z/19)^2 x V_4 (B1278's theorem on Y_9) ===")
    # the alphabet and the generation-count distribution over the whole group (Z/19)^2 x V_4 (order 1444) -- B1278 counted
    # over (Z/76)^2 (order 5776): the order-4 parts have h^1 = 0 and add 5776 - 1444 = 4332 zeros
    G = np.array(list(itertools.product(range(P19), range(P19), range(2), range(2))), dtype=np.int64)
    mG = multiplicity(G[:, :2], G[:, 2:])
    dist = collections.Counter(mG.tolist()); dist[0] += 5776 - len(G)
    print(f"  generation counts sum_i h^1(chi_i psi) over the 5776 characters: {dict(sorted(dist.items()))}  (B1278: {{0: 5628, 2: 3, 3: 145}})")
    out['dist'] = dict(dist)
    ok = dist == collections.Counter({0: 5628, 2: 3, 3: 145})

    E = enumerate_lines(expr)
    mult, sm, full, three, broken = E['mult'], E['sm'], E['full'], E['three'], E['broken']
    counts = dict(k3=145, k2=dist[2], three_gen=int(three.sum()), su5_broken=int((three & broken).sum()), sm_vacua=int(sm.sum()), full=int(full.sum()))
    print(f"\n=== the lines: (psi_Q, psi_u, psi_L) in K3^3 = {E['n_lines']} ===")
    for k in ('three_gen', 'su5_broken', 'sm_vacua', 'full'):
        print(f"  {k:11s}: model {counts[k]:7d}   B1278 {B1278[k]:7d}   {'OK' if counts[k] == B1278[k] else 'MISMATCH'}")
    ok = ok and all(counts[k] == B1278[k] for k in B1278)
    out['counts'] = counts

    # what is projected, on the SM lines
    hist = collections.Counter(zip(*(mult[l][sm].tolist() for l in ('H_u', 'H_d', 'D', 'Dbar'))))
    hist = {k: v for k, v in sorted(hist.items())}
    print(f"\n=== the SM lines' survival ===")
    print(f"  (H_u, H_d, D, Dbar totals) -> lines: {hist}")
    print(f"  B1300(a), the pipeline:      {B1300A_HIST}   match: {hist == B1300A_HIST}")
    ok = ok and hist == B1300A_HIST
    tot = {l: mult[l][sm] for l in LABELS}
    split = (tot['D'] == 0) & (tot['Dbar'] == 0)
    ever = {l: int((tot[l] < 3).sum()) for l in LABELS}
    print(f"  doublet-triplet split lines (no D, no Dbar, both Higgs doublets, three generations, SU(5) broken): {int(split.sum())}")
    print(f"  D total on the SM lines: {sorted(set(tot['D'].tolist()))};  lines on which a multiplet loses a generation: {ever}")
    print(f"  D total on ALL {int(three.sum())} three-generation lines (SM or not): {sorted(set(mult['D'][three].tolist()))}; on all {E['n_lines']} lines of K3^3: {sorted(set(mult['D'].tolist()))}")
    ok = ok and int(split.sum()) == 0 and set(mult['D'].tolist()) == {3}
    out.update(hist=hist, n_split=int(split.sum()), ever=ever)
    # the projected components are exactly the family characters
    proj_is_family = True
    for l in LABELS:
        x = E['chars'][l][sm]; m = tot[l]
        fam = (x[:, 0] == 0) & (x[:, 1] == 0) & ((x[:, 2] != 0) | (x[:, 3] != 0))
        proj_is_family &= bool(((m == 2) == fam).all()) and bool((m[~fam] == 3).all())
    print(f"  on the SM lines a multiplet loses a generation iff its character IS a family character (and then exactly that generation): {proj_is_family}")
    ok = ok and proj_is_family
    # the (N, nu^c) histogram and the per-generation patterns of the non-full lines, for B1300(a)'s record
    hist_SNu = collections.Counter(zip(tot['S'].tolist(), tot['nu^c'].tolist()))
    print(f"  (N, nu^c totals) -> lines: {dict(sorted(hist_SNu.items()))}")
    nonfull = sm & ~full
    # which generation is projected: the family character chi_g = (0, 0, v_g) with v_g in {(1,0), (0,1), (1,1)} -> g
    vidx = {(1, 0): 0, (0, 1): 1, (1, 1): 2}
    pat = collections.Counter()
    for l in LABELS:
        x = E['chars'][l][nonfull]
        fam = (x[:, 0] == 0) & (x[:, 1] == 0) & ((x[:, 2] != 0) | (x[:, 3] != 0))
        for row in x[fam]:
            pat[(l, vidx[(int(row[2]), int(row[3]))])] += 1
    print(f"  non-full SM lines: {int(nonfull.sum())}; (multiplet, generation) projected -> lines: {dict(sorted(pat.items()))}")
    out.update(hist_SNu=dict(hist_SNu), n_nonfull=int(nonfull.sum()), projected=dict(pat))
    # how many multiplets does a non-full line lose?
    lost = sum((mult[l] < 3).astype(int) for l in LABELS)[nonfull]
    print(f"  multiplets losing a generation per non-full line -> lines: {dict(sorted(collections.Counter(lost.tolist()).items()))}")
    # the non-SM three-generation lines: the 31 104 of B1278
    nonsm = three & broken & ~sm
    spectra = collections.Counter(tuple(int(mult[l][t]) for l in LABELS) for t in np.where(nonsm)[0])
    print(f"  the {int(nonsm.sum())} SU(5)-breaking three-generation lines that are NOT SM vacua, by (Q,u^c,d^c,L,e^c,H_u,H_d,D,Dbar,N,nu^c) multiplicities: {dict(spectra)}")
    out['nonsm_spectra'] = {str(k): v for k, v in spectra.items()}

    # the theorem, checked on the alphabet itself: the square of every letter is a letter of odd order; no square is a family character
    K = alphabet()
    sq = np.concatenate([(2 * K[:, :2]) % P19, (2 * K[:, 2:]) % 2], axis=1)
    letters = {tuple(x) for x in K.tolist()}
    sq_in = all(tuple(x) in letters for x in sq.tolist())
    sq_fam = any(x[0] == 0 and x[1] == 0 and (x[2] or x[3]) for x in sq.tolist())
    print(f"\n=== THE TRIPLET'S PROTECTION: psi_D = psi_Q^-2; the square of every letter of K3 is a letter ({sq_in}) and none is a family character ({not sq_fam}) ===")
    ok = ok and sq_in and not sq_fam
    out['theorem'] = dict(squares_in_alphabet=sq_in, square_is_family=sq_fam)

    if verify_weights:
        t1 = time.time()
        wok, table = verify_against_pipeline()
        print(f"\n  coordinate table re-derived from B1278's loaders and Smith form: {'MATCH' if wok else 'MISMATCH'} ({time.time() - t1:.0f} s)")
        ok = ok and wok
        out['weights_verified'] = wok
    print(f"\n  ({time.time() - t0:.1f} s)")
    out['ok'] = ok
    return out


if __name__ == "__main__":
    out = main(verify_weights='--verify-weights' in sys.argv)
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
