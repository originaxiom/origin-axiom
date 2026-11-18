"""B1957: the physical lane's package 'all seats dependency plan' (2026-11-17): the mathematics of its findings MAIN-01
and XF-01 to XF-06 and of its conditional projection, on main.  Nothing of any seat's is run.
 D0  custody (needs the seats' branches fetched): its 21 excerpts are in files with the pinned sha256, at the pinned lines.
 D1  MAIN-01, a fault in main's own B1953: for D(a, b) = zeta^(3ab) X^a Z^b on C^5 and the parity P, tr D = 0 and
     tr(D P) = 1 for all 24 non-zero (a, b); so the trace over the 3 is 1/2 and over the 2 is -1/2, not 1 and -1.
 D2  the projection to operators commuting with the gauge group: (F/6) on the 3 and -(F/4) on the 2 is -(F/12) times
     6Y = diag(-2, -2, -2, 3, 3); the lane's own preserved draft had twice that.
 D3  XF-05: log(v/M) = -a Vol + log c is solved by c = (v/M) exp(a Vol) for every v/M, so it removes no input while c is
     free.  XF-06: V = lambda(log phi) phi^4/4 is stationary where 4 lambda + beta = 0, not where lambda = 0.
 D4  XF-01: a first-order operator with zero values at both ends of an interval (an n x (n - 1) matrix) has kernel 0 and
     its adjoint (the transpose) kernel 1; a second matrix of the same shape with the derivative's sign reversed is not
     that adjoint and has kernel 0 too.
 D5  END-01, main's own canon(): the nearest value is returned where linear interpolation is not finite, and the only
     flag tests the upper edge (read in main's file; register row P-864)."""
import functools, itertools, json, subprocess, hashlib, pathlib, cmath
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)
LANE = "8d5c91032"; DIR = "reports/physical_bridge_2026_09_05/all_seats_dependency_plan_2026_11_17/"

if __name__ == "__main__":
    show = lambda c, pth: subprocess.run(["git", "show", "%s:%s" % (c, pth)], capture_output=True).stdout
    raw = show(LANE, DIR + "QUOTATIONS.json")
    if raw:
        ok = 0; ex = json.loads(raw)["excerpts"]
        for it in ex:
            b = show(it["head"], it["path"]); lines = b.decode("utf-8", "replace").split("\n"); lit = it["literal_excerpt"] if isinstance(it["literal_excerpt"], str) else "\n".join(it["literal_excerpt"])
            ok += bool(b) and hashlib.sha256(b).hexdigest() == it["source_sha256"] and "\n".join(lines[it["start"] - 1:it["end"]]).strip() == lit.strip()
        print("D0: excerpts held by hash and line range: %d of %d" % (ok, len(ex)))
    else: print("D0: the lane's branch is not fetched here; custody not checked")
    z = cmath.exp(2j * cmath.pi / 5); X = np.roll(np.eye(5), 1, axis=0); Z = np.diag([z ** k for k in range(5)]); P = np.zeros((5, 5)); P[(-np.arange(5)) % 5, np.arange(5)] = 1
    P3, P2 = (np.eye(5) + P) / 2, (np.eye(5) - P) / 2; worst = [0, 0, 0, 0]
    for a, b in itertools.product(range(5), repeat=2):
        if (a, b) == (0, 0): continue
        D = z ** (3 * a * b) * np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b)
        for i, (val, want) in enumerate(((np.trace(D), 0), (np.trace(D @ P), 1), (np.trace(D @ P3), 0.5), (np.trace(D @ P2), -0.5))): worst[i] = max(worst[i], abs(val - want))
    print("D1: over the 24 operators, the largest distances of tr D, tr(D P), tr over the 3 and tr over the 2 from 0, 1, 1/2, -1/2: %s; the ranks of the two projectors: %d, %d" % (["%.1e" % w for w in worst], round(np.trace(P3).real), round(np.trace(P2).real)))
    F = sp.symbols("F"); Y6 = sp.diag(-2, -2, -2, 3, 3); proj = sp.diag(F / 6, F / 6, F / 6, -F / 4, -F / 4)
    print("D2: the projection minus -(F/12) 6Y: %s; minus the preserved draft's -(F/6) 6Y: %s" % (all(sp.simplify(e) == 0 for e in (proj + F / 12 * Y6)), all(sp.simplify(e) == 0 for e in (proj + F / 6 * Y6))))
    v, a_, Vol, c = sp.symbols("v a Vol c", positive=True); sol = sp.solve(sp.Eq(sp.log(v), -a_ * Vol + sp.log(c)), c)
    phi = sp.symbols("phi", positive=True); lam = sp.Function("lam"); Vp = sp.simplify(sp.diff(lam(sp.log(phi)) * phi ** 4 / 4, phi) / phi ** 3)
    print("D3: c = %s for every v/M (written v here); V'(phi)/phi^3 = %s, zero where 4 lambda + beta = 0" % (sol, Vp))
    n = 12; h = 1.0 / n; mass = np.tanh(np.linspace(-3, 3, n))
    def op(sign):
        A = np.zeros((n, n - 1))
        for j in range(n - 1): A[j, j] += sign / h; A[j + 1, j] -= sign / h; A[j, j] += mass[j] / 2; A[j + 1, j] += mass[j + 1] / 2
        return A
    Dp, Dm = op(1.0), op(-1.0); nul = lambda A: A.shape[1] - np.linalg.matrix_rank(A)
    print("D4: the %d x %d operator: kernel %d; its transpose: kernel %d; the same shape with the sign reversed: kernel %d, and it has the adjoint's shape: %s" % (n, n - 1, nul(Dp), nul(Dp.T), nul(Dm), Dm.shape == Dp.T.shape))
    root = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()) if "__file__" in globals() else None
    src = next((root / "frontier").glob("B1927_*")) / "verification" / "canon_readout.py"; body = src.read_text().split("def canon(")[1].split("\ndef ")[0]
    print("D5: main's canon(): a nearest-value fallback is present: %s; a flag for the upper edge: %s; a flag for the lower edge or the hull: %s" % ("near(" in body and "isfinite" in body, "y > YMAX" in body, "YMIN" in body or "hull" in body.lower()))
