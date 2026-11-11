#!/usr/bin/env python3
"""THE V1 CARD: does an end of the window in Im tau move a null's count of well-fitted random targets?
NULL-ONLY: no measured target enters any statistic.

The audit's finding V1 says the nulls behind the six's rarities have an unpriced window in Im tau.  This card decides it
for two named nulls, sealed in PREREGISTRATION.md before either stage ran:
    N1   B1726's null: its 47 880 rows on the plain grid Im tau = 2.05 ... 3.45; the worst-factor measure
    N2   B1753's null: its 21 408 rows at 223 apexes of height 2.01 ... 3.56; chi-square (its decisive cell) and the worst factor
The instruments are main's sealed modules, loaded unchanged and checked by hash.  The measured targets their loaders build
(T6, T9) are deleted in every process before anything is computed.  No comparison file is opened, and no value of a
statistic is kept or printed: only where the best rows lie and how many targets change.  (Chi-square's weights are the
measurement's relative uncertainties, as the sealed measure defines them; main's loader reads that file.)

    python3 -B v1_card.py --selftest                  a toy instrument; no file of the record is read
    python3 -B v1_card.py --stage controls            planted targets only: rows of the census used as targets; no random target is drawn
    python3 -B v1_card.py --stage null --workers 8    the random targets of the sealed cells, and fresh ones; refuses to run before the controls

Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, time, hashlib, pathlib, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
MENUS = ("seat", "cov", "free")
QS = (0.05, 0.01, 0.001, 0.0001)
Q_DECISIVE = 0.001
Q_LOSS = (0.01, 0.001)
STRIDE = 97                                             # K1 plants every 97th row
TOL = {"wf": 1e-9, "chi2": 1e-3}                        # a planted row must be found again to this (chi-square is expanded, so not exact)
INSTRUMENTS = {
    "N1": {"arc": "B1726_the_two_ingredients_replicated", "loads": "B1726's compare.py", "n_min": 6, "measures": ("wf",),
           "banked": list(range(1726, 1746)), "fresh": list(range(9172601, 9172831)),
           "sha": {"frontier/B1726_the_two_ingredients_replicated/verification/compare.py": "4cd90052f73d12f40daedb95b46d79b0ec5222e551cca58c9e395672f8016692",
                   "frontier/B1726_the_two_ingredients_replicated/verification/census.jsonl": "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d"}},
    "N2": {"arc": "B1753_the_six_on_the_five_ality_lines", "loads": "B1753's compare.py, which loads B1741's", "n_min": 15, "measures": ("chi2", "wf"),
           "banked": list(range(1789, 1809)), "fresh": list(range(9175301, 9175531)),
           "sha": {"frontier/B1753_the_six_on_the_five_ality_lines/verification/compare.py": "4ebaccfa1397b5d8bfc1f50c1f0e1abf7d3fd105ec3d9e68281b171c7e85038e",
                   "frontier/B1753_the_six_on_the_five_ality_lines/verification/census.jsonl": "c7f58dced34d6858bcfed9d25e01dfe27d4f212a29dd3a4d53f49010ad410c69",
                   "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py": "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"}},
}
DECISIVE = (("N1", "wf|seat"), ("N2", "chi2|seat"), ("N2", "wf|seat"))
ENDS = ("bottom", "top")
_I = {}


# ------------------------------------------------------------------ the counting (used by every stage, and by the self-test)
def layers(points, n_min, depth=3):
    """the boundary of a set of (Re tau, Im tau) points, layer by layer.  A layer is a pair (bottom, top): at each end, the
    fewest extreme distinct heights that hold at least n_min of the points still left.  Layer 1 is the boundary."""
    left = sorted(set(points), key=lambda p: (p[1], p[0])); out = []
    for _ in range(depth):
        hs = sorted({p[1] for p in left})

        def take(order):
            got = []
            for h in order:
                got += [p for p in left if p[1] == h]
                if len(got) >= n_min: break
            return frozenset(got)
        bot, top = take(hs), take(hs[::-1])
        assert not (bot & top), "the window is too short for %d layers" % depth
        out.append((bot, top)); left = [p for p in left if p not in bot and p not in top]
    return out


def clopper(h, n, level=0.95):
    """the exact two-sided interval for a share h of n"""
    from scipy.stats import beta
    a = (1 - level) / 2
    return (float(beta.ppf(a, h, n - h + 1)) if h > 0 else 0.0, float(beta.ppf(1 - a, h + 1, n - h)) if h < n else 1.0)


def tail_size(q, n):
    return max(1, int(math.ceil(q * n - 1e-9)))


def summarise(s, row, masks, qs=QS):
    """s: each target's best statistic; row: the row that gave it; masks: {name: boolean over rows}.
    For all targets and for each tail (the best-fitted share q, ties by position): the share whose best row lies on each
    mask, its exact 95% interval, the rows' own share of the mask, and their ratio."""
    s = np.asarray(s, dtype=float); row = np.asarray(row); n = len(s)
    order = np.argsort(s, kind="stable")
    out = {"targets": int(n), "rows_share": {k: float(np.mean(m)) for k, m in masks.items()}, "populations": {}}
    pops = [("all", order)] + [("best %g%%" % (100 * q), order[:tail_size(q, n)]) for q in qs]
    for name, idx in pops:
        d = {"n": int(len(idx)), "share": {}}             # no value of the statistic is kept or printed: only where the best rows lie
        for k, m in masks.items():
            h = int(np.sum(m[row[idx]])); lo, hi = clopper(h, len(idx)); r = out["rows_share"][k]
            d["share"][k] = {"hits": h, "share": h / len(idx), "ci95": [lo, hi], "rows_share": r, "ratio_to_rows_share": (h / len(idx)) / r if r > 0 else None}
        out["populations"][name] = d
    return out


