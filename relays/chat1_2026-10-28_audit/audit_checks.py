"""chat1, 2026-10-28: THE AUDIT's checks. The numbers that this seat's relay THE EXACT END, THE SELECTOR AND THE AUDIT
cites from its integrity audit of the record's negatives, recomputed from committed files with the arcs' own code.

Post hoc and labelled. Five read-only auditors found these first (their scripts are not committed); this script
reproduces the numbers the relay uses, so it is not blind. It is committed before its one run. The parts are
independent: a part that fails prints its traceback and the rest run on.
  A  this seat's THE CLASS AND THE END (422cd8ecd): B1720's apexes counted up to T and up to the mirror, with the sign
     relation of J(v) and J(2v) per reading; the permutation's margins; B1786's best row under (S~, S).
  B  P-323 (this seat's census): (i) an exactly one-channel Higgs on (1/3, 1/12), (1/6, 5/12) and (2/5, 1/2); (ii) the
     40 slope-2/5 lines in both phase-free readings; (iii) the residue's sub-threshold r^2 scaling; (iv) stricter N
     criteria; (v) the lines whose norms pair.
  C  B1739 (main): |V_ud|'s per-Im-tau quantiles against r, per split reading; where the aligned rows sit; the joint test
     (the six among the rows with |V_ud| >= 0.97, the Standard Model's reading); B1726's least chi2_six per reading
     assignment with B1740's compare.py.
  D  B1740 (main): the F_-2 rows' m2/m3 floors.
  E  B1790 (main): on the mirror lines, a holomorphic section (DR with K negated, at tau or at tau - 1) against the S~
     reading, with B1790's referee module; and a control off the line.
  F  W172 (the SM seat's instruments, unchanged): the X-minimum with the bosons' weight 0 (matter only) at the rows'
     heights; the bosons' weight below which the minimum leaves the mirror point at Im tau 2.96 and 3.12; the rows' place
     in the X-well at full content; the distinct heights.
  G  W174 (the SM seat's committed census): the slope-2/5 patterns with the (4,5) exponents in place of (5,6).
  H  this seat's horocycle test: its search, unchanged, on three deep planted shifts.
Run:  python3 -B audit_checks.py <main's checkout at 52dc780da or later> <the SM seat's checkout at 0722f0ad5 or later>"""
import sys, io, json, math, time, contextlib, importlib.util, pathlib, traceback
from fractions import Fraction as Fr
import numpy as np
MAIN = pathlib.Path(sys.argv[1]).resolve(); SMC = pathlib.Path(sys.argv[2]).resolve()
HERE = pathlib.Path(__file__).resolve().parent; REPO = HERE.parents[1]
A25 = Fr(2, 5)


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


def clean(text):
    for p, tag in ((str(MAIN), "<main>"), (str(SMC), "<sm>"), (str(REPO), "<repo>")):
        text = text.replace(p, tag)
    return text


