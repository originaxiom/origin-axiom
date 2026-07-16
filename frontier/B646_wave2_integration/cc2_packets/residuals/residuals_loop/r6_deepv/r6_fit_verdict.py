"""
r6_fit_verdict.py -- R6 deep-V fits, controls, window discipline, and the locked verdict.

FIT DISCIPLINE (reused from V6, stated once):
  - Same window rule: fit window [lo, 160]; lo = smallest of LO_CANDIDATES whose pooled
    exponential-fit R^2 on the MAIN model's closed curve at the LARGEST available N for
    that V reaches R2_TARGET=0.995. If NO candidate reaches it, fall back to lo=80 and
    FLAG the window rule as unmet (that flag itself is evidence the log-linear regime
    is gone). The chosen window is applied uniformly to every model at that V.
  - Paired per-realization errors: a_C (position-averaged closed) and a_O (edge open)
    fitted PER REALIZATION, Delta = a_O - a_C formed per realization BEFORE averaging
    (lib_fit.fit_all_realizations; identical to V6).
  - Window-sensitivity sweep: Delta(lo) for every lo candidate; sign stability recorded.
  - Functional-form check: exponential vs power-law R^2 (pooled), both branches, plus
    a preregistered PLATEAU diagnostic for the localized regime: pooled local slope on
    the EARLY window [8,40] vs the LATE window [100,160]; |s_late/s_early| < 0.25 with
    finite curve values means the curve is saturating (neither exponential nor power).

LOCKED VERDICT RULES (preregistered, evaluated per (V, N), then overall):
  LOCALIZED-DIFFERENTIAL: some (V,N) has |Delta| >= 3*SEM, sign stable across the FULL
    lo sweep, AND Welch p<0.05 vs BOTH controls (V-scaled random shuffle, periodic),
    with the main closed curve still well-posed (pooled exp R^2 >= 0.95 on the chosen
    window, no plateau flag).
  REGIME-CHANGE: no (V,N) qualifies above AND at some (V,N) the main-model observable
    changed character (window rule unmet, pooled exp R^2 < 0.95, or plateau flag) --
    the report then DESCRIBES what replaces the exponential (saturation level, better
    functional form, gap/PR context) rather than quoting an ill-posed Delta.
  NULL-EXTENDS: observable well-posed everywhere, no qualifying differential.
Priority: LOCALIZED-DIFFERENTIAL > REGIME-CHANGE > NULL-EXTENDS (a demonstrable
differential requires well-posedness, so it can only win where the observable holds).
"""
import sys
import json
import numpy as np

sys.path.insert(0, "/Users/dri/oa-seat-cc2/seat-work/veins/v6_tension")
from lib_fit import (per_realization_curves, fit_all_realizations, mean_sem,   # noqa: E402
                      one_sample_t, welch_t, exp_fit, power_fit, linfit_r2)

MODELS = ["main", "random", "periodic"]
V_VALUES = (4, 8, 16)
N_VALUES = (610, 1597)
HI = 160
LO_CANDIDATES = [8, 12, 16, 20, 28, 40, 60, 80]
R2_TARGET = 0.995          # V6 window rule
R2_ILLPOSED = 0.95         # below this (pooled exp, chosen window): Delta ill-posed
PLATEAU_RATIO = 0.25       # |s_late/s_early| below this = saturating curve
EARLY = (8, 40)
LATE = (100, 160)
SIGMA_DISCOVERY = 3.0
P_CONTROL = 0.05


def load(model, V, N):
    try:
        d = np.load(f"outputs/raw_{model}_V{V}_{N}.npz")
    except FileNotFoundError:
        return None
    return d['ells'], d['closed_logabs'], d['open_logabs'], d['positions']


def pick_window(V, n_largest):
    dat = load("main", V, n_largest)
    ells, closed_logabs, open_logabs, _ = dat
    closed_curve, _ = per_realization_curves(closed_logabs, open_logabs)
    pooled_closed = closed_curve.mean(axis=0)
    chosen, scan = None, []
    for lo in LO_CANDIDATES:
        fit = exp_fit(ells, pooled_closed, lo, HI)
        scan.append({'lo': lo, 'hi': HI, 'r2': fit['r2'], 'rate': fit['rate']})
        if fit['r2'] >= R2_TARGET and chosen is None:
            chosen = lo
    rule_met = chosen is not None
    if chosen is None:
        chosen = LO_CANDIDATES[-1]
    return chosen, HI, scan, rule_met


