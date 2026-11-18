"""B1957: the physical lane's package 'input assessment recheck' (PHYSICAL-C6, 2026-11-17): its four hand checks of
another seat's cross-form and joining claims, rebuilt on main.  Nothing of any seat's is run.
 H0  custody (needs the seats' branches fetched): every file the package's receipt pins has the pinned sha256 at the
     pinned commit; and the lines of the other seat's scripts that the hand checks are about say what the package says
     (the new stage-four script carries -48 at lines 287 and 1006; the parabolic control's ratio at line 452; the
     second fundamental form as a projected raw derivative at lines 618 to 620).
 H1  E + f T on the five of weights 2, 1, 0, -1, -2 (E with four non-zero entries above the diagonal, T with entries at
     (3, 0) and (4, 1)): the minor on rows 0..3 and columns 1..4 is c0 c1 c2 c3, and the determinant vanishes for every
     f, so the kernel is a line for every f; and ker(Q+ x 1) meets ker(1 x Q-) in ker Q+ x ker Q-.
 H2  the frame-change control: on C^2 with U(1) acting by phase, X(s) = exp(i beta s)(1, s) has horizontal tangent
     v = exp(i beta s)(0, 1); the projected raw derivative of v at 0 is beta (0, i), and the covariant one is zero.
 H3  the planar example: with q_s = 2[(1 - s) e1 + s(a e1 + b e2)], r_s = (1 - s) e1 - s(a e1 + b e2), a^2 + b^2 = 1:
     |t|^2 = d = 10 - 6a, D = |X|^2 = 5 - d s(1 - s), N = <JX, t> = 3b, |v|^2 = d - N^2/D, <X, v> = D'/2,
     |P_h Jv|^2 = 16/D, and the missing term's squared norm is 144 b^2/D^3.
 H4  the parabola y = c u(1 - u): its induced metric is 1 + c^2 (1 - 2u)^2, so its tension carries
     2 sqrt(b) int u(1 - u) sqrt(1 + c^2 (1 - 2u)^2) du, more than sqrt(b)/3 for c not 0.
 H5  two cells: M = [[D, 0], [0, D2], [k, -k L]] with D2 = U D U^dagger-type rotation of the second cell.  With the link
     fixed at L = 1 the kernel is ker D meet U ker D; with the link transported, L = U^dagger, it is ker D again."""
