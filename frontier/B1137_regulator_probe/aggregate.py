"""STEP 5 -- aggregate real_grid.jsonl + null_grid.jsonl into the final per-target table,
base-rate table, and HIT/DISJOINT/FLOOR verdict, with Sidak look-elsewhere correction.
"""
import json, math, sys, os

def load_jsonl(path):
    rows = []
    # De-duplicate by cell identity (name, D, H). The writer used to append, so grids produced
    # before B1207 can carry the same cell many times; counting a cell twice inflates
    # M_grid_cells and deflates the Sidak alpha off multiplicity that was never tested.
    seen = set()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                r = json.loads(line)
                k = (r.get('name'), r.get('D'), r.get('H'))
                if k in seen:
                    continue
                seen.add(k)
                rows.append(r)
    return rows

def involves_regulator_from_row(r):
    """Defense-in-depth: recompute the involves-regulator gate directly from saved coeffs,
    rather than trusting a stored ADMITTED flag -- catches the V-alone-tautology artifact
    (found 2026-08-22: a terminating-decimal V is always trivially "rational" on its own,
    e.g. delta_CP digits=0 truncates to exactly 4.0, m_s/m_d digits=1 to exactly 20; PSLQ
    then trivially returns c0+c1*V=0 with EVERY regulator coefficient zero -- uninformative
    about the object, and must never count as admitted regardless of what a stale run's
    ADMITTED field said)."""
    coeffs = r.get('coeffs')
    D = r.get('D')
    if not coeffs or D is None:
        return False
    return any(c != 0 for c in coeffs[1 + D:])

def really_admitted(r):
    return bool(r.get('ADMITTED') and r.get('involves_V') and involves_regulator_from_row(r))

def sidak_alpha_cell(alpha_family, M):
    return 1 - (1 - alpha_family) ** (1.0 / M)

def main(real_path, null_path, targets_json, alpha_family=0.05):
    real = load_jsonl(real_path)
    null = load_jsonl(null_path) if null_path and __import__('os').path.exists(null_path) else []
    targets = json.load(open(targets_json))
    target_names = [t['name'] for t in targets]

    M = len(real)
    alpha_cell = sidak_alpha_cell(alpha_family, max(M, 1))

    # null base rate per H (D=3 proxy applied to all D)
    null_by_H = {}
    for h in sorted(set(r['H'] for r in null)) if null else []:
        cells = [r for r in null if r['H'] == h]
        n = len(cells)
        k_admitted = sum(1 for r in cells if really_admitted(r))
        k_found_involvesV = sum(1 for r in cells if r.get('found') and r.get('involves_V')
                                 and involves_regulator_from_row(r))
        null_by_H[h] = {'n': n, 'k_admitted': k_admitted, 'rate_admitted': k_admitted / n if n else None,
                         'k_found_involvesV': k_found_involvesV,
                         'rate_found_involvesV': k_found_involvesV / n if n else None}

    # per-target rollup
    per_target = {name: {'cells_tested': 0, 'raw_found': 0, 'involves_V': 0, 'involves_regulator': 0,
                          'height_ok': 0, 'exact_stable': 0, 'within_1sigma': 0, 'admitted_cells': []}
                  for name in target_names}
    for r in real:
        pt = per_target.get(r['name'])
        if pt is None:
            continue
        pt['cells_tested'] += 1
        if r.get('found'):
            pt['raw_found'] += 1
        if r.get('involves_V'):
            pt['involves_V'] += 1
        if r.get('involves_V') and involves_regulator_from_row(r):
            pt['involves_regulator'] += 1
        if r.get('height_aware_ok'):
            pt['height_ok'] += 1
        if r.get('exact_stable'):
            pt['exact_stable'] += 1
        if r.get('within_1sigma'):
            pt['within_1sigma'] += 1
        if really_admitted(r):
            pt['admitted_cells'].append(r)

    report_rows = []
    any_surviving_hit = False
    for name in target_names:
        pt = per_target[name]
        best = None
        verdict = 'NONE'
        for cand in pt['admitted_cells']:
            nb = null_by_H.get(cand['H'], {'rate_admitted': None, 'n': 0})
            passes_baserate = (nb['rate_admitted'] is not None and nb['rate_admitted'] <= alpha_cell)
            cand['null_rate_at_H'] = nb['rate_admitted']
            cand['null_n_at_H'] = nb['n']
            cand['alpha_cell_sidak'] = alpha_cell
            cand['passes_baserate'] = passes_baserate
            if passes_baserate:
                verdict = 'HIT-CANDIDATE'
                any_surviving_hit = True
                best = cand
                break
            elif best is None:
                best = cand
        if pt['admitted_cells'] and verdict == 'NONE':
            verdict = 'ADMITTED-BUT-BASERATE-FAILS'
        report_rows.append({'target': name, 'cells_tested': pt['cells_tested'],
                             'raw_found': pt['raw_found'], 'involves_V': pt['involves_V'],
                             'involves_regulator': pt['involves_regulator'],
                             'height_ok': pt['height_ok'], 'exact_stable': pt['exact_stable'],
                             'within_1sigma': pt['within_1sigma'], 'verdict': verdict,
                             'best_candidate': best})

    overall = 'HIT' if any_surviving_hit else ('DISJOINT' if M > 0 else 'FLOOR')
    out = {'M_grid_cells': M, 'alpha_family': alpha_family, 'alpha_cell_sidak': alpha_cell,
           'null_by_H': null_by_H, 'per_target': report_rows, 'overall_verdict': overall,
           'H_LIST': sorted(set(r['H'] for r in real)), 'D_LIST': sorted(set(r['D'] for r in real)),
           'dps_by_H': {r['H']: r['dps'] for r in real},
           'maxsteps': 4000}
    return out

if __name__ == '__main__':
    real_path = sys.argv[1] if len(sys.argv) > 1 else 'results/real_grid.jsonl'
    null_path = sys.argv[2] if len(sys.argv) > 2 else 'results/null_grid.jsonl'
    targets_json = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'frontier', 'B743_rung1_widened', 'pdg_targets.json')
    out = main(real_path, null_path, targets_json)
    json.dump(out, open('results/final_report.json', 'w'), indent=1, default=str)
    print(f"M grid cells = {out['M_grid_cells']}")
    print(f"alpha_cell (Sidak, family=0.05) = {out['alpha_cell_sidak']:.6f}")
    print(f"overall verdict = {out['overall_verdict']}")
    print()
    print("null base rates by H:")
    for h, v in out['null_by_H'].items():
        print(f"  H={h}: n={v['n']}  rate_admitted={v['rate_admitted']}  rate_found&involvesV={v['rate_found_involvesV']}")
    print()
    for row in out['per_target']:
        print(f"{row['target']:28s} tested={row['cells_tested']:3d} found={row['raw_found']:3d} "
              f"involvesV={row['involves_V']:3d} heightOK={row['height_ok']:3d} "
              f"stable={row['exact_stable']:3d} sigma={row['within_1sigma']:3d}  verdict={row['verdict']}")
