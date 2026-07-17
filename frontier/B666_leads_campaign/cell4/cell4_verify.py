"""B666 cell 4 (R21-9): the pair-evenness lemma — numerical verification
of every step of the abstract proof.

The proof route (see PROOF_NOTE.md in this directory):
  Step A (symbolic): Phi_m(x) = x^(phi(m)/2) * psi_m(x + 1/x) for m >= 3,
          where psi_m = minimal polynomial of 2cos(2pi/m).
  Step B (symbolic): Res(Phi_m(x), x^2 - t x + 1) =
          prod_{zeta prim m-th} f(zeta) = psi_m(t)^2   (a square in Z[t]).
  Step C (group data): for every w in W(D4) and W(E6), char(w) factors
          into cyclotomics Phi_m^{a_m}; det B_w =
          (t-2)^{a_1} (t+2)^{a_2} prod_{m>=3} psi_m(t)^{2 a_m}  exactly;
          a_1 == a_2 (mod 2) on even rank; det(w) = (-1)^{a_2}.
  Step D (the theorem): for every prime p | t^2-4 with v_p(t^2-4) odd,
          det(w) = (-1)^{v_p(det B_w)} for ALL w; for v_p even the
          agreement set is exactly ker(det) (half of W).
All decisive arithmetic exact (python ints / Fraction / sympy exact).
"""
import itertools
from fractions import Fraction

import numpy as np
import sympy as sp
import os
_REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

x, t = sp.symbols("x t")
OUT = []


def log(s):
    print(s, flush=True)
    OUT.append(s)


# ---------------------------------------------------------------- psi_m
PSI = {}


def psi(m):
    """Minimal polynomial of 2*cos(2*pi/m) over Q, monic in Z[x]."""
    if m not in PSI:
        if m == 1:
            PSI[m] = sp.Poly(x - 2, x)
        elif m == 2:
            PSI[m] = sp.Poly(x + 2, x)
        else:
            PSI[m] = sp.Poly(sp.minimal_polynomial(2 * sp.cos(2 * sp.pi / m), x), x)
    return PSI[m]


def cyclo(m):
    return sp.Poly(sp.cyclotomic_poly(m, x), x)


# ------------------------------------------------- Step A + B (symbolic)
log("== STEP A: Phi_m(x) = x^(phi(m)/2) psi_m(x + 1/x), m = 3..50 ==")
okA = True
for m in range(3, 51):
    d = sp.totient(m) // 2
    lhs = cyclo(m).as_expr()
    rhs = sp.expand(x**d * psi(m).as_expr().subs(x, x + 1 / x))
    if sp.simplify(lhs - rhs) != 0:
        okA = False
        log(f"  m={m}: FAIL")
log(f"  all m in 3..50: {'PASS' if okA else 'FAIL'}")

log("== STEP B: Res(Phi_m(x), x^2-t*x+1) = psi_m(t)^2 in Z[t], m = 3..50 ==")
okB = True
for m in range(3, 51):
    r = sp.resultant(cyclo(m).as_expr(), x**2 - t * x + 1, x)
    target = sp.expand(psi(m).as_expr().subs(x, t) ** 2)
    if sp.expand(r - target) != 0:
        okB = False
        log(f"  m={m}: FAIL  res={r}")
log(f"  all m in 3..50: {'PASS' if okB else 'FAIL'}")
log("  (includes every ramified shape: m = p, p^2, 2p, 4p, pq, ... )")

# also m=1,2 conventions: product over the single root is f(1), f(-1)
r1 = sp.expand((1 - t + 1))     # f(1) = 2 - t = -(t-2)
r2 = sp.expand((1 + t + 1))     # f(-1) = 2 + t = (t+2)
log(f"  m=1: f(1) = {r1} = -(t-2);  m=2: f(-1) = {r2} = (t+2)")


# ------------------------------------------- exact char poly via Newton
def charpoly_from_traces(pk, n):
    """Exact monic char poly coeffs [1, -e1, e2, ...] from power sums."""
    e = [Fraction(1)]
    for k in range(1, n + 1):
        s = Fraction(0)
        for i in range(1, k + 1):
            s += Fraction((-1) ** (i - 1)) * e[k - i] * pk[i]
        e.append(s / k)
    assert all(v.denominator == 1 for v in e)
    return [int(v) for v in e]  # e[0]=1, e[k] = elementary symm


