import numpy as np, sympy as sp, itertools
exec(open('v.py').read().split("for ci, (g_S, info) in enumerate(cands):")[0].replace("print(","(lambda *a,**k:None)("))
np.set_printoptions(precision=4, suppress=True, linewidth=150)

# ---- (0) exact ----
x = sp.symbols('x')
Mx = sp.Matrix([[2,1],[1,1]])
print("(0) det", Mx.det(), "trace", Mx.trace())
fp = sp.solve(sp.Eq(x, (2*x+1)/(x+1)), x); print("fixed points", fp)
a, b = sorted(fp, key=lambda t: float(t))
cen = sp.simplify((a+b)/2); rad = sp.simplify((b-a)/2)
print("centre", cen, "radius", rad, "radius^2", sp.simplify(rad**2))
I = sp.I; om = sp.Rational(-1,2) + sp.sqrt(3)/2*I
def onaxis(z): return sp.simplify(sp.expand(sp.Abs(z-cen)**2 - rad**2))
print("|i-c|^2 - r^2 =", onaxis(I))
print("|omega-c|^2 - r^2 =", onaxis(om), " (|omega-c|^2 =", sp.simplify(sp.Abs(om-cen)**2), ")")
print("also e^{i pi/3}:", onaxis(sp.Rational(1,2)+sp.sqrt(3)/2*I))
print("M(i) =", sp.simplify((2*I+1)/(I+1)), " on axis:", onaxis(sp.simplify((2*I+1)/(I+1))))
# i is on the axis; axis of M is geodesic; M fixes the geodesic setwise; i is a point on it
# also: S_mod = S fixes i; is S the order-4 elt: [[0,-1],[1,0]]
print("is the circle through i,  Re(i)=0 in (-1/phi, phi)?", float(a) < 0 < float(b))

# ---- extra: all 6 elements w/ eigenvalue pattern: which axis is the single? ----
print("\nEXTRA: the other eigen-pattern elements (fix e1 or e2 rather than e3)")
for g, info in cands_all:
    fixed_axis = [i for i in range(3) if abs(g[i,i]) > .5]
    swapped = [i for i in range(3) if i not in fixed_axis]
    # diag subspace action Dirac: M->g^dag M g ; find eigenspaces among 3-dim diag
    D = np.zeros((3,3)); 
    # restricted to diagonal
    def act(M): return g.conj().T @ M @ g
    A = np.array([[act(np.diag(np.eye(3)[j]).astype(complex))[i,i] for j in range(3)] for i in range(3)])
    ev, V = np.linalg.eig(A)
    for k in range(3):
        pass
    print(" fixed axis", fixed_axis, "swapped", swapped, " diag action matrix:\n", np.round(A.real,3).tolist())

# ---- positive control: the test can fail ----
print("\nCONTROL: generic random diagonal (inner-fixed only, no S-constraint):", classify(sing(np.diag(rng.normal(size=3)+1j*rng.normal(size=3)))))
# full 9-dim space, S eigenspaces without inner constraint
for name,(actf,basis) in tensors.items():
    g_S = cands[0][0]
    d=len(basis); Bm=np.array([b.flatten() for b in basis]).T
    R = rep_matrix(actf(g_S), basis)
    cnt={}
    for k in range(48):
        lam=np.exp(2j*np.pi*k/48)
        Ns=nullspace(R-lam*np.eye(d),tol=1e-8)
        if Ns.shape[1]==0: continue
        cl={}
        for t in range(200):
            coef=rng.normal(size=Ns.shape[1])+1j*rng.normal(size=Ns.shape[1])
            M=(Bm@(Ns@coef)).reshape(3,3)
            c=classify(sing(M)); cl[c]=cl.get(c,0)+1
        cnt[k]=(Ns.shape[1],cl)
    print(f"CONTROL full space (no inner constraint) {name}: ", cnt)

# ---- (4) mixing ----
print("\n(4) mixing between two sectors")
g_S, info = cands[0]
def sector_matrices():
    # pick two random elements from (possibly different) tensors / eigenspaces
    out=[]
    for name,(actf,basis) in tensors.items():
        d=len(basis); Bm=np.array([b.flatten() for b in basis]).T
        R=lambda g: rep_matrix(actf(g),basis)
        A=np.vstack([R(ia)-np.eye(d),R(ib)-np.eye(d)]); N=nullspace(A)
        RS=R(g_S); Ares=np.linalg.lstsq(N,RS@N,rcond=None)[0]
        for k in range(48):
            lam=np.exp(2j*np.pi*k/48)
            Ns=nullspace(Ares-lam*np.eye(3),tol=1e-8)
            if Ns.shape[1]==0: continue
            coef=rng.normal(size=Ns.shape[1])+1j*rng.normal(size=Ns.shape[1])
            out.append((name,k,(Bm@(N@(Ns@coef))).reshape(3,3)))
    return out
secs = sector_matrices()
print(" sectors:", [(n.strip(),k) for n,k,_ in secs])
def axis_sorted_U(M):
    # left singular vectors read off the coordinate axes (M diagonal): permutation sorting |M_ii| ascending
    s=np.abs(np.diag(M)); idx=np.argsort(s)
    P=np.zeros((3,3)); 
    for r,i in enumerate(idx): P[i,r]=1
    return P
allperm=True
for (n1,k1,M1),(n2,k2,M2) in itertools.combinations(secs,2):
    # M1 = U1 diag V1^dag ; mixing U = U1^dag U2 with axis-adapted bases
    U = axis_sorted_U(M1).T @ axis_sorted_U(M2)
    isperm = np.allclose(np.sort(np.abs(U).flatten())[-3:],1) and np.allclose(U@U.T,np.eye(3)) and np.allclose(np.abs(U),np.round(np.abs(U)))
    allperm &= isperm
    # numerical SVD-based mixing (arbitrary basis in degenerate pair)
    U1,s1,_=np.linalg.svd(M1); U2,s2,_=np.linalg.svd(M2)
    Un=U1.conj().T@U2
    print(f" {n1.strip()}[{k1}] vs {n2.strip()}[{k2}]: axis-adapted mixing is a permutation: {isperm}; numpy-SVD |U|^2 =\n{np.round(np.abs(Un)**2,3)}")
print(" all axis-adapted mixings permutations:", allperm)
# the invariant statement: block structure with e3 -> e3
print(" e3 row/column of |U_svd|^2 (numpy SVD) - single-to-single and pair-to-pair block structure is basis independent only up to sorting; check M M^dag eigenvectors")
for (n1,k1,M1),(n2,k2,M2) in itertools.combinations(secs,2):
    # does the single vector of sector1 (e3) coincide with e3 of sector 2? always, both axis e3
    pass
