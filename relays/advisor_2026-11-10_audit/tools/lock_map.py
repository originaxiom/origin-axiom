#!/usr/bin/env python3
"""Map locks to arcs: PROVED / NEGATIVE arcs guarded only by text-reading locks, by dependency in-degree and era.
Run arc_stats.py and lock_census.py first.
Run from the repository root:  python3 relays/advisor_2026-11-10_audit/tools/lock_map.py
Read-only: writes its JSON next to itself."""
import json, re, glob, os, collections
S=os.path.dirname(os.path.abspath(__file__))
stats=json.load(open(S+'/lockcensus.json'))
indeg=dict(json.load(open(S+'/indeg.json'))['indeg'])
A={}
for p in glob.glob('frontier/B*/arc_verdict.json'):
    d=json.load(open(p)); A.setdefault(d['id'],d)
arc_locks=collections.defaultdict(list)
for s in stats:
    ids=set(re.findall(r'[bB](\d{1,4})(?!\d)', os.path.basename(s['f'])))
    m=re.match(r'frontier/B(\d+)_',s['f'])
    if m: ids={m.group(1)}
    for i in ids: arc_locks['B'+i].append(s)
proved=[k for k,v in A.items() if v['verdict']=='PROVED']
textonly=[k for k in proved if arc_locks[k] and all(s['cls'].startswith('TEXT_ONLY') for s in arc_locks[k])]
nolock=[k for k in proved if not arc_locks[k]]
print('PROVED',len(proved),'| locked only by TEXT_ONLY locks',len(textonly),'| no lock matched by name',len(nolock))
neg=[k for k,v in A.items() if v['verdict']=='NEGATIVE']
print('NEGATIVE',len(neg),'| text-only',sum(1 for k in neg if arc_locks[k] and all(s['cls'].startswith('TEXT_ONLY') for s in arc_locks[k])),'| none',sum(1 for k in neg if not arc_locks[k]))
print('text-only PROVED by in-degree:')
for k in sorted(textonly,key=lambda k:-indeg.get(k,0))[:25]:
    print(indeg.get(k,0),k,[s['f'] for s in arc_locks[k]][:2], A[k]['claim_one_line'][:90])
print('law-creating PROVED arcs text-only:',sum(1 for k in textonly if A[k].get('creates_law')),'of',sum(1 for k in proved if A[k].get('creates_law')))
# by era
import statistics
def era(k): n=int(k[1:]); return n//300*300
c=collections.Counter(era(k) for k in proved); t=collections.Counter(era(k) for k in textonly)
for e in sorted(c): print(f'B{e}-{e+299}: PROVED {c[e]}, text-only {t[e]} ({100*t[e]//c[e]}%)')
