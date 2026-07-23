"""
r6_sweep.py -- R6 deep-V sweep: V in {4, 8, 16} (on-site spread comparable to /
exceeding the bandwidth 4t: the localized regime), sigma-word chains at
N in {610, 1597}, half filling, OBC.

REUSED VERBATIM from the calibrated V6 pipeline (veins/v6_tension): lib_chain
(words, charges, Hamiltonians), lib_observables (FCS determinant strings), and
step2_run_sweep.run_main_like / ELLS / N_POS (the measurement loop: closed strings
at 20 bulk positions x ell grid 4..160 step 2, one edge-anchored open string per
realization). Nothing about the observable pipeline is rewritten here; only the
V values, the job list, and the localization diagnostics (participation ratio,
Fermi-gap) are new.

MODELS per V (same controls as V6, V-scaled):
  main     : sigma-word, on-site V*charge/11, R=20 realizations (non-overlapping
             length-N windows of the long sigma-word; r=0 = repo-convention word).
  random   : SAME letter multiset, ONE global shuffle with seed=1 (identical
             construction to V6), at the same V. R=20.
  periodic : (abAB)^k at the same V, R=4 (the 4 inequivalent phases).
(The V=0 control is not re-run: it is V-independent and was banked in V6; the gate
 step re-verified the V=0 analytics.)

LOCALIZATION SANITY (preregistered): participation ratio PR = 1/sum_i |psi_i|^4 of
the 20 mid-spectrum eigenstates (indices N/2-10 .. N/2+9, i.e. the states at the
half-filling Fermi index), main word realization 0, for V in {0, 1, 4, 8, 16}.
PR should DROP with V if the deep regime is really localized. Also recorded: the
Fermi gap E[npart]-E[npart-1] vs the mean level spacing (insulator-vs-metal flag),
and the letter frequencies / cumulative band filling (where half filling falls).

RUNTIME GUARD (~25 min total cell budget): jobs are ordered so (V=16, N=1597) runs
LAST; if elapsed sweep time exceeds GUARD_SECONDS when it is reached, it is dropped
and the drop is recorded in the manifest and stdout.
"""
import sys
import json
import time
import numpy as np

sys.path.insert(0, "/Users/dri/oa-seat-cc2/seat-work/veins/v6_tension")
from lib_chain import (sigma_prefix, periodic_word, charges_of,        # noqa: E402
                        build_H_bands, LETTERS)
from scipy.linalg import eigh_tridiagonal                              # noqa: E402
import step2_run_sweep as s2                                           # noqa: E402

V_VALUES = (4.0, 8.0, 16.0)
N_VALUES = (610, 1597)
R_MAIN = 20
R_PERIODIC = 4
SEED_RANDOM = 1
GUARD_SECONDS = 1150          # drop (V=16, N=1597) if sweep already past this
PR_V_LIST = (0.0, 1.0, 4.0, 8.0, 16.0)   # includes extended-regime baselines


# ---------------- word construction (identical to V6 step2 conventions) ----------
long_main_cache = {}
long_random_cache = {}


def get_long_main(N):
    if N not in long_main_cache:
        long_main_cache[N] = sigma_prefix(R_MAIN * N + 8)
    return long_main_cache[N]


def get_long_random(N):
    if N not in long_random_cache:
        base = get_long_main(N)[:R_MAIN * N]
        arr = np.array(list(base))
        rng = np.random.default_rng(SEED_RANDOM)
        rng.shuffle(arr)
        long_random_cache[N] = ''.join(arr.tolist())
    return long_random_cache[N]


def word_main(N, r):
    w = get_long_main(N)
    return w[r * N:(r + 1) * N]


def word_random(N, r):
    w = get_long_random(N)
    return w[r * N:(r + 1) * N]


def word_periodic(N, r):
    return periodic_word(N, offset=r)


