"""Explicit scoped audit; NEVER turns the original dictionary failure into success."""
import hashlib,importlib.util,json,os,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sp=importlib.util.spec_from_file_location('scope_capture',HERE.parent/'surface_mode_transport_2026_10_15/execute.py')
capture=importlib.util.module_from_spec(sp);sp.loader.exec_module(capture);capture.ROOT=ROOT
def scoped(data):
    checks=data['checks'];bad=[k for k,v in checks.items() if not v]
    assert len(checks)==39 and bad==['full positive identity flavour Clifford map']
    assert data['all_passed'] is False
    src=data['records']['source'];assert src['signed_time_weights']==['1']*4
    assert not src['direct_and_component_bulk_residual'] and not src['all_local_flavour_maps']
    rejects=src['all_rejected_flavour_maps'];assert len(rejects)==24
    assert rejects[0]=={'permutation':[0,1,2,3],'reason':['inconsistent edge',1,0,10,'1','-1']}
    return True
def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    pins=json.loads((HERE/'INPUTS.json').read_text())['source_files']
    want={r['path']:r['sha256'] for r in pins}
    hashes=lambda:{p:capture.sha(ROOT/p) for p in want}
    before=hashes();tree=capture.tree();index=subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT)
    assert before==want
    receipt={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'original_full_dictionary_gate_passed':False,'runs':[]};values=[];raws=[];passed=True
    for name in ('probe','reference','clifford_diagnostic'):
        start=time.monotonic()
        p=subprocess.run([sys.executable,'-B',str(HERE/(name+'.py'))],cwd=ROOT,
            env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,timeout=1200)
        row={'program':name,'exit_code':p.returncode,'seconds':time.monotonic()-start}
        for kind,raw in [('stdout',p.stdout),('stderr',p.stderr)]:
            (out/(name+'.'+kind+'.log')).write_bytes(raw)
            row[kind]={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
        receipt['runs'].append(row)
        try:
            data=json.loads(p.stdout)
            if name=='clifford_diagnostic':assert p.returncode==0 and data['all_passed']
            else:
                assert p.returncode==1 and scoped(data);values.append(data);raws.append(p.stdout)
        except (ValueError,AssertionError,KeyError):passed=False;break
    receipt.update(source_pins=len(want),tracked_files=len(tree),pins_match=before==want,
        pins_unchanged=before==hashes(),tracked_unchanged=tree==capture.tree(),
        index_unchanged=index==subprocess.check_output(['git','ls-files','--stage','-z'],cwd=ROOT),
        fingerprint_before=hashlib.sha256(json.dumps(tree,sort_keys=True).encode()).hexdigest(),
        complete_action_records_identical=len(raws)==2 and raws[0]==raws[1])
    receipt['scope_audit_passed']=passed and receipt['complete_action_records_identical'] and all(receipt[k] for k in ('pins_match','pins_unchanged','tracked_unchanged','index_unchanged'))
    if not receipt['scope_audit_passed']:
        for p in want:
            dest=out/'source_snapshot'/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((ROOT/p).read_bytes())
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
    return 0 if receipt['scope_audit_passed'] else 1
if __name__=='__main__':raise SystemExit(main())
