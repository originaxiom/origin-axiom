#!/usr/bin/env python3
"""Arc statistics: verdict counts, duplicate ids, dependency in-degree, PROVED arcs without a named lock or script.
Run from the repository root:  python3 relays/advisor_2026-11-10_audit/tools/arc_stats.py
Read-only: writes its JSON next to itself."""
import json, glob, os, re, collections
arcs={}
for p in glob.glob('frontier/B*/arc_verdict.json'):
    try: d=json.load(open(p))
    except Exception as e: print('BADJSON',p,e); continue
    d['_dir']=os.path.dirname(p); arcs.setdefault(d.get('id'),[]).append(d)
dups={k:len(v) for k,v in arcs.items() if len(v)>1}
print('arcs',len(arcs),'dup ids',len(dups), list(dups.items())[:10])
indeg=collections.Counter()
for k,vs in arcs.items():
    for v in vs:
        for dep in v.get('depends_on') or []: indeg[dep]+=1
A={k:v[0] for k,v in arcs.items()}
print('verdicts',collections.Counter(v.get('verdict') for v in A.values()))
print('reach',collections.Counter((v.get('scope') or {}).get('reach') if isinstance(v.get('scope'),dict) else 'noscope' for v in A.values()))
print('creates_law',sum(1 for v in A.values() if v.get('creates_law')))
print('TOP in-degree:')
for k,n in indeg.most_common(45):
    v=A.get(k)
    print(n,k,v.get('verdict') if v else 'MISSING', (v.get('claim_one_line') or '')[:110] if v else '')
# PROVED with no test lock / no verification dir
nolock=[]; nover=[]
tests=' '.join(os.listdir('tests'))
for k,v in A.items():
    if v.get('verdict')!='PROVED': continue
    d=v['_dir']; num=k[1:]
    has_local=bool(glob.glob(d+'/verification/test_*.py'))
    has_t=bool(re.search(r'test_b%s[_.]'%num, tests)) or bool(re.search(r'b%s(?!\d)'%num, tests))
    if not(has_local or has_t): nolock.append(k)
    if not os.path.isdir(d+'/verification') and not glob.glob(d+'/*.py'): nover.append(k)
print('PROVED without an obviously named lock',len(nolock), sorted(nolock,key=lambda s:int(re.sub(r'\D','',s)))[:60])
print('PROVED with no verification dir and no .py',len(nover), nover[:40])
json.dump({'indeg':indeg.most_common(200)}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'indeg.json'),'w'))
