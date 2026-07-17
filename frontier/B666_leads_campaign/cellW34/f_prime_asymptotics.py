"""B666 cell W3-4 — F' (re-scoped per ADDENDUM_1 amendment / B668):
THE ASYMPTOTICS DERIVATION NOTE — the computations.

Classifies the banked observable families by genuine large-k behavior and
derives the exact growth exponents.  Anchors (verify-don't-trust):
  - SU(2) KP product formula vs the banked su2_data closed form (B238);
  - SU(3) KP product formula vs the banked su3_data Weyl sum at k=2 (B238);
  - SU(3) Casimir vs the banked su32_wrt header formula;
  - E6 KP product formula vs a Weyl-sum S_00 at k=2 built by the banked
    B570 method (BFS Weyl group, |W| = 51840 asserted);
  - torsion towers vs cellB2's exact 78-entry landscape (B617 closed form).

Exact arithmetic (sympy Integer/Rational) in every decisive identity;
mpmath (40 digits) for the asymptotic-slope demonstrations.
"""
import json
import os

import numpy as np
import sympy as sp
from mpmath import mp, mpf, pi as MPPI, sin as msin, log as mlog

mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

print("=" * 72)
print("PART A — root systems, exact identities, KP growth exponents")
print("=" * 72)

CARTAN = {
    "A1": [[2]],
    "A2": [[2, -1], [-1, 2]],
    # E6, the banked B570 convention (node 2 = the branch node)
    "E6": [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
           [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
}
EXPECT = {"A1": dict(npos=1, det=2, hv=2, dim=3),
          "A2": dict(npos=3, det=3, hv=3, dim=8),
          "E6": dict(npos=36, det=3, hv=12, dim=78)}


def positive_roots(A):
    """Closure from the simple roots (simply-laced, (a_i,a_i)=2): coords in
    the simple-root basis; (b, a_i) = (A b)_i."""
    n = len(A)
    A = sp.Matrix(A)
    roots = {tuple(int(x) for x in sp.eye(n).col(i)) for i in range(n)}
    frontier = set(roots)
    while frontier:
        new = set()
        for b in frontier:
            bv = sp.Matrix(list(b))
            pair = A * bv
            for i in range(n):
                # root string: q = p - <b, a_i>; p = #{j>0: b - j a_i is a root}
                p = 0
                cur = list(b)
                while True:
                    cur = list(cur)
                    cur[i] -= 1
                    t = tuple(cur)
                    if all(c == 0 for c in t) or t in roots or \
                       tuple(-c for c in t) in roots:
                        if all(c == 0 for c in t):
                            break
                        if t in roots or tuple(-c for c in t) in roots:
                            p += 1
                    else:
                        break
                q = p - pair[i]
                if q > 0:
                    up = list(b)
                    up[i] += 1
                    t = tuple(up)
                    if t not in roots:
                        new.add(t)
        roots |= new
        frontier = new
    return sorted(roots, key=lambda t: (sum(t), t))


SYS = {}
for name, A in CARTAN.items():
    n = len(A)
    Am = sp.Matrix(A)
    pos = positive_roots(A)
    npos = len(pos)
    hts = [sum(r) for r in pos]
    hv = 1 + max(hts)                      # 1 + ht(theta), simply-laced
    dim = n + 2 * npos
    e = EXPECT[name]
    assert npos == e["npos"] and int(Am.det()) == e["det"] \
        and hv == e["hv"] and dim == e["dim"], (name, npos, Am.det(), hv, dim)
    # (rho, alpha) = ht(alpha) exactly: rho coords solve A rho = ones
    rho = Am.solve(sp.ones(n, 1))
    for r, h in zip(pos, hts):
        assert (rho.T * Am * sp.Matrix(list(r)))[0] == h
    # THE IDENTITY sum_{alpha>0} c_a c_a^T = h_vee * A^{-1}
    Ssum = sp.zeros(n, n)
    for r in pos:
        cv = sp.Matrix(list(r))
        Ssum += cv * cv.T
    assert sp.simplify(Ssum - hv * Am.inv()) == sp.zeros(n, n), name
    SYS[name] = dict(A=Am, n=n, pos=pos, hts=hts, hv=hv, dim=dim,
                     det=int(Am.det()), npos=npos)
    print(f"  {name}: |D+|={npos}, det A={int(Am.det())}, h_vee={hv}, "
          f"dim={dim}; (rho,alpha)=ht exact; "
          f"sum_a (mu,a)(nu,a) = h_vee (mu,nu) EXACT (matrix identity)")


def weyl_dim(name, labels):
    S = SYS[name]
    d = sp.Integer(1)
    for r, h in zip(S["pos"], S["hts"]):
        extra = sum(sp.Integer(l) * c for l, c in zip(labels, r))
        d *= sp.Rational(h + extra, h)
    return sp.nsimplify(d)


assert weyl_dim("A1", (1,)) == 2 and weyl_dim("A1", (2,)) == 3
assert weyl_dim("A2", (1, 0)) == 3 and weyl_dim("A2", (1, 1)) == 8
assert weyl_dim("E6", (1, 0, 0, 0, 0, 0)) == 27
assert weyl_dim("E6", (0, 1, 0, 0, 0, 0)) == 78
print("  Weyl dims verified: A1 fund=2; A2 fund=3, adj=8; E6 w1=27, adj=78")


def casimir(name, labels):
    """C2(lambda) = (lambda, lambda+2rho), (theta,theta)=2 normalization;
    exact rational: l^T A^{-1} l + 2 l^T A^{-1} ones."""
    S = SYS[name]
    l = sp.Matrix([sp.Integer(x) for x in labels])
    Ainv = S["A"].inv()
    return sp.nsimplify((l.T * Ainv * l)[0] +
                        2 * (l.T * Ainv * sp.ones(S["n"], 1))[0])


# anchor: banked su32_wrt header formula C2 = (2/3)(a^2+ab+b^2) + 2(a+b)
for (a, b) in [(1, 0), (1, 1), (2, 1)]:
    banked = sp.Rational(2, 3) * (a * a + a * b + b * b) + 2 * (a + b)
    assert casimir("A2", (a, b)) == banked, (a, b)
print("  C2 anchor: A2 Casimir == banked su32_wrt header formula (3 cases)")
c27, c78 = casimir("E6", (1, 0, 0, 0, 0, 0)), casimir("E6", (0, 1, 0, 0, 0, 0))
print(f"  C2(E6 27) = {c27} (exact), C2(E6 78) = {c78} = 2 h_vee "
      f"(adjoint check: {c78 == 24})")
assert c78 == 24


def S00(name, kappa):
    """KP: S00 = kappa^{-r/2} (det A)^{-1/2} prod_{a>0} 2 sin(pi ht(a)/kappa)."""
    S = SYS[name]
    v = mpf(kappa) ** (-mpf(S["n"]) / 2) / mp.sqrt(S["det"])
    for h in S["hts"]:
        v *= 2 * msin(MPPI * h / mpf(kappa))
    return v


# ---- anchors of the product formula ----
for k in (3, 10):
    kap = k + 2
    banked = mp.sqrt(mpf(2) / kap) * msin(MPPI / kap)
    assert abs(S00("A1", kap) - banked) < mpf(10) ** -35
print("  S00 anchor A1: == banked su2_data closed form sqrt(2/kap)sin(pi/kap)"
      " (k=3,10; 35 digits)")

# A2 anchor at k=2 vs the banked su3_data Weyl sum (exec'd from B238 source)
src = open(os.path.join(REPO, "frontier", "B238_su32_levelrank",
                        "su32_wrt.py")).read()
ns = {}
exec("import cmath\nimport itertools\nimport numpy as np\n" +
     src[src.index("def su3_data"):src.index("def su2_data")], ns)
_, S3, _, _ = ns["su3_data"](2)
# the banked Weyl sum carries the (-i)^{|D+|} phase: compare moduli
assert abs(S00("A2", 5) - abs(S3[0, 0])) < 1e-12
print(f"  S00 anchor A2: KP product {float(S00('A2', 5)):.12f} == banked "
      f"su3_data(2) Weyl sum |S[0,0]| {abs(S3[0, 0]):.12f} "
      f"(their S00 = +i * this, the (-i)^3 Weyl-denominator phase)")

# E6 anchor at k=2 vs a Weyl-sum S00 built by the banked B570 method
C6 = np.array(CARTAN["E6"], dtype=np.int64)
gens = []
for j in range(6):
    M = np.eye(6, dtype=np.int64)
    M[j, :] -= C6[:, j]
    gens.append(M)
I6 = np.eye(6, dtype=np.int64)
seen = {I6.tobytes(): 1}
frontier = [(I6, 1)]
mats, signs = [I6], [1]
while frontier:
    new = []
    for M, s in frontier:
        for g in gens:
            Mg = g @ M
            key = Mg.tobytes()
            if key not in seen:
                seen[key] = -s
                new.append((Mg, -s))
                mats.append(Mg)
                signs.append(-s)
    frontier = new
W = np.array(mats, dtype=float)
eps = np.array(signs, dtype=float)
assert len(W) == 51840
rho_c = np.linalg.solve(np.array(CARTAN["E6"], dtype=float), np.ones(6))
G = np.array(CARTAN["E6"], dtype=float)
KH = 14.0
ips = np.einsum('wij,j->wi', W, rho_c) @ (G @ rho_c)
Z = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
# normalized S00 = |Z| / sqrt(sum over the 9 primaries not needed): use the
# denominator-identity route instead: Z should equal (-i)^{|D+|}-phased
# product; compare |Z| * kappa^{-r/2} normalization directly:
S00_weyl = abs(Z) / (KH ** 3 * np.sqrt(3.0))
# |Z| = prod 2 sin(pi ht /kappa) * kappa^{r/2}*sqrt(det)*S00 => S00 formula:
assert abs(S00_weyl - float(S00("E6", 14))) < 1e-9, (S00_weyl,
                                                     float(S00("E6", 14)))
print(f"  S00 anchor E6: KP product {float(S00('E6', 14)):.12e} == Weyl-sum "
      f"|Z|/(kap^3 sqrt3) {S00_weyl:.12e}  (|W|=51840, banked B570 method)")

# ---- THE GROWTH EXPONENTS ----
print("\n  S00 growth exponent (slope of log S00 between kappa=1e3, 1e4):")
for name in ("A1", "A2", "E6"):
    s1, s2 = S00(name, 1000), S00(name, 10000)
    slope = (mlog(s2) - mlog(s1)) / (mlog(mpf(10000)) - mlog(mpf(1000)))
    tgt = -sp.Rational(SYS[name]["dim"], 2)
    print(f"    {name}: slope = {float(slope):+.6f}   target -dim/2 = "
          f"{float(tgt):+.1f}   |diff| = {abs(float(slope) - float(tgt)):.2e}")
    # the constant: S00 * kappa^{dim/2} -> (det A)^{-1/2} prod 2 pi ht
    C = mpf(1) / mp.sqrt(SYS[name]["det"])
    for h in SYS[name]["hts"]:
        C *= 2 * MPPI * h
    ratio = S00(name, 100000) * mpf(100000) ** (mpf(SYS[name]["dim"]) / 2) / C
    print(f"        constant check: S00*kap^(dim/2)/C_g at kap=1e5 = "
          f"{float(ratio):.9f} (-> 1)")

print("\n  fixed-rep quantum dimension: d(kappa) = dim*(1 - pi^2 h_vee C2 /"
      " (6 kappa^2) + O(kappa^-4))")


def qdim(name, labels, kappa):
    S = SYS[name]
    v = mpf(1)
    for r, h in zip(S["pos"], S["hts"]):
        extra = sum(l * c for l, c in zip(labels, r))
        v *= msin(MPPI * (h + extra) / mpf(kappa)) / msin(MPPI * h / mpf(kappa))
    return v


for name, labels in [("A1", (1,)), ("A1", (2,)), ("A2", (1, 0)),
                     ("A2", (1, 1)), ("E6", (1, 0, 0, 0, 0, 0)),
                     ("E6", (0, 1, 0, 0, 0, 0))]:
    dim = weyl_dim(name, labels)
    C2 = casimir(name, labels)
    hv = SYS[name]["hv"]
    pred = -sp.pi ** 2 * hv * C2 / 6
    k1, k2 = mpf(1000), mpf(2000)
    c1 = k1 ** 2 * (qdim(name, labels, k1) / mpf(int(dim)) - 1)
    c2_ = k2 ** 2 * (qdim(name, labels, k2) / mpf(int(dim)) - 1)
    rich = (4 * c2_ - c1) / 3                     # kills the kappa^-4 term
    predf = float(sp.N(pred, 30))
    print(f"    {name} {labels}: dim={dim}, C2={C2}; Richardson kappa^2 "
          f"coeff = {float(rich):+.8f} vs -pi^2 h C2/6 = {predf:+.8f}  "
          f"(rel err {abs((float(rich)-predf)/predf):.1e})")

print("\n  alcove-interior quantum dimension growth (lambda = s*rho, "
      "s = floor(kappa/(2(h_vee-1)))): slope -> |D+| = (dim-r)/2")
for name in ("A1", "A2", "E6"):
    S = SYS[name]
    vals = []
    for kap in (2000, 4000):
        s = kap // (2 * (S["hv"] - 1))
        v = qdim(name, tuple([s] * S["n"]), mpf(kap))
        vals.append((kap, v))
    slope = (mlog(vals[1][1]) - mlog(vals[0][1])) / \
            (mlog(mpf(vals[1][0])) - mlog(mpf(vals[0][0])))
    print(f"    {name}: slope = {float(slope):+.4f}   |D+| = {S['npos']}")

# S_{lm}/S00 -> dim*dim (A1 witness) and T-entry convergence (one line each)
kap = mpf(100000)
r = msin(MPPI * 4 / kap) / msin(MPPI * 1 / kap)
print(f"\n  fixed-label S-entry: S_11/S_00 (A1, kap=1e5) = {float(r):.6f} "
      f"-> dim*dim = 4; every fixed entry scales as kappa^(-dim g/2)")
print("  T-entries: h_l = C2/(2 kappa) -> 0, c -> dim g, both with "
      "CONVERGENT 1/kappa series => bounded oscillatory, no resurgent data")

print()
print("=" * 72)
print("PART B — the torsion towers (exact, vs cellB2's banked landscape)")
print("=" * 72)

LT = json.load(open(os.path.join(REPO, "frontier", "B666_leads_campaign",
                                 "cellB2", "landscape_table.json")))
TAU = LT["tau"]
EXPS = (1, 4, 5, 7, 8, 11)

# B1: the beta-product form  |tau_m(tr)| = prod_{j=1}^m (beta^j - beta^-j)^2
#     (exact, all 78 entries; equivalent to B617's closed form)
ok = 0
for tr in range(3, 16):
    s_rad = sp.sqrt(sp.Integer(tr) ** 2 - 4)
    beta = (sp.Integer(tr) + s_rad) / 2
    binv = (sp.Integer(tr) - s_rad) / 2
    for m in EXPS:
        p = sp.Integer(1)
        for j in range(1, m + 1):
            p = sp.expand(p * sp.expand((beta ** j - binv ** j) ** 2))
        banked = abs(sp.Integer(TAU[str(tr)][str(m)]))
        assert p == banked, (tr, m)
        ok += 1
print(f"  B1: |tau_m(tr)| == prod_(j=1..m) (beta^j - beta^-j)^2 EXACT at all "
      f"{ok}/78 banked entries")

# B2: the bigrowth law  log|tau_m| = m(m+1) log beta + 2 log (q;q)_m, q=b^-2
print("  B2: log|tau_m| - m(m+1) log beta - 2 log (q;q)_m == 0 (30-digit "
      "check, 6 spot entries):")
for (tr, m) in [(3, 1), (3, 11), (7, 5), (10, 8), (15, 4), (15, 11)]:
    b = (mpf(tr) + mp.sqrt(mpf(tr) ** 2 - 4)) / 2
    q = b ** -2
    lhs = mlog(mpf(int(abs(int(TAU[str(tr)][str(m)])))))
    poch = mpf(1)
    for j in range(1, m + 1):
        poch *= (1 - q ** j)
    resid = lhs - m * (m + 1) * mlog(b) - 2 * mlog(poch)
    assert abs(resid) < mpf(10) ** -28
    print(f"    tr={tr:2d} m={m:2d}: residual = {float(resid):.1e}")

# B3: m-direction — the (q;q)_infty limit and the epsilon_m envelope (tr=3)
b = (mpf(3) + mp.sqrt(mpf(5))) / 2
q = b ** -2
qq_inf = mpf(1)
for j in range(1, 400):
    qq_inf *= (1 - q ** j)
print(f"  B3: tr=3: q = beta^-2 = {float(q):.6f}, 2 log(q;q)_inf = "
      f"{float(2 * mlog(qq_inf)):.9f}")
print("      eps_m = 2 log[(q;q)_m/(q;q)_inf]  vs the envelope 3 q^(m+1):")
for m in EXPS:
    poch = mpf(1)
    for j in range(1, m + 1):
        poch *= (1 - q ** j)
    epsm = 2 * mlog(poch / qq_inf)
    env = 3 * q ** (m + 1)
    print(f"      m={m:2d}: eps_m = {float(epsm):+.3e}   3q^(m+1) = "
          f"{float(env):.3e}   inside: {abs(epsm) < env}")

# B4: tr-direction at fixed m — |tau_m(tr)|/tr^(m(m+1)) -> 1 (exact rationals)
print("  B4: |tau_m(tr)| / tr^(m(m+1)) at tr = 12..15 (m=4) and tr=15 (all m):")
for tr in (12, 13, 14, 15):
    v = sp.Rational(abs(sp.Integer(TAU[str(tr)]["4"])), sp.Integer(tr) ** 20)
    print(f"      m=4, tr={tr}: {float(v):.6f}")
for m in EXPS:
    v = sp.Rational(abs(sp.Integer(TAU["15"][str(m)])),
                    sp.Integer(15) ** (m * (m + 1)))
    print(f"      tr=15, m={m:2d}: {float(v):.6f}   (exponent m(m+1) = "
          f"{m * (m + 1)})")

print()
print("=" * 72)
print("PART C — class P (periodic) is cited from the banked record, no")
print("computation: melody theorem N0 (B651), exact minimal period")
print("P = 175560 = 2^3*3*5*7*11*19 (B662/G), word-universality (B669:")
print("finite exact q-support => exactly periodic, all four words).")
print("=" * 72)
print("\nasymptotics computations done — see ASYMPTOTICS_NOTE.md")
