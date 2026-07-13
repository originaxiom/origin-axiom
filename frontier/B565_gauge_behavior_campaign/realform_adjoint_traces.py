import snappy, numpy as np, itertools, math
np.set_printoptions(suppress=True)
M = snappy.Manifold('4_1'); G = M.fundamental_group()
def mat(w):
    S = G.SL2C(w)
    return np.array([[complex(S[0,0]), complex(S[0,1])],[complex(S[1,0]), complex(S[1,1])]])

def sym_power(A, d):
    """Matrix of Sym^d(A) on basis x^{d-i} y^i, i=0..d."""
    n = d+1
    S = np.zeros((n,n), dtype=complex)
    a,b,c,dd = A[0,0],A[0,1],A[1,0],A[1,1]
    import sympy as sp
    x, y = sp.symbols('x y')
    ax, ay = sp.nsimplify(0), sp.nsimplify(0)
    # substitute x -> a x + c y, y -> b x + d y  (column-vector convention consistent for traces)
    for i in range(n):
        poly = sp.expand((sp.Float(A[0,0].real,30)+sp.I*sp.Float(A[0,0].imag,30) ) ) # too slow; do numerically
    return None

# numeric Sym^d via multilinear: trace only needed -> tr Sym^d(A) = h_d(eigs)
# Instead do a FULL matrix Jordan check for the meridian using exact sympy unipotent conjugacy:
import sympy as sp
mu = mat(G.meridian())
print("meridian =\n", np.round(mu,9), " tr =", np.trace(mu))
# rho(mu) = -U with U unipotent (tr = -2). Ad depends only on image in PSL2; Sym^{2m}(-U)=Sym^{2m}(U).
# Jordan type of Sym^{2m}(unipotent J2): verify single block of size 2m+1 exactly in sympy.
J = sp.Matrix([[1,1],[0,1]])
def sym_mat(Asp, d):
    x, y = sp.symbols('x y')
    xi = Asp[0,0]*x + Asp[1,0]*y   # action on coordinates s.t. Sym^1 = A
    yi = Asp[0,1]*x + Asp[1,1]*y
    basis = [x**(d-i)*y**i for i in range(d+1)]
    S = sp.zeros(d+1, d+1)
    for j,bj in enumerate(basis):
        img = sp.expand(bj.subs({x: xi, y: yi}, simultaneous=True))
        p = sp.Poly(img, x, y)
        for i in range(d+1):
            S[i,j] = p.coeff_monomial(x**(d-i)*y**i)
    return S
# gate the convention: Sym^1(J) == J
assert sym_mat(J,1) == J
blocks = []
for m in [1,4,5,7,8,11]:
    S = sym_mat(J, 2*m)
    N = S - sp.eye(2*m+1)
    k = 0; P = sp.eye(2*m+1)
    while True:
        P = P*N; k += 1
        if P == sp.zeros(2*m+1, 2*m+1): break
    blocks.append((2*m, k))
    assert k == 2*m+1, (m,k)
print("Sym^{2m}(unipotent): nilpotency degrees (block sizes):", blocks)
print("=> Ad_e6(rho(mu)) unipotent, Jordan blocks", [b[1] for b in blocks],
      "-> (Ad-1)^22 != 0, (Ad-1)^23 = 0 : REGULAR unipotent in E6; blocks {3,15,23} + {9,17} + {11}")
print("f4 blocks:", [2*m+1 for m in [1,5,7,11]], " (regular unipotent in F4, (Ad-1)^22!=0)")

# independent matrix-level check of tr Ad_e6(a): numeric Sym^d of the actual SnapPy matrix
def sym_mat_num(A, d):
    x, y = sp.symbols('x y')
    Asp = sp.Matrix(2,2, lambda i,j: sp.Float(A[i,j].real, 30) + sp.I*sp.Float(A[i,j].imag, 30))
    return sym_mat(Asp, d)
a = mat('a')
tot = 0
for m in [1,4,5,7,8,11]:
    S = sym_mat_num(a, 2*m)
    tot += complex(sp.trace(S))
print("\nmatrix-level tr Ad_e6(a) =", tot)
print("exact prediction         = 37437270 + 38799960*sqrt(3) i =", 37437270 + 38799960*math.sqrt(3)*1j)
