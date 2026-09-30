"""B1503 -- THE APEX INDEX RULE, run as sealed (PREREGISTRATION.md, sha256 in SEAL_LEDGER).

For every element gamma of B1501's census (the four homogeneous nearly Kaehler links, order <= 12, the listed automorphisms):
  0 = sum_points prod_j (1 - e^{-i theta_j})^{-1} + sum_curves (i/8) cot(theta/2) sin^{-2}(theta/2) (d_1 - d_2)
(the link's Dirac operator has no kernel, so its equivariant index vanishes; Atiyah-Singer's Lefschetz formula in Todd form).

The instrument:
- the fixed components by B1501's own sealed routine (same seeds), checked against census.json in number and type;
- the J-angles: d gamma on T^{1,0} (J the canonical J, constant in the left-translation frame);
- the degrees of a fixed sphere's normal J-eigenlines two ways: isotropy weights (the stabiliser of the point in the derived algebra of
  the centraliser, orthogonal to the part fixing the sphere pointwise; d_j = 2 w_j / w_T), and lattice Chern numbers over the sphere
  swept by the complementary su(2) (Fukui-Hatsugai-Suzuki, orientation fixed by deg TC = +2);
- tori: d_1 = d_2 = 0 (homogeneous; B1502 section 5's lattice value);
- the rule on every class to 1e-8, or the run stops.
Witten's cubic inflow of a curve with transverse Z_N: n = (N/2)(d_1 - d_2).
"""
import hashlib
import importlib.util
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SEALED_SHA256 = "d42607502486ef75759bb807912b9f4bd8c09965429080d04a237357885a1719"
RULE_TOL = 1e-8                    # sealed
DEG_TOL = 1e-6                     # sealed: degrees are integers to this
GRIDS = ((16, 32), (24, 48))       # the lattice sweep of a sphere: (polar rows, azimuthal columns)
CONTROLS = [("S6", (Fraction(0), Fraction(1, 13))), ("S6", (Fraction(1, 13), Fraction(3, 13))),
            ("CP3", (Fraction(0), Fraction(1, 13))), ("CP3", (Fraction(3, 26), Fraction(3, 26))),
            ("F12", (Fraction(1, 13), Fraction(1, 13))), ("S3xS3", (Fraction(1, 26),) * 3)]


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load(ROOT / "frontier" / "B1501_the_torus_link_census" / "verification" / "torus_link_census.py", "b1501_census")
C5 = _load(ROOT / "frontier" / "B1502_the_local_models_chirality" / "verification" / "cubic_inflow.py", "b1502_cubic_inflow")
LINKS = {}


# ------------------------------------------------------------------------------------------------------ the fixed-point terms
def point_term(eigs):
    """an isolated fixed point: prod_j (1 - e^{-i theta_j})^{-1}, e = e^{i theta} the eigenvalues of d gamma on T^{1,0}"""
    return complex(np.prod([1.0 / (1.0 - 1.0 / e) for e in eigs]))


def curve_term_general(lams, degs, chi):
    """a fixed curve: int_C Td(TC) prod_j (1 - mu_j e^{-x_j})^{-1}, mu_j = 1/lam_j, int_C x_j = d_j, int_C c_1(TC) = chi"""
    mus = [1.0 / l for l in lams]
    A = [1.0 / (1.0 - m) for m in mus]
    B = [-m / (1.0 - m) ** 2 for m in mus]
    total = chi / 2.0 * np.prod(A)
    for j in range(len(lams)):
        total += B[j] * degs[j] * np.prod([A[k] for k in range(len(lams)) if k != j])
    return complex(total)


def curve_term(theta, delta):
    """the closed form for the SU(3) case (normal e^{+-i theta}, d_1 + d_2 = -chi): (i/8) cot(theta/2) sin^{-2}(theta/2) delta"""
    return complex(1j / 8.0 / np.tan(theta / 2.0) / np.sin(theta / 2.0) ** 2 * delta)


def order_of(z, cap=200):
    return next(k for k in range(1, cap) if abs(z ** k - 1) < 1e-9)


