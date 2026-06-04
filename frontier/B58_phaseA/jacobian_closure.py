"""B58 Phase A -- exact (n^2-1) fixed-line Jacobian via eps-series over F_p.

The (n^2-1) fixed-line Jacobian of the metallic trace map is the tower object
whose char(J) factors over the Dickson catalog {char(+-M^k)} -- the a_d/b_d
multiplicities.  B63/B65 built it by rep-perturbation numerics + rational
interpolation; B66 by rep-perturbation + mpmath SVD-pinv, which CEILINGS OUT at
n=6 (gauge degeneracy = ill-conditioned pinv).  This module computes the SAME
object via the same pinv-LIMIT but EXACTLY over F_p (no float conditioning).

The limit.  B66 forms DT(eps)=DX(eps).pinv(Dx(eps)) with A=exp(eps P), B=exp(eps Q)
and extrapolates eps->0.  rho(eps) is NOT a fixed point of phi (so DT.Dx=DX is
INCONSISTENT for eps!=0); the trace map is first-order degenerate at the identity
(Dx(0)=0), so DT(0) is a 0/0 least-squares limit -- exactly why a pinv is needed.
We compute it exactly.  Work in the ring F_p[eps]/(eps^{L+1}) (x) F_p[h]/(h^2):
reps A=(I+h g)exp(eps P) are EXACTLY in SL(n) to all tracked eps-orders.  The h^1
part of tr(word) is the gradient row Dx(eps)=sum_{l>=1} Dx_l eps^l (eps^1 alone is
the rank-3 Fricke block; the n^2-1 coordinates only separate across orders 1..L).
The least-squares solution satisfies the NORMAL equations exactly:
    DT(eps) G(eps) = R(eps),   G = Dx S Dx^T,  R = DX S Dx^T   (S a random metric)
which (unlike DT.Dx=DX) are consistent; their power-series solution DT(eps)=sum DT_j
eps^j is analytic at 0, and DT_0 is the fixed-line Jacobian.  Solving order-by-order
DECOUPLES BY ROW, so each solve is small and exact over F_p.

Pipeline.  Words (the n^2-1 coordinate basis) are picked by B66's proven near-fixed-
line QR-pivot (b66_select) -- a BASIS choice only; the Jacobian is then computed
exactly and validated prime-stable + against B65, so the selection does not affect
rigor.  The n x n matrix arithmetic AUTOMATICALLY enforces Cayley-Hamilton / the
exterior-power closure (a concrete matrix satisfies its own char poly), so
e_2..e_{n-1} need no hand-built multi-block trace identities (the gap B64 localized,
B65 sidestepped).

Status (m=1; sigma:(X,Y)->(X+Y,X)).  VALIDATED exact + prime-stable at n=3 and n=4
(the POC gate: reproduces B65's a_d=(1,1,1,1), b_2=1 EXACTLY).  At n=5 it reproduces
the tower EXCEPT the char(M^2) block (resolves multiplicity 1, not 2) and the (t+1)
parity (1, not 2), leaving a degree-3 untagged remainder; this is L-stable and
prime-stable (converged).  The localized gap is the doubly-degenerate even-k /
e_2=tr(Lambda^2 A) sector -- note the *fundamental* char(M^1) multiplicity-2
resolves correctly, only the Lambda^2-sector multiplicity-2 fails.  Computer-assisted
modular EVIDENCE, not a symbolic proof.  No commit until reviewed.
"""

from __future__ import annotations

import sys
from math import factorial
from pathlib import Path

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "B58_stage1"))
from step1_cotangent import rref, solve, tag_charpoly  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "B66_sl6_tower"))

t = sp.symbols("t")


def b66_select(n, maxlen, seed=20):
    """Pick n^2-1 words forming a valid coordinate system AT THE FIXED LINE.

    The fixed-line Jacobian's coordinates must be independent over F_p(eps) (in the
    eps->0 limit), NOT merely at a generic rep -- power traces like tr(A),tr(A^2),...
    are independent generically but Newton-dependent at the fixed line.  B66's QR-pivot
    at a near-fixed-line rep (the proven selection) picks such a set.  This is only a
    BASIS choice; the Jacobian is then computed exactly over F_p and validated
    prime-stable + against B65, so the selection method does not affect rigor."""
    import validate as _v
    return _v.select_words(n, maxlen, seed)

KNOWN_TOWER = {
    3: {"char(M^-1)": 1, "char(M^2)": 1, "char(M^3)": 1, "(t-1)": 1, "(t+1)": 1},
    4: {"char(M^-1)": 1, "char(M^1)": 1, "char(M^2)": 1, "char(M^3)": 1, "char(M^4)": 1,
        "char(-M^2)": 1, "(t-1)": 2, "(t+1)": 1},
    5: {"char(M^-1)": 1, "char(M^1)": 2, "char(M^2)": 2, "char(M^3)": 1, "char(M^4)": 1,
        "char(M^5)": 1, "char(-M^2)": 1, "char(-M^3)": 1, "(t-1)": 2, "(t+1)": 2},
}


