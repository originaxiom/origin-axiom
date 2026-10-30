"""STEP A v2 -- the vacuum directions against the record's declared directions (data-free):
    python3 -I analysis_vacua.py -> analysis_vacua.json
For every interior vacuum of section D (primary convention), 1 - |<S*, Y(tau*)>| / |Y(tau*)| for the declared directions
evaluated at the vacuum's own tau*: DR, a0 (= F_-2 as a direction, checks_extra 5), R (= F_2), and B1730's one-unit F_a.
(B1810's t = -5/288 is not reconstructed here.)  Also: the n = 2 vacua against Y1 x Y2 at tau*."""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
from model import Triplet, form_values, unit
from search import Model, make_copies, fs_dist

d = json.loads((HERE / "step_a_v2.json").read_text())
DECL = [("DR", Triplet("DR"))] + [("F_%d" % a, Triplet("F", a)) for a in (-10, -6, -2, 2, 6, 10, 14, 18, 22, 26)]


def dirs_at(tau):
    th, dth, ddth, E4, E6, ae = form_values(tau)
    out = {}
    for name, T in DECL:
        v, f = T.vec_noeta(th, dth, ddth, E4); out[name] = unit(v)
    return out


rows = []; mins = []
for r in d["D"]["configs"]:
    if "best" not in r or r["tnorm"] != "N":
        continue
    b = r["best"]
    tau = complex(*b["tau"]); S = np.array([complex(*c) for c in b["S"]])
    dd = dirs_at(tau)
    dev_h = {k: float(1 - abs(np.vdot(v, S))) for k, v in dd.items()}                    # Hermitian overlap (Fubini-Study)
    row = dict(menu=r["menu"], n=r["n"], mu2=r["mu2"], m02=r["m02"], lv=r["lv"], tau=b["tau"],
               min_dev_hermitian=min(dev_h.values()), argmin=min(dev_h, key=dev_h.get))
    if r["n"] == 2:
        m = Model(make_copies(2, r["menu"]), r["mu2"], r["m02"], r["lv"])
        A, D, W = m.pieces(tau)
        row["fs_to_cross_product"] = fs_dist(S, np.cross(W[0], W[1]))
    rows.append(row); mins.append(row["min_dev_hermitian"])
out = dict(rows=rows, smallest_over_all_vacua=min(mins) if mins else None,
           reading="1 - |<S*, Y_hat(tau*)>|: zero iff the vacuum direction equals that declared direction at the same tau")
(HERE / "analysis_vacua.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("vacua compared:", len(rows), " smallest 1-overlap with a declared direction at the same tau*: %.3g" % out["smallest_over_all_vacua"])
for row in rows:
    if row["n"] == 2:
        print("  n=2 %s mu2=%.1f lv=%.1f m0^2/mu2=%.2f tau*=%.5f%+.5fi  FS(S*, Y1xY2)=%.1e  nearest declared %s (1-ov %.3f)" % (
            row["menu"], row["mu2"], row["lv"], row["m02"] / row["mu2"], row["tau"][0], row["tau"][1], row["fs_to_cross_product"],
            row["argmin"], row["min_dev_hermitian"]))
