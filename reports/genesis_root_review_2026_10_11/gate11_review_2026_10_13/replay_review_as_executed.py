"""Read-only archive assessment: unchanged producers in disposable copies.

No original archive, repository source, environment setting or remote is edited.
Targeted B1634 relation controls are declared here before this instrument runs.
This is a replay/reconciliation, not a blind new scientific prediction.
"""
from pathlib import Path
import ast
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/private/tmp/oa-through-gate11-read-qrhkm68c/Origin_Axiom_Banking_Seat_2026_10_13/EXPANDED_POST_GATE3')
JOBS = [
    ('gate4', '04_JOINING_GATE_4', ['verify_exact.py', 'verify_projector.py'], ['EXACT_RESULTS.json', 'MATRICES.json', 'PROJECTOR_RESULTS.json']),
    ('gate6', '06_JOINING_GATE_6/weave_joining_gate6_2026_10_11', ['verify_reference.py'], ['outputs/REFERENCE_RESULTS.json']),
    ('gate7', '07_JOINING_GATE_7/weave_joining_gate7_2026_10_12', ['verify_reference.py'], ['outputs/REFERENCE_RESULTS.json']),
    ('gate9', '09_JOINT_WEAVE_GATE_9/Gate9_Weave_Joint_Action', ['verify_reference.py'], ['REFERENCE_RESULTS.json']),
    ('gate10', '10_FAITHFUL_GATE_10/Gate10_Faithful_Records', ['verify_reference.py'], ['REFERENCE_GATE10.json']),
    ('gate11', '11_JOINT_STATE_GATE_11/Gate11', ['verify_exact.py', 'verify_reference.py', 'verify_hilbert.py', 'verify_lift_forks.py'], ['RESULTS_GATE11.json', 'REFERENCE_RESULTS.json', 'HILBERT_RESULTS.json', 'LIFT_FORKS_RESULTS.json']),
]

def sha(b):
    return hashlib.sha256(b).hexdigest()

def hashes(directory):
    return {str(p.relative_to(directory)): sha(p.read_bytes()) for p in directory.rglob('*') if p.is_file()}

def scientific(obj):
    if isinstance(obj, dict):
        return {k: scientific(v) for k, v in obj.items() if k != 'elapsed_seconds'}
    if isinstance(obj, list):
        return [scientific(v) for v in obj]
    return obj

def run_job(job):
    label, rel, scripts, result_names = job
    source = SOURCE / rel
    before = hashes(source)
    target = ROOT / label
    shutil.copytree(source, target)
    runs = []
    env = dict(os.environ, LC_ALL='C', LANG='C', PYTHONDONTWRITEBYTECODE='1')
    for script in scripts:
        start = time.monotonic()
        proc = subprocess.run([sys.executable, str(target / script)], cwd=target, env=env, capture_output=True, timeout=120)
        (ROOT / f'{label}_{script}.stdout').write_bytes(proc.stdout)
        (ROOT / f'{label}_{script}.stderr').write_bytes(proc.stderr)
        runs.append({'script': script, 'source_sha256': before[script], 'exit_code': proc.returncode,
                     'elapsed_seconds': time.monotonic()-start,
                     'stdout_sha256': sha(proc.stdout), 'stderr_sha256': sha(proc.stderr),
                     'stdout_bytes': len(proc.stdout), 'stderr_bytes': len(proc.stderr)})
        print(label, script, 'exit', proc.returncode, flush=True)
        if proc.returncode:
            break
    results = {}
    for name in result_names:
        old = json.loads((source/name).read_text())
        new = json.loads((target/name).read_text())
        results[name] = {'scientific_json_equal': scientific(old) == scientific(new),
                         'byte_equal': (source/name).read_bytes() == (target/name).read_bytes(),
                         'source_sha256': before[name], 'replay_sha256': sha((target/name).read_bytes())}
    return {'source_directory': str(source), 'copy_directory': str(target), 'runs': runs,
            'results': results, 'original_source_unchanged': hashes(source) == before}

def ruled_metaplectic_check():
    """Exact independent tuple arithmetic; read matrix constants, not producer code.

    B1634's existing Mp2 presentation has s^2=(st)^3, s^8=1.
    With s=(L R^-1 L)^-1 and t=L, check it without scalar repairs.
    Keep the separate optional based-sign obstruction as an opposing control.
    """
    p = SOURCE/'11_JOINT_STATE_GATE_11/Gate11/verify_exact.py'
    constants = {}
    for node in ast.parse(p.read_text()).body:
        if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in {'I','LL','RR','DD'}:
                constants[node.targets[0].id] = ast.literal_eval(node.value)
    identity = (0, constants['I'])
    def product(a,b):
        return ((a[0]+b[0]) % 8, tuple(sum(a[1][3*i+k]*b[1][3*k+j] for k in range(3)) for i in range(3) for j in range(3)))
    def inverse(a):
        return ((-a[0])%8, tuple(a[1][3*j+i] for i in range(3) for j in range(3)))
    def power(a,n):
        out=identity
        for _ in range(n):
            out=product(out,a)
        return out
    left=(7,constants['LL']); right=(1,constants['RR'])
    delta=product(product(left,inverse(right)),left)
    s=inverse(delta); t=left
    checks = {
        'ruled_braid_relation': delta == product(product(inverse(right),left),inverse(right)),
        'Mp2_s_squared_equals_st_cubed_without_rephasing': power(s,2)==power(product(s,t),3),
        'Mp2_s_eighth_is_identity': power(s,8)==identity,
        'Mp2_s_fourth_is_minus_identity_not_ordinary_SL2': power(s,4)==(4,constants['I']),
        'optional_based_sign_is_separate_and_its_lift_squares_minus_identity': power((6,constants['DD']),2)==(4,constants['I']),
    }
    assert all(checks.values()), checks
    return {'checks': checks, 'grade': 'exact relations of the source normal-form matrices; not a rerun of theta-function identification or an Aut(F2) lift classification',
            'source_sha256': sha(p.read_bytes())}

if __name__ == '__main__':
    print('interpreter', sys.executable, flush=True)
    before=hashes(SOURCE)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=dict(zip((job[0] for job in JOBS), pool.map(run_job, JOBS)))
    result={'replays': results, 'ruled_metaplectic_relation_controls': ruled_metaplectic_check(),
            'all_original_expanded_files_unchanged': before == hashes(SOURCE),
            'comparison_ignores_only_field': 'elapsed_seconds', 'interpreter': sys.executable}
    (ROOT/'REPLAY_RECEIPT.json').write_text(json.dumps(result, indent=2)+'\n')
    good=all(all(run['exit_code']==0 for run in value['runs']) and value['original_source_unchanged'] and
             all(check['scientific_json_equal'] for check in value['results'].values()) for value in results.values())
    print('all_scientific_replays_equal', good, flush=True)
    print('ruled_Mp2_controls', result['ruled_metaplectic_relation_controls']['checks'], flush=True)
    raise SystemExit(0 if good and result['all_original_expanded_files_unchanged'] else 1)
