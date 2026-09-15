"""OUTSIDE BENCH -- L72 PHASE 2: auditing the flagged closure claim.

Seal: outside_bench/seals/L72_PHASE2_AUDIT_PREREG.md
      sha256 0daa7ada95b244277c404027c03f0eb34424910fcdd3598c9ab14033dd0545cb
      committed before this file was written.

CELL 1  do the cell's two committed artifacts agree?
CELL 2  the Deligne splitting, rebuilt independently
CELL 3  is the rank-3 factor the unitary SU(2)_5-even, or a Galois conjugate?

The E6 level-2 stage is rebuilt here from the Cartan matrix (the memo-206 instrument).

Run: python3 outside_bench/certificates/l72_phase2_audit.py
"""
import json
import pathlib
import re
import subprocess

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
CELL = ROOT / 'frontier/B775_phase2_wave1/cells/P2W5-L72'

print("=" * 78)
print("L72 PHASE 2 AUDIT -- outside bench")
print("seal sha256 0daa7ada95b244277c404027c03f0eb34424910fcdd3598c9ab14033dd0545cb")
print(f"HEAD = {subprocess.check_output(['git','-C',str(ROOT),'rev-parse','--short','HEAD']).decode().strip()}")
print("=" * 78)

# ============================================================ CELL 1
print("\n" + "=" * 78)
print("CELL 1 -- do the cell's two committed artifacts agree?")
print("=" * 78)
out = (CELL / 'output.txt').read_text()
res = json.loads((CELL / 'results.json').read_text())
m = re.search(r'^VERDICT:\s*(\S+)', out, re.M)
v_txt, v_json = m.group(1), res['verdict']
print(f"  output.txt   'VERDICT:'          = {v_txt}")
print(f"  results.json ['verdict']         = {v_json}")
gline = re.search(r'^gates:\s*(.*)$', out, re.M).group(1)
printed = {}
for part in gline.split('|'):
    k, _, val = part.strip().rpartition(' ')
    printed[k.strip()] = (val.strip() == 'True')
print(f"\n  gates printed in output.txt : {printed}")
print(f"  gates stored in results.json: {res['gates']}")
ALIAS = {'modular-data': 'modular_data', 'level1-6j': 'level1_6j', 'level2-6j': 'level2_6j',
         'A2': 'A2_6j_both_levels', 'A3': 'A3_CS_theta_odd', 'wall': 'W_computed_wall',
         'index': 'index_ok', 'deformation': 'deformation_ok'}
disagree = []
for k, val in printed.items():
    j = ALIAS.get(k)
    if j in res['gates'] and res['gates'][j] != val:
        disagree.append((k, val, j, res['gates'][j]))
print("\n  gate-by-gate:")
for k, val in printed.items():
    j = ALIAS.get(k, k)
    jv = res['gates'].get(j, '(absent)')
    mark = '   <-- DISAGREE' if (j in res['gates'] and jv != val) else ''
    print(f"    {k:14s} output.txt={str(val):5s}   results.json[{j}]={str(jv):9s}{mark}")
only_json = set(res['gates']) - {ALIAS.get(k, k) for k in printed}
print(f"  gates present ONLY in results.json: {sorted(only_json)}")
agree = (v_txt.replace('-A', '') == v_json or v_txt == v_json) and not disagree
print(f"\n  CELL 1 OUTCOME: {'A' if agree else 'B'}")
print(f"    verdict strings agree: {v_txt == v_json}")
print(f"    gates disagreeing: {len(disagree)}  {[(a, b, c, d) for a, b, c, d in disagree]}")
print(f"\n  the cell's OWN fenced residual, quoted from results.json:")
for r in res['residuals_external']:
    print(f"    - {r}")

# ============================================================ the stage (control C1)
print("\n" + "=" * 78)
print("C1 -- the E6 level-2 stage, rebuilt here from the Cartan matrix")
print("=" * 78)
C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
MARKS = np.array([1, 2, 2, 3, 2, 1], dtype=np.int64)
H_VEE, DIM_E6, DETC, K = 12, 78, 3, 2
CI3 = np.rint(np.linalg.inv(C6.astype(float)) * DETC).astype(np.int64)
assert np.array_equal(CI3 @ C6, DETC * np.eye(6, dtype=np.int64))


def weyl_group():
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64); M[j, :] -= C6[:, j]; gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes(): 1}; layer = [(I, 1)]; mats, signs = [I], [1]
    while layer:
        nxt = []
        for M, s in layer:
            for g in gens:
                Mg = g @ M; k = Mg.tobytes()
                if k not in seen:
                    seen[k] = -s; nxt.append((Mg, -s)); mats.append(Mg); signs.append(-s)
        layer = nxt
    return np.array(mats), np.array(signs, dtype=np.int64)


