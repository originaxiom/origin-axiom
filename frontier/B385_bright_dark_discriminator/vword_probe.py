"""B385 continuation -- the accumulated word-shift map v_word(j,l), 5-parts, riddle pair.

Derivation (banked in FINDINGS): D = C.Z^{-8}, WR = X^{-8}.WR_c exactly. Pushing all
Heisenberg insertions T(u) right through canonical lifts via T(u) U(g) = U(g) T(g^{-1}u).phase:
    W_m^j W_m2^l = U_std(gamma') . T(v_word) . phase
with v_word = sum of gLeft^{-1}-transported insertion vectors; insertions per seed-m factor:
X^{-8} carries u=(-8,0) BEFORE the WR_c-lift, Z^{-8} carries u=(0,-8) AFTER the C-lift...
Bookkeeping done stepwise: build the word left-to-right, tracking (gAccum, vAccum):
  state := U_std(gAccum) T(vAccum) phase.  Appending a factor U_std(h) T(u):
  U T(v) U(h) T(u) = U U(h) T(h^{-1}v) T(u) = U_std(g h) T(h^{-1} v + u) phase.
Factors: WR-step = U_std(s) with pre-insertion: X^{-8}.WR_c = T((-8,0)).U_std(s)
       = U_std(s) T(s^{-1}(-8,0)); D-step = C.Z^{-8} = U_std(t) T((0,-8)).
(s = gamma of WR_c = [[1,1],[0,1]], t = gamma of C = [[1,0],[1,1]].)"""
import json, os
from math import gcd

def mm(a,b): return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%15,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%15],
                     [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%15,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%15]]
def minv(g):
    return [[g[1][1]%15, -g[0][1]%15], [-g[1][0]%15, g[0][0]%15]]   # det 1
def mv(g,v): return ((g[0][0]*v[0]+g[0][1]*v[1])%15, (g[1][0]*v[0]+g[1][1]*v[1])%15)

S = [[1,1],[0,1]]   # gamma(WR_c)
T = [[1,0],[1,1]]   # gamma(C)
Si = minv(S)

def append(state, h, u_pre=None, u_post=None):
    """state=(g,v); factor = [T(u_pre)] U_std(h) [T(u_post)]."""
    g, v = state
    if u_pre is not None:
        # T(v)T(u_pre) accumulate BEFORE h: v' = v + u_pre? no: state ends ...T(v); appending
        # T(u_pre)U(h)T(u_post): T(v)T(u_pre)=T(v+u_pre) phase; then push through h.
        v = ((v[0]+u_pre[0])%15, (v[1]+u_pre[1])%15)
    hi = minv(h)
    v = mv(hi, v)
    g = mm(g, h)
    if u_post is not None:
        v = ((v[0]+u_post[0])%15, (v[1]+u_post[1])%15)
    return (g, v)

def seed_step(state, m):
    """append W_m = (X^-8 WR_c)^m (C Z^-8)^m."""
    for _ in range(m):
        state = append(state, S, u_pre=(-8%15,0))
    for _ in range(m):
        state = append(state, T, u_post=(0,-8%15))
    return state

def word_shift(m1, m2, j, l):
    st = ([[1,0],[0,1]], (0,0))
    for _ in range(j): st = seed_step(st, m1)
    for _ in range(l): st = seed_step(st, m2)
    return st

# sanity: gamma of W_m must equal [[1+m^2,m],[m,1]]
for m in (1,2,3,4,5,7):
    g,_ = word_shift(m, 1, 1, 0)
    assert g == [[(1+m*m)%15, m%15],[m%15, 1]], (m, g)
print("gamma sanity ok")

ORDS = {1:20, 2:12, 3:6, 4:20, 5:4, 7:12}
def vmap(m1, m2):
    o1,o2 = ORDS[m1], ORDS[m2]
    out = {}
    for j in range(o1):
        for l in range(o2):
            g,v = word_shift(m1,m2,j,l)
            out[(j,l)] = (g,v)
    return out

def profile(m1,m2):
    vm = vmap(m1,m2)
    p5 = {}
    for (j,l),(g,v) in vm.items():
        v5 = (v[0]%5, v[1]%5)
        p5[v5] = p5.get(v5,0)+1
    return p5

RIDDLE = [(3,4,"bright"), (1,3,"dark")]
res = {}
for m1,m2,st in RIDDLE + [(1,2,"bright"),(1,4,"dark"),(2,3,"bright"),(1,5,"dark"),(4,5,"dark"),(2,7,"bright"),(3,5,"dark"),(2,4,"bright"),(1,7,"bright"),(3,7,"bright")]:
    p = profile(m1,m2)
    zero_frac = p.get((0,0),0)
    tot = sum(p.values())
    supp = sorted(p)
    res[f"{m1},{m2}"] = dict(status=st, support=[list(x) for x in supp],
                             nsupport=len(supp), zero=zero_frac, total=tot)
    print(f"{m1},{m2} {st:7s}: 5-part support size {len(supp):2d}, zero-cells {zero_frac}/{tot}, support {supp[:8]}{'...' if len(supp)>8 else ''}")
# separation scan: support-size / zero-fraction / support-set
for feat in ("nsupport","zero"):
    bv = {res[k][feat] for k in res if res[k]["status"]=="bright"}
    dv = {res[k][feat] for k in res if res[k]["status"]=="dark"}
    print(f"separates by {feat}:", not (bv & dv), " bright:", sorted(bv), " dark:", sorted(dv))
bv = {tuple(map(tuple,res[k]["support"])) for k in res if res[k]["status"]=="bright"}
dv = {tuple(map(tuple,res[k]["support"])) for k in res if res[k]["status"]=="dark"}
print("separates by support-set:", not (bv & dv))
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"vword.json"),"w"), indent=1)
print("DONE")
