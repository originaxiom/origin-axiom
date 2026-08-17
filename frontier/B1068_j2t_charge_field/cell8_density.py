import sys,os,subprocess,sympy as sp
HERE=os.path.dirname(os.path.abspath(__file__))
primes=[p for p in sp.primerange(200,1000) if p%3==1]
res={}
for p in primes:
    try:
        out=subprocess.run([sys.executable,os.path.join(HERE,"cell6_pure.py"),str(p)],
                           capture_output=True,text=True,timeout=600).stdout
        line=[l for l in out.splitlines() if "omega  " in l]
        if not line: continue
        n=int(line[0].split("pure points")[1].split("at")[0].strip())
        res[p]=n
        print(f"  p={p:4d} -> {n}", flush=True)
    except Exception:
        pass
s=sum(1 for v in res.values() if v==2); t=len(res)
print(f"\nSPLIT DENSITY: {s}/{t} = {s/t:.3f}")
print("  a QUADRATIC extension splits with density 1/2")
print("  1/3 -> cubic ; 1/6 -> S3 sextic ; 1/4 -> biquadratic ; 1/10 -> degree-10ish")
print(f"  observed {s/t:.3f} -> consistent with 1/{round(t/s) if s else 'inf'}")