def leave_out_loss(s, row, k, mask, recompute):
    """of the k best-fitted targets, the share that is no longer fitted as well as the k-th once the rows of `mask` are
    removed.  recompute(idx) returns the best statistic of the targets idx over the rows left.  Only a target whose best
    row lies in the mask can change, so only those are recomputed."""
    s = np.asarray(s, dtype=float); order = np.argsort(s, kind="stable")[:k]; theta = float(s[order[-1]])
    idx = order[mask[np.asarray(row)[order]]]
    s2 = np.asarray(recompute(idx), dtype=float) if len(idx) else np.zeros(0)
    lost = int(np.sum(s2 > theta + 1e-9 * (1 + abs(theta)))); lo, hi = clopper(lost, k); r = float(np.mean(mask))
    return {"n": int(k), "with_their_best_row_there": int(len(idx)), "lost": lost, "loss": lost / k, "ci95": [lo, hi], "rows_share": r,
            "ratio_to_rows_share": (lost / k) / r}


def verdict(loss, valid):
    """the reading sealed in PREREGISTRATION.md, section 6, applied to one decisive cell.
    loss: {"bottom": leave_out_loss(...) for layer 1 at the bottom, "top": the same at the top}; valid: control K2 for this measure."""
    if not valid: return "NOT VALID: the leave-out control K2 failed for this measure"
    res = {}
    for end in ENDS:
        c = loss[end]; r, ratio = c["rows_share"], c["ratio_to_rows_share"]
        res[end] = "A" if (ratio >= 2 and c["ci95"][0] > r) else ("C" if ratio < 0.5 else "B")
    each = "bottom %s, top %s" % (res["bottom"], res["top"])
    if "A" in res.values(): return "A: an end of the window is a lever (%s)" % each
    if all(v == "C" for v in res.values()): return "C: the ends add almost nothing (%s)" % each
    return "B: an end is like other rows (%s)" % each


# ------------------------------------------------------------------ main's instruments, unchanged
def _root():
    return next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())


def instrument(name):
    """main's module for N1 or N2, its arrays with the measured targets deleted, and the row geometry"""
    if name not in _I:
        cfg = INSTRUMENTS[name]; root = _root()
        for rel, sha in cfg["sha"].items():
            got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
            assert got == sha, "%s is not the sealed file (%s)" % (rel, got[:16])
        path = root / "frontier" / cfg["arc"] / "verification" / "compare.py"
        sp = importlib.util.spec_from_file_location("v1card_%s_compare" % name.lower(), path)
        mod = importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
        C = mod.C if name == "N2" else mod                  # B1753's compare re-points B1741's module and exposes it as C
        A = C.arrays()
        for k in ("T6", "T9"): A.pop(k)                     # the measured targets: deleted before anything is computed
        assert "T6" not in C.arrays() and "T9" not in C.arrays()
        pts = [(round(float(l[1]), 9), round(float(l[2]), 9)) for l in A["lab"]]
        lay = layers(pts, cfg["n_min"], 3)
        masks = {}
        for k, (bot, top) in enumerate(lay, 1):
            masks["bottom layer %d" % k] = np.array([p in bot for p in pts]); masks["top layer %d" % k] = np.array([p in top for p in pts])
        _I[name] = {"C": C, "A": A, "pts": pts, "layers": lay, "masks": masks, "im": np.array([p[1] for p in pts])}
    return _I[name]