# ------------------------------------------------------------------------------------------------------------- the J-analysis
def t10(link):
    w, V = np.linalg.eig(link.J)
    sel = [i for i in range(6) if abs(w[i] - 1j) < 1e-8]
    assert len(sel) == 3
    Q, _ = np.linalg.qr(V[:, sel])
    return Q


def d_on_t10(link, gam, g, Q):
    D = link.differential(gam, g)
    D3 = Q.conj().T @ D @ Q
    leak = float(np.abs(D @ Q - Q @ D3).max())
    return D3, leak


def curve_lines(D3):
    """eigen-decomposition on a curve: the tangent line (eigenvalue 1) and N_1 (e^{i theta}, 0 < theta < pi), N_2 (e^{-i theta})"""
    w, V = np.linalg.eig(D3)
    iT = int(np.argmin(np.abs(w - 1)))
    rest = [i for i in range(3) if i != iT]
    if abs(w[rest[0]].imag) < 1e-9 and abs(w[rest[1]].imag) < 1e-9:
        return {"tangent": (w[iT], V[:, iT]), "theta": float(np.pi), "N1": None, "N2": None, "eigs": w}
    i1 = rest[0] if w[rest[0]].imag > 0 else rest[1]
    i2 = rest[1] if i1 == rest[0] else rest[0]
    return {"tangent": (w[iT], V[:, iT]), "theta": float(np.angle(w[i1])), "N1": (w[i1], V[:, i1]), "N2": (w[i2], V[:, i2]),
            "eigs": w}


def ad_on_m(link, W):
    return np.array([[T.ip(Bt, W @ B - B @ W) for B in link.m_basis] for Bt in link.m_basis])


# ------------------------------------------------------------------------------------- sphere degrees by isotropy weights
def derived_basis(cbasis):
    br = [X @ Y - Y @ X for X in cbasis for Y in cbasis]
    br = [B for B in br if np.linalg.norm(B) > 1e-12]
    return T.orthonormal(br) if br else []


def sphere_weights(link, gam, rep, cbasis, Q, lines):
    """Z: the stabiliser of rep in [c, c], orthogonal to the part fixing the sphere pointwise; d_j = 2 w_j / w_T"""
    dc = derived_basis(cbasis)
    if not dc:
        return None
    M = np.array([[T.ip(B, T.dag(rep) @ Z @ rep) for Z in dc] for B in link.m_basis])      # m-part of Ad(rep^-1) Z
    N = T.null_space(M, 1e-9)
    s = [sum(N[i, j] * dc[i] for i in range(len(dc))) for j in range(N.shape[1])]
    s = T.orthonormal(s) if s else []
    vecs = [lines["tangent"][1], lines["N1"][1], lines["N2"][1]]
    W = np.zeros((len(s), 3))
    offdiag = 0.0
    for k, Z in enumerate(s):
        A3 = Q.conj().T @ ad_on_m(link, T.dag(rep) @ Z @ rep) @ Q
        V = np.array(vecs).T
        Dg = np.linalg.solve(V, A3 @ V)                            # A3 in the eigenbasis of d gamma: diagonal
        offdiag = max(offdiag, float(np.abs(Dg - np.diag(np.diag(Dg))).max()))
        W[k] = np.diag(Dg).imag
    wT = W[:, 0]
    if np.linalg.norm(wT) < 1e-9:
        return {"error": "no stabiliser element rotates the tangent line", "dim s": len(s)}
    z = wT / np.linalg.norm(wT)                                    # orthogonal to ker w_T in the orthonormal basis of s
    w = z @ W
    d1, d2 = 2 * w[1] / w[0], 2 * w[2] / w[0]
    # the moving directions: [c, c] minus s (2-dimensional for a sphere)
    S = np.array([[T.ip(a, b) for b in dc] for a in s]) if s else np.zeros((0, len(dc)))
    P = T.null_space(S, 1e-9) if len(s) else np.eye(len(dc))
    moving = T.orthonormal([sum(P[i, j] * dc[i] for i in range(len(dc))) for j in range(P.shape[1])])
    Z0 = sum(z[k] * s[k] for k in range(len(s)))
    return {"d1": float(d1), "d2": float(d2), "dim [c,c]": len(dc), "dim stabiliser": len(s),
            "dim kernel on the sphere": len(s) - 1, "weights (T, N1, N2)": [float(x) for x in w],
            "weights off-diagonal": offdiag, "moving": moving, "Z0": Z0}


