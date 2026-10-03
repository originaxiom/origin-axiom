#!/usr/bin/env python3
"""B1523 post-run check X1, third pass (written after the census and after route F's first two passes; disclosed): route F with
its fixed point LOCATED from SnapPy's holonomy, and READ by route F's own code, unchanged.

Why: Newton from random starts (passes one and two, no SnapPy holonomy) misses the hyperbolic fixed point on many long words.
How the fixed point is located here:
  - SnapPy's fundamental group of the bundle (ManifoldHP) and its SL(2, C) holonomy; the map to Z from the relators' exponent
    sums (b_1 = 1); every reduced word of length <= 7 in SnapPy's generators that maps to 0 is a fibre element.
  - Among pairs (u, v) of fibre elements, a triple (tr u, tr v, tr uv) on the Markoff surface x^2 + y^2 + z^2 = x y z that
    route F's own trace map fixes, up to an even sign change (SnapPy's SL(2) lift is fixed only up to a sign character of the
    fibre).
  - That triple only seeds route F's 60-digit Newton (route_f_reach.polish): the fixed point is then a fixed point of route F's
    trace map to 1e-40, its cusp shape must match SnapPy's (up to mod 1, sign and conjugation), and every matching root, up to
    complex conjugation, is read; their readings must agree.
  - When the word's own seeds reach no matching root, its cyclic rotations are tried in turn (the same oriented manifold; the
    rotation read is recorded), as in the second pass. This fallback was added after the pass's first attempt on all 536, which
    found no seed for +-LLLRLRLRRLRR and read every other manifold; its log is route_f_seeded_run.txt. Only those two were run
    again (--retry, log route_f_seeded_retry_run.txt); the records of the other 534 are the first attempt's.
What it shares with routes R and C: SnapPy's holonomy, used only to locate the representation, which is unique (Mostow). The
reading (the modules, the cocycles on F_2 x| Z, the ranks, the fibre boundary) is route F's own, as in passes one and two.
Usage: python3 route_f_seeded.py SIGN WORD [...]      (single manifolds)
       python3 route_f_seeded.py --all                (all 536 manifolds; writes route_f_seeded.jsonl and route_f_seeded.json)
       python3 route_f_seeded.py --retry              (re-runs the manifolds not reached, then rewrites route_f_seeded.json)"""
import json
import pathlib
import sys
import time
import warnings

import numpy as np

warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_f as F  # noqa: E402
import route_f_reach as R  # noqa: E402
import mpmath as mp  # noqa: E402


