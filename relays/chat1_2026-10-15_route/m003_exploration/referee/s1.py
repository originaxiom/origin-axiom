import math, itertools
def word(w):
    A,B,C,D = 1,0,0,1
    for ch in w:
        if ch=="L": A,B,C,D = A+B,B,C+D,D
        else: A,B,C,D = A,A+B,C,C+D
    return A,B,C,D
def lines(g,N,eps):
    A,B,C,D=g
    return [(a,b) for a in range(N) for b in range(N) if (a,b)!=(0,0) and math.gcd(math.gcd(a,b),N)==1
            and ((a*D+b*B)-eps*a)%N==0 and ((a*C+b*A)-eps*b)%N==0]
want = {}
for n in range(2,11):
    for t in itertools.product("LR", repeat=n):
        w="".join(t); g=word(w); A,B,C,D=g
        if C>30 or C==0: continue
        for N in (13,15,9,25,21):
            for eps in (1,-1):
                for (a,b) in lines(g,N,eps):
                    Q=C*a*a+(A-D)*a*b-B*b*b; c=(eps*Q//N)%N
                    kind = "b0" if b==0 else ("a0" if a==0 else "gen")
                    key=(N,eps,kind)
                    if c!=0 and key not in want: want[key]=(w,g,(a,b),c)
for k,v in sorted(want.items()): print(k,v)
