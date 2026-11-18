"""B1957: the left unitaries of B1953's covariance law, read out (the web seat's section 13.2, item 3; 2026-11-18).  Main's own
code only: B1953's weyl_operator.py fits Y(g tau, w) = c phi U_L Y(tau, w g) U_R^dagger for g = T and S at the 24 points.  It
did not print U_L's form.  Here, for the down and up sectors, both readings and both base points: |U_L(T)| and |U_L(S)| as
permutations of the three blocks; the projective orders of U_L(T), U_L(S) and their product; the order of the group they
generate up to phases; whether U_L(T) is a real signed permutation up to one phase; and U_L against U_R.
The web seat's note W-A2 states these (its lines 110 to 116 and 187) as its referee's algebra, not computed on the frame."""
import sys, itertools, pathlib, numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1953_*")) / "verification")); import weyl_operator as WO
def proj_order(U, nmax=24):
    P = np.eye(3, dtype=complex)
    for n in range(1, nmax + 1):
        P = P @ U
        d = P / P[np.unravel_index(np.argmax(abs(P)), P.shape)]
        if np.abs(d - np.diag(np.diag(d))).max() < 1e-8 and np.abs(np.abs(np.diag(d)) - 1).max() < 1e-8 and np.abs(np.diag(d) - d[0, 0]).max() < 1e-8: return n
    return None
def group_order(gens):
    key = lambda M: tuple(np.round(M / (M.flat[np.flatnonzero(abs(M) > 1e-6)[0]] / abs(M.flat[np.flatnonzero(abs(M) > 1e-6)[0]])), 5).flatten().tolist())
    seen = {key(np.eye(3, dtype=complex)): np.eye(3, dtype=complex)}; todo = [np.eye(3, dtype=complex)]
    while todo and len(seen) < 500:
        g = todo.pop()
        for h in gens:
            n = g @ h; k = key(n)
            if k not in seen: seen[k] = n; todo.append(n)
    return len(seen)
rows = []
for (tx, ty) in WO.BASES:
    for sec in ("down", "up"):
        Ys, _ = WO.images(tx, ty, sec)
        for rd in ("S", "St"):
            lt, ls = WO.law(Ys["t"][rd], Ys["T"][rd], "T"), WO.law(Ys["t"][rd], Ys["S"][rd], "S")
            UT, US = lt["UL"], ls["UL"]; A = np.abs(UT).round(3); B = np.abs(US).round(3)
            perm = lambda M: all(sorted(r) == [0, 0, 1] for r in M.tolist()) and all(sorted(c) == [0, 0, 1] for c in M.T.tolist())
            ph = UT[np.abs(UT) > 0.5]; real_signed = np.abs((ph / ph[0]).imag).max() < 1e-8        # up to one phase, the entries are +-1
            lr = lambda l: min(np.abs(l["UL"] - c * l["UR"]).max() for c in [np.vdot(l["UR"].flatten(), l["UL"].flatten()) / 3])
            rows.append((tx, sec, rd, max(lt["residual"], ls["residual"]), perm(A), perm(B), [int(np.argmax(r)) for r in A], [int(np.argmax(r)) for r in B], proj_order(UT), proj_order(US), proj_order(US @ UT), group_order([UT, US]), bool(real_signed), max(lr(lt), lr(ls))))
for r in rows: print("base %s %-4s %-2s: law residual %.1e; |U_L(T)|, |U_L(S)| permutations: %s, %s (rows -> columns %s, %s); projective orders of T, S, ST: %s, %s, %s; group generated, up to phases: %d; U_L(T) real signed up to one phase: %s; |U_L - c U_R| at most %.1e" % r)
print("all eight cases: orders (4, 2, 3): %s; group order 24: %s" % (all(r[8:11] == (4, 2, 3) for r in rows), all(r[11] == 24 for r in rows)))
