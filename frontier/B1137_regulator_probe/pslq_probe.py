"""R48-3 THE REGULATOR PROBE -- main driver: STEP 3 (real-target grid) + STEP 4 (matched null).

Grid (primary, prereg-mandated): 18 SM targets x D in {1,2,3} x H in {1e2,1e3,1e4,1e6}, FULL
pruned 25-element regulator/constant basis (single combined vector, per the sealed sec C).
Null: N surrogates x D=3 (conservative proxy for D=1,2 -- see NOTE below) x same 4 H.

Precision policy (declared choice): dps(H) = max(100, ceil(1.3*n_dim*log10(H)) + 40), n_dim~29 ==
comfortably >=60 (prereg floor) and scaled to the PSLQ-theoretic requirement for a meaningful
search/certificate at that height (E25 coefficient-height-awareness extended to precision).
maxsteps=4000 uniformly (benchmarked: 21-48s/cell worst case across the whole H range at n~29).
V is represented at its OWN trustworthy precision (JSON 'digits' field, truncated) inside the
search vector (we do not manufacture precision the measurement doesn't have); the final within-1
sigma check uses the full central value + rel_unc (the physical comparison).
"""
import sys, os, time, json, math, argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from mpmath import mp, mpf, pslq, nstr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import basis as basismod
import targets as targetsmod
import surrogates as surmod
import verify as verifymod

H_LIST = [100, 1000, 10000, 1000000]
D_LIST = [1, 2, 3]
MAXSTEPS = 4000
N_DIM_APPROX = 29

def dps_for_H(H):
    d = int(math.ceil(1.3 * N_DIM_APPROX * math.log10(H))) + 40
    return max(100, d)

def run_cell(V_str, digits, rel_unc, name, D, H):
    dps = dps_for_H(H)
    b, forms, R = basismod.build_pruned_basis(dps=dps)
    basis_keys = forms['FULL']
    mp.dps = dps + 25
    d_use = max(int(digits), 1)
    V_full = mpf(V_str)
    V_trunc_str = nstr(V_full, d_use)
    V = mpf(V_trunc_str)
    vec = [mpf(1)]
    for k in range(1, D + 1):
        vec.append(V ** k)
    basis_vals = [mp.mpf(b[kk]) for kk in basis_keys]
    vec += basis_vals
    n_dim = len(vec)
    tol = mpf(10) ** (-(dps - 10))
    t0 = time.time()
    rel = pslq(vec, maxcoeff=int(H), maxsteps=MAXSTEPS, tol=tol)
    dt = time.time() - t0
    result = {'name': name, 'D': D, 'H': H, 'dps': dps, 'digits': digits, 'n_dim': n_dim,
              'V_trunc': V_trunc_str, 'time': dt, 'found': False}
    if rel is None or all(c == 0 for c in rel):
        return result
    coeffs = [int(c) for c in rel]
    result['found'] = True
    result['coeffs'] = coeffs
    if not verifymod.involves_V(coeffs, D):
        result['involves_V'] = False
        return result
    result['involves_V'] = True
    # V is a TERMINATING DECIMAL by construction (nstr-truncated to its digit budget), so it is
    # ALWAYS trivially rational -- PSLQ will essentially always find c0 + c1*V (+0*regulators) = 0
    # for low-digit targets (e.g. delta_CP digits=0 -> "4.0", m_s/m_d digits=1 -> "20"). That says
    # nothing about the regulators and must be rejected here, not just left to the (weaker)
    # downstream checks -- found empirically 2026-08-22 (16/117 "found" cells slipped through the
    # OLD pipeline's exact/within-1sigma checks precisely because a V-alone tautology reproduces
    # itself exactly at any precision and trivially sits inside its own sigma).
    if not verifymod.involves_regulator(coeffs, D):
        result['involves_regulator'] = False
        return result
    result['involves_regulator'] = True
    resid = sum(mpf(coeffs[i]) * vec[i] for i in range(len(vec)))
    maxh_actual = max(abs(c) for c in coeffs)
    ok_h, slack = verifymod.height_aware_ok(resid, dps, maxh_actual, n_dim)
    result.update({'residual': nstr(resid, 6), 'coeff_height': maxh_actual,
                    'height_aware_ok': ok_h, 'slack_digits': slack})
    if not ok_h:
        return result

    def get_vec_at_dps(dps_hi, D_):
        # IMPORTANT: re-parse V fresh from its exact truncated-decimal STRING at the boosted
        # precision, rather than reusing the mpf object created at the (lower) search precision --
        # reusing a stale low-precision mpf silently caps the achievable residual at ~its original
        # precision regardless of how much the regulators are boosted, corrupting the stability
        # verdict (found empirically: caused false "unstable" reads on the V-alone tautologies
        # above, for the wrong reason -- V has a fixed TRUE precision floor, but re-parsing its own
        # exact decimal string is still lossless up to that floor and must be done fresh each time).
        b2, forms2, R2 = basismod.build_pruned_basis(dps=dps_hi)
        Vhi = mpf(V_trunc_str)
        vv = [mpf(1)]
        for k in range(1, D_ + 1):
            vv.append(Vhi ** k)
        vv += [mp.mpf(b2[kk]) for kk in basis_keys]
        return vv

    stable, resid_hi_digits = verifymod.exact_reverify(coeffs, basis_keys, dps, get_vec_at_dps, D)
    result.update({'exact_stable': stable, 'resid_hi_digits': resid_hi_digits})
    if not stable:
        return result

    dps_hi = dps + verifymod.BOOST
    b3, forms3, R3 = basismod.build_pruned_basis(dps=dps_hi)
    K_reg_hi = sum(mp.mpf(coeffs[D + 1 + j]) * mp.mpf(b3[basis_keys[j]]) for j in range(len(basis_keys)))
    roots = verifymod.solve_for_V_roots(coeffs, D, K_reg_hi, dps_hi)
    ok_sigma, best_root, sigma_dev = verifymod.within_1sigma(roots, V_full, rel_unc)
    result.update({'within_1sigma': ok_sigma,
                    'best_root': nstr(best_root, dps_hi) if best_root is not None else None,
                    'sigma_dev': sigma_dev})
    result['ADMITTED'] = bool(ok_h and stable and ok_sigma)
    return result

