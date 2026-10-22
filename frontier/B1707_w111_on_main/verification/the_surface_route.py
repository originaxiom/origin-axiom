"""B1707 (P-211; Review 67's R67-6): the SM seat's W111 (the surface route) checked on main's own code.  No data.  F_{2g} on a_1, b_1, ...;
words are lists of (generator index, +-1).  The moves (W111's): the twists tau_k: b_k -> b_k a_k, tau'_k: a_k -> a_k b_k;
the adjacent swap sigma_k; the mixing move mu' = conj(gamma^-1) o mu with mu: a_1 -> gamma a_1, b_2 -> gamma b_2,
gamma = b_1^-1 a_2.  Checked: each move keeps the boundary word's class (exactly, by free reduction, up to the stated
conjugation); (a) a numerical search for SL(2, C) characters of F_4 (g = 2) fixed by the twists and the swap -- the
residual of the trace conditions on the words of length <= 3 minimised from random starts; the minima's traces; the
control at g = 1 finds the quaternion point; (b) the Heisenberg group's Schrodinger representation for p = 3, 5 at
g = 1, 2: the character fixed by every move on 400 random words; (c) the extraspecial 2-group (Pauli) representations,
every choice of the generators' squares, at g = 1 and 2: which are fixed by every move."""
import itertools, json, math, pathlib, random
import numpy as np
from scipy.optimize import least_squares
HERE = pathlib.Path(__file__).resolve().parent
def gens(g): return [("a", k) for k in range(g)] + [("b", k) for k in range(g)]
def inv(w): return [(x, -e) for x, e in reversed(w)]
def red(w):
    out = []
    for t in w:
        if out and out[-1][0] == t[0] and out[-1][1] == -t[1]: out.pop()
        else: out.append(t)
    return out
def comm(u, v): return red(u + v + inv(u) + inv(v))
def L(x, k): return [((x, k), 1)]
def boundary(g):
    w = []
    for k in range(g): w += comm(L("a", k), L("b", k))
    return red(w)
def apply(phi, w):
    out = []
    for (gen, e) in w:
        img = phi.get(gen, [(gen, 1)])
        out += img if e == 1 else inv(img)
    return red(out)
def tau(k): return {("b", k): [(("b", k), 1), (("a", k), 1)]}
def taup(k): return {("a", k): [(("a", k), 1), (("b", k), 1)]}
def sigma(k):
    c = comm(L("a", k), L("b", k))
    return {("a", k): red(c + L("a", k + 1) + inv(c)), ("b", k): red(c + L("b", k + 1) + inv(c)), ("a", k + 1): L("a", k), ("b", k + 1): L("b", k)}
def mu_prime():
    gam = red(inv(L("b", 0)) + L("a", 1)); gi = inv(gam)
    mu = {("a", 0): red(gam + L("a", 0)), ("b", 1): red(gam + L("b", 1))}
    # mu' = conj by gamma^-1 after mu, on handles 1 and 2: x -> gamma^-1 mu(x) gamma
    out = {}
    for x in [("a", 0), ("b", 0), ("a", 1), ("b", 1)]:
        out[x] = red(gi + mu.get(x, [(x, 1)]) + gam)
    return out
def cyc_reduce(w):
    w = red(w)
    while len(w) > 1 and w[0][0] == w[-1][0] and w[0][1] == -w[-1][1]: w = w[1:-1]
    return w
def same_class(u, v):
    u, v = cyc_reduce(u), cyc_reduce(v)
    if len(u) != len(v): return False
    return any(u[i:] + u[:i] == v for i in range(max(1, len(u))))
def moves(g):
    M = {}
    for k in range(g): M["tau%d" % k] = tau(k); M["tau'%d" % k] = taup(k)
    for k in range(g - 1): M["sigma%d" % k] = sigma(k)
    if g >= 2: M["mu'"] = mu_prime()
    return M
out = {"boundary_kept": {}}
for g in (1, 2, 3):
    d = boundary(g)
    out["boundary_kept"][g] = {n: same_class(apply(phi, d), d) for n, phi in moves(g).items()}
def ev(w, img):
    M = None                                   # no np.eye per call: under this NumPy each one was retained (a leak)
    for (gen, e) in w:
        X = img[gen] if e == 1 else np.linalg.inv(img[gen])
        M = X if M is None else M @ X
    return M if M is not None else np.eye(img[next(iter(img))].shape[0], dtype=complex)
# (a) SL(2, C) characters fixed by the twists and the swap, g = 2 (and the control g = 1)
def trace_words(g):
    G = gens(g); W = [L(*x) for x in G]
    for i, j in itertools.combinations(range(len(G)), 2): W.append(L(*G[i]) + L(*G[j]))
    for i, j, k in itertools.combinations(range(len(G)), 3): W.append(L(*G[i]) + L(*G[j]) + L(*G[k])); W.append(L(*G[i]) + L(*G[k]) + L(*G[j]))
    return W
