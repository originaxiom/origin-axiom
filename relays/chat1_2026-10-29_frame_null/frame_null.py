"""THE FRAME NULL (P-412): the script of the sealed rule FRAME_NULL_RULE.md (this directory; sealed and pushed before this
script was committed).  One command, resumable:
    python3 -B frame_null.py --run [--workers 2] [--max-seconds 6600] > frame_null_run.txt
        C0 (a)-(d) and the stop rule; then the draws in chunks of 5 000 (N1 chunks 0-19, N2 100-119, R1 200-203, R2
        300-303), each saved in chunks_frame_null/ (git-ignored); when every chunk is done, the cells: writes
        frame_null_cells.json and prints the cells.  A part stopped by its time limit prints progress counts only.
    python3 -B frame_null.py --synthetic
        the arithmetic on synthetic arrays only (no row of the population is read): the round trip, the fast path against
        a direct sum on both menus and for every null, the marginals, and the timing.
The population: B1753's completed census as B1798 assembled it.  The measure: B1741's chi2_six (its sigmas, its seat
configurations, its tie rule), with the lepton factor over the GJ scan's nine values (M9).  The exponents: B1785's
exponents.json, a fixed reference transform.  Extracted from main at REV with the pins below."""
import contextlib, gzip, hashlib, importlib.util, io, json, math, os, pathlib, subprocess, sys, tempfile, time
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / ".git").exists())
CH = HERE / "chunks_frame_null"
OUT_CELLS = HERE / "frame_null_cells.json"
REV = "8edb4b560"
V41 = "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/"
V49 = "frontier/B1749_the_six_at_fresh_apexes/verification/"
V53 = "frontier/B1753_the_six_on_the_five_ality_lines/verification/"
V98 = "frontier/B1798_the_six_graded_under_the_class_choosing_null/verification/"
EXJ = "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"
HZ = "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
FILES = {
    V41 + "compare.py": "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd",
    HZ: "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f",
    "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json": "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606",
    V49 + "compare.py": "4343edad05853db04989da1461e1bb99a9151180d17e483a16386454f39740e6",
    V53 + "census.jsonl": "c7f58dced34d6858bcfed9d25e01dfe27d4f212a29dd3a4d53f49010ad410c69",
    V98 + "feat_null.py": "a91e5878842333639eb8c85bad39dc65c40c8735d0d465756a2c1f024d7a3d65",
    V98 + "b1753_all266/census_ext.jsonl.gz": "e5a092850aa050e44531b53601c3677dea10b02c4bd52cefc677c6f67d8d5c40",
    V98 + "b1753_all266/census_ext_tail.jsonl.gz": "943f71b79db6e7f76527181833c13cc883bf9ea99707c2ca80b1f40e56b8a856",
    V98 + "b1753_all266/RAW_SHA256.txt": "0c25fb164e0fc1c286cf1a12395a8d8500ac0b30bf1f01a3db3bf7b8cf580784",
    EXJ: "541552c89269f6bc8ba434e1b8096179360c0c1adcf9697d08a423d54867ddf6",
    "frontier/B1726_the_two_ingredients_replicated/verification/census.py": "185cf17d8b51c11559bf14650d5ad1dd12745eaa228fc40da0a8b9181d1986bf",
    "frontier/B1723_the_golden_valley/verification/b1656_funcs.py": "31f09c433c14312d9cee8cfa29a632a72ce13fc46ae838757bf9b22958f22528",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py": "a8d4ea9bae79dde894b192b7c3645685c1c97890665c96123be20ea6e9073aac",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/qseries.py": "113b36d3da004a8a0b69d6f3fd8a38776f56ecbd14254e843c41232741ff1e6d",
    "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json": "688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774",
}
T_SEAT = 2.739034460748371                       # B1798's data minimum on the seat menu (control (b))
POINTS, DUPS, NLINES, NAPEX = 59318, 247, 266, 223
CHUNK = 5000
JOBS = {"N1": range(0, 20), "N2": range(100, 120), "R1": range(200, 204), "R2": range(300, 304)}
DRAWS = {"N1": 100000, "N2": 100000, "R1": 20000, "R2": 20000}
M_GRADE, M_READ = 100, (59, 100)
SECS, RDS, HORS, GENS = ("up", "down", "lep"), ("S", "St"), ("L_max", "L_2"), ("m2/m3", "m1/m3")
NAMES = ("up2", "up1", "down2", "down1", "lep2", "lep1")
SEAT_CFG = ((1, 0, 0), (1, 1, 1))                # (up, down, lepton) reading index, S~ = 1, S = 0
C_SEAT = (1.0, 3.0)
C_NINE = (1 / 3, 1 / 2, 2 / 3, 1.0, 3 / 2, 2.0, 3.0, 4.0, 5.0)   # the GJ scan's nine values (B1798 sec. 4)
TIE = 1e-9
_G = {}


