"""Credited immutable source, tree and index capture."""
# BANKED IDENTITY: both methods replay actual source. PRIOR ART: mode capture.
import hashlib,importlib.util,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('all_response_capture',HERE.parent/'surface_mode_transport_2026_10_15/execute.py')
capture=importlib.util.module_from_spec(sp);sp.loader.exec_module(capture)
capture.HERE=HERE;capture.ROOT=HERE.parents[2]
def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    want={r['path']:r['sha256'] for r in json.loads((HERE/'INPUTS.json').read_text())['source_files']}
    def state():return {'pins':{p:capture.sha(capture.ROOT/p) for p in want},'tree':capture.tree(),
      'index_sha256':hashlib.sha256(subprocess.check_output(['git','ls-files','--stage','-z'],cwd=capture.ROOT)).hexdigest()}
    before=state();(out/'before.json').write_text(json.dumps(before,indent=2)+'\n');outputs=[]
    rec={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=capture.ROOT,text=True).strip(),'pins_match':before['pins']==want,'runs':[]}
    if rec['pins_match']:
        for name in ('probe','reference'):
            start=time.monotonic();sp=out/(name+'.stdout.log');ep=out/(name+'.stderr.log')
            with sp.open('wb') as so,ep.open('wb') as se:
                p=subprocess.Popen([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=capture.ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=so,stderr=se)
                try:code=p.wait(timeout=1200)
                except subprocess.TimeoutExpired:p.kill();p.wait();code=124
            stdout=sp.read_bytes();stderr=ep.read_bytes()
            rec['runs'].append({'program':name,'exit_code':code,'seconds':time.monotonic()-start,
              'stdout':{'bytes':len(stdout),'sha256':hashlib.sha256(stdout).hexdigest()},'stderr':{'bytes':len(stderr),'sha256':hashlib.sha256(stderr).hexdigest()}})
            if code:break
            obj=json.loads(stdout);(out/(name+'.json')).write_bytes(stdout);outputs.append(obj)
            if not obj['all_passed']:break
    after=state();(out/'after.json').write_text(json.dumps(after,indent=2)+'\n')
    rec.update(source_pins=len(want),tracked_files=len(before['tree']),pins_unchanged=before['pins']==after['pins'],tracked_unchanged=before['tree']==after['tree'],
      index_unchanged=before['index_sha256']==after['index_sha256'],fingerprint_before=hashlib.sha256(json.dumps(before['tree'],sort_keys=True).encode()).hexdigest(),
      fingerprint_after=hashlib.sha256(json.dumps(after['tree'],sort_keys=True).encode()).hexdigest(),complete_records_agree=len(outputs)==2 and outputs[0]==outputs[1])
    rec['passed']=rec['pins_match'] and rec['pins_unchanged'] and rec['tracked_unchanged'] and rec['index_unchanged'] and rec['complete_records_agree'] and all(o['all_passed'] for o in outputs)
    if not rec['passed']:
        for path in want:
            dest=out/'source_snapshot'/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((capture.ROOT/path).read_bytes())
        for name in ('INPUTS.json','ARTIFACT_HASHES.txt'):(out/name).write_bytes((HERE/name).read_bytes())
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2));return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
