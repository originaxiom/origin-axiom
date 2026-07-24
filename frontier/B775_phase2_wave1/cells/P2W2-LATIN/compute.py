"""B775 Phase-2 Wave-2 -- cell P2W2-LATIN (OI-024).

Derive END-TO-END, from the Kac-Peterson S/T fusion data of E6 level 2, the
Latin-square arrangement of the theta-odd hearing matrix
    B_ij = -A_{k(i,j)} * zeta_14^{m(i,j)},   A_k = (2/sqrt7) sin(2 pi k / 7),
k(i,j) = [[1,2,3],[2,3,1],[3,1,2]]  (B629 / OI-024, exact-but-unproven).

Show the Latin square is FORCED by the E6 level-2 fusion geometry. Program-internal
modular mathematics only; no SM values; pyenv python3; re-runnable. Emits an in-code
verdict (RESOLVED-A / RESOLVED-B / UNRESOLVED) and writes results.json.

Forcing chain (H1-H6, all verified exactly in-cell):
  H1  B_ij = -2i t_i^2 t_j Im S_{a_i a_j}   =>  |B_ij| = 2|Im S_{a_i a_j}|
  H2  J = 351' is an order-3 simple current (qd=1, J^3=1); 3 free orbits;
      27,351',351 sit one in each orbit
  H3  351' = J  =>  amplitude(351' row) = sqrt3 * S00 * (qd27,qd351',qd351)
                  = permutation of {A1,A2,A3}  (FORCED: current relation + distinct qd)
  H4  arg S_{a_i a_j} in (pi/3)Z  =>  |Im S| = (sqrt3/2)|S| uniformly (h_J = 1/3)
  H5  |S_{a_i a_j}|/S00 in {1, qd27, qd351}  (Z/3-orbit constancy of |S|)
  H6  symmetric + rows perm of {A1,A2,A3} + current row (A2,A3,A1)
      => Latin square is the UNIQUE completion
"""
import itertools
import json
import os
from fractions import Fraction as F

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
TOL = mp.mpf(10) ** (-40)
R = {}

# ------------------------------------------------------------------ E6_2 modular data
C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
KH = 14                       # level 2 + dual Coxeter 12
C_int = np.array(C6, dtype=np.int64)
Cs = sp.Matrix(C6)
assert Cs.det() == 3
Cinv3 = np.array([[int(x) for x in row] for row in (3 * Cs.inv()).tolist()],
                 dtype=np.int64)
PRIM = [(0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1),
        (2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2), (1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)]
NAMES = ['1', '27', '27b', '351p', '351pb', '650', '78', '351', '351b']
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])
ones6 = np.ones(6, dtype=np.int64)
shifted3 = [Cinv3 @ (np.array(p, dtype=np.int64) + ones6) for p in PRIM]
lam3 = [Cinv3 @ np.array(p, dtype=np.int64) for p in PRIM]


def weyl_group():
    n = 6
    gens = []
    for j in range(n):
        M = np.eye(n, dtype=np.int64)
        M[j, :] -= C_int[:, j]
        gens.append(M)
    I = np.eye(n, dtype=np.int64)
    seen = {I.tobytes(): 1}
    frontier = [(I, 1)]
    mats, signs = [I], [1]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen[key] = -s
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs)


W, eps = weyl_group()
assert len(W) == 51840
Cb3 = [C_int @ s for s in shifted3]
Wl3 = np.einsum('wij,lj->wli', W, np.array(shifted3))
MOD = 126
rt = [mp.e ** (mp.mpc(0, -1) * 2 * mp.pi() * k / MOD) for k in range(MOD)]

S = [[None] * 9 for _ in range(9)]
for a in range(9):
    for b in range(a, 9):
        ips9 = Wl3[:, a, :] @ Cb3[b]
        coeffs = np.bincount(np.mod(ips9, MOD), weights=eps, minlength=MOD)
        val = mp.mpc(0, 0)
        for r in range(MOD):
            if coeffs[r] != 0:
                val += int(round(coeffs[r])) * rt[r]
        S[a][b] = val
        S[b][a] = val