# ------------------------------------------------------------------------------------------------ main's instruments
def tree():
    """main's files at REV, extracted with the pins into a private tree (GENESIS.md is the instruments' root marker)"""
    if "tmp" not in _G:
        tmp = pathlib.Path(os.environ.get("FNULL_TMP") or tempfile.mkdtemp())
        if not (tmp / "GENESIS.md").exists():
            for rel, sha in FILES.items():
                b = subprocess.run(["git", "show", "%s:%s" % (REV, rel)], cwd=ROOT, capture_output=True, check=True).stdout
                assert hashlib.sha256(b).hexdigest() == sha, rel
                p = tmp / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
            raw = {}
            for l in (tmp / V98 / "b1753_all266/RAW_SHA256.txt").read_text().splitlines():
                if l.strip():
                    h, name = l.split(); raw[name] = h
            for gz in ("census_ext.jsonl.gz", "census_ext_tail.jsonl.gz"):
                b = gzip.decompress((tmp / V98 / "b1753_all266" / gz).read_bytes())
                assert hashlib.sha256(b).hexdigest() == raw["b1753_all266/" + gz[:-3]], gz
                (tmp / V98 / "b1753_all266" / gz[:-3]).write_bytes(b)
            (tmp / "GENESIS.md").write_text("root marker for the imported instruments\n")
        os.environ["FNULL_TMP"] = str(tmp)
        _G["tmp"] = tmp
    return _G["tmp"]


def _module(name, rel):
    if name not in sys.modules:
        sp = importlib.util.spec_from_file_location(name, tree() / rel); m = importlib.util.module_from_spec(sp)
        sys.modules[name] = m
        with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(m)
    return sys.modules[name]


def C41():
    """B1741's compare.py, unchanged (its sigmas)"""
    return _module("b1741_compare_plain", V41 + "compare.py")


def lines266():
    L = _module("b1726_census", "frontier/B1726_the_two_ingredients_replicated/verification/census.py").lines()
    assert len(L) == NLINES
    return [(str(a), str(b)) for a, b in L]


