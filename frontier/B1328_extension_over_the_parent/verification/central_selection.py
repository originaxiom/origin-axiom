import itertools
def cyc(n):
    return list(range(n)),(lambda x,y:(x+y)%n),0,(lambda x:(-x)%n),f"C{n}"
def prod2(G,H):
    (ea,ma,ia,va,na)=G; (eb,mb,ib,vb,nb)=H
    els=[(x,y) for x in ea for y in eb]
    return els,(lambda p,q:(ma(p[0],q[0]),mb(p[1],q[1]))),(ia,ib),(lambda p:(va(p[0]),vb(p[1]))),f"{na}x{nb}"
def quat8():
    # Q8 as units in the quaternion group, via 2x2 matrices over F_3? use explicit table
    els=['1','-1','i','-i','j','-j','k','-k']
    T={('1',x):x for x in els}
    def sgn(s): return (-1 if s.startswith('-') else 1, s.lstrip('-'))
    base={('i','j'):'k',('j','k'):'i',('k','i'):'j',('j','i'):'-k',('k','j'):'-i',('i','k'):'-j',
          ('i','i'):'-1',('j','j'):'-1',('k','k'):'-1'}
    def mul(x,y):
        sx,bx=sgn(x); sy,by=sgn(y); s=sx*sy
        if bx=='1': r=by
        elif by=='1': r=bx
        else:
            r=base[(bx,by)]
            if r.startswith('-'): s=-s; r=r[1:]
        if r=='1' and s==-1: return '-1'
        if r=='-1': s=-s; r='1'
        return ('-' if s==-1 else '')+r
    inv={x:next(y for y in els if mul(x,y)=='1') for x in els}
    return els,mul,'1',(lambda x:inv[x]),'Q8'
def dih(n):
    els=[(r,f) for r in range(n) for f in (0,1)]
    def mul(x,y):
        r1,f1=x; r2,f2=y
        return ((r1 + (r2 if f1==0 else -r2))%n,(f1+f2)%2)
    inv={x:next(y for y in els if mul(x,y)==(0,0)) for x in els}
    return els,mul,(0,0),(lambda x:inv[x]),f"D{n}"
def sl2(p):
    els=[(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
    def mul(x,y):
        a,b,c,d=x; e,f,g,h=y
        return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
    I=(1,0,0,1); inv={}
    for x in els:
        for y in els:
            if mul(x,y)==I: inv[x]=y; break
    return els,mul,I,(lambda x:inv[x]),f"SL(2,{p})"

M000_REL=["aabbAB"]; M004_REL=["aaabABBAb"]; SCHREIER=["aA","bA","aa","ab"]
def run(G):
    els,mul,idt,inv,name=G; n=len(els)
    def ev(w,img):
        r=idt
        for ch in w: r=mul(r, img[ch.lower()] if ch.islower() else inv(img[ch.lower()]))
        return r
    def gen(gs):
        seen={idt}; fr=[idt]
        while fr:
            nx=[]
            for u in fr:
                for g in gs:
                    v=mul(u,g)
                    if v not in seen: seen.add(v); nx.append(v)
            fr=nx
        return seen
    centre=[z for z in els if all(mul(z,x)==mul(x,z) for x in els)]
    c2=[z for z in centre if mul(z,z)==idt]
    s000=[{'a':x,'b':y} for x,y in itertools.product(els,repeat=2)
          if all(ev(r,{'a':x,'b':y})==idt for r in M000_REL) and len(gen([x,y]))==n]
    s004=sum(1 for x,y in itertools.product(els,repeat=2)
             if all(ev(r,{'a':x,'b':y})==idt for r in M004_REL) and len(gen([x,y]))==n)
    restr={}
    for img in s000: restr.setdefault(tuple(ev(s,img) for s in SCHREIER),[]).append(img)
    fib=sorted(set(len(v) for v in restr.values())) or [0]
    pred=len(c2)
    ok = (not s000) or (fib==[pred])
    print(f"{name:10s} |Q|={n:4d} |Z(Q)[2]|={pred:2d}  Surj(m000)={len(s000):4d} Surj(m004)={s004:4d} "
          f"restr={len(restr):4d} fibre={str(fib):7s} predicted={pred}  {'OK' if ok else '*** RULE FAILS ***'}")
for G in [cyc(2),cyc(3),cyc(4),cyc(6),cyc(8),cyc(12),prod2(cyc(2),cyc(2)),prod2(cyc(2),cyc(4)),
          quat8(),dih(4),dih(6),sl2(3),sl2(5)]:
    run(G)

print()
print("=== CORRECTED RULE: fibre = #{ z in Z(Q)[2] : z.phi is STILL SURJECTIVE } ===")
def run2(G):
    els,mul,idt,inv,name=G; n=len(els)
    def ev(w,img):
        r=idt
        for ch in w: r=mul(r, img[ch.lower()] if ch.islower() else inv(img[ch.lower()]))
        return r
    def gen(gs):
        seen={idt}; fr=[idt]
        while fr:
            nx=[]
            for u in fr:
                for g in gs:
                    v=mul(u,g)
                    if v not in seen: seen.add(v); nx.append(v)
            fr=nx
        return seen
    centre=[z for z in els if all(mul(z,x)==mul(x,z) for x in els)]
    c2=[z for z in centre if mul(z,z)==idt]
    s000=[{'a':x,'b':y} for x,y in itertools.product(els,repeat=2)
          if all(ev(r,{'a':x,'b':y})==idt for r in M000_REL) and len(gen([x,y]))==n]
    if not s000:
        print(f"{name:10s} no surjection -- the mechanism has no content here"); return True
    restr={}
    for img in s000: restr.setdefault(tuple(ev(s,img) for s in SCHREIER),[]).append(img)
    fib=sorted(set(len(v) for v in restr.values()))
    # predicted: for each phi, how many central involutions keep it surjective (w(a)=w(b)=1)
    preds=set()
    for img in s000:
        k=sum(1 for z in c2 if len(gen([mul(z,img['a']),mul(z,img['b'])]))==n)
        preds.add(k)
    ok = fib==sorted(preds)
    print(f"{name:10s} |Z(Q)[2]|={len(c2)}  observed fibre={fib}  predicted={sorted(preds)}  {'OK' if ok else '*** FAILS ***'}")
    return ok
allok=True
for G in [cyc(2),cyc(3),cyc(4),cyc(6),cyc(8),cyc(12),prod2(cyc(2),cyc(2)),prod2(cyc(2),cyc(4)),
          quat8(),dih(4),dih(6),sl2(3),sl2(5)]:
    allok &= run2(G)
print()
print("corrected rule holds on every group tested:", allok)
