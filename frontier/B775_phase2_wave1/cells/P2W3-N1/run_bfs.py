import time
from probe_forward import child_irreducibles
from sympy import Poly, symbols
from collections import Counter
x=symbols('x')
for p in (5,7):
    seed=Poly(x**2-x-1,x,modulus=p)
    seed_facs=[tuple(int(c)%p for c in f.monic().all_coeffs()) for f,_ in seed.factor_list()[1]]
    known=set(seed_facs); frontier=list(seed_facs); pops=0; t0=time.time()
    while frontier:
        q=frontier.pop(); pops+=1
        for c in child_irreducibles([int(v) for v in q],p):
            if c not in known:
                known.add(c); frontier.append(c)
        if pops%25==0:
            print(f'  p={p} pops={pops} known={len(known)} frontier={len(frontier)} t={time.time()-t0:.1f}s',flush=True)
        if len(known)>5000:
            print(f'  p={p} EXCEEDED 5000',flush=True); break
    degs=sorted(len(k)-1 for k in known)
    print(f'p={p} DONE pops={pops} orbit_size={len(known)} degdist={dict(Counter(degs))} t={time.time()-t0:.1f}s',flush=True)
