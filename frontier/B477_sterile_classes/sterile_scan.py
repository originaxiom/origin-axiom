#!/usr/bin/env python3
"""B477 recon — the sterile obstruction classes: which H^2 classes carry no
representations, per manifold, per rank; correlate with the class structure."""
import json, sys
sys.path.insert(0, '../B461_relation_r2_borromean')
import snappy

d = json.load(open('../B461_relation_r2_borromean/ptolemy_systems.json'))
for nm in ['L6a4', 's776', 'm129']:
    M = snappy.Manifold(nm)
    print(f"== {nm} (cusps: {M.num_cusps()}, H1: {M.homology()}) ==", flush=True)
    for rank_key, label in (('2', 'SL(2)'), ('3', 'SL(3)')):
        if rank_key not in d[nm]: continue
        # obstruction classes from snappy for cross-reference
        try:
            V = M.ptolemy_variety(int(rank_key), obstruction_class='all')
            n_classes = len(V)
        except Exception as e:
            n_classes = f"err {e}"
        print(f"  {label}: {len(d[nm][rank_key])} exported classes (snappy reports {n_classes})", flush=True)
print("STERILE SCAN CONTEXT DONE", flush=True)
