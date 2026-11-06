"""P-455 on P-717's excursion (data-free, frame-internal): along one period of the axis of A = L^5 R (LR)^5 (in the coordinates
where its apex is at Re 1/2), the frame's per-sector singular-value ratios at E4 = L_2 - pi/2, with the thread's own line
(2/5, 4/5) carried along; each point reduced to the fundamental domain by T and S with the line transformed (v -> v g^-1).
Compares the ratios at the apex with their hyperbolic-arclength average over the period. No measured number is read."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"): os.environ.setdefault(_v, "1")
import sys, math, json, time, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier/B1842_the_closure_instruments/verification"))
import exact_card_instrument as X
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5
# the axis of A in apex coordinates (from audit/drafts/p718/compat.py's search): apex Re 1/2, Im h; radius h; translation length l
def mat(s):
    L = np.array([[1,0],[1,1]], dtype=object); R = np.array([[1,1],[0,1]], dtype=object); M = np.eye(2, dtype=object)
    for ch in s: M = M.dot(L if ch == 'L' else R)
    return M
h = 3.118047822312      # k = 5 approximant's apex height (P-717's control)
trA = int(sum(mat('L'*5 + 'R' + 'LR'*5)[i][i] for i in range(2)))
ell = 2 * math.acosh(trA / 2)
def reduce_full(tau, a, b):
    a, b = Fr(a), Fr(b)
    for _ in range(200):
        while tau.real > 0.5: tau, b = tau - 1, (b + a) % 1
        while tau.real < -0.5: tau, b = tau + 1, (b - a) % 1
        if abs(tau) < 1 - 1e-12:
            tau = -1 / tau; a, b = (-b) % 1, a % 1          # (tau, v) ~ (S tau, v S^-1), v S^-1 = (-b, a)
        else: break
    return tau, a, b
def point(t):
    tau = complex(0.5 + h * math.tanh(t), h / math.cosh(t))
    tr, a, b = reduce_full(tau, "2/5", "4/5")
    Y0, info = X.yukawas_exact(tr.real, tr.imag, a, b, 0.0, ("up", "down", "lep"))
    d = info["L_2"] - math.pi / 2 - info["L_max"]
    Y, info = X.yukawas_exact(tr.real, tr.imag, a, b, d, ("up", "down", "lep"))
    out = {}
    for sec in ("up", "down", "lep"):
        for rn in ("S", "St"):
            r = X.ratios_of(np.asarray(Y[sec][rn]))
            out[sec + "_" + rn] = [math.log(max(x, 1e-300)) for x in r]
    return tau, tr, (str(a), str(b)), out
if __name__ == "__main__":
    ts = np.linspace(-ell / 2, ell / 2, N, endpoint=False) + (ell / N) / 2 if N > 1 else np.array([0.0])
    t0 = time.time(); rows = []
    for t in ts:
        tau, tr, ln, out = point(float(t)); rows.append({"t": float(t), "tau": [tau.real, tau.imag], "reduced": [tr.real, tr.imag], "line": ln, "lnratios": out})
        print("t %+.3f  tau %.4f+%.4fi -> reduced %.4f+%.4fi line %s  up_St %s down_S %s  (%.0f s)" % (t, tau.real, tau.imag, tr.real, tr.imag, ln,
              ["%.2f" % x for x in out["up_St"]], ["%.2f" % x for x in out["down_S"]], time.time() - t0), flush=True)
    json.dump({"tr_A": trA, "ell": ell, "h": h, "rows": rows}, open(pathlib.Path(__file__).parent / ("period_N%d.json" % N), "w"), indent=1)
