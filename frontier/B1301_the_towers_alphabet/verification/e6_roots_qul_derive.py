#!/usr/bin/env python3
"""Derive the E6 roots' coordinates modulo the SM roots in the basis (w_Q, w_u^c, w_L) from B1277's descent data (the
loaders take about two minutes); write e6_roots_qul.json: for each of the 72 roots its (Q, u^c, L) triple and whether it is
an SU(5) root (orthogonal to the weights of N and nu^c), plus the 27's table as a control against B1300."""
import sys, json, pathlib, time
from fractions import Fraction as F
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for arc in ("B1267_spectrum_law_rebuilt", "B1268_cusped_net_chirality_bound", "B1269_transport_computed",
            "B1273_the_three_fold_closing", "B1274_the_tower_and_its_doubles", "B1275_the_cubic_made_explicit",
            "B1276_the_relations_the_chain_forces", "B1277_the_vacuum_manifold_of_the_closing", "B1278_the_six_fold_closing"):
    sys.path.insert(0, str(ROOT / "frontier" / arc / "verification"))
from six_fold_closing import C, R, VM, smith_with_transforms

def derive():
    t0 = time.time()
    wts, rep = C.load(); lab, hy, wts2 = R.sm_labels(); assert wts2 == wts
    sub, Y, rts, Mf, ip, a1, a2 = VM.descent_data()
    sm_roots = sorted(set(a2) | {a1, tuple(-x for x in a1)})
    Rm = sp.Matrix([list(a) for a in sm_roots]); D, U, V = smith_with_transforms(Rm)
    dprime = [int(D[j, j]) for j in range(min(D.shape))]; rank = sum(1 for d in dprime if d != 0)
    assert dprime[:rank] == [1] * rank and rank == 3
    free = list(range(rank, 6)); VT = V.T
    smith = lambda w: tuple(int(x) for x in (VT * sp.Matrix(list(w))))[rank:]
    comp = {l: next(i for i in range(27) if lab[i] == l) for l in ('Q', 'u^c', 'L')}
    B = sp.Matrix([smith(wts[comp['Q']]), smith(wts[comp['u^c']]), smith(wts[comp['L']])]).T
    assert abs(B.det()) == 1
    Binv = B.inv()
    qul = lambda w: tuple(int(x) for x in (Binv * sp.Matrix(smith(w))))
    iN = next(i for i in range(27) if lab[i] == 'S'); inc = next(i for i in range(27) if lab[i] == 'nu^c')
    wN, wnc = [F(x) for x in wts[iN]], [F(x) for x in wts[inc]]
    roots = []
    for a in rts.values():
        roots.append(dict(root=[int(x) for x in a], qul=qul(a), su5=bool(ip(a, wN) == 0 and ip(a, wnc) == 0), sm=tuple(a) in set(sm_roots)))
    table = {}
    for i in range(27):
        table.setdefault(lab[i], qul(wts[i]))
        assert table[lab[i]] == qul(wts[i])
    out = dict(roots=roots, table27=table, n_su5=sum(r['su5'] for r in roots), n_sm=sum(r['sm'] for r in roots), seconds=round(time.time() - t0))
    (HERE / 'e6_roots_qul.json').write_text(json.dumps(out))
    return out

if __name__ == "__main__":
    out = derive()
    print(f"72 roots: {len(out['roots'])}; SU(5) roots {out['n_su5']}; SM roots {out['n_sm']}; roots with trivial (Q,u,L) coordinates: {sum(1 for r in out['roots'] if r['qul'] == (0, 0, 0))}")
    print("table of the 27:", out['table27'])
    print(f"({out['seconds']} s)")
