"""Durable first-run capture. Never overwrite earlier results."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SOURCES = ['PREREGISTRATION.md', 'PROOF.md', 'SOURCE_SCOPE.md', 'verify.py', 'test_verify.py', 'execute.py']


def hashes():
    return {p: hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in SOURCES}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: execute.py NEW_OUTPUT_DIRECTORY')
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=False)
    rec = {'sources_before': hashes(), 'runs': []}
    jobs = [('native', [sys.executable, str(HERE/'verify.py')]),
            ('tests', [sys.executable, '-m', 'pytest', '-q', str(HERE/'test_verify.py')])]
    for label, command in jobs:
        start = time.monotonic()
        p = subprocess.run(command, cwd=HERE, env=dict(os.environ, LC_ALL='C', LANG='C', PYTHONDONTWRITEBYTECODE='1'), capture_output=True)
        row = {'label': label, 'exit_code': p.returncode, 'elapsed_seconds': time.monotonic()-start}
        for kind, content in [('stdout', p.stdout), ('stderr', p.stderr)]:
            name = label+'.'+kind+'.log'
            (out/name).write_bytes(content)
            row[kind] = {'file': name, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()}
        rec['runs'].append(row)
        if p.returncode:
            break
    rec['sources_after'] = hashes()
    rec['source_unchanged'] = rec['sources_before'] == rec['sources_after']
    rec['passed'] = len(rec['runs']) == len(jobs) and all(r['exit_code'] == 0 for r in rec['runs']) and rec['source_unchanged']
    (out/'EXECUTION_RECEIPT.json').write_text(json.dumps(rec, indent=2)+'\n')
    print(json.dumps(rec, indent=2))
    return 0 if rec['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
