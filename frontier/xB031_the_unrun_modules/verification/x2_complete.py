"""xB031 X2 -- B1418's own run() (byte-identical c2_run.py) on t12835, BUDGET REMOVED.
Reproduces the 3110 it ran AND completes the 3325 it did not.  MS = [1,2,3] exactly as B1418."""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import NF
from c2_run import run
K = NF([1, 0, -1, 0, 1]); z = K.alpha()
S = [K.pw(z, k) for k in range(12)]
out = run('t12835', K, S, [1, 2, 3], 10**9, 'xB031 X2: B1418 range, budget removed')
json.dump(out, open(pathlib.Path(__file__).with_name('x2_t12835.json'), 'w'), indent=1, default=str)
nr = sum(1 for r in out if r.get('status') != 'RUN')
Is = sorted({r['I'] for r in out if r.get('status') == 'RUN'})
print(f"X2 DONE: total {len(out)}, NOT RUN {nr}, I values {Is}, "
      f"max|I| {max(abs(i) for i in Is) if Is else None}")
