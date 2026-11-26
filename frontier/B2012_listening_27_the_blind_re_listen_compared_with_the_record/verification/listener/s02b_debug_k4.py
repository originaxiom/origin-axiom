# s02b_debug_k4.py -- why did the float search miss some k=4 orbits? BFS from torsion points directly.
import math
def key(p): return tuple(int(round(c*1e8)) for c in p)
def moves(p):
    x, y, z = p
    return [(x, z, x*z-y), (z, y, y*z-x), (x, x*y-z, y), (x*y-z, y, x)]
def orbit(c, cap=20000):
    orb = {key(c): c}; st = [c]
    while st:
        p = st.pop()
        for q in moves(p):
            kq = key(q)
            if kq not in orb:
                orb[kq] = q; st.append(q)
                if len(orb) > cap: return None
    return orb
for N in range(1, 21):
    t = 2*math.cos(2*math.pi/N)
    o = orbit((t, 2.0, t))
    print(N, None if o is None else len(o), "max|coord|=%.3e" % (max(max(abs(c) for c in p) for p in o.values()) if o else -1))
