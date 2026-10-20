"""Smoke test before the seal (disclosed): the targets' orders, and n = 2 for the CONTROLS only (Q8, H(3), H(5))."""
import importlib.util, pathlib, time
spec = importlib.util.spec_from_file_location("h", pathlib.Path(__file__).resolve().parents[1] / "the_common_point_in_higher_targets.py")
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
T = h.targets(); print({k: len(v) for k, v in T.items()})
for name in ("Q8 (SU2)", "H(3) (U3)", "H(5) (U5)"):
    t = time.time(); f, tested = h.common_points(T[name], 2, len(T[name]))
    print(f"n=2 {name}: filtered generating pairs {tested}, fixed by every move {f} ({time.time() - t:.1f} s)")
