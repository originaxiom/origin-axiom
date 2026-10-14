"""Compare two census JSON outputs (list of cells or a single cell). Ignores timing fields; normalises dict keys to str."""
import json, sys
IGN = {'seconds'}
def norm(x):
    if isinstance(x, dict): return {str(k): norm(v) for k, v in x.items()}
    if isinstance(x, list): return [norm(v) for v in x]
    return x
def load(f):
    d = json.load(open(f))
    return d if isinstance(d, list) else [d]
a, b = load(sys.argv[1]), load(sys.argv[2])
ka = {(r['root'], r['n']): r for r in a}; kb = {(r['root'], r['n']): r for r in b}
print(f"cells: committed {len(a)}, rerun {len(b)}; common {len(set(ka) & set(kb))}")
ndiff = 0
for k in ka:
    if k not in kb: print('  missing in rerun:', k); continue
    ra, rb = norm(ka[k]), norm(kb[k])
    d = {f: (ra.get(f), rb.get(f)) for f in set(ra) | set(rb) if f not in IGN and ra.get(f) != rb.get(f)}
    if d: ndiff += 1; print('  DIFF', k, d)
print(f"cells differing (excluding timing): {ndiff}")