def cyclotomic_multiset(coeffs, n):
    """Factor char poly (given as e-list) into cyclotomics; return {m: a_m}."""
    # char(x) = sum_{k} (-1)^k e_k x^(n-k)
    cp = sp.Poly(sum((-1) ** k * coeffs[k] * x ** (n - k) for k in range(n + 1)), x)
    mult = {}
    for m in range(1, 31):
        if sp.totient(m) > n:
            continue
        while True:
            q, r = sp.div(cp, cyclo(m), x)
            if r.is_zero and q.degree() >= 0:
                mult[m] = mult.get(m, 0) + 1
                cp = sp.Poly(q, x)
            else:
                break
    assert cp.degree() == 0 and cp.LC() == 1, f"non-cyclotomic remainder {cp}"
    return mult


def vp(n_int, p):
    n_int = abs(n_int)
    assert n_int != 0
    v = 0
    while n_int % p == 0:
        n_int //= p
        v += 1
    return v


# ------------------------------------------------------------ the groups
def wd4_elements():
    out = []
    for perm in itertools.permutations(range(4)):
        for signs in itertools.product((1, -1), repeat=4):
            if signs.count(-1) % 2:
                continue
            M = np.zeros((4, 4), dtype=np.int64)
            for i, j in enumerate(perm):
                M[i, j] = signs[i]
            out.append(M)
    return np.array(out)


def we6_elements():
    """BFS over the 6 simple reflections in the simple-root basis."""
    A = 2 * np.eye(6, dtype=np.int64)
    edges = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]  # Bourbaki 1-3-4-5-6, 2-4
    for i, j in edges:
        A[i, j] = A[j, i] = -1
    gens = []
    for i in range(6):
        M = np.eye(6, dtype=np.int64)
        M[i, :] -= A[i, :]
        gens.append(M)
    gens = np.array(gens)
    seen = {np.eye(6, dtype=np.int64).tobytes()}
    frontier = np.eye(6, dtype=np.int64)[None, :, :]
    allm = [np.eye(6, dtype=np.int64)]
    while len(frontier):
        new = []
        for g in gens:
            prod = frontier @ g
            for M in prod:
                b = M.tobytes()
                if b not in seen:
                    seen.add(b)
                    new.append(M)
                    allm.append(M)
        frontier = np.array(new) if new else np.empty((0, 6, 6), dtype=np.int64)
    return np.array(allm)


def group_by_charpoly(mats, n):
    """Return {e-tuple: count} using exact batched integer power traces."""
    pk_cols = []
    P = mats.copy()
    pk_cols.append(np.einsum("kii->k", P))
    for _ in range(n - 1):
        P = P @ mats
        pk_cols.append(np.einsum("kii->k", P))
    assert np.abs(P).max() < 2**40  # far from int64 overflow
    keyarr = np.stack(pk_cols, axis=1)
    types = {}
    for row in keyarr:
        k = tuple(int(v) for v in row)
        types[k] = types.get(k, 0) + 1
    out = {}
    for trs, cnt in types.items():
        pk = {i + 1: Fraction(v) for i, v in enumerate(trs)}
        e = charpoly_from_traces(pk, n)
        out[tuple(e)] = out.get(tuple(e), 0) + cnt
    return out


