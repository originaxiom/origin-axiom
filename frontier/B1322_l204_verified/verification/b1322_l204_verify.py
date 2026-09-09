"""B1322 -- L204 verified: main's own Fox calculus at the SM seat's banked points (sm:B1350 @ 7484ad01; DESIGN sealed before this ran).
Presentation (the seat's, B1267): <a, b | a w b^-1 w^-1>, w = b a^-1 b^-1 a; meridian a; longitude lambda = w w*, w* = a b^-1 a^-1 b.
Points: v10_direction_points.json -- per direction the 27 x 27 matrices of a ('1') and b ('2') at 100 digits."""
import sys, json, time
import mpmath as mp
mp.mp.dps = 110
PTS = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv) > 2 else "b1322_l204_verify.json"
W = [2, -1, -2, 1]; WSTAR = [1, -2, -1, 2]; REL = [1] + W + [-2] + [-x for x in reversed(W)]; LONG = W + WSTAR
def _parse_str(z):
    """the seat writes each entry as a pair [re, im] of decimal strings at 100 digits (or a single string)"""
    if isinstance(z, (list, tuple)) and len(z) == 2: return mp.mpc(mp.mpf(str(z[0]).strip()), mp.mpf(str(z[1]).strip()))
    s = str(z).strip().strip("()").replace(" ", "")
    if "j" not in s and "i" not in s: return mp.mpc(mp.mpf(s), 0)
    s = s.rstrip("ji"); k = max(s.rfind("+"), s.rfind("-"))
    if k <= 0: return mp.mpc(0, mp.mpf(s))
    return mp.mpc(mp.mpf(s[:k]), mp.mpf(s[k:]))
def load(entry):
    A = mp.matrix([[_parse_str(z) for z in row] for row in entry["1"]]); B = mp.matrix([[_parse_str(z) for z in row] for row in entry["2"]]); return A, B
def inv(M): return mp.inverse(M)
def ev(word, mats, invs):
    R = mp.eye(27)
    for g in word: R = R * (mats[abs(g)] if g > 0 else invs[abs(g)])
    return R
def fox(word, x, mats, invs):
    """left Fox derivative d(word)/dx evaluated in the representation"""
    D = mp.zeros(27); P = mp.eye(27)
    for g in word:
        if g == x: D += P
        if g == -x: D -= P * invs[x]
        P = P * (mats[abs(g)] if g > 0 else invs[abs(g)])
    return D
def rank_with_gap(M, tol=mp.mpf("1e-50")):
    """Gaussian elimination with full pivoting; pivots relative to the largest entry; rank = count above tol; returns rank, smallest accepted, largest rejected"""
    A = M.copy(); rows, cols = A.rows, A.cols; scale = max(abs(A[i, j]) for i in range(rows) for j in range(cols)) or mp.mpf(1); pivs = []
    r = 0
    for _ in range(min(rows, cols)):
        best, bi, bj = mp.mpf(0), None, None
        for i in range(r, rows):
            for j in range(cols):
                v = abs(A[i, j])
                if v > best: best, bi, bj = v, i, j
        if bi is None or best == 0: break
        pivs.append(best / scale)
        if bi != r:
            for j in range(cols): A[r, j], A[bi, j] = A[bi, j], A[r, j]
        for i in range(rows):
            if i != r and A[i, bj] != 0:
                f = A[i, bj] / A[r, bj]
                for j in range(cols): A[i, j] -= f * A[r, j]
        r += 1
    acc = [p for p in pivs if p > tol]; rej = [p for p in pivs if p <= tol]
    return len(acc), (min(acc) if acc else None), (max(rej) if rej else None)
def hstack(A, B):
    M = mp.zeros(A.rows, A.cols + B.cols)
    for i in range(A.rows):
        for j in range(A.cols): M[i, j] = A[i, j]
        for j in range(B.cols): M[i, A.cols + j] = B[i, j]
    return M
def vstack(A, B):
    M = mp.zeros(A.rows + B.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols): M[i, j] = A[i, j]
    for i in range(B.rows):
        for j in range(A.cols): M[A.rows + i, j] = B[i, j]
    return M
