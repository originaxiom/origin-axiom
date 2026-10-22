"""B1722 (P-285, the completion map's C2): which thread? The record's two measures on B1720's census of 121 thread
classes, read against the six measured ratios with the calibration sealed in.  No new mass computation: the rows are
B1720's stored output (ceabd0407), pinned by its sha256.
  mu_U  the weave's uniform word measure (B1629): a primitive class of length n carries its n rotations, each 2^-n.
  mu_A  the action weight at L154's c = 6 (B1088: S = -Vol sigma, c = 6 sigma): e^{-c Vol / 6 pi} = e^{-Vol/pi}, Vol the
        hyperbolic volume of the class's once-punctured torus bundle (SnapPy, b++w).
For a target t (the six ratios) let f_k(t) be class k's best worst factor over its lines, horocycles and readings.
  E_mu(t) = sum_k mu(k) ln f_k(t)          the measure-weighted mean log-misfit of a thread drawn from mu (no threshold)
Cells: for each mu, the fraction of 4 000 random hierarchical targets (B1695's prior, seed 1722) with E_mu <= E_mu(data).
Read-outs: P_mu(f <= F) for F = 1.5, 2, 3; the classes carrying most of each measure; the best class's volume and weights.
Importing computes nothing.
    python3 -B which_thread.py      # writes which_thread.json beside itself"""
import hashlib, json, math, random, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1720 = ROOT / "frontier" / "B1720_the_thread_fixes_the_point" / "verification" / "the_thread_census.json"
B1720_SHA = "6073f24b7c3437b075991f5364a3dbf3c094f8964868d4f3b06512a4a7063305"   # B1720's committed output (ceabd0407)
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
N = 4000


def rows_by_class(G):
    out = [[] for _ in G["classes"]]
    for p in G["rows"]:
        for hor in ("L_max", "L_2"):
            for rd in ("S", "St", "conjS"):
                vals = p["up|%s|%s" % (hor, rd)] + p["down|%s|S" % hor] + p["lep|%s|S" % hor]
                out[p["class"]].append([math.log(max(z, 1e-300)) for z in vals])
    return [np.array(r) for r in out]


def f_of(R, target):
    """each class's best worst factor (in log) for the target"""
    return np.array([np.min(np.max(np.abs(r - target), axis=1)) for r in R])


def measures(words):
    import snappy
    muU = np.array([len(w) * 2.0 ** -len(w) for w in words]); muU /= muU.sum()
    vol = np.array([float(snappy.Manifold("b++" + w).volume()) for w in words])
    muA = np.exp(-vol / math.pi); muA /= muA.sum()
    return muU, muA, vol


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2: break
        tg += [r2, r1]
    return np.log(np.array(tg))


def main():
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA
    assert hashlib.sha256(B1720.read_bytes()).hexdigest().startswith(B1720_SHA)
    d = json.loads(DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    tgt = np.log(np.array([d["c"] / d["t"], d["u"] / d["t"], d["s"] / d["b"], d["d"] / d["b"], d["mu"] / d["tau"], d["e"] / d["tau"]]))
    G = json.loads(B1720.read_text(encoding="utf-8")); words = [c["word"] for c in G["classes"]]
    R = rows_by_class(G); muU, muA, vol = measures(words); fd = f_of(R, tgt)
    E = lambda mu, lf: float(np.sum(mu * lf))
    EU, EA = E(muU, fd), E(muA, fd)
    rng = random.Random(1722); hU = hA = 0; sU, sA = [], []
    for _ in range(N):
        lf = f_of(R, r_masses(rng)); eu, ea = E(muU, lf), E(muA, lf); sU.append(eu); sA.append(ea)
        hU += eu <= EU + 1e-12; hA += ea <= EA + 1e-12
    P = lambda mu, F: float(np.sum(mu[fd <= math.log(F) + 1e-12]))
    top = lambda mu: [(words[i], round(float(mu[i]), 4), round(math.exp(fd[i]), 3)) for i in np.argsort(-mu)[:6]]
    best = int(np.argmin(fd))
    out = {"B1720_rows_sha256": hashlib.sha256(B1720.read_bytes()).hexdigest(), "classes": len(words),
           "data": {"E_uniform": EU, "E_action": EA, "P_uniform": {str(F): P(muU, F) for F in (1.5, 2, 3)}, "P_action": {str(F): P(muA, F) for F in (1.5, 2, 3)},
                    "best_class": words[best], "best_factor": math.exp(fd[best]), "best_class_volume": float(vol[best]),
                    "best_class_mu_uniform": float(muU[best]), "best_class_mu_action": float(muA[best])},
           "calibration_uniform": {"N": N, "fraction_as_good": hU / N, "median_E": float(np.median(sU))},
           "calibration_action": {"N": N, "fraction_as_good": hA / N, "median_E": float(np.median(sA))},
           "top_classes_uniform": top(muU), "top_classes_action": top(muA),
           "W1_uniform_specific_p_below_0.01": hU / N <= 0.01, "W2_action_specific_p_below_0.01": hA / N <= 0.01}
    json.dump(out, open(HERE / "which_thread.json", "w"), indent=1)
    print("W1 (uniform)", out["W1_uniform_specific_p_below_0.01"], hU / N, "| W2 (action)", out["W2_action_specific_p_below_0.01"], hA / N)


if __name__ == "__main__":
    main()
