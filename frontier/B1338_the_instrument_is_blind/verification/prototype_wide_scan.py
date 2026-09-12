"""already_banked, widened to the two surfaces it cannot currently see.

B1202's instrument is MANDATORY before writing MISSING / OPEN / "never run". It scans
frontier/*/arc_verdict.json and frontier/*/**/FINDINGS.md IN THE WORKING TREE, and nothing else.
Its declared blind regions are SUBJECT-MATTER negative controls (inflation, dark matter), not a
statement about search scope. So two surfaces are invisible to it, and both are where the record's
rediscoveries actually live:

  (a) docs/ -- the LEDGERS. I-26's row saying a price is "untouched", HARVEST_LEDGER's 277
      SCHEDULED rows. A register row is exactly what the instrument exists to beat, and it cannot
      read the registers.
  (b) the 156 SCHEDULED artifacts readable only AT OTHER COMMITS (B1337). memo 152 "what exactly we
      do not have", memo 158 "the live route is not unrun, it is run". Off the working tree,
      therefore invisible.

This adds both without changing the existing verdict surface, and B1202's two negative controls
must STILL come back clean -- an instrument that fires on everything discriminates nothing.
"""
import json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[0]
ROOT = pathlib.Path('/home/user/origin-axiom')
SETTLED = {"PROVED","NEGATIVE","RESOLVED","RESOLVED-A","THEOREM","RETRACTED"}

def _terms(argv):
    raw=" ".join(argv).lower()
    return [t for t in re.split(r"[^a-z0-9_^+\-/()=]+",raw) if len(t)>2]

def scan_tree(terms, exclude=()):
    hits=[]
    for vp in sorted(ROOT.glob("frontier/*/arc_verdict.json")):
        try: d=json.loads(vp.read_text(encoding="utf-8",errors="ignore"))
        except Exception: continue
        if any(x in vp.parent.name for x in exclude): continue
        blob=json.dumps(d).lower(); n=sum(1 for t in terms if t in blob)
        if n: hits.append((n,d.get("verdict","?"),vp.parent.name,(d.get("claim_one_line") or "")[:150]))
    for fp in sorted(ROOT.glob("frontier/*/**/FINDINGS.md")):
        if any(x in str(fp) for x in exclude): continue
        try: txt=fp.read_text(encoding="utf-8",errors="ignore").lower()
        except Exception: continue
        n=sum(1 for t in terms if t in txt)
        if n>=max(2,len(terms)-1):
            head=fp.read_text(encoding="utf-8",errors="ignore").splitlines()[:2]
            hits.append((n,"FINDINGS",str(fp.relative_to(ROOT))," ".join(head)[:150]))
    return hits

def scan_docs(terms):
    """(a) the LEDGERS -- the surface a register-vs-corpus instrument most needs and least has"""
    hits=[]
    for fp in sorted(ROOT.glob("docs/*.md")):
        try: raw=fp.read_text(encoding="utf-8",errors="ignore")
        except Exception: continue
        for i,line in enumerate(raw.splitlines()):
            low=line.lower(); n=sum(1 for t in terms if t in low)
            if n>=max(2,len(terms)-1) and len(line)>80:
                hits.append((n,"LEDGER",f"{fp.name}:{i+1}",line.strip()[:150]))
    return hits

def scan_offtree(terms, idx):
    """(b) the SCHEDULED artifacts readable only at other commits (B1337's list)"""
    hits=[]
    for e in idx:
        try:
            txt=subprocess.run(['git','show',f"{e['commit']}:{e['path']}"],
                               capture_output=True,cwd=ROOT).stdout.decode('utf-8','ignore').lower()
        except Exception: continue
        if not txt: continue
        n=sum(1 for t in terms if t in txt)
        if n>=max(2,len(terms)-1):
            hits.append((n,"SCHEDULED",f"{e['seat']} {e['arc']}",e['claim'][:150]))
    return hits

def main():
    argv=[a for a in sys.argv[1:] if not a.startswith('--')]
    exclude=tuple(a.split('=',1)[1] for a in sys.argv[1:] if a.startswith('--exclude='))
    terms=_terms(argv)
    idx=json.loads((ROOT/'frontier/B1337_the_scheduled_sweep/verification/readable_scheduled.json').read_text())
    tree=scan_tree(terms,exclude); docs=scan_docs(terms); off=scan_offtree(terms,idx)
    print(f"already-banked+: terms {terms}")
    settled=[h for h in tree if h[1] in SETTLED]
    print(f"  working tree : {len(tree)} hits, {len(settled)} SETTLED arcs")
    print(f"  LEDGERS      : {len(docs)} hits   <- new surface (a)")
    print(f"  SCHEDULED    : {len(off)} hits   <- new surface (b)")
    for lbl,hs in (("SETTLED",settled),("LEDGER",docs),("SCHEDULED",off)):
        for h in sorted(hs,key=lambda x:-x[0])[:3]:
            print(f"   *** [{h[0]}t] {h[1]:10s} {h[2][:52]:52s} {h[3][:96]}")
    return 0 if not (settled or docs or off) else 1
sys.exit(main())