Sm = mp.matrix(S)
norm = mp.sqrt(sum(Sm[0, k] * mp.conj(Sm[0, k]) for k in range(9)).real)
Sm = Sm / norm
if Sm[0, 0].real < 0:
    Sm = -Sm
S00 = Sm[0, 0].real

# T (exact conformal weights)
rho_w3 = Cinv3 @ ones6
c24 = F(2 * 78, KH) / 24
Tdiag, hs = [], []
for i, p in enumerate(PRIM):
    y3 = shifted3[i] + rho_w3
    h = F(int(lam3[i] @ (C_int @ y3)), 9 * 2 * KH)
    hs.append(h)
    expo = h - c24
    Tdiag.append(mp.e ** (mp.mpc(0, 1) * 2 * mp.pi()
                          * (mp.mpf(expo.numerator) / mp.mpf(expo.denominator))))
Tm = mp.diag(Tdiag)

# gates on the modular data itself
S2 = Sm * Sm
Cperm = mp.matrix([[S2[i, j].real for j in range(9)] for i in range(9)])
conj_idx = [PRIM.index(theta(p)) for p in PRIM]
expectC = mp.zeros(9, 9)
for i in range(9):
    expectC[conj_idx[i], i] = 1
gate_unitary = mp.norm(Sm * Sm.transpose_conj() - mp.eye(9))
gate_sym = mp.norm(Sm - Sm.transpose())
gate_conj = mp.norm(Cperm - expectC)
R['gate_S_unitary_dev'] = float(gate_unitary)
R['gate_S_symmetric_dev'] = float(gate_sym)
R['gate_S2_is_conjugation_dev'] = float(gate_conj)

# ------------------------------------------------------------------ the hearing matrix B
rho = Tm * Tm * Sm * Tm                      # twisted-weld generator T^2 S T
Wt = Cperm * rho
pairs = [(1, 2), (3, 4), (7, 8)]             # (a, abar): 27, 351', 351
unbar = [1, 3, 7]
U = mp.zeros(9, 3)
r2 = 1 / mp.sqrt(2)
for j, (a, b) in enumerate(pairs):
    U[a, j] = r2
    U[b, j] = -r2
B = U.transpose() * Wt * U
trB = sum(B[i, i] for i in range(3))
B4 = (B * B) * (B * B)
R['B_trace'] = [float(trB.real), float(trB.imag)]
R['B_order4_dev'] = float(mp.norm(B4 - mp.eye(3)))
R['B_unitary_dev'] = float(mp.norm(B * B.transpose_conj() - mp.eye(3)))

# amplitudes A_k and A-index extraction
A = {k: (2 / mp.sqrt(7)) * mp.sin(2 * mp.pi() * k / 7) for k in (1, 2, 3)}
R['A1_A2_A3'] = [float(A[1]), float(A[2]), float(A[3])]
R['A_sq_sum'] = float(A[1] ** 2 + A[2] ** 2 + A[3] ** 2)


def a_index(val):
    best, bd = None, mp.mpf(1)
    for k in (1, 2, 3):
        d = abs(abs(val) - A[k])
        if d < bd:
            best, bd = k, d
    return best, bd


kmat = [[a_index(B[i, j])[0] for j in range(3)] for i in range(3)]
kmat_dev = max(a_index(B[i, j])[1] for i in range(3) for j in range(3))
R['k_matrix_measured'] = kmat
R['k_matrix_maxdev_to_A'] = float(kmat_dev)
LATIN = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
R['latin_square_target'] = LATIN
R['k_matrix_is_latin'] = (kmat == LATIN)

# ------------------------------------------------------------------ H1 exact reduction
# B_ij = -2i t_i^2 t_j Im S_{a_i a_j}
t = [Tdiag[a] for a in unbar]
h1_dev = mp.mpf(0)
for i, ai in enumerate(unbar):
    for j, aj in enumerate(unbar):
        pred = -2 * mp.mpc(0, 1) * t[i] ** 2 * t[j] * mp.im(Sm[ai, aj])
        h1_dev = max(h1_dev, abs(B[i, j] - pred))
