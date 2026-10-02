#!/usr/bin/env python3
"""B1501 -- why check (4) of `post_run_checks.py` is a same-bench check (2026-10-02; main's S37 found it failing on one class).

Check (4) re-runs classes and compares their records with `census.json`, per-component seed counts included. The 400 seeds of a
class are Gaussian coordinates in the link's Lie-algebra basis (`torus_link_census.py`, `random_elements`). For S^6 and CP^3
that basis is an SVD null-space basis (lines 237 and 393 of the census script), which is unique only up to an orthogonal change,
and the linear-algebra library may return another one on another CPU kernel; S3xS3 and F12 use explicit bases. This script runs,
in fresh processes, the default kernel and OpenBLAS's Haswell kernel (OPENBLAS_CORETYPE=Haswell, read when numpy loads):
  (a) each link's basis, compared between the two kernels;
  (b) the class S^6 L(3/11, 3/11), the one S^6 class in check (4)'s sample: its converged count, its components (type,
      dimension, the fixed point) and its per-component seed split, against the record.
Nothing in the census is re-run beyond that one class.  Usage: python3 bench_dependence.py  (writes bench_dependence_run.txt)"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LABEL = "S6 L(3/11,3/11)"

CHILD = r'''
import json, sys, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location("b1501_census", sys.argv[1])
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
from numpy._core._multiarray_umath import __cpu_features__ as cpu
bases = {name: np.array(L().g_basis, dtype=complex) for name, L in T.LINKS.items()}
out = {"AVX512F": bool(cpu.get("AVX512F")), "bases": {n: [b.real.tolist(), b.imag.tolist()] for n, b in bases.items()}}
link = T.LINKS["S6"]()
cls = [c for c in T.enumerate_classes(link) if T.class_label(c) == sys.argv[2]][0]
r = T.run_class(link, cls)
out["record"] = {"converged": r["converged"],
                 "components": sorted([[c["dim"], c["topology"]["type"], [round(x, 6) + 0.0 for x in c["point (embedding)"]], c["seeds"]]
                                      for c in r["components"]], key=lambda z: z[2])}
print(json.dumps(out))
'''


def run(env_extra):
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", **env_extra)
    p = subprocess.run([sys.executable, "-c", CHILD, str(HERE / "torus_link_census.py"), LABEL], env=env, capture_output=True,
                       text=True, check=True)
    return json.loads(p.stdout.strip().splitlines()[-1])


def main():
    import numpy as np
    t0 = time.time()
    committed = [r for r in json.loads((HERE / "census.json").read_text(encoding="utf-8"))["records"] if r["label"] == LABEL][0]
    rec = {"class": LABEL, "numpy": np.__version__,
           "committed": {"converged": committed["converged"],
                         "components": sorted([[c["dim"], c["topology"]["type"], [round(x, 6) + 0.0 for x in c["point (embedding)"]],
                                                c["seeds"]] for c in committed["components"]], key=lambda z: z[2])}}
    runs = {"default kernel": run({}), "OPENBLAS_CORETYPE=Haswell": run({"OPENBLAS_CORETYPE": "Haswell"})}
    a, b = runs["default kernel"], runs["OPENBLAS_CORETYPE=Haswell"]
    rec["CPU has AVX-512"] = a["AVX512F"]
    rec["(a) basis max |difference| between the kernels"] = {
        name: float("%.2e" % np.abs((np.array(a["bases"][name][0]) + 1j * np.array(a["bases"][name][1]))
                                    - (np.array(b["bases"][name][0]) + 1j * np.array(b["bases"][name][1]))).max()) for name in a["bases"]}
    for k, r in runs.items():
        rec[f"(b) {k}"] = r["record"]
        rec[f"(b) {k}: same components as the record (dim, type, point)"] = (
            [z[:3] for z in r["record"]["components"]] == [z[:3] for z in rec["committed"]["components"]])
        rec[f"(b) {k}: same seed split as the record"] = (r["record"]["converged"] == rec["committed"]["converged"] and
                                                          [z[3] for z in r["record"]["components"]] == [z[3] for z in rec["committed"]["components"]])
    rec["seconds"] = round(time.time() - t0, 1)
    text = json.dumps(rec, indent=1, ensure_ascii=False)
    (HERE / "bench_dependence_run.txt").write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
