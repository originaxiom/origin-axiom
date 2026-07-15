import mpmath as mp
from numeric import apply_word, jac_numeric, solve_fixed
import random

mp.mp.dps = 60

def process(word, trials=80, seed=1):
    random.seed(seed)
    found = []
    for trial in range(trials):
        x0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        y0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        z0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        sol = solve_fixed(word, x0,y0,z0)
        if sol is None: continue
        x,y,z = sol
        if abs(x)<1e-6 and abs(y)<1e-6 and abs(z)<1e-6:
            continue
        dup=False
        for s2 in found:
            if abs(s2[0]-x)<1e-15 and abs(s2[1]-y)<1e-15 and abs(s2[2]-z)<1e-15:
                dup=True;break
        if not dup:
            found.append((x,y,z))
    results=[]
    for s in found:
        J = jac_numeric(word, s)
        ev = mp.eig(J, left=False, right=False)
        ev_sorted = sorted(ev, key=lambda v: abs(v.real-1)+abs(v.imag))
        nontrivial = [v for v in ev if abs(v-1) > 1e-6]
        if len(nontrivial)==2:
            Jsum = nontrivial[0]+nontrivial[1]
        else:
            Jsum = None
        results.append((s, ev, Jsum))
    return results

if __name__=='__main__':
    import sys
    word = sys.argv[1]
    res = process(word)
    print(f"word={word}, #fixed pts found (nontrivial): {len(res)}")
    seen_J = set()
    for s,ev,Jsum in res:
        if Jsum is not None:
            key = round(Jsum.real,8)
            if key not in seen_J:
                seen_J.add(key)
                print("  J =", Jsum)