def primaries(k):
    out = []
    def rec(i, rem, acc):
        if i == 6:
            out.append(tuple(acc)); return
        for v in range(rem // MARKS[i] + 1):
            rec(i + 1, rem - v * MARKS[i], acc + [v])
    rec(0, k, [])
    return sorted(out, key=lambda t: (sum(t), t))


W, eps = weyl_group()
assert len(W) == 51840, len(W)
KH = K + H_VEE
PRIM = primaries(K)
N = len(PRIM)
rho = np.ones(6, dtype=np.int64)
A = np.array([np.array(p, dtype=np.int64) + rho for p in PRIM])
X = (CI3 @ A.T).T
MOD = 9 * KH
Y = C6 @ X.T
zeta = np.exp(-2j * np.pi * np.arange(MOD) / MOD)
epsc = eps.astype(np.complex128)
Su = np.empty((N, N), dtype=complex)
for l in range(N):
    Su[l] = epsc @ zeta[(W @ X[l] @ Y) % MOD]
S0 = Su / np.sqrt(Su @ Su)[np.unravel_index(np.argmax(np.abs(Su @ Su)), (N, N))]
c = K * DIM_E6 / KH
h = np.array([float(np.array(p) @ (CI3 / DETC) @ (np.array(p) + 2 * rho)) / (2 * KH) for p in PRIM])
T = np.diag(np.exp(2j * np.pi * (h - c / 24)))
sg = min((s for s in (1.0, -1.0)),
         key=lambda s: np.abs(np.linalg.matrix_power(s * S0 @ T, 3) - (S0 @ S0)).max())
S = sg * S0
Cperm = S @ S
d = (S[0, :] / S[0, 0]).real
Nv = np.einsum('il,jl,kl,l->ijk', S, S, S.conj(), 1.0 / S[0, :])
print(f"  |W(E6)| = {len(W)}   rank = {N}   c = {c:.6f}")
print(f"  S symmetric {np.abs(S-S.T).max():.2e}  unitary {np.abs(S@S.conj().T-np.eye(N)).max():.2e}"
      f"  (ST)^3=S^2 {np.abs(np.linalg.matrix_power(S@T,3)-Cperm).max():.2e}")
print(f"  Verlinde integral {np.abs(Nv-np.rint(Nv.real)).max():.2e}  min {np.rint(Nv.real).min():.0f}")
flip = lambda t: (t[5], t[1], t[4], t[3], t[2], t[0])
idx = {p: i for i, p in enumerate(PRIM)}
assert [int(np.argmax(np.rint(Cperm.real)[i])) for i in range(N)] == [idx[flip(p)] for p in PRIM]
print("  C = S^2 IS the E6 diagram flip (gate)")
print(f"  qdims = {np.round(d, 6)}")
print(f"  h     = {[str(p) for p in PRIM]}")
print(f"          {np.round(h, 6)}")

# ============================================================ CELL 2
print("\n" + "=" * 78)
print("CELL 2 -- the Deligne splitting, rebuilt independently")
print("=" * 78)
cur = [i for i in range(N) if abs(d[i] - 1) < 1e-9]
print(f"  objects with qdim 1 (simple currents): {cur}  ->  {[''.join(map(str,PRIM[i])) for i in cur]}")
fus = np.rint(Nv.real).astype(int)
closed = all(fus[a, b, cc] == 0 or cc in cur for a in cur for b in cur for cc in range(N))
table = [[next(cc for cc in range(N) if fus[a, b, cc]) for b in cur] for a in cur]
print(f"  closed under fusion: {closed}   fusion table (as indices): {table}")
Sp = S[np.ix_(cur, cur)]
detp = abs(np.linalg.det(Sp))
print(f"  |det S restricted to the currents| = {detp:.10f}  -> pointed subcategory MODULAR: {detp > 1e-9}")
cz = [i for i in range(N)
      if all(abs(S[i, j] - d[i] * d[j] * S[0, 0]) < 1e-9 for j in cur)]
print(f"  Mueger centraliser = {cz}  ->  {[''.join(map(str,PRIM[i])) for i in cz]}   rank {len(cz)}")
print(f"    its qdims = {np.round(d[cz], 6)}")
print(f"    its h     = {np.round(h[cz], 6)}   (as fractions of 1/21: {np.round(h[cz]*21)})")
# the Deligne product, under the bijection (current, centraliser object) -> object
pair, bij = {}, {}
for a in cur:
    for b in cz:
        k = next((kk for kk in range(N) if fus[a, b, kk]), None)
        pair[(a, b)] = k
        bij[k] = (a, b)
ok_bij = len(set(pair.values())) == N
Sc = S[np.ix_(cz, cz)] / S[0, 0]          # normalised centraliser S
Tc = np.diag(np.diag(T)[cz]) / T[0, 0]
errS = max(abs(S[pair[bij[i]], pair[bij[j]]] - Sp[cur.index(bij[i][0]), cur.index(bij[j][0])]
               * Sc[cz.index(bij[i][1]), cz.index(bij[j][1])] * S[0, 0] / S[0, 0])
           for i in range(N) for j in range(N)) if ok_bij else float('nan')
# recompute cleanly: S^{E6} = S^{pointed} (x) S^{centraliser-normalised-by-S00}
E = np.zeros((N, N), dtype=complex)
for i in range(N):
    for j in range(N):
        (a, b), (a2, b2) = bij[i], bij[j]
        E[i, j] = Sp[cur.index(a), cur.index(a2)] * Sc[cz.index(b), cz.index(b2)]
errS = float(np.abs(S - E).max())
ET = np.zeros((N, N), dtype=complex)
for i in range(N):
    (a, b) = bij[i]
    ET[i, i] = T[a, a] * Tc[cz.index(b), cz.index(b)]
errT = float(np.abs(np.diag(T) - np.diag(ET)).max())
print(f"  object bijection (current, centraliser) -> primary is a bijection: {ok_bij}")
print(f"  worst |S^E6 - S^pointed (x) S^centraliser| = {errS:.3e}")
print(f"  worst |T^E6 - T^pointed (x) T^centraliser| = {errT:.3e}")
cell2 = (len(cur) == 3 and closed and detp > 1e-9 and len(cz) == 3
         and errS < 1e-10 and errT < 1e-10)
print(f"\n  CELL 2 OUTCOME: {'A' if cell2 else 'B'}")

# ============================================================ CELL 3 + C2 + C3
print("\n" + "=" * 78)
print("CELL 3 -- is the rank-3 factor the unitary SU(2)_5-even, or a Galois conjugate?")
print("=" * 78)
print("  C2 (cross-bench) -- P2W5-L72 printed for its centraliser:  h = 0, 6/7, 9/7 ;"
      "  qdim = 1, 1.801938, 2.24698")
mine_h = sorted(round(x % 1, 9) for x in h[cz])
theirs_h = sorted(round(x % 1, 9) for x in (0, 6 / 7, 9 / 7))
mine_d = sorted(round(float(x), 6) for x in d[cz])
print(f"     this bench: h mod 1 = {mine_h}   qdim = {mine_d}")
print(f"     P2W5-L72  : h mod 1 = {theirs_h}   qdim = {sorted([1.0, 1.801938, 2.24698])}")
assert mine_h == theirs_h, "centraliser twists disagree with the cell"
assert all(abs(a - b) < 1e-5 for a, b in zip(mine_d, sorted([1.0, 1.801938, 2.24698])))
print("     C2 PASSES: two independent builds agree on the centraliser.")

print("\n  the Galois sweep over k' in (Z/7)*  [SU(2)_5 even part, spins j = 0,1,2]:")
J = [0, 1, 2]
best = []
for kp in range(1, 7):
    Sg = np.array([[np.sqrt(2 / 7) * np.sin(np.pi * kp * (2 * a + 1) * (2 * b + 1) / 7)
                    for b in J] for a in J])
    hg = np.array([kp * j * (j + 1) / 7 for j in J])
    dg = Sg[0, :] / Sg[0, 0]
    # match by sorting both sides on (h mod 1, qdim) -- a permutation-free comparison
    ordm = sorted(range(3), key=lambda i: (round(h[cz][i] % 1, 9), round(d[cz][i], 6)))
    ordg = sorted(range(3), key=lambda i: (round(hg[i] % 1, 9), round(dg[i], 6)))
    Sm = (S[np.ix_([cz[i] for i in ordm], [cz[i] for i in ordm])] / S[0, 0]).real
    Sgg = (Sg[np.ix_(ordg, ordg)] / Sg[0, 0])
    eS = float(np.abs(Sm / np.linalg.norm(Sm) - Sgg / np.linalg.norm(Sgg)).max())
    eT = max(abs(np.exp(2j * np.pi * (h[cz][ordm[i]] - h[cz][ordm[0]]))
                 - np.exp(2j * np.pi * (hg[ordg[i]] - hg[ordg[0]]))) for i in range(3))
    print(f"    k'={kp}  qdims {np.round(np.sort(dg),6)}   worst|dS| {eS:.3e}   worst|dT| {eT:.3e}"
          f"   {'MATCH' if (eS < 1e-10 and eT < 1e-10) else 'reject'}")
    best.append((kp, eS, eT, eS < 1e-10 and eT < 1e-10))
matches = [b[0] for b in best if b[3]]
rejects = [b[0] for b in best if not b[3]]
print(f"\n  C3 (MB12 transversality): conjugates REJECTED = {rejects}  (must be non-empty)")
if not rejects:
    print("  *** C3 FAILED -- CELL 3 may not be read (memo 164). Stopping.")
    raise SystemExit(1)
print(f"  matches: {matches}")
print(f"  CELL 3 OUTCOME: {'A' if len(matches) == 1 else 'B'}")

print("\n" + "=" * 78)
print("DONE -- outcomes above; interpretation lives in the memo, not here.")
print("=" * 78)
