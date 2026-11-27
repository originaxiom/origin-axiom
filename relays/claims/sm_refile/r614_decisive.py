"""Decisive wrapper for the SM seat's P-614 card (the discrete symmetry surviving 27 -> SM, on the root).

Runs the seat's DISCLOSED POST-HOC script relays/sm_r614/posthoc_run.py UNCHANGED. The sealed relays/sm_r614/run.py
stopped at its block-A assertion because of a colour-label bug (its flip of the colour convention also flipped the
singlets); posthoc_run.py is run.py with that one line fixed, disclosed on relays/SM_R614_THE_DISCRETE_REMNANT.md.

The sealed folder is copied to a fresh temporary directory, the script runs there with the repository root (the
parent holding frontier/ and GENESIS.md) as its main-checkout argument, and its JSON output is read back. Nothing is
written into the repository. Run from the repo root:  python3 relays/claims/sm_refile/r614_decisive.py
Exit 0 when the run completes and the decisive values come out; 1 otherwise.
"""
import sys, os, json, shutil, tempfile, subprocess, pathlib


def find_root():
    for s in (pathlib.Path(__file__).resolve().parent, pathlib.Path.cwd()):
        for d in (s, *s.parents):
            if (d / 'frontier').is_dir() and (d / 'GENESIS.md').is_file() and (d / 'relays' / 'sm_r614').is_dir():
                return d
    return None


def main():
    root = find_root()
    if root is None:
        print('FAILED: repository root not found'); return 1
    tmp = tempfile.mkdtemp(prefix='r614_')
    try:
        work = os.path.join(tmp, 'sm_r614')
        shutil.copytree(str(root / 'relays' / 'sm_r614'), work)
        for f in ('r614_results_posthoc.json', 'r614_results.json'):
            p = os.path.join(work, f)
            if os.path.exists(p): os.remove(p)
        r = subprocess.run([sys.executable, '-B', os.path.join(work, 'posthoc_run.py'), str(root)], cwd=work,
                           capture_output=True, text=True)
        out = os.path.join(work, 'r614_results_posthoc.json')
        if r.returncode != 0 or not os.path.exists(out):
            print('FAILED: the script exited %d: %s' % (r.returncode, (r.stderr.strip().splitlines() or [''])[-1]))
            return 1
        d = json.load(open(out))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    B, E, G, M = d['B'], d['E'], d['G'], d['M']
    lines = [
        'A1 SM embeddings on main weights matching B1303: %d of %d' % (d['A1']['matched'], d['A1']['tried']),
        'B eta per multiplet: ' + ', '.join('%s %s' % kv for kv in B['eta_per_multiplet'].items()),
        'B eta equal on nu^c and N: %s; beta.eta = %s; eta in coroot lattice: %s'
        % (B['equal_on_the_two_singlets'], B['beta_dot_eta'], B['eta_in_coroot_lattice']),
    ]
    for k, v in E.items():
        lines.append('%s: stabiliser dim %d rank %d, SM inside %s, torus components %s, matter parity %s'
                     % (k, v['stab_dim'], v['stab_rank'], v['SM_inside'], v['torus_component_group'] or 'trivial',
                        v['matter_parity']['found']))
    c = d['E5_census']
    lines.append('E5 census: %d gradings; odd on all 15: %d; odd-on-15 counts %s; SM-central %d; in SM torus %d'
                 % (len(c), sum(x['odd_on_15'] == 15 for x in c), sorted({x['odd_on_15'] for x in c}),
                    sum(x['sm_central'] for x in c), sum(x['in_SM_torus'] for x in c)))
    for k in ('G1 nu^c', 'G2 N', 'G3 nu^c and N'):
        v = G[k]
        lines.append('%s: identity dim %d, residual mod SM %s, matter parity %s, nu^c nu^c allowed %s'
                     % (k, v['identity_dim'], v['component_group_mod_SM'] or 'trivial', v['matter_parity']['found'],
                        v['nu_nu_allowed_by_every_generator']))
    lines.append('G4 exp(2 pi i eta/5) is an SM element: %s' % G['eta_over_5_is_SM_element'])
    lines.append('M 27^3: zero-sum triples %d; with two SM singlets %d; all eta-neutral %s'
                 % (M['zero_sum_triples'], M['triples_with_two_singlets'], M['all_triples_eta_neutral']))
    for l in lines:
        print('DECISIVE: ' + l)
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:      # noqa: BLE001
        print('FAILED: %s: %s' % (type(e).__name__, e)); sys.exit(1)
