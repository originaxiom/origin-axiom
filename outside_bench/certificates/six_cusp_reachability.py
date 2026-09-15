import snappy, sys
base=snappy.Manifold('m004')
print("max cusp count of m004's covers, by degree (B1295 went to 10):")
best={}
covers={}
for deg in range(2,13):
    try: cs_=base.covers(deg)
    except Exception as e:
        print(f"  degree {deg}: enumeration failed"); continue
    mx=0; store=[]
    for C in cs_:
        n=C.num_cusps()
        mx=max(mx,n)
        if n>=6: store.append(C)
    best[deg]=(len(cs_),mx)
    covers[deg]=store
    print(f"  degree {deg:>2}: {len(cs_):>3} covers, max cusps = {mx}"
          + (f"   <-- {len(store)} cover(s) with >=6 cusps" if store else ""), flush=True)
have=[ (d,C) for d,lst in covers.items() for C in lst ]
print(f"\ncovers with >= 6 cusps found: {len(have)}")
if not have:
    print("NONE to degree 12 -> the six-cusp target is NOT reachable in this range.")
    sys.exit()
