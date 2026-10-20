import itertools, io, contextlib
def red(w):
    o=[]
    for c in w:
        if o and o[-1]==c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def inv(w): return "".join(c.swapcase() for c in reversed(w))
def is_basis(u,v):
    u,v=red(u),red(v)
    seen=set()
    while True:
        best=(len(u)+len(v),u,v)
        for x,y in ((u,v),(v,u)):
            for yy in (y,inv(y)):
                for cand in (red(x+yy),red(yy+x)):
                    pair=(cand,y) if (x,y)==(u,v) else (y,cand) if False else None
        # simpler: enumerate replacements of u by u*v^±, v^±*u and v by v*u^±, u^±*v
        opts=[]
        for yy in (v,inv(v)):
            opts += [(red(u+yy),v),(red(yy+u),v)]
        for yy in (u,inv(u)):
            opts += [(u,red(v+yy)),(u,red(yy+v))]
        m=min(opts,key=lambda p:len(p[0])+len(p[1]))
        if len(m[0])+len(m[1])<len(u)+len(v): u,v=m
        else: break
    return len(u)==1 and len(v)==1 and {u.lower(),v.lower()}=={"a","b"}
pos=["".join(w) for L in range(1,5) for w in itertools.product("ab",repeat=L)]
def idet(u,v): return u.count("a")*v.count("b")-u.count("b")*v.count("a")
n_det1=0;n_basis=0;ex=[]
for u in pos:
    for v in pos:
        if idet(u,v)==1:
            n_det1+=1
            if is_basis(u,v): n_basis+=1
            elif len(ex)<8: ex.append((u,v))
print("positive pairs len<=4 with abelianised det = 1:",n_det1,"; of them bases of F2 (automorphisms):",n_basis)
print("examples of det-1 pairs that are NOT bases (non-invertible endomorphisms):",ex)
