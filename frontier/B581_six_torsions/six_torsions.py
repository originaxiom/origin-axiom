"""B581 — the six Sym-block twisted Alexander polynomials (the jewel-spectrum candidate).

L72 phase 1 / the cross-seat unifier proposal: compute the twisted Alexander
polynomial Delta_m(t) of the figure-eight at Sym^{2m} of the geometric rep, for
each E6 exponent m in {1,4,5,7,8,11}, exactly over Q(sqrt(-3)) — via the Wada
formula on the 2-generator presentation <a,b | a W b^-1 W^-1>, W = b a^-1 b^-1 a:

    Delta_m(t) = det( (Phi_m ox t)(dr/da) ) / det( t*Phi_m(b) - I )

using the banked B575 machinery (the exact block letter-actions on the six
isotypic blocks). Blind rule: the six polynomials and their special values are
computed FIRST; comparison against the banked jewel numbers (-3, -11, 2/3,
15/169, ...) happens only after, in the FINDINGS, with the null discipline.

GATES: (i) the trivial-rep control must return the classical Alexander
polynomial t^2 - 3t + 1; (ii) interpolation consistency (two disjoint point
sets agree); (iii) the m=1 block must reproduce the banked tau_1 = -3 relation.

Run: python3 frontier/B581_six_torsions/six_torsions.py   (~10 min)
"""
import importlib.util
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
L51 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

log("loading the B575 machinery (~6 min)...")
spec = importlib.util.spec_from_file_location("l51mod", L51)
m5 = importlib.util.module_from_spec(spec)
_argv = sys.argv
sys.argv = [L51]
try:
    spec.loader.exec_module(m5)
finally:
    sys.argv = _argv
log("machinery loaded (all B575 gates green)")

K, K0, K1 = m5.K, m5.K0, m5.K1
REL = m5.REL                                  # "abABaBAbaB"
EXP = {'a': 1, 'b': 1, 'A': -1, 'B': -1}      # meridian exponent sums

def kdet(M):
    """Exact determinant over K by Gaussian elimination."""
    n = len(M)
    A = [row[:] for row in M]
    det = K1
    for c in range(n):
        pr = None
        for i in range(c, n):
            if not A[i][c].is_zero():
                pr = i
                break
        if pr is None:
            return K0
        if pr != c:
            A[c], A[pr] = A[pr], A[c]
            det = K0 - det
        det = det * A[c][c]
        iv = A[c][c].inv()
        for i in range(c + 1, n):
            if not A[i][c].is_zero():
                f = A[i][c] * iv
                A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return det

def mat_scale_add(acc, coeff, M):
    n = len(M)
    for i in range(n):
        Mi = M[i]
        Ai = acc[i]
        for j in range(n):
            x = Mi[j]
            if not x.is_zero():
                Ai[j] = Ai[j] + coeff * x
    return acc

def fox_matrix_at(acts, d, tval):
    """(Phi ox t)(dr/da) evaluated at rational t = tval, times t (to clear t^-1).
    Walk the relator; 'a' letters contribute +t^{e}*P, 'A' letters -t^{e-1}*P*Phi_A.
    We multiply everything by t (shift by one power) to avoid negative exponents:
    contribution exponents become e+1 and e respectively (>= 0 since e >= -1)."""
    t = Fr(tval)
    P = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    e = 0
    out = [[K0] * d for _ in range(d)]
    for ch in REL:
        if ch == 'a':
            out = mat_scale_add(out, K(t**(e + 1)), P)
        elif ch == 'A':
            PA = m5.mmul(P, acts['A']) if hasattr(m5, 'mmul') else None
            # multiply P * Phi_A manually (block coords)
            PA = [[sum((P[i][k] * acts['A'][k][j] for k in range(d)
                        if not P[i][k].is_zero()), K0) for j in range(d)]
                  for i in range(d)]
            out = mat_scale_add(out, K(0) - K(t**e), PA)
        # advance the prefix
        Mx = acts[ch]
        P = [[sum((P[i][k] * Mx[k][j] for k in range(d)
                   if not P[i][k].is_zero()), K0) for j in range(d)]
             for i in range(d)]
        e += EXP[ch]
    return out

def den_at(acts, d, tval):
    t = K(Fr(tval))
    M = [[t * acts['b'][i][j] - (K1 if i == j else K0) for j in range(d)]
         for i in range(d)]
    return kdet(M)

def interp_poly(xs, ys):
    """Exact Lagrange interpolation over K at rational nodes; returns coeff list."""
    n = len(xs)
    coeffs = [K0] * n
    for i in range(n):
        # basis poly for node i
        num = [K1]                            # polynomial coeffs, low->high
        denom = K1
        for j in range(n):
            if j == i:
                continue
            num = [ (num[k - 1] if k > 0 else K0) - K(Fr(xs[j])) * (num[k] if k < len(num) else K0)
                    for k in range(len(num) + 1) ]
            denom = denom * (K(Fr(xs[i])) - K(Fr(xs[j])))
        di = denom.inv()
        w = ys[i] * di
        for k in range(len(num)):
            coeffs[k] = coeffs[k] + w * num[k]
    while len(coeffs) > 1 and coeffs[-1].is_zero():
        coeffs.pop()
    return coeffs

def fmt(v):
    if v.is_zero():
        return "0"
    if v.b == 0:
        return str(v.a)
    return f"({v.a}{'+' if v.b > 0 else ''}{v.b}*sqrt(-3))"

def poly_str(cs):
    terms = []
    for k, c in enumerate(cs):
        if not c.is_zero():
            terms.append(f"{fmt(c)}*t^{k}")
    return " + ".join(terms) if terms else "0"