# ------------------------------------------------------------------------------------------- sphere degrees by lattice
def first_return(link, X, rep):
    base = link.embed(rep)

    def dist(t):
        return float(np.linalg.norm(link.embed(T.expm_skew(t * X) @ rep) - base))
    ts = np.linspace(0.01, 40.0, 16000)
    d = np.array([dist(t) for t in ts])
    # the first local minimum below 1e-2 after leaving the point
    for i in range(1, len(ts) - 1):
        if d[i] < 1e-2 and d[i] <= d[i - 1] and d[i] <= d[i + 1] and ts[i] > 0.1:
            a, b = ts[i - 1], ts[i + 1]
            for _ in range(80):                                    # golden-section refinement
                m1, m2 = a + 0.382 * (b - a), a + 0.618 * (b - a)
                if dist(m1) < dist(m2):
                    b = m2
                else:
                    a = m1
            t0 = (a + b) / 2
            return t0, dist(t0)
    return None, None


def sphere_lattice(link, gam, rep, Q, theta, moving, grid):
    X, Y = moving
    Tp, resid = first_return(link, X, rep)
    if Tp is None:
        return {"error": "no return of the sweep"}
    n_th, n_ph = grid
    ths = np.linspace(0.0, Tp / 2.0, n_th + 1)
    phs = 2 * np.pi * np.arange(n_ph) / n_ph
    frames = {"T": [], "N1": [], "N2": []}
    worst_fix, worst_leak, antipode = 0.0, 0.0, 0.0
    for a in ths:
        rows = {"T": [], "N1": [], "N2": []}
        for b in phs:
            g = T.expm_skew(a * (np.cos(b) * X + np.sin(b) * Y)) @ rep
            worst_fix = max(worst_fix, float(np.linalg.norm(link.residual(gam, g))))
            D3, leak = d_on_t10(link, gam, g, Q)
            worst_leak = max(worst_leak, leak)
            w, V = np.linalg.eig(D3)
            targets = {"T": 1.0, "N1": np.exp(1j * theta), "N2": np.exp(-1j * theta)}
            for key, tv in targets.items():
                i = int(np.argmin(np.abs(w - tv)))
                c = Q @ V[:, i]
                Yr = T.from_coords(c.real, link.m_basis)
                Yi = T.from_coords(c.imag, link.m_basis)
                v = link.dembed(g, Yr) + 1j * link.dembed(g, Yi)
                rows[key].append((v / np.linalg.norm(v))[:, None])
        for key in rows:
            frames[key].append(rows[key])
    # the far pole is one point
    far = [link.embed(T.expm_skew((Tp / 2) * (np.cos(b) * X + np.sin(b) * Y)) @ rep) for b in phs[:4]]
    antipode = float(max(np.linalg.norm(f - far[0]) for f in far))
    out = {"return time": Tp, "return residual": resid, "far pole spread": antipode, "worst fixed-point residual": worst_fix,
           "worst T10 leak": worst_leak}
    for key in frames:
        out["c1 " + key] = polar_chern(frames[key])
    return out


def polar_chern(frames):
    """FHS on a polar grid: rows 0..n_th (both poles included), columns periodic"""
    n1, n2 = len(frames), len(frames[0])

    def link_(A, B):
        d = complex(np.vdot(A, B))                                 # frames are unit columns: the overlap <A, B>
        return d / abs(d)
    total = 0.0
    for i in range(n1 - 1):
        for j in range(n2):
            a, b = frames[i][j], frames[i + 1][j]
            c, d = frames[i + 1][(j + 1) % n2], frames[i][(j + 1) % n2]
            total += np.angle(link_(a, b) * link_(b, c) * link_(c, d) * link_(d, a))
    return float(total / (2 * np.pi))


