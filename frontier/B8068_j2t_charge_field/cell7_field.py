import sys,os,subprocess,sympy as sp
HERE=os.path.dirname(os.path.abspath(__file__))
primes=[p for p in sp.primerange(1000,2600) if p%3==1][:14]
res={}
for p in primes:
    try:
        out=subprocess.run([sys.executable,os.path.join(HERE,"cell6_pure.py"),str(p)],
                           capture_output=True,text=True,timeout=900).stdout
        line=[l for l in out.splitlines() if "omega  " in l]
        if not line: continue
        n=int(line[0].split("pure points")[1].split("at")[0].strip())
        res[p]=n
        print(f"  p = {p:5d}  ->  {n} pure points  ({'SPLIT' if n else 'inert'})")
    except Exception as ex:
        print(f"  p = {p:5d}  ->  skipped ({type(ex).__name__})")
print(f"\nsplitting pattern: {res}")
split={p for p,n in res.items() if n==2}
inert={p for p,n in res.items() if n==0}
print(f"  split at {sorted(split)}")
print(f"  inert at {sorted(inert)}")
print("\nmatching against small discriminants (Legendre symbol must be +1 exactly on the split set):")
for d in [-1,2,-2,3,-3,5,-5,6,7,-7,11,-11,13,15,-15,21,33,77,-77,-19,17,-23,6237,-6237]:
    ok=all((sp.legendre_symbol(d%p,p)==1)==(p in split) for p in res if p not in (2,) and d%p!=0)
    if ok: print(f"    d = {d:6d}   MATCHES  -> the pure spinors live over Q(sqrt({d}))"
                 f"   {'REAL' if d>0 else 'IMAGINARY'}")
