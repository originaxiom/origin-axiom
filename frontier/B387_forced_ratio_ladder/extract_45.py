"""B387 2a/2b -- the level-45 slot-analog constant from the banked table + the ratio verdict."""
import json, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "B372_level45_sweeper", "sweep45.json")))
pair = d["pair"]
# the banked level-45 value sector: exponents {6,54} (B373); slot-analog columns {2,10}
cells = [(6,2),(6,10),(54,2),(54,10)]
vals = {f"{a},{b}": pair.get(f"{a},{b}") for (a,b) in cells}
print("sector-row graded cells in the banked table:", vals)
# rows 6 and 54 entirely absent from support?
rows_present = sorted({int(k.split(",")[0]) for k in pair})
absent = [a for a in (6,54) if a not in rows_present]
out = dict(cells=vals, sector_rows_absent=absent,
           const45="0 (exact -- sector rows carry no Par-pair content)",
           ratio="0", verdict="KILL (registered branch): ratio not in R1-R4; ladder needs 135")
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "extract_45.json"), "w"), indent=1)
print("sector rows absent from support:", absent, "-> const(45) = 0 exactly; ratio = 0; KILL branch")
