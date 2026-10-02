# Extra: search for orientation-reversing endomorphisms among short-word substitutions; run C2 on them; relator at q=1
import itertools, random, json
import mpmath as mp
import sympy as sp
exec(open('route2.py').read().split("QS=[")[0])   # reuse defs only (ev, intertwiners, etc.)
from sympy import Rational as R
mp.mp.dps=50
def sl2(z): return (mp.matrix([[1,1],[0,1]]), mp.matrix([[1,0],[z,1]]))
def evmp(word,mats):
    P=mp.eye(2)
    for g,e in word:
        A=mats[0] if g=='m' else mats[1]
        P=P*(A if e==1 else mp.inverse(A))
    return P
z=mp.mpc(0.5,mp.sqrt(3)/2); P=sl2(z)
# relator at q=1 for the 8 sigmas
out={'relator_at_q1':{n:bool(ev(apply_sigma(s,REL),rho(R(1)))==sp.eye(4)) for n,s in SIGMAS.items()}}
# enumerate reduced words up to length 3
def reduced(L):
    res=[]
    for w in itertools.product([('m',1),('m',-1),('n',1),('n',-1)],repeat=L):
        if all(not(w[i][0]==w[i+1][0] and w[i][1]==-w[i+1][1]) for i in range(L-1)): res.append(list(w))
    return res
words=[w for L in (1,2,3) for w in reduced(L)]
def expsum(w): return sum(e for g,e in w)
rng=random.Random(3)
test=[]
for L in range(1,9):
    for w in itertools.product([('m',1),('m',-1),('n',1),('n',-1)],repeat=L):
        if sum(e for g,e in w)==0: test.append(list(w))
rng.shuffle(test); test=test[:200]
def tr(w): 
    M=evmp(w,P); return M[0,0]+M[1,1]
found=[]
for w1 in words:
    if abs(expsum(w1))!=1: continue
    for w2 in words:
        if abs(expsum(w2))!=1: continue
        sig=(tuple(w1),tuple(w2))
        if mp.norm(evmp(apply_sigma(sig,REL),P)-mp.eye(2))>1e-30: continue
        pres=all(abs(tr(apply_sigma(sig,w))-tr(w))<1e-30 for w in test)
        conj=all(abs(tr(apply_sigma(sig,w))-mp.conj(tr(w)))<1e-30 for w in test)
        found.append((w1,w2,pres,conj))
def s(w): return ''.join(g if e==1 else g.upper() for g,e in w)
out['n_endo_candidates']=len(found)
out['candidates']=[(s(a),s(b),p,c) for a,b,p,c in found]
# C2 on conjugated (orientation reversing) ones plus relator check in rho_q
QS=[R(2),R(3),R(1,5)]
C2x={}
for a,b,p,c in found:
    if not c: continue
    sig=(tuple(a),tuple(b))
    key=s(a)+','+s(b)
    C2x[key]={}
    for q in QS:
        r=rho(q)
        rel_ok=bool(ev(apply_sigma(sig,REL),r)==sp.eye(4))
        S=sigma_mats(sig,r)
        T={"rho_q":r,"rho_q*":dual(r),"rho_1/q":rho(1/q),"rho_1/q*":dual(rho(1/q))}
        row={tn:conj_decision(S,Tm)['conjugate'] for tn,Tm in T.items()}
        trl=ev(LONG,r).trace(); trli=ev(LONG,r).inv().trace(); ts=ev(apply_sigma(sig,LONG),r).trace()
        C2x[key][str(q)]=dict(rel_ok_in_rho_q=rel_ok,targets=row,tr_sigma_l_eq_l=bool(ts==trl),tr_sigma_l_eq_linv=bool(ts==trli))
out['C2_orientation_reversing_candidates']=C2x
json.dump(out,open('extra_results.json','w'),indent=1)
print(json.dumps(out['relator_at_q1'],indent=1))
print(out['n_endo_candidates'])
for c in out['candidates']: print(c)
for k,v in C2x.items(): print(k,json.dumps(v))
