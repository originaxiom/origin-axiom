"""First source-fixed capture; receipt survives nonzero science exits."""
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
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    pins=json.loads((HERE/'INPUTS.json').read_text())['source_files']
    def hashes():return {r['path']:digest(ROOT/r['path']) for r in pins}
    sealed={r['path']:r['sha256'] for r in pins};before=hashes()
    def tree():
        paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
        return {os.fsdecode(p):digest(ROOT/os.fsdecode(p)) for p in paths if p and (ROOT/os.fsdecode(p)).is_file()}
    tb=tree()
    rec={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
         'sources_before':before,'matches_seal':before==sealed,'runs':[]}
    if rec['matches_seal']:
        for label in ('probe','reference'):
            t=time.monotonic()
            p=subprocess.run([sys.executable,'-B',str(HERE/(label+'.py'))],cwd=ROOT,
                             env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,timeout=900)
            row={'label':label,'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-t}
            for kind,b in [('stdout',p.stdout),('stderr',p.stderr)]:
                name=label+'.'+kind+'.log';(out/name).write_bytes(b)
                row[kind]={'file':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
            rec['runs'].append(row)
            if p.returncode:break
    rec['sources_after']=hashes();rec['sources_unchanged']=before==rec['sources_after']
    ta=tree();rec['tracked_tree_unchanged']=tb==ta;rec['tracked_file_count']=len(tb)
    rec['tracked_tree_before_digest']=hashlib.sha256(json.dumps(tb,sort_keys=True).encode()).hexdigest()
    rec['tracked_tree_after_digest']=hashlib.sha256(json.dumps(ta,sort_keys=True).encode()).hexdigest()
    rec['passed']=rec['matches_seal'] and rec['sources_unchanged'] and tb==ta and len(rec['runs'])==2 and all(r['exit_code']==0 for r in rec['runs'])
    if rec['passed']:
        a=json.loads((out/'probe.stdout.log').read_text());b=json.loads((out/'reference.stdout.log').read_text())
        rec['records_agree']=a['records']==b['records'];rec['passed'] &= rec['records_agree']
        rec['predicate_counts']=[len(a['checks']),len(b['checks'])]
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec,indent=2));return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
