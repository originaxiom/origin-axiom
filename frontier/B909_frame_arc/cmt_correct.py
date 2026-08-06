import io, contextlib, sympy as sp, numpy as np
from fractions import Fraction as Fr
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open('os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'B854_centralizer_exact', 'e6_centralizer.py')').read(),'b854','exec'), globals())
import sympy as sp
s = sp.Symbol('s')
# THE CORRECTED WALL POLYNOMIAL: kappa (the section-LV truth; the shipped cmt.py
# carried the RETRACTED section-LIV septic -- caught at banking by root mismatch)
KAPPA = sp.Poly(2771822592000*s**3 + 3033676800*s**2 - 56402640*s - 6859, s)
Tn = {}
for i in range(78):
    for j in range(i+1, 78):
        v = bracket_basis(i, j)
        nz = [(k, c) for k, c in enumerate(v) if c != 0]
        if nz: Tn[(i, j)] = nz
print("bracket table ready", flush=True)
from sympy import nextprime
pairs = []
p = 40009
while len(pairs) < 5:
    p = nextprime(p)
    if 2771822592000 % p == 0: continue
    r = sp.Poly(KAPPA.as_expr(), s, modulus=p).ground_roots()
    for x in sorted(int(x) % p for x in r):
        pairs.append((p, x))
print("kappa (root,prime) pairs:", pairs, flush=True)
for q, sstar in pairs:
    def rq(x):
        xr = sp.Rational(x); return (xr.p % q)*pow(xr.q % q, -1, q) % q
    Gq = {n: np.array([[rq(sp.Matrix(ADS[n])[i, j]) for j in range(78)]
                       for i in range(78)], dtype=np.int64) for n in ns}
    def rn(A0):
        A = [[int(x) % q for x in row] for row in
             (A0.tolist() if hasattr(A0, 'tolist') else A0)]
        n_, m_ = len(A), len(A[0]); piv = []; rr = 0
        for c in range(m_):
            pr = next((x for x in range(rr, n_) if A[x][c] % q), None)
            if pr is None: continue
            A[rr], A[pr] = A[pr], A[rr]
            iv = pow(A[rr][c], -1, q); A[rr] = [(e*iv) % q for e in A[rr]]
            for x in range(n_):
                if x != rr and A[x][c]:
                    f2 = A[x][c]; A[x] = [(A[x][j]-f2*A[rr][j]) % q for j in range(m_)]
            piv.append(c); rr += 1
        fr = [c for c in range(m_) if c not in piv]; K = []
        for f3 in fr:
            v = [0]*m_; v[f3] = 1
            for i, c in enumerate(piv): v[c] = int((-A[i][f3]) % q)
            K.append(v)
        return rr, (np.array(K, dtype=np.int64) % q
                    if K else np.zeros((0, m_), dtype=np.int64))
    def bv(u, v2):
        w = np.zeros(78, dtype=np.int64)
        for (i, j), nz in Tn.items():
            cij = (int(u[i])*int(v2[j])-int(u[j])*int(v2[i])) % q
            if cij:
                for k, c in nz:
                    f3 = Fr(c)
                    w[k] = (w[k]+cij*(f3.numerator % q)*pow(f3.denominator % q, -1, q)) % q
        return w
    _, CORE = rn(np.vstack([Gq[8], Gq[16]]))
    M = (Gq[14] + sstar*Gq[22]) % q
    _, Z = rn(M)
    dz = Z.shape[0]
    Dk = [bv(Z[a], Z[b]) for a in range(dz) for b in range(a+1, dz)]
    dd, _ = rn(np.vstack(Dk)) if Dk else (0, None)
    _, ZC = rn(np.vstack([M, np.vstack([Gq[8], Gq[16]])]))
    print(f"q={q}, s*={sstar}: dim z = {dz}; derived >= {dd}; "
          f"z∩core = {ZC.shape[0]}; center-by-count = {dz - dd}", flush=True)
print("CMT-DONE", flush=True)
