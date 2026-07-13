import itertools, math
# ---- stage data (banked pointers) ----
SUB={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}; LET=['a','b','A','B']
chi=[1,3,6,7]; chi3=[(c**3)%11 for c in chi]
lin=lambda m:sum(m[i]*chi[i] for i in range(4))%11
cub=lambda m:sum(m[i]*chi3[i] for i in range(4))%11
AF =lambda m:lin(m)==0 and cub(m)==0

def test_chi3(): assert chi3==[1,5,7,2]

def test_three_casts_anomaly_free():
    for m in ([0,1,1,5],[1,5,1,0],[3,2,1,1]):
        assert sum(m)==7 and AF(m)

def test_exhaustiveness_minimal_total_7():
    counts={T:sum(1 for m in itertools.product(range(T+1),repeat=4) if sum(m)==T and AF(m)) for T in range(1,8)}
    assert counts=={1:0,2:0,3:0,4:0,5:0,6:0,7:3}
    sols=sorted(m for m in itertools.product(range(8),repeat=4) if sum(m)==7 and AF(m))
    assert sols==[(0,1,1,5),(1,5,1,0),(3,2,1,1)]

def test_2131_fails():
    v=[2,1,3,1]; assert lin(v)==8 and not AF(v)

def test_grammar_edges_and_incidence():
    w='a'
    for _ in range(10): w=''.join(SUB[c] for c in w)
    edges=sorted({w[i:i+2] for i in range(len(w)-1)})
    assert edges==['AA','AB','Aa','Ba','aA','ab','bA'] and len(edges)==7
    idx={'a':0,'b':1,'A':2,'B':3}; src=[0]*4; tgt=[0]*4
    for e in edges: src[idx[e[0]]]+=1; tgt[idx[e[1]]]+=1
    assert src==[2,1,3,1] and tgt==[2,1,3,1]   # Eulerian-balanced de Bruijn graph
    assert not AF(src)

def test_image_bigram_counts():
    bg={}
    for c in LET:
        im=SUB[c]
        for i in range(len(im)-1): bg[im[i:i+2]]=bg.get(im[i:i+2],0)+1
    assert bg=={'ab':2,'bA':2,'AA':1,'AB':3,'aA':2}

def test_no_natural_7_structure_anomaly_free():
    for v in ([2,1,3,1],[4,2,4,0],[0,2,5,3],[4,2,5,3],[5,3,4,2]):
        assert not AF(v)

def test_part_i_no_cast_embeds_in_DFib():
    # DFib dims as (rational, phi-coeff), phi^2=1+phi
    DIM=[(1,0),(0,1),(0,1),(1,1)]  # 11,1t,t1,tt
    LAG=[1,0,0,1]                  # unique Lagrangian algebra
    phi=(1+5**0.5)/2; d=[1,phi,phi,phi*phi]
    def prop(n):
        I=[i for i in range(4) if n[i]>0]
        if not I: return True
        c=n[I[0]]/d[I[0]]; return all(abs(n[i]-c*d[i])<1e-9 for i in range(4))
    for cast in ([0,1,1,5],[1,5,1,0],[3,2,1,1]):
        for p in itertools.permutations(range(4)):
            n=[0]*4
            for i in range(4): n[p[i]]=cast[i]
            pcoef=sum(n[i]*DIM[i][1] for i in range(4))
            assert pcoef!=0            # S1: integer total quantum dim fails
            assert n!=LAG              # S3: not the Lagrangian vector
            assert not prop(n)         # S4: not proportional to dim-vector

def test_base_rate():
    comps=[m for m in itertools.product(range(8),repeat=4) if sum(m)==7]
    assert len(comps)==math.comb(10,3)==120
    assert sum(1 for m in comps if AF(m))==3   # 3/120 = 2.5%

if __name__=='__main__':
    for f in list(globals()):
        if f.startswith('test_'): globals()[f](); print('PASS',f)
    print('ALL PASS')