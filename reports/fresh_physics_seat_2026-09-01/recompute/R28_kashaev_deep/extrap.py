import mpmath as mp, json
mp.mp.dps=200
d=json.load(open("S_values.json")); Ns=sorted(int(k) for k in d); Sv={N:mp.mpf(d[str(N)]) for N in Ns}
C0=mp.mpf(3)**mp.mpf(-0.25); pi=mp.pi; r3=mp.sqrt(3)
bank={1:mp.mpf(11)/108*r3*pi*C0, 2:mp.mpf(697)/7776*pi**2*C0, 3:mp.mpf(724351)/12597120*r3*pi**3*C0, 4:mp.mpf(278392949)/1813985280*pi**4*C0}
def fit(nodes,M):
    A=mp.matrix([[mp.mpf(1)/mp.mpf(N)**k for k in range(M)] for N in nodes]); b=mp.matrix([Sv[N] for N in nodes])
    return mp.lu_solve(A,b)
def digits(a,b): return int(-mp.log10(abs(a-b)/abs(b)))
res={}
for M in [12,16,20,24,28,30]:
    subsets=[Ns[-M:], Ns[:M], Ns[::2][:M] if len(Ns[::2])>=M else Ns[-M:]]
    fits=[fit(s,M) for s in subsets]
    line=[]
    for k in range(5):
        vals=[f[k] for f in fits]
        stab=int(-mp.log10(max(abs(v-vals[0]) for v in vals[1:])/abs(vals[0]))) if len(set(map(str,subsets)))>1 else -1
        match=digits(vals[0],bank[k]) if k else digits(vals[0],C0)
        line.append((k,mp.nstr(vals[0],30),stab,match))
    res[M]=line
    print("M=",M); [print("  k=%d %s  stable=%d  matchbank=%d"%l) for l in line]
