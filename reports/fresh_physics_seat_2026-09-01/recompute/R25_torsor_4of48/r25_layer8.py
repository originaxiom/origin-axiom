#!/usr/bin/env python3
"""R25 addendum — recompute B1127's LAYER 8 fences, which the original R25 cell did not re-run:

  (a) layer8a  "unsigned pi_mirror": the bare permutation lift of the diagram fold (e_r -> e_{pi r},
      h_r -> h_{pi r}, all signs +1, NO recursive sign extension) — is it an involution? an automorphism?
      Bank: theta^2 = I true, automorphism failures 38/60 random trials, valid_as_automorphism False.
      Here: theta^2 checked exactly; bracket failures counted EXACTLY over all 78^2 basis pairs (plus a
      seeded random-vector trial of the bank's kind for a rate comparison).

  (b) layer8b  "secondary compact-referenced construction" sigma' = tau . theta_split . theta_A with
      theta_split = antipodal/pi=id, eps=+1 (the linear shadow of the compact conjugation sigma_c, R25
      control: global (0,78,0)) and theta_A one element of antipodal/class-A.  Bank (one base element):
      commute True, product involution True, I2 stable True, I2 antilinear signature (5,3,0), NOT compact.
      Here: all 16 antipodal/A elements theta_A (the bank's base is one of them, we do not know which),
      each composed with theta_split; commute / involution / automorphism / I2-stability / I2 signature /
      global signature, exactly.  Structural expectation: theta_split . theta_A is in the permute/pi_mirror
      family (antipodal o antipodal = permute), and R25 found (5,3,0) on ALL 24 permute elements — so the
      bank's (5,3,0) should hold for every choice of base, not just theirs.

Uses r25_lib (own construction, Jacobi-verified).  Output: r25_layer8.json / r25_layer8.txt
"""
import json, os, random, itertools
import numpy as np, sympy as sp
import r25_lib as L

HERE = os.path.dirname(os.path.abspath(__file__))
N = L.N
out = {}
lines = []
def say(s):
    print(s, flush=True); lines.append(s)

def brk(u, v): return np.einsum('a,b,abc->c', u, v, L.C)

def i2_sig(T):
    """antilinear signature on the 8-dim I2 = A2 (2 Cartan + 6 root vectors; NOT a coordinate subspace),
    exactly as r25_torsor.py: restrict T to I2 (T P = P S, integer S), V+/V- of S, exact sympy Gram with
    the i factor on V-, exact signature.  Returns None if I2 is not T-stable."""
    P = np.array(L.I2_basis).T
    S = np.rint(np.linalg.lstsq(P.astype(float), (T @ P).astype(float), rcond=None)[0]).astype(int)
    if not (T @ P == P @ S).all(): return None
    M = sp.Matrix(S)
    Vp = (M - sp.eye(8)).nullspace(); Vm = (M + sp.eye(8)).nullspace()
    KI2 = sp.Matrix(P.T @ L.K @ P)
    vecs = [(v, 1) for v in Vp] + [(v, sp.I) for v in Vm]
    G = sp.zeros(8, 8)
    for i, (u, cu) in enumerate(vecs):
        for j, (w, cw) in enumerate(vecs):
            G[i, j] = sp.expand(cu * cw * (u.T * KI2 * w)[0])
    assert all(sp.im(x) == 0 for x in G)
    return L.sig(G)

