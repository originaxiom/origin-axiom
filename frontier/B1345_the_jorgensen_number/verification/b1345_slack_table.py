import warnings; warnings.filterwarnings("ignore")
import snappy, itertools, math
def cx(v):
    try: return complex(v)
    except Exception: return complex(float(v.real()), float(v.imag()))
def words(gens, maxlen):
    alpha = [g for g in gens] + [g.upper() for g in gens]
    out = []
    for L in range(1, maxlen+1):
        for w in itertools.product(alpha, repeat=L):
            s = "".join(w)
            if any(s[i].lower()==s[i+1].lower() and s[i]!=s[i+1] for i in range(len(s)-1)): continue
            out.append(s)
    return out
def jmin(name, maxlen=4):
    M = snappy.ManifoldHP(name); G = M.fundamental_group()
    inv = lambda X: type(X)([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])
    mats = {}
    for w in words(G.generators(), maxlen):
        try: mats[w] = G.SL2C(w)
        except Exception: pass
    best = None
    for a,b in itertools.combinations(mats,2):
        A,B = mats[a],mats[b]
        trA = cx(A[0,0]+A[1,1]); C = A*B*inv(A)*inv(B); trC = cx(C[0,0]+C[1,1])
        if abs(trC-2) < 1e-9: continue
        J = abs(trA**2-4)+abs(trC-2)
        if best is None or J < best[0]: best = (J,a,b)
    return best

CLAIMED = {"m000":1, "m004":1, "m009":math.sqrt(2), "m136":2*math.sqrt(2), "m003":4, "m206":4,
           "t12835":4, "v2873":3*math.sqrt(3), "s958":7, "m202":7, "t12833":13}
print(f"{'manifold':10s} {'J computed':>18s} {'chat1 claims':>14s}  match   amphichiral")
for nm, claim in CLAIMED.items():
    try:
        J,a,b = jmin(nm, 3)
        M = snappy.Manifold(nm)
        try: amph = M.symmetry_group().is_amphicheiral()
        except Exception: amph = "?"
        ok = abs(J-claim) < 1e-9
        print(f"{nm:10s} {J:18.12f} {claim:14.9f}  {'YES' if ok else 'NO ':5s}  {amph}")
    except Exception as e:
        print(f"{nm:10s}  ERROR {type(e).__name__}: {str(e)[:50]}")