import functools, itertools, json, subprocess, hashlib
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    LANE = "8d5c91032"; show = lambda c, pth: subprocess.run(["git", "show", "%s:%s" % (c, pth)], capture_output=True).stdout
    raw = show(LANE, "reports/physical_bridge_2026_09_05/input_assessment_recheck_2026_11_17/RECEIPT.json")
    if raw:
        d = json.loads(raw); items = [it for k in ("new_upstream_artifacts", "guard_sources", "canonical_sources") for it in d[k]]
        ok = sum(hashlib.sha256(show(it["commit"], it["path"])).hexdigest() == it["sha256"] for it in items)
        s4 = show("80fdd90b2", "relays/x_synthesis_4_verify/verify_x_synthesis_4.py").decode().split("\n"); s2 = show("80fdd90b2", "relays/x_synthesis_2_verify/verify_x_synthesis_2.py").decode().split("\n")
        print("H0: pinned files with the pinned sha256: %d of %d; -48 at lines 287 and 1006 of the stage-four script: %s; the ratio sqrt(b)/sqrt(b + c^2) at line 452 of the stage-two script: %s; a projected raw derivative at lines 618 to 620: %s" % (
            ok, len(items), all("48" in s4[i - 1] and "y2_tr" in s4[i - 1] for i in (287, 1006)), "math.sqrt(b_cmp) / math.sqrt(b_cmp + c_cmp * c_cmp)" in s2[451], "dvs_ds = (vs_p - vs_m) / (2 * hs)" in s2[618] and "proj_perp_horiz(dvs_ds" in s2[619]))
    else: print("H0: the lane's branch is not fetched here; custody not checked")
    c0, c1, c2, c3, t0, t1, f = sp.symbols("c0 c1 c2 c3 t0 t1 f"); Q = sp.zeros(5, 5)
    for i, c in enumerate((c0, c1, c2, c3)): Q[i, i + 1] = c
    Q[3, 0] = f * t0; Q[4, 1] = f * t1
    minor = Q[0:4, 1:5].det(); rng = np.random.default_rng(48); ks = []
    for _ in range(4):
        vals = {s: complex(rng.normal(), rng.normal()) for s in (c0, c1, c2, c3, t0, t1, f)}; ks.append(int(5 - np.linalg.matrix_rank(np.array(Q.subs(vals).evalf(), dtype=complex))))
    A = rng.normal(size=(5, 5)); A[:, 0] = 0; Bm = rng.normal(size=(5, 5)); Bm[:, 1] = Bm[:, 0]            # two matrices with one-dimensional kernels
    kA = 5 - np.linalg.matrix_rank(A); kB = 5 - np.linalg.matrix_rank(Bm); joint = 25 - np.linalg.matrix_rank(np.vstack([np.kron(A, np.eye(5)), np.kron(np.eye(5), Bm)]))
    print("H1: the minor on rows 0..3, columns 1..4: %s; det(E + f T) = %s; kernel dimensions at four random points: %s; kernels of dimension %d and %d give a joint kernel of dimension %d" % (minor, sp.factor(Q.det()), ks, kA, kB, joint))
    s, beta = sp.symbols("s beta", real=True); X = sp.Matrix([sp.exp(sp.I * beta * s), sp.exp(sp.I * beta * s) * s]); dX = X.diff(s); rip = lambda u, w: sp.re(sum(sp.conjugate(a) * b for a, b in zip(u, w)))
    al = sp.simplify(rip(sp.I * X, dX) / rip(X, X)); v = sp.simplify(dX - al * sp.I * X); dv0 = v.diff(s).subs(s, 0); cov0 = sp.simplify((v.diff(s) - sp.I * al * v).subs(s, 0))
    vert = sp.Matrix([sp.I, 0]); tang = sp.Matrix([0, 1]); perp = sp.simplify(dv0 - rip(vert, dv0) * vert - rip(tang, dv0) * tang)
    print("H2: alpha = %s; v = %s; the projected raw derivative at 0: %s; the covariant derivative at 0: %s" % (sp.simplify(al), list(sp.simplify(v)), list(perp), list(cov0)))
    a, b = sp.symbols("a b", real=True); e1 = sp.Matrix([1, 0]); e2 = sp.Matrix([0, 1]); w = a * e1 + b * e2
    q = 2 * ((1 - s) * e1 + s * w); r = (1 - s) * e1 - s * w; J = sp.Matrix([[0, -1], [1, 0]]); dot = lambda u, v2: (u.T * v2)[0]
    red = lambda ex: sp.simplify(sp.expand(ex).subs(b ** 2, 1 - a ** 2))
    tq, tr = q.diff(s), r.diff(s); d = red(dot(tq, tq) + dot(tr, tr)); D = red(dot(q, q) + dot(r, r)); N = red(dot(J * q, tq) + dot(J * r, tr)); alpha = N / D
    vq, vr = tq - alpha * J * q, tr - alpha * J * r; v2 = sp.simplify(red(sp.together(dot(vq, vq) + dot(vr, vr)) * D) / D); Xv = sp.simplify(red(sp.together(dot(q, vq) + dot(r, vr)) * D) / D)
    Jv_sq = sp.simplify(v2 - Xv ** 2 / D); dd = 10 - 6 * a
    chk = [sp.simplify(d - dd), sp.simplify(D - (5 - dd * s * (1 - s))), sp.simplify(sp.expand(N ** 2 - 9 * b ** 2).subs(b ** 2, 1 - a ** 2)), sp.simplify(sp.expand((v2 - (dd - 9 * (1 - a ** 2) / D)) * D)), sp.simplify(Xv - sp.diff(D, s) / 2), sp.simplify(sp.expand((Jv_sq - 16 / D) * D ** 2).subs(b ** 2, 1 - a ** 2))]
    print("H3: differences from the note's d, D, N^2, |v|^2, <X, v> and |P_h Jv|^2 = 16/D: %s; so the missing term is alpha^2 times 16/D = 144 b^2/D^3; N = %s" % (chk, sp.factor(N)))
    u, c, bb = sp.symbols("u c b0", positive=True); Kc = sp.simplify(1 + sp.diff(c * u * (1 - u), u) ** 2); num = [float(sp.Integral(2 * u * (1 - u) * sp.sqrt(1 + cv ** 2 * (1 - 2 * u) ** 2), (u, 0, 1)).evalf()) for cv in (0, 1, 3)]
    print("H4: the induced metric on the parabola: %s; 2 int u(1 - u) sqrt(K) du at c = 0, 1, 3: %s (1/3 at c = 0)" % (sp.expand(Kc), [round(x, 5) for x in num]))
    n, m = 6, 8; Dm = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n)); k0 = rng.normal(size=n) + 1j * rng.normal(size=n); Dm = Dm - np.outer(Dm @ k0, k0.conj()) / (k0.conj() @ k0)        # D with the kernel line k0
    Uq = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))[0]; Wq = np.linalg.qr(rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m)))[0]; D2 = Wq @ Dm @ Uq.conj().T; kap = 0.5
    def nullity(Lk): return 2 * n - np.linalg.matrix_rank(np.vstack([np.hstack([Dm, np.zeros((m, n))]), np.hstack([np.zeros((m, n)), D2]), np.hstack([kap * np.eye(n), -kap * Lk])]), tol=1e-9)
    same = 2 * n - np.linalg.matrix_rank(np.vstack([np.hstack([Dm, np.zeros((m, n))]), np.hstack([np.zeros((m, n)), Dm]), np.hstack([kap * np.eye(n), -kap * np.eye(n)])]), tol=1e-9)
    print("H5: kernel of D: %d; the same-axis two-cell operator: %d; the second cell rotated with the link fixed at 1: %d; with the link transported (L = U^dagger): %d" % (n - np.linalg.matrix_rank(Dm, tol=1e-9), same, nullity(np.eye(n)), nullity(Uq.conj().T)))