# ------------------------------------------------------------------------------------------------------------- one class
def components(link, cls):
    """B1501's run_class up to the clustering, with the same random stream: the same components, representatives kept"""
    label = T.class_label(cls)
    rng = np.random.default_rng(T.label_seed(label))
    gam = T.gamma_of(link, cls)
    cbasis = link.centraliser_basis(gam)
    g, res = T.newton_fixed(link, gam, link.random_elements(rng, T.N_SEEDS))
    sols = g[res < T.CONV_TOL]
    comps = []
    if len(sols):
        groups, _ = T.cluster_components(link, gam, sols, rng)
        for members in groups:
            rep = sols[members[0]]
            dim = 6 - T.rank_of(link.differential(gam, rep) - np.eye(6), 1e-8)
            top = T.topology(link, rep, cbasis)
            comps.append({"rep": rep, "dim": int(dim), "type": top["type"], "seeds": len(members)})
    return label, gam, cbasis, comps


def run_class(cls):
    t0 = time.time()
    link = LINKS[cls["link"]]
    label, gam, cbasis, comps = components(link, cls)
    Q = t10(link)
    rec = {"label": label, "link": cls["link"], "order": cls["order"], "outer": cls["outer"], "q": [str(x) for x in cls["q"]],
           "components": []}
    s_pts, s_cur = 0j, 0j
    for c in comps:
        rep = c["rep"]
        D3, leak = d_on_t10(link, gam, rep, Q)
        cr = {"type": c["type"], "dim": c["dim"], "seeds": c["seeds"], "T10 leak": leak}
        if c["type"] == "point":
            eigs = np.linalg.eigvals(D3)
            cr["angles"] = sorted(float(np.angle(e)) for e in eigs)
            cr["det - 1"] = float(abs(np.prod(eigs) - 1))
            cr["term"] = point_term(eigs)
            s_pts += cr["term"]
        else:
            lines = curve_lines(D3)
            cr["theta"] = lines["theta"]
            if lines["N1"] is None:                                  # order-2 normal: no condition, Delta undefined
                cr["term"] = 0j
                cr["normal"] = "e^{i pi} (order 2): contributes 0"
            elif c["type"] == "torus":
                cr["N"] = order_of(lines["N1"][0])
                cr["d"] = [0, 0]
                cr["degrees from"] = "homogeneous torus (B1502 section 5)"
                cr["term"] = curve_term(lines["theta"], 0)
                cr["n"] = 0
            elif c["type"] == "sphere":
                cr["N"] = order_of(lines["N1"][0])
                sw = sphere_weights(link, gam, rep, cbasis, Q, lines)
                if sw is None or "error" in sw:
                    cr["error"] = sw
                    cr["term"] = complex(np.nan)
                else:
                    cr["weights"] = {k: v for k, v in sw.items() if k not in ("moving", "Z0")}
                    d1, d2 = sw["d1"], sw["d2"]
                    lat = []
                    for grid in GRIDS:
                        if len(sw["moving"]) != 2:
                            lat.append({"error": "moving directions %d" % len(sw["moving"])})
                            continue
                        lat.append(dict(grid=list(grid), **sphere_lattice(link, gam, rep, Q, lines["theta"], sw["moving"], grid)))
                    cr["lattice"] = lat
                    D1, D2 = int(round(d1)), int(round(d2))
                    cr["d"] = [D1, D2]
                    cr["integral"] = bool(abs(d1 - D1) < DEG_TOL and abs(d2 - D2) < DEG_TOL)
                    cr["d1 + d2 = -2"] = bool(D1 + D2 == -2)
                    agree = True
                    for L_ in lat:
                        if "error" in L_:
                            agree = False
                            continue
                        sgn = 1.0 if L_["c1 T"] > 0 else -1.0
                        agree &= abs(sgn * L_["c1 T"] - 2) < 1e-6 and abs(sgn * L_["c1 N1"] - D1) < 1e-6 and \
                            abs(sgn * L_["c1 N2"] - D2) < 1e-6
                    cr["lattice agrees"] = bool(agree)
                    cr["term"] = curve_term(lines["theta"], D1 - D2)
                    cr["term (general Todd form)"] = curve_term_general([lines["N1"][0], lines["N2"][0]], [D1, D2], 2)
                    cr["n"] = cr["N"] / 2 * (D1 - D2)
            else:
                cr["error"] = "unexpected type"
                cr["term"] = complex(np.nan)
            s_cur += cr["term"]
        rec["components"].append(cr)
    rec["points' sum"] = s_pts
    rec["curves' sum"] = s_cur
    rec["S"] = s_pts + s_cur
    rec["seconds"] = round(time.time() - t0, 1)
    return rec


