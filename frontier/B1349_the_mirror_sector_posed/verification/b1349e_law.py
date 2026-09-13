"""The gcd(m,15) law, verified EXHAUSTIVELY and EXACTLY, and emitted for banking.

The verification is COMPLETE, not inductive: ord(R) = ord(L) = 15, so R^m L^m depends on m
only through m mod 15, and m = 1..15 is the entire family.
"""
import importlib.util, json, math, os
import sympy as sp
from sympy import Rational as Q

HERE = os.path.dirname(os.path.abspath(__file__))
sp2 = importlib.util.spec_from_file_location("exact60", os.path.join(HERE, "b1349c_exact_instrument.py"))
X = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(X)
S, T, W, red, conj, mmul = X.S, X.T, X.W, X.red, X.conj, X.mmul
N = 6; ix = {w: i for i, w in enumerate(W)}; I6 = sp.eye(N)
def cmat(A): return sp.Matrix(A.rows, A.cols, lambda i, j: conj(A[i, j]))
def re_(e):  return red(sp.expand((e + conj(e)) * Q(1, 2)))
C = sp.zeros(N, N)
for i, w in enumerate(W): C[ix[(w[1], w[0])], i] = 1
Cm = sp.Matrix(N, N, lambda i, j: sp.Integer(C[i, j]))
R = T; L = mmul(mmul(cmat(S), cmat(T)), S)
def mpow(A, k):
    P = I6
    for _ in range(k): P = mmul(P, A)
    return P
assert mpow(R, 15) == I6 and mpow(L, 15) == I6, "period-15 control"
Bev = sp.zeros(N, 4)
Bev[ix[(0,0)],0] = 1; Bev[ix[(1,1)],1] = 1
Bev[ix[(0,1)],2] = Bev[ix[(1,0)],2] = 1
Bev[ix[(0,2)],3] = Bev[ix[(2,0)],3] = 1
Bod = sp.zeros(N, 2)
Bod[ix[(0,1)],0], Bod[ix[(1,0)],0] = 1, -1
Bod[ix[(0,2)],1], Bod[ix[(2,0)],1] = 1, -1

def Qform(m, B):
    Wd = mmul(Cm, mmul(mpow(R, m), mpow(L, m)))
    k = B.cols
    A = sp.Matrix(k, k, lambda i, j:
                  red(sp.expand(sum(B[a, i] * Wd[a, b] * B[b, j] for a in range(N) for b in range(N)))))
    return sp.Matrix(k, k, lambda i, j: re_((A[i, j] + A[j, i]) * Q(1, 2))), B.T * B

ZN = sp.exp(2 * sp.pi * sp.I / 60)
def fnum(e): return float(sp.re(sp.N(sp.sympify(e).subs(X.z, ZN), 30)))
def exact_scalar(Qm, G):
    k = Qm.rows
    lam = sp.Rational(1, k) * sum(Qm[i, i] * Q(1, G[i, i]) for i in range(k))
    lam = red(sp.expand(lam))
    return lam, sp.simplify(sp.expand(Qm - sp.Matrix(k, k, lambda i, j: red(sp.expand(lam * G[i, j]))))) == sp.zeros(k, k)

print("=" * 78)
print("THE LAW, exhaustively over the full period m = 1..15")
print("=" * 78)
res = {"even": {}, "odd": {}}
viol = []
for m in range(1, 16):
    Qm, G = Qform(m, Bev)
    lam, scalar = exact_scalar(Qm, G)
    coprime = (math.gcd(m, 15) == 1)
    # THE LAW: ear-independent  <=>  gcd(m,15) > 1
    if scalar == coprime: viol.append(m)
    tl = red(sp.expand(sum(Qm[i, i] * Q(1, G[i, i]) for i in range(4))))
    res["even"][m] = dict(gcd=math.gcd(m, 15), ear_independent=bool(scalar),
                          lam=fnum(lam), trace_is_zero=bool(sp.simplify(tl) == 0))
    print(f"  m={m:2d} gcd={math.gcd(m,15):2d}  ear-independent={str(bool(scalar)):5s}"
          f"  lambda={fnum(lam):+.9f}  tr(G^-1 Q)=0 ? {str(bool(sp.simplify(tl)==0)):5s}"
          f"  {'<-- LAW VIOLATION' if m in viol else ''}")
print()
print(f"  LAW: (Re h ear-independent on theta-even)  <=>  gcd(m,15) > 1")
print(f"  violations over the complete period: {viol}   ->  LAW {'HOLDS' if not viol else 'FAILS'}")
assert not viol, "the law fails -- do not bank it"
units = [m for m in range(1, 16) if math.gcd(m, 15) == 1]
assert all(res["even"][m]["trace_is_zero"] for m in units), "tracelessness on units failed"
assert not any(res["even"][m]["trace_is_zero"] and res["even"][m]["gcd"] > 1 and res["even"][m]["lam"] != 0
               for m in range(1, 16))
print(f"  EXTRA (exact): tr(G^-1 Q_m) = 0 for ALL {len(units)} units of Z/15 -- the ear-dependent")
print(f"         readings are traceless, so the row carries NO mean, only spread.")
lams = sorted({round(res['even'][m]['lam'], 12) for m in range(1, 16) if res['even'][m]['ear_independent']})
print(f"  the ear-INDEPENDENT lambdas: {lams}  ({len(lams)} distinct)")

print()
print("=" * 78)
print("CONTROL: the ODD sector is ear-independent for EVERY m (B856 holds on all 15, exactly)")
print("=" * 78)
odd_all = True
for m in range(1, 16):
    Qm, G = Qform(m, Bod)
    lam, scalar = exact_scalar(Qm, G)
    odd_all &= bool(scalar)
    res["odd"][m] = dict(ear_independent=bool(scalar), lam=fnum(lam))
print(f"  odd sector ear-independent for all m=1..15 ? {odd_all}")
assert odd_all, "B856's ear-independence must hold on the whole period"
olam = sorted({round(res['odd'][m]['lam'], 12) for m in range(1, 16)})
print(f"  the odd lambdas over the full period: {olam}  ({len(olam)} distinct)")
print(f"  B856 period-5 control: Re h_odd(m) == Re h_odd(m+5) for all m ? "
      f"{all(abs(res['odd'][m]['lam'] - res['odd'][(m+5-1)%15+1]['lam']) < 1e-12 for m in range(1,16))}")

json.dump(res, open(os.path.join(HERE, "b1349e_results.json"), "w"), indent=1, sort_keys=True)
print("\n  wrote b1349e_results.json")
