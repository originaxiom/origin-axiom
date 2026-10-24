"""B1747 (P-360): main's independent check of the web seat's sealed READING TEST on a seeded sample of its rows.
Under the Standard Model's reading (up sees the conjugate Higgs, down quarks and leptons the Higgs; c = 3), the minimum over
h in CP^2 of B1720's chi2_nine, on main's own instrument (B1740's via B1742's channels), from main's own starts (2 000 random
directions screened, the best ten and the record's forms refined by least squares) -- not the seat's optima.  Sample: the
seat's twenty lowest rows and twenty test rows drawn with seed 360."""
import sys, json, math, pathlib, subprocess
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import least_squares
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
import pencils as P      # noqa: E402


def git_json(path):
    return json.loads(subprocess.run(["git", "show", "origin/chat1/web-seat:" + path], cwd=ROOT, capture_output=True, text=True, check=True).stdout)


def nine_sm(h, M, hor, B):
    Su = P.R.Smat(list(np.conj(h)), B); Sd = P.R.Smat(list(h), B)
    Y = {"up": B.coupling(Su, M[("up", hor)]), "down": B.coupling(Sd, M[("down", hor)]), "lep": B.coupling(Sd, M[("lep", hor)])}
    six = []
    for s in ("up", "down", "lep"):
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300); six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, P.LC, -P.LC])
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    ck = np.log(np.maximum([abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])], 1e-300))
    return (np.concatenate([six, ck]) - P.T9) / P.S9, V


def row_min(line, re_t, im_t, hor):
    a, b = line; B = P.R.CEN._modules()["B"]; M = P.SC.channels(re_t, im_t, a, b); F = P.forms(complex(re_t, im_t))
    rng = np.random.default_rng(int(1000 * re_t + 100 * im_t) + (7 if hor == "L_2" else 0))
    cand = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(2000)]
    scored = sorted(((float((nine_sm(h / np.linalg.norm(h), M, hor, B)[0] ** 2).sum()), h) for h in cand), key=lambda x: x[0])
    starts = [h for _, h in scored[:10]] + [F[k] for k in F] + [np.conj(F[k]) for k in F]
    best = (scored[0][0], scored[0][1])
    for h0 in starts:
        f = lambda p: nine_sm(np.array([p[0] + 1j * p[1], p[2] + 1j * p[3], p[4] + 1j * p[5]]), M, hor, B)[0]
        r = least_squares(f, np.concatenate([[x.real, x.imag] for x in h0]), method="trf", max_nfev=400)
        c = float((r.fun ** 2).sum())
        if c < best[0]: best = (c, r.x)
    return best[0]


def task(t):
    line, re_t, im_t, hor, seat = t
    return {"line": [str(line[0]), str(line[1])], "tau": [re_t, im_t], "hor": hor, "seat": seat, "main": row_min(line, re_t, im_t, hor)}


if __name__ == "__main__":
    from multiprocessing import Pool
    HERE = pathlib.Path(__file__).resolve().parent
    cells = git_json("relays/chat1_2026-10-23_attack/reading_test_cells.json")
    idx = git_json("relays/chat1_2026-10-23_attack/reading_test_store_index.json")
    lines = [(Fr(a), Fr(b)) for _, a, b in idx["lines"]]
    tasks = []
    for r in cells["the twenty lowest rows"]:
        a, b = r["line"].strip("()").split(", "); tasks.append(((Fr(a), Fr(b)), r["tau"][0], r["tau"][1], r["hor"], r["chi2_nine"]))
    rr = git_json("relays/chat1_2026-10-23_attack/reading_test_rows.json")["rows"]
    rng = np.random.default_rng(360); test = [r for r in rr if r.get("p", 10 ** 9) < len(idx["tasks"]) and not r.get("degenerate")]
    for j in rng.choice(len(test), size=20, replace=False):
        r = test[int(j)]; k, re_t, im_t = idx["tasks"][r["p"]]; tasks.append((lines[k], re_t, im_t, r["hor"], r["chi2_nine"]))
    with Pool(8) as Pp: out = Pp.map(task, tasks)
    (HERE / "sm_reading_check.json").write_text(json.dumps(out, indent=1) + "\n")
    lo = min(o["main"] for o in out)
    print("rows checked", len(out), "| main's lowest chi2_nine %.2f | rows below 21.67: %d | below 100: %d" % (lo, sum(o["main"] < 21.67 for o in out), sum(o["main"] < 100 for o in out)))
    print("main below the seat by more than 1%% on %d rows; median main/seat %.3f" % (sum(o["main"] < 0.99 * o["seat"] for o in out), float(np.median([o["main"] / o["seat"] for o in out]))))
    for o in out[:6]: print(o)