def unpack(x, g):
    img = {}
    for n, gen in enumerate(gens(g)):
        A = (x[8 * n:8 * n + 4] + 1j * x[8 * n + 4:8 * n + 8]).reshape(2, 2)
        A = A / np.sqrt(np.linalg.det(A) + 0j); img[gen] = A
    return img
PRE = {}
def residual(x, g, Ws, Ms):
    img = unpack(x, g); r = []
    key = (g, id(Ws))
    if key not in PRE: PRE[key] = [(apply(phi, w), w) for phi in Ms.values() for w in Ws]
    for fw, w in PRE[key]:
        d = np.trace(ev(fw, img)) - np.trace(ev(w, img)); r += [d.real, d.imag]
    return np.array(r)
search = {}
for g in (1, 2):
    Ws = trace_words(g); Ms = {n: p for n, p in moves(g).items() if not n.startswith("mu")}
    rng = np.random.default_rng(211 + g); sols = []
    for trial in range(40):
        x0 = rng.normal(size=8 * 2 * g)
        res = least_squares(residual, x0, args=(g, Ws, Ms), xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
        fun = float(np.sum(res.fun ** 2))
        if fun < 1e-14:
            img = unpack(res.x, g)
            tr = [complex(np.trace(ev(w, img))) for w in Ws]
            sols.append({"residual": fun, "max_abs_tr_minus_2": max(abs(t - 2) for t in tr), "max_abs_tr": max(abs(t) for t in tr),
                         "handle_triples": [[round(abs(np.trace(img[("a", k)])), 6), round(abs(np.trace(img[("b", k)])), 6), round(abs(np.trace(img[("a", k)] @ img[("b", k)])), 6)] for k in range(g)]})
    triv = sum(1 for s in sols if s["max_abs_tr_minus_2"] < 1e-5 or all(abs(t - 2) < 1e-5 for t in []))
    quat = sum(1 for s in sols if all(max(t) < 1e-5 for t in s["handle_triples"]))
    search[g] = {"converged": len(sols), "trivial_or_traces_2": sum(1 for s in sols if s["max_abs_tr_minus_2"] < 1e-5),
                 "quaternion_handles": quat, "other": [s for s in sols if s["max_abs_tr_minus_2"] >= 1e-5 and not all(max(t) < 1e-5 for t in s["handle_triples"])][:5]}
out["a_search"] = search
# (b), (c): the Heisenberg and extraspecial representations
def clock_shift(p):
    X = np.roll(np.eye(p), 1, axis=0).astype(complex); Z = np.diag([np.exp(2j * np.pi * j / p) for j in range(p)]); return X, Z
def kron_at(M, k, g, p):
    out = np.array([[1.0 + 0j]])
    for j in range(g): out = np.kron(out, M if j == k else np.eye(p))
    return out
def rand_word(g, n, rng):
    G = gens(g); return red([(G[rng.integers(len(G))], int(rng.choice([1, -1]))) for _ in range(n)])
def fixed(img, g, nwords=400, seed=7):
    rng = np.random.default_rng(seed); Ms = moves(g); bad = {}
    for nm, phi in Ms.items():
        for _ in range(nwords):
            w = rand_word(g, int(rng.integers(1, 9)), rng)
            if abs(np.trace(ev(apply(phi, w), img)) - np.trace(ev(w, img))) > 1e-8: bad[nm] = bad.get(nm, 0) + 1
    return bad
heis = {}
for p in (3, 5):
    for g in (1, 2):
        X, Z = clock_shift(p); img = {}
        for k in range(g): img[("a", k)] = kron_at(X, k, g, p); img[("b", k)] = kron_at(Z, k, g, p)
        heis["p=%d g=%d" % (p, g)] = fixed(img, g)
out["b_heisenberg_moves_breaking"] = heis
PX = np.array([[0, 1], [1, 0]], dtype=complex); PZ = np.array([[1, 0], [0, -1]], dtype=complex)
extra = {}
for g in (1, 2):
    for signs in itertools.product((1, 1j), repeat=2 * g):        # 1: square +I; i: square -I
        img = {}
        for k in range(g): img[("a", k)] = signs[2 * k] * kron_at(PX, k, g, 2); img[("b", k)] = signs[2 * k + 1] * kron_at(PZ, k, g, 2)
        bad = fixed(img, g, nwords=300)
        extra["g=%d squares %s" % (g, "".join("-" if s == 1j else "+" for s in signs))] = {"fixed": not bad, "moves_breaking": sorted(bad)}
out["c_extraspecial"] = extra
json.dump(out, open(HERE / "the_surface_route.json", "w"), indent=1, default=str)
print(json.dumps({"boundary_kept": out["boundary_kept"], "a": {g: {k: v for k, v in s.items() if k != "other"} for g, s in search.items()},
                  "a_other": {g: s["other"] for g, s in search.items()}, "b": heis,
                  "c_fixed": [k for k, v in extra.items() if v["fixed"]]}, indent=1, default=str))
