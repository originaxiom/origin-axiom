import sys; sys.path.insert(0,'.')
from ref4 import *
mp.mp.dps = 40
CASES = [("RLRLLLRLR",13,-1,(0,1)), ("LLRLRR",13,1,(1,8)), ("LLLRRR",13,-1,(1,5)), ("LLLRLR",15,-1,(3,8)),
         ("RLRLLLLRRR",15,-1,(0,1)), ("LLLRRLRL",9,-1,(1,0)), ("LLRLLRRL",9,1,(1,0)), ("LLLRLLRLR",25,-1,(1,3)),
         ("LLLLLRLR",21,-1,(3,10)), ("LLLRLRRR",5,1,(1,3)), ("LLLRLRRR",5,1,(2,1))]
CH_ = {"up":(1,-4),"down":(1,2),"lep":(-3,6),"r1":(2,-5),"r2":(4,3)}
worst = 0
for w,N,eps,(a,b) in CASES:
    g = word(w); A,B,C,D = g
    assert ((a*D+b*B)-eps*a)%N==0 and ((a*C+b*A)-eps*b)%N==0
    Q = C*a*a+(A-D)*a*b-B*b*b; c = eps*Q//N
    law, tau = lawfit(g); tg=(A*tau+B)/(C*tau+D); J=C*tau+D
    out=[]
    for nm,(qL,qR) in CH_.items():
        s = qL*qL+qR*qR; pred = mp.exp(-2j*mp.pi*c*s/N)
        vu=(mp.mpf((qL+qR)*b)/N, mp.mpf((qL+qR)*a)/N); vd=(mp.mpf((qL-qR)*b)/N, mp.mpf((qL-qR)*a)/N)
        u0,ug = quat(tau,vu,vd), quat(tg,vu,vd)
        rs = [ug[s_]*mp.sqrt(J)/u0[law[s_][0]]/law[s_][1] for s_ in (1,2,3) if abs(u0[law[s_][0]])>mp.mpf(10)**-25]
        idr = (ug[0]*mp.sqrt(J)/u0[0]/pred) if abs(u0[0])>mp.mpf(10)**-25 else None
        devs = [min(abs(r-pred),abs(r+pred)) for r in rs]; worst=max([worst]+[float(d) for d in devs])
        sg = "".join("+" if abs(r-pred)<abs(r+pred) else "-" for r in rs)
        cl = "C" if (c*s)%N==0 else "x"
        out.append(f"{nm}:{cl}{sg} dev{mp.nstr(max(devs),2)} id:{(mp.nstr(mp.arg(idr)/(2*mp.pi)*8,3)+"/8") if idr is not None else "0"}")
    print(f"{eps:+d}{w} {g} N={N} w=({a},{b}) Q={Q} c={c}: ", "; ".join(out))
print("worst dev up to sign:", worst)
