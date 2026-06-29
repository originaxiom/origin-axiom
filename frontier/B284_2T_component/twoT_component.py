"""B284 -- verifying chat-1's claim 3: the figure-eight's 2T-factoring representation. Is it (a) object-specific and
(b) a DISTINGUISHED component whose local structure the generic smooth point lacks?  Run with python (numpy).

Result: (a) YES object-specific -- the finite-image 2T rep exists EXACTLY (tetrahedral angle cos=-1/3, image order
24); it exists only because pi_1(4_1) surjects onto 2T (B282: 5_2/6_1/6_2/7_4 do not). (b) NO -- its LOCAL
deformation is GENERIC: dim_C H^1(Ad) = 1, identical to the geometric rep. It is a special finite-image POINT on the
generic canonical component -- in fact the arithmetic reduction mod 3 of the geometric point (meridian trace 2 -> -1
mod 3; geometric Riley root u = omega in Q(sqrt-3)). So chat-1's KERNEL is right (object-specific point exists) but
the STRONGER form fails (no anomalous component). Reinforces B282: object-specificity is GLOBAL/arithmetic existence,
not LOCAL geometry.

NB: H^1 must use the COMPLEX sl2 adjoint (basis e,h,f) -- a real-su(2) projection is valid only for the SU(2) 2T rep
and wrongly gives 0 for the SL(2,C) geometric rep (caught during this verification).
"""
import numpy as np

I2 = np.eye(2, dtype=complex)
_sx = np.array([[0,1],[1,0]],dtype=complex); _sy = np.array([[0,-1j],[1j,0]],dtype=complex); _sz = np.array([[1,0],[0,-1]],dtype=complex)
_E = np.array([[0,1],[0,0]],dtype=complex); _H = np.array([[1,0],[0,-1]],dtype=complex); _F = np.array([[0,0],[1,0]],dtype=complex)
W_SEQ = ['b','A','B','a']                                   # W = b a^-1 b^-1 a
def _inv(seq): return [s.lower() if s.isupper() else s.upper() for s in seq[::-1]]
R_SEQ = ['a'] + W_SEQ + ['B'] + _inv(W_SEQ)                # relator a W b^-1 W^-1

def _Ad(g):                                                # complex sl2 adjoint, basis (e,h,f)
    gi = np.linalg.inv(g); cols = []
    for X in (_E, _H, _F):
        Y = g @ X @ gi; cols.append([Y[0,1], Y[0,0], Y[1,0]])
    return np.array(cols).T
def _word(g, seq):
    M = I2.copy()
    for s in seq: M = M @ (np.linalg.inv(g[s.lower()]) if s.isupper() else g[s.lower()])
    return M
def relator_residual(g): return float(np.linalg.norm(_word(g, R_SEQ) - I2))
def dim_H1(g):                                             # dim_C H^1(pi_1(4_1); Ad rho) via Fox calculus
    d0 = np.vstack([_Ad(g['a'])-np.eye(3), _Ad(g['b'])-np.eye(3)])
    def fox(x):
        D = np.zeros((3,3), complex); pref = np.eye(3, dtype=complex)
        for s in R_SEQ:
            Adg = _Ad(g[s.lower()])
            if s.lower()==x: D = D + (pref if s.islower() else -pref@np.linalg.inv(Adg))
            pref = pref @ (np.linalg.inv(Adg) if s.isupper() else Adg)
        return D
    d1 = np.hstack([fox('a'), fox('b')])
    rk = lambda M: int(np.linalg.matrix_rank(M, tol=1e-7))
    return (6 - rk(d1)) - rk(d0)

def geometric_rep():                                       # parabolic, exact Riley root u = omega in Q(sqrt-3)
    w = np.exp(2j*np.pi/3)
    return {'a': np.array([[1,1],[0,1]],dtype=complex), 'b': np.array([[1,0],[-w,1]],dtype=complex)}
def twoT_rep():                                            # order-3 meridians, tetrahedral angle cos = -1/3
    def su2(axis, ang):
        n = np.array(axis,float); n /= np.linalg.norm(n)
        return np.cos(ang/2)*I2 - 1j*np.sin(ang/2)*(n[0]*_sx+n[1]*_sy+n[2]*_sz)
    al = np.arccos(-1/3)
    return {'a': su2([0,0,1], 4*np.pi/3), 'b': su2([np.sin(al),0,np.cos(al)], 4*np.pi/3)}
def image_order(g, cap=400):
    elts=[I2]; frontier=[I2]; gg=[g['a'],g['b'],np.linalg.inv(g['a']),np.linalg.inv(g['b'])]
    for _ in range(12):
        new=[]
        for M in frontier:
            for h in gg:
                Mn = M@h
                if not any(np.linalg.norm(Mn-E)<1e-6 for E in elts): elts.append(Mn); new.append(Mn)
        frontier = new
        if not new or len(elts) > cap: break
    return len(elts)

if __name__ == "__main__":
    geo, tt = geometric_rep(), twoT_rep()
    print(f"geometric rep : residual={relator_residual(geo):.1e}  tr(b)={np.real(np.trace(geo['b'])):+.2f} (parabolic)"
          f"  dim_C H^1={dim_H1(geo)}  (B264 expects 1)")
    print(f"finite 2T rep : residual={relator_residual(tt):.1e}  tr(b)={np.real(np.trace(tt['b'])):+.2f}"
          f"  image order={image_order(tt)}  dim_C H^1={dim_H1(tt)}")
    assert relator_residual(tt) < 1e-10 and image_order(tt) == 24
    assert dim_H1(geo) == 1 and dim_H1(tt) == 1
    print("\nVERDICT: 2T rep is object-specific (image 24; needs pi_1->2T, B282) BUT local H^1=1 = generic.")
    print("=> a special finite-image POINT on the generic component (arithmetic reduction mod 3 of the geometric")
    print("   point: trace 2 -> -1 mod 3), NOT an anomalous component. chat-1 claim-3 kernel right, stronger form")
    print("   fails. Reinforces B282.")