def wf_best(C, T, menus, keep=None):
    """the worst-factor measure: main's errs and best_over, unchanged.  keep (an index array) restricts the rows."""
    out = {m: (np.empty(len(T)), np.empty(len(T), dtype=np.int64)) for m in menus}
    for j, t in enumerate(T):
        eu, ed, el, _ek = C.errs(t)
        if keep is not None: eu, ed, el = eu[keep], ed[keep], {k: v[keep] for k, v in el.items()}
        for m in menus:
            w, i, _cfg = C.best_over(t, m, (eu, ed, el, None))
            out[m][0][j] = w; out[m][1][j] = i if keep is None else keep[i]
    return out


def chi_best(C, T, menus, keep=None):
    """chi-square: main's chi2_features, unchanged; its min_chi2 with the row kept as well as the minimum"""
    T = np.asarray(T); out = {}
    for m in menus:
        best = np.full(len(T), np.inf); arg = np.zeros(len(T), dtype=np.int64)
        for X, f in C.chi2_features(m, False):
            if keep is not None: X = X[keep]
            x2 = (X ** 2).sum(1)
            for s0 in range(0, len(T), 400):
                t = f(T[s0:s0 + 400]); c = x2[:, None] - 2 * X @ t.T + (t ** 2).sum(1)[None, :]
                mn = c.min(0); a = c.argmin(0); upd = mn < best[s0:s0 + 400]
                best[s0:s0 + 400] = np.where(upd, mn, best[s0:s0 + 400]); arg[s0:s0 + 400] = np.where(upd, a, arg[s0:s0 + 400])
        out[m] = (best, arg if keep is None else np.asarray(keep)[arg])
    return out


BEST = {"wf": wf_best, "chi2": chi_best}


def planted(A, rows):
    """each given row as a target: its own six logs under the seat's first reading (up S~, down S, leptons S), c = 1.
    Under every menu the statistic at that row is zero."""
    return np.concatenate([A["U"][rows, 1], A["Dn"][rows, 0], A["E"][rows, 0]], axis=1)


