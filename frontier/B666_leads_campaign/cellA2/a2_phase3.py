"""B666 CELL A' — phase 3: the 78-valued cup H^1(27) x H^1(27bar) ->
H^2(D;78), fully exact (312 x 312 Fox membership over K = Q(sqrt-3)),
plus the final assembly of the cell verdict.

The 27bar slot basis = the five greedy H^1(D;27bar) classes (cellH
convention).  Both slot orders are computed; the Koszul relation
[u cup zbar] = -[zbar cup u] is gated by membership of the sums.
NONZ verdicts get exact left-functional certificates; ZERO verdicts are
exact coboundary-solves (Solver).  Assembly: reads phase2_results.json
+ ckpt_phase1.json, runs the candidate analysis (slot symmetry,
eigenvalue structure, sigma*-behavior, field of definition) and writes
a2_results.json.
"""
import os
import sys
import json
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from a2_common import load, log, kser   # noqa: E402

n = load(run_g0=False, need_bar=True)
K, K0, K1 = n.K, n.K0, n.K1
kde = n.kde

log("loading checkpoints...")
with open(os.path.join(HERE, "ckpt_phase1.json")) as fh:
    ck = json.load(fh)
with open(os.path.join(HERE, "phase2_results.json")) as fh:
    p2 = json.load(fh)


def devec(v):
    return [kde(t) for t in v]


AD = {ch: [devec(row) for row in ck["AD"][ch]] for ch in "abcdABCD"}
E78 = {}
for kstr, v in ck["E_78"].items():
    o, a, b = kstr.split(",")
    E78[(o, int(a), int(b))] = devec(v)

# Ad word cache + relator gate
ADC = {"": [[K1 if i == j else K0 for j in range(78)] for i in range(78)]}


def adw(w):
    w = n.freduce(w)
    if w not in ADC:
        ADC[w] = n.mmul(adw(w[:-1]), AD[w[-1]])
    return ADC[w]