# --------------------------------------------------------------------------- #
# sl(n) basis + random samples over F_p
# --------------------------------------------------------------------------- #

def basis_sln(n):
    B = []
    for i in range(n):
        for j in range(n):
            if i != j:
                e = np.zeros((n, n), dtype=np.int64)
                e[i, j] = 1
                B.append(e)
    for i in range(n - 1):
        e = np.zeros((n, n), dtype=np.int64)
        e[i, i], e[i + 1, i + 1] = 1, -1
        B.append(e)
    return B


def random_traceless(n, p, rng):
    Z = rng.integers(0, p, size=(n, n)).astype(np.int64)
    Z[n - 1, n - 1] = (-Z[np.arange(n - 1), np.arange(n - 1)].sum()) % p
    return Z % p


# --------------------------------------------------------------------------- #
# eps-polynomial matrices: array (L+1, n, n) = sum_e coeff[e] eps^e   (mod p, eps^{L+1}=0)
# --------------------------------------------------------------------------- #

def ep_zero(L, n):
    return np.zeros((L + 1, n, n), dtype=np.int64)


def ep_eye(L, n):
    Z = ep_zero(L, n)
    Z[0] = np.eye(n, dtype=np.int64)
    return Z


def ep_mul(A, B, p):
    L = A.shape[0] - 1
    n = A.shape[1]
    C = np.zeros((L + 1, n, n), dtype=np.int64)
    for e in range(L + 1):
        acc = np.zeros((n, n), dtype=np.int64)
        for i in range(e + 1):
            acc += A[i] @ B[e - i]
        C[e] = acc % p
    return C


def ep_inv(A, p):
    """inverse of an eps-poly with A[0]=I:  sum_{k=0}^L (-N)^k,  N=A-I (N nilpotent)."""
    L = A.shape[0] - 1
    n = A.shape[1]
    negN = (-A) % p
    negN[0] = (negN[0] + np.eye(n, dtype=np.int64)) % p       # -(A-I) = I - A, then const-> 0
    negN[0] = 0
    acc = ep_eye(L, n)
    term = ep_eye(L, n)
    for _ in range(1, L + 1):
        term = ep_mul(term, negN, p)
        acc = (acc + term) % p
    return acc


def ep_exp(P, p, L):
    """exp(eps P) truncated:  coeff of eps^k is P^k / k!  (det = 1 to all orders)."""
    n = P.shape[0]
    E = ep_zero(L, n)
    Pk = np.eye(n, dtype=np.int64)
    for k in range(L + 1):
        invk = pow(factorial(k) % p, p - 2, p)
        E[k] = (Pk * invk) % p
        Pk = (Pk @ P) % p
    return E


# --------------------------------------------------------------------------- #
# dual eps-h elements: (h0, h1), each an eps-poly  (value + d/dh part; h^2=0)
# --------------------------------------------------------------------------- #

def de_mul(A, B, p):
    a0, a1 = A
    b0, b1 = B
    return (ep_mul(a0, b0, p), (ep_mul(a0, b1, p) + ep_mul(a1, b0, p)) % p)


def de_inv(A, p):
    a0, a1 = A
    a0i = ep_inv(a0, p)
    return (a0i, (-ep_mul(ep_mul(a0i, a1, p), a0i, p)) % p)


def de_pow(A, k, p):
    L = A[0].shape[0] - 1
    n = A[0].shape[1]
    R = (ep_eye(L, n), ep_zero(L, n))
    for _ in range(k):
        R = de_mul(R, A, p)
    return R


def de_trace_h1(A, p):
    """eps-poly of the h^1 part of tr(A): the gradient row as a series in eps."""
    h1 = A[1]
    return np.array([int(np.trace(h1[e])) % p for e in range(h1.shape[0])], dtype=np.int64)


# --------------------------------------------------------------------------- #
# the gradient series Dx_l (substitute=False) and DX_l (=True), l = 1..L
# --------------------------------------------------------------------------- #

def _const_ep(g, L, p):
    n = g.shape[0]
    G = ep_zero(L, n)
    G[0] = g % p
    return G


