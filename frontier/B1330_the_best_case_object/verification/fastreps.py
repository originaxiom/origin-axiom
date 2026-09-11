"""Table-driven SL(2,p) hom enumeration. 336^3 brute force is hopeless in Python;
precompute the Cayley table and vectorise the last generator with numpy."""
import numpy as np

def build(p):
    els=[(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
    idx={e:i for i,e in enumerate(els)}; n=len(els)
    def mul(x,y):
        a,b,c,d=x; e,f,g,h=y
        return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
    MUL=np.empty((n,n),dtype=np.int32)
    for i,x in enumerate(els):
        row=MUL[i]
        for j,y in enumerate(els): row[j]=idx[mul(x,y)]
    I=idx[(1,0,0,1)]
    INV=np.empty(n,dtype=np.int32)
    for i in range(n):
        INV[i]=int(np.where(MUL[i]==I)[0][0])
    return els,idx,MUL,INV,I,n

def word_vec(word, fixed, varying_letter, MUL, INV, I, n):
    """Evaluate `word` for every value of the varying generator at once.
    `fixed` maps letters -> element index; the varying letter ranges over 0..n-1."""
    cur=np.full(n, I, dtype=np.int32)
    vals=np.arange(n,dtype=np.int32)
    for ch in word:
        g=ch.lower()
        if g==varying_letter:
            step = vals if ch.islower() else INV[vals]
            cur = MUL[cur, step]
        else:
            e = fixed[g] if ch.islower() else int(INV[fixed[g]])
            cur = MUL[cur, e]
    return cur

def homs_3gen(gens, rels, p):
    """all homomorphisms for a 3-generator presentation, as dicts of element indices"""
    els,idx,MUL,INV,I,n = build(p)
    ga,gb,gc = gens
    out=[]
    for ia in range(n):
        for ib in range(n):
            fixed={ga:ia, gb:ib}
            ok=None
            for r in rels:
                v=word_vec(r, fixed, gc, MUL, INV, I, n)
                m=(v==I)
                ok = m if ok is None else (ok & m)
                if not ok.any(): break
            if ok is not None and ok.any():
                for ic in np.where(ok)[0]:
                    out.append({ga:ia, gb:ib, gc:int(ic)})
    return out, els, idx, MUL, INV, I, n

def homs_2gen(gens, rels, p):
    els,idx,MUL,INV,I,n = build(p)
    ga,gb = gens
    out=[]
    for ia in range(n):
        fixed={ga:ia}
        ok=None
        for r in rels:
            v=word_vec(r, fixed, gb, MUL, INV, I, n)
            m=(v==I)
            ok = m if ok is None else (ok & m)
            if not ok.any(): break
        if ok is not None and ok.any():
            for ib in np.where(ok)[0]:
                out.append({ga:ia, gb:int(ib)})
    return out, els, idx, MUL, INV, I, n
