"""B444 — extract the SL(3) Ptolemy (boundary-unipotent) equation systems.

Run under the pyenv env (needs SnapPy):  python3 extract_ptolemy.py
Writes sl3_ptolemy.json (equations + variables) for the sage elimination step.

The Ptolemy variety with obstruction_class=0 parametrises boundary-UNIPOTENT
SL(3,C) representations. For a hyperbolic ONE-cusped manifold this is a
0-dimensional variety, so it has a well-defined field of definition (the
"SL(3) elimination field"). Torus knots (e.g. 3_1) are non-hyperbolic and give
a POSITIVE-dimensional variety — no discrete field — which is itself the control
signal that the method is measuring hyperbolic arithmetic.
"""
import json
import snappy

KNOTS = ["4_1", "5_2", "3_1"]  # object ; decisive control ; degenerate (torus) control

out = {}
for name in KNOTS:
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=0)
    out[name] = {
        "eqs": [str(e) for e in V.equations],
        "vars": [str(v) for v in V.variables],
        "ntet": M.num_tetrahedra(),
    }
    print(f"{name}: {M.num_tetrahedra()} tet, {len(out[name]['vars'])} vars, "
          f"{len(out[name]['eqs'])} eqs")

with open("sl3_ptolemy.json", "w") as f:
    json.dump(out, f, indent=0)
print("[wrote sl3_ptolemy.json]")