def analyze(model, V, N, lo, hi):
    dat = load(model, V, N)
    if dat is None:
        return None
    ells, closed_logabs, open_logabs, positions = dat
    closed_curve, open_curve = per_realization_curves(closed_logabs, open_logabs)
    R = closed_curve.shape[0]
    fits = fit_all_realizations(ells, closed_curve, open_curve, lo, hi)
    aC = mean_sem(fits['aC']); aO = mean_sem(fits['aO']); dd = mean_sem(fits['delta'])
    t, p, dof = one_sample_t(fits['delta'], 0.0)

    pooled_closed = closed_curve.mean(axis=0)
    pooled_open = open_curve.mean(axis=0)
    ec = exp_fit(ells, pooled_closed, lo, hi); pc = power_fit(ells, pooled_closed, lo, hi)
    eo = exp_fit(ells, pooled_open, lo, hi); po = power_fit(ells, pooled_open, lo, hi)

    # plateau diagnostic (pooled closed & open)
    sC_early = exp_fit(ells, pooled_closed, *EARLY)['rate']
    sC_late = exp_fit(ells, pooled_closed, *LATE)['rate']
    sO_early = exp_fit(ells, pooled_open, *EARLY)['rate']
    sO_late = exp_fit(ells, pooled_open, *LATE)['rate']
    ratC = abs(sC_late / sC_early) if sC_early != 0 else np.inf
    ratO = abs(sO_late / sO_early) if sO_early != 0 else np.inf
    plateauC = bool(ratC < PLATEAU_RATIO)
    plateauO = bool(ratO < PLATEAU_RATIO)
    # saturation level estimate: mean pooled ln|W| over the last 5 ell points
    satC = float(pooled_closed[-5:].mean()); satO = float(pooled_open[-5:].mean())

    return {
        'model': model, 'V': V, 'N': N, 'R': R, 'lo': lo, 'hi': hi,
        'aC_mean': aC[0], 'aC_sem': aC[1], 'aO_mean': aO[0], 'aO_sem': aO[1],
        'delta_mean': dd[0], 'delta_sem': dd[1], 'delta_t': t, 'delta_p': p, 'dof': dof,
        'aC_r2_mean': float(fits['aC_r2'].mean()), 'aO_r2_mean': float(fits['aO_r2'].mean()),
        'closed_exp_r2': ec['r2'], 'closed_pow_r2': pc['r2'],
        'open_exp_r2': eo['r2'], 'open_pow_r2': po['r2'],
        'closed_better': 'exp' if ec['r2'] >= pc['r2'] else 'pow',
        'open_better': 'exp' if eo['r2'] >= po['r2'] else 'pow',
        'sC_early': sC_early, 'sC_late': sC_late, 'slope_ratio_C': float(ratC),
        'sO_early': sO_early, 'sO_late': sO_late, 'slope_ratio_O': float(ratO),
        'plateau_C': plateauC, 'plateau_O': plateauO,
        'sat_lnW_closed_tail': satC, 'sat_lnW_open_tail': satO,
        'per_realization': fits,
    }


def delta_window_scan(model, V, N, hi=HI):
    dat = load(model, V, N)
    if dat is None:
        return None
    ells, closed_logabs, open_logabs, _ = dat
    closed_curve, open_curve = per_realization_curves(closed_logabs, open_logabs)
    rows = []
    for lo in LO_CANDIDATES:
        fits = fit_all_realizations(ells, closed_curve, open_curve, lo, hi)
        m, s, _ = mean_sem(fits['delta'])
        rows.append({'lo': lo, 'delta_mean': m, 'delta_sem': s})
    return rows


