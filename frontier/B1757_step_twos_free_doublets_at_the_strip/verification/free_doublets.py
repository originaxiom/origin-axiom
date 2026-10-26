"""B1757 (POST HOC data, labelled; at the SM seat's ask, its relay §277): step 2's two free Higgs doublets at the six's
strip (P-377; S217's audit-room run `two_doublets_at_the_strip.py`, which stored only the pulls), rerun with the same
starts, seeds and fit, and this time writing the fitted vectors.  Both doublets read S, the leptons with H_d, c = 3;
B1656's frame at B1667's end through B1743's tracked modules (pencils.py, target.py); points on (2/5, 1/10) at Im tau
2.95-3.10; both horocycles.  nine2() is S217's audit-room function, carried verbatim.  Each vector is normalised and its
largest component made real and positive (the chi-square is blind to each doublet's overall phase).
    python3 -B free_doublets.py [--workers 2]      # writes free_doublets.json"""
import sys, json, math, pathlib
from multiprocessing import Pool
import numpy as np
from scipy.optimize import least_squares
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
import pencils as P      # noqa: E402
POINTS = [(1, 0.3145, 3.0345), (1, 0.333333, 3.055050), (1, 0.3145, 3.10), (1, 0.3145, 2.95)]


def nine2(hu, hd, M, hor, B):
    Su, Sd = P.R.Smat(list(hu), B), P.R.Smat(list(hd), B)
    Y = {"up": B.coupling(Su, M[("up", hor)]), "down": B.coupling(Sd, M[("down", hor)]), "lep": B.coupling(Sd, M[("lep", hor)])}
    six = []
    for s in ("up", "down", "lep"):
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300); six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, P.LC, -P.LC])
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    ck = np.log(np.maximum([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])], 1e-300))
    return (np.concatenate([six, ck]) - P.T9) / P.S9


def canon(v):
    v = np.asarray(v, dtype=complex); v = v / np.linalg.norm(v); k = int(np.argmax(np.abs(v)))
    return v * np.exp(-1j * np.angle(v[k]))


def both_free(task):
    k, re_t, im_t = task; a, b = P.LINES[k]; B = P.R.CEN._modules()["B"]; M = P.SC.channels(re_t, im_t, a, b)
    F = P.forms(complex(re_t, im_t)); rng = np.random.default_rng(int(1e4 * re_t + 100 * im_t + k)); out = []
    cands = [F[x] for x in F] + [np.conj(F[x]) for x in F]
    for hor in ("L_max", "L_2"):
        best = (np.inf, None, None, None)
        starts = [(cu, cd) for cu in cands[:8] for cd in cands[:8]] + [(rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)) for _ in range(40)]
        sc = sorted(((float((nine2(u / np.linalg.norm(u), d / np.linalg.norm(d), M, hor, B) ** 2).sum()), u, d) for u, d in starts), key=lambda x: x[0])[:8]
        for _, u0, d0 in sc:
            cv = lambda p: (np.array([p[0] + 1j * p[1], p[2] + 1j * p[3], p[4] + 1j * p[5]]), np.array([p[6] + 1j * p[7], p[8] + 1j * p[9], p[10] + 1j * p[11]]))
            f = lambda p: nine2(*cv(p), M, hor, B)
            r = least_squares(f, np.concatenate([[x.real, x.imag] for x in list(u0) + list(d0)]), method="trf", max_nfev=600)
            c = float((r.fun ** 2).sum())
            if c < best[0]:
                u, d = cv(r.x); best = (c, r.fun.tolist(), canon(u), canon(d))
        c, pulls, u, d = best
        out.append({"line": [str(a), str(b)], "tau": [re_t, im_t], "hor": hor, "chi2_nine": c, "pulls": pulls,
                    "H_u": [[float(z.real), float(z.imag)] for z in u], "H_d": [[float(z.real), float(z.imag)] for z in d],
                    "H_u_dot_H_u_over_norm2": abs(complex(np.sum(u * u))), "H_d_dot_H_d_over_norm2": abs(complex(np.sum(d * d)))})
    return out


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    with Pool(nw) as Pp: res = [x for part in Pp.map(both_free, POINTS) for x in part]
    json.dump(res, open(HERE / "free_doublets.json", "w"), indent=1)
    for r in res: print("tau %.4f+%.4fi %-5s chi2_nine %8.2f" % (r["tau"][0], r["tau"][1], r["hor"], r["chi2_nine"]))
    print("free_doublets exit 0")
