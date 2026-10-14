"""Source-fixed full-even extension capture, separately sealed from channel science."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    if len(sys.argv)!=2:raise SystemExit('full_even_execute.py NEW_OUTPUT_DIRECTORY')
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    pins=json.loads((HERE/'FULL_EVEN_INPUTS.json').read_text())['source_files']
    hashes=lambda:{r['path']:digest(ROOT/r['path']) for r in pins}
    before=hashes();sealed={r['path']:r['sha256'] for r in pins}
    rec={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
         'sources_before':before,'matches_seal':before==sealed,'runs':[]}
    if rec['matches_seal']:
        for label in ['full_even_probe','full_even_reference']:
            start=time.monotonic();p=subprocess.run([sys.executable,str(HERE/(label+'.py'))],cwd=ROOT,
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,timeout=900)
            row={'label':label,'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-start}
            for kind,b in [('stdout',p.stdout),('stderr',p.stderr)]:
                name=label+'.'+kind+'.log';(out/name).write_bytes(b)
                row[kind]={'file':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
            rec['runs'].append(row)
            if p.returncode:break
    rec['sources_after']=hashes();rec['sources_unchanged']=before==rec['sources_after']
    rec['passed']=rec['matches_seal'] and rec['sources_unchanged'] and len(rec['runs'])==2 and all(r['exit_code']==0 for r in rec['runs'])
    if rec['passed']:
        a=json.loads((out/'full_even_probe.stdout.log').read_text());b=json.loads((out/'full_even_reference.stdout.log').read_text())
        rec['records_agree']=a['records']==b['records'];rec['passed']=rec['passed'] and rec['records_agree']
        rec['predicate_counts']=[len(a['checks']),len(b['checks'])]
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec,indent=2));return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
