#!/usr/bin/env python3
"""B1483 cell C2b: B1477's zero_witness.witness, unchanged, on o10_150729 (m003's five-cusped cyclic cover of degree 5)."""
import sys, json, pathlib, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent; FR = next(p for p in HERE.parents if p.name == "frontier")
sys.path.insert(0, str(FR / "B1477_what_decides_the_swap_the_mirrors_shear_on_the_cusp" / "verification"))
import zero_witness as ZW
r = ZW.witness("o10_150729")
json.dump(r, open(HERE / "witness_o10_150729.json", "w"), indent=0, default=str)
print(json.dumps({k: v for k, v in r.items() if k not in ("spectrum_rows",)}, default=str)[:1500])
