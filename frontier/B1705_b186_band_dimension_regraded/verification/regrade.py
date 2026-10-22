"""B1705 (Review 67, R66-4): B186's band box dimension re-graded.  At lambda = 0 the operator is Hermitian, so the band's
spectrum is real; B186's lock counted it in two dimensions after rescaling the general solver's noise-level imaginary
parts to unit range.  Here, under single-threaded and default BLAS (each in its own process): the lock's two-dimensional
value, the band counted on the line (the real parts, and eigvalsh), and the off-axis value (lambda = 2i, two-dimensional,
its imaginary parts genuine).
    python3 -B regrade.py      # writes regrade.json beside itself"""
import json, os, subprocess, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
CHILD = r'''
import importlib.util, json, sys
import numpy as np
spec = importlib.util.spec_from_file_location("t", sys.argv[1]); t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
def box1d(x, scales=2.0**np.arange(-2, -8, -1)):
    x = (x - x.min()) / np.ptp(x); Ns = [len({int(a // s) for a in x}) for s in scales]
    return float(np.polyfit(np.log(1 / scales), np.log(np.array(Ns, float)), 1)[0])
def herm(word):
    L = len(word); H = np.zeros((L, L)); i = np.arange(L - 1); H[i, i + 1] = 1; H[i + 1, i] = 1; H[0, L - 1] = 1; H[L - 1, 0] = 1
    return np.linalg.eigvalsh(H)
out = {}
for m, depth in [(1, 12), (2, 6)]:
    w = t._word(depth, m); ev = t._spectrum(w, 0.0)
    out[str(m)] = {"depth": depth, "band_imag_max": float(np.abs(ev.imag).max()), "d_band_lock_2d": t._box_dim(ev),
                   "d_band_line": box1d(np.sort(ev.real)), "d_band_line_eigvalsh": box1d(herm(w)), "d_off": t._box_dim(t._spectrum(w, 2.0j))}
print(json.dumps(out))
'''
LOCK = ROOT / "tests" / "test_b186_hyperbolicity_certification.py"
res = {}
for name, env in (("single-threaded BLAS", {"VECLIB_MAXIMUM_THREADS": "1", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}),
                  ("default BLAS", {})):
    e = {k: v for k, v in os.environ.items() if k not in ("VECLIB_MAXIMUM_THREADS", "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS")}
    e.update(env)
    r = subprocess.run([sys.executable, "-c", CHILD, str(LOCK)], capture_output=True, text=True, env=e, check=True)
    res[name] = json.loads(r.stdout)
res["the line count is BLAS-independent"] = all(abs(res["single-threaded BLAS"][m]["d_band_line"] - res["default BLAS"][m]["d_band_line"]) < 1e-12 for m in ("1", "2"))
res["the ordering holds by at least 0.1 at both settings"] = all(res[s][m]["d_band_line"] - res[s][m]["d_off"] > 0.1 for s in ("single-threaded BLAS", "default BLAS") for m in ("1", "2"))
json.dump(res, open(HERE / "regrade.json", "w"), indent=1)
print(json.dumps(res, indent=1))