# ---------------- localization / spectrum diagnostics ----------------------------
def participation_ratio(vecs):
    """vecs: (N, k) eigenvector columns. PR = 1/sum psi^4 per column."""
    return 1.0 / np.sum(vecs ** 4, axis=0)


def spectrum_diagnostics(word, V, n_mid=20):
    """Full-spectrum + mid-spectrum diagnostics for one word at one V."""
    N = len(word)
    diag, offdiag = build_H_bands(word, V=V)
    evals = eigh_tridiagonal(diag, offdiag, eigvals_only=True)
    npart = N // 2
    gap = float(evals[npart] - evals[npart - 1])
    mean_spacing = float((evals[-1] - evals[0]) / (N - 1))
    mid = N // 2
    lo_i, hi_i = mid - n_mid // 2, mid + n_mid // 2 - 1
    _, vecs = eigh_tridiagonal(diag, offdiag, select='i', select_range=(lo_i, hi_i))
    pr = participation_ratio(vecs)
    return {
        'N': N, 'V': V, 'npart': npart,
        'E_min': float(evals[0]), 'E_max': float(evals[-1]),
        'fermi_gap': gap, 'mean_spacing': mean_spacing,
        'gap_over_spacing': gap / mean_spacing,
        'mid_states': [int(lo_i), int(hi_i)],
        'PR_mean': float(pr.mean()), 'PR_sd': float(pr.std(ddof=1)),
        'PR_min': float(pr.min()), 'PR_max': float(pr.max()),
    }