def frob(M): return mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))
def cohomology(mats, invs):
    """h0, h1 of the one-relator presentation with coefficients in the 27 given by mats; plus the cusp fixed space"""
    I = mp.eye(27); d0 = vstack(mats[1] - I, mats[2] - I)                      # 54 x 27
    d1 = hstack(fox(REL, 1, mats, invs), fox(REL, 2, mats, invs))              # 27 x 54
    r0, a0, j0 = rank_with_gap(d0); r1, a1, j1 = rank_with_gap(d1)
    h0 = 27 - r0; h1 = (54 - r1) - r0
    lam = ev(LONG, mats, invs); comm = frob(mats[1] * lam - lam * mats[1])
    rc, ac, jc = rank_with_gap(vstack(mats[1] - I, lam - I)); h0_cusp = 27 - rc
    return dict(h0=h0, h1=h1, h0_cusp=h0_cusp, rank_d0=r0, rank_d1=r1, gaps=dict(d0=(mp.nstr(a0, 3) if a0 is not None else None, mp.nstr(j0, 3) if j0 is not None else None), d1=(mp.nstr(a1, 3) if a1 is not None else None, mp.nstr(j1, 3) if j1 is not None else None), cusp=(mp.nstr(ac, 3) if ac is not None else None, mp.nstr(jc, 3) if jc is not None else None)), mu_lambda_commutator=str(mp.nstr(comm, 3)))
def dual(mats): return {k: mp.inverse(M).T for k, M in mats.items()}
def analyse(A, B, label):
    t0 = time.time(); mats = {1: A, 2: B}; invs = {1: inv(A), 2: inv(B)}
    rel = frob(ev(REL, mats, invs) - mp.eye(27))
    sd = max(abs(sum(ev([g], mats, invs)[i, i] for i in range(27)) - sum(ev([-g], mats, invs)[i, i] for i in range(27))) for g in (1, 2)) if True else None
    tr_ab = sum(ev([1, 2], mats, invs)[i, i] for i in range(27)); tr_ba_inv = sum(ev([-2, -1], mats, invs)[i, i] for i in range(27)); sd = max(sd, abs(tr_ab - tr_ba_inv))
    c27 = cohomology(mats, invs); dm = dual(mats); c27b = cohomology(dm, {k: inv(M) for k, M in dm.items()})
    N = c27["h1"] - c27b["h1"]
    res = dict(label=label, relator_residual=str(mp.nstr(rel, 3)), self_duality_defect=str(mp.nstr(sd, 3)), h1_27=c27["h1"], h1_27bar=c27b["h1"], h0_27=c27["h0"], h0_27bar=c27b["h0"],
               h0_cusp_27=c27["h0_cusp"], h0_cusp_27bar=c27b["h0_cusp"], N=N, bound=(-c27["h0_cusp"], c27b["h0_cusp"]), gaps27=c27["gaps"], gaps27bar=c27b["gaps"], mu_lambda=c27["mu_lambda_commutator"], seconds=round(time.time() - t0))
    print(f"  {label:<20} relator {res['relator_residual']:>8}  non-self-dual defect {res['self_duality_defect']:>8}  h1(27)={c27['h1']} h1(27bar)={c27b['h1']}  h0(dM;27)={c27['h0_cusp']} h0(dM;27bar)={c27b['h0_cusp']}  N={N}  bound {res['bound']}  d1 gap {c27['gaps']['d1']}  [{res['seconds']}s]", flush=True)
    return res
if __name__ == "__main__":
    pts = json.load(open(PTS)); out = dict(points=PTS, dps=110, results=[], controls={})
    for label, entry in pts.items():
        A, B = load(entry); out["results"].append(analyse(A, B, label))
    # control (ii): a perturbed point must fail the relator
    A, B = load(pts[list(pts)[0]]); A2 = A.copy(); A2[0, 0] += mp.mpf("1e-30"); rel = frob(ev(REL, {1: A2, 2: B}, {1: inv(A2), 2: inv(B)}) - mp.eye(27))
    out["controls"]["perturbed_relator_residual"] = str(mp.nstr(rel, 3)); print("  control: perturbed point relator residual", out["controls"]["perturbed_relator_residual"], "(must be >> 1e-60)")
    ok = all(r["h1_27"] == 0 and r["h1_27bar"] == 0 and r["h0_cusp_27"] == 0 and r["h0_cusp_27bar"] == 0 and r["N"] == 0 and mp.mpf(r["relator_residual"]) <= mp.mpf("1e-60") and mp.mpf(r["self_duality_defect"]) > mp.mpf("1e-12") for r in out["results"]) and mp.mpf(out["controls"]["perturbed_relator_residual"]) > mp.mpf("1e-40")
    out["verdict"] = "PASS" if ok else "FAIL"; json.dump(out, open(OUT, "w"), indent=1); print("B1322 L204 VERIFY:", out["verdict"])