def fm_ratio_curve(model, V, N):
    dat = load(model, V, N)
    if dat is None:
        return None
    ells, closed_logabs, open_logabs, _ = dat
    closed_curve, open_curve = per_realization_curves(closed_logabs, open_logabs)
    pooled_closed = closed_curve.mean(axis=0)
    pooled_open = open_curve.mean(axis=0)
    out = []
    for ell in ells[ells <= ells.max() // 2]:
        i2 = np.where(ells == 2 * ell)[0]
        if len(i2) == 0:
            continue
        logR = pooled_open[i2[0]] - 0.5 * pooled_closed[i2[0]]
        out.append((int(ell), float(np.exp(logR))))
    return out


def main():
    all_res, windows, scans, verdict_rows = {}, {}, {}, []

    for V in V_VALUES:
        n_avail = [N for N in N_VALUES if load("main", V, N) is not None]
        if not n_avail:
            print(f"V={V}: NO DATA (dropped by runtime guard)")
            continue
        n_largest = max(n_avail)
        lo, hi, scan, rule_met = pick_window(V, n_largest)
        windows[V] = {'lo': lo, 'hi': hi, 'rule_met': rule_met, 'picked_on_N': n_largest}
        scans[V] = scan
        print("=" * 96)
        print(f"V = {V}   (window picked on main N={n_largest}; V6 rule: pooled exp R^2 >= {R2_TARGET})")
        for row in scan:
            print(f"  window scan lo={row['lo']:3d}: R^2={row['r2']:.5f}  rate={row['rate']:+.5f}")
        print(f"  CHOSEN WINDOW ell in [{lo},{hi}]  (rule met: {rule_met}"
              f"{'' if rule_met else '  -> FLAG: no log-linear regime at R^2>=0.995'})")
        print()
        hdr = (f"  {'model':9s} {'N':>5} {'R':>2}  {'a_C':>9} {'+-':>7}  {'a_O':>9} {'+-':>7}  "
               f"{'Delta':>9} {'+-':>7} {'t':>7} {'p':>9}  {'R2exp/pow C':>13} {'R2exp/pow O':>13} "
               f"{'sl.ratio C/O':>13} {'plate':>5}")
        print(hdr)
        for N in n_avail:
            for model in MODELS:
                r = analyze(model, V, N, lo, hi)
                if r is None:
                    continue
                all_res[(model, V, N)] = r
                print(f"  {model:9s} {N:>5} {r['R']:>2}  "
                      f"{r['aC_mean']:>+9.5f} {r['aC_sem']:>7.5f}  "
                      f"{r['aO_mean']:>+9.5f} {r['aO_sem']:>7.5f}  "
                      f"{r['delta_mean']:>+9.5f} {r['delta_sem']:>7.5f} "
                      f"{r['delta_t']:>+7.2f} {r['delta_p']:>9.2e}  "
                      f"{r['closed_exp_r2']:.4f}/{r['closed_pow_r2']:.4f} "
                      f"{r['open_exp_r2']:.4f}/{r['open_pow_r2']:.4f} "
                      f"{r['slope_ratio_C']:>6.3f}/{r['slope_ratio_O']:>5.3f} "
                      f"{'CY' if r['plateau_C'] else 'C-'}{'OY' if r['plateau_O'] else 'O-'}")
        # window sensitivity of Delta
        print(f"\n  DELTA WINDOW-SENSITIVITY (V={V}; hi={HI} fixed; sign-stability check):")
        wscan = {}
        for N in n_avail:
            for model in MODELS:
                rows = delta_window_scan(model, V, N)
                if rows is None:
                    continue
                wscan[(model, N)] = rows
                line = "  ".join(f"lo={r['lo']:2d}:{r['delta_mean']:+.4f}" for r in rows)
                signs = set(np.sign(r['delta_mean']) for r in rows)
                stable = len(signs) == 1
                print(f"    {model:9s} N={N:5d}: {line}   sign-stable={stable}")
                wscan[(model, N, 'stable')] = stable
        # cross-model Welch on per-realization Delta
        print(f"\n  CONTROL COMPARISON (Welch t on per-realization Delta, V={V}):")
        cross = {}
        for N in n_avail:
            md = all_res[("main", V, N)]['per_realization']['delta']
            for ctrl in ("random", "periodic"):
                key = (ctrl, V, N)
                if key not in all_res:
                    continue
                cd = all_res[key]['per_realization']['delta']
                t, p = welch_t(md, cd)
                cross[(N, ctrl)] = {'t': t, 'p': p}
                print(f"    N={N:5d} main vs {ctrl:9s}: Delta_main={md.mean():+.5f} "
                      f"Delta_ctrl={cd.mean():+.5f}  Welch t={t:+.2f} p={p:.2e}")
        # FM ratio
        print(f"\n  FREDENHAGEN-MARCU R(ell)=|open(2l)|/sqrt|closed(2l)| (pooled, V={V}):")
        for N in n_avail:
            for model in MODELS:
                fm = fm_ratio_curve(model, V, N)
                if fm is None:
                    continue
                e_arr = np.array([e for e, _ in fm], dtype=float)
                r_arr = np.array([v for _, v in fm])
                slope, _, r2, _ = linfit_r2(e_arr, r_arr)
                print(f"    {model:9s} N={N:5d}: R({int(e_arr[0])})={r_arr[0]:.4f} "
                      f"R({int(e_arr[len(e_arr)//2])})={r_arr[len(e_arr)//2]:.4f} "
                      f"R({int(e_arr[-1])})={r_arr[-1]:.4f}  trend slope={slope:+.2e} (R^2={r2:.3f})")
        # verdict bookkeeping per (V,N)
        for N in n_avail:
            r = all_res[("main", V, N)]
            sigma = abs(r['delta_mean']) / r['delta_sem'] if r['delta_sem'] > 0 else 0.0
            stable = wscan.get(("main", N, 'stable'), False)
            p_rand = cross.get((N, "random"), {}).get('p', 1.0)
            p_per = cross.get((N, "periodic"), {}).get('p', 1.0)
            well_posed = (r['closed_exp_r2'] >= R2_ILLPOSED and not r['plateau_C']
                          and windows[V]['rule_met'])
            qualifies = (well_posed and sigma >= SIGMA_DISCOVERY and stable
                         and p_rand < P_CONTROL and p_per < P_CONTROL)
            regime_flag = not well_posed
            verdict_rows.append({
                'V': V, 'N': N, 'sigma': float(sigma), 'sign_stable': bool(stable),
                'p_vs_random': float(p_rand), 'p_vs_periodic': float(p_per),
                'well_posed': bool(well_posed), 'window_rule_met': windows[V]['rule_met'],
                'closed_exp_r2': r['closed_exp_r2'], 'plateau_C': r['plateau_C'],
                'closed_better': r['closed_better'], 'open_better': r['open_better'],
                'LOCALIZED_DIFFERENTIAL': bool(qualifies), 'REGIME_CHANGE_flag': bool(regime_flag),
                'delta_mean': r['delta_mean'], 'delta_sem': r['delta_sem'],
            })
        print()

    # ---------------- overall locked verdict ----------------
    print("=" * 96)
    print("PER-(V,N) VERDICT TABLE (locked criteria):")
    print(f"  {'V':>3} {'N':>5} {'|Delta|/SEM':>11} {'sign-stable':>11} {'p_vs_rand':>10} "
          f"{'p_vs_per':>10} {'well-posed':>10} {'LOC-DIFF':>8} {'REGIME':>7}")
    for row in verdict_rows:
        print(f"  {row['V']:>3} {row['N']:>5} {row['sigma']:>11.2f} "
              f"{str(row['sign_stable']):>11} {row['p_vs_random']:>10.2e} "
              f"{row['p_vs_periodic']:>10.2e} {str(row['well_posed']):>10} "
              f"{str(row['LOCALIZED_DIFFERENTIAL']):>8} {str(row['REGIME_CHANGE_flag']):>7}")

    any_locdiff = any(r['LOCALIZED_DIFFERENTIAL'] for r in verdict_rows)
    any_regime = any(r['REGIME_CHANGE_flag'] for r in verdict_rows)
    if any_locdiff:
        verdict = "LOCALIZED-DIFFERENTIAL"
    elif any_regime:
        verdict = "REGIME-CHANGE"
    else:
        verdict = "NULL-EXTENDS"
    print(f"\nOVERALL LOCKED VERDICT: {verdict}")

    # serialize
    def jsonify(r):
        rr = {k: v for k, v in r.items() if k != 'per_realization'}
        rr['per_realization'] = {k: v.tolist() for k, v in r['per_realization'].items()}
        return rr

    out = {
        'windows': {str(V): windows[V] for V in windows},
        'window_scans': {str(V): scans[V] for V in scans},
        'results': {f"{m}_V{V}_{N}": jsonify(all_res[(m, V, N)])
                    for (m, V, N) in all_res},
        'verdict_rows': verdict_rows,
        'verdict': verdict,
    }
    with open("outputs/fit_summary.json", "w") as f:
        json.dump(out, f, indent=2)
    print("wrote outputs/fit_summary.json")


if __name__ == "__main__":
    main()
