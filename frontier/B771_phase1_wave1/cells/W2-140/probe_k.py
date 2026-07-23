"""W2-140 auxiliary: k-CONSTRAINED Newton -- direct existence probe for the rigid sublocus
[A,B] = s*mu^k on a given (m,o,n,exps) cell.

Random sweeps only find the rigid sublocus by chance (it can be codim>=1 in the component:
B199 Result B).  Here we ADD the constraint to the system and let Newton converge onto the
sublocus directly, for each candidate (s,k).  A verified hit = full bundle relations 1e-10 +
constraint 1e-10 + irreducible + loxodromic (order(mu)=inf) + non-central longitude
=> the k-sublocus EXISTS (a point on it is exhibited).  Repeated misses across many seeds are
evidence of absence (bounded, honest: absence-of-hits, not proof).

Usage: python3 probe_k.py m o n e0,e1,... kmin kmax seeds  > out
pyenv python3.  Standalone math; no physics.
"""
import sys, json
import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from compute import make_A, irred, mu_order  # noqa: E402


def resid(x, A, Ai, Am, Aim, m, n, gfix, s, k):
    B = x[:n * n].reshape(n, n)
    t = x[n * n:].reshape(n, n)
    F1 = t @ np.linalg.matrix_power(B, m) - Ai @ t @ A
    F2 = t @ B - Am @ B @ t
    comm = A @ B @ Ai @ np.linalg.inv(B)
    mu = Aim @ t
    G = comm - s * np.linalg.matrix_power(mu, k)
    extra = [np.linalg.det(B) - 1, np.linalg.det(t) - 1] + [t[i, i + 1] - 1 for i in gfix]
    return np.concatenate([F1.reshape(-1), F2.reshape(-1), G.reshape(-1),
                           np.array(extra, complex)])


def probe(m, o, n, exps, s, k, nseeds, rng_seed=0, iters=250):
    A = make_A(o, exps)[0]
    Ai = np.linalg.inv(A)
    Am = np.linalg.matrix_power(A, m)
    Aim = np.linalg.matrix_power(Ai, m)
    gfix = list(range(n - 1))
    rng = np.random.default_rng(rng_seed)
    hits = 0
    sample = None
    for _ in range(nseeds):
        x = rng.standard_normal(2 * n * n) + 1j * rng.standard_normal(2 * n * n)
        ok = False
        for _ in range(iters):
            g = resid(x, A, Ai, Am, Aim, m, n, gfix, s, k)
            mx = np.max(np.abs(g))
            if mx < 1e-12:
                ok = True
                break
            if mx > 1e9 or not np.isfinite(mx):
                break
            h = 1e-7
            J = np.zeros((g.size, 2 * n * n), complex)
            for j in range(2 * n * n):
                xp = x.copy()
                xp[j] += h
                J[:, j] = (resid(xp, A, Ai, Am, Aim, m, n, gfix, s, k) - g) / h
            try:
                st, *_ = np.linalg.lstsq(J, g, rcond=None)
            except np.linalg.LinAlgError:
                break
            x = x - st
        if not ok:
            continue
        B = x[:n * n].reshape(n, n)
        t = x[n * n:].reshape(n, n)
        if abs(np.linalg.det(t)) < 1e-3 or np.linalg.cond(t) > 1e6:
            continue
        mu = Aim @ t
        if np.max(np.abs(mu - t)) < 1e-6:
            continue
        order, off = mu_order(mu)
        if order is not None:                       # need loxodromic (geometric stratum)
            continue
        if irred(A, B, n) != n * n:
            continue
        comm = A @ B @ Ai @ np.linalg.inv(B)
        offc = np.max(np.abs(comm - np.trace(comm) / n * np.eye(n)))
        if offc < 1e-4:
            continue
        hits += 1
        if sample is None:
            sample = {"mu_abs": [round(float(a), 4) for a in np.abs(np.linalg.eigvals(mu))],
                      "cond_t": float(np.linalg.cond(t)),
                      "resid": float(np.max(np.abs(resid(x, A, Ai, Am, Aim, m, n, gfix, s, k))))}
    return hits, sample


if __name__ == "__main__":
    m, o, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    exps = [int(a) for a in sys.argv[4].split(",")]
    kmin, kmax, nseeds = int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
    out = {}
    for k in range(kmin, kmax + 1):
        for s in (1, -1):
            hits, sample = probe(m, o, n, exps, s, k, nseeds)
            out["s=%+d k=%d" % (s, k)] = {"hits": hits, "of": nseeds, "sample": sample}
            print("m=%d o=%d n=%d exps=%s  s=%+d k=%d : hits=%d/%d %s" %
                  (m, o, n, exps, s, k, hits, nseeds,
                   "" if sample is None else json.dumps(sample)), flush=True)
    with open(__file__.rsplit("/", 1)[0] +
              "/results/probe_m%d_o%d_n%d_%s.json" % (m, o, n, "".join(map(str, exps))), "w") as f:
        json.dump(out, f, indent=1)
