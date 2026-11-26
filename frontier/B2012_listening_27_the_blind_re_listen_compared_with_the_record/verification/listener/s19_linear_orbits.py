# s19_linear_orbits.py -- orbits of the linearised groups <dL,dR> on F_p^3 at (0,0,0) and at (2,2,2), to compare with the
# orbits of the full moves mod p^2 inside the fibre over the fixed point (s11 output).
import numpy as np
from collections import Counter
def orbs(M1, M2, p):
    seen = set(); out = []
    for a in range(p):
        for b in range(p):
            for c in range(p):
                v = (a, b, c)
                if v in seen: continue
                st = [v]; o = {v}
                while st:
                    u = st.pop()
                    for M in (M1, M2):
                        w = tuple(int(t) % p for t in np.array(M) @ np.array(u))
                        if w not in o: o.add(w); st.append(w)
                seen |= o; out.append(len(o))
    c = Counter(out)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))
for p in (5, 7, 11):
    print("p=%d  at (0,0,0): %s   |   at (2,2,2): %s" % (p, orbs([[1,0,0],[0,0,1],[0,-1,0]], [[0,0,1],[0,1,0],[-1,0,0]], p),
                                                      orbs([[1,0,0],[0,0,1],[2,-1,2]], [[0,0,1],[0,1,0],[-1,2,2]], p)))
