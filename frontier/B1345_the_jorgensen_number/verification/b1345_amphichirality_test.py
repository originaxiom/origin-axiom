"""Does |z| = 1 track AMPHICHIRALITY? Callahan's own uniqueness theorem answers it."""
import warnings; warnings.filterwarnings("ignore")
import snappy, itertools
def cx(v):
    try: return complex(v)
    except Exception: return complex(float(v.real()), float(v.imag()))
def jmin(M, maxlen=4):
    G = M.fundamental_group()
    inv = lambda X: type(X)([[X[1,1],-X[0,1]],[-X[1,0],X[0,0]]])
    alpha = [g for g in G.generators()]+[g.upper() for g in G.generators()]
    W=[]
    for L in range(1,maxlen+1):
        for w in itertools.product(alpha,repeat=L):
            s="".join(w)
            if any(s[i].lower()==s[i+1].lower() and s[i]!=s[i+1] for i in range(len(s)-1)): continue
            W.append(s)
    mats={}
    for w in W:
        try: mats[w]=G.SL2C(w)
        except Exception: pass
    best=None
    for a,b in itertools.combinations(mats,2):
        A,B=mats[a],mats[b]; trA=cx(A[0,0]+A[1,1]); C=A*B*inv(A)*inv(B); trC=cx(C[0,0]+C[1,1])
        if abs(trC-2)<1e-9: continue
        J=abs(trA**2-4)+abs(trC-2)
        if best is None or J<best: best=J
    return best

print("THE TEST: chat1 reads |z| = 1 as 'the arithmetic shadow of amphichirality'.")
print("Callahan's OWN uniqueness theorem says m004 is the ONLY manifold with J = 1.")
print("So any OTHER amphichiral knot must have J > 1 -- which refutes the reading.\n")
print(f"{'knot':8s} {'amphichiral':>12s} {'J':>18s}")
for k in ["4_1","6_3","8_3","8_9","8_12","8_17","8_18","5_2","6_1","7_4"]:
    try:
        M = snappy.ManifoldHP(k)
        try: amph = snappy.Manifold(k).symmetry_group().is_amphicheiral()
        except Exception: amph = "?"
        J = jmin(M, 3)
        print(f"{k:8s} {str(amph):>12s} {J:18.12f}")
    except Exception as e:
        print(f"{k:8s}  ERROR {type(e).__name__}")
