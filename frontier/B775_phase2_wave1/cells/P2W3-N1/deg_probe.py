import time
from probe_forward import child_irreducibles
from sympy import Poly, symbols
x=symbols('x')
p=5
seed=Poly(x**2-x-1,x,modulus=p)
frontier=[tuple(int(c)%p for c in f.monic().all_coeffs()) for f,_ in seed.factor_list()[1]]
known=set(frontier)
level=0
while frontier and level<15:
    t0=time.time()
    nxt=[]
    for q in frontier:
        for c in child_irreducibles([int(v) for v in q],p):
            if c not in known:
                known.add(c); nxt.append(c)
    maxd=max((len(k)-1 for k in known),default=0)
    print(f'level {level}: frontier_in={len(frontier)} new={len(nxt)} total_known={len(known)} maxdeg={maxd} ({time.time()-t0:.2f}s)',flush=True)
    frontier=nxt; level+=1
print('final known',len(known),flush=True)
