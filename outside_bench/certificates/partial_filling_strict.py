import snappy
# The logic being tested: B1227 gives amphichiral => 2*CS = 0 in R/(1/2)Z => CS in {0, 1/4}.
# Contrapositive: CS not in {0, 1/4} (mod 1/2)  =>  NOT amphichiral.
def offend(c):
    c=float(c)%0.5
    return min(abs(c-0.0),abs(c-0.25),abs(c-0.5))
base=snappy.Manifold('m004')
strict=[]; loose=[]
for deg in range(4,9):
    for C in base.covers(deg):
        if C.num_cusps()<2: continue
        for slope in [(1,0),(1,1),(2,1),(3,1),(1,2),(3,2)]:
            N=C.copy()
            try: N.dehn_fill(slope,0)
            except Exception: continue
            st=str(N.solution_type())
            try: c=float(N.chern_simons()); v=float(N.volume())
            except Exception: continue
            unf=sum(1 for i in N.cusp_info('is_complete') if i)
            if unf<1: continue
            d=offend(c)
            rec=(deg,C.num_cusps(),slope,unf,st,c,v,d)
            loose.append(rec)
            if st=='all tetrahedra positively oriented' and d>1e-6: strict.append(rec)
print("STRICT TEST: positively-oriented geometric solution, >=1 cusp left,")
print("             and CS NOT in {0, 1/4} mod 1/2 (so amphichirality is genuinely broken)\n")
print(f"  {'deg':>3} {'cusps':>5} {'fill':>7} {'left':>4} {'volume':>12} {'CS':>13} {'dist to {0,1/4}':>16}")
seen=set()
for r in strict:
    k=(r[0],r[1],r[2])
    if k in seen: continue
    seen.add(k)
    print(f"  {r[0]:>3} {r[1]:>5} {str(r[2]):>7} {r[3]:>4} {r[6]:>12.7f} {r[5]:>+13.9f} {r[7]:>16.6f}")
print(f"\n  candidates surviving the STRICT test : {len(strict)}  (of {len(loose)} that returned a CS at all)")
print(f"  distinct (degree, cusps, slope) triples: {len(seen)}")
# control: the base object must FAIL the test
c0=float(base.chern_simons())
print(f"\n  CONTROL -- m004 itself: CS = {c0:.3e}, dist to {{0,1/4}} = {offend(c0):.3e}"
      f"  -> {'FAILS (correct: it IS amphichiral)' if offend(c0)<1e-6 else 'PASSES (WRONG)'}")
# control: an unfilled multi-cusped cover must also FAIL
for C in base.covers(5):
    if C.num_cusps()>=2:
        cc=float(C.chern_simons())
        print(f"  CONTROL -- unfilled deg-5 cover ({C.num_cusps()} cusps): CS = {cc:.3e},"
              f" dist = {offend(cc):.3e} -> {'FAILS (correct: covers inherit CS=0)' if offend(cc)<1e-6 else 'PASSES (WRONG)'}")
        break
