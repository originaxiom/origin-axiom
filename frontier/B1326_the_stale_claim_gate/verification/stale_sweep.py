"""Systematic stale-claim sweep: does any RETRACTED or SUPERSEDED arc still speak in main's live docs?"""
import json, glob, re, os, subprocess
ret={}; sup={}
for f in glob.glob('frontier/*/arc_verdict.json'):
    try: d=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    if d.get('verdict')=='RETRACTED':
        ret[d['id']]=dict(dir=os.path.dirname(f), by=(d.get('retracted') or {}).get('by'),
                          reason=((d.get('retracted') or {}).get('reason') or '')[:200])
    if d.get('superseded_by'):
        sup[d['id']]=dict(dir=os.path.dirname(f), by=d['superseded_by'])
print(f"RETRACTED arcs: {len(ret)}   arcs with superseded_by: {len(sup)}")

LIVE = ['papers/P3_THE_PAPER/main.tex','CLAIMS.md','docs/THE_CLAIM.md','README.md',
        'docs/TOE_REQUIREMENTS_LEDGER.md','docs/GUT_REQUIREMENTS_LEDGER.md',
        'docs/THE_LADDER.md','docs/GRAND_COMPUTATION_LEDGER.md','docs/THEOREM_LEDGER.md',
        'docs/THEOREM_REGISTRY.md','docs/IDENTIFICATION_LEDGER.md','docs/FALSIFIER_REGISTER.md']
LIVE=[p for p in LIVE if os.path.exists(p)]
print("live documents scanned:", len(LIVE))
print()
print("=== retracted/superseded arc IDs cited in live docs ===")
flagged=[]
for path in LIVE:
    txt=open(path,encoding='utf-8',errors='replace').read()
    for aid,info in list(ret.items())+ [(k,v) for k,v in sup.items()]:
        for m in re.finditer(r'\b'+aid+r'\b', txt):
            # take the surrounding sentence
            s=max(0,m.start()-260); e=min(len(txt),m.end()+260)
            ctx=txt[s:e].replace('\n',' ')
            aware = re.search(r'RETRACT|retract|withdraw|WITHDRAW|supersed|SUPERSED|corrected|CORRECTED|stale|former', ctx)
            if not aware:
                flagged.append((path,aid,ctx[:210]))
seen=set(); out=[]
for p,a,c in flagged:
    if (p,a) in seen: continue
    seen.add((p,a)); out.append((p,a,c))
print(f"citations with NO retraction/supersession marker nearby: {len(out)}")
for p,a,c in out[:30]:
    kind='RETRACTED' if a in ret else 'superseded'
    print(f"\n  [{kind}] {a}  in  {p}\n    ...{c}...")
