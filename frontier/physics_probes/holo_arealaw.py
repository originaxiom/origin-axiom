"""Does the metallic/quasicrystal system carry HOLOGRAPHIC (area-law) entanglement,
or BULK (volume/extensive) entanglement? This is the decidable signature of 'is this
2D boundary information of a holographic universe'.

Standard sharp test (Ryu-Takayanagi / Bekenstein-Hawking content):
  - In 1D, a "region" is an interval; its "boundary" is its endpoints (0, 1, or 2 of them).
  - AREA LAW (holographic / gapped bulk-boundary): S(region) -> const, set by # boundary points,
    INDEPENDENT of region length L.
  - VOLUME / extensive: S grows with L (linearly).
  - CRITICAL (1D CFT, c): S ~ (c/3) log L for one boundary point, (c/3)*2*... for an interval in
    the bulk; LOG growth -- between area and volume, the hallmark of a *critical* 1D chain.

We compute S for:
  (A) an interval [0,L) with ONE boundary point (the other end at the chain edge) -> tests log vs const vs linear
  (B) a bulk interval [a, a+L) with TWO boundary points -> RT: S should be ~2x the one-cut value if area-law/CFT
  (C) MUTUAL INFORMATION between two separated bulk intervals -> holographic systems have a sharp
      'entanglement plateau' / specific decay; tests structure beyond a single number.
Free fermions at half filling on the Fibonacci (m=1) chain; correlation-matrix method (exact).
Controls: clean periodic chain (known c=1 critical) and strong random disorder (known area-law/localized).
"""
import numpy as np

def chain_H(kind, N, seed=0):
    if kind == "fibonacci":
        a,b="a","b"
        while len(a) < N: a,b=a+b,a
        w=a[:N]; diag=np.array([0.5 if c=="a" else -0.5 for c in w])
    elif kind == "periodic":
        diag=np.zeros(N)
    elif kind == "random":
        rng=np.random.default_rng(seed); diag=rng.uniform(-3,3,N)   # strong disorder -> localized/area-law
    H=np.diag(diag)+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)
    return H

def corr_matrix(H, fill=0.5):
    w,U=np.linalg.eigh(H); nocc=int(round(fill*H.shape[0]))
    occ=U[:,:nocc]; return occ@occ.conj().T

def S_region(C, idx):
    Csub=C[np.ix_(idx,idx)]; p=np.linalg.eigvalsh(Csub); p=np.clip(p,1e-13,1-1e-13)
    return float(-np.sum(p*np.log(p)+(1-p)*np.log(1-p)))

N=1597  # Fibonacci length
res={}
for kind in ("fibonacci","periodic","random"):
    C=corr_matrix(chain_H(kind,N))
    # (A) one boundary point: interval [0,L)
    Ls=[10,20,40,80,160,320,640]
    SA=[S_region(C, list(range(L))) for L in Ls]
    # (B) bulk interval [N/2 - L/2, N/2 + L/2): two boundary points
    SB=[S_region(C, list(range(N//2-L//2, N//2+L//2))) for L in Ls]
    res[kind]=(Ls,SA,SB)

def fit_log(Ls,S):  # S = A*log L + B
    A,B=np.polyfit(np.log(Ls),S,1); return A,B
def fit_lin(Ls,S):  # S = a*L + b ; report slope a
    a,b=np.polyfit(Ls,S,1); return a

print("=== ONE boundary point: S of interval [0,L) vs L ===")
print(f"{'L':>5} | {'Fibonacci':>10} {'periodic':>10} {'random':>10}")
Ls=res['fibonacci'][0]
for i,L in enumerate(Ls):
    print(f"{L:>5} | {res['fibonacci'][1][i]:>10.4f} {res['periodic'][1][i]:>10.4f} {res['random'][1][i]:>10.4f}")
print("\nfits (one boundary point):")
for kind in ("fibonacci","periodic","random"):
    Ls,SA,_=res[kind]
    aL,_=fit_log(Ls,SA); slope=fit_lin(Ls,SA)
    print(f"  {kind:>10}: log-slope (c/3 if CFT) = {aL:+.4f}  | linear-slope = {slope:+.5f}  | last-3 spread = {np.ptp(SA[-3:]):.3f}")

print("\n=== TWO boundary points (bulk interval): RT predicts ~2x the one-cut log-coeff ===")
for kind in ("fibonacci","periodic","random"):
    Ls,_,SB=res[kind]
    aL,_=fit_log(Ls,SB); slope=fit_lin(Ls,SB)
    print(f"  {kind:>10}: log-slope = {aL:+.4f}  | linear-slope = {slope:+.5f}  | S(L) values: {[round(s,2) for s in SB]}")

print("\n=== VERDICT LOGIC ===")
print("  AREA LAW (holographic boundary): S -> const, flat in L (log-slope ~ 0, linear-slope ~ 0).")
print("  CRITICAL CFT:                    S ~ (c/3) log L (log-slope > 0, linear-slope ~ 0).")
print("  VOLUME/extensive:                S ~ linear in L (linear-slope > 0).")
