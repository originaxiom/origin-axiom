#!/usr/bin/env python3
"""B1523 post-run check X1, second pass (written after the seal, after the census and after route F's first pass; disclosed): route F's
reach widened. Route F's first pass found the fibre representation by Newton at 60 digits from 600 random starts and missed the
hyperbolic fixed point on some longer words (route_f_batch.json, "not reached"). This file changes only how that fixed point is
found; everything that reads (the modules, the cocycles, the ranks, the fibre boundary) is route_f.py's, unchanged.

  - Newton on the same equations (T_phi(x, y, z) = (x, y, z) on x^2 + y^2 + z^2 = x y z), vectorised in double precision over many
    random starts at once, with the Jacobian carried through the trace map letter by letter (forward derivatives).
  - The distinct non-real roots are polished at 60 digits by mpmath from the double-precision root; a root is kept only if the
    equations hold to 1e-40 and its third coordinate is fixed to 1e-35 (route F's own tests).
  - Newton's basins depend on the word's basis, so when the word itself reaches no matching root its cyclic rotations are tried
    in turn (the same oriented manifold; the rotation read is recorded).
  - The hyperbolic one is the root whose cusp shape matches SnapPy's (route F's test, unchanged), counted up to complex conjugation
    (the mirror image's structure, with the same real modules). Several roots can still match: the representation twisted by a sign
    character of the fibre that the monodromy fixes is again a fixed point, with the same image in PSL(2, C). Each matching root
    is read, and a manifold whose readings disagree is reported, not read.
Usage: python3 route_f_reach.py SIGN WORD [SIGN WORD ...]       (one manifold at a time, for checks)
       python3 route_f_reach.py --batch                         (the first pass's misses; writes route_f_reach.json)"""
import json
import pathlib
import sys
import time
import warnings

import numpy as np
import mpmath as mp

warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_f as F  # noqa: E402


def newton_np(steps, n, rng, iters=80):
    """double-precision Newton from n random starts at once; returns the converged roots (N, 3)"""
    mag = 10.0 ** rng.uniform(-0.5, 2.5, size=(n, 3))
    P = mag * np.exp(2j * np.pi * rng.uniform(0, 1, size=(n, 3)))
    alive = np.ones(n, dtype=bool)
    for _ in range(iters):
        x, y, z = P[:, 0], P[:, 1], P[:, 2]
        dx = np.zeros((len(P), 3), complex); dx[:, 0] = 1
        dy = np.zeros((len(P), 3), complex); dy[:, 1] = 1
        dz = np.zeros((len(P), 3), complex); dz[:, 2] = 1
        X, Y, Z, dX, dY, dZ = x, y, z, dx, dy, dz
        for st in steps:
            if st == "L":
                X, Y, Z, dX, dY, dZ = Z, Y, Y * Z - X, dZ, dY, Z[:, None] * dY + Y[:, None] * dZ - dX
            elif st == "R":
                X, Y, Z, dX, dY, dZ = X, Z, X * Z - Y, dX, dZ, Z[:, None] * dX + X[:, None] * dZ - dY
        Fv = np.stack([X - x, Y - y, x * x + y * y + z * z - x * y * z], axis=1)
        J = np.stack([dX - dx, dY - dy, np.stack([2 * x - y * z, 2 * y - x * z, 2 * z - x * y], axis=1)], axis=1)
        with np.errstate(all="ignore"):
            # one singular Jacobian must not stop the batch: those starts are dropped, the others go on
            det = np.linalg.det(J)
            sing = ~np.isfinite(det) | (np.abs(det) < 1e-250) | ~np.isfinite(Fv).all(axis=1)
            J[sing] = np.eye(3)
            Fv[sing] = 0
            step = np.linalg.solve(J, Fv[:, :, None])[:, :, 0]
            step[sing] = np.nan
            # damp very long steps
            scale = np.maximum(1.0, np.abs(step).max(axis=1) / (1.0 + np.abs(P).max(axis=1)))
            P = P - step / scale[:, None]
        bad = ~np.isfinite(P).all(axis=1) | (np.abs(P).max(axis=1) > 1e8)
        P[bad] = 1.0
        alive &= ~bad
    x, y, z = P[:, 0], P[:, 1], P[:, 2]
    X, Y, Z = F.trace_map(steps, x, y, z)
    res = np.abs(np.stack([X - x, Y - y, Z - z, x * x + y * y + z * z - x * y * z], axis=1)).max(axis=1)
    size = 1.0 + np.abs(P).max(axis=1) ** 2
    ok = alive & (res < 1e-6 * size) & (np.abs(P.imag).sum(axis=1) > 1e-6)
    return P[ok]


