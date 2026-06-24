"""B199 -- the geometric-stratum metallic-exponent grid engine (Goal A, P1).

Computes the exponent k in [A,B] = s*mu^k (mu = A^-m t) ON THE GEOMETRIC / CUSPED STRATUM only --
the reps where mu has INFINITE order (loxodromic). Finite-order-mu reps are Dehn-filling/orbifold
points where k is ambiguous mod order(mu) (B198/V191); they are bucketed separately and EXCLUDED
from the geometric exponent. Reuses the B198 numeric engine; adds the order(mu) split + the clean
per-rep gates (irreducible Burnside=n^2, non-degenerate mu!=t, on-variety, clean best-fit margin).

Standalone character-variety / low-dim-topology math. No physics; nothing to CLAIMS.md. pyenv.
"""
import os, sys, json
import numpy as np
from collections import Counter

_B198 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B198_metallic_exponent_CAS")
sys.path.insert(0, _B198)
from gauge_newton import make_A, newton_t, newton_bt, irred, exponent  # noqa: E402


def mu_order(mu, tol=1e-6, maxd=60):
    """Return (finite_order:int|None, loxodromic_offset:float). finite_order=None => infinite order."""
    ev = np.linalg.eigvals(mu)
    off = float(np.max(np.abs(np.abs(ev) - 1.0)))           # >0 => loxodromic (off unit circle)
    order = next((d for d in range(1, maxd + 1) if np.max(np.abs(ev ** d - 1)) < tol), None)
    return order, off


def _kmargin(A, B, t, m, k, kmax=16):
    """err at the winning k, and the smallest err at any OTHER j (the best-fit margin)."""
    Ai = np.linalg.inv(A)
    comm = A @ B @ Ai @ np.linalg.inv(B)
    mu = np.linalg.matrix_power(Ai, m) @ t
    errk = 9e9; second = 9e9
    for j in range(0, kmax + 1):
        muj = np.linalg.matrix_power(mu, j)
        e = min(np.max(np.abs(comm - muj)), np.max(np.abs(comm + muj)))
        if j == k:
            errk = e
        else:
            second = min(second, e)
    return errk, second


def geom_exponent_cell(m, o, n, exps, seeds=400, rng_seeds=(0, 1, 7),
                       relresid=1e-10, errtol=1e-6, want_geo=8):
    """Structured geometric-stratum result for one cell. Returns the P1 schema dict."""
    A = make_A(o, exps)[0]
    Ai = np.linalg.inv(A)
    gfix = list(range(n - 1))
    geo = Counter()        # (s,k) on order(mu)=inf reps
    fin = Counter()        # (s,k) on finite-order-mu reps
    fin_orders = set()
    n_irred = 0
    lox_sample = None
    max_relresid = 0.0
    for rs in rng_seeds:
        rng = np.random.default_rng(rs)
        for _ in range(seeds):
            if m == 1:
                Aa, Aii, Ai2 = make_A(o, exps)
                t, r = newton_t(Aa, Aii, Ai2, n, gfix, rng)
                B = None if t is None else Ai2 @ t @ Aa @ np.linalg.inv(t)
            else:
                x, r = newton_bt(A, m, n, gfix, rng)
                B, t = (None, None) if x is None else (x[:n * n].reshape(n, n), x[n * n:].reshape(n, n))
            if t is None or r > relresid or abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e6:
                continue
            mu = np.linalg.matrix_power(Ai, m) @ t
            if np.max(np.abs(mu - t)) < 1e-6:          # A^m=I degenerate (mu=t): not a metallic cusp
                continue
            if irred(A, B, n) != n * n:                # geometric reps are irreducible
                continue
            n_irred += 1
            max_relresid = max(max_relresid, float(r))
            s_, k_, err = exponent(A, B, t, m)
            if err > errtol:
                continue                                # no clean [A,B]=+-mu^k for this rep
            errk, second = _kmargin(A, B, t, m, k_)
            order, off = mu_order(mu)
            if order is None:                           # INFINITE order -> geometric stratum
                if second > 0.01:                       # clean best-fit (not noise)
                    geo[(s_, k_)] += 1
                    if lox_sample is None:
                        lox_sample = {"mu_abs": [round(float(a), 4) for a in np.abs(np.linalg.eigvals(mu))],
                                      "offset": round(off, 4), "errk": float(errk), "second": float(second)}
            else:
                fin[(s_, k_)] += 1
                fin_orders.add(int(order))
        if sum(geo.values()) >= want_geo:
            break
    geo_dom = max(geo.items(), key=lambda kv: kv[1])[0] if geo else None
    geo_unique = (len(geo) == 1)
    return {
        "id": "m%d_o%d_n%d" % (m, o, n), "m": m, "o": o, "n": n, "exps": list(exps),
        "n_irred_reps": n_irred,
        "geometric": {"exponents": {str(k): v for k, v in geo.items()},
                      "dominant_s_k": list(geo_dom) if geo_dom else None,
                      "unique": geo_unique, "reps": int(sum(geo.values()))},
        "finite_order": {"exponents": {str(k): v for k, v in fin.items()},
                         "orders_seen": sorted(fin_orders), "reps": int(sum(fin.values()))},
        "geometric_k": (geo_dom[1] if geo_dom else None),
        "geometric_s": (geo_dom[0] if geo_dom else None),
        "loxodromic_sample": lox_sample,
        "empty": (n_irred == 0),
        "max_relresid": max_relresid,
        "seeds_used": list(rng_seeds),
        "tier": "num",
    }


if __name__ == "__main__":
    # smoke-test: validation cells must reproduce known geometric k (o=4 m=1 -> 3, o=3 m=1 -> 4)
    smoke = [(1, 4, 3, [0, 1, 3], 3), (1, 3, 4, [0, 0, 1, 2], 4)]
    ok = True
    for (m, o, n, exps, expect) in smoke:
        res = geom_exponent_cell(m, o, n, exps, seeds=150, rng_seeds=(0, 1))
        got = res["geometric_k"]
        flag = "OK" if got == expect else "MISMATCH"
        if got != expect:
            ok = False
        print("m=%d o=%d n=%d : geometric_k=%s (expect %d) reps=%d unique=%s lox=%s  [%s]" % (
            m, o, n, got, expect, res["geometric"]["reps"], res["geometric"]["unique"],
            bool(res["loxodromic_sample"]), flag))
    print("ALL CHECKS PASS" if ok else "SMOKE-TEST FAILED")
