"""Pre-seal check Q8 (main, 2026-11-14; expectations in EXPECTATIONS_truncation.md, written first): the exact horoball norm
against the small-cut weight 2 pi L_2 + c_s, and its effect on world 1's seven claimed outputs averaged over the 24 lines
of order 5, at 8 points of the fundamental domain. Reuses the exact_end machinery on main (B1838's verification, its
functions imported unchanged). Writes truncation.json beside itself."""
import sys, json, math, pathlib, time
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.argv = ["x", str(ROOT)]
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1838_*")) / "verification"))
import exact_end_web_seat as E
B, C, K = E.B, E.C, E.K
HERE = pathlib.Path(__file__).resolve().parent
TAUS = [complex(0.25, 3.0), complex(0.3, 2.5), complex(0.0, 2.0), complex(0.25, 1.5), complex(0.0, 1.2),
        complex(0.0, 1.0), complex(0.25, 0.97), complex(0.45, 0.9)]
LINES = [(i / 5, j / 5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]


def outputs(rd, Mw):
    Yu = B.coupling(rd["St"], Mw["up"]); Yd = B.coupling(rd["S"], Mw["down"]); Ye = B.coupling(rd["S"], Mw["lep"])
    r = lambda Y: (lambda sv: [sv[1] / sv[0], sv[2] / sv[0]])(np.linalg.svd(Y, compute_uv=False))
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    return np.array(r(Yu) + r(Yd) + [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])])


if __name__ == "__main__":
    t0 = time.time(); res = []
    c = C.track(TAUS[0]); c, _ = C.solve_accessory(TAUS[0], c); prev = TAUS[0]
    for tau in TAUS:
        try:
            if tau != prev:
                c, _ = C.newton_walk(prev, c, tau); prev = tau
            G = E.geometry(tau, c); rd = E.higgs(tau)
        except Exception as ex:
            print("tau %s: geometry failed (%s)" % (tau, ex), flush=True); res.append({"tau": [tau.real, tau.imag], "failed": str(ex)}); continue
        acc = {"small": [], "exact": []}; gaps = []; failed = 0
        for a, b in LINES:
            w = a * tau + b; Mw = {"small": {}, "exact": {}}
            try:
                for sec, (lf, rf) in K.SECT.items():
                    x, y = B.sector_twists(w, tau, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, tau); cs = B.cA(x, y, tau, R)
                    Nx, _ = E.twisted_norms(tau, G["al"], G["be"], G["L_2"], x, y, R)
                    sm = {s: (2 * math.pi * G["L_2"] + cs[s] if cs[s] is not None else None) for s in B.UNITS}
                    gaps += [Nx[s] / sm[s] - 1 for s in B.UNITS if sm[s] and abs(R[s]) > 1e-12]
                    for kind, nm in (("small", sm), ("exact", Nx)):
                        u = {s: (math.sqrt(nm[s]) * R[s] if nm.get(s) is not None and nm[s] > 0 else 0) for s in B.UNITS}
                        Mw[kind][sec] = B.weighted_M(u)
                for kind in acc:
                    acc[kind].append(outputs(rd, Mw[kind]))
            except Exception as ex:
                failed += 1
        if not acc["small"]:
            res.append({"tau": [tau.real, tau.imag], "failed": "every line"}); continue
        Fs, Fx = np.mean(acc["small"], 0), np.mean(acc["exact"], 0)
        d = np.abs(np.log(Fx / Fs))
        row = {"tau": [tau.real, tau.imag], "L_2": G["L_2"], "lines": len(acc["small"]), "lines_failed": failed,
               "norm_gap_max": float(np.max(np.abs(gaps))), "norm_gap_median": float(np.median(np.abs(gaps))),
               "dln_seven": d.tolist(), "dln_max": float(d.max())}
        res.append(row)
        print("tau %s  L_2 %.3f  lines %d (failed %d)  norm gap median %.2e max %.2e  seven outputs max |d ln| %.2e  (%.0f s)" % (
            tau, G["L_2"], row["lines"], failed, row["norm_gap_median"], row["norm_gap_max"], row["dln_max"], time.time() - t0), flush=True)
    (HERE / "truncation.json").write_text(json.dumps(res, indent=1))