def distinct(P, tol=1e-6):
    """one representative per root: bucket by a coarse rounding, then compare within the bucket and its neighbours on x's real
    part (a root split across buckets is only polished twice; the 60-digit list below removes the copy)"""
    out, buckets = [], {}
    for p in P:
        s = 1 + np.abs(p).max()
        key = int(np.floor(p[0].real / (1e3 * tol * s)))
        if any(np.abs(p - q).max() < tol * (1 + np.abs(q).max()) for k in (key - 1, key, key + 1) for q in buckets.get(k, [])):
            continue
        buckets.setdefault(key, []).append(p)
        out.append(p)
    return out


def polish(steps, p):
    def G(x, y, z):
        X, Y, Z = F.trace_map(steps, x, y, z)
        return [X - x, Y - y, x * x + y * y + z * z - x * y * z]
    try:
        r = mp.findroot(G, [mp.mpc(complex(v)) for v in p], tol=mp.mpf(10) ** -50, maxsteps=60)
    except (ZeroDivisionError, ValueError):
        return None
    x, y, z = r[0], r[1], r[2]
    if max(abs(v) for v in G(x, y, z)) > mp.mpf(10) ** -40:
        return None
    if abs(F.trace_map(steps, x, y, z)[2] - z) > mp.mpf(10) ** -35:
        return None
    if abs(mp.im(x)) + abs(mp.im(y)) + abs(mp.im(z)) < mp.mpf(10) ** -20:
        return None
    return x, y, z


def same_up_to_conjugation(r, u):
    """the complex conjugate of a fixed point is the mirror image's structure: the same real modules, the same reading"""
    d = abs(r[0] - u[0]) + abs(r[1] - u[1]) + abs(r[2] - u[2])
    dc = abs(r[0] - mp.conj(u[0])) + abs(r[1] - mp.conj(u[1])) + abs(r[2] - mp.conj(u[2]))
    return min(d, dc) < mp.mpf(10) ** -25


def reach(sign, word, snappy_shape, rounds=8, per_round=25000, seed=11):
    """every root matching SnapPy's cusp shape, up to complex conjugation, among the distinct roots of up to `rounds` batches;
    the search stops after the first round that finds one, having finished that round"""
    steps = F.letters(sign, word)
    rng = np.random.default_rng(seed)

    def matches(sh):
        if abs(abs(sh.imag) - abs(snappy_shape.imag)) > 1e-9:
            return False
        return any(abs((sh.real + e * snappy_shape.real) - round(sh.real + e * snappy_shape.real)) < 1e-9 for e in (1, -1))

    seen, found = [], []
    for k in range(rounds):
        new = [p for p in distinct(newton_np(steps, per_round, rng))
               if not any(np.abs(p - q).max() < 1e-6 * (1 + np.abs(q).max()) for q in seen)]
        seen.extend(new)
        for p in new:
            r = polish(steps, p)
            if r is None:
                continue
            A, B = F.rep_from_traces(*r)
            T, _ = F.monodromy_fast(steps, A, B)
            sh, _ = F.cusp_shape(sign, A, B, T)
            if sh is not None and matches(complex(sh)) and not any(same_up_to_conjugation(r, u) for u in found):
                found.append(r)
        if found:
            return found, len(seen), k + 1
    return found, len(seen), rounds