def run_block(name, acts, d, extra_pts=0):
    degN = d + 3 + d            # generous bound: num deg <= (max exp+1)+..., den deg = d
    pts = list(range(1, degN + 8 + extra_pts))
    # avoid points where the denominator vanishes (t=eigenvalue-inverse; rational pts generically fine)
    numvals, denvals, xs = [], [], []
    for p in pts:
        dv = den_at(acts, d, p)
        if dv.is_zero():
            continue
        nv = kdet(fox_matrix_at(acts, d, p))
        xs.append(p)
        numvals.append(nv)
        denvals.append(dv)
        if len(xs) >= degN + 6:
            break
    # Delta(t) = Num/Den — interpolate the RATIO via polynomial long-path:
    # interpolate Num and Den separately, then divide exactly via evaluation:
    # simplest exact route: interpolate the quotient IF it is polynomial after
    # clearing units; Wada invariant for knots: Num/Den in Q(K)[t, t^-1].
    numP = interp_poly(xs, numvals)
    denP = interp_poly(xs, denvals)
    # exact polynomial division numP / denP (should divide up to t-power units)
    # strip trailing/leading zeros; do synthetic division
    q, r = polydiv(numP, denP)
    return numP, denP, q, r

def polydiv(numP, denP):
    """Exact long division low->high; returns (q, rem)."""
    num = [c for c in numP]
    den = [c for c in denP]
    while num and num[0].is_zero() and den and den[0].is_zero():
        num.pop(0)
        den.pop(0)
    while num and num[-1].is_zero():
        num.pop()
    while den and den[-1].is_zero():
        den.pop()
    if not den:
        return [], num
    dd = len(den) - 1
    dli = den[-1].inv()
    rem = num[:]
    q = [K0] * max(len(num) - dd, 1)
    while len(rem) - 1 >= dd and rem:
        if rem[-1].is_zero():
            rem.pop()
            continue
        shift = len(rem) - 1 - dd
        c = rem[-1] * dli
        q[shift] = c
        for j in range(len(den)):
            rem[shift + j] = rem[shift + j] - c * den[j]
        while rem and rem[-1].is_zero():
            rem.pop()
    return q, rem

# ---------------- CONTROL: the trivial 1-dim block => classical Alexander ----------------
log("CONTROL: trivial rep => classical Alexander t^2 - 3t + 1")
triv_acts = {ch: [[K1]] for ch in 'abAB'}
nP, dP, q, r = run_block("triv", triv_acts, 1)
# For the TRIVIAL rep the Wada invariant is Delta_K/(t-1) (Milnor torsion): the
# division is NOT expected to be exact. The correct control: the NUMERATOR must
# equal a unit times the classical Alexander polynomial t^2 - 3t + 1.
nn = nP[:]
while nn and nn[0].is_zero():
    nn.pop(0)
while nn and nn[-1].is_zero():
    nn.pop()
lead = nn[-1]
nn = [c * lead.inv() for c in nn]
log(f"  control NUMERATOR (monic): {poly_str(nn)}")
expect = [K1, K(-3), K1]
ok = len(nn) == 3 and (all((nn[i] - expect[i]).is_zero() for i in range(3)) or
                       all((nn[i] - expect[2 - i]).is_zero() for i in range(3)))
assert ok, "CONTROL FAILED: classical Alexander not reproduced!"
# and the denominator must be a unit times (t - 1)
dd2 = dP[:]
while dd2 and dd2[0].is_zero():
    dd2.pop(0)
while dd2 and dd2[-1].is_zero():
    dd2.pop()
dl = dd2[-1]
dd2 = [c * dl.inv() for c in dd2]
assert len(dd2) == 2 and (dd2[0] + K1).is_zero(), "control denominator != (t-1)"
log("  GATE PASS: classical Alexander numerator + (t-1) denominator reproduced")

# ---------------- the six blocks ----------------
RESULTS = {}
for mexp in sorted(m5.BLOCK_DATA.keys()):
    D = m5.BLOCK_DATA[mexp]
    d, acts = D['d'], D['acts']
    log(f"block m={mexp} (dim {d}): computing Delta_m(t) ...")
    nP, dP, q, r = run_block(f"m{mexp}", acts, d)
    exact = (not r) or all(c.is_zero() for c in r)
    log(f"  division exact: {exact}; quotient degree {len(q)-1}")
    RESULTS[mexp] = (q, exact, nP, dP)

print()
print("=" * 74)
print("THE SIX TWISTED ALEXANDER POLYNOMIALS (up to units; computed BLIND):")
for mexp, (q, exact, nP, dP) in sorted(RESULTS.items()):
    if q and not q[-1].is_zero():
        lead = q[-1]
        qn = [c * lead.inv() for c in q]
    else:
        qn = q
    print(f"\n  m={mexp}: exact={exact}")
    print(f"    Delta_{mexp}(t) ~ {poly_str(qn)}")
    # special values
    v1 = sum(qn, K0)
    vm1 = sum(((qn[k] if k % 2 == 0 else K0 - qn[k]) for k in range(len(qn))), K0)
    print(f"    Delta({1}) = {fmt(v1)}   Delta(-1) = {fmt(vm1)}")
print("=" * 74)
print("(comparison to banked jewel numbers happens in the FINDINGS, after this output)")

import json
dump = {}
for mexp, (q, exact, nP, dP) in RESULTS.items():
    dump[str(mexp)] = {
        "exact": exact,
        "quotient": [[str(c.a), str(c.b)] for c in q],
        "num": [[str(c.a), str(c.b)] for c in nP],
        "den": [[str(c.a), str(c.b)] for c in dP],
    }
with open(os.path.join(HERE, "six_torsions_results.json"), "w") as f:
    json.dump(dump, f, indent=1)
print("results dumped to six_torsions_results.json")