def _worker(args):
    return run_cell(*args)

def real_grid_tasks(targets):
    tasks = []
    for t in targets:
        for D in D_LIST:
            for H in H_LIST:
                tasks.append((t['value'], t['digits'], t['rel_unc'], t['name'], D, H))
    return tasks

def null_tasks(surrogates, D_for_null=3):
    tasks = []
    for i, s in enumerate(surrogates):
        for H in H_LIST:
            tasks.append((s['value'], s['digits'], s['rel_unc'], f"NULL_{i}", D_for_null, H))
    return tasks

def run_pool(tasks, out_path, workers=16, label='cells'):
    n = len(tasks)
    done = 0
    t_start = time.time()
    # 'w', not 'a': there is no resume logic here, so append made every re-run TRIPLE-COUNT
    # into the same grid -- this bench's real_grid.jsonl held 648 rows (3 x 216) and the
    # aggregate then re-derived M_grid_cells = 432 and halved the Sidak alpha off duplicate
    # multiplicity. Caught 2026-08-29 in the slow lane's first full run (B1207).
    with open(out_path, 'w') as f:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(_worker, task): task for task in tasks}
            for fut in as_completed(futs):
                r = fut.result()
                f.write(json.dumps(r) + '\n')
                f.flush()
                done += 1
                if done % 10 == 0 or done == n:
                    el = time.time() - t_start
                    print(f"[{label}] {done}/{n}  elapsed={el:.0f}s  rate={done/el:.3f}/s  "
                          f"eta={(n-done)/(done/el) if done else 0:.0f}s", flush=True)
    return out_path

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['real', 'null', 'bothtest'])
    ap.add_argument('--n-surrogates', type=int, default=500)
    ap.add_argument('--seed', type=int, default=17)
    ap.add_argument('--workers', type=int, default=16)
    ap.add_argument('--out', default=None)
    ap.add_argument('--limit', type=int, default=None)
    args = ap.parse_args()

    targets, sha = targetsmod.load_targets()
    print(f"targets: {len(targets)}  sha256={sha}")

    if args.mode == 'real':
        tasks = real_grid_tasks(targets)
        if args.limit: tasks = tasks[:args.limit]
        out = args.out or 'results/real_grid.jsonl'
        print(f"REAL grid: {len(tasks)} cells -> {out}")
        run_pool(tasks, out, workers=args.workers, label='real')
    elif args.mode == 'null':
        dps0 = dps_for_H(100)
        b, forms, R = basismod.build_pruned_basis(dps=dps0)
        surs = surmod.make_n_surrogates(args.n_surrogates, b, forms['FULL'], targets, dps=dps0, seed=args.seed)
        json.dump([{'name': s['name'], 'value': s['value'], 'digits': s['digits'], 'rel_unc': s['rel_unc']}
                   for s in surs], open('results/surrogates_used.json', 'w'), indent=1)
        tasks = null_tasks(surs, D_for_null=3)
        if args.limit: tasks = tasks[:args.limit]
        out = args.out or 'results/null_grid.jsonl'
        print(f"NULL grid: {len(surs)} surrogates x {len(H_LIST)} H = {len(tasks)} cells -> {out}")
        run_pool(tasks, out, workers=args.workers, label='null')
    elif args.mode == 'bothtest':
        tasks = real_grid_tasks(targets)[:4]
        run_pool(tasks, 'results/test.jsonl', workers=4, label='test')
