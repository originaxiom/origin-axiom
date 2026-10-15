import math
exec(open("s2.py").read().split("for w in")[0])
def h2(w):
    best=None
    for i in range(len(w)):
        A,B,C,D=word(w[i:]+w[:i]); m=min(abs(B),abs(C))
        if best is None or m<best: best=m
    t=sum(word(w)[k] for k in (0,3)); return math.sqrt(t*t-4)/(2*best)
for w in ("LLLRLLRLR","LLLLLLLRLLLLR","LLLLLLRLLLLLLRLR","LLLLRLLRLLLRLLR","LLLRLRLLLRLRLR","LLLRLRRR"):
    print(w, round(h2(w),3), round(true_height(w,150)[0],3))
def lyndon(n, alphabet="LR"):
    k=len(alphabet); w=[-1]
    while w:
        w[-1]+=1; m=len(w); yield "".join(alphabet[i] for i in w)
        while len(w)<n: w.append(w[len(w)-m])
        while w and w[-1]==k-1: w.pop()
low={}; short={}
for w in lyndon(16):
    if len(w)<2: continue
    A,B,C,D=word(w)
    for N in (5,7):
        for eps in (1,-1):
            ok=False
            for a in range(N):
                for b in range(N):
                    if (a,b)==(0,0) or math.gcd(math.gcd(a,b),N)!=1: continue
                    if ((a*D+b*B)-eps*a)%N or ((a*C+b*A)-eps*b)%N: continue
                    if (C*a*a+(A-D)*a*b-B*b*b) % (N*N)==0: ok=True
            if ok:
                h=h2(w)
                if (N,eps) not in low or h<low[(N,eps)][1]: low[(N,eps)]=(w,h)
print("true lowest-height closing threads (len<=16):",{k:(v[0],round(v[1],2)) for k,v in sorted(low.items())})
