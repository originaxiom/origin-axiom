#!/usr/bin/env python3
"""Run the three final instruments and record literal output and exit codes."""
from pathlib import Path
import subprocess,sys,time,json,hashlib,datetime
root=Path(__file__).resolve().parent
records=[]
for name in ['verify_coupled.py','verify_slab_reference.py','verify_constraints.py']:
    start=time.perf_counter()
    cp=subprocess.run([sys.executable,str(root/name)],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    elapsed=time.perf_counter()-start
    log=name.replace('.py','_REPLAY.log');(root/log).write_bytes(cp.stdout)
    records.append({'script':name,'command':[sys.executable,name],'exit_code':cp.returncode,
      'elapsed_seconds':elapsed,'stdout_stderr_file':log,'bytes':len(cp.stdout),
      'log_sha256':hashlib.sha256(cp.stdout).hexdigest(),
      'script_sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()})
    print(name,cp.returncode,round(elapsed,3),flush=True)
    if cp.returncode:raise RuntimeError(f'{name} failed; inspect {log}')
(root/'FINAL_REPLAY_RECEIPT.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':records},indent=2)+'\n')