def main():
    t_start = time.time()
    print("=" * 78)
    print("R6 SWEEP: deep-V localized regime, V in {4,8,16}, N in {610,1597}")
    print(f"ell grid: {s2.ELLS[0]}..{s2.ELLS[-1]} step 2 ({len(s2.ELLS)} pts); "
          f"n_pos={s2.N_POS}; R_main={R_MAIN}; R_periodic={R_PERIODIC}; seed_random={SEED_RANDOM}")
    print("engine: veins/v6_tension step2_run_sweep.run_main_like (imported, not rewritten)")
    print("=" * 78)

    # ---- letter frequencies & band-filling context (main word, realization 0) ----
    print("\nBAND-FILLING CONTEXT (main word r=0): charges a=1, b=3, A=6, B=7; bands fill")
    print("in charge order at deep V; cumulative letter frequency vs half filling 0.5:")
    freq_info = {}
    for N in N_VALUES:
        w = word_main(N, 0)
        freqs = {c: w.count(c) / N for c in LETTERS}
        cum = np.cumsum([freqs['a'], freqs['b'], freqs['A'], freqs['B']])
        freq_info[N] = {'freqs': freqs, 'cumulative_aAbB_chargeorder': cum.tolist()}
        print(f"  N={N}: f_a={freqs['a']:.4f} f_b={freqs['b']:.4f} f_A={freqs['A']:.4f} "
              f"f_B={freqs['B']:.4f} | cumulative (a,b,A,B charge order): "
              f"{cum[0]:.4f}, {cum[1]:.4f}, {cum[2]:.4f}, {cum[3]:.4f}  "
              f"[half filling 0.5 falls in the "
              f"{'a' if 0.5 <= cum[0] else 'b' if 0.5 <= cum[1] else 'A' if 0.5 <= cum[2] else 'B'}-band]")

    # ---- localization sanity: PR + Fermi gap vs V (BEFORE the string sweep) ------
    print("\nLOCALIZATION SANITY (main word r=0; 20 mid-spectrum states at the Fermi index):")
    print(f"{'N':>6} {'V':>6} {'PR_mean':>10} {'PR_sd':>9} {'PR_min':>9} {'PR_max':>9} "
          f"{'fermi_gap':>11} {'gap/spacing':>12}")
    diagnostics = []
    for N in N_VALUES:
        w = word_main(N, 0)
        for V in PR_V_LIST:
            d = spectrum_diagnostics(w, V)
            diagnostics.append(d)
            print(f"{N:>6} {V:>6.1f} {d['PR_mean']:>10.2f} {d['PR_sd']:>9.2f} "
                  f"{d['PR_min']:>9.2f} {d['PR_max']:>9.2f} {d['fermi_gap']:>11.5f} "
                  f"{d['gap_over_spacing']:>12.2f}")
    # controls' localization at deep V (context for control comparability):
    print("\nLOCALIZATION of CONTROLS (r=0 word, V=8 shown; random should localize too, "
          "periodic stays Bloch-extended within its bands):")
    ctrl_diag = []
    for N in (1597,):
        for label, w in (("random", word_random(N, 0)), ("periodic", word_periodic(N, 0))):
            for V in (4.0, 8.0, 16.0):
                d = spectrum_diagnostics(w, V)
                d['model'] = label
                ctrl_diag.append(d)
                print(f"  {label:9s} N={N} V={V:4.1f}: PR_mean={d['PR_mean']:8.2f}  "
                      f"fermi_gap={d['fermi_gap']:.5f}  gap/spacing={d['gap_over_spacing']:.2f}")

    # ---- the string sweep ---------------------------------------------------------
    print("\nSTRING SWEEP (closed: 20 bulk positions; open: edge-anchored; per realization):")
    jobs = []
    for V in V_VALUES:
        for N in N_VALUES:
            jobs.append((V, N))
    # ensure (16,1597) is last (it is, given the loop order above, but make it explicit)
    jobs.sort(key=lambda vn: (vn[0] == 16.0 and vn[1] == 1597, vn[0], vn[1]))

    manifest = {"ells": s2.ELLS.tolist(), "n_pos": s2.N_POS, "r_main": R_MAIN,
                "r_periodic": R_PERIODIC, "seed_random": SEED_RANDOM,
                "v_values": list(V_VALUES), "n_values": list(N_VALUES),
                "guard_seconds": GUARD_SECONDS,
                "freq_info": {str(k): v for k, v in freq_info.items()},
                "localization_main": diagnostics, "localization_controls": ctrl_diag,
                "runs": [], "dropped": []}

    model_specs = [("main", word_main, R_MAIN), ("random", word_random, R_MAIN),
                   ("periodic", word_periodic, R_PERIODIC)]

    for V, N in jobs:
        elapsed = time.time() - t_start
        if V == 16.0 and N == 1597 and elapsed > GUARD_SECONDS:
            note = (f"DROPPED (V=16, N=1597): elapsed sweep time {elapsed:.0f}s > "
                    f"guard {GUARD_SECONDS}s (preregistered runtime guard)")
            print(note, flush=True)
            manifest["dropped"].append({"V": V, "N": N, "elapsed": elapsed})
            continue
        for model, word_fn, R in model_specs:
            t0 = time.time()
            closed_all, open_all, positions = s2.run_main_like(
                N, seed_word_fn=word_fn, R=R, reuse_flat=False, V=V)
            dt = time.time() - t0
            nonfinite = int((~np.isfinite(closed_all)).sum() + (~np.isfinite(open_all)).sum())
            fname = f"outputs/raw_{model}_V{int(V)}_{N}.npz"
            np.savez_compressed(fname, ells=s2.ELLS, closed_logabs=closed_all,
                                 open_logabs=open_all, positions=positions)
            print(f"[{model:9s} V={V:4.1f} N={N:5d}] R={R:2d}  wrote {fname}  "
                  f"({dt:.1f}s, nonfinite={nonfinite})", flush=True)
            manifest["runs"].append({"model": model, "V": V, "N": N, "R": R,
                                      "seconds": dt, "file": fname,
                                      "nonfinite": nonfinite})

    manifest["total_seconds"] = time.time() - t_start
    with open("outputs/sweep_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nDONE. total {manifest['total_seconds']:.1f}s. wrote outputs/sweep_manifest.json")


if __name__ == "__main__":
    main()
