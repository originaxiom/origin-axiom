"""Immutable exact science and raw first-output custody."""
import hashlib,json,os,platform,subprocess,sys,tempfile,time
from pathlib import Path
HERE=Path(__file__).resolve().parent;REPO=HERE.parents[2]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def state():
    names=subprocess.check_output(['git','ls-files','-z'],cwd=REPO).split(b'\0')
    return {n.decode():sha(REPO/n.decode()) for n in names if n}
def main():
    out=Path(tempfile.mkdtemp(prefix='oa-four-d-unit-')).resolve()
    print('OUTPUT_DIRECTORY='+str(out),flush=True)
    receipt={'status':'IN_PROGRESS','commands':[],'scope':'specified total metric/YM lift; no three-family operator'}
    before=state();inputs=json.loads((HERE/'INPUTS.json').read_text())
    try:
        assert __debug__
        import sympy
        versions={'python':platform.python_version(),'sympy':sympy.__version__}
        assert versions==inputs['environment'],'unsealed dependency versions'
        receipt['environment']=versions
        assert not subprocess.check_output(['git','status','--porcelain'],cwd=REPO).strip()
        receipt['seal_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO).decode().strip()
        for row in inputs['source_files']:assert sha(REPO/row['path'])==row['sha256'],row['path']
        for row in inputs['foreign_sources']:
            data=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=REPO)
            assert hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
        receipt['initial_source_hashes_match']=True
        for name in ('probe','reference'):
            command=[sys.executable,'-u',str(HERE/(name+'.py'))]
            row={'name':name,'resource_cap_seconds':900};receipt['commands'].append(row)
            start=time.monotonic();print('START '+name,flush=True)
            env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
            env.pop('PYTHONOPTIMIZE',None);env.pop('PYTHONPATH',None)
            with (out/(name+'.stdout.log')).open('xb') as stdout,(out/(name+'.stderr.log')).open('xb') as stderr:
                try:result=subprocess.run(command,cwd=REPO,stdout=stdout,stderr=stderr,timeout=900,env=env)
                except subprocess.TimeoutExpired:
                    row.update(exit_code=None,resource_timeout=True,elapsed_seconds=time.monotonic()-start)
                    raise
            row.update(exit_code=result.returncode,elapsed_seconds=time.monotonic()-start)
            assert result.returncode==0,name
            data=json.loads((out/(name+'.stdout.log')).read_text())
            checks=data['checks'] if name=='probe' else data['exact_checks']
            assert checks and all(v is True for v in checks.values()),name
            row['exact_predicates']=len(checks);print('PASS '+name,flush=True)
        assert before==state(),'tracked tree changed during science'
        for row in inputs['source_files']:assert sha(REPO/row['path'])==row['sha256'],row['path']
        receipt.update(status='PASS',tracked_worktree_unchanged=True,source_inputs_unchanged=True)
    except Exception as exc:
        receipt.update(status='STOPPED_NOT_PROGRAM_KILL',error=f'{type(exc).__name__}: {exc}')
        print(receipt['error'],flush=True)
    receipt['files']=[{'path':p.name,'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(out.iterdir()) if p.is_file()]
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('FINAL_STATUS='+receipt['status'],flush=True)
    return 0 if receipt['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
