import snappy, json
def tau_of(divs):
    t=0
    for d in divs:
        if d==0: continue
        n=d
        while n%2==0: n//=2
        if n!=d: t+=1
    return t
C=snappy.OrientableClosedCensus
print("closed census", len(C), flush=True)
rows=[]
for i,M in enumerate(C):
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
        divs=[d for d in M.homology().elementary_divisors() if d!=0]
        t=tau_of(divs)
        cs=float(M.chern_simons())%1.0          # SAME object, no re-instantiation
        d0=min(cs,1.0-cs); dh=abs(cs-0.5)
        cls="0" if d0<1e-7 else ("1/2" if dh<1e-7 else f"{cs:.6f}")
        rows.append((str(M), str(M.homology()), t, cls))
    except Exception: pass
    if (i+1)%2000==0: print(f"  {i+1} amph={len(rows)}", flush=True)
json.dump(rows, open('closedaps.json','w'))
pred=lambda t: "1/2" if t%2 else "0"
ok=sum(1 for r in rows if r[3]==pred(r[2]))
print(f"\n=== APS  cs = tau/2 mod 1  on CLOSED amphichiral manifolds ===")
for r in sorted(rows,key=lambda r:(r[2]%2,r[0])):
    print(f"  {r[0]:24s} H1={r[1]:22s} tau={r[2]} {'odd ' if r[2]%2 else 'even'} "
          f"cs mod 1={r[3]:10s} pred={pred(r[2]):4s} {'OK' if r[3]==pred(r[2]) else 'MISMATCH'}")
print(f"\n  agree {ok}/{len(rows)}")