# ------------------------------------------------------------------ stage 1: the planted controls (no random target)
def controls(log):
    out = {}
    for name, cfg in INSTRUMENTS.items():
        I = instrument(name); C, A, masks = I["C"], I["A"], I["masks"]; n = len(I["pts"]); pts = I["pts"]
        t0 = time.time()
        log("%s (%s): %d rows at %d points; heights %.4f ... %.4f" % (name, cfg["loads"], n, len(set(pts)), I["im"].min(), I["im"].max()))
        for k, (bot, top) in enumerate(I["layers"], 1):
            log("   layer %d   bottom: %2d points, heights %.4f ... %.4f, rows' share %.4f   |   top: %2d points, heights %.4f ... %.4f, rows' share %.4f" % (
                k, len(bot), min(p[1] for p in bot), max(p[1] for p in bot), masks["bottom layer %d" % k].mean(),
                len(top), min(p[1] for p in top), max(p[1] for p in top), masks["top layer %d" % k].mean()))
        res = {"rows": n, "points": len(set(pts)), "layers": [{"bottom_points": len(b), "top_points": len(t)} for b, t in I["layers"]],
               "rows_share": {k: float(m.mean()) for k, m in masks.items()}, "K1": {}, "K2": {}, "K3": {}}
        V = planted(A, np.arange(n)); _u, inv, cnt = np.unique(V, axis=0, return_inverse=True, return_counts=True)
        twin = cnt[np.ravel(inv)] > 1                       # a row whose six planted values another row shares exactly cannot be told from it
        res["rows_with_an_exact_twin"] = int(twin.sum())
        log("   rows whose six planted values another row shares exactly: %d of %d (never planted)" % (twin.sum(), n))

        # K1: a planted row is found again, at zero and at its own height
        rows = np.unique(np.concatenate([np.arange(0, n, STRIDE), [n - 1]])); rows = rows[~twin[rows]]; T = V[rows]; k1 = True
        for meas in cfg["measures"]:
            t1 = time.time(); got = BEST[meas](C, T, MENUS); rate = len(rows) / max(time.time() - t1, 1e-9)
            for m in MENUS:
                s, r = got[m]
                zero = np.abs(s) <= TOL[meas]
                point = np.array([pts[a] == pts[b] for a, b in zip(r, rows)]); height = I["im"][r] == I["im"][rows]
                ok = bool(zero.all() and height.mean() >= 0.99); k1 &= ok
                res["K1"]["%s|%s" % (meas, m)] = {"planted": int(len(rows)), "found_at_zero": int(zero.sum()), "at_the_planted_point": int(point.sum()),
                                                  "at_the_planted_height": int(height.sum()), "largest_statistic": float(np.max(np.abs(s))), "holds": ok}
                log("   K1 %-10s planted %d rows: found at zero %d, at the planted point %d, at the planted height %d; largest statistic %.2e -> %s" % (
                    "%s|%s" % (meas, m), len(rows), zero.sum(), point.sum(), height.sum(), np.max(np.abs(s)), "HOLDS" if ok else "FAILS"))
            res["K1"]["%s_targets_per_second_three_menus" % meas] = rate
            log("   the %s measure, three menus: %.0f targets a second in one process" % (meas, rate))
        res["K1"]["holds"] = bool(k1)

        # K2: the leave-out count, on plants whose answer is known.  A planted row of layer 1 is fitted at zero; with layer 1
        # removed it must be lost.  A planted row of layer 3 must be kept when layer 1 is removed.
        for meas in cfg["measures"]:
            ok2 = True
            for end in ENDS:
                mask = masks["%s layer 1" % end]; keep = np.flatnonzero(~mask)
                for what, want in (("layer 1", "all"), ("layer 3", "none")):
                    src = np.flatnonzero(masks["%s %s" % (end, what)] & ~twin); T = V[src]
                    for m in MENUS:
                        s_full, r_full = BEST[meas](C, T, (m,))[m]
                        zero = int(np.sum(np.abs(s_full) <= TOL[meas]))
                        # the threshold of "fitted" is the tolerance: every plant is given the statistic TOL, so that the k-th best is TOL
                        L = leave_out_loss(np.full(len(src), TOL[meas]), r_full, len(src), mask, lambda idx: BEST[meas](C, T[idx], (m,), keep)[m][0])
                        ok = bool(zero == len(src) and (L["lost"] >= 0.99 * len(src) if want == "all" else L["lost"] == 0)); ok2 &= ok
                        res["K2"]["%s|%s|%s|planted in %s" % (meas, m, end, what)] = {"planted": int(len(src)), "fitted_at_zero_with_every_row": zero,
                                                                                    "lost_without_layer_1": L["lost"], "expected": want, "holds": ok}
                        log("   K2 %-4s %-4s %-6s planted %5d rows of %s: at zero with every row %d; lost without layer 1 at that end: %d (expected %s) -> %s" % (
                            meas, m, end, len(src), what, zero, L["lost"], want, "HOLDS" if ok else "FAILS"))
            res["K2"]["%s_holds" % meas] = bool(ok2)

        # K3, a read-out and not a control: where does a row of layer 1 find its best fit once layers 1 and 2 are gone?
        outer = masks["bottom layer 1"] | masks["top layer 1"] | masks["bottom layer 2"] | masks["top layer 2"]
        keep = np.flatnonzero(~outer)
        for meas in cfg["measures"]:
            for end in ENDS:
                src = np.flatnonzero(masks["%s layer 1" % end] & ~twin); T = V[src]
                s, r = BEST[meas](C, T, ("seat",), keep)["seat"]
                live = np.abs(s) > TOL[meas]                 # a planted row with a twin left inside says nothing
                land = masks["%s layer 3" % end][r[live]]; far = masks["%s layer 3" % ("bottom" if end == "top" else "top")][r[live]]
                share = float(land.mean()) if live.any() else float("nan"); rs = float(masks["%s layer 3" % end][keep].mean())
                lo, hi = clopper(int(land.sum()), int(live.sum())) if live.any() else (float("nan"), float("nan"))
                res["K3"]["%s|%s" % (meas, end)] = {"planted": int(len(src)), "dropped_as_twins": int((~live).sum()), "landed_on_the_nearest_layer_left": int(land.sum()),
                                                    "share": share, "ci95": [lo, hi], "landed_on_the_far_end": int(far.sum()),
                                                    "rows_share_of_that_layer_in_the_narrowed_window": rs, "ratio": share / rs if rs > 0 else None}
                log("   K3 %-4s %-6s (read-out) %d rows of layer 1 against the window without layers 1 and 2 (%d dropped as twins): %d find their best fit on the nearest layer left, share %.4f [%.4f, %.4f]; rows' share of it %.4f; ratio %.2f; on the far end %d" % (
                    meas, end, len(src), (~live).sum(), land.sum(), share, lo, hi, rs, share / rs if rs > 0 else float("nan"), far.sum()))
        res["seconds"] = time.time() - t0
        out[name] = res
    out["K1_holds"] = bool(all(out[n]["K1"]["holds"] for n in INSTRUMENTS))
    json.dump(out, open(HERE / "v1_controls.json", "w"), indent=1)
    log("K1 holds for both instruments: %s | K2 holds: %s" % (out["K1_holds"], ", ".join("%s %s %s" % (n, meas, out[n]["K2"]["%s_holds" % meas]) for n, cfg in INSTRUMENTS.items() for meas in cfg["measures"])))
    log("controls exit 0")


