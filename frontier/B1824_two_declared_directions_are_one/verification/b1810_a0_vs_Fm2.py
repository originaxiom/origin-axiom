"""B1824's consequence on a committed table: in B1810's symmetry-selection table (data-free outputs of the frame at the
four configurations the object's symmetry fixes), the rows of direction a0 and of direction F_-2 must coincide in every
mass ratio, row by row (same configuration, radius and reading); |V| and J only where V is defined."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]   # frontier/B1824_*/verification/ -> the root
d = json.loads((ROOT / "frontier/B1810_the_symmetry_selection_value_table/verification/symmetry_selection_table.json").read_text())
rows = d["rows"]
key = lambda r: (r["config"], r["radius"], r["reading"])
A = {key(r): r for r in rows if r["direction"] == "a0"}; F = {key(r): r for r in rows if r["direction"] == "F_-2"}
assert set(A) == set(F), (len(A), len(F))
dm = 0.0; dv_def = 0.0; dv_undef = 0.0; n_def = 0; n_undef = 0; dJ = 0.0
for k in A:
    a, f = A[k], F[k]
    for s in ("up", "down", "lepton"):
        dm = max(dm, max(abs(x - y) for x, y in zip(a[s], f[s])))
    va = [x for row in a["|V| (3x3)"] for x in row]; vf = [x for row in f["|V| (3x3)"] for x in row]
    dv = max(abs(x - y) for x, y in zip(va, vf))
    if a["V defined"] and f["V defined"]:
        n_def += 1; dv_def = max(dv_def, dv); dJ = max(dJ, abs(a["J"] - f["J"]))
    else:
        n_undef += 1; dv_undef = max(dv_undef, dv)
out = dict(pairs=len(A), max_mass_ratio_difference=dm, V_defined_pairs=n_def, max_V_difference_where_defined=dv_def,
           max_J_difference_where_defined=dJ, V_undefined_pairs=n_undef, max_V_difference_where_undefined=dv_undef)
print(json.dumps(out, indent=1))
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
