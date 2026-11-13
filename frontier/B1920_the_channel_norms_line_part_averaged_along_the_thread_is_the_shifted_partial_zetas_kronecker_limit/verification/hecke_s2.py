"""Main's own check, behind the SM seat, of SM-C7's step 2 conventions: Hecke's formula at s = 2, both sides by main's code.

    integral over one period of E_c(z, s) ds  =  H(s) * Z_tot(s, chi),   H(s) = 2^(-s) sqrt(pi) Gamma(s/2) / Gamma((s+1)/2)

E_c(z, s) = sum' e(c . (m, n)) y^s |m z + n|^(-2s) (the v-twisted series, (m, n) = v), chi(v) = e((i v0 + j v1)/N),
c = (i, j)/N; Z_tot(s, chi) = sum over v in (Z^2 - 0)/<M> of chi(v) |Q(v)|^(-s), Q(v) = (b v1^2 + (a - d) v0 v1 - c v0^2)/sqrt(D).
At s = 2 both sides converge absolutely. Left: the lattice sum at Gauss-Legendre nodes of one period of the geodesic of
gamma = M^T (|m| <= Mmax, the inner sum over n to |n| <= Nmax). Right: orbit representatives in the fundamental strip
0 <= log|alpha/beta| < 2 log lambda of each sign quadrant (v = alpha r1 + beta r2, r1, r2 M's eigenvectors), every lattice
point with |Q| <= X, and the tail estimated by the next cutoff. Main's code; nothing of the seat's is read or run."""
import math, cmath, sys, io, contextlib, pathlib, json
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1737_the_slope_is_a_zeta_value" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import the_slope_is_a_zeta_value as B


def geodesic(M):
    a, b, c, d = (int(x) for x in (M[0][0], M[0][1], M[1][0], M[1][1]))
    D = (a + d) ** 2 - 4
    r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b)
    beta, betap = max(r1, r2), min(r1, r2)
    lam = max(abs(((a + d) + math.sqrt(D)) / 2), abs(((a + d) - math.sqrt(D)) / 2))
    return beta, betap, 2 * math.log(lam), D


def lhs(M, c, s=2.0, nodes=96, Mmax=60, Nmax=4000):
    beta, betap, ell, _ = geodesic(M)
    x, w = np.polynomial.legendre.leggauss(nodes)
    t = ell / 2 * x                                            # one period, centred at the top: ds = dt
    z = (beta * 1j * np.exp(t) + betap) / (1j * np.exp(t) + 1)
    y = z.imag
    total = np.zeros(len(t), dtype=complex)
    n = np.arange(-Nmax, Nmax + 1)
    for m in range(-Mmax, Mmax + 1):
        lat = m * z[:, None] + n[None, :]
        ph = np.exp(2j * np.pi * (c[0] * m + c[1] * n))[None, :]
        term = ph * (np.abs(lat) ** (-2 * s))
        if m == 0:
            term[:, Nmax] = 0
        total += term.sum(1)
    return ell / 2 * np.sum(w * (y ** s) * total)


def rhs(M, i, j, N, s=2.0, X=4000.0):
    Mf = np.array([[float(M[0][0]), float(M[0][1])], [float(M[1][0]), float(M[1][1])]])
    ev, R = np.linalg.eig(Mf)
    halve = ev.real.min() < 0                                  # negative eigenvalues: sum over <M^2> and halve
    G = Mf @ Mf if halve else Mf
    ev, R = np.linalg.eig(G); order = np.argsort(-np.abs(ev.real)); ev = ev.real[order]; R = R[:, order].real
    lam = ev[0]
    a, b, cc, d = (int(x) for x in (M[0][0], M[0][1], M[1][0], M[1][1]))
    D = (a + d) ** 2 - 4
    Q = lambda v0, v1: (b * v1 ** 2 + (a - d) * v0 * v1 - cc * v0 ** 2) / math.sqrt(D)
    Rinv = np.linalg.inv(R)
    # the region |Q| <= X inside the strip: bound the box by the strip's corners in (alpha, beta)
    # Q(alpha r1 + beta r2) = q12 * alpha * beta for a constant q12 (Q vanishes on each eigenline)
    q12 = (Q(*(R[:, 0] + R[:, 1])) - Q(*R[:, 0]) - Q(*R[:, 1]))
    A = math.sqrt(X / abs(q12)) * lam * 1.05; Bm = math.sqrt(X / abs(q12)) * 1.05      # t < 2 log lambda: |alpha| < sqrt(X) lambda
    corners = np.array([[sa * A, sb * Bm] for sa in (1, -1) for sb in (1, -1)])
    pts = corners @ R.T
    lo = np.floor(pts.min(0)).astype(int) - 1; hi = np.ceil(pts.max(0)).astype(int) + 1
    tot = 0j; count = 0
    for v0 in range(lo[0], hi[0] + 1):
        v1 = np.arange(lo[1], hi[1] + 1)
        V = np.vstack([np.full_like(v1, v0), v1]).astype(float)
        al, be = Rinv @ V
        ok = (np.abs(al) > 1e-12) & (np.abs(be) > 1e-12)
        t = np.where(ok, np.log(np.abs(al) / np.where(ok, np.abs(be), 1)), -1)
        q = q12 * al * be
        sel = ok & (t >= 0) & (t < 2 * math.log(lam)) & (np.abs(q) <= X)      # M scales alpha/beta by lambda^2
        if not sel.any():
            continue
        chi = np.exp(2j * np.pi * ((i * v0 + j * v1[sel]) % N) / N)
        tot += np.sum(chi * np.abs(q[sel]) ** (-s)); count += int(sel.sum())
    return (tot / 2 if halve else tot), count


def H(s):
    return 2 ** (-s) * math.sqrt(math.pi) * math.gamma(s / 2) / math.gamma((s + 1) / 2)


if __name__ == "__main__":
    SL = B._sl(); out = []
    for st, k in [("+LR", 2), ("-LR", 1), ("+LR", 3), ("-LR", 2)]:
        eps = 1 if st[0] == "+" else -1; word = st[1:]
        with contextlib.redirect_stdout(io.StringIO()):
            N, F, S = SL.exact_slopes(eps, word, k)
        M = B.abel_M(SL, eps, word, k)
        for (i, j, _) in list(S)[:6]:
            if (i, j) == (0, 0):
                continue
            L = lhs(M, (i / N, j / N))
            R1, n1 = rhs(M, i, j, N, X=2000.0); R2, n2 = rhs(M, i, j, N, X=8000.0)
            rel = abs(L - H(2) * R2) / max(abs(L), 1e-12)
            out.append({"level": [st, k], "ij": [i, j], "lhs": [L.real, L.imag], "H*Z_tot (X=8000)": [(H(2) * R2).real, (H(2) * R2).imag],
                        "rel": rel, "tail 2000->8000": abs(R2 - R1) / max(abs(R2), 1e-12), "orbit reps": n2})
            print(st, k, (i, j), "lhs %.8f%+.8fi" % (L.real, L.imag), "H*Z %.8f%+.8fi" % ((H(2) * R2).real, (H(2) * R2).imag),
                  "rel %.1e" % rel, "tail %.1e" % out[-1]["tail 2000->8000"], flush=True)
    (HERE / "hecke_s2.json").write_text(json.dumps(out, indent=1))
