"""c2: reproduce S248's 0.2724 (L = 0.65) and 0.0211 (L = 2.5) for a ∝ R at tau = i with the same machinery as c1,
and the L-dependence of m2/m3(i) for a ∝ R between B1667's two canonical radii (sensitivity to the horocycle choice)."""
import importlib.util, pathlib, json
spec = importlib.util.spec_from_file_location("c1", pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
masses, secs = g["masses"], g["secs"]
out = {}
for L in (0.65, 0.688385709056232, 0.8, 1.0, 1.5, 2.0, 2.5, 2.7192576281085956, 10.0):
    m1, m2 = masses(secs["R (k=-1/2)"], 1j, L)
    m1b, m2b = masses(secs["a0 (k=7/2)"], 1j, L)
    out["%.6g" % L] = {"R: m2/m3": "%.5g" % m2, "a0: m1/m3": "%.5g" % m1b, "a0: m2/m3": "%.5g" % m2b}
    print(L, out["%.6g" % L], flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