def fibre_words(name, Lmax=7):
    """SnapPy's generators' holonomy (double precision, for the search only) and every reduced word of length <= Lmax in the
    kernel of the map to Z"""
    import snappy
    import sympy
    G = snappy.ManifoldHP(name).fundamental_group()
    gens, rels = G.generators(), G.relators()
    E = [[sum((1 if ch == g else -1 if ch == g.upper() else 0) for ch in r) for g in gens] for r in rels]
    ns = sympy.Matrix(E).nullspace()
    assert len(ns) == 1, (name, "b_1 is not 1")
    h = ns[0]
    den = sympy.ilcm(*[x.q for x in h])
    h = [int(x * den) for x in h]
    g0 = int(np.gcd.reduce(np.abs(h)))
    h = [x // g0 for x in h]
    mats = {}
    for g in gens:
        S = G.SL2C(g)
        A = np.array([[complex(S[i, j]) for j in range(2)] for i in range(2)])
        mats[g], mats[g.upper()] = A, np.linalg.inv(A)
    letters = list(gens) + [g.upper() for g in gens]
    inv = {c: (c.upper() if c.islower() else c.lower()) for c in letters}
    deg = {c: h[gens.index(c.lower())] * (1 if c.islower() else -1) for c in letters}
    fib, frontier = [], [("", np.eye(2, dtype=complex), 0)]
    for _ in range(Lmax):
        nxt = []
        for w, Mw, d in frontier:
            for c in letters:
                if w and w[-1] == inv[c]:
                    continue
                W, MW, D = w + c, Mw @ mats[c], d + deg[c]
                nxt.append((W, MW, D))
                if D == 0:
                    fib.append(MW)
        frontier = nxt
    return np.array(fib)


def seeds(sign, word, Lmax=7, cap=40):
    """distinct triples fixed by route F's trace map, from pairs of fibre elements (double precision)"""
    name = ("b++" if sign == "+" else "b+-") + word
    Ms = fibre_words(name, Lmax)
    tr = np.trace(Ms, axis1=1, axis2=2)
    steps = F.letters(sign, word)
    out = []
    for i in range(len(Ms)):
        z = np.trace(Ms[i] @ Ms, axis1=1, axis2=2)
        x = np.full(len(Ms), tr[i])
        y = tr
        size = 1 + np.abs(x) ** 2 + np.abs(y) ** 2 + np.abs(z) ** 2
        ok = np.abs(x * x + y * y + z * z - x * y * z) < 1e-7 * size
        if not ok.any():
            continue
        idx = np.nonzero(ok)[0]
        for sx, sy in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
            xs, ys, zs = sx * x[idx], sy * y[idx], sx * sy * z[idx]
            X, Y, Z = F.trace_map(steps, xs, ys, zs)
            res = np.abs(X - xs) + np.abs(Y - ys) + np.abs(Z - zs)
            for k in np.nonzero(res < 1e-6 * (1 + np.abs(xs) + np.abs(ys) + np.abs(zs)))[0]:
                p = np.array([xs[k], ys[k], zs[k]])
                if not any(np.abs(p - q).max() < 1e-6 * (1 + np.abs(q).max()) for q in out):
                    out.append(p)
        if len(out) >= cap or (out and i > 50):
            break
    return out


def record(sign, word, snappy_shape):
    """the word, and then its cyclic rotations while no seed reaches a root matching SnapPy's cusp shape (the cusp shape is
    unchanged mod 1 under a rotation, as in the second pass)"""
    t0 = time.time()

    def matches(sh):
        if abs(abs(sh.imag) - abs(snappy_shape.imag)) > 1e-9:
            return False
        return any(abs((sh.real + e * snappy_shape.real) - round(sh.real + e * snappy_shape.real)) < 1e-9 for e in (1, -1))

    tried = []
    for k in range(len(word)):
        w = word[k:] + word[:k]
        steps = F.letters(sign, w)
        cands = seeds(sign, w)
        found = []
        for p in cands:
            r = R.polish(steps, p)
            if r is None:
                continue
            A, B = F.rep_from_traces(*r)
            T, _ = F.monodromy_fast(steps, A, B)
            sh, _ = F.cusp_shape(sign, A, B, T)
            if sh is not None and matches(complex(sh)) and not any(R.same_up_to_conjugation(r, u) for u in found):
                found.append(r)
        tried.append({"rotation": sign + w, "seeds": len(cands), "matching roots": len(found)})
        if found:
            break
    out = {"state": sign + word, "seeds": len(cands), "matching roots (up to conjugation)": len(found)}
    if len(tried) > 1:
        out["rotations tried"] = tried
        out["rotation read"] = (sign + w) if found else None
    reads = [R.read(sign, w, r) for r in found]
    keys = [([d["H1 " + k]["dim"] for k in ("triv", "so", "v")], d["fibre boundary residual"] is not None
             and d["fibre boundary residual"] > 1e-20) for d in reads]
    out["readings agree"] = len(set(map(str, keys))) <= 1
    out["hyperbolic found"] = bool(found) and out["readings agree"]
    if out["hyperbolic found"]:
        out.update(reads[0])
        if len(reads) > 1:
            out["other matching roots, fibre-boundary residuals"] = [d["fibre boundary residual"] for d in reads[1:]]
    out["seconds"] = round(time.time() - t0, 1)
    return out


def one(state):
    import snappy
    sign, word = state[0], state[1:]
    try:
        sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
        return record(sign, word, sh)
    except Exception as e:  # reported, never swallowed
        return {"state": state, "error": f"{type(e).__name__}: {e}"}


def run_all():
    import multiprocessing as mpc
    import snappy  # noqa: F401
    rows = {r["manifold"]: r for r in json.loads((HERE / "read_out.json").read_text())["rows"]}
    states = sorted(rows, key=lambda s: (rows[s]["length"], s))
    out_path = HERE / "route_f_seeded.jsonl"
    done = {}
    if out_path.exists():
        for line in out_path.read_text().splitlines():
            d = json.loads(line)
            done[d["state"]] = d
    todo = [s for s in states if s not in done]
    print(f"route F seeded pass: {len(states)} manifolds, {len(done)} done, {len(todo)} to run", flush=True)
    with mpc.Pool(4) as pool, out_path.open("a") as f:
        for d in pool.imap_unordered(one, todo):
            f.write(json.dumps(d, default=str) + "\n")
            f.flush()
            done[d["state"]] = d
            print(d["state"], d.get("hyperbolic found"), d.get("matching roots (up to conjugation)"),
                  [d.get("H1 " + k, {}).get("dim") for k in ("triv", "so", "v")], d.get("fibre boundary residual"),
                  d.get("seconds"), d.get("error", ""), flush=True)
    summarise(done, states, rows)


def summarise(done, states, rows):
    reached = [d for d in done.values() if d.get("hyperbolic found")]
    agree = [d for d in reached if [d["H1 " + k]["dim"] for k in ("triv", "so", "v")] == rows[d["state"]]["dims R"]
             and (d["fibre boundary residual"] is not None and d["fibre boundary residual"] > 1e-20) == rows[d["state"]]["fibre boundary rigid"]]
    # the passes without SnapPy's holonomy, where they reached the same manifold: the same reading
    other = {}
    for fn in ("route_f_batch.json", "route_f_reach.json"):
        p = HERE / fn
        if p.exists():
            for d in json.loads(p.read_text())["records"]:
                if d.get("hyperbolic found"):
                    other.setdefault(d["state"], []).append(d)
    cross = [s for s in other if s in done and done[s].get("hyperbolic found")]
    cross_disagree = sorted(s for s in cross if any(
        [o["H1 " + k]["dim"] for k in ("triv", "so", "v")] != [done[s]["H1 " + k]["dim"] for k in ("triv", "so", "v")]
        or (o["fibre boundary residual"] > 1e-20) != (done[s]["fibre boundary residual"] > 1e-20) for o in other[s]))
    summary = {"manifolds": len(states), "reached": len(reached),
               "not reached": sorted(s for s in states if not done.get(s, {}).get("hyperbolic found")),
               "errors": sorted(d["state"] for d in done.values() if "error" in d),
               "matching roots whose readings disagree": sorted(d["state"] for d in done.values() if d.get("readings agree") is False),
               "agree with the census (dimensions and the fibre boundary)": len(agree),
               "disagree": sorted(d["state"] for d in reached if d not in agree),
               "reached also by a pass without SnapPy's holonomy": len(cross),
               "readings differing from those passes": cross_disagree,
               "smallest fibre-boundary residual among those reached": min((d["fibre boundary residual"] for d in reached
                                                                            if d["fibre boundary residual"] is not None), default=None),
               "largest T residual": max((d["T residual"] for d in reached), default=None),
               "read through a rotation of the word": sorted(d["state"] for d in reached if d.get("rotation read")),
               "records": sorted(done.values(), key=lambda d: d["state"])}
    (HERE / "route_f_seeded.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "records"}, default=str))


def retry():
    """re-run only the manifolds the pass has not reached (the records of the others are kept), then rewrite the summary"""
    import multiprocessing as mpc
    import snappy  # noqa: F401
    rows = {r["manifold"]: r for r in json.loads((HERE / "read_out.json").read_text())["rows"]}
    states = sorted(rows, key=lambda s: (rows[s]["length"], s))
    out_path = HERE / "route_f_seeded.jsonl"
    done = {}
    for line in out_path.read_text().splitlines():
        d = json.loads(line)
        done[d["state"]] = d
    todo = [s for s in states if not done.get(s, {}).get("hyperbolic found")]
    print(f"route F seeded pass, retry: {len(todo)} manifolds not reached: {todo}", flush=True)
    with mpc.Pool(4) as pool:
        for d in pool.imap_unordered(one, todo):
            done[d["state"]] = d
            print(json.dumps(d, default=str), flush=True)
    out_path.write_text("".join(json.dumps(done[s], default=str) + "\n" for s in states if s in done))
    summarise(done, states, rows)


if __name__ == "__main__":
    if sys.argv[1:] == ["--all"]:
        run_all()
    elif sys.argv[1:] == ["--retry"]:
        retry()
    else:
        import snappy
        for st in sys.argv[1:]:
            sign, word = st[0], st[1:]
            sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
            print(json.dumps(record(sign, word, sh), default=str), flush=True)
