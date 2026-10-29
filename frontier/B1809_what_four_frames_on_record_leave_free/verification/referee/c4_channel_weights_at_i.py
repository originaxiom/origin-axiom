"""c4: the channel weights 2 pi L + c_r at tau = i (zero line) at B1667's canonical radii -- how close L_max(i) sits to a
channel's switch-off (the record's u_r = sqrt(2 pi L + c_r) R_r, set to 0 when the bracket is <= 0)."""
import pathlib, math, json
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
B = g["B"]
t = 1j; x, yy = B.sector_twists(0, t, 1, -4); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
out = {"c_r": {k: c[k] for k in B.UNITS}, "|R_r|": {k: abs(R[k]) for k in B.UNITS}}
for Ln, L in (("L_max(i)", g["LI"][0]), ("L_2(i)", g["LI"][1])):
    out[Ln] = {k: (2 * math.pi * L + c[k] if c[k] is not None else None) for k in B.UNITS}
print(json.dumps(out, indent=1, default=str))
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
