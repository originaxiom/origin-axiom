"""
Step 3: spot-check the Deloup-Turaev / Jeffrey Theorem 1 reciprocity formula itself
(the corrected formula (3) in Deloup-Turaev "On Reciprocity", arXiv:math/0512050)
on the psi=0 sub-sector: W = Q (+) Q (Q = A2 root lattice, rank 2), r = kappa,
h = [[I, I-w^{-1}],[I-w, -I]] (self-adjoint w.r.t. the A2 weight inner product),
psi = 0.

LHS = vol(W*) * sum_{x in W/kap W} exp( i*pi/kap * <x, h(x)> )
RHS = |det h|^{-1/2} * exp(i*pi*sigma(g)/4) * kap^{l/2}
        * sum_{y in W*/h(W*)} exp( -i*pi*kap * <y, h^{-1}(y)> )

Both sides computed independently (brute force, orthonormal coordinates via Cholesky
of the A2 Gram matrix), compared for several (w, kappa).
"""
import numpy as np
import itertools

K = np.array([[2., 1.], [1., 2.]])          # A2 Cartan-type Gram matrix; ip(u,v)=u.K.v/3
Omega = np.kron(np.eye(2), K) / 3.0          # 4x4 Gram matrix on (mu_a,mu_b,alpha_a,alpha_b)
C = np.linalg.cholesky(Omega).T              # Omega = C^T C ... use C s.t. y=Cx has <x,x'>=y.y'
# verify
assert np.allclose(C.T @ C, Omega)

S1 = np.array([[-1, 0], [1, 1]])
S2 = np.array([[1, 1], [0, -1]])
WEYL = []
for word in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    M = np.eye(2, dtype=int)
    for g in word:
        M = (S1 if g == 0 else S2) @ M
    WEYL.append((M, (-1) ** len(word)))

I2 = np.eye(2, dtype=int)
I4 = np.eye(4)

# Q lattice basis in weight coords: rows of the Cartan matrix (simple roots)
q1 = np.array([2, -1])
q2 = np.array([-1, 2])

def h_matrix(w):
    winv = np.linalg.inv(w)
    top = np.hstack([I2, I2 - winv])
    bot = np.hstack([I2 - w, -I2])
    return np.vstack([top, bot]).astype(float)

def run_case(wi, pm, kap):
    Wm, sg = WEYL[wi]
    w = pm * Wm
    h_x = h_matrix(w)  # weight coords
    # self-adjointness check: Omega @ h_x == h_x.T @ Omega
    assert np.allclose(Omega @ h_x, h_x.T @ Omega, atol=1e-8)
    h_y = C @ h_x @ np.linalg.inv(C)
    assert np.allclose(h_y, h_y.T, atol=1e-6), "h_y not symmetric"

    # W = Q (+) Q basis, weight coords -> y coords
    BW_x = np.zeros((4, 4))
    BW_x[0:2, 0] = q1; BW_x[0:2, 1] = q2
    BW_x[2:4, 2] = q1; BW_x[2:4, 3] = q2
    BW_y = C @ BW_x
    volW = abs(np.linalg.det(BW_y))
    BWstar_y = np.linalg.inv(BW_y.T)   # dual basis
    volWstar = abs(np.linalg.det(BWstar_y))
    assert abs(volWstar - 1.0 / volW) < 1e-8

    det_h = np.linalg.det(h_y)
    eigs = np.linalg.eigvalsh(h_y)
    sigma = int(round(np.sum(eigs > 1e-9) - np.sum(eigs < -1e-9)))

    # LHS: x in W/kap W, i.e. x = BW_y @ n, n in {0,...,kap-1}^4
    LHS = 0j
    for n in itertools.product(range(kap), repeat=4):
        x = BW_y @ np.array(n, dtype=float)
        LHS += np.exp(1j * np.pi / kap * (x @ h_y @ x))
    LHS *= volWstar

    # RHS: y in W*/h(W*).  Express h_y in the W*-basis: M = BWstar_y^{-1} h_y BWstar_y
    M = np.linalg.inv(BWstar_y) @ h_y @ BWstar_y
    Mint = np.round(M).astype(int)
    assert np.allclose(M, Mint, atol=1e-6), f"h(W*) not subset of W* (M not integer): {M}"
    detM = int(round(np.linalg.det(Mint)))
    assert abs(detM) == round(abs(det_h)), (detM, det_h)

    # enumerate reps of Z^4 / Mint(Z^4) via brute force over a bounding box (|detM| small)
    D = abs(detM)
    reps_n = []
    seen = set()
    # brute force: search box [-D,D]^4, reduce via HNF-free approach:
    # use the fact that coset reps correspond to n in a fundamental domain of M.
    # simplest robust method: Smith normal form.
    box = range(-D, D + 1)
    coset_reps = {}
    for n in itertools.product(box, repeat=4):
        nvec = np.array(n)
        # coset label: solve for m = M^{-1} n mod 1 pattern -> use frac part of M^{-1}@n
        frac = np.linalg.inv(Mint.astype(float)) @ nvec
        label = tuple(np.round((frac - np.floor(frac)) * 100000).astype(int))
        if label not in coset_reps:
            coset_reps[label] = nvec
        if len(coset_reps) == D:
            break
    assert len(coset_reps) == D, f"only found {len(coset_reps)}/{D} coset reps"

    h_y_inv = np.linalg.inv(h_y)
    RHS = 0j
    for nvec in coset_reps.values():
        yv = BWstar_y @ nvec.astype(float)
        RHS += np.exp(-1j * np.pi * kap * (yv @ h_y_inv @ yv))
    RHS *= (abs(det_h) ** -0.5) * np.exp(1j * np.pi * sigma / 4) * (kap ** 2)

    return LHS, RHS, det_h, sigma


print(f"{'wi':>3} {'pm':>3} {'kap':>4} {'det(h)':>7} {'sigma':>6}   LHS                RHS                |LHS-RHS|")
for wi in (0, 1, 3):     # identity, one reflection, one rotation (representative cases)
    for pm in (1, -1):
        for kap in (5, 6, 7):
            LHS, RHS, det_h, sigma = run_case(wi, pm, kap)
            diff = abs(LHS - RHS)
            print(f"{wi:>3} {pm:>+3} {kap:>4} {det_h:>7.0f} {sigma:>6}  "
                  f"{LHS.real:+.4f}{LHS.imag:+.4f}j   {RHS.real:+.4f}{RHS.imag:+.4f}j   {diff:.2e}")