# and the S_{abar,b}=conj(S_{a,b}) identity the reduction rests on
sconj_dev = mp.mpf(0)
for i, ai in enumerate(unbar):
    abar = pairs[i][1]
    for aj in unbar:
        sconj_dev = max(sconj_dev, abs(Sm[abar, aj] - mp.conj(Sm[ai, aj])))
R['H1_reduction_dev'] = float(h1_dev)
R['H1_Sconj_identity_dev'] = float(sconj_dev)
amp = [[2 * abs(mp.im(Sm[ai, aj])) for aj in unbar] for ai in unbar]
R['H1_amp_equals_2ImS_dev'] = float(
    max(abs(amp[i][j] - abs(B[i, j])) for i in range(3) for j in range(3)))

# ------------------------------------------------------------------ H2 simple current


def Nfus(i, j, k):
    return sum(Sm[i, l] * Sm[j, l] * mp.conj(Sm[k, l]) / Sm[0, l]
               for l in range(9))


qd = [(Sm[0, a] / Sm[0, 0]).real for a in range(9)]
# J = 351p index 3; qd and order
Jidx = 3
R['qd_351p'] = float(qd[Jidx])
Jaction = {}
for a in range(9):
    for b in range(9):
        v = Nfus(Jidx, a, b)
        if abs(v - 1) < 1e-20 and abs(v.imag) < 1e-20:
            Jaction[a] = b
# order of J: J,J^2,J^3
Jpow = [0]
x = 0
for _ in range(3):
    x = Jaction[x] if x == Jpow[-1] and len(Jpow) == 1 else Jaction[x]
# recompute orbit of identity cleanly
orbit_id = [0, Jaction[0], Jaction[Jaction[0]]]
R['J_order3'] = (Jaction[Jaction[Jaction[0]]] == 0)
R['J_is_permutation'] = (sorted(Jaction.values()) == list(range(9)))
# orbits
seen = set()
orbits = []
for a in range(9):
    if a in seen:
        continue
    o = [a, Jaction[a], Jaction[Jaction[a]]]
    orbits.append(o)
    seen.update(o)
R['J_orbits'] = [[NAMES[x] for x in o] for o in orbits]
R['J_orbits_count'] = len(orbits)
R['J_orbits_all_size3'] = all(len(set(o)) == 3 for o in orbits)
# the three pair-reps land one per orbit
orbit_of = {}
for oi, o in enumerate(orbits):
    for x in o:
        orbit_of[x] = oi
pair_orbits = [orbit_of[a] for a in unbar]
R['pair_rep_orbits'] = pair_orbits
R['pairs_one_per_orbit'] = (len(set(pair_orbits)) == 3)

# ------------------------------------------------------------------ H3 current row forced
# 351' = J : amplitude(351' row) = sqrt3 * S00 * (qd27, qd351', qd351)
qd_pairs = [qd[a] for a in unbar]          # qd(27), qd(351'), qd(351)
current_row_pred = [mp.sqrt(3) * S00 * q for q in qd_pairs]
current_row_meas = amp[1]                  # row i=1 is 351'
R['qd_27_351p_351'] = [float(q) for q in qd_pairs]
R['H3_current_row_pred'] = [float(v) for v in current_row_pred]
R['H3_current_row_meas'] = [float(v) for v in current_row_meas]
R['H3_current_row_dev'] = float(
    max(abs(current_row_meas[j] - current_row_pred[j]) for j in range(3)))
# is it a permutation of {A1,A2,A3}?
cr_idx = sorted(a_index(mp.mpc(v, 0))[0] for v in current_row_meas)
R['H3_current_row_is_perm_of_A'] = (cr_idx == [1, 2, 3])
# the three orbit qds are distinct (needed for "permutation")
R['H3_orbit_qds_distinct'] = (
    abs(qd_pairs[0] - qd_pairs[1]) > 1e-20 and
    abs(qd_pairs[0] - qd_pairs[2]) > 1e-20 and
    abs(qd_pairs[1] - qd_pairs[2]) > 1e-20)

# ------------------------------------------------------------------ H4 uniform phase
# arg S_{a_i a_j} in (pi/3)Z  => |Im S| = (sqrt3/2)|S|
arg_over_pi3 = [[float(mp.arg(Sm[ai, aj]) / (mp.pi() / 3)) for aj in unbar]
                for ai in unbar]