# ------------------------------------------------------------------------------------------------ the population
def load():
    """the 118 636 rows: logs v (n, 6, 2), exponents e (n, 6, 2), residuals, Im tau, line, horocycle, sheet and apex;
    B1798's dedup; rows ordered (line, Re tau, Im tau) then horocycle"""
    if "v" in _G: return
    t = tree(); rows, seen, dup = [], {}, 0
    for rel in (V53 + "census.jsonl", V98 + "b1753_all266/census_ext.jsonl", V98 + "b1753_all266/census_ext_tail.jsonl"):
        for l in (t / rel).read_text(encoding="utf-8").splitlines():
            if not l.strip(): continue
            r = json.loads(l); key = (r["line"], r["Re_tau"], r["Im_tau"])
            if key in seen:
                q = seen[key]; dup += 1
                assert all(q[k] == r[k] for k in r if k.startswith(("up|", "down|", "lep|", "ckm|"))), key
                continue
            seen[key] = r; rows.append(r)
    rows.sort(key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
    L = lines266()
    ex = {(d["alpha"], d["b"]): d for d in json.loads((t / EXJ).read_text())}
    apexes = {}
    for r in rows: apexes.setdefault(r["line"], []).append((r["Re_tau"], r["Im_tau"]))
    first = apexes[rows[0]["line"]]
    same_apexes = all(a == first for a in apexes.values()) and len(first) == NAPEX
    where = {xy: i for i, xy in enumerate(first)}
    lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    v, e, res, im, li, hi, sheet, apex, clamp = [], [], [], [], [], [], [], [], 0
    for r in rows:
        rec = ex[L[r["line"]]]; ai = where.get((r["Re_tau"], r["Im_tau"]), -1)
        for h_i, h in enumerate(HORS):
            vv = np.zeros((6, 2)); ee = np.zeros((6, 2)); rr = np.zeros((6, 2)); cl = 0
            for s_i, s in enumerate(SECS):
                for a_i, a in enumerate(RDS):
                    raw = r["%s|%s|%s" % (s, h, a)]; cl |= int(min(raw) <= 1e-300)
                    for g_i, g in enumerate(GENS):
                        k = 2 * s_i + g_i; x = rec["%s|%s|%s|%s" % (s, h, a, g)]
                        vv[k, a_i] = lg(raw[g_i]); ee[k, a_i] = x["exponent"]; rr[k, a_i] = x["resid"]
            clamp += cl
            v.append(vv); e.append(ee); res.append(rr); im.append(r["Im_tau"]); li.append(r["line"]); hi.append(h_i)
            sheet.append(2 * r["line"] + h_i); apex.append(ai)
    _G.update(v=np.array(v), e=np.array(e), res=np.array(res), im=np.array(im), line=np.array(li), hor=np.array(hi),
              sheet=np.array(sheet), apex=np.array(apex), npoints=len(rows), dups=dup, nlines=len(apexes),
              same_apexes=same_apexes, clamp=clamp, lines=L)
    _G["B"] = 2 * math.pi * _G["im"][:, None, None] * _G["e"]
    _G["P"] = _G["v"] + _G["B"]
    if same_apexes:                                  # idx[sheet, apex] -> row, for R2
        idx = np.full((2 * NLINES, NAPEX), -1, dtype=np.int64); idx[_G["sheet"], _G["apex"]] = np.arange(len(v))
        _G["idx"] = idx


def target():
    if "t" not in _G:
        s6, _ = C41().sigmas()
        d = json.loads((tree() / HZ).read_text())["masses_GeV"]["value"]
        t6 = np.log(np.array([d["c"] / d["t"], d["u"] / d["t"], d["s"] / d["b"], d["d"] / d["b"], d["mu"] / d["tau"], d["e"] / d["tau"]]))
        _G.update(t=t6, s=np.asarray(s6, dtype=float))
    return _G["t"], _G["s"]


def stat(v, t, s, cs=C_NINE):
    """the direct form: B1741's chi2_six minimised over the rows, the seat configurations and c in cs (c multiplies
    m_mu/m_tau and divides m_e/m_tau); v: (n, 6, 2).  Returns T."""
    best = math.inf
    for (a, b, l) in SEAT_CFG:
        x = np.stack([v[:, 0, a], v[:, 1, a], v[:, 2, b], v[:, 3, b], v[:, 4, l], v[:, 5, l]], 1)
        for c in cs:
            k = math.log(c); y = x.copy(); y[:, 4] += k; y[:, 5] -= k
            best = min(best, float((((y - t) / s) ** 2).sum(1).min()))
    return best


# The seat configurations read up only in S~, so the fast path needs ten columns: (up2, S~), (up1, S~) and the down and
# lepton ratios in both readings.  COLS lists them as (ratio k, reading a).
COLS = [(0, 1), (1, 1), (2, 0), (3, 0), (2, 1), (3, 1), (4, 0), (5, 0), (4, 1), (5, 1)]


def prep_fast(P, B, t, s):
    """the columns scaled by sigma: d = Pn[src] - Bn is (v' - t) / sigma for the column"""
    Pn = [np.ascontiguousarray(P[:, k, a] / s[k]) for k, a in COLS]
    Bn = [np.ascontiguousarray((B[:, k, a] + t[k]) / s[k]) for k, a in COLS]
    return dict(Pn=Pn, Bn=Bn, s=s, inv=[1.0 / s[k] for k, a in COLS])


def _sources(kind, rng, n, F, ident):
    """per ratio k, the source row of its prefactor (None: the row itself); for N2 the drawn prefactors instead"""
    if ident: return {k: None for k in range(6)}, None
    if kind == "N2":
        return None, {k: rng.standard_normal(n) for k in range(6)}      # one P per (row, ratio), both readings
    if kind == "R2":
        idx = F["idx"]; ns = idx.shape[0]; out = {}
        for k in range(6):
            sig = rng.permutation(ns); out[k] = idx[sig[F["sheet"]], F["apex"]]
        return out, None
    groups = [(0,), (1,), (2,), (3,), (4,), (5,)] if kind == "N1" else [(0,), (1,), (2, 4), (3, 5)]
    out = {}
    for g in groups:
        pi = rng.permutation(n)
        for k in g: out[k] = pi
    return out, None


def fast(kind, rng, F, cs=C_NINE, ident=False):
    """T of one null draw (or of the frame itself with ident=True); returns (T, row, configuration, c index)"""
    Pn, Bn, inv, s = F["Pn"], F["Bn"], F["inv"], F["s"]; n = Pn[0].shape[0]
    src, z = _sources(kind, rng, n, F, ident)
    if z is not None:
        d = [z[k] * inv[i] - Bn[i] for i, (k, a) in enumerate(COLS)]
    else:
        d = [(Pn[i] if src[k] is None else Pn[i][src[k]]) - Bn[i] for i, (k, a) in enumerate(COLS)]
    up = d[0] * d[0] + d[1] * d[1]
    dn = (d[2] * d[2] + d[3] * d[3], d[4] * d[4] + d[5] * d[5])
    best = (math.inf, -1, -1, -1)
    for mi, (dl, l4, l5) in enumerate(((dn[0], d[6], d[7]), (dn[1], d[8], d[9]))):
        base = up + dl
        for ci, c in enumerate(cs):
            k = math.log(c)
            chi = base + (l4 + k / s[4]) ** 2 + (l5 - k / s[5]) ** 2
            j = int(np.argmin(chi))
            if chi[j] < best[0]: best = (float(chi[j]), j, mi, ci)
    return best


def fast_data():
    if "F" not in _G:
        load(); t, s = target(); F = prep_fast(_G["P"], _G["B"], t, s)
        F.update(sheet=_G["sheet"], apex=_G["apex"], idx=_G.get("idx")); _G["F"] = F
    return _G["F"]


def chunk_job(job):
    kind, j = job
    p = CH / ("%s_%03d.npz" % (kind, j))
    if p.exists(): return job
    F = fast_data()
    rng = np.random.Generator(np.random.PCG64(np.random.SeedSequence(412000 + j)))
    T = np.empty(CHUNK); arg = np.zeros((CHUNK, 3), dtype=np.int64)
    for i in range(CHUNK):
        T[i], *a = fast(kind, rng, F); arg[i] = a
    tmp = p.with_suffix(".tmp.npz"); np.savez(tmp, T=T, arg=arg, seed=412000 + j); os.replace(tmp, p)
    return job


# ------------------------------------------------------------------------------------------------ C0, the cells
def c0():
    load(); t, s = target(); out = {}
    out["a_loader"] = dict(points=_G["npoints"], duplicates=_G["dups"], lines=_G["nlines"], rows=int(_G["v"].shape[0]),
                           same_223_apexes=bool(_G["same_apexes"]),
                           ok=(_G["npoints"] == POINTS and _G["dups"] == DUPS and _G["nlines"] == NLINES
                               and _G["v"].shape[0] == 2 * POINTS and bool(_G["same_apexes"])))
    own = stat(_G["v"], t, s, C_SEAT)
    F98 = _module("b1798_feat_null", V98 + "feat_null.py"); C = F98.C_for("b1753_all")
    with contextlib.redirect_stdout(io.StringIO()): C._load()
    ref = float(C.min_chi2(C.chi2_features("seat", False), C._A["T6"][None, :])[0])
    out["b_measure"] = dict(own_seat=own, b1741_min_chi2=ref, ok=abs(own - T_SEAT) < 1e-9 and abs(ref - T_SEAT) < 1e-9)
    ident = _G["P"] - _G["B"]; rt = float(np.max(np.abs(ident - _G["v"])))
    F = fast_data()
    f_seat = fast("N1", None, F, C_SEAT, ident=True)[0]; f_nine = fast("N1", None, F, C_NINE, ident=True)[0]
    d_nine = stat(_G["v"], t, s, C_NINE)
    out["c_round_trip"] = dict(max_dev=rt, fast_seat=f_seat, fast_nine=f_nine, direct_nine=d_nine,
                               ok=rt < 1e-12 and abs(f_seat - own) < 1e-9 and abs(f_nine - d_nine) < 1e-9)
    used = np.zeros((6, 2), dtype=bool)
    for k, a in COLS: used[k, a] = True
    e_used = _G["e"][:, used]; r_used = _G["res"][:, used]
    out["d_exponents"] = dict(lines_in_json=len(set(_G["lines"])), finite=bool(np.isfinite(_G["e"]).all()),
                              rows_with_a_used_residual_above_0_07=int((r_used > 0.07).any(1).sum()),
                              used_entries_with_residual_above_0_07=int((r_used > 0.07).sum()),
                              used_entries_below_0=int((e_used < 0).sum()), used_entries=int(e_used.size),
                              ok=bool(np.isfinite(_G["e"]).all()) and len(set(_G["lines"])) == NLINES)
    out["ok"] = all(out[k]["ok"] for k in ("a_loader", "b_measure", "c_round_trip", "d_exponents"))
    _G["T_data"] = d_nine
    return out


def r975(h, n):
    from scipy.stats import beta
    return float(beta.ppf(0.975, h + 1, n - h)) if h < n else 1.0


def lo95(h, n):
    from scipy.stats import beta
    return float(beta.ppf(0.025, h, n - h + 1)) if h > 0 else 0.0


def cells(C0):
    load(); T_data = _G["T_data"]
    out = {"C0": C0, "T_data_M9": T_data, "T_data_seat": C0["b_measure"]["own_seat"], "m_grade": M_GRADE}
    seeds = []
    for kind, js in JOBS.items():
        z = [np.load(CH / ("%s_%03d.npz" % (kind, j))) for j in js]
        T = np.concatenate([x["T"] for x in z]); arg = np.concatenate([x["arg"] for x in z]); seeds += [int(x["seed"]) for x in z]
        n = len(T); hit = T <= T_data + TIE; h = int(hit.sum()); r = r975(h, n)
        d = dict(draws=n, hits=h, rate=h / n, r975=r, lo95=lo95(h, n), m_r={str(m): m * r for m in M_READ},
                 quantiles={q: float(np.quantile(T, float(q))) for q in ("0", "0.001", "0.01", "0.1", "0.5")})
        d["first_hits"] = [dict(T=float(T[i]), slope=_G["lines"][int(_G["line"][arg[i, 0]])][0],
                                im_tau=float(_G["im"][arg[i, 0]]), horocycle=HORS[int(_G["hor"][arg[i, 0]])],
                                configuration=["(S~,S,S)", "(S~,S~,S~)"][int(arg[i, 1])], c=C_NINE[int(arg[i, 2])])
                           for i in np.flatnonzero(hit)[:200]]
        if kind in ("N1", "N2"):
            d["grade"] = "SPECIFIC" if M_GRADE * r < 0.01 else ("CAPACITY" if lo95(h, n) >= 0.01 else "INTERMEDIATE")
        out[kind] = d
    out["e_completeness"] = dict(seeds_distinct=len(seeds) == len(set(seeds)),
                                 ok=len(seeds) == len(set(seeds)) and all(out[k]["draws"] == DRAWS[k] for k in DRAWS))
    used = np.zeros((6, 2), dtype=bool)
    for k, a in COLS: used[k, a] = True
    good = ~(_G["res"][:, used] > 0.07).any(1); P = _G["P"]
    out["R4"] = {"%s|%s|%s" % (NAMES[k], RDS[a], lab): [float(np.quantile(P[m, k, a], q)) for q in (0.1, 0.5, 0.9)]
                 for k in range(6) for a in range(2) for lab, m in (("fit_good", good), ("fit_poor", ~good)) if m.any()}
    out["R4_rows_fit_good"] = int(good.sum()); out["R4_rows_with_a_clamped_ratio"] = int(_G["clamp"])
    return out


# ------------------------------------------------------------------------------------------------ synthetic checks
def synthetic():
    """no row of the population: random arrays with the population's shape and a sheet structure"""
    rng = np.random.default_rng(7); nl, na = 20, 15; n = 2 * nl * na
    v = rng.normal(-4, 2, (n, 6, 2)); e = rng.uniform(0.1, 1, (n, 6, 2)); im = rng.uniform(2, 3.6, n)
    sheet = np.repeat(np.arange(2 * nl), na); apex = np.tile(np.arange(na), 2 * nl)
    idx = np.full((2 * nl, na), -1); idx[sheet, apex] = np.arange(n)
    B = 2 * math.pi * im[:, None, None] * e; P = v + B
    t = np.array([-5.6, -11.8, -4.0, -7.0, -2.8, -8.2]); s = np.array([0.13, 0.25, 0.14, 0.12, 0.10, 0.10])
    assert np.max(np.abs((P - B) - v)) < 1e-12
    F = prep_fast(P, B, t, s); F.update(sheet=sheet, apex=apex, idx=idx)
    for cs in (C_SEAT, C_NINE):
        assert abs(fast("N1", None, F, cs, ident=True)[0] - stat(v, t, s, cs)) < 1e-9
    for kind in ("N1", "N2", "R1", "R2"):                        # the fast path on a draw against the direct sum
        T1 = fast(kind, np.random.Generator(np.random.PCG64(np.random.SeedSequence(5))), F)[0]
        g2 = np.random.Generator(np.random.PCG64(np.random.SeedSequence(5)))
        src, z = _sources(kind, g2, n, F, False)
        if z is not None:
            w = np.stack([z[k] for k in range(6)], 1)[:, :, None] - B
        else:
            w = np.stack([P[src[k], k, :] for k in range(6)], 1) - B
        assert abs(T1 - stat(w, t, s)) < 1e-9, kind
        if kind in ("N1", "R2"):                                   # each ratio's marginal kept
            for k in range(6): assert np.allclose(np.sort((w + B)[:, k, 0]), np.sort(P[:, k, 0]))
        if kind == "R2":                                           # whole sheets: each row keeps its apex
            for k in range(6): assert np.array_equal(apex[src[k]], apex)
        if kind == "R1":
            assert np.array_equal(src[2], src[4]) and np.array_equal(src[3], src[5])
    big = 2 * NLINES * NAPEX; Pb = rng.normal(0, 2, (big, 6, 2)); Bb = rng.uniform(5, 15, (big, 6, 2))
    sb = np.repeat(np.arange(2 * NLINES), NAPEX); ab = np.tile(np.arange(NAPEX), 2 * NLINES)
    ib = np.full((2 * NLINES, NAPEX), -1); ib[sb, ab] = np.arange(big)
    Fb = prep_fast(Pb, Bb, t, s); Fb.update(sheet=sb, apex=ab, idx=ib); g = np.random.default_rng(3)
    for kind in ("N1", "N2", "R1", "R2"):
        t0 = time.time()
        for _ in range(30): fast(kind, g, Fb)
        print("synthetic %s: %.1f ms per draw at %d rows" % (kind, 1000 * (time.time() - t0) / 30, big))
    print("synthetic checks: pass")


def main():
    if "--synthetic" in sys.argv: return synthetic()
    if "--run" not in sys.argv: raise SystemExit(__doc__)
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
    tmax = float(sys.argv[sys.argv.index("--max-seconds") + 1]) if "--max-seconds" in sys.argv else 6600.0
    CH.mkdir(exist_ok=True); t0 = time.time()
    C0 = c0()
    if not C0["ok"]:
        print(json.dumps({"C0": C0}, indent=1)); print("STOP: C0 failed; no cell computed"); return
    print("C0 (a)-(d) hold", flush=True)
    jobs = [(k, j) for k, js in JOBS.items() for j in js]
    todo = [jb for jb in jobs if not (CH / ("%s_%03d.npz" % jb)).exists()]
    print("chunks to do: %d of %d" % (len(todo), len(jobs)), flush=True)
    if todo:
        from multiprocessing import Pool
        with Pool(nw) as pool:
            done = 0
            for _ in pool.imap_unordered(chunk_job, todo):
                done += 1; print("chunk %d of %d done (%.0f s)" % (done, len(todo), time.time() - t0), flush=True)
                if time.time() - t0 > tmax:
                    pool.terminate(); print("stopped by the time limit; rerun to resume"); return
    out = cells(C0)
    OUT_CELLS.write_text(json.dumps(out, indent=1))
    print("T_data on M9 %.9f; on the seat menu %.9f" % (out["T_data_M9"], out["T_data_seat"]))
    for k in ("N1", "N2", "R1", "R2"):
        d = out[k]
        print("%s: hits %d of %d, r975 %.3e, lo95 %.3e, m*r %s%s" % (k, d["hits"], d["draws"], d["r975"], d["lo95"],
              {m: round(x, 5) for m, x in d["m_r"].items()}, ("  GRADE " + d["grade"]) if "grade" in d else ""))
    print("completeness:", out["e_completeness"]["ok"])


if __name__ == "__main__":
    main()