# ------------------------------------------------------------------ stage 2: the null
def null_seed(arg):
    name, seed = arg
    I = instrument(name); C = I["C"]
    d6, _d9 = C.draws(seed); T = np.array(d6); out = {}
    for meas in INSTRUMENTS[name]["measures"]:
        got = BEST[meas](C, T, MENUS)
        for m in MENUS: out["%s|%s" % (meas, m)] = (got[m][0].astype(np.float64), got[m][1].astype(np.int32))
    return name, seed, out


def null(workers, log):
    from multiprocessing import get_context
    ctl = HERE / "v1_controls.json"
    if not ctl.is_file(): sys.exit("refused: the planted controls have not been run (no v1_controls.json beside this script)")
    ctl = json.loads(ctl.read_text(encoding="utf-8"))
    if not ctl.get("K1_holds"): sys.exit("refused: control K1 failed; the instrument does not find a planted row")
    tasks = [(n, s) for n, cfg in INSTRUMENTS.items() for s in cfg["banked"] + cfg["fresh"]]
    got = {n: {} for n in INSTRUMENTS}; t0 = time.time()
    with get_context("fork").Pool(workers) as P:
        for k, (name, seed, out) in enumerate(P.imap_unordered(null_seed, tasks, chunksize=1), 1):
            got[name][seed] = out
            if k % 25 == 0 or k == len(tasks): log("   %d of %d seeds (%.0f s)" % (k, len(tasks), time.time() - t0))
    res = {"q_decisive": Q_DECISIVE, "instruments": {}, "decisive": {}}
    for name, cfg in INSTRUMENTS.items():
        I = instrument(name); C = I["C"]; masks = dict(I["masks"]); im = I["im"]; seeds = cfg["banked"] + cfg["fresh"]
        if name == "N1":
            for h in sorted(set(im.tolist())): masks["Im tau %.2f" % h] = im == h
        else:
            for lo in (2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4): masks["Im tau [%.1f, %.1f)" % (lo, lo + 0.2)] = (im >= lo) & (im < lo + 0.2)
            top10 = sorted(set(im.tolist()))[-10:]; masks["the ten highest heights"] = np.isin(im, top10)
        masks["both ends, layer 1"] = masks["bottom layer 1"] | masks["top layer 1"]
        profile = [k for k in masks if k.startswith("Im tau")]
        targets = np.concatenate([np.array(C.draws(s)[0]) for s in seeds])          # the same draws again, to recompute the few that can change
        r = {"K2": {meas: bool(ctl[name]["K2"]["%s_holds" % meas]) for meas in cfg["measures"]}, "rows": int(len(im)),
             "seeds_banked": cfg["banked"], "seeds_fresh": [cfg["fresh"][0], cfg["fresh"][-1]], "cells": {}}
        for key in ["%s|%s" % (meas, m) for meas in cfg["measures"] for m in MENUS]:
            meas, menu = key.split("|")

            def cat(ss): return (np.concatenate([got[name][s][key][0] for s in ss]), np.concatenate([got[name][s][key][1] for s in ss]))
            sb, rb = cat(cfg["banked"]); sa, ra = cat(seeds); assert len(sa) == len(targets)
            cell = {"banked_seeds": summarise(sb, rb, masks, QS[:2]), "all_seeds": summarise(sa, ra, masks, QS), "leave_out": {}}
            for q in Q_LOSS:
                k = tail_size(q, len(sa)); d = {}
                for lay_k in (1, 3):
                    for end in ENDS:
                        mask = I["masks"]["%s layer %d" % (end, lay_k)]; keep = np.flatnonzero(~mask)
                        d["%s layer %d" % (end, lay_k)] = leave_out_loss(sa, ra, k, mask, lambda idx: BEST[meas](C, targets[idx], (menu,), keep)[menu][0])
                cell["leave_out"]["best %g%%" % (100 * q)] = d
            r["cells"][key] = cell
            tag = "best %g%%" % (100 * Q_DECISIVE); d = cell["leave_out"][tag]; pop = cell["all_seeds"]["populations"][tag]
            log("%s %-10s %s of %d targets (%d):" % (name, key, tag, len(sa), pop["n"]))
            for end in ENDS:
                c = d["%s layer 1" % end]; c3 = d["%s layer 3" % end]
                log("      %-6s end: lost without layer 1: %4d, loss %.4f [%.4f, %.4f]; rows' share %.4f; ratio %.2f   (best row there: %d; lost without layer 3 instead: %d)" % (
                    end, c["lost"], c["loss"], c["ci95"][0], c["ci95"][1], c["rows_share"], c["ratio_to_rows_share"], c["with_their_best_row_there"], c3["lost"]))
            log("      where the best rows lie, share by height: " + "  ".join("%s %.3f" % (k.replace("Im tau ", ""), pop["share"][k]["share"]) for k in profile))
            allp = cell["all_seeds"]["populations"]["all"]["share"]
            log("      ALL targets, best row on: bottom layer 1 %.4f, top layer 1 %.4f, both %.4f" % (allp["bottom layer 1"]["share"], allp["top layer 1"]["share"], allp["both ends, layer 1"]["share"]))
            if (name, key) in DECISIVE:
                v = verdict({e: d["%s layer 1" % e] for e in ENDS}, r["K2"][meas]); res["decisive"]["%s %s" % (name, key)] = v; log("      DECISIVE CELL -> %s" % v)
        res["instruments"][name] = r
    # the audit's figure: is any share of ALL targets on an upper end within 17% to 23%?
    fig = {}
    for name, key, mask in (("N1", "wf|seat", "top layer 1"), ("N1", "wf|seat", "both ends, layer 1"), ("N2", "chi2|seat", "top layer 1"),
                            ("N2", "chi2|seat", "Im tau [3.4, 3.6)"), ("N2", "chi2|seat", "the ten highest heights"), ("N2", "wf|seat", "top layer 1")):
        for ss in ("banked_seeds", "all_seeds"):
            fig["%s %s | %s | %s" % (name, key, mask, ss)] = res["instruments"][name]["cells"][key][ss]["populations"]["all"]["share"][mask]["share"]
    res["the_audits_figure"] = {"shares_of_all_targets": fig, "reproduced": bool(any(0.17 <= v <= 0.23 for v in fig.values()))}
    for k, v in fig.items(): log("the audit's figure, candidates: %-66s %.4f" % (k, v))
    log("the audit's 20%% reproduced by one of them (17%% to 23%%): %s" % res["the_audits_figure"]["reproduced"])
    json.dump(res, open(HERE / "v1_null.json", "w"), indent=1)
    log("null exit 0")


