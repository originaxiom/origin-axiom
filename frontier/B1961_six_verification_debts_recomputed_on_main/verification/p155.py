"""p155. Claims: (a) 42 even-trace signed threads, D4 (2 kernels) or V4 (4 kernels); 16 (B1655) / 17 (B1602 as sealed) carry on SOME kernel, 26/25 on none;
(b) +-LLR generation shape (-1,-1) on every candidate kernel; (c) which kernel is forced is identifiable.
Expect: counts over candidates reproduce from stored per-kernel members; carrier status varies by kernel on some threads, so the forced kernel matters;
identification NOT possible from record (tau sign choices 'not located in SnapPy generators'). Reads stored JSON only; runs no seat code."""
import pathlib as __pl
__ROOT__ = next(q for q in __pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file())
import json,glob,os,collections
R=str(__ROOT__) + '/frontier/B1602_the_forced_cover_on_every_thread/verification/'
C=str(__ROOT__) + '/frontier/B1603_the_count_at_every_member/verification/'
th={}
for f in glob.glob(R+'forced_b*.json'):
    d=json.load(open(f)); th[d['thread']]=d
ev={k:d for k,d in th.items() if d['deck']!='A4'}
print('threads',len(th),'even-trace',len(ev),collections.Counter((d['deck'],d['kernels']) for d in ev.values()))
some=[k for k,d in ev.items() if d['any_member']]; print('carry on some kernel',len(some),'none',len(ev)-len(some))
allk=[k for k,d in ev.items() if all(c['members']>0 for c in d['covers'])]; print('carry on EVERY kernel',len(allk))
mixed=[k for k in some if k not in allk]; print('carry on some not all (kernel-dependent):',len(mixed))
for k in sorted(mixed): print(' ',k,ev[k]['deck'],[c['members'] for c in ev[k]['covers']])
for pos in range(4):
    n=sum(1 for d in ev.values() if len(d['covers'])>pos and d['covers'][pos]['members']>0)
    m=sum(1 for d in ev.values() if len(d['covers'])>pos)
    print('kernel index',pos,'carriers',n,'of',m,'threads having it')
print('threads with one kernel',[k for k,d in ev.items() if d['kernels']==1])
# B1603 generation shape per kernel not stored? inspect keys
for t in ['b++LLR','b+-LLR']:
    d=json.load(open(C+f'count_{t}.json')); print(t,list(d.keys())[:12])
    for k,v in d.items():
        if isinstance(v,list): print(k,len(v), (list(v[0].keys()) if v and isinstance(v[0],dict) else v[:2]))
print('--- reliability tiers (B1604 stored, read only)')
t=json.load(open(glob.glob(str(__ROOT__) + '/frontier/B1604*/verification/tiers.json')[0]))
te=[x for x in t if x['deck']!='A4']
print(collections.Counter(x['tier'] for x in te))
rel=collections.defaultdict(list)
for x in te: rel[x['thread']].append(x)
car_rel=[k for k,v in rel.items() if any(x['tier']=='reliable' and x['members']>0 for x in v)]
car_any=[k for k,v in rel.items() if any(x['members']>0 for x in v)]
print('threads',len(rel),'carry on some reliable kernel',len(car_rel),'carry on any kernel',len(car_any))
print('gen-shaped threads on reliable kernels',sorted({k for k,v in rel.items() for x in v if x['tier']=='reliable' and x['generation_shaped']>0}))
for k in ['b++LLR','b+-LLR']:
    print(k,[(x['kernel'],x['tier'],x['members'],x['generation_shaped']) for x in rel[k]])
# kernel-by-kernel carrier on reliable only, per index
for pos in range(4):
    xs=[x for x in te if x['kernel']==pos and x['tier']=='reliable']
    print('kernel',pos,'reliable',len(xs),'carriers',sum(1 for x in xs if x['members']>0),'genshaped kernels',sum(1 for x in xs if x['generation_shaped']>0))