# ---------------------------------------------------------------------------------------------------------------- A
def partA():
    R = REPO / "relays" / "chat1_2026-10-28_riddles"
    e = json.loads((R / "explore_ckm_and_bit.json").read_text())

    def red(t, lines):
        re_, im_ = t; k = math.floor(re_ + 0.5 + 1e-9)
        return (round(re_ - k, 9), round(im_, 9)), tuple((Fr(a), (Fr(b) + k * Fr(a)) % 1) for a, b in lines)

    def mir(key):
        (re_, im_), ls = key
        return red((-re_, im_), [(a, (-b) % 1) for a, b in ls])
    allk, off = {}, {}
    for r in e["B"]:
        k = red(tuple(r["tau"]), r["lines"]); allk.setdefault(k, []).append(r)
        if not r["on_mirror_line"]: off.setdefault(k, []).append(r)
    on = {k for k, rs in allk.items() if rs[0]["on_mirror_line"]}
    classes = set()
    for k in off: classes.add(min(k, mir(k)) if mir(k) in off else k)
    print("A  B1720's %d apexes: %d T-distinct configurations, %d on the mirror lines and %d off them (%d up to the mirror)"
          % (len(e["B"]), len(allk), len(on), len(off), len(classes)))
    for key in sorted(next(iter(off.values()))[0]["v"].keys()):
        opp = sum(1 for rs in off.values() if rs[0]["v"][key] * rs[0]["2v"][key] < 0)
        same = sum(1 for rs in off.values() if rs[0]["v"][key] * rs[0]["2v"][key] > 0)
        print("   %-16s J(v) against J(2v): opposite %2d, same %2d, of %d" % (key, opp, same, len(off)))
    for pair in ("St|S", "S|St", "S|S", "St|St"):
        perms, mm, mo = {}, 1.0, 0.0
        for r in e["A"]:
            V = np.array(r["pairs"][pair]["absV"]); p = r["pairs"][pair]["best_perm"]; perms[tuple(p)] = perms.get(tuple(p), 0) + 1
            mm = min(mm, min(V[i, p[i]] for i in range(3))); mo = max(mo, max(V[i, j] for i in range(3) for j in range(3) if j != p[i]))
        print("A  reading (up %s, down %s), %d rows: best-matching permutations %s; smallest matched |V| %.3f; largest entry off it %.3f"
              % (pair.split("|")[0], pair.split("|")[1], len(e["A"]), perms, mm, mo))
    C = json.loads((R / "riddles_checks.json").read_text())["C"]["absV_rows_u_c_t_cols_d_s_b"]["St|S"]
    print("A  B1786's best row under (S~, S): |V_us| %.4f, |V_cb| %.4f, |V_td| %.4f" % (C[0][1], C[1][2], C[2][0]))


