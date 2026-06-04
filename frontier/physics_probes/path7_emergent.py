"""PATH 7 probe -- does the system have the STRUCTURE for emergent geometry/gravity?
The thesis ('reality as residue') matches the SPIRIT of emergent-gravity programs (Jacobson,
Verlinde): geometry as a statistic of counted microstates. For that to even be possible, the
microscopic system needs the right kind of entropy scaling. Two controlled tests:

 (A) Entanglement entropy scaling of the quasicrystal ground state (free fermions, half-filling).
     Emergent-geometry / holographic structure needs a clean S(L) law. Critical 1D -> S~(c/3)logL.
     CONTROL: compare to (i) a clean periodic chain (c=1, S~(1/3)logL) and (ii) random disorder
     (area-law, S->const). Where does the quasicrystal sit?

 (B) The substitution's complexity/entropy scaling (the 'counting' the thesis would use).
     PRIOR KILL in the repo: topological entropy of the trace map = n*log(mu) -- LINEAR in n.
     For emergent geometry you typically want area-law / sub-extensive counting, NOT linear.
     We re-confirm the scaling to see if the natural 'entropy' is the wrong kind (a closure)."""
import numpy as np

def fib_chain_H(VA, VB, depth=12):
    a,b="a","b"
    for _ in range(depth): a,b=a+b,a   # Fibonacci
    w=a; N=len(w)
    diag=np.array([VA if c=="a" else VB for c in w])
    H=np.diag(diag)+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)
    return H,N

def entanglement_entropy(H, N, cut):
    # free fermions at half filling: fill lowest N//2 eigenstates; S from correlation matrix on [0,cut)
    w,U=np.linalg.eigh(H)
    occ=U[:,:N//2]                       # lowest half filled
    C=occ@occ.conj().T                   # correlation matrix C_ij=<c_i^dag c_j>
    Csub=C[:cut,:cut]
    p=np.linalg.eigvalsh(Csub)
    p=np.clip(p,1e-12,1-1e-12)
    return -np.sum(p*np.log(p)+(1-p)*np.log(1-p))

print("PATH 7 -- (A) entanglement entropy scaling S(L), half-filling free fermions:\n")
# quasicrystal
Hq,Nq=fib_chain_H(0.5,-0.5,depth=13)
# periodic (all same site energy) = clean critical c=1
Hp=np.diag(np.zeros(Nq))+np.diag(np.ones(Nq-1),1)+np.diag(np.ones(Nq-1),-1)
# random disorder
rng=np.random.default_rng(0)
Hr=np.diag(rng.uniform(-0.5,0.5,Nq))+np.diag(np.ones(Nq-1),1)+np.diag(np.ones(Nq-1),-1)

cuts=[8,16,32,64,128,256]
print("   cut L  | quasicrystal | periodic(c=1) | random")
rows={"q":[],"p":[],"r":[]}
for L in cuts:
    sq=entanglement_entropy(Hq,Nq,L); sp=entanglement_entropy(Hp,Nq,L); sr=entanglement_entropy(Hr,Nq,L)
    rows["q"].append(sq); rows["p"].append(sp); rows["r"].append(sr)
    print(f"   {L:5d}  |   {sq:.4f}     |   {sp:.4f}      | {sr:.4f}")
# fit S = A*log(L)+B for each
import numpy as np
def slope(L,S):
    x=np.log(np.array(L)); y=np.array(S); A=np.polyfit(x,y,1)[0]; return A
print(f"\n   log-fit slope A (S ~ A*log L):  quasicrystal {slope(cuts,rows['q']):.3f}   "
      f"periodic {slope(cuts,rows['p']):.3f}   random {slope(cuts,rows['r']):.3f}")
print("   read: periodic ~1/3 (c=1 critical); random ~0 (area law); quasicrystal in between/log = critical-like.")
print("   -> If quasicrystal shows clean log growth it is CRITICAL (conformal-like) -- the *necessary*")
print("      structural precondition for any emergent-geometry reading. NOT sufficient: still 1D, still")
print("      no spacetime/gravity, no thesis content. It only says 'not obviously disqualified'.\n")

print("PATH 7 -- (B) substitution complexity scaling (the 'counting'):")
# factor complexity of the Fibonacci word p(k) = number of distinct length-k subwords = k+1 (Sturmian)
def factor_complexity(word, k):
    return len(set(word[i:i+k] for i in range(len(word)-k+1)))
a,b="a","b"
for _ in range(18): a,b=a+b,a
W=a
ks=[2,4,8,16,32,64]
pk=[factor_complexity(W,k) for k in ks]
print(f"   factor complexity p(k) for k={ks}: {pk}")
print(f"   p(k)-k = {[pk[i]-ks[i] for i in range(len(ks))]}  -> p(k)=k+1 (Sturmian): LINEAR complexity.")
print("   topological entropy = lim (1/k)log p(k) = 0 (sub-exponential); the SL(n) tower entropy")
print("   was found = n*log(mu), LINEAR in n (repo kill). Either way the natural counting is")
print("   LINEAR/zero-entropy -- NOT the sub-extensive/area scaling holographic emergence wants.")
print("   -> CONTROLLED NEGATIVE: the system's intrinsic 'entropy' is the wrong kind for the thesis's")
print("      emergent-geometry route. This WEAKENS Path 7 honestly (not a feeling -- a computed scaling).")