for w in n.RELATORS:
    Mw = adw(w)
    assert all((Mw[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(78) for j in range(78)), "Ad relator gate"
log("Ad(relator) = I at 78 re-verified (4 relators)")

# ---------------------------------------------------------------------------
log("Fox map at 78 (L78[r][g], exact) + membership solver...")
L78 = []
for r in range(4):
    Lr = {}
    for g in "abcd":
        M = [[K0] * 78 for _ in range(78)]
        for (w, sgn) in n.POSLIST[r][g]:
            Aw = adw(w)
            for i in range(78):
                Mi, Ai = M[i], Aw[i]
                for j in range(78):
                    if not Ai[j].is_zero():
                        Mi[j] = (Mi[j] + Ai[j]) if sgn > 0 \
                            else (Mi[j] - Ai[j])
        Lr[g] = M
    L78.append(Lr)

cols78 = []
for gi, g in enumerate("abcd"):
    for j in range(78):
        col = []
        for r in range(4):
            col.extend([L78[r][g][i][j] for i in range(78)])
        cols78.append(col)
SOLV78 = n.Solver(cols78)
log("312 x 312 Fox solver ready (exact rref)")

# left-null functionals (exact): nullspace of PHI^T
lnull = n.nullspace([col[:] for col in cols78])
h2_78 = len(lnull)
log(f"coker dim = h^2(2-complex; 78) = {h2_78} (exact)")

# CONTROL: left-null really annihilates a random Fox image
xi = [K((7 * t + 1) % 5 - 2, (3 * t + 2) % 3 - 1) for t in range(78)]
fg = {g: [xv - x2 for xv, x2 in zip(n.applyg(adw(g), xi), xi)]
      for g in "abcd"}
img = []
for r in range(4):
    acc = [K0] * 78
    for g in "abcd":
        v = n.applyg(L78[r][g], fg[g])
        acc = [acc[t] + v[t] for t in range(78)]
    img.extend(acc)
SOLV78.coords(img)          # must be solvable (it IS a Fox image)
for y in lnull[:5]:
    s = sum((y[t] * img[t] for t in range(312)
             if not img[t].is_zero()), K0)
    assert s.is_zero(), "left-null does not annihilate a Fox image"
log("CONTROL PASS: Fox image solvable + annihilated by the left-null")

# ---------------------------------------------------------------------------
log("78-cup class tables (both orders) + Koszul gate...")
T78 = {}
for key, E in E78.items():
    try:
        SOLV78.coords(E)
        T78[key] = "ZERO"
    except ValueError:
        wit = None
        for yi, y in enumerate(lnull):
            s = sum((y[t] * E[t] for t in range(312)
                     if not E[t].is_zero()), K0)
            if not s.is_zero():
                wit = (yi, str(s))
                break
        assert wit is not None, f"NONZ without left-null witness at {key}"
        T78[key] = "NONZ"
for order, label in (("ub", "u_i cup zbar_t"), ("bu", "zbar_t cup u_i")):
    log(f"  [{label}] class table (rows = first slot):")
    for a in range(5):
        row = [T78[(order, a, b)] for b in range(5)]
        log("    " + " ".join(f"{v:5s}" for v in row))
kosz_ok = True
for i in range(5):
    for t in range(5):
        Es = [E78[("ub", i, t)][r] + E78[("bu", t, i)][r]
              for r in range(312)]
        try:
            SOLV78.coords(Es)
        except ValueError:
            kosz_ok = False
            log(f"  KOSZUL VIOLATION at (u_{i}, zbar_{t})")
log(f"  Koszul gate [u cup zbar] = -[zbar cup u] (all 25): "
    f"{'PASS' if kosz_ok else 'FAIL'}")
assert kosz_ok

# ---------------------------------------------------------------------------
log("ASSEMBLY: the cell verdict...")
cert = p2["certified"]


def getcert(kind, fam, i, j):
    return cert.get(str((kind, fam, "pair", i, j)), "MISSING")


SOLO = (2, 3, 4)
lam_solo = {(i, j): getcert("lam", "lam", i, j) for i in SOLO for j in SOLO}
pw_solo = {(i, j): getcert("sym", "pw", i, j) for i in SOLO for j in SOLO}
lam_full = {(i, j): getcert("lam", "lam", i, j)
            for i in range(5) for j in range(5)}
pw_full = {(i, j): getcert("sym", "pw", i, j)
           for i in range(5) for j in range(5)}
t78_solo_rel = {(i, t): T78[("ub", i, t)] for i in SOLO for t in range(5)}

any_lam_solo = any(v.startswith("NONZ") for v in lam_solo.values())
any_pw_solo = any(v.startswith("NONZ") for v in pw_solo.values())
any_78 = any(v == "NONZ" for v in T78.values())

symdiff = {(i, j): cert.get(str(("lam", "lam", "symdiff", i, j)), "MISSING")
           for i in range(5) for j in range(5) if i < j}
log(f"Lambda-cup slot symmetry ([c_ij] = [c_ji]) certificates: "
    + ", ".join(f"({i},{j})={v}" for (i, j), v in symdiff.items()))
slot_symmetric = all(v.startswith("ZERO") for v in symdiff.values())

analysis = {}
if any_lam_solo:
    log("THE Lambda-solo block is NONZERO: candidate analysis...")
    import sympy as sp
    r3 = sp.sqrt(3) * sp.I

    def tosp(x):
        return sp.Rational(x.a) + sp.Rational(x.b) * r3

    med = {name: {k: kde(v) for k, v in tab.items()}
           for name, tab in ck["mediated"].items()
           if name.startswith("lam_")}
    ys = {kk: devec(v) for kk, v in p2.get("y_exact", {}).items()
          if kk.startswith("lam:")}
    E_LAM = {tuple(map(int, k.split(","))): devec(v)
             for k, v in ck["E_LAM"].items()}

    def solo_matrix_from_scalar(fn):
        return [[fn(i, j) for j in SOLO] for i in SOLO]

    mats = {}
    for name, tab in med.items():
        mats["mediated:" + name] = solo_matrix_from_scalar(
            lambda i, j: tab[str((i, j))])
    for kk, y in ys.items():
        mats["yfunc:" + kk] = solo_matrix_from_scalar(
            lambda i, j: sum((y[r] * E_LAM[(i, j)][r] for r in range(1404)
                              if not E_LAM[(i, j)][r].is_zero()), K0))
    for name, M in mats.items():
        Msp = sp.Matrix([[tosp(x) for x in row] for row in M])
        sym_ = all((M[a][b] - M[b][a]).is_zero()
                   for a in range(3) for b in range(3))
        cp = sp.expand(Msp.charpoly().as_expr())
        ev = Msp.eigenvals()
        rk = Msp.rank()
        ratl = all(x.b == 0 for row in M for x in row)
        log(f"  scalarized solo 3x3 [{name}]:")
        for row in M:
            log("    [" + ", ".join(str(x) for x in row) + "]")
        log(f"    symmetric: {sym_}; rank: {rk}; rational entries: {ratl}")
        log(f"    charpoly: {cp}")
        log(f"    eigenvalues: {ev}")
        analysis[name] = {
            "matrix": [[kser(x) for x in row] for row in M],
            "symmetric": sym_, "rank": int(rk),
            "rational": ratl, "charpoly": str(cp),
            "eigenvalues": {str(k): int(v) for k, v in ev.items()},
            "n_distinct_eigenvalues": len(ev),
        }
    # sigma*-behavior (exploratory characterization): full 5x5 mediated
    sig_path = os.path.join(HERE, "..", "..", "B662_successor_campaign",
                            "cellC", "sigma_matrix_golden.json")
    try:
        with open(sig_path) as fh:
            sig = json.load(fh)
        SG = [[K(Fr(e[0]), Fr(e[1])) for e in row]
              for row in sig["matrix"]]
        for name, tab in med.items():
            M5 = [[tab[str((i, j))] for j in range(5)] for i in range(5)]
            # sigma* antilinear: candidate relation
            #   M'[i][j] = sum_kl SG[i][k] SG[j][l] conj(M[k][l])
            Mc = [[K(x.a, -x.b) for x in row] for row in M5]
            MT = [[sum((SG[i][k] * SG[j][l] * Mc[k][l]
                        for k in range(5) for l in range(5)
                        if not (SG[i][k].is_zero() or SG[j][l].is_zero()
                                or Mc[k][l].is_zero())), K0)
                   for j in range(5)] for i in range(5)]
            same = all((MT[i][j] - M5[i][j]).is_zero()
                       for i in range(5) for j in range(5))
            neg = all((MT[i][j] + M5[i][j]).is_zero()
                      for i in range(5) for j in range(5))
            log(f"  sigma*-transform of [{name}]: "
                f"Sig conj(M) Sig^T == M: {same}; == -M: {neg}")
            analysis[name + ":sigma"] = {"equal": same, "minus": neg}
    except FileNotFoundError:
        log("  (sigma matrix json not found; sigma*-behavior skipped)")
else:
    log("the Lambda-solo block is entirely ZERO")

verdict_bits = []
verdict_bits.append(
    ("Lambda^2(27)=351 cup, solo block {2,3,4}: "
     + ("NONZERO (slot-symmetric candidate EXISTS)" if any_lam_solo
        else "all ZERO")))
verdict_bits.append(
    "351' cup, solo block: " + ("NONZERO" if any_pw_solo else "all ZERO"))
verdict_bits.append(
    "78 cup (27 x 27bar), all 25 pairs: "
    + ("some NONZERO" if any_78 else "all ZERO"))
verdict_bits.append(
    "Lambda slot symmetry [c_ij]=[c_ji]: "
    + ("CERTIFIED" if slot_symmetric else "VIOLATED/UNCERTIFIED"))
VERDICT = " | ".join(verdict_bits)
log("VERDICT: " + VERDICT)

res = {
    "cell": "B666 cell A' (cellA2): the uncomputed cups",
    "verdict": VERDICT,
    "lambda_table_certified": {f"{i},{j}": lam_full[(i, j)]
                               for i in range(5) for j in range(5)},
    "pw351p_table_certified": {f"{i},{j}": pw_full[(i, j)]
                               for i in range(5) for j in range(5)},
    "sym_full_table_certified": {
        f"{i},{j}": getcert("sym", "sym", i, j)
        for i in range(5) for j in range(5)},
    "t78_tables": {f"{k[0]},{k[1]},{k[2]}": v for k, v in T78.items()},
    "h2_78_2complex": h2_78,
    "coker_dims_discovery": p2["coker_dims_discovery"],
    "slot_symmetry_lambda": {f"{i},{j}": v
                             for (i, j), v in symdiff.items()},
    "koszul_78_gate": kosz_ok,
    "h0_dims": ck["h0_dims"],
    "fun_dims": ck["fun_dims"],
    "candidate_analysis": analysis,
    "primes_used": p2["primes_used"],
}
with open(os.path.join(HERE, "a2_results.json"), "w") as fh:
    json.dump(res, fh, indent=1)
log("a2_results.json written")
log("PHASE 3 COMPLETE")
