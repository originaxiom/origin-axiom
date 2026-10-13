"""Capture sealed native, separate-method and test executions without overwriting."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
NAMES = ['PREREGISTRATION.md','PROOF.md','PRESEAL_NOTES.md','verify.py',
         'reference.py','test_verify.py','execute.py',
         '../noncompact_admission/candidate.json']


def hashes():
    return {name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in NAMES}


def main():
    out = Path(sys.argv[1]).resolve()
    out.mkdir(parents=True,exist_ok=False)
    before = hashes()
    jobs = [('native',[sys.executable,str(HERE/'verify.py'),str(out)]),
            ('reference',[sys.executable,str(HERE/'reference.py'),str(out)]),
            ('tests',[sys.executable,'-m','pytest','-q',str(HERE/'test_verify.py')])]
    receipt = {'sources_before':before,'runs':[]}
    env = dict(os.environ,LC_ALL='C',LANG='C',PYTHONDONTWRITEBYTECODE='1')
    for label,command in jobs:
        start = time.monotonic()
        p = subprocess.run(command,cwd=HERE,env=env,capture_output=True,check=False)
        row = {'label':label,'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-start}
        for kind,data in [('stdout',p.stdout),('stderr',p.stderr)]:
            filename = label+'.'+kind+'.log'
            (out/filename).write_bytes(data)
            row[kind] = {'file':filename,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
        receipt['runs'].append(row)
        print(json.dumps(row),flush=True)
        if p.returncode:
            break
    receipt['sources_after'] = hashes()
    receipt['source_unchanged'] = before == receipt['sources_after']
    receipt['all_scheduled_runs_passed'] = len(receipt['runs']) == len(jobs) and all(
        row['exit_code'] == 0 for row in receipt['runs']) and receipt['source_unchanged']
    receipt['outputs'] = {f.name:hashlib.sha256(f.read_bytes()).hexdigest()
                          for f in sorted(out.iterdir()) if f.is_file()}
    (out/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'all_scheduled_runs_passed':receipt['all_scheduled_runs_passed']}))
    return 0 if receipt['all_scheduled_runs_passed'] else 1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: execute.py NEW_OUTPUT_DIRECTORY')
    raise SystemExit(main())
