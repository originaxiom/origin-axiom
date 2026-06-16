"""ROUTE R1 -- figure-eight m=1, SL(3), {1,i,-i} (o=4): EXACT family + PROVE [A,B]=+-mu^k over Q(i).

Locus: t11=i t22, t00=(1+i)t22, with off-diagonal products p=t01 t10, q=t02 t20, r=t12 t21 obeying
  (C0)  p - i q = 0
  (C1)  (1-i) p - r - i t22^2 = 0
  (C2)  (1-i) q + i r - t22^2 = 0
Solve: from C0, p = i q. C1: (1-i) i q - r - i t22^2 = (i+1) q - r - i t22^2 = 0 => r = (1+i)q - i t22^2.
C2: (1-i) q + i((1+i)q - i t22^2) - t22^2 = (1-i)q + (i-1)q + t22^2 - t22^2 = 0. IDENTICALLY 0.
So C2 is dependent; free choice is q and t22 (and one off-diag entry per pair as gauge/scale).

Family parametrization (gauge: centralizer of A = diagonal torus; use it to set t01=t02=t12=1, then
t10=p=iq, t20=q, t21=r=(1+i)q - i t22^2). Two essential params (q, t22) after gauge -- matches an
A-polynomial CURVE (1-dim moduli after the 2-dim diagonal-gauge quotient of the 3-dim diagonal torus...).

We PROVE: [A,B] = c * mu^k as polynomial matrix identity (cleared of inverses), reading off k.
B = A^-2 t A t^-1, mu = A^-1 t. Clear t^-1 = adj(t)/det(t).
"""
import sympy as sp

I = sp.I
n = 3

def family():
    q, t22 = sp.symbols("q t22")
    t11 = I * t22
    t00 = (1 + I) * t22
    p = I * q
    r = (1 + I) * q - I * t22**2
    # gauge: diagonal conjugation g=diag(g0,g1,g2) sends t_ij -> (g_i/g_j) t_ij; products t_ij t_ji invariant.
    # Set t01=t02=t12=1 (3 conditions, but torus is 2-dim projectively); to be safe keep symbolic upper, fix lower by products.
    t01, t02, t12 = sp.Integer(1), sp.Integer(1), sp.Integer(1)
    t10 = p / t01
    t20 = q / t02
    t21 = r / t12
    A = sp.diag(1, I, -I)
    t = sp.Matrix([[t00, t01, t02],
                   [t10, t11, t12],
                   [t20, t21, t22]])
    return A, t, (q, t22)

def verify_on_variety():
    A, t, params = family()
    Ai = sp.diag(1, -I, I); A2 = sp.diag(1, -1, -1)
    S = sp.expand(t * A2 * t * A - Ai * t * A * t)
    ok = all(sp.simplify(S[r, c]) == 0 for r in range(n) for c in range(n))
    return ok, A, t, params

def prove_identity():
    ok, A, t, params = verify_on_variety()
    q, t22 = params
    Ai = sp.diag(1, -I, I); A2 = sp.diag(1, -1, -1)
    det = sp.cancel(t.det())
    u = t.adjugate()               # t^-1 = u/det
    mu = sp.expand(Ai * t)         # meridian A^-1 t
    # B = A^-2 t A t^-1, [A,B] = A B A^-1 B^-1
    # Clear inverses: B = A2 t A u / det ; B^-1 = (t A2 t^-1 A2) ... compute directly with u/det
    B = sp.expand(A2 * t * A * u) / det                  # B*det? keep symbolic; we use rational then cancel
    # longitude [A,B] = A B A^-1 B^-1 ; B^-1 = A t^-1 ... recompute B^-1 honestly:
    # B = A^-2 t A t^-1 => B^-1 = t A^-1 t^-1 A^2
    Bi = sp.expand(t * Ai * u) / det * A2                 # = t A^-1 t^-1 A^2
    comm = sp.expand(A * B * Ai * Bi)
    comm = sp.Matrix(n, n, lambda r, c: sp.cancel(comm[r, c]))
    # find k by testing mu^k * scalar
    results = {}
    for k in range(1, 9):
        muk = mu
        for _ in range(k - 1):
            muk = sp.expand(muk * mu)
        # comm should equal c * muk; test the ratio on a nonzero entry then verify full
        for sgn in (1, -1):
            # candidate c = (det t)^? ; on SL(3) det t may not be 1, allow c = scalar(params)
            # Solve c from comm = c*sgn*muk at one entry, then check all
            cand = None
            for r in range(n):
                for c2 in range(n):
                    if sp.simplify(muk[r, c2]) != 0:
                        cand = sp.cancel(comm[r, c2] / (sgn * muk[r, c2]))
                        break
                if cand is not None:
                    break
            if cand is None:
                continue
            diff = sp.Matrix(n, n, lambda r, c2: sp.cancel(comm[r, c2] - sgn * cand * muk[r, c2]))
            if all(sp.simplify(diff[r, c2]) == 0 for r in range(n) for c2 in range(n)):
                results[(sgn, k)] = sp.simplify(cand)
    return ok, det, results

def main():
    ok, det, results = prove_identity()
    print(f"family on variety (S=0 exactly over Q(i)): {ok}")
    print(f"det t = {sp.factor(det)}")
    print("Matrix identities [A,B] = sgn * c * mu^k that hold IDENTICALLY over Q(i):")
    for (sgn, k), c in sorted(results.items(), key=lambda kv: kv[0][1]):
        print(f"   [A,B] = ({'+' if sgn>0 else '-'}1) * ({c}) * mu^{k}")
    if not results:
        print("   NONE found for k<=8 -- investigate.")

if __name__ == "__main__":
    main()
