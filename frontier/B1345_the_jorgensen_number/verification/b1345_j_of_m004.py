"""Minimise the Jorgensen quantity over short word pairs -- this estimates J(Gamma) honestly."""
import warnings; warnings.filterwarnings("ignore")
import snappy, itertools

def cx(v):
    try: return complex(v)
    except Exception: return complex(float(v.real()), float(v.imag()))

def words(gens, maxlen):
    alpha = [g for g in gens] + [g.upper() for g in gens]
    out = []
    for L in range(1, maxlen+1):
        for w in itertools.product(alpha, repeat=L):
            s = "".join(w)
            if any(s[i].lower() == s[i+1].lower() and s[i] != s[i+1] for i in range(len(s)-1)):
                continue                       # drop obvious cancellations
            out.append(s)
    return out

def jmin(name, maxlen=3, report=True):
    M = snappy.ManifoldHP(name); G = M.fundamental_group()
    inv = lambda X: type(X)([[X[1,1], -X[0,1]], [-X[1,0], X[0,0]]])
    W = words(G.generators(), maxlen)
    mats = {}
    for w in W:
        try: mats[w] = G.SL2C(w)
        except Exception: pass
    best = None
    for a, b in itertools.combinations(mats, 2):
        A, B = mats[a], mats[b]
        trA = cx(A[0,0]+A[1,1])
        C = A*B*inv(A)*inv(B); trC = cx(C[0,0]+C[1,1])
        if abs(trC - 2) < 1e-9: continue                    # elementary / commuting: excluded
        J = abs(trA**2 - 4) + abs(trC - 2)
        if best is None or J < best[0]: best = (J, a, b, trA, trC)
    if report:
        J,a,b,trA,trC = best
        print(f"  {name:9s} J_min over |w| <= {maxlen}: {J:.15f}   at ({a},{b})")
        print(f"      tr A = {trA:.12f}  ->  |tr^2A - 4| = {abs(trA**2-4):.3e}")
        print(f"      tr[A,B] - 2 = {trC-2:.12f}  ->  modulus {abs(trC-2):.15f}")
    return best[0]

print("=== m004: minimise over word pairs ===")
for L in (2,3,4):
    j = jmin("m004", L, report=(L==4))
    print(f"   maxlen {L}: J_min = {j:.15f}    == 1? {abs(j-1)<1e-12}")
