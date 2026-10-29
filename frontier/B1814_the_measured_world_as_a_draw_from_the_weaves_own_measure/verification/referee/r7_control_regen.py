"""Referee R7: regenerate control.json by calling the sealed census.py's control(pool) (imported read-only from the arc;
nothing written there) and compare with the committed control.json."""
import sys, json, hashlib, importlib.util, pathlib, time
from multiprocessing import Pool
ARC = pathlib.Path(__file__).resolve().parents[1]
src = ARC / "census.py"
assert hashlib.sha256(src.read_bytes()).hexdigest() == "6d95b183ec55cbae55a1394704a135ea53b9c3695e5db18654614d47b3349788"
sp = importlib.util.spec_from_file_location("b1814_census", src); C = importlib.util.module_from_spec(sp)
sys.modules["b1814_census"] = C; sp.loader.exec_module(C)
if __name__ == "__main__":
    t0 = time.time()
    with Pool(4) as P: c = C.control(P)
    old = json.loads((ARC / "control.json").read_text())
    new = json.loads(json.dumps(c))
    (pathlib.Path(__file__).resolve().parent / "r7_control.json").write_text(json.dumps(c, indent=1) + "\n")
    print("%.0f s" % (time.time() - t0)); print("identical:", new == old)
    for k in old:
        if new.get(k) != old[k]: print("differs", k, old[k], new.get(k))
