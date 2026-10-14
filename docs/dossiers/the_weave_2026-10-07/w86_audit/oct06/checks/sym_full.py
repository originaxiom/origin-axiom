"""Audit: are SnapPy's symmetry groups in the listening log certified full? Same tick construction as listening_log.py."""
import snappy
ACTS = {'golden': (1, 'b-+L'), 'silver': (2, 'b-+LL'), 'bronze': (3, 'b-+LLL')}
for act, (m, name) in ACTS.items():
    Lw, Rw = 'L' * m, 'R' * m
    def tick(k):
        return snappy.Manifold('b++' + (Lw + Rw) * (k // 2)) if k % 2 == 0 else snappy.Manifold('b-+' + Lw + (Rw + Lw) * ((k - 1) // 2))
    row = []
    for k in range(1, 11):
        C = tick(k); G = C.symmetry_group()
        cs = float(C.chern_simons()) if C.is_orientable() else None
        row.append((k, G.order(), G.is_full_group(), None if cs is None else round(cs, 12)))
    print(act, row, flush=True)