def global_sig(T):
    """global antilinear signature of sigma = tau.theta on V+(theta) (+) i V-(theta): exact rational
    eigenvector bases (sympy nullspace), Gram of the Killing form with the i.i = -1 sign on V-, cross
    terms must vanish exactly; signature by numpy eigvalsh (78x78 Gram, integer entries, gaps large)"""
    M = sp.Matrix(T)
    Bp = [np.array(v, dtype=object).reshape(-1) for v in (M - sp.eye(N)).nullspace()]
    Bm = [np.array(v, dtype=object).reshape(-1) for v in (M + sp.eye(N)).nullspace()]
    Kf = sp.Matrix(L.K)
    vecs = [(sp.Matrix(v), 1) for v in Bp] + [(sp.Matrix(v), -1) for v in Bm]   # -1: (i)(i) = -1
    n = len(vecs)
    G = np.zeros((n, n))
    for i, (u, cu) in enumerate(vecs):
        for j, (w, cw) in enumerate(vecs):
            val = (u.T * Kf * w)[0]
            if cu != cw:
                assert val == 0, 'V+ and V- not K-orthogonal'
            G[i, j] = float(val) * (1 if cu == cw == 1 else (-1 if cu == cw == -1 else 0))
    return L.sig_np(G), (len(Bp), len(Bm))

# ----------------------------------------------------------------------------------------------
# (a) unsigned fold
# ----------------------------------------------------------------------------------------------
T_un = np.zeros((N, N), dtype=int)
for i in range(6):
    T_un[:, i] = L.hvec(L.pi_mirror(L.simple[i]))
for r in L.roots:
    T_un[:, 6 + L.ridx[r]] = L.evec(L.pi_mirror(r))
inv_un = bool(L.is_inv(T_un))
aut_un = bool(L.is_aut(T_un))
# exact failure count over all basis pairs
fail_pairs, fail_by_kind = 0, {'h-e': 0, 'e-e': 0, 'h-h': 0}
for a in range(N):
    ea = np.eye(N, dtype=int)[a]
    for b in range(N):
        eb = np.eye(N, dtype=int)[b]
        lhs = T_un @ brk(ea, eb)
        rhs = brk(T_un @ ea, T_un @ eb)
        if not (lhs == rhs).all():
            fail_pairs += 1
            kind = 'h-h' if (a < 6 and b < 6) else ('h-e' if (a < 6 or b < 6) else 'e-e')
            fail_by_kind[kind] += 1
# bank-style random sparse-vector trial (seeded), rate only
rng = random.Random(20260901)
def rand_vec():
    v = np.zeros(N, dtype=int)
    for _ in range(4):
        v += rng.randint(-3, 3) * np.eye(N, dtype=int)[rng.randrange(N)]
    return v
fail_rand = 0
for _ in range(60):
    x, y = rand_vec(), rand_vec()
    if not (T_un @ brk(x, y) == brk(T_un @ x, T_un @ y)).all(): fail_rand += 1
say('(a) unsigned pi_mirror fold (permute, all signs +1, no sign extension):')
say('    theta^2 = I: %s   automorphism (all 78^2 pairs): %s   exact failing basis pairs: %d / %d  %s'
    % (inv_un, aut_un, fail_pairs, N * N, fail_by_kind))
say('    bank-style random 4-sparse vector trial: %d / 60 fail   (bank: 38 / 60)' % fail_rand)
# which e-e pairs fail?  pairs (r,s) with r+s a root where eps(pi r, pi s) != eps(r, s)
mism = sum(1 for r in L.roots for s in L.roots
           if tuple(np.array(r) + np.array(s)) in L.ridx and L.eps(L.pi_mirror(r), L.pi_mirror(s)) != L.eps(r, s))
say('    root pairs (r,s), r+s a root, with cocycle eps(pi r, pi s) != eps(r, s): %d  (these are the e-e failures)' % mism)
out['layer8a_unsigned_pi_mirror'] = dict(theta_squared_is_identity=inv_un, is_automorphism=aut_un,
    failing_basis_pairs=fail_pairs, of_pairs=N * N, failing_by_kind=fail_by_kind,
    random_trial_failures_of_60=fail_rand, bank_random_failures_of_60=38, valid_as_automorphism=bool(inv_un and aut_un),
    cocycle_mismatch_root_pairs=mism)

