#!/usr/bin/env python3
"""TWO_INGREDIENTS_RULE.md: main's fibre frame (B1720's instrument at main's 3412bf09d, unchanged) on B1713's 266
lines at Re tau in {0.1, 0.4}, Im tau = 2.0 .. 3.5 (step 0.1), both horocycles; every sector with every Higgs
reading (S, St = eps S* eps^T, conjS), and the CKM (B1713's left-vector convention) for every (up, down) reading pair.
No data.  Checkpointed: each point is appended to two_ingredients_census.jsonl as it completes; a rerun skips done
points.  The control C1 compares this instrument with main's own ratios_at at one point.
    python3 -B two_ingredients_census.py [--workers 2] [--max-seconds 6600]"""
import hashlib, io, json, math, os, subprocess, sys, tempfile, time, contextlib, pathlib
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
REV = "3412bf09d"
FILES = {
    "frontier/B1720_the_thread_fixes_the_point/verification/b1656_funcs.py": "31f09c433c14312d9cee8cfa29a632a72ce13fc46ae838757bf9b22958f22528",
    "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.py": "6ba0ff01e77cbe2019b54fd66f1b7eb1215360ae7a28caedf90c569d62bc399b",
    "frontier/B1720_the_thread_fixes_the_point/verification/thread_geometry.py": "2d783fbe5e822f4bbc17929c79065c84886331eb69ffd46f14d4ef4968d7eae9",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py": "a8d4ea9bae79dde894b192b7c3645685c1c97890665c96123be20ea6e9073aac",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py": None,
    "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json": "688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774",
}
OUTL = HERE / "two_ingredients_census.jsonl"

TMP = pathlib.Path(os.environ.get("TI_TMP") or tempfile.mkdtemp())
if not (TMP / "GENESIS.md").exists():
    for rel, sha in FILES.items():
        b = subprocess.run(["git", "show", f"{REV}:{rel}"], cwd=ROOT, capture_output=True, check=True).stdout
        if sha is not None:
            assert hashlib.sha256(b).hexdigest() == sha, rel
        p = TMP / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
    (TMP / "GENESIS.md").write_text("root marker for the imported instrument\n")
os.environ["TI_TMP"] = str(TMP)                      # the pool's workers import from the same tree
VDIR = TMP / "frontier/B1720_the_thread_fixes_the_point/verification"
sys.path.insert(0, str(VDIR)); _argv = sys.argv; sys.argv = ["x"]
with contextlib.redirect_stdout(io.StringIO()):
    import the_thread_census as TC
sys.argv = _argv
import numpy as np
import mpmath as mp
B, te = TC.B, TC.te


def _lines(lo, hi):                                   # B1713's list, verbatim logic
    seen, out = set(), []
    for N in range(lo, hi + 1):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N); na, nb = (-a) % 1, (-b) % 1
                key = min((a, b), (na, nb))
                if key in seen:
                    continue
                seen.add(key); out.append(("N=%d" % N, key[0], key[1]))
    return out


LINES = _lines(1, 7) + _lines(8, 12)
RE = [0.1, 0.4]
IM = [round(2.0 + 0.1 * j, 2) for j in range(16)]
TASKS = [(k, r, y) for k in range(len(LINES)) for r in RE for y in IM]


def ckm_left(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]


def evaluate(re_t, im_t, a, b):
    t = complex(re_t, im_t); w = a * t + b
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    readings = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T, "conjS": np.conj(S)}
    res, Y = {}, {}
    for sec, (lf, rf) in TC.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        for which in ("L_max", "L_2"):
            L = TC.L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * R[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M = B.weighted_M(u)
            for rn, SS in readings.items():
                Ym = B.coupling(SS, M); Y[(sec, which, rn)] = Ym
                sv = np.linalg.svd(Ym, compute_uv=False)
                res["%s|%s|%s" % (sec, which, rn)] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    for which in ("L_max", "L_2"):
        for ru in readings:
            for rd in readings:
                res["ckm|%s|%s|%s" % (which, ru, rd)] = ckm_left(Y[("up", which, ru)], Y[("down", which, rd)])
    return res


def point(task):
    k, re_t, y = task
    tag, a, b = LINES[k]
    r = evaluate(re_t, y, float(a), float(b))
    r.update({"line": k, "Re_tau": re_t, "Im_tau": y})
    return r


def control():
    t, a, b = complex(0.5, 3.08), 2 / 5, 1 / 10
    mine = evaluate(t.real, t.imag, a, b)
    ours = [x for sec in ("up", "down", "lep") for x in mine["%s|L_max|S" % sec]]
    main = TC.ratios_at(t, a, b)
    return {"tau": [0.5, 3.08], "line": [a, b], "this_instrument": ours, "main_ratios_at": main,
            "max_abs_log": max(abs(math.log(p / q)) for p, q in zip(ours, main))}


if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    budget = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    done = set()
    if OUTL.exists():
        for line in OUTL.read_text().splitlines():
            if line.strip():
                r = json.loads(line); done.add((r["line"], r["Re_tau"], r["Im_tau"]))
    todo = [tk for tk in TASKS if tk not in done]
    print(f"{len(TASKS)} points; {len(done)} done; {len(todo)} to do", flush=True)
    if not (HERE / "two_ingredients_control.json").exists():
        (HERE / "two_ingredients_control.json").write_text(json.dumps(control(), indent=1) + "\n")
    t0 = time.time(); n = 0
    with Pool(nw) as P, open(OUTL, "a") as fh:
        for r in P.imap_unordered(point, todo, chunksize=2):
            fh.write(json.dumps(r) + "\n"); fh.flush(); n += 1
            if time.time() - t0 > budget:
                print(f"budget reached after {n} points; rerun to resume", flush=True)
                P.terminate(); break
    print(f"wrote {n} points in {time.time() - t0:.0f} s; total {len(done) + n} of {len(TASKS)}", flush=True)
