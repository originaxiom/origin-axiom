import sympy as s
simp=lambda x:x.applyfunc(s.simplify)
I=s.eye(2);A=s.diag(s.I,-s.I);B=s.Matrix([[0,1],[-1,0]]);C=A*B
nL=(I+A)/s.sqrt(2);nR=(I-B)/s.sqrt(2)
pairs=[(1,-1),(-1,-1),(-1,1)]; Q={(1,1):I,(1,-1):A,(-1,1):B,(-1,-1):C}
for name,n in [('L',nL),('R',nR)]:
    Qblocks=s.zeros(6);transformed=s.zeros(6)
    for col,p in enumerate(pairs):
        a,b=p
        pn=(a,a*b) if name=='L' else (a*b,b)
        row=pairs.index(pn)
        if name=='L': M=a*n.inv()*A
        else: M=n.inv()-(b*B-I)*(a*b*A-I).inv()*n.inv()*a*A
        M=simp(M)
        Qblocks[2*row:2*row+2,2*col:2*col+2]=M
        common=simp(Q[pn].inv()*M*Q[p]); transformed[2*row:2*row+2,2*col:2*col+2]=common
        print(name,p,pn,'block common:',common)
    print(name,'raw',Qblocks,'\ncommon',transformed,'\npositive:',transformed.extract([0,2,4],[0,2,4]),'\nnegative:',transformed.extract([1,3,5],[1,3,5]))
