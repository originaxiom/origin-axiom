"""S12: at which levels does the figure-eight knot group contain the principal congruence subgroup of PSL(2,O_3)?
Riley's representation a=[[1,1],[0,1]], b=[[1,0],[-w,1]], w^2+w+1=0 (a length-10 relator, the figure-eight's).
Gamma contains Gamma(I) iff [PSL(2,O/I) : image(Gamma)] = [PSL(2,O) : Gamma] = 12, with PSL(2,O/I) = SL(2,O/I)/{+-1}.
Result: index 1 at (sqrt-3),(3); 6 at (2); 12 at (4) and (8)  => level (4).   Run: sage -python congruence_levels.py"""
from sage.all import *
K=QuadraticField(-3,'s'); s=K.gen(); w=(-1+s)/2
a=matrix(K,[[1,1],[0,1]]); b=matrix(K,[[1,0],[-w,1]]); I2=identity_matrix(K,2)
def image_size(J, cap=200000):
    J=K.ideal(J)
    def red(m): return matrix(K,[[J.reduce(m[i,j]) for j in range(2)] for i in range(2)])
    def key(m):
        m1=red(m); m2=red(-m); return min(str(m1.list()), str(m2.list()))
    gens=[a,b,a**-1,b**-1]; seen={key(I2)}; frontier=[red(I2)]
    while frontier:
        nxt=[]
        for m in frontier:
            for g in gens:
                mm=red(m*g); k=key(mm)
                if k not in seen: seen.add(k); nxt.append(mm)
        frontier=nxt
        if len(seen)>cap: return None
    return len(seen)
def psl_order(J):
    J=K.ideal(J); N=J.norm(); o=QQ(N)**3
    for P,e in J.factor(): o*=(1-QQ(1)/P.norm()**2)
    o=Integer(o); return o//2 if (K(2) not in J) else o
if __name__=='__main__':
    for J,name in [(s,'(sqrt-3)'),(2,'(2)'),(3,'(3)'),(4,'(4)'),(8,'(8)')]:
        im=image_size(J); po=psl_order(J); idx=(po/im) if im else None
        print('level %-9s |PSL(2,O/I)|=%-7s |image|=%-7s index=%-5s contains Gamma(I): %s'%(name,po,im,idx,idx==12), flush=True)