def jsonable(x):
    if isinstance(x, complex):
        return [x.real, x.imag]
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, np.ndarray):
        return jsonable(x.tolist())
    return x


# ------------------------------------------------------------------------------------------------------ the banked identity
def banked_identity(log):
    out = {}
    log("BANKED IDENTITY")
    # the formula's controls: holomorphic Lefschetz number 1
    worst = 0.0
    for lam in (np.exp(0.7j), np.exp(2.1j), np.exp(1j * np.pi / 3), np.exp(-2.5j)):
        cp1 = point_term([lam]) + point_term([1 / lam])
        cp2 = point_term([1 / lam, 1 / lam]) + curve_term_general([lam], [1], 2)
        worst = max(worst, abs(cp1 - 1), abs(cp2 - 1))
    out["CP1 and CP2 Lefschetz number 1 (worst)"] = worst
    log("  the terms: CP^1 (z -> lam z) and CP^2 (diag(1, 1, lam): a line with normal O(1) and a point) give Lefschetz number 1 to %.1e"
        % worst)
    assert worst < 1e-12
    worst = 0.0
    for th in (0.4, 1.3, 2 * np.pi / 3, 2.9):
        for d1, d2, chi in ((0, -2, 2), (-1, -1, 2), (3, -5, 2), (1, -1, 0), (-2, 2, 0)):
            worst = max(worst, abs(curve_term_general([np.exp(1j * th), np.exp(-1j * th)], [d1, d2], chi)
                                   - curve_term(th, d1 - d2)))
    out["closed curve form = general Todd form (worst)"] = worst
    log("  the closed curve term equals the general Todd form (chi terms cancel when d1 + d2 = -chi) to %.1e" % worst)
    assert worst < 1e-12
    ctrl = {m: float(round(C5.lattice_chern(C5.qwz_frames(m, 24))[0], 9)) + 0.0 for m in (-3.0, -1.0, 1.0, 3.0)}
    out["QWZ"] = {str(k): v for k, v in ctrl.items()}
    log("  the lattice routine: Qi-Wu-Zhang lower band %s" % ctrl)
    assert abs(abs(ctrl[1.0]) - 1) < 1e-9 and abs(abs(ctrl[-1.0]) - 1) < 1e-9 and ctrl[3.0] == 0 and ctrl[-3.0] == 0
    rng = np.random.default_rng(1503)
    for name, link in LINKS.items():
        rec = T.structure_checks(link, rng)
        out["structures " + name] = {k: rec[k] for k in ("J^2+1", "J orthogonal", "Ad(K) commutes with J")}
        log("  %-6s J^2 = -1 to %.1e, J orthogonal to %.1e, Ad(K) commutes with J to %.1e, listed automorphisms preserve J" % (
            name, rec["J^2+1"], rec["J orthogonal"], rec["Ad(K) commutes with J"]))
    # non-census controls (order 13, outside the census's order <= 12): the whole pipeline, one of each fixed-set shape
    ctrl = []
    for link, q in CONTROLS:
        cls = {"link": link, "q": q, "outer": None, "order": T.left_order(LINKS[link], q)}
        r = run_class(cls)
        ok = abs(r["S"]) < RULE_TOL and all(not c.get("error") and c["T10 leak"] < 1e-9 for c in r["components"]) and all(
            c["integral"] and c["d1 + d2 = -2"] and c["lattice agrees"] for c in r["components"] if c["type"] == "sphere")
        ctrl.append({"class": r["label"], "shape": [c["type"] for c in r["components"]], "|S|": abs(r["S"]),
                     "d": [c.get("d") for c in r["components"] if c["type"] != "point"], "ok": ok})
        log("  control %-20s (order %d, not in the census): %s, |S| = %.1e, curve degrees %s: %s" % (
            r["label"], cls["order"], dict(Counter(c["type"] for c in r["components"])), abs(r["S"]), ctrl[-1]["d"],
            "PASS" if ok else "FAIL"))
        assert ok, r["label"]
    out["controls"] = ctrl
    return out