# ---------------------------------------------------------------------------------------------------------------- B
def partB():
    ARC = REPO / "relays" / "chat1_2026-10-28_p323"
    P = load("p323", ARC / "p323_strong_angle.py")
    B = load("b1656_audit", MAIN / "frontier" / "B1723_the_golden_valley" / "verification" / "b1656_funcs.py")
    d = np.load(ARC / "p323_census.npz"); idx = json.loads((ARC / "p323_census_index.json").read_text())
    R, C, L, H = d["R"], d["C"], d["L"], d["H"]; nl = R.shape[0]
    LINES = [(Fr(a), Fr(b)) for a, b in idx["lines"]]

    def ckm_J(Yu, Yd):
        Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
        return float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))

    def Dvals(th):
        dd = P.wrap(th[1:] - th[:1]); D1 = dd[:6].mean(0); D2 = dd[6:].mean(0)
        with np.errstate(divide="ignore", invalid="ignore"):
            return D1, D1 / D2
    E = np.eye(3, dtype=complex); cu, cd = P.READINGS[P.SM]
    for ln in [(Fr(1, 3), Fr(1, 12)), (Fr(1, 6), Fr(5, 12)), (Fr(2, 5), Fr(1, 2))]:
        li = LINES.index(ln); D1s, rs, Js, m2 = [], [], [], []
        for e in range(3):
            Hs = np.broadcast_to(E[e], (13, 1, 3)).copy()
            for ci in range(6):
                u, _ = P.weights(R[li, ci][None, None], C[li, ci][None, None], L[li, ci][None, None][..., 0])
                fs = P.factors(u, Hs[None, None], cu, cd); th = P.theta_of(fs, "Y")[0, 0]
                D1, r = Dvals(th); D1s.append(abs(float(D1[0]))); rs.append(float(r[0]))
                u0, _ = P.weights(R[li, ci, 0], C[li, ci, 0], L[li, ci, 0, 0])
                M = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s] for s in P.UNITS]))
                S = E[e][0] * B.QI + E[e][1] * B.QJ + E[e][2] * B.QK
                St = np.conj(E[e][0]) * B.QI + np.conj(E[e][1]) * B.QJ + np.conj(E[e][2]) * B.QK
                Yu, Yd = B.coupling(St, M[0]), B.coupling(S, M[1]); Js.append(abs(ckm_J(Yu, Yd)))
                sv = np.linalg.svd(Yu, compute_uv=False); m2.append(float(sv[1] / sv[0]))
        rr = [x for x, dd in zip(rs, D1s) if dd > 1e-11]
        print("B  (i) one-channel Higgs (e_0, e_1, e_2) on (%s, %s), the six centres, L_max, (S~, S): max |D(r1)| %.1e; ratio D(r1)/D(r2) "
              "%.1f-%.1f where |D(r1)| > 1e-11; |J| %.1e-%.1e; up m2/m3 %.2f-%.2f" % (ln[0], ln[1], max(D1s), min(rr), max(rr), min(Js), max(Js), min(m2), max(m2)))
    Q = P.all_quantities(R, C, L, H)
    QP = [P.all_quantities(*P.perturbed((R, C, L, H), p), keep=False) for p in range(P.NPERT)]
    sig = {k: np.max([np.abs(P.wrap(qp[k][0] - Q[k][0])) for qp in QP], axis=0) for k in Q if k[0] != "clamp"}
    clamp_ok = {hr: (Q[("clamp", hr)] == Q[("clamp", hr)][:, :, :1]).all(axis=(2, 3, 4)) for hr in range(2)}
    J = {}
    for hr in range(2):
        u0, _ = P.weights(R[:, :, 0], C[:, :, 0], L[:, :, 0, hr])
        M0 = np.einsum("...s,sab->...ab", u0, np.array([B.EDUAL[s] for s in P.UNITS]))
        for name in P.PHASE_FREE:
            cu_, cd_ = P.READINGS[name]; Ys = []
            for sec, cj in ((0, cu_), (1, cd_)):
                hv = np.conj(H[:, :, 0]) if cj else H[:, :, 0]
                S = hv[..., 0, None, None] * B.QI + hv[..., 1, None, None] * B.QJ + hv[..., 2, None, None] * B.QK
                Mx = M0[:, :, sec][:, :, None]; Y = np.zeros(S.shape[:-2] + (3, 3), complex)
                for a_, Ca in enumerate(B.BLOCKS):
                    for b_, Cb in enumerate(B.BLOCKS):
                        Y[..., a_, b_] = np.einsum("...ij,...ij->...", Ca.T @ B.EPS @ S @ Cb, np.broadcast_to(Mx, S.shape))
                Ys.append(Y)
            JJ = np.zeros((nl, 6, len(P.HIGGS)))
            for li in range(nl):
                for ci in range(6):
                    for hi in range(len(P.HIGGS)):
                        JJ[li, ci, hi] = ckm_J(Ys[0][li, ci, hi], Ys[1][li, ci, hi])
            J[(name, hr)] = JJ
    res, cnt = {}, {}
    for name in P.PHASE_FREE:
        for hr in range(2):
            th, fs = Q[("Y", name, hr)]
            valid, _ = P.validity(fs, "Y", True, clamp_ok[hr][..., None] * np.ones((1, 1, len(P.HIGGS)), bool))
            valid = valid & (np.abs(J[(name, hr)]) > 1e-9)
            D1, D2, sD, cls, ratio = P.classify(np.moveaxis(th, 2, -1), np.moveaxis(sig[("Y", name, hr)], 2, -1))
            vd = P.verdicts(np.moveaxis(valid, 1, -1), np.moveaxis(cls, 1, -1))
            res[(name, hr)] = (valid, D1, D2, sD, cls, ratio, vd)
            for v in np.unique(vd): cnt[v] = cnt.get(v, 0) + int((vd == v).sum())
    tot = sum(cnt.values()); withr = cnt.get("NOT HARMONIC", 0) + cnt.get("HARMONIC", 0) + cnt.get("UNDETERMINED", 0)
    print("B  H1's verdicts reproduced: %s; NOT HARMONIC %.1f%% of the %d with a reading, %.1f%% of all %d"
          % (dict(sorted(cnt.items())), 100 * cnt["NOT HARMONIC"] / withr, withr, 100 * cnt["NOT HARMONIC"] / tot, tot))
    l25 = [i for i, (a, b) in enumerate(LINES) if a == A25]
    for name in P.PHASE_FREE:
        for hr in range(2):
            vd = res[(name, hr)][6]; c = {}
            for li in l25:
                for hi in range(len(P.HIGGS)): c[vd[li, hi]] = c.get(vd[li, hi], 0) + 1
            print("B  (ii) the %d slope-2/5 lines, reading %s, %s: %s" % (len(l25), name, P.HORS[hr], c))
    for tgt in ("UNDETERMINED", "NOISE-LIMITED"):
        n = sub = 0
        for (valid, D1, D2, sD, cls, ratio, vd) in res.values():
            for li in range(nl):
                for hi in range(len(P.HIGGS)):
                    if vd[li, hi] != tgt: continue
                    n += 1; v = valid[li, :, hi]
                    sub += bool((v & (ratio[li, :, hi] >= 3.5) & (ratio[li, :, hi] <= 4.5) & (np.abs(D1[li, :, hi]) > 100 * sD[li, :, hi])).any())
        print("B  (iii) %s: %d combinations; with a valid centre scaling as r^2 (ratio 3.5-4.5, |D(r1)| > 100 sigma_D): %d" % (tgt, n, sub))
    for (thrD, kmin, rlo, rhi) in [(1e-6, 1, 3, 5), (1e-4, 1, 3, 5), (1e-4, 2, 3.8, 4.2)]:
        t = 0
        for (valid, D1, D2, sD, cls, ratio, vd) in res.values():
            N = valid & (sD <= 1e-9) & (np.abs(D1) > thrD) & (ratio >= rlo) & (ratio <= rhi)
            t += int((N.sum(axis=1) >= kmin).sum())
        print("B  (iv) NOT HARMONIC with N := |D(r1)| > %.0e, ratio %.1f-%.1f, at least %d N centres: %d (%.1f%% of %d)" % (thrD, rlo, rhi, kmin, t, 100 * t / withr, withr))
    c0 = C[:, :, 0]

    def paired(li):
        x = c0[li]; s = np.nanmax(np.abs(x))
        return any(all(np.all(np.abs(x[..., a] - x[..., b]) <= 1e-9 * s) for a, b in p) for p in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))))
    pl = [LINES[li] for li in range(nl) if paired(li)]
    orders = sorted({math.lcm(a.denominator, b.denominator) for a, b in pl})
    print("B  (v) lines whose norms pair: %d, of orders %s; on slope 2/5: %d" % (len(pl), orders, sum(1 for a, b in pl if a == A25)))


