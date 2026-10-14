"""Quiescent live tests with whole tracked-tree and exact source custody."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
TESTS=[
    'tests/test_physical_bridge_surface_based_gauge.py',
    'tests/test_physical_bridge_surface_odd_form.py',
    'tests/test_physical_bridge_surface_even_channels.py',
    'tests/test_physical_bridge_surface_full_even.py',
    'tests/test_physical_bridge_surface_global_spin.py',
    'tests/test_physical_bridge_surface_parent_dictionary.py',
    'tests/test_physical_bridge_based_transition_prerequisite.py',
    'tests/test_physical_bridge_weave_registered_embedding.py',
    'tests/test_physical_bridge_weave_field_map.py',
    'tests/test_physical_bridge_weave_gauge_limit.py',
    'tests/test_physical_bridge_weave_companion_roster.py',
]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    def tree():
        paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).split(b'\0')
        return {os.fsdecode(p):digest(ROOT/os.fsdecode(p)) for p in paths if p and (ROOT/os.fsdecode(p)).is_file()}
    before=tree();t=time.monotonic()
    cmd=[sys.executable,'-B','-m','pytest','-q','-p','no:cacheprovider']+TESTS
    p=subprocess.run(cmd,cwd=ROOT,capture_output=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),timeout=900)
    after=tree();rec={'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-t,'tests':TESTS,
                     'tracked_file_count':len(before),'tracked_tree_unchanged':before==after,
                     'tree_before_sha256':hashlib.sha256(json.dumps(before,sort_keys=True).encode()).hexdigest(),
                     'tree_after_sha256':hashlib.sha256(json.dumps(after,sort_keys=True).encode()).hexdigest(),
                     'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()}
    for kind,b in [('stdout',p.stdout),('stderr',p.stderr)]:
        name=kind+'.log';(out/name).write_bytes(b)
        rec[kind]={'file':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
    rec['passed']=p.returncode==0 and before==after
    (out/'RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec,indent=2));return 0 if rec['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
