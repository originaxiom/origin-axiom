"""Smoke test before the seal (disclosed): the instrument on the rank-2 control only (C0's known answer), with timing."""
import importlib.util, pathlib, time
spec = importlib.util.spec_from_file_location("cp", pathlib.Path(__file__).resolve().parents[1] / "the_common_point.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.groups()
print({k: len(v) for k, v in G.items()})
for name in ("Dic2", "Dic3", "2T", "2O", "2I"):
    cp.ORDERS_CUR[0] = cp.ORDERS[name]; t = time.time()
    found, tested = cp.common_points(G[name], 2)
    print(f"n=2 {name}: tested {tested}, common points {[f['traces'] for f in found]}  ({time.time() - t:.2f} s)")
