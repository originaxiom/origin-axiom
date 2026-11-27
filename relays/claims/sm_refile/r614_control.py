"""Failing control for the SM seat's P-614 card.

The decisive script is relays/sm_r614/posthoc_run.py (the disclosed post-hoc fix of the sealed run.py). This control
copies the sealed folder to a fresh temporary directory and makes ONE deliberate change in the copy: the U1-eta
direction eta = 3 gamma = (3 chi - 5 psi)/4 is replaced by psi (a wrong abelian direction, the cloud memos' frame).
psi is 1 on nu^c and 4 on N, so the claim's premise (both singlets carry the same eta charge) and its conclusion
(the residual is trivial, exp(2 pi i eta/5) an SM element) must not come out together. Nothing is written into the
repository. Run from the repo root:  python3 relays/claims/sm_refile/r614_control.py

Exit 1 with "CONTROL FAILS:" when the perturbed run completes and the check rejects it (the expected outcome);
exit 0 with "CONTROL DID NOT FAIL:" if the decisive values come out anyway; exit 3 with "CONTROL INVALID:" on a crash,
a missing file, or an edit that did not apply.
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
        print('CONTROL INVALID: repository root not found'); return 3
    tmp = tempfile.mkdtemp(prefix='r614c_')
    try:
        work = os.path.join(tmp, 'sm_r614')
        shutil.copytree(str(root / 'relays' / 'sm_r614'), work)
        for f in ('r614_results_posthoc.json', 'r614_results.json'):
            p = os.path.join(work, f)
            if os.path.exists(p): os.remove(p)
        sp = os.path.join(work, 'posthoc_run.py'); src = open(sp).read()
        old = '    eta = [3 * g for g in gamma]'
        if src.count(old) != 1:
            print('CONTROL INVALID: the edit did not apply (%d occurrences)' % src.count(old)); return 3
        open(sp, 'w').write(src.replace(old, '    eta = list(psi)                                 # PLANTED: wrong'))
        r = subprocess.run([sys.executable, '-B', sp, str(root)], cwd=work, capture_output=True, text=True)
        out = os.path.join(work, 'r614_results_posthoc.json')
        if r.returncode != 0 or not os.path.exists(out):
            print('CONTROL INVALID: the perturbed run crashed (exit %d): %s'
                  % (r.returncode, (r.stderr.strip().splitlines() or [''])[-1])); return 3
        d = json.load(open(out))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    equal = d['B']['equal_on_the_two_singlets']
    trivial = all(d['G'][k]['component_group_mod_SM'] == [] for k in ('G1 nu^c', 'G2 N', 'G3 nu^c and N'))
    g4 = d['G']['eta_over_5_is_SM_element']
    print('CONTROL: planted eta = psi; equal on nu^c and N: %s; residual trivial in G1-G3: %s; G4: %s'
          % (equal, trivial, g4))
    if equal and trivial and g4:
        print('CONTROL DID NOT FAIL: the decisive values came out with the wrong direction'); return 0
    print('CONTROL FAILS: with psi in place of U1-eta the claim does not come out (as it must)'); return 1


if __name__ == '__main__':
    try:
        rc = main()
    except BaseException as e:      # noqa: BLE001
        print('CONTROL INVALID: %s: %s' % (type(e).__name__, e)); rc = 3
    sys.exit(rc)