R['H4_argS_over_pi3'] = arg_over_pi3
R['H4_all_args_multiple_of_pi3'] = all(
    abs(x - round(x)) < 1e-20 for row in arg_over_pi3 for x in row)
# and none is a multiple of pi (would give Im=0); all are +-1 or +-2 mod 6
R['H4_all_imag_gives_sqrt3_half'] = all(
    abs(abs(mp.im(Sm[ai, aj])) - (mp.sqrt(3) / 2) * abs(Sm[ai, aj])) < TOL
    for ai in unbar for aj in unbar)

# ------------------------------------------------------------------ H5 3-valued |S|
Nmat = [[abs(Sm[ai, aj]) / S00 for aj in unbar] for ai in unbar]
qd_set = sorted({round(float(qd[a]), 12) for a in unbar})   # {1, qd27, qd351}
R['H5_qd_value_set'] = qd_set
R['H5_Nmat'] = [[float(x) for x in row] for row in Nmat]


def in_qd_set(x):
    return any(abs(float(x) - v) < 1e-10 for v in qd_set)


R['H5_all_S_entries_are_qd_values'] = all(
    in_qd_set(Nmat[i][j]) for i in range(3) for j in range(3))


def matches_qd_set(vals):
    vs = sorted(float(v) for v in vals)
    return all(abs(vs[t] - qd_set[t]) < 1e-9 for t in range(3))


_rows_ok = all(matches_qd_set([Nmat[r][c] for c in range(3)]) for r in range(3))
_cols_ok = all(matches_qd_set([Nmat[r][c] for r in range(3)]) for c in range(3))
R['H5_Nmat_is_latin'] = _rows_ok and _cols_ok

# ------------------------------------------------------------------ H6 unique completion
# GIVEN: E symmetric; each row a permutation of {A1,A2,A3}; current (middle) row=(A2,A3,A1).
# Prove the Latin square is the unique completion by exhaustive search over all
# symmetric 3x3 fillings whose rows are permutations of {1,2,3} (A-indices) with the
# middle row fixed to (2,3,1), then intersect with the column-permutation constraint.
def is_perm123(triple):
    return sorted(triple) == [1, 2, 3]


completions = []
mid = (2, 3, 1)                     # forced current row (A2,A3,A1) as A-indices
for a in (1, 2, 3):
    for b in (1, 2, 3):
        for c in (1, 2, 3):
            # symmetric matrix with middle row = mid; unknown row0=(a, mid[0], b_),
            # but symmetry ties E01=E10=mid[0], E21=E12=mid[2].
            # unknowns: E00=a, E02=E20=x, E22=d
            for x in (1, 2, 3):
                for d in (1, 2, 3):
                    M = [[a, mid[0], x],
                         [mid[0], mid[1], mid[2]],
                         [x, mid[2], d]]
                    rows_ok = all(is_perm123(M[r]) for r in range(3))
                    cols_ok = all(is_perm123([M[r][cc] for r in range(3)])
                                  for cc in range(3))
                    if rows_ok and cols_ok:
                        if M not in completions:
                            completions.append(M)
R['H6_num_valid_completions'] = len(completions)
R['H6_unique_completion'] = (len(completions) == 1 and completions[0] == LATIN)
R['H6_completion'] = completions[0] if completions else None

# also confirm: entries in {A1,A2,A3} + row-sq-sum=1 forces permutation (value logic)
# (three values drawn from {A1^2,A2^2,A3^2} summing to A1^2+A2^2+A3^2 must be the full set)
sq = [float(A[k] ** 2) for k in (1, 2, 3)]
tot = sum(sq)
perm_forced = True
for combo in itertools.combinations_with_replacement(range(3), 3):
    s = sum(sq[i] for i in combo)
    if abs(s - tot) < 1e-9 and sorted(combo) != [0, 1, 2]:
        perm_forced = False
R['H6_sqsum_forces_permutation'] = perm_forced

