#!/usr/bin/env python3
"""SM-R612 (P-612, main's page M53): COUNT THE IMAGE, NOT THE ROWS.  Is the frozen map of frame A to the six and D
constant under each of its choices -- the lepton factor c, the 2/5 line class (slope and offset), the end norm, tau and
the Higgs direction -- and how large is each choice's image?  Card: relays/cards/SM_R612_count-the-image.md, written and
pushed with this script before it is run on the test population below.

Data-free.  The frame's outputs are compared only with themselves: logs of singular-value ratios, never a measured
value.  The frame is main's frozen-row instrument, used unchanged: B1842's exact_card_instrument (B1726's compute()
construction, B1838's exact twisted norms over B1667's cell, B1691's Higgs sections), with the frame-A reading
(S~, S, S) at a0 = 0.
Only the menu of each choice is supplied here (the Higgs section index and the end level), from main's own formulas:
the ends E1-E4 of B1840's closed list and the small-cut norm 2 pi L + c_s of B1726; the Higgs menu R, DR, D^2R of B1691.

Outputs per evaluation (natural logs): up, down, lepton (ln m1/m2, ln m2/m3) -- the six -- and ln D, with
D = c^2 R2 R1, R2 = (m2/m3)_e/(m2/m3)_d, R1 = (m1/m3)_d/(m1/m3)_e (B1789 sec. 1); c multiplies the lepton m2/m3 by c
and divides its m1/m3 by c (B1789 sec. 1).

    python3 -B run.py MAIN_CHECKOUT            # the sealed run: prints the tables, writes r612_results.json
    python3 -B run.py MAIN_CHECKOUT --smoke    # import and smoke test on points outside the test population;
                                               # prints no result"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, time, pathlib, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
CONST_TOL, NONCONST_TOL, IMG_TOL = 1e-8, 1e-5, 1e-5     # constancy and clustering thresholds on |delta ln|
RANK_TOL = 1e-4                                         # a Jacobian singular value above this counts (d ln / d param)
READ = {"up": "St", "down": "S", "lep": "S"}             # frame A's reading (S~, S, S), A05
SECS = ("up", "down", "lep")
NAMES = ["ln u12", "ln u23", "ln d12", "ln d23", "ln e12", "ln e23", "ln D"]
QUARK, LEPTON, DIDX = [0, 1, 2, 3], [4, 5], [6]
ENDS = ("E1", "E2", "E3", "E4", "inf", "SC_Lmax", "SC_L2")
HIGGS_MENU = {"R": 0, "DR": 1, "D2R": 2}
C_BASE, C_MENU = 3.0, (1.0, 2.0, 3.0, 4.0, 5.0)
BASE_LINE = (F(2, 5), F(4, 5))                           # A03 at B1841's row, order 5
# the test population, fixed on the card before any run
TAUS = (complex(0.21, 2.97), complex(-0.33, 3.08), complex(0.44, 3.02))
TAU_MIRROR = complex(0.0, 3.0)
# smoke inputs, outside the test population
SMOKE_TAU, SMOKE_LINE = complex(0.1, 2.6), (F(1, 3), F(1, 7))

_S = {}


def load(main):
    if not _S:
        p = pathlib.Path(main).resolve() / "frontier" / "B1842_the_closure_instruments" / "verification"
        sp = importlib.util.spec_from_file_location("r612_x", p / "exact_card_instrument.py")
        X = importlib.util.module_from_spec(sp); sp.loader.exec_module(X)
        M = X.mods()
        _S.update(X=X, ee=M["ee"], B=M["B"], te=M["ee"].te, geo={})
    return _S


def geo(tau):
    S = _S; key = (round(tau.real, 12), round(tau.imag, 12))
    if key not in S["geo"]:
        c, res = S["X"].accessory(tau); S["geo"][key] = (S["ee"].geometry(tau, c), res)
    return S["geo"][key][0]


def higgs_vec(tau, k):
    return np.array([complex(_S["te"].ev(cc, mp.mpc(tau.real, tau.imag))) for cc in _S["te"].B[k]])


def readings(av):
    B = _S["B"]; Sm = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    return {"S": Sm, "St": B.EPS @ np.conj(Sm) @ B.EPS.T}


def level(end, G, dd=0.0):
    return {"E1": G["L_2"], "E2": math.log(2.0), "E3": G["L_max"], "E4": G["L_2"] - math.pi / 2}[end] + dd


def frame(tau, a, b, end="E4", dd=0.0, higgs="DR", dh=None, c=C_BASE, plant_eps=0.0, unreduced=False, raw=False):
    """frame A's outputs at (tau, line (a, b)); end in ENDS (dd shifts an exact level); higgs a menu name, plus dh (a
    complex 3-vector in units of |DR(tau)|) added; c the lepton factor; plant_eps rescales one down channel weight."""
    S = _S; X, ee, B = S["X"], S["ee"], S["B"]
    if unreduced:
        assert end == "inf"; a, b = F(a), F(b); G = None
    else:
        tau, a, b = X.reduce(tau, a, b); G = geo(tau)
    av = higgs_vec(tau, HIGGS_MENU[higgs])
    if dh is not None:
        av = av + np.asarray(dh, dtype=complex) * np.linalg.norm(higgs_vec(tau, 1))
    rd = readings(av); w = float(a) * tau + float(b); sv = {}; Ys = {}
    for sec in SECS:
        ql, qr = X.CHARGES[sec]
        x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau)
        if end == "inf":
            N = {s: (1.0 if abs(R[s]) > 1e-12 else 0.0) for s in B.UNITS}
        elif end in ("SC_Lmax", "SC_L2"):
            cs = B.cA(x, yy, tau, R); L = G["L_max"] if end == "SC_Lmax" else G["L_2"]
            N = {s: (2 * math.pi * L + cs[s] if cs[s] is not None and 2 * math.pi * L + cs[s] > 0 else 0.0)
                 for s in B.UNITS}
        else:
            N, _ = ee.twisted_norms(tau, G["al"], G["be"], level(end, G, dd), x, yy, R, nth=X.NTH, ns=X.NS)
        u = {s: (math.sqrt(N[s]) * R[s] if N.get(s) is not None and N[s] > 0 else 0) for s in B.UNITS}
        if plant_eps and sec == "down":
            s0 = max(B.UNITS, key=lambda s: abs(u[s]) if u[s] != 0 else -1.0); u[s0] = u[s0] * (1 + plant_eps)
        Y = B.coupling(rd[READ[sec]], B.weighted_M(u)); Ys[sec] = Y
        sv[sec] = np.linalg.svd(Y, compute_uv=False)
    if raw:
        return Ys
    lg = lambda v: math.log(v) if v > 0 else -1e3          # an exact zero is a sentinel, flagged by its size
    out = []
    for sec in SECS:
        s3, s2, s1 = sv[sec]
        r12, r23 = (s1 / s2 if s2 > 0 else 0.0), s2 / s3
        if sec == "lep":
            out += [lg(r12) - 2 * math.log(c), lg(r23) + math.log(c)]
        else:
            out += [lg(r12), lg(r23)]
    d23, d13 = sv["down"][1] / sv["down"][0], sv["down"][2] / sv["down"][0]
    e23, e13 = sv["lep"][1] / sv["lep"][0], sv["lep"][2] / sv["lep"][0]
    lD = (2 * math.log(c) + lg(e23) - lg(d23) + lg(d13) - lg(e13)) if min(d23, d13, e23, e13) > 0 else -1e3
    return np.array(out + [lD])


def spread(vs, idx):
    A = np.array(vs)[:, idx]; return float(np.max(A.max(axis=0) - A.min(axis=0)))


def verdict(s):
    return "CONSTANT" if s < CONST_TOL else ("NON-CONSTANT" if s > NONCONST_TOL else "UNRESOLVED")


def image_count(vs, idx):
    reps = []
    for v in vs:
        v = np.asarray(v)[idx]
        if not any(float(np.max(np.abs(v - r))) < IMG_TOL for r in reps):
            reps.append(v)
    return len(reps)


def block_report(vs):
    return {blk: {"spread": spread(vs, idx), "verdict": verdict(spread(vs, idx)), "images": image_count(vs, idx)}
            for blk, idx in (("six", list(range(6))), ("quark four", QUARK), ("lepton two", LEPTON), ("D", DIDX),
                             ("six and D", list(range(7))))}


def jacobian(f, p0, hs):
    cols = []
    for i, h in enumerate(hs):
        e = np.zeros(len(p0)); e[i] = h
        cols.append((f(p0 + e) - f(p0 - e)) / (2 * h))
    return np.array(cols).T


def rank_of(J):
    s = np.linalg.svd(J, compute_uv=False); return int(np.sum(s > RANK_TOL)), [float(x) for x in s]


def jac_both(f, p0, hs):
    """the rank at steps h and h/2; agreement is required, else the rank is UNRESOLVED"""
    J1 = jacobian(f, p0, hs); J2 = jacobian(f, p0, [h / 2 for h in hs])
    r1, s1 = rank_of(J1); r2, s2 = rank_of(J2)
    return {"rank": r1 if r1 == r2 else "UNRESOLVED", "rank_h": r1, "rank_h2": r2, "sv_h": s1, "sv_h2": s2,
            "max_abs_row_h2": [float(np.max(np.abs(J2[i]))) for i in range(J2.shape[0])]}


# ---- the tests -------------------------------------------------------------------------------------------------------
def test_c(tau):
    vs = [frame(tau, *BASE_LINE, c=c) for c in C_MENU]
    lD = [v[6] for v in vs]; lD1 = lD[0]
    pl1 = max(abs((x - lD1) - 2 * math.log(c)) for x, c in zip(lD, C_MENU))
    return {"blocks": block_report(vs), "PL1_D_scales_as_c2_dev": pl1}


def test_class(tau):
    a = BASE_LINE[0]
    offs = [F(k, 10) for k in range(10)]
    vs = {str(b): frame(tau, a, b) for b in offs}
    o5 = [vs[str(b)] for b in offs if b.denominator <= 5]; o10 = [vs[str(b)] for b in offs if b.denominator == 10]
    rep = {"offsets_blocks": block_report(list(vs.values())),
           "D_minus_2lnc_on_order5_offsets": [float(v[6] - 2 * math.log(C_BASE)) for v in o5],
           "D_minus_2lnc_on_order10_offsets": [float(v[6] - 2 * math.log(C_BASE)) for v in o10]}
    lat = {}
    for j in range(10):
        for k in range(10):
            if (j, k) != (0, 0):
                lat[(j, k)] = frame(tau, F(j, 10), F(k, 10))
    vals = list(lat.values())
    sign_dev = max(float(np.max(np.abs(lat[(j, k)] - lat[((-j) % 10, (-k) % 10)]))) for (j, k) in lat)
    dlines = sorted("%d/10,%d/10" % jk for jk, v in lat.items() if abs(v[6] - 2 * math.log(C_BASE)) < CONST_TOL)
    dundef = sorted("%d/10,%d/10" % jk for jk, v in lat.items() if v[6] < -500)
    slopes = {}
    for (j, k), v in lat.items():
        slopes.setdefault(j, []).append(v)
    rep.update({"lattice_blocks": block_report(vals), "lattice_lines": len(vals), "sign_pair_max_dev": sign_dev,
                "lines_with_D_equal_c2": dlines, "n_lines_with_D_equal_c2": len(dlines),
                "lines_with_D_undefined": dundef,
                "per_slope_images_six": {"%d/10" % j: image_count(v, list(range(6)))
                                         for j, v in sorted(slopes.items())},
                "sentinel_zero_masses": int(sum(1 for v in vals if np.min(v) < -500))})
    return rep


def test_end(tau):
    vs = {e: frame(tau, *BASE_LINE, end=e) for e in ENDS}
    return {"blocks": block_report(list(vs.values())),
            "D_minus_2lnc_per_end": {e: float(v[6] - 2 * math.log(C_BASE)) for e, v in vs.items()}}


def test_higgs(tau):
    vs = {h: frame(tau, *BASE_LINE, higgs=h) for h in HIGGS_MENU}
    av = higgs_vec(tau, 1) / np.linalg.norm(higgs_vec(tau, 1))
    lam = 2.7 * np.exp(0.9j)
    pl3 = float(np.max(np.abs(frame(tau, *BASE_LINE, dh=(lam - 1) * av) - vs["DR"])))
    def f(p):
        return frame(tau, *BASE_LINE, dh=np.array([p[0] + 1j * p[1], p[2] + 1j * p[3], p[4] + 1j * p[5]]))
    jr = jac_both(f, np.zeros(6), [1e-3] * 6)
    # the two directions that must be null: along av (scale) and i av (phase)
    def g(t, ph):
        return frame(tau, *BASE_LINE, dh=(t + 1j * ph) * av)
    null = max(float(np.max(np.abs(g(1e-3, 0) - g(-1e-3, 0)))), float(np.max(np.abs(g(0, 1e-3) - g(0, -1e-3)))))
    return {"menu_blocks": block_report(list(vs.values())), "PL3_scale_phase_dev": pl3, "null_dir_fd_dev": null,
            "local": jr, "D_minus_2lnc_per_menu": {h: float(v[6] - 2 * math.log(C_BASE)) for h, v in vs.items()}}


def test_tau(tau):
    def f(p):
        return frame(complex(p[0], p[1]), *BASE_LINE)
    def finf(p):
        return frame(complex(p[0], p[1]), *BASE_LINE, end="inf")
    p0 = np.array([tau.real, tau.imag])
    return {"E4": jac_both(f, p0, [1e-3, 1e-3]), "inf": jac_both(finf, p0, [1e-3, 1e-3])}


def test_joint(tau):
    """all continuous choices together: Re tau, Im tau, the end level (about E4), the Higgs (6 real), ln c"""
    def f(p):
        dh = np.array([p[3] + 1j * p[4], p[5] + 1j * p[6], p[7] + 1j * p[8]])
        return frame(complex(p[0], p[1]), *BASE_LINE, dd=p[2], dh=dh, c=C_BASE * math.exp(p[9]))
    p0 = np.zeros(10); p0[0], p0[1] = tau.real, tau.imag
    return jac_both(f, p0, [1e-3] * 10)


def plants(tau):
    base = frame(tau, *BASE_LINE)
    pl2 = float(np.max(np.abs(frame(tau, *BASE_LINE, plant_eps=1e-4) - base)))
    qc = spread([frame(tau, *BASE_LINE, c=c) for c in C_MENU], QUARK)
    # T-law at the cusp limit: theta machinery at the unreduced tau + 1, line (a, b - a)
    a, b = BASE_LINE
    t1 = frame(tau, a, b, end="inf"); t2 = frame(tau + 1, a, (b - a) % 1, end="inf", unreduced=True)
    return {"PL2_channel_plant_dev": pl2, "PL2_verdict": verdict(pl2), "PL6_c_on_quark_four_spread": qc,
            "PL5_T_law_dev": float(np.max(np.abs(t1 - t2)))}


def mirror_plant():
    """T-FRAME-MIRROR at Re tau = 0: (a, b) and (a, -b) at tau = i y must give the same outputs (exact end E4)"""
    dev = 0.0
    for k in range(10):
        b = F(k, 10)
        d = frame(TAU_MIRROR, BASE_LINE[0], b) - frame(TAU_MIRROR, BASE_LINE[0], (-b) % 1)
        dev = max(dev, float(np.max(np.abs(d))))
    return dev


def c_id(tau, a, b):
    """the instrument identity: frame()'s down/lepton/up matrices at DR, E-level L_max + 0.1, equal B1842's"""
    X = _S["X"]; G = geo(X.reduce(tau, a, b)[0])
    Y, _ = X.yukawas_exact(tau.real, tau.imag, a, b, 0.1, SECS)
    Z = frame(tau, a, b, end="E3", dd=0.1, raw=True)
    return max(float(np.max(np.abs(Y[s][READ[s]] - Z[s])) / np.max(np.abs(Y[s][READ[s]]))) for s in SECS)


def smoke(main):
    t0 = time.time(); load(main)
    a, b = SMOKE_LINE
    assert c_id(SMOKE_TAU, a, b) < 1e-12
    for e in ENDS:
        assert np.all(np.isfinite(frame(SMOKE_TAU, a, b, end=e)))
    for h in HIGGS_MENU:
        assert np.all(np.isfinite(frame(SMOKE_TAU, a, b, higgs=h)))
    assert np.all(np.isfinite(frame(SMOKE_TAU + 1, a, (b - a) % 1, end="inf", unreduced=True)))
    _ = frame(SMOKE_TAU, a, b, plant_eps=1e-4, c=2.0, dd=0.01, dh=np.array([1e-3, 0, 1e-3j]))
    _n = image_count([_, _], list(range(7))); _v = verdict(spread([_, _], list(range(7))))
    _ = jacobian(lambda p: frame(SMOKE_TAU, a, b, c=C_BASE * math.exp(p[0])), np.zeros(1), [1e-3])
    print("smoke ok: every routine ran on points outside the test population (%.0f s); no result printed"
          % (time.time() - t0))


def main(main_dir):
    t0 = time.time(); load(main_dir)
    res = {"taus": [[t.real, t.imag] for t in TAUS], "base_line": [str(x) for x in BASE_LINE]}
    res["C_ID"] = c_id(TAUS[0], *BASE_LINE); print("C-ID (instrument identity): %.1e" % res["C_ID"], flush=True)
    res["PL4_mirror_dev"] = mirror_plant(); print("PL4 mirror at Re tau = 0: %.1e" % res["PL4_mirror_dev"], flush=True)
    for t in TAUS:
        key = "%.2f%+.2fi" % (t.real, t.imag); r = res.setdefault(key, {})
        for name, fn in (("plants", plants), ("c", test_c), ("end", test_end), ("higgs", test_higgs),
                         ("class", test_class), ("tau", test_tau), ("joint", test_joint)):
            r[name] = fn(t); print("[%5.0f s] %s %s done" % (time.time() - t0, key, name), flush=True)
    json.dump(res, open(HERE / "r612_results.json", "w"), indent=1, default=str)
    report(res)


def report(res):
    print("\n== plants and controls ==")
    print("C-ID %.1e | PL4 mirror %.1e" % (res["C_ID"], res["PL4_mirror_dev"]))
    keys = [k for k in res if k[0] in "-0123456789"]
    for k in keys:
        p = res[k]["plants"]
        print("%s PL1 D~c^2 dev %.1e | PL2 channel plant %.1e (%s) | PL3 Higgs scale/phase %.1e | PL5 T-law %.1e | "
              "PL6 c on quark four %.1e" % (k, res[k]["c"]["PL1_D_scales_as_c2_dev"], p["PL2_channel_plant_dev"],
                                            p["PL2_verdict"], res[k]["higgs"]["PL3_scale_phase_dev"],
                                            p["PL5_T_law_dev"], p["PL6_c_on_quark_four_spread"]))
    print("\n== discrete images (verdict, images) per block: six | quark four | lepton two | D ==")
    for k in keys:
        r = res[k]
        for lab, br in (("c in {1..5}", r["c"]["blocks"]), ("2/5 offsets (10)", r["class"]["offsets_blocks"]),
                        ("all 1/10 lines (99)", r["class"]["lattice_blocks"]), ("ends (7)", r["end"]["blocks"]),
                        ("Higgs R, DR, D2R", r["higgs"]["menu_blocks"])):
            print("%s %-20s" % (k, lab) + " | ".join("%s %s %d" % (b, br[b]["verdict"], br[b]["images"])
                                                    for b in ("six", "quark four", "lepton two", "D")))
        c = r["class"]
        print("%s sign pairs max dev %.1e | lines with D = c^2: %d | D undefined (a zero mass): %d | "
              "per-slope six images %s" % (k, c["sign_pair_max_dev"], c["n_lines_with_D_equal_c2"],
                                           len(c["lines_with_D_undefined"]), c["per_slope_images_six"]))
    print("\n== continuous images: Jacobian rank (h, h/2), max |d ln D| ==")
    for k in keys:
        r = res[k]
        for lab, j in (("tau at E4", r["tau"]["E4"]), ("tau at inf", r["tau"]["inf"]),
                       ("Higgs CP2 (6 real)", r["higgs"]["local"]), ("joint (10)", r["joint"])):
            print("%s %-20s rank %s (%d, %d); max|dlnD| %.1e; sv %s" % (k, lab, j["rank"], j["rank_h"], j["rank_h2"],
                  j["max_abs_row_h2"][6], " ".join("%.1e" % s for s in j["sv_h2"])))
    print("\n== beside P-418: rows counted against the image ==")
    rows = (("tau", "A01", 1), ("the 2/5 class", "A02, A03", 2), ("the Higgs direction", "A04", 1),
            ("the end norm", "A07, A09", 2), ("the lepton factor c", "A10", 1))
    k = keys[0]; r = res[k]
    img = {"tau": "dim %s" % r["tau"]["E4"]["rank"], "the 2/5 class": "%d offsets -> %d; 99 lines -> %d" % (
        10, r["class"]["offsets_blocks"]["six and D"]["images"], r["class"]["lattice_blocks"]["six and D"]["images"]),
           "the Higgs direction": "menu 3 -> %d; CP2 dim %s" % (r["higgs"]["menu_blocks"]["six and D"]["images"],
                                                                 r["higgs"]["local"]["rank"]),
           "the end norm": "menu 7 -> %d" % r["end"]["blocks"]["six and D"]["images"],
           "the lepton factor c": "menu 5 -> %d" % r["c"]["blocks"]["six and D"]["images"]}
    for name, code, n in rows:
        print("%-22s %-9s P-418 rows %d | image in (six, D) at %s: %s" % (name, code, n, k, img[name]))
    print("joint continuous image dim (all keys): %s" % [res[k]["joint"]["rank"] for k in keys])


if __name__ == "__main__":
    if "--smoke" in sys.argv:
        smoke(sys.argv[1])
    else:
        main(sys.argv[1])
