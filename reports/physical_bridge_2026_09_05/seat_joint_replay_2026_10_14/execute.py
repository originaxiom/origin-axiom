"""Pinned original producer replay with discriminating output validation."""
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
    want={r['path']:r['sha256'] for r in pins}
    def hashes():return {p:digest(ROOT/p) for p in want}
    def tree():
        paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
        return {os.fsdecode(p):digest(ROOT/os.fsdecode(p)) for p in paths if p and (ROOT/os.fsdecode(p)).is_file()}
    before=hashes();tb=tree();rec={'seal_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        'pins_match':before==want,'runs':[],'checks':{}}
    programs=('where_a_higgs_couples','the_lane_su2_branching','the_completion_dichotomy')
    if rec['pins_match']:
        for name in programs:
            t=time.monotonic();p=subprocess.run([sys.executable,'-B',str(HERE/'incoming'/(name+'.py'))],cwd=ROOT,
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,timeout=300)
            row={'program':name,'exit_code':p.returncode,'seconds':time.monotonic()-t}
            for kind,data in [('stdout',p.stdout),('stderr',p.stderr)]:
                fn=name+'.'+kind+'.log';(out/fn).write_bytes(data);row[kind]={'file':fn,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
            rec['runs'].append(row)
            if p.returncode:break
            generated=HERE/'incoming'/(name+'.json');b=generated.read_bytes();(out/(name+'.json')).write_bytes(b)
            actual=json.loads(b);expected=json.loads((HERE/'expected'/(name+'.json')).read_text())
            rec['checks'][name+' complete incoming record reproduced']=actual==expected
            if name=='the_completion_dichotomy':
                rec['checks']['actual commutant0/1/8 and preserved failed M2']=actual['M1']['holds'] and actual['M2']['trace-free commutant dimensions']=={'through O':0,'through S3 only':1,'trivially':8} and not actual['M2']['holds']
            elif name=='the_lane_su2_branching':
                rec['checks']['complete branching and preserved signed failure']=actual['irreps (dimension: copies)']=={'1':55,'2':52,'3':27,'4':2} and actual['odd part dimension']==112 and actual['embedding index']==3 and actual['H_Q(beta)']=='1' and not actual['B3']['holds'] and actual['B4']['holds']
            else:
                rec['checks']['theta/covariance and opposing controls']=actual['U2_all_nontrivial'] and actual['U2_max_dev_from_sign']<1e-25 and actual['U3']['a_isotropy_max_generic_points']<1e-25 and all(v>1-1e-12 for v in actual['U4_exact_law_D1'].values()) and all(v<1-1e-6 for v in actual['U4_control_swapped_matrix_puncture_max'].values()) and actual['U5']['group_order']==24 and actual['U5']['commutant_dim']==1
    after=hashes();ta=tree();rec.update(sources_unchanged=before==after,tracked_unchanged=tb==ta,pin_count=len(pins),tracked_count=len(tb))
    rec['before_digest']=hashlib.sha256(json.dumps(tb,sort_keys=True).encode()).hexdigest();rec['after_digest']=hashlib.sha256(json.dumps(ta,sort_keys=True).encode()).hexdigest()
    rec['passed']=rec['pins_match'] and before==after and tb==ta and len(rec['runs'])==3 and all(r['exit_code']==0 for r in rec['runs']) and len(rec['checks'])==6 and all(rec['checks'].values())
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2));return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
