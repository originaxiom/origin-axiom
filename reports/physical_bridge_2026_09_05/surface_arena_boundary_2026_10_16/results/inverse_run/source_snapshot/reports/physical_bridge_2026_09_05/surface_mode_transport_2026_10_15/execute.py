"""Presealed capture; failures, source pins, tree and index stay auditable."""
import hashlib,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tree():
    paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
    return {os.fsdecode(p):sha(ROOT/os.fsdecode(p)) for p in paths if p and (ROOT/os.fsdecode(p)).is_file()}
def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    want={r['path']:r['sha256'] for r in json.loads((HERE/'INPUTS.json').read_text())['source_files']}
    def pins():return {p:sha(ROOT/p) for p in want}
    before=pins();tb=tree();index=subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT)
    rec={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
         'pins_match':before==want,'runs':[]};outputs=[]
    if before==want:
        for name in ('probe','reference'):
            started=time.monotonic()
            try:
                p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
                    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,timeout=1200)
                stdout,stderr,code=p.stdout,p.stderr,p.returncode
            except subprocess.TimeoutExpired as exc:
                stdout,stderr,code=exc.stdout or b'',exc.stderr or b'',124
            row={'program':name,'exit_code':code,'seconds':time.monotonic()-started}
            for kind,data in [('stdout',stdout),('stderr',stderr)]:
                (out/(name+'.'+kind+'.log')).write_bytes(data)
                row[kind]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
            rec['runs'].append(row)
            if code:break
            obj=json.loads(stdout);(out/(name+'.json')).write_bytes(stdout);outputs.append(obj)
            if not obj['all_passed']:break
    after=pins();ta=tree();rec.update(source_pins=len(want),tracked_files=len(tb),
        pins_unchanged=before==after,tracked_unchanged=tb==ta,
        index_unchanged=index==subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT),
        fingerprint_before=hashlib.sha256(json.dumps(tb,sort_keys=True).encode()).hexdigest(),
        fingerprint_after=hashlib.sha256(json.dumps(ta,sort_keys=True).encode()).hexdigest())
    rec['complete_records_agree']=len(outputs)==2 and outputs[0]==outputs[1]
    rec['passed']=rec['pins_match'] and rec['pins_unchanged'] and rec['tracked_unchanged'] and rec['index_unchanged'] and rec['complete_records_agree'] and all(o['all_passed'] for o in outputs)
    if not rec['passed']:
        for path in want:
            dest=out/'source_snapshot'/path;dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes((ROOT/path).read_bytes())
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
    return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
