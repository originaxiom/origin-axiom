import sys,importlib.util,numpy as np,random,os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'B1617_the_weave_at_tau_omega', 'verification'))
sys.path.insert(0,os.getcwd())
spec=importlib.util.spec_from_file_location('om','weave_at_omega.py');om=importlib.util.module_from_spec(spec);spec.loader.exec_module(om)
def red(w):
    out=[]
    for c in w:
        if out and out[-1]==c.swapcase(): out.pop()
        else: out.append(c)
    return ''.join(out)
def sub(auto,w):
    out=''
    for c in w:
        im=auto[c.lower()]
        out+= im if c.islower() else ''.join(x.swapcase() for x in reversed(im))
    return red(out)
def comp(f,g): return {k:sub(f,g[k]) for k in 'ab'}  # f after g
L={"a":"a","b":"ab"};R={"a":"ab","b":"b"}
# test the multiplicativity of M_of on positive words: M(f g) vs M(f) M(g) or M(g)M(f)
random.seed(2);bad_sign=0;ok=0;none=0
for t in range(200):
    f=random.choice([L,R]);g=random.choice([L,R])
    for _ in range(random.randint(0,3)): g=comp(random.choice([L,R]),g)
    fg=comp(f,g)
    A,B,C=om.M_of(f),om.M_of(g),om.M_of(fg)
    if A is None or B is None or C is None: none+=1;continue
    cands=[A@B,B@A]
    if any(np.allclose(C,x) for x in cands): ok+=1
    elif any(np.allclose(C,-x) for x in cands): bad_sign+=1
    else: none+=1
print("pointwise M_of on positive words: product law holds",ok,"; fails by exact sign -1:",bad_sign,"; other/None:",none)
