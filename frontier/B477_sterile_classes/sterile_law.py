#!/usr/bin/env python3
"""B477 — the sterile-class law: introspect the SL(2) obstruction classes for
L6a4/s776/m129, extract each class's cocycle data, and test the simplest laws
against the banked B461 emptiness table."""
import snappy

BANKED = {  # from B461 FINDINGS: status per SL(2) obstruction class index
 's776': {'nonempty': {0: 'dim3-geom', 13: 'dim1'} | {k: 'dim0' for k in (1,2,3)},  # 3 zero-dim classes Q(sqrt-7); F_p dims: 0->3, 1-12->0, 13->1
 },
}
for nm in ['L6a4', 's776', 'm129']:
    M = snappy.Manifold(nm)
    print(f"== {nm}: cusps={M.num_cusps()}, H1={M.homology()} ==", flush=True)
    V = M.ptolemy_variety(2, obstruction_class='all')
    print(f"  {len(V)} obstruction classes", flush=True)
    v0 = V[0]
    print("  variety attrs:", [a for a in dir(v0) if 'obstruction' in a.lower() or 'class' in a.lower()], flush=True)
    for i, v in enumerate(V):
        oc = getattr(v, '_obstruction_class', None)
        info = None
        if oc is not None:
            for attr in ('H2_class', 'class_index', '_H2_class', 'identified_face_classes'):
                if hasattr(oc, attr):
                    info = (attr, getattr(oc, attr)); break
            if info is None:
                info = ('repr', repr(oc)[:100])
        print(f"   class {i}: {info}", flush=True)
print("STERILE INTROSPECT DONE", flush=True)