# ----------------------------------------------------------------------------------------------
# (b) secondary construction over ALL 16 antipodal/A elements
# ----------------------------------------------------------------------------------------------
theta_split = L.build_theta(L.ident, 'antipodal', (1,) * 6)
assert L.is_aut(theta_split) and L.is_inv(theta_split)
sig_split, _ = global_sig(theta_split)
say('(b) theta_split = antipodal/id, eps=+1: automorphism+involution; global antilinear sig %s (sigma_c control, expect (0,78,0))' % (sig_split,))
assert sig_split == (0, 78, 0)

# the 16 antipodal/A elements: the involutive sign lifts of pi_mirror in the antipodal family
elemsA = []
for eps6 in itertools.product((1, -1), repeat=6):
    T = L.build_theta(L.pi_mirror, 'antipodal', eps6)
    if L.is_inv(T):
        assert L.is_aut(T)
        elemsA.append((eps6, T))
say('    antipodal/A elements found: %d (expect 16)' % len(elemsA))
assert len(elemsA) == 16

rows = []
for eps6, TA in elemsA:
    P = theta_split @ TA
    commute = bool((theta_split @ TA == TA @ theta_split).all())
    invol = bool(L.is_inv(P))
    aut = bool(L.is_aut(P))
    # is the product a permute/pi_mirror family element?  h_r -> h_{pi r} and e_r -> +-e_{pi r}
    in_permute = all((P[:, i] == L.hvec(L.pi_mirror(L.simple[i]))).all() for i in range(6)) and \
                 all(abs(P[:, 6 + L.ridx[r]]).sum() == 1 and P[6 + L.ridx[L.pi_mirror(r)], 6 + L.ridx[r]] != 0 for r in L.roots)
    # I2 stability + 8-dim I2 antilinear signature
    csig = i2_sig(P)
    stable = csig is not None
    gsig, gdims = global_sig(P)
    A_isig = i2_sig(TA)
    A_gsig, _ = global_sig(TA)
    rows.append(dict(eps6=list(eps6), theta_A_I2_sig=list(A_isig), theta_A_global_sig=list(A_gsig),
                     commute=commute, product_involution=invol, product_automorphism=aut, product_in_permute_piMirror=bool(in_permute),
                     I2_stable=stable, product_I2_antilinear_sig=list(csig) if csig else None, product_I2_compact=bool(csig == (0, 8, 0)),
                     product_global_antilinear_sig=list(gsig)))
    say('    eps6=%s  theta_A: I2 %s glob %s | product: commute=%s invol=%s aut=%s permute/piMirror=%s I2stable=%s  I2 sig %s compact=%s  glob %s'
        % (''.join('+' if e > 0 else '-' for e in eps6), A_isig, A_gsig, commute, invol, aut, in_permute, stable, csig, csig == (0, 8, 0), gsig))
n_compact = sum(1 for r in rows if r['product_I2_compact'])
say('    products with compact I2: %d / 16   (bank, one base element: (5,3,0) not compact)' % n_compact)
say('    products from the 4 compact theta_A (R25 hits): %s'
    % [r['product_I2_antilinear_sig'] for r in rows if r['theta_A_I2_sig'] == [0, 8, 0]])
out['layer8b_secondary_construction_all_16_bases'] = rows
out['layer8b_summary'] = dict(n_bases=16, all_commute=all(r['commute'] for r in rows), all_involution=all(r['product_involution'] for r in rows),
    all_automorphism=all(r['product_automorphism'] for r in rows), all_in_permute_piMirror=all(r['product_in_permute_piMirror'] for r in rows),
    all_I2_stable=all(r['I2_stable'] for r in rows), I2_sigs=sorted(set(tuple(r['product_I2_antilinear_sig']) for r in rows)),
    n_compact=n_compact, bank_I2_sig=[5, 3, 0], bank_compact=False)
say('    summary: %s' % json.dumps(out['layer8b_summary']))

json.dump(out, open(HERE + '/r25_layer8.json', 'w'), indent=1)
open(HERE + '/r25_layer8.txt', 'w').write('\n'.join(lines) + '\n')
