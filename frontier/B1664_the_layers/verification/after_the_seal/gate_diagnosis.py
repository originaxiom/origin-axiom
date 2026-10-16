"""POST-SEAL DIAGNOSIS (B1664's failed gate; labelled, not a cell): which threads give the NaN period-phase error, and
what is the phase error on all the others? The sealed instrument's own functions, rerun on every thread to trace 600."""
import importlib.util, math, pathlib, json
from multiprocessing import Pool
import numpy as np
P = pathlib.Path(__file__).resolve().parents[1] / "the_layers.py"
spec = importlib.util.spec_from_file_location("b1664", P); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def start_height(job):
    word, tr = job
    M = (1, 0, 0, 1)
    for ch in word:
        a, b, c, d = M; M = (a, a + b, c, c + d) if ch == "L" else (a + b, b, c + d, d)
    a, b, c, d = M; ell = 2*math.acosh(tr/2); disc = math.sqrt(tr*tr - 4)
    xa, xr = ((a - d) + disc)/(2*c), ((a - d) - disc)/(2*c); s0 = -ell/2 + 0.123*ell; w_ = 1j*math.exp(s0)
    return m.reduce_track((xa*w_ + xr)/(w_ + 1))[0].imag
def one(job):
    r = m.thread(job); return (job[0][:30], job[1], r.get("ph_err"), r.get("coh"), start_height(job))
if __name__ == "__main__":
    th = m.threads_upto(m.TMAX)
    with Pool(8) as pool: res = pool.map(one, th, chunksize=16)
    bad = [x for x in res if x[2] is None or not math.isfinite(x[2])]
    good = [x for x in res if x[2] is not None and math.isfinite(x[2])]
    out = dict(n=len(res), n_nan=len(bad), nan_start_heights_min=min(x[4] for x in bad) if bad else None,
               all_nan_start_above_cut=all(x[4] > m.YCUT for x in bad), any_good_start_above_cut=any(x[4] > m.YCUT for x in good),
               max_phase_err_others=max(x[2] for x in good), nan_examples=[x[0] for x in bad[:5]])
    print(json.dumps(out, indent=1)); (pathlib.Path(__file__).with_name("gate_diagnosis_output.json")).write_text(json.dumps(out, indent=1) + "\n")