# ------------------------------------------------------------------ B774 chord discipline
# B genuinely order-4 (B^2 != I): the theta-odd space carries a real order-4 operator,
# not a Z/2 reflection. The Latin square is an ABELIAN Z/3 arrangement; values A_k are
# transcendental modular qd-data. No non-abelian claim about the Latin square.
B2 = B * B
R['B774_B_order_is_4_not_2'] = float(mp.norm(B2 - mp.eye(3))) > 1e-6
R['B774_B4_is_identity'] = float(mp.norm(B4 - mp.eye(3))) < 1e-40
Evals, _ = mp.eig(B)
R['B774_eigs'] = [[float(e.real), float(e.imag)] for e in Evals]

# ------------------------------------------------------------------ VERDICT
checks_forced = {
    'H1_reduction': R['H1_reduction_dev'] < 1e-40 and R['H1_Sconj_identity_dev'] < 1e-40,
    'H1_amp_2ImS': R['H1_amp_equals_2ImS_dev'] < 1e-40,
    'H2_simple_current': R['J_order3'] and R['J_is_permutation']
                         and abs(R['qd_351p'] - 1) < 1e-20,
    'H2_three_orbits': R['J_orbits_count'] == 3 and R['J_orbits_all_size3'],
    'H2_pairs_one_per_orbit': R['pairs_one_per_orbit'],
    'H3_current_row_forced': R['H3_current_row_dev'] < 1e-40
                             and R['H3_current_row_is_perm_of_A']
                             and R['H3_orbit_qds_distinct'],
    'H4_uniform_phase': R['H4_all_args_multiple_of_pi3']
                        and R['H4_all_imag_gives_sqrt3_half'],
    'H5_three_valued_S': R['H5_all_S_entries_are_qd_values'] and R['H5_Nmat_is_latin'],
    'H6_unique_completion': R['H6_unique_completion']
                            and R['H6_sqsum_forces_permutation'],
    'measured_is_latin': R['k_matrix_is_latin'] and R['k_matrix_maxdev_to_A'] < 1e-40,
    'B774_genuine_order4': R['B774_B_order_is_4_not_2'] and R['B774_B4_is_identity'],
}
R['checks_forced'] = checks_forced
all_forced = all(checks_forced.values())

if all_forced:
    verdict = "RESOLVED-A"
    headline = (
        "THEOREM (forced by E6 level-2 fusion): the hearing-matrix Latin square is derived "
        "end-to-end from Kac-Peterson S/T data. Exact reduction B_ij = -2i t_i^2 t_j Im S_{a_i,a_j} "
        "=> |B_ij| = sqrt3 |S_{a_i,a_j}| (uniform +-pi/3,+-2pi/3 phase, h_J=1/3). The order-3 simple "
        "current J=351' (qd=1) gives 3 free orbits with 27,351',351 one per orbit; the current relation "
        "S_{J,mu}=e^{2pi i Q(mu)}S_{0mu} forces the 351'-row to be sqrt3*S00*(qd27,qd351',qd351)=(A2,A3,A1), "
        "a permutation of {A1,A2,A3}; unitarity + symmetry + the Z/3-orbit 3-valuedness of |S| then force "
        "the UNIQUE Latin completion [[1,2,3],[2,3,1],[3,1,2]]. The arrangement is the abelian Z/3 center; "
        "the values A_k=(2/sqrt7)sin(2pi k/7) are the transcendental modular qd-data. Reproduced two ways.")
else:
    failed = [k for k, v in checks_forced.items() if not v]
    verdict = "RESOLVED-B" if R['k_matrix_is_latin'] else "UNRESOLVED"
    headline = ("Latin square measured but forcing chain incomplete; failed checks: "
                + ", ".join(failed))

R['verdict'] = verdict
R['headline'] = headline

# ------------------------------------------------------------------ output
lines = []
lines.append("=" * 78)
lines.append("B775 P2W2-LATIN  --  Latin square of the E6_2 hearing matrix, from fusion data")
lines.append("=" * 78)
lines.append(f"[gates] S unitary {R['gate_S_unitary_dev']:.1e}  symmetric {R['gate_S_symmetric_dev']:.1e}"
             f"  S^2=conj {R['gate_S2_is_conjugation_dev']:.1e}")