# ------------------------------------------------------------------ the self-test: a toy instrument, nothing of the record
def selftest():
    rng = np.random.default_rng(20261111); ok = True

    def check(label, cond):
        nonlocal ok; ok &= bool(cond); print("   %-112s %s" % (label, "ok" if cond else "FAILS"))
    # layers on a plain grid and on an uneven set
    grid = [(re, round(2.05 + 0.1 * k, 2)) for re in (0.05, 0.2, 0.35) for k in range(15)]
    L = layers(grid, 3, 3)
    check("grid: layer 1 is the lowest and the highest value, layer 2 the next, layer 3 the next", [sorted({p[1] for p in b}) + sorted({p[1] for p in t}) for b, t in L] == [[2.05, 3.45], [2.15, 3.35], [2.25, 3.25]])
    uneven = [(0.1 * i, h) for i, h in enumerate([2.0, 2.0, 2.1, 2.3, 2.3, 2.3, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.1, 3.2, 3.3, 3.3, 3.4, 3.5, 3.5, 3.5, 3.6])]
    L = layers(uneven, 3, 2)
    check("uneven: bottom layer 1 takes heights until it holds 3 points (2.0, 2.0, 2.1); top takes 3.6 and the three at 3.5", sorted(p[1] for p in L[0][0]) == [2.0, 2.0, 2.1] and sorted(p[1] for p in L[0][1]) == [3.5, 3.5, 3.5, 3.6])
    check("uneven: layer 2 starts where layer 1 ended (bottom 2.3 x 3; top 3.4, 3.3, 3.3)", sorted(p[1] for p in L[1][0]) == [2.3, 2.3, 2.3] and sorted(p[1] for p in L[1][1]) == [3.3, 3.3, 3.4])
    # summarise against a count written another way
    n_rows, n = 600, 20000
    top = np.zeros(n_rows, bool); top[-40:] = True; bot = np.zeros(n_rows, bool); bot[:40] = True
    s = rng.normal(size=n); row = rng.integers(0, n_rows, size=n)
    S = summarise(s, row, {"top": top, "bot": bot}, (0.05, 0.01))
    k = 200; idx = sorted(range(n), key=lambda j: (s[j], j))[:k]; brute = sum(1 for j in idx if row[j] >= n_rows - 40)
    check("summarise: the best 1%% is the 200 smallest statistics, and its count on a mask equals a count by hand (%d)" % brute, S["populations"]["best 1%"]["n"] == k and S["populations"]["best 1%"]["share"]["top"]["hits"] == brute)
    check("summarise: the rows' share is the mask's mean (40 of 600)", abs(S["rows_share"]["top"] - 40 / 600) < 1e-15)
    a = S["populations"]["all"]["share"]["top"]; lo, hi = clopper(a["hits"], n, 0.999)
    check("summarise: with rows drawn evenly, the share of all targets on a mask is the rows' share within its 99.9% interval", lo <= 40 / 600 <= hi)
    lo, hi = clopper(0, 100); check("clopper: 0 of 100 gives [0, 0.0362]", lo == 0.0 and abs(hi - 0.03622) < 2e-5)

    # a toy instrument: rows are points, a target's statistic is its squared distance to the nearest row
    class Toy:
        X = None

        @staticmethod
        def chi2_features(menu, nine): return [(Toy.X, lambda T: T)]
    Toy.X = rng.normal(size=(50, 6))
    T = Toy.X[[3, 17, 44]] + 1e-9
    b, r = chi_best(Toy, T, ("seat",))["seat"]
    check("chi_best: three planted rows found again (rows 3, 17, 44)", r.tolist() == [3, 17, 44] and float(np.max(np.abs(b))) < 1e-9)
    keep = np.array([j for j in range(50) if j not in (3, 17, 44)])
    b2, r2 = chi_best(Toy, T, ("seat",), keep)["seat"]
    direct = [int(keep[np.argmin(((Toy.X[keep] - t) ** 2).sum(1))]) for t in T]
    check("chi_best with rows removed: the row returned is an index into the full table, and the nearest left", r2.tolist() == direct and not set(r2.tolist()) & {3, 17, 44})

    # leave_out_loss against a recount of every target, and the three readings on toys whose answer is known.
    # Rows at heights 0 ... 29 (four in each); the layer at height 29 is the top end, the one at height 0 the bottom end.
    hgt = np.repeat(np.arange(30.0), 4); Toy.X = np.stack([hgt, np.tile(np.arange(4.0), 30)] + [np.zeros(120)] * 4, axis=1)
    ends = {"bottom": hgt == 0, "top": hgt == 29}

    def toy(heights):
        Tt = np.stack([heights, rng.uniform(-0.5, 3.5, size=len(heights))] + [np.zeros(len(heights))] * 4, axis=1)
        s, row = chi_best(Toy, Tt, ("seat",))["seat"]; k = len(heights) // 4; out = {}
        for end, mask in list(ends.items()) + [("inner", hgt == 15)]:
            keep = np.flatnonzero(~mask)
            L = leave_out_loss(s, row, k, mask, lambda idx: chi_best(Toy, Tt[idx], ("seat",), keep)["seat"][0])
            order = np.argsort(s, kind="stable")[:k]; theta = s[order[-1]]
            s_all = chi_best(Toy, Tt, ("seat",), keep)["seat"][0]; L["recount"] = int(np.sum(s_all[order] > theta + 1e-9 * (1 + abs(theta))))
            out[end] = L
        return out
    even = toy(rng.uniform(-3, 32, size=12000))
    check("leave_out_loss equals a recount of every target, at the top, the bottom and an inner layer (%d, %d, %d)" % (even["top"]["lost"], even["bottom"]["lost"], even["inner"]["lost"]),
          all(even[e]["lost"] == even[e]["recount"] for e in even))
    check("toy, targets spread evenly and beyond both ends: an end layer costs about what any layer costs (ratios %.2f and %.2f): read as B" % (even["bottom"]["ratio_to_rows_share"], even["top"]["ratio_to_rows_share"]),
          verdict(even, True).startswith("B") and "bottom B, top B" in verdict(even, True))
    rising = toy(np.concatenate([rng.uniform(-3, 32, size=6000), rng.uniform(27.5, 31, size=6000)]))
    check("toy, half the targets crowded at and beyond the top end: the top is a lever (ratio %.2f): read as A at the top" % rising["top"]["ratio_to_rows_share"],
          verdict(rising, True).startswith("A") and "top A" in verdict(rising, True) and rising["top"]["lost"] == rising["top"]["recount"])
    falling = toy(rng.uniform(-3, 20, size=12000))
    check("toy, no target above height 20: the top end adds nothing (ratio %.2f): read as C at the top, B at the bottom" % falling["top"]["ratio_to_rows_share"],
          "top C" in verdict(falling, True) and "bottom B" in verdict(falling, True))

    # verdict: planted readings
    mk = lambda lost, kk=1000, r=1 / 15: {"lost": lost, "loss": lost / kk, "ci95": list(clopper(lost, kk)), "rows_share": r, "ratio_to_rows_share": (lost / kk) / r}
    v = verdict({"bottom": mk(60), "top": mk(300)}, True)
    check("verdict: 300 of 1000 lost at the top (ratio 4.5), 60 at the bottom: read as A, top A and bottom B", v.startswith("A") and "top A" in v and "bottom B" in v)
    check("verdict: 60 and 70 of 1000 lost (ratios about 1): read as B", verdict({"bottom": mk(60), "top": mk(70)}, True).startswith("B"))
    check("verdict: 10 and 20 of 1000 lost (ratios under 0.5): read as C", verdict({"bottom": mk(10), "top": mk(20)}, True).startswith("C"))
    check("verdict: 4 of 30 lost where the rows' share is 0.067 (ratio 2.0, but the interval reaches below the share): read as B, not A", verdict({"bottom": mk(2, 30), "top": mk(4, 30)}, True).startswith("B"))
    check("verdict: the control failed: read as NOT VALID whatever the counts", verdict({"bottom": mk(60), "top": mk(300)}, False).startswith("NOT VALID"))
    print("selftest: %s" % ("every check holds" if ok else "A CHECK FAILS")); print("selftest exit %d" % (0 if ok else 1)); sys.exit(0 if ok else 1)


def main():
    if "--selftest" in sys.argv: selftest()
    stage = sys.argv[sys.argv.index("--stage") + 1] if "--stage" in sys.argv else None
    if stage not in ("controls", "null"): sys.exit(__doc__)
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    lines = []

    def log(x):
        print(x, flush=True); lines.append(x)
    log("THE V1 CARD, stage %s; this script sha256 %s" % (stage, hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()[:16]))
    controls(log) if stage == "controls" else null(workers, log)
    (HERE / ("v1_%s_run.txt" % stage)).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