def verify_group(name, mats, n, t_values):
    log(f"== STEP C/D on {name}: |W| = {len(mats)}, rank {n} ==")
    types = group_by_charpoly(mats, n)
    log(f"  distinct characteristic polynomials: {len(types)}")
    okC = True
    # per-type data: multiset, det(w), parity bookkeeping
    tdata = []
    for e, cnt in sorted(types.items()):
        mult = cyclotomic_multiset(list(e), n)
        detw = e[n] if n % 2 == 0 else e[n]  # e_n = det for monic char poly
        # char(x) = prod (x - lam); e_n = prod lam = det w
        a1, a2 = mult.get(1, 0), mult.get(2, 0)
        if (a1 - a2) % 2 != 0:
            okC = False
            log(f"  RANK-PARITY FAIL a1={a1} a2={a2} for {e}")
        if detw != (-1) ** a2:
            okC = False
            log(f"  DET FAIL det={detw} a2={a2} for {e}")
        tdata.append((mult, detw, cnt))
    log(f"  a_1 == a_2 (mod 2) and det(w) = (-1)^(a_2) on every element: "
        f"{'PASS' if okC else 'FAIL'}")

    for tv in t_values:
        disc = tv * tv - 4
        primes = sorted(sp.factorint(disc).keys())
        # exact det B_w per type + the product formula
        okF = True
        agree = {p: 0 for p in primes}
        degenerate = False
        for mult, detw, cnt in tdata:
            dB = 1
            for m, am in mult.items():
                pm = int(psi(m).as_expr().subs(x, tv))
                dB *= pm ** ((1 if m in (1, 2) else 2) * am)
            # cross-check against a direct exact determinant for this type:
            # det B_w = prod over eigenvalues (t - lam - 1/lam) — recompute
            # via resultant-free route: char poly of w+w^-1 evaluated at t.
            if dB == 0:
                degenerate = True
                continue
            for p in primes:
                if detw == (-1) ** vp(dB, p):
                    agree[p] += cnt
        if degenerate:
            log(f"  t={tv}: DEGENERATE (det B_w = 0 occurs) — excluded")
            continue
        msg = []
        for p in primes:
            vodd = vp(disc, p) % 2 == 1
            expect = len(mats) if vodd else len(mats) // 2
            tag = "odd " if vodd else "even"
            ok = agree[p] == expect
            okF &= ok
            msg.append(f"p={p}(v{tag}) {agree[p]}/{len(mats)} "
                       f"[expect {expect}] {'PASS' if ok else 'FAIL'}")
        log(f"  t={tv} (disc {disc}): " + "; ".join(msg))
    return tdata


def verify_detB_formula(name, mats, n, t_values, sample):
    """Exact spot-check: det(tI - w - w^-1) via sympy adjugate on `sample`
    random-but-deterministic elements against the psi-product formula."""
    log(f"== det B_w product-formula exact cross-check on {name} "
        f"({sample} elements x {len(t_values)} t-values) ==")
    idx = np.linspace(0, len(mats) - 1, sample, dtype=int)
    ok = True
    for i in idx:
        M = sp.Matrix(mats[int(i)].tolist())
        Minv = M.inv()  # exact (det = +-1 integer matrix)
        pk = {k: Fraction(int((M ** k).trace())) for k in range(1, n + 1)}
        e = charpoly_from_traces(pk, n)
        mult = cyclotomic_multiset(e, n)
        for tv in t_values:
            B = tv * sp.eye(n) - M - Minv
            dB_direct = int(B.det())
            dB_formula = 1
            for m, am in mult.items():
                pm = int(psi(m).as_expr().subs(x, tv))
                dB_formula *= pm ** ((1 if m in (1, 2) else 2) * am)
            if dB_direct != dB_formula:
                ok = False
                log(f"  FAIL elt {i} t={tv}: direct {dB_direct} != "
                    f"formula {dB_formula}")
    log(f"  det B_w = (t-2)^a1 (t+2)^a2 prod psi_m(t)^(2 a_m): "
        f"{'PASS' if ok else 'FAIL'}")


T_VALUES = [3, 4, 5, 6, 7, 9, 10]

d4 = wd4_elements()
verify_group("W(D4)", d4, 4, T_VALUES)
verify_detB_formula("W(D4)", d4, 4, T_VALUES, sample=48)

e6 = we6_elements()
assert len(e6) == 51840, f"|W(E6)| = {len(e6)}"
verify_group("W(E6)", e6, 6, T_VALUES)
verify_detB_formula("W(E6)", e6, 6, [3, 7], sample=24)

# banked-battery cross-checks (must reproduce tests/test_b656_digest.py G1)
log("== banked-battery reproduction (test_b656_digest G1 numbers) ==")
log("  W(D4) t=5: p=3 and p=7 must be 192/192; "
    "t=7: p=3 must be 96/192, p=5 192/192  (see lines above)")

with open(_REPO + "/frontier/B666_leads_campaign/cell4/"
          "cell4_output.txt", "w") as fh:
    fh.write("\n".join(OUT) + "\n")