def main(workers=4, identity_only=False):
    t0 = time.time()
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)
    digest = hashlib.sha256((HERE.parent / "PREREGISTRATION.md").read_bytes()).hexdigest()
    assert digest == SEALED_SHA256, digest
    log("B1503 THE APEX INDEX RULE, run as sealed. PREREGISTRATION sha256 %s (matches SEAL_LEDGER)" % digest)
    for name, L in T.LINKS.items():
        LINKS[name] = L()
    identity = banked_identity(log)
    if identity_only:
        log("THE BANKED IDENTITY PASSES (formula, lattice, structures, controls); S6's pairs are checked at the start of the run")
        (HERE / "identity_run.txt").write_text("\n".join(lines) + "\n")
        return 0
    census = {r["label"]: r for r in json.load(open(ROOT / "frontier" / "B1501_the_torus_link_census" / "verification"
                                                     / "census.json"))["records"]}
    classes = []
    for name, link in LINKS.items():
        classes += T.enumerate_classes(link)
    log("classes: %d (B1501's census)" % len(classes))
    import multiprocessing as mp
    ctx = mp.get_context("fork")
    s6 = [c for c in classes if c["link"] == "S6"]
    rest = [c for c in classes if c["link"] != "S6"]
    with ctx.Pool(workers) as pool:
        recs_s6 = list(pool.imap(run_class, s6, chunksize=1))
    pairs = [r for r in recs_s6 if [c["type"] for c in r["components"]] == ["point", "point"]]
    worst_pair = max(abs(r["components"][0]["term"] + r["components"][1]["term"]) for r in pairs)
    log("  S6's pairs: %d two-point classes, the two terms opposite to %.1e" % (len(pairs), worst_pair))
    identity["S6 pairs"] = {"classes": len(pairs), "worst |t1 + t2|": worst_pair}
    assert worst_pair < RULE_TOL, "S6 pairs fail: the run stops"
    log("THE BANKED IDENTITY PASSES")
    with ctx.Pool(workers) as pool:
        recs = recs_s6 + list(pool.imap(run_class, rest, chunksize=1))
    log("census evaluated in %.0f s" % (time.time() - t0))

    # ---- the identity against census.json, and the internal checks
    mismatch, bad = [], []
    for r in recs:
        cen = census[r["label"]]
        a = Counter(c["type"] for c in r["components"])
        b = Counter(c["topology"]["type"] for c in cen["components"])
        if a != b:
            mismatch.append((r["label"], dict(a), dict(b)))
        for c in r["components"]:
            if c.get("error") or c["T10 leak"] > 1e-9 or (c["type"] == "point" and c["det - 1"] > 1e-9):
                bad.append((r["label"], c["type"], c.get("error"), c["T10 leak"]))
            if c["type"] == "sphere" and "d" in c and not (c["integral"] and c["d1 + d2 = -2"] and c["lattice agrees"]):
                bad.append((r["label"], "sphere degrees", c["weights"], c.get("lattice")))
    log("components against census.json: %s" % ("all %d classes agree" % len(recs) if not mismatch else "MISMATCH %s" % mismatch[:5]))
    log("internal checks (T10 invariant, det 1 at points, integral degrees, d1 + d2 = -2, weights = lattice): %s"
        % ("all pass" if not bad else "FAIL %s" % bad[:3]))
    worst = max((abs(r["S"]) for r in recs if r["components"]), default=0.0)
    with_fix = [r for r in recs if r["components"]]
    rule_ok = all(abs(r["S"]) < RULE_TOL for r in with_fix) and not mismatch and not bad
    log("THE RULE on %d classes with fixed points: worst |S| = %.1e -> %s" % (len(with_fix), worst, "HOLDS" if rule_ok else "FAILS"))
    out = {"sealed sha256": digest, "banked identity": identity, "classes": len(recs), "classes with fixed points": len(with_fix),
           "component mismatches": mismatch, "internal failures": bad, "worst |S|": worst, "rule holds": rule_ok}
    if not rule_ok:
        log("THE RUN STOPS: no census reading is made")
        json.dump(jsonable(dict(out, records=recs)), open(HERE / "apex_index_rule.json", "w"), indent=1)
        (HERE / "apex_index_rule_run.txt").write_text("\n".join(lines) + "\n")
        return 1

    # ---- the reading
    out["reading"] = readout(recs, log)
    out["records"] = recs
    log("%.0f s in all" % (time.time() - t0))
    json.dump(jsonable(out), open(HERE / "apex_index_rule.json", "w"), indent=1)
    (HERE / "apex_index_rule_run.txt").write_text("\n".join(lines) + "\n")
    return 0


