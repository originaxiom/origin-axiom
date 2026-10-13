"""Capture the first finite run, never overwrite an earlier output directory."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
NAMES = ['PREREGISTRATION.md', 'PROOF.md', 'SOURCE_SCOPE.md', 'verify.py', 'test_verify.py', 'execute.py']


def hashes():
    return {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in NAMES}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: execute.py NEW_OUTPUT_DIRECTORY')
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=False)
    before = hashes()
    jobs = [('native', [sys.executable, str(HERE/'verify.py')]),
            ('tests', [sys.executable, '-m', 'pytest', '-q', str(HERE/'test_verify.py')])]
    receipt = {'sources_before': before, 'runs': []}
    env = dict(os.environ, LC_ALL='C', LANG='C', PYTHONDONTWRITEBYTECODE='1')
    for label, command in jobs:
        start = time.monotonic()
        p = subprocess.run(command, cwd=HERE, env=env, capture_output=True, check=False)
        row = {'label': label, 'exit_code': p.returncode, 'elapsed_seconds': time.monotonic()-start}
        for kind, content in [('stdout', p.stdout), ('stderr', p.stderr)]:
            filename = label+'.'+kind+'.log'
            (out/filename).write_bytes(content)
            row[kind] = {'file': filename, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}
        receipt['runs'].append(row)
        if p.returncode != 0:
            break
    receipt['sources_after'] = hashes()
    receipt['source_unchanged'] = before == receipt['sources_after']
    receipt['all_scheduled_runs_passed'] = len(receipt['runs']) == len(jobs) and all(
        row['exit_code'] == 0 for row in receipt['runs']) and receipt['source_unchanged']
    (out/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))
    return 0 if receipt['all_scheduled_runs_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