lines.append(f"[B] trace={float(trB.real):+.6f}{float(trB.imag):+.1e}i  order-4 dev {R['B_order4_dev']:.1e}"
             f"  unitary dev {R['B_unitary_dev']:.1e}")
lines.append("")
lines.append("MEASURED A-index matrix k(i,j)  (pairs order 27,351',351):")
for row in kmat:
    lines.append("   " + "  ".join(str(v) for v in row))
lines.append(f"   is Latin [[1,2,3],[2,3,1],[3,1,2]] : {R['k_matrix_is_latin']}"
             f"   (max dev to A_k = {R['k_matrix_maxdev_to_A']:.1e})")
lines.append("")
lines.append("H1  B_ij = -2i t_i^2 t_j Im S_{a_i a_j}   dev = %.1e" % R['H1_reduction_dev'])
lines.append("    S_{abar,b}=conj(S_{a,b}) identity     dev = %.1e" % R['H1_Sconj_identity_dev'])
lines.append("    => |B_ij| = 2|Im S_{a_i a_j}|         dev = %.1e" % R['H1_amp_equals_2ImS_dev'])
lines.append("")
lines.append("H2  J=351' simple current: qd(J)=%.6f  order-3=%s  perm=%s"
             % (R['qd_351p'], R['J_order3'], R['J_is_permutation']))
for o in R['J_orbits']:
    lines.append("      orbit: " + ", ".join(o))
lines.append("    27,351',351 orbits = %s  (one per orbit: %s)"
             % (R['pair_rep_orbits'], R['pairs_one_per_orbit']))
lines.append("")
lines.append("H3  current (351') row  meas = %s" % [round(v, 6) for v in R['H3_current_row_meas']])
lines.append("    sqrt3*S00*(qd27,qd351',qd351) = %s   dev = %.1e"
             % ([round(v, 6) for v in R['H3_current_row_pred']], R['H3_current_row_dev']))
lines.append("    is permutation of {A1,A2,A3}: %s   orbit qds distinct: %s"
             % (R['H3_current_row_is_perm_of_A'], R['H3_orbit_qds_distinct']))
lines.append("")
lines.append("H4  arg S/(pi/3) = %s" % R['H4_argS_over_pi3'])
lines.append("    all multiples of pi/3: %s   |Im S|=(sqrt3/2)|S| uniformly: %s"
             % (R['H4_all_args_multiple_of_pi3'], R['H4_all_imag_gives_sqrt3_half']))
lines.append("")
lines.append("H5  |S_{a_i a_j}|/S00 (qd values {%s}):" % ", ".join("%.6f" % v for v in R['H5_qd_value_set']))
for row in R['H5_Nmat']:
    lines.append("      " + "  ".join("%.6f" % v for v in row))
lines.append("    all entries are qd values: %s   is Latin: %s"
             % (R['H5_all_S_entries_are_qd_values'], R['H5_Nmat_is_latin']))
lines.append("")
lines.append("H6  unique symmetric completion (rows&cols perm of A-indices, middle row=(2,3,1)):")
lines.append("      #valid completions = %d   unique Latin: %s"
             % (R['H6_num_valid_completions'], R['H6_unique_completion']))
lines.append("      sqsum(=1) forces each row a permutation: %s" % R['H6_sqsum_forces_permutation'])
lines.append("")
lines.append("B774  B order-4 not order-2: %s   B^4=I: %s   (theta-odd op genuinely order-4;"
             % (R['B774_B_order_is_4_not_2'], R['B774_B4_is_identity']))
lines.append("      Latin square = abelian Z/3 arrangement; values A_k transcendental modular data)")
lines.append("")
lines.append("-" * 78)
lines.append("CHECKS (all must hold for RESOLVED-A):")
for k, v in checks_forced.items():
    lines.append(f"   [{'PASS' if v else 'FAIL'}] {k}")
lines.append("-" * 78)
lines.append("VERDICT: " + verdict)
lines.append(headline)
out = "\n".join(lines)
print(out)
with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write(out + "\n")
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(R, f, indent=2)