def build_grad_series(words, P, Q, basis, p, L, m=1, substitute=False):
    """Returns array (L, len(words), 2*dim): eps^l coeff (l=1..L) of the h^1 trace,
    columns = A-perturbations (by each basis elt) then B-perturbations."""
    n = P.shape[0]
    dim = len(basis)
    expP, expQ = ep_exp(P, p, L), ep_exp(Q, p, L)
    out = np.zeros((L, len(words), 2 * dim), dtype=np.int64)
    for which in ("A", "B"):
        for jg, g in enumerate(basis):
            col = jg if which == "A" else dim + jg
            G = _const_ep(g, L, p)
            if which == "A":
                A_d = (expP, ep_mul(G, expP, p))       # (I + h g) exp(eps P)
                B_d = (expQ, ep_zero(L, n))
            else:
                A_d = (expP, ep_zero(L, n))
                B_d = (expQ, ep_mul(G, expQ, p))
            if substitute:                              # phi_m: a -> a^m b, b -> a
                A_eff = de_mul(de_pow(A_d, m, p), B_d, p)
                B_eff = A_d
            else:
                A_eff, B_eff = A_d, B_d
            mats = {"A": A_eff, "B": B_eff, "a": de_inv(A_eff, p), "b": de_inv(B_eff, p)}
            for r, w in enumerate(words):
                acc = (ep_eye(L, n), ep_zero(L, n))
                for c in w:
                    acc = de_mul(acc, mats[c], p)
                series = de_trace_h1(acc, p)            # eps^0..eps^L ; eps^0 == 0
                out[:, r, col] = series[1:]
    return out


# --------------------------------------------------------------------------- #
# solve the eps power series for DT_0  (least-squares normal equations -- consistent)
#
# rho(eps) is NOT a fixed point of phi for eps!=0, so DT.Dx=DX is INCONSISTENT;
# B66 uses the least-squares pinv whose eps->0 limit is the fixed-point Jacobian.
# Exact F_p analog: the NORMAL equations DT.G = R (G=Dx S Dx^T, R=DX S Dx^T) ARE
# consistent (any LS solution satisfies them), and the eps->0 limit is independent
# of the metric S (the residual -> 0 at the fixed point).  Random S avoids accidental
# F_p singularity of the Gram; prime/seed variation tests metric-independence.
# --------------------------------------------------------------------------- #

def build_GR(Dx, DX, S, p):
    """G_l = sum_{i+j=l} Dx_i S Dx_j^T,  R_l = sum DX_i S Dx_j^T.  Only l<=L+1 are
    COMPLETE (for l>L+1 the pairs with index>L are missing from the eps-truncation),
    so we return orders up to L+1 only."""
    L, dim, _ = Dx.shape
    DxS = np.einsum("lij,jk->lik", Dx, S) % p
    DXS = np.einsum("lij,jk->lik", DX, S) % p
    mo = L + 1
    G = np.zeros((mo + 1, dim, dim), dtype=np.int64)
    R = np.zeros((mo + 1, dim, dim), dtype=np.int64)
    for l in range(2, mo + 1):
        for i in range(max(1, l - L), min(L, l - 1) + 1):
            G[l] = (G[l] + DxS[i - 1] @ Dx[l - i - 1].T) % p
            R[l] = (R[l] + DXS[i - 1] @ Dx[l - i - 1].T) % p
    return G, R


def solve_DT0(G, R, dim, L, p):
    """Solve the power series DT(eps) G(eps) = R(eps): R_m = sum_{j=0}^{m-2} DT_j G_{m-j}.
    Decouples per row a; one shared coefficient matrix.  Returns DT_0 (the eps->0 limit).
    Uses only the COMPLETE orders (m<=L+1)."""
    mo = L + 1
    jmax = mo - 2                       # DT orders 0..jmax
    morders = list(range(2, mo + 1))    # equation orders
    rows, cols = len(morders) * dim, (jmax + 1) * dim
    Mcoef = np.zeros((rows, cols), dtype=np.int64)
    for mi, m in enumerate(morders):
        for j in range(0, jmax + 1):
            o = m - j
            if 2 <= o <= mo:            # coeff of DT_j[a,b] in eqn (m,c) is G_{m-j}[b,c]
                r0, c0 = mi * dim, j * dim
                Mcoef[r0:r0 + dim, c0:c0 + dim] = (Mcoef[r0:r0 + dim, c0:c0 + dim] + G[o].T) % p
    DT0 = np.zeros((dim, dim), dtype=np.int64)
    for a in range(dim):
        rhs = np.concatenate([R[m][a, :] % p for m in morders])
        z = solve(Mcoef, rhs, p)
        if z is None:
            return None, a
        DT0[a, :] = z[:dim] % p
    return DT0, None


# --------------------------------------------------------------------------- #
# driver
# --------------------------------------------------------------------------- #

PRIMES = [2000003, 2000029, 2000039]