def kinds(r):
    k = Counter(c["type"] for c in r["components"])
    return (k.get("point", 0), k.get("sphere", 0), k.get("torus", 0))


def readout(recs, log):
    rd = {}
    tol = 1e-9
    # D1, D2, D3: decided at design time
    s6_single = [r for r in recs if r["link"] == "S6" and kinds(r) == (0, 1, 0)]
    d1 = all(c.get("d", [0, 0])[0] == c.get("d", [0, 0])[1] for r in s6_single for c in r["components"])
    tor = [r for r in recs if kinds(r)[2] > 0]
    d2 = all(abs(r["S"]) < tol and all(c.get("n", 0) == 0 for c in r["components"]) for r in tor)
    sig = {r["label"]: r for r in recs if r["link"] == "S3xS3" and kinds(r) == (1, 1, 0)}
    d3 = {}
    for lab, r in sig.items():
        sph = [c for c in r["components"] if c["type"] == "sphere"][0]
        pt = [c for c in r["components"] if c["type"] == "point"][0]
        d3[lab] = {"point angles": pt["angles"], "point term": pt["term"], "sphere theta": sph["theta"], "sphere d": sph.get("d"),
                   "Delta": sph["d"][0] - sph["d"][1] if "d" in sph else None, "N": sph.get("N"), "n": sph.get("n")}
    d3_ok = d3.get("S3xS3 L(0,0,0) o sigma", {}).get("Delta") == 2 and d3.get("S3xS3 L(0,0,0) o sigma^2", {}).get("Delta") == -2
    rd["D1 S6 single spheres Delta = 0"] = d1
    rd["D2 torus classes n = 0"] = d2
    rd["D3 the 3-symmetry"] = d3
    rd["D3 holds (Delta = 2 for sigma, -2 for sigma^2)"] = d3_ok
    log("DECIDED AT DESIGN TIME, CHECKED: D1 (S6's %d single spheres Delta = 0) %s; D2 (%d torus classes n = 0) %s; D3 (the 3-symmetry) %s"
        % (len(s6_single), "YES" if d1 else "NO", len(tor), "YES" if d2 else "NO", "YES" if d3_ok else "NO"))
    for lab, v in d3.items():
        log("   %s: point angles %s, term %s; sphere theta %.6f, (d1, d2) = %s, Delta %s, N %s, n = %s" % (
            lab, [round(a, 6) for a in v["point angles"]], np.round(v["point term"], 9), v["sphere theta"], v["sphere d"], v["Delta"],
            v["N"], v["n"]))

    # P1: CP3's two-sphere classes
    two = [r for r in recs if r["link"] == "CP3" and kinds(r) == (0, 2, 0) and r["order"] >= 3]
    p1_rows, p1_ok, p1_pi = [], True, []
    for r in two:
        sph = r["components"]
        if any("d" not in c for c in sph):
            p1_pi.append(r["label"])
            continue
        th = [c["theta"] for c in sph]
        De = [c["d"][0] - c["d"][1] for c in sph]
        ok = abs(th[0] - th[1]) < 1e-9 and De[0] == -De[1] and abs(De[0]) == 2
        p1_ok &= ok
        p1_rows.append({"class": r["label"], "theta": th, "d": [c["d"] for c in sph], "Delta": De, "n": [c["n"] for c in sph],
                        "pair": ok})
    rd["P1"] = {"classes": len(two), "evaluated": len(p1_rows), "theta = pi (listed separately)": p1_pi, "rows": p1_rows,
                "answer": "YES" if p1_ok and p1_rows else "NO"}
    log("P1 (CP3's two-sphere classes of order >= 3: one angle, Delta = +-2 opposite): %s -- %d evaluated, %d with theta = pi listed"
        % (rd["P1"]["answer"], len(p1_rows), len(p1_pi)))
    for row in p1_rows:
        if not row["pair"]:
            log("   not a pair: %s theta %s d %s" % (row["class"], [round(t, 6) for t in row["theta"]], row["d"]))

    # P2: CP3's one-sphere classes
    one = [r for r in recs if r["link"] == "CP3" and kinds(r) == (2, 1, 0)]
    p2_rows, p2_ok, p2_pi = [], True, []
    for r in one:
        sph = [c for c in r["components"] if c["type"] == "sphere"][0]
        if "d" not in sph:
            p2_pi.append(r["label"])
            continue
        ok = abs(r["points' sum"]) < tol and sph["d"][0] == sph["d"][1]
        p2_ok &= ok
        p2_rows.append({"class": r["label"], "points' sum": r["points' sum"], "sphere d": sph["d"], "ok": ok})
    rd["P2"] = {"classes": len(one), "evaluated": len(p2_rows), "theta = pi (listed separately)": p2_pi, "rows": p2_rows,
                "answer": "YES" if p2_ok and p2_rows else "NO"}
    log("P2 (CP3's one-sphere classes: the points cancel, Delta = 0): %s -- %d evaluated, %d with theta = pi listed"
        % (rd["P2"]["answer"], len(p2_rows), len(p2_pi)))
    for row in p2_rows:
        if not row["ok"]:
            log("   not so: %s points' sum %s sphere d %s" % (row["class"], np.round(row["points' sum"], 9), row["sphere d"]))

    # P3: F12's three-sphere classes
    three = [r for r in recs if r["link"] == "F12" and kinds(r) == (0, 3, 0)]
    p3_bad, p3_n, p3_pi = [], 0, 0
    for r in three:
        for c in r["components"]:
            if "d" not in c:
                p3_pi += 1
                continue
            p3_n += 1
            if c["d"][0] != c["d"][1]:
                p3_bad.append((r["label"], c["d"], c["theta"]))
    rd["P3"] = {"classes": len(three), "spheres evaluated": p3_n, "theta = pi spheres": p3_pi, "Delta != 0": p3_bad,
                "answer": "YES" if not p3_bad else "NO"}
    log("P3 (F12's spheres all Delta = 0): %s -- %d spheres evaluated in %d classes, %d with theta = pi; exceptions %s"
        % (rd["P3"]["answer"], p3_n, len(three), p3_pi, p3_bad[:6]))

    # P4: the table
    table = {}
    for link in ("S6", "S3xS3", "CP3", "F12"):
        rs = [r for r in recs if r["link"] == link and r["components"]]
        curves = [c for r in rs for c in r["components"] if c["type"] in ("sphere", "torus") and "d" in c]
        forced = [r["label"] for r in rs if any(c.get("n", 0) != 0 for c in r["components"])]
        dset = sorted({tuple(c["d"]) for c in curves})
        nmax = max((abs(c["n"]) for c in curves), default=0)
        balanced_by_points = [r["label"] for r in rs if abs(r["curves' sum"]) > tol and abs(r["points' sum"]) > tol]
        table[link] = {"classes with fixed points": len(rs), "curves with degrees": len(curves), "classes with n != 0": len(forced),
                       "(d1, d2) met": [list(x) for x in dset], "largest |n|": nmax, "curves balanced against points": balanced_by_points,
                       "examples with n != 0": forced[:8]}
        log("P4 %-6s %3d classes with fixed points; %3d curves with degrees, (d1, d2) met %s; %d classes with n != 0 (largest |n| %s); "
            "curves balanced against points in %d classes %s" % (link, len(rs), len(curves), dset, len(forced), nmax,
                                                                   len(balanced_by_points), balanced_by_points[:4]))
    rd["P4"] = table
    return rd


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--identity"]
    raise SystemExit(main(int(args[0]) if args else 4, identity_only="--identity" in sys.argv))
