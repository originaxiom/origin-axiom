import snappy,warnings,cmath,math,json,sys;warnings.filterwarnings('ignore')
def mm(X,Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0],X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],[X[1][0]*Y[0][0]+X[1][1]*Y[1][0],X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def inv(X): return [[X[1][1],-X[0][1]],[-X[1][0],X[0][0]]]
def toO3(z):
    y=z.imag/(math.sqrt(3)/2); x=z.real+y/2
    if abs(x-round(x))<1e-6 and abs(y-round(y))<1e-6: return (round(x),round(y))
    return None
def exact(name):
    M=snappy.ManifoldHP(name); G=M.fundamental_group()
    def mat(w):
        X=G.SL2C(w); return [[complex(X[0,0]),complex(X[0,1])],[complex(X[1,0]),complex(X[1,1])]]
    gens=G.generators()
    for mer,lon in G.peripheral_curves():
        P=mat(mer); a,b,c,d=P[0][0],P[0][1],P[1][0],P[1][1]
        if abs(c)<1e-9: C=[[1,0],[0,1]]
        else:
            z=(a-d)/(2*c); C=[[0,-1],[1,-z]]
        Pc=mm(mm(C,P),inv(C))
        base=Pc[0][1]*Pc[0][0]
        # try scalings s so that translation becomes small O3 element
        for t in [1,2,3,(1,1),(2,1),(1,2),(0,1),(3,0)]:
            tz=t if isinstance(t,int) else t[0]+t[1]*complex(-0.5,math.sqrt(3)/2)
            lam=cmath.sqrt(base/tz); D=[[1/lam,0],[0,lam]]
            for shift in [0, 0.5, complex(0,math.sqrt(3)/6), complex(0.5,math.sqrt(3)/6)]:
                Tm=[[1,shift],[0,1]]
                ex={}
                ok=True
                for g in gens:
                    Y=mm(mm(Tm,mm(mm(D,mm(mm(C,mat(g)),inv(C))),inv(D))),inv(Tm))
                    e=[toO3(Y[i][j]) for i in range(2) for j in range(2)]
                    if None in e: ok=False;break
                    ex[g]=e
                if ok: return {'gens':gens,'rels':G.relators(),'rep':ex}
    return None
for n in sys.argv[1:]:
    print(n, json.dumps(exact(n)))