def jacobian(n, p, seed, maxlen, L, words=None, m=1):
    rng = np.random.default_rng(seed)
    basis = [b % p for b in basis_sln(n)]
    P, Q = random_traceless(n, p, rng), random_traceless(n, p, rng)
    dim = n * n - 1
    if words is None:                                   # default: B66's proven near-fixed-line selection
        words = b66_select(n, maxlen, seed=20)
    info = {"dim": dim, "n_words": len(words)}
    info["words"] = words
    Dx = build_grad_series(words, P, Q, basis, p, L, m=m, substitute=False)
    DX = build_grad_series(words, P, Q, basis, p, L, m=m, substitute=True)
    U = rng.integers(0, p, size=(2 * dim, 2 * dim)).astype(np.int64)
    S = (U + U.T) % p                                   # random symmetric metric
    G, R = build_GR(Dx, DX, S, p)
    DT0, badrow = solve_DT0(G, R, dim, L, p)
    if DT0 is None:
        info["status"] = f"INCONSISTENT/UNDETERMINED at row {badrow} (increase L?)"
        return None, info
    info["status"] = "ok"
    return DT0, info


def a_b_rows(tower):
    a, b = {}, {}
    for lab, mult in tower.items():
        if lab.startswith("char(M^") and not lab.startswith("char(M^-"):
            a[int(lab[len("char(M^"):-1])] = mult
        elif lab.startswith("char(-M^"):
            b[int(lab[len("char(-M^"):-1])] = mult
    return a, b


def run_n(n, maxlen, L, primes=PRIMES, m=1, verbose=True):
    words = b66_select(n, maxlen, seed=20)              # one basis, reused across primes
    results = []
    for pi, p in enumerate(primes):
        DT, info = jacobian(n, p, seed=20 + pi, maxlen=maxlen, L=L, words=words, m=m)
        if DT is None:
            results.append({"prime": p, "status": info["status"]})
            if verbose:
                print(f"  SL({n}) p={p}: {info['status']}")
            continue
        tower, remok = tag_charpoly(DT, p, kmax=2 * n)
        if not remok:
            tower["UNTAGGED_REMAINDER"] = 1
        a, b = a_b_rows(tower)
        results.append({"prime": p, "status": "ok", "tower": tower, "a_d": a, "b_d": b,
                        "untagged": not remok})
        if verbose:
            print(f"  SL({n}) p={p}: a_d={dict(sorted(a.items()))} b_d={dict(sorted(b.items()))}"
                  f"{'' if remok else '  [UNTAGGED REMAINDER]'}")
    ok_res = [r for r in results if r["status"] == "ok"]
    stable = (len(ok_res) == len(primes) and all(ok_res[0]["tower"] == r["tower"] for r in ok_res))
    expected = KNOWN_TOWER.get(n)
    gate = ((ok_res[0]["tower"] == expected) and stable) if (expected and ok_res) else None
    return {"n": n, "dim": n * n - 1, "maxlen": maxlen, "L": L, "n_words": len(words),
            "words": words, "results": results, "prime_stable": stable,
            "expected": expected, "gate_pass": gate}


PLAN = [(3, 4, 8), (4, 4, 12), (5, 4, 12)]   # (n, maxlen, L)


def main():
    import json
    print("B58 Phase A -- exact (n^2-1) fixed-line Jacobian over F_p (m=1)")
    print("Method: eps-series F_p[eps]/(eps^{L+1}) (x) F_p[h]/(h^2); LS normal-equation pinv-limit\n")
    out = {"job": "B58_phaseA_jacobian_closure", "m": 1, "primes": PRIMES,
           "method": ("exact F_p eps-series least-squares pinv-limit of B66's DT(eps)="
                      "DX.pinv(Dx); B66 near-fixed-line word selection (basis choice); "
                      "n x n matrix arithmetic auto-enforces Cayley-Hamilton/exterior-power closure"),
           "results": {}}
    for n, ml, L in PLAN:
        print(f"SL({n}) (dim {n*n-1}, maxlen {ml}, L={L}):")
        res = run_n(n, ml, L)
        tag = {True: "GATE PASS", False: "GATE FAIL", None: "(sanity, no gate)"}[res["gate_pass"]]
        a = res["results"][0].get("a_d") if res["results"][0].get("status") == "ok" else None
        b = res["results"][0].get("b_d") if res["results"][0].get("status") == "ok" else None
        print(f"  a_d={a} b_d={b}  prime-stable={res['prime_stable']}  ->  {tag}\n")
        out["results"][f"n={n}"] = {
            "dim": res["dim"], "maxlen": ml, "L": L, "n_words": res["n_words"],
            "words": res["words"], "prime_stable": res["prime_stable"],
            "gate_pass": res["gate_pass"], "expected_tower": res["expected"],
            "computed_tower": res["results"][0].get("tower"),
            "a_d": a, "b_d": b}
    OUT = Path(__file__).resolve().parent / "phaseA_results.json"
    OUT.write_text(json.dumps(out, indent=2, default=str))
    print(f"wrote {OUT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