# ---------------------------------------------------------------------------------------------------------------- C, D
def census_rows(rel):
    return [json.loads(l) for l in (MAIN / rel).read_text().splitlines() if l.strip()]


def targets():
    v = json.loads((MAIN / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text())["masses_GeV"]
    vv, ee = v["value"], v["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    T6 = np.log([vv[a] / vv[b] for a, b in pr])
    s6 = np.array([math.sqrt((ee[a] / vv[a]) ** 2 + (ee[b] / vv[b]) ** 2 + 0.01) for a, b in pr])
    return T6, s6


def partC():
    rows = census_rows("frontier/B1726_the_two_ingredients_replicated/verification/census.jsonl")
    res = json.loads((MAIN / "frontier/B1739_the_higgs_is_nearly_null/verification/the_higgs_is_nearly_null.json").read_text())
    g = [(p["tau"][1], p["reality_r"]) for p in res["A"]["grid"] if abs(p["tau"][0] - 0.35) < 1e-9]
    gi, gr = np.array([a for a, b in g]), np.log([b for a, b in g])
    RD = ("S", "St")
    for (ru, rd) in (("St", "S"), ("S", "St")):
        V, I = [], []
        for r in rows:
            for h in ("L_max", "L_2"):
                k = r["ckm|%s|%s|%s" % (h, ru, rd)]; V.append(math.sqrt(max(0.0, 1 - k[0] ** 2 - k[2] ** 2))); I.append(r["Im_tau"])
        V, I = np.array(V), np.array(I); ims = sorted(set(I.tolist())); lr = np.interp(ims, gi, gr)
        sl = []
        for q in (0.1, 0.25, 0.5, 0.75):
            ys = np.log([max(np.quantile(V[I == y], q), 1e-9) for y in ims]); sl.append(np.polyfit(lr, ys, 1)[0])
        med_r = [np.median(V[I == y]) / math.exp(l) for y, l in zip(ims, lr)]
        fr = [np.mean(V[I == y] > 0.97) for y in ims]
        print("C  B1739, reading (up %s, down %s): slope of ln quantile(|V_ud|) against ln r at q = 0.10/0.25/0.50/0.75: %s; median |V_ud| / r "
              "from %.1f to %.1f; share with |V_ud| > 0.97 from %.3f to %.3f (Im tau %.2f to %.2f)"
              % (ru, rd, " ".join("%.2f" % x for x in sl), med_r[0], med_r[-1], fr[0], fr[-1], ims[0], ims[-1]))
    T6, s6 = targets(); U, D, E, K, IM, LN = [], [], [], [], [], []
    lg = lambda x: np.log(np.maximum(np.array(x, float), 1e-300))
    for r in rows:
        for h in ("L_max", "L_2"):
            U.append([lg(r["up|%s|%s" % (h, a)]) for a in RD]); D.append([lg(r["down|%s|%s" % (h, a)]) for a in RD])
            E.append([lg(r["lep|%s|%s" % (h, a)]) for a in RD]); K.append(r["ckm|%s|St|S" % h][:3]); IM.append(r["Im_tau"]); LN.append(r["line"])
    U, D, E, K, IM = map(np.array, (U, D, E, K, IM))
    Vud = np.sqrt(np.clip(1 - K[:, 0] ** 2 - K[:, 2] ** 2, 0, None)); al = Vud >= 0.97
    print("C  the Standard Model's reading: %d rows; |V_ud| > 0.97 at %.1f%% (%.1f%% at Im tau 3.0-3.5)" % (len(Vud), 100 * np.mean(Vud > 0.97), 100 * np.mean(Vud[IM >= 3.0] > 0.97)))
    best_all, best_al, fac_al = np.inf, np.inf, []
    for l in (0, 1):
        for c in (1, 3):
            k = math.log(c); X = np.concatenate([U[:, 1], D[:, 0], (E[:, l, 0] + k)[:, None], (E[:, l, 1] - k)[:, None]], axis=1)
            chi = (((X - T6) / s6) ** 2).sum(1); w = np.max(np.abs(X - T6), axis=1)
            best_all = min(best_all, chi.min()); best_al = min(best_al, chi[al].min()); fac_al.append(math.exp(w[al].min()))
    print("C  joint test, up S~ and down S, lepton S or S~, c in {1, 3}: least chi2_six over all rows %.2f; over the %d rows with |V_ud| >= 0.97 "
          "%.1f; their best six within a factor %.2f-%.2f" % (best_all, al.sum(), best_al, min(fac_al), max(fac_al)))
    cmp = load("cmp1740", MAIN / "frontier/B1740_the_non_null_higgs_under_the_standard_models_reading/verification/compare.py")
    Pc = cmp.B1726_CENSUS; Ac = cmp.arrays(Pc); out = []
    for cfg in ((1, 0, 0), (1, 1, 1), (0, 1, 1), (0, 0, 0)):
        cmp.SM = (cfg,); F = cmp.chi2_features("sm", False, Pc); out.append("%s %.2f" % ("".join("~" if x else "S" for x in cfg), float(cmp.min_chi2(F, Ac["T6"][None, :])[0])))
    print("C  B1726's least chi2_six per assignment (up, down, lepton; ~ = S~), B1740's compare.py:", "; ".join(out))


def partD():
    rows = census_rows("frontier/B1740_the_non_null_higgs_under_the_standard_models_reading/verification/census.jsonl")
    T6, _ = targets(); I, X = [], {s: [] for s in ("up", "down", "lep")}
    for r in rows:
        for h in ("L_max", "L_2"):
            for s in X: X[s].append([r["%s|%s|%s" % (s, h, a)][0] for a in ("S", "St")])
            I.append(r["Im_tau"])
    I = np.array(I); X = {s: np.array(x) for s, x in X.items()}; ims = sorted(set(I.tolist()))
    print("D  B1740's F_-2 rows: %d (x 2 horocycles); least m2/m3 (reading S): up %.3f (measured %.2e), down %.3f, leptons %.3f; up's least from "
          "%.3f at Im tau %.2f to %.3f at %.2f" % (len(rows), X["up"][:, 0].min(), math.exp(T6[0]), X["down"][:, 0].min(), X["lep"][:, 0].min(),
                                                  X["up"][I == ims[0], 0].min(), ims[0], X["up"][I == ims[-1], 0].min(), ims[-1]))


# ---------------------------------------------------------------------------------------------------------------- E
def partE():
    REF = MAIN / "frontier/B1790_the_reading_not_derived_in_the_frame/verification/referee"
    sys.path.insert(0, str(REF))
    with contextlib.redirect_stdout(io.StringIO()):
        import common as Cr
    Dp = np.diag([1, 1, -1])
    for tau, hol, label in ((complex(0.0, 3.0), complex(0.0, 3.0), "Re tau 0, the section DR'(tau)"),
                            (complex(0.5, 3.0), complex(-0.5, 3.0), "Re tau 1/2, the section DR'(tau - 1)"),
                            (complex(0.35, 3.05), complex(0.35, 3.05), "control, Re tau 0.35, DR'(tau)")):
        sp = Cr.spectra(tau, Fr(2, 5), Fr(1, 10), "L_max"); sq = Cr.spectra(tau, Fr(2, 5), Fr(1, 10), "L_max", Shiggs=Cr.quat(Dp @ Cr.comps(hol)))
        print("E  B1790, (2/5, 1/10) at %s, %s: largest |d ln| of the holomorphic section's spectra against the S~ reading %.2e, against S %.2e"
              % (tau, label, max(Cr.dln(sp[(s, "St")], sq[(s, "S")]) for s in Cr.SECT), max(Cr.dln(sp[(s, "S")], sq[(s, "S")]) for s in Cr.SECT)))


# ---------------------------------------------------------------------------------------------------------------- F, G
def partF():
    d = SMC / "docs" / "dossiers" / "the_weave_2026-10-07"; sys.path.insert(0, str(d))
    with contextlib.redirect_stdout(io.StringIO()):
        import the_potential_off_the_mirror as W175
    W72 = W175.W72; b = Fr(W72.LINE[1]) if not isinstance(W72.LINE[1], Fr) else W72.LINE[1]
    js = json.loads((d / "the_price_of_cp_at_the_counted_line.json").read_text())
    rows = [(r["row"][3], r["X_row"]) for r in js["P3"]["per row"]]
    hs = sorted({round(y, 9) for y, _ in rows}); psi = np.asarray(W175.W67.psi_of(A25, b))
    t5 = lambda x, y: min((x - y) % 5, 5 - (x - y) % 5)
    print("F  W172's line %s; %d rows at %d distinct heights (as stored: %d)" % (W72.LINE, len(rows), len(hs), len({y for y, _ in rows})))
    w0 = W72.weights(0.0); xs, dist, gap = [], [], []
    for y in hs:
        m, _ = W175.x_minimum(b, y, w0); X = m["X*"]; xs.append(min(X, (2 - X) % 5))
        V1 = float(W72.kq(1.0, y, W175.S, psi) @ w0); gap.append(m["V*"] - V1)
        dist.append(min(min(t5(X, xr), t5((2 - X) % 5, xr)) for yy, xr in rows if abs(yy - y) < 1e-7))
    print("F  matter only (bosons x 0): X* (or its mirror image 2 - X*) %.4f-%.4f at the %d heights; V(X*) - V(1) %.4f to %.4f; distance to the "
          "nearest row's X at that height %.3f-%.3f; the rows' X %.3f-%.3f" % (min(xs), max(xs), len(hs), min(gap), max(gap), min(dist), max(dist),
                                                                          min(x for _, x in rows), max(x for _, x in rows)))
    for y in (2.960539291988587, 3.118684093682859):
        out = []
        for beta in (0.0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.5, 1.0):
            m, _ = W175.x_minimum(b, y, W72.weights(beta)); X = m["X*"]; out.append("%.2f:%.3f" % (beta, min(t5(X, 1.0), t5(X, 3.5))))
        print("F  Im tau %.4f, bosons' weight: distance of X* from the mirror points {1, 3.5}: %s" % (y, " ".join(out)))
    w1 = W72.weights(1.0); up, price, amps = [], [], {}
    for y, xr in rows:
        k = round(y, 9)
        if k not in amps:
            Xs, vals, _ = W175.profile(b, y, w1); m, _ = W175.x_minimum(b, y, w1); amps[k] = (vals.max() - vals.min(), m["V*"])
        amp, Vs = amps[k]; vr = float(W72.kq(xr, y, W175.S, psi) @ w1)
        up.append((vr - Vs) / amp); price.append((vr - Vs) / 2 / amp)
    print("F  full content: the X-well's amplitude %.3f-%.3f; the rows sit %.3f-%.3f of the way up it; the price (V(X_row) - V*)/2 is %.3f-%.3f of "
          "the amplitude" % (min(a for a, _ in amps.values()), max(a for a, _ in amps.values()), min(up), max(up), min(price), max(price)))


def partG():
    d = json.loads((SMC / "docs/dossiers/the_weave_2026-10-07/the_skeleton_census.json").read_text())
    D6 = np.array(d["the six (data, read once)"]); L3 = math.log(3); FL = math.log(1e-12)
    S = np.linspace(-80, 0, 160001)[:-1]

    def exc(n):
        n = np.asarray(n, float); w = np.abs(D6[None, :] - S[:, None] * n[None, :]).max(1); return w.min() - L3
    unc = {tuple(l) for l in d["S0"]["unconverged lines"]}; rows = []
    for e in d["per line"]:
        if e["line"][0] != "2/5": continue
        for p in e["per Re tau"]:
            n = p["pattern n_i"]
            if n is None or any(v is None for v in n): continue
            sp = {float(k): np.array(v) for k, v in p["six per height"].items()}
            if not all(h in sp for h in (4.0, 5.0, 6.0)): continue
            e45 = -(sp[5.0] - sp[4.0]) / (2 * math.pi); e56 = -(sp[6.0] - sp[5.0]) / (2 * math.pi)
            ok = bool(((sp[4.0] > FL) & (sp[5.0] > FL) & (sp[6.0] > FL)).all())
            rows.append((exc(n), exc(e45) if ok else None, exc(n + (e56 - e45)) if ok else None, tuple(e["line"]), p["x"], tuple(e["line"]) in unc))
    print("G  W174, slope-2/5 patterns: %d; least excess over ln 3 with the stored (5,6) exponents %.3f; passing with the (4,5) exponents: %s"
          % (len(rows), min(r[0] for r in rows),
             ", ".join("(%s, %s)@%s %+.3f%s" % (r[3][0], r[3][1], r[4], r[1], " unconverged" if r[5] else "") for r in sorted(rows, key=lambda r: r[1] if r[1] is not None else 9) if r[1] is not None and r[1] < 0)))
    ex = [r[2] for r in rows if r[1] is not None and r[1] < 0]
    print("G  the same patterns with the exponents extrapolated past (5,6) (linear in the step): excess %s" % " ".join("%+.3f" % x for x in ex))


# ---------------------------------------------------------------------------------------------------------------- H
def partH():
    Hm = load("horocycle_audit", REPO / "relays" / "chat1_2026-10-28_horocycle" / "horocycle.py")
    z = np.load(REPO / "relays" / "chat1_2026-10-28_horocycle" / "horocycle_census.npz")
    bp = json.loads((REPO / "relays" / "chat1_2026-10-28_horocycle" / "horocycle_census.json").read_text())["base_points"]
    G = z["G"]
    for k, delta in ((0, complex(0.05, -1.0)), (55, complex(-0.15, -1.2)), (160, complex(0.0, -0.65))):
        li, re_, im_ = bp[k]; tp = complex(re_, im_); t0 = tp + delta; t1 = time.time()
        y = Hm.six(Hm.point(t0.real, t0.imag, li)[0], 1)
        A, dt, fl, it, ev, path, _ = Hm.search(li, tp, y, 1, G)
        print("H  base point %d (line (2/5, %s) at %.2f%+.2fi), planted shift %s (below G: %s): found distance %.1e, shift recovered to %.1e, flagged %s, "
              "%d iterations (%.0f s)" % (k, Hm.lines()[li][1], re_, im_, delta, t0.imag < 2.3, A, abs(dt - delta), fl, it, time.time() - t1))


if __name__ == "__main__":
    t0 = time.time()
    for name, f in (("A", partA), ("B", partB), ("C", partC), ("D", partD), ("E", partE), ("F", partF), ("G", partG), ("H", partH)):
        t = time.time()
        try:
            f()
        except Exception:
            print("%s FAILED:\n%s" % (name, clean(traceback.format_exc())))
        print("   (part %s: %.0f s)" % (name, time.time() - t), flush=True)
    print("audit_checks exit 0 (%.0f s)" % (time.time() - t0))
