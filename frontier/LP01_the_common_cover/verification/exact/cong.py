# exact Z[w] (w^2 = -1 - w) as pairs (x, y) = x + y w
def add(u,v): return (u[0]+v[0],u[1]+v[1])
def neg(u): return (-u[0],-u[1])
def mul(u,v): x,y=u; s,t=v; return (x*s - y*t, x*t + y*s - y*t)
W=(0,1); ONE=(1,0); ZERO=(0,0)
def M(a,b,c,d): return (a,b,c,d)
def mm(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))
def minv(X): a,b,c,d=X; return (d,neg(b),neg(c),a)
z6=(1,1) # zeta6 = 1 + w
m004={'a':M(W,ONE,neg(z6),(-1,0)), 'b':M(ONE,(2,0),neg(z6),(-1,-2))}
m202={'a':M(mul((-2,0),z6),add((-1,0),neg(z6)),z6,z6), 'b':M(neg(z6),z6,add((-1,0),z6),ZERO)}
def word(rep,w):
    X=(ONE,ZERO,ZERO,ONE)
    for ch in w: X=mm(X, rep[ch] if ch.islower() else minv(rep[ch.lower()]))
    return X
I=(ONE,ZERO,ZERO,ONE); mI=((-1,0),ZERO,ZERO,(-1,0))
for nm,rep,rel in [('m004',m004,'aaabABBAb'),('m202',m202,'aabbAbAABBaB')]:
    R=word(rep,rel); print(nm,'relator ->', 'I' if R==I else '-I' if R==mI else R)
    for g in rep: a,b,c,d=rep[g]; print('  det',g, add(mul(a,d),neg(mul(b,c))))