def read(sign, word, root):
    steps = F.letters(sign, word)
    A, B = F.rep_from_traces(*root)
    T, tres = F.monodromy_fast(steps, A, B)
    sh, comm = F.cusp_shape(sign, A, B, T)
    out = {"shape": [complex(sh).real, complex(sh).imag], "T residual": float(tres), "commutation": float(comm)}
    for kind in ("triv", "so"):
        info, _ = F.cohomology_fast(steps, A, B, T, kind)
        out["H1 " + kind] = info
    res, info = F.fibre_boundary_fast(steps, A, B, T)
    out["H1 v"] = info
    out["fibre boundary residual"] = res
    return out


def record(sign, word, snappy_shape, rounds=2, per_round=20000):
    """the word and then its cyclic rotations (the same oriented manifold: a rotation conjugates the monodromy, and the cusp shape
    is unchanged mod 1), until one reaches a root matching SnapPy's cusp shape; every matching root of that rotation is read (sign
    twists of one representation, by characters the monodromy fixes, so the readings must agree; a disagreement is reported and
    the manifold is not read)"""
    t0 = time.time()
    nseen = 0
    for k in range(len(word)):
        w = word[k:] + word[:k]
        found, n, r = reach(sign, w, snappy_shape, rounds=rounds, per_round=per_round, seed=11 + k)
        nseen += n
        if found:
            break
    out = {"state": sign + word, "distinct non-real roots seen (double precision, all rotations tried)": nseen,
           "rotation read": (sign + w) if found else None, "matching roots (up to conjugation)": len(found)}
    reads = [read(sign, w, r) for r in found]
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


def batch():
    import multiprocessing as mpc
    import snappy  # noqa: F401
    first = json.loads((HERE / "route_f_batch.json").read_text())
    todo = first["not reached"]
    print(f"route F second pass: {len(todo)} manifolds the first pass did not reach", flush=True)
    recs = {}
    with mpc.Pool(4) as pool:
        for d in pool.imap_unordered(one, todo):
            recs[d["state"]] = d
            print(d["state"], d.get("hyperbolic found"), d.get("matching roots (up to conjugation)"),
                  [d.get("H1 " + k, {}).get("dim") for k in ("triv", "so", "v")], d.get("fibre boundary residual"),
                  d.get("seconds"), flush=True)
    rows = {r["manifold"]: r for r in json.loads((HERE / "read_out.json").read_text())["rows"]}
    reached = [d for d in recs.values() if d.get("hyperbolic found")]
    agree = [d for d in reached if [d["H1 " + k]["dim"] for k in ("triv", "so", "v")] == rows[d["state"]]["dims R"]
             and (d["fibre boundary residual"] is not None and d["fibre boundary residual"] > 1e-20) == rows[d["state"]]["fibre boundary rigid"]]
    summary = {"first pass not reached": len(todo), "reached now": len(reached),
               "still not reached": sorted(s for s in todo if not recs.get(s, {}).get("hyperbolic found")),
               "more than one matching root (up to conjugation)": sorted(d["state"] for d in recs.values()
                                                                         if d.get("matching roots (up to conjugation)", 0) > 1),
               "matching roots whose readings disagree": sorted(d["state"] for d in recs.values() if d.get("readings agree") is False),
               "agree with the census (dimensions and the fibre boundary)": len(agree),
               "disagree": sorted(d["state"] for d in reached if d not in agree),
               "smallest fibre-boundary residual among those reached": min((d["fibre boundary residual"] for d in reached
                                                                            if d["fibre boundary residual"] is not None), default=None),
               "records": sorted(recs.values(), key=lambda d: d["state"])}
    (HERE / "route_f_reach.json").write_text(json.dumps(summary, indent=1, default=str))
    print(json.dumps({k: v for k, v in summary.items() if k != "records"}, default=str))


if __name__ == "__main__":
    if sys.argv[1:] == ["--batch"]:
        batch()
    else:
        import snappy
        args = sys.argv[1:]
        for i in range(0, len(args), 2):
            sign, word = args[i], args[i + 1]
            sh = complex(snappy.Manifold(("b++" if sign == "+" else "b+-") + word).cusp_info("shape")[0])
            print(json.dumps(record(sign, word, sh), default=str), flush=True)
