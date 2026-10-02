"""B1502 -- THE LOCAL MODELS' CHIRALITY: what B1501's two torus models put at a cusp point, checked with own code.

The two models (B1501): M1 = C(S3 x S3)/Gamma with Gamma inside the diagonal U(1) of SU(2)^3 (the locus is the cone over the diagonal
torus, SU(n)-type); M2 = C(F12)/<gamma>, gamma = L_{diag(1,w,w^2)} R_P (the locus is the cone over the Coxeter torus, A2).

(1) Rational cohomology of the links, H*(G/K; R) = H*(g, k) (relative Lie algebra cohomology: K-invariant forms on m with the
    Chevalley-Eilenberg differential), and the action of the listed outer elements on it.  H^k(Y/Gamma; Q) = H^k(Y; Q)^Gamma, so any
    finite Gamma containing a torus-fixing element has H^2 = H^4 = 0 when that element has no invariant classes.
(2) The torus links in H_2(Y; Q): S3 x S3 has H_2 = 0; the Coxeter torus is an orbit of the maximal torus T of SU(3), which has fixed
    points on F12 (the six Weyl points), so the orbit map is null-homotopic and [F] = 0.
(3) M1's smooth phases: the three Bryant-Salamon smoothings X_k of C(S3 x S3), modelled as S3 x H with SU(2)^3 acting by
    (a_i q a_j^-1, a_k p a_j^-1) for (i, j, k) cyclic.  Every element of SU(2)^3 acts, so Gamma does; the fixed set of a non-central
    (t, t, t) is S1 x C, the filling of the cone over the torus along the circle theta_k, i.e. the lattice vector e_k of B1501's period
    lattice (a shortest vector, an A2 root), one per phase; the three phases are permuted by sigma.
(4) M2's smooth phases: the Bryant-Salamon smoothings of C(F12) are the cohomogeneity-one SU(3)-manifolds with group diagram
    T < U(2)_j < SU(3) (the three U(2) containing T).  A right action R_n extends to X_j only if n U(2)_j n^-1 = U(2)_j; R_P permutes
    the three U(2)_j, so no element L_a R_P^{+-1} (every torus-fixing element of F12, B1501 section 2) acts on any X_j.
"""
import importlib.util
import itertools
import json
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1501_census", ROOT / "frontier" / "B1501_the_torus_link_census" / "verification" / "torus_link_census.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)


# ----------------------------------------------------------------------------------------------------- (1) relative cohomology
def subsets(n, k):
    return list(itertools.combinations(range(n), k))


def sort_sign(seq):
    seq = list(seq)
    sign = 1
    for a in range(len(seq)):
        for b in range(len(seq) - 1 - a):
            if seq[b] > seq[b + 1]:
                seq[b], seq[b + 1] = seq[b + 1], seq[b]
                sign = -sign
    return tuple(seq), sign


def wedge_power(A, k):
    """Lambda^k of a linear map A (on vectors), in the basis of sorted k-subsets"""
    B = subsets(A.shape[0], k)
    if k == 0:
        return np.ones((1, 1))
    return np.array([[np.linalg.det(A[np.ix_(I, J)]) for J in B] for I in B])


def derivation_power(A, k):
    """the extension of a derivation A (on vectors) to Lambda^k"""
    n = A.shape[0]
    B = subsets(n, k)
    idx = {I: i for i, I in enumerate(B)}
    M = np.zeros((len(B), len(B)))
    for c, J in enumerate(B):
        for pos in range(k):
            for i in range(n):
                if A[i, J[pos]] == 0:
                    continue
                K = list(J)
                K[pos] = i
                if len(set(K)) < k:
                    continue
                K2, s = sort_sign(K)
                M[idx[K2], c] += s * A[i, J[pos]]
    return M


def relative_cohomology(link):
    """Betti numbers of G/K from the K-invariant forms on m, the harmonic representatives, and d^2 on invariants"""
    m = link.m_basis
    n = len(m)
    c = np.array([[[T.ip(m[a], m[b] @ m[e] - m[e] @ m[b]) for e in range(n)] for b in range(n)] for a in range(n)])
    B = {k: subsets(n, k) for k in range(n + 1)}
    idx = {k: {I: i for i, I in enumerate(B[k])} for k in range(n + 1)}

    def d_of(k):
        # d e^a = -sum_{b<e} c[a,b,e] e^b ^ e^e, extended as an antiderivation
        M = np.zeros((len(B[k + 1]), len(B[k])))
        for col, I in enumerate(B[k]):
            for s, a in enumerate(I):
                for (b, e) in B[2]:
                    coef = -c[a, b, e]
                    if abs(coef) < 1e-15:
                        continue
                    new = list(I[:s]) + [b, e] + list(I[s + 1:])
                    if len(set(new)) < k + 1:
                        continue
                    K2, sg = sort_sign(new)
                    M[idx[k + 1][K2], col] += (-1) ** s * sg * coef
        return M
    D = {k: d_of(k) for k in range(n)}
    inv = {}
    for k in range(n + 1):
        rows = []
        for Z in link.k_basis:
            A = np.array([[T.ip(m[a], Z @ m[b] - m[b] @ Z) for b in range(n)] for a in range(n)])
            rows.append(derivation_power(-A.T, k))
        inv[k] = T.null_space(np.vstack(rows), 1e-9)
    harm, betti = {}, []
    for k in range(n + 1):
        V = inv[k]
        closed = V @ (T.null_space(D[k] @ V, 1e-9) if k < n else np.eye(V.shape[1]))
        if k > 0 and inv[k - 1].shape[1]:
            Im = D[k - 1] @ inv[k - 1]
            # the exact forms' span by an absolute cutoff, as the script's other rank decisions (2026-10-02, main's S37): numpy's
            # pinv default, 1e-15 x sigma_max, inverted a rounding-level singular value on main's bench (8e-15 beside 3.46) and read
            # b3(CP3) = 1; and any cutoff relative to sigma_max inverts pure noise where the image is exactly zero (sigma_max ~ 1e-15)
            u_im, s_im, _ = np.linalg.svd(Im, full_matrices=False)
            Q = u_im[:, s_im > 1e-9]
            closed = closed - Q @ (Q.conj().T @ closed)
        if closed.size:
            u, s, _ = np.linalg.svd(closed, full_matrices=False)
            harm[k] = u[:, : int(np.sum(s > 1e-8))]
        else:
            harm[k] = np.zeros((len(B[k]), 0))
        betti.append(harm[k].shape[1])
    d2 = max(float(np.abs(D[k + 1] @ D[k] @ inv[k]).max(initial=0.0)) for k in range(n - 1))
    return betti, harm, d2


def action_on_cohomology(harm, A, k):
    """the pullback of an isometry A of m (on vectors) on the harmonic k-forms: trace and the dimension of the invariants"""
    Hk = harm[k]
    if Hk.shape[1] == 0:
        return {"dim": 0, "trace": 0.0, "invariants": 0}
    M = Hk.T @ wedge_power(A.T, k) @ Hk
    ev = np.linalg.eigvals(M)
    return {"dim": int(Hk.shape[1]), "trace": round(float(np.real(np.trace(M))), 10),
            "invariants": int(np.sum(np.abs(ev - 1) < 1e-8)), "eigenvalues": [str(np.round(z, 10)) for z in ev]}


def outer_on_m(link, o):
    elem = ("aut", None, o) if isinstance(o, dict) else ("right", o)
    return T.transport_on_m(link, elem)


# ----------------------------------------------------------------------------------------------------------- (3) M1's phases
def quat(a, b):
    """the quaternion a + b j as a 2x2 complex matrix (unit quaternions are SU(2))"""
    return np.array([[a, -np.conj(b)], [b, np.conj(a)]])


def m1_phase(k, t_angle, rng, seeds=200):
    """X_k = S3 x H, SU(2)^3 acting by (a_i q a_j^-1, a_k p a_j^-1), (i, j, k) cyclic.  The fixed set of (t, t, t), t = diag(e^{i x},
    e^{-i x}) non-central: Newton from random (q, p); report the solutions' form, the tangent dimension, the collapsing circle."""
    t = np.diag([np.exp(1j * t_angle), np.exp(-1j * t_angle)])

    def act(q, p):
        return t @ q @ T.dag(t), t @ p @ T.dag(t)

    def resid(x):
        q = quat(x[0] + 1j * x[1], x[2] + 1j * x[3])
        p = quat(x[4] + 1j * x[5], x[6] + 1j * x[7])
        q2, p2 = act(q, p)
        r = np.concatenate([(q2 - q).reshape(-1), (p2 - p).reshape(-1), [np.linalg.norm([x[0], x[1], x[2], x[3]]) ** 2 - 1]])
        return np.concatenate([r.real, r.imag])
    sols = []
    for _ in range(seeds):
        x = rng.normal(size=8)
        x[:4] /= np.linalg.norm(x[:4])
        x[4:] *= rng.uniform(0.2, 3.0)
        for _it in range(50):
            R = resid(x)
            if np.linalg.norm(R) < 1e-14:
                break
            J = np.zeros((len(R), 8))
            h = 1e-7
            for i in range(8):
                e = np.zeros(8)
                e[i] = h
                J[:, i] = (resid(x + e) - resid(x - e)) / (2 * h)
            x = x - np.linalg.lstsq(J, R, rcond=None)[0]
        if np.linalg.norm(resid(x)) < 1e-10:
            sols.append(x.copy())
    sols = np.array(sols)
    # the claimed fixed set: q diagonal (x[2] = x[3] = 0) and p diagonal (x[6] = x[7] = 0)
    off = float(np.abs(sols[:, [2, 3, 6, 7]]).max()) if len(sols) else None
    # its tangent dimension at a point: the kernel of the linearised residual (on the sphere x R^4)
    x0 = sols[0]
    J = np.zeros((len(resid(x0)), 8))
    for i in range(8):
        e = np.zeros(8)
        e[i] = 1e-7
        J[:, i] = (resid(x0 + e) - resid(x0 - e)) / 2e-7
    tangent_dim = 8 - T.rank_of(J, 1e-6)
    return {"phase": k, "t angle": t_angle, "fixed seeds": int(len(sols)), "largest off-diagonal part": off,
            "tangent dimension": int(tangent_dim)}


def m1_collapsing_circle(k):
    """at |p| = r the point (q, p) of X_k is [a] with a_j = 1, a_i = q, a_k = p/|p|; on the fixed set q = diag(e^{i phi}),
    p = diag(a, conj a): the torus element (theta_i, theta_j, theta_k) = (phi, 0, arg a).  The circle that collapses at p = 0 is
    arg a with phi fixed: the q-vector e_k.  Returns e_k and its norm in B1501's Gram (units (2 pi)^2), against the lattice minimum."""
    e = np.zeros(3)
    e[k - 1] = 1.0
    P = np.eye(3) - np.ones((3, 3)) / 3                              # modulo the diagonal (the stabiliser direction)
    v = P @ e
    norm = float(v @ v)                                              # |X|^2 = sum (theta_i - mean)^2 in units (2 pi)^2
    lattice = [P @ np.array(u, dtype=float) for u in itertools.product(range(-2, 3), repeat=3)]
    minimum = min(float(w @ w) for w in lattice if float(w @ w) > 1e-9)
    return {"phase": k, "collapsing circle (q-vector)": e.astype(int).tolist(), "norm (2 pi)^2": round(norm, 12),
            "lattice minimum": round(minimum, 12), "shortest": abs(norm - minimum) < 1e-12}


def m1_orbit_types():
    """the SU(2)^3 action on X_3 = S3 x H: stabiliser dimensions at a principal point (p != 0) and on the zero section (p = 0)"""
    link = T.S3xS3()
    gb = link.g_basis

    def stab_dim(q, p):
        cols = []
        for X in gb:
            X1, X2, X3 = T.blocks(X)
            dq = X1 @ q - q @ X2
            dp = X3 @ p - p @ X2
            cols.append(np.concatenate([dq.reshape(-1), dp.reshape(-1)]))
        M = np.array(cols).T
        M = np.concatenate([M.real, M.imag])
        return len(gb) - T.rank_of(M, 1e-9)
    q = quat(np.exp(0.3j) * np.cos(0.4), np.sin(0.4) * np.exp(1.1j))
    return {"principal stabiliser dim (orbit dim 9 - s)": stab_dim(q, 1.7 * quat(0.6 + 0.2j, 0.3 - 0.7j) / 1.0),
            "zero-section stabiliser dim": stab_dim(q, np.zeros((2, 2), dtype=complex))}


# ----------------------------------------------------------------------------------------------------------- (4) M2's phases
def u2_subalgebras():
    """the three u(2) in su(3) containing t: t plus the root plane of one pair (a, b)"""
    out = {}
    for a, b in itertools.combinations(range(3), 2):
        E = np.zeros((3, 3), dtype=complex)
        E[a, b], E[b, a] = 1, -1
        F = np.zeros((3, 3), dtype=complex)
        F[a, b], F[b, a] = 1j, 1j
        out[(a, b)] = [E, F]
    return out


def which_u2(root_plane, subs):
    """the pair (a, b) whose root plane equals the given plane"""
    for key, (E, F) in subs.items():
        M = np.array([np.concatenate([X.reshape(-1).real, X.reshape(-1).imag]) for X in [E, F] + root_plane])
        if T.rank_of(M, 1e-9) == 2:
            return key
    return None


def m2_phases():
    link = T.F12()
    subs = u2_subalgebras()
    out = {}
    s = np.zeros((3, 3), dtype=complex)
    s[0, 1], s[1, 0], s[2, 2] = 1, 1, -1
    for name, n in [("R_P", link.outer["R_P"]), ("R_P^2", link.outer["R_P^2"]), ("transposition (12), excluded", s)]:
        images = {}
        for key, plane in subs.items():
            images[str(key)] = str(which_u2([n @ X @ T.dag(n) for X in plane], subs))
        fixed = [k for k, v in images.items() if k == v]
        out[name] = {"U(2)_j -> n U(2)_j n^-1": images, "preserved": fixed}
    return out


# ------------------------------------------------------------------------------------------------------ (2) the torus links
def torus_fixed_points_on_f12():
    """T fixes the six Weyl points wT (w a signed permutation matrix in SU(3)): the orbit map of the Coxeter torus is null-homotopic"""
    link = T.F12()
    worst = 0.0
    pts = 0
    for perm in itertools.permutations(range(3)):
        w = np.zeros((3, 3), dtype=complex)
        for i, j in enumerate(perm):
            w[j, i] = 1
        w[:, 0] *= np.linalg.det(w)                                    # make det = +1
        for q in [(0.13, 0.41), (0.37, 0.05), (0.21, 0.66)]:
            t = link.torus(q)
            worst = max(worst, float(np.linalg.norm(link.embed(t @ w) - link.embed(w))))
        pts += 1
    return {"Weyl points": pts, "worst |t.p - p| over the torus": worst}


def torus_cohomology(A, B):
    """H*(Z^2; V) for commuting A, B on V (the cusp torus's local system), by the Koszul complex V -> V^2 -> V"""
    n = A.shape[0]
    I = np.eye(n)
    d0 = np.vstack([A - I, B - I])
    d1 = np.hstack([B - I, -(A - I)])
    assert np.abs(d1 @ d0).max() < 1e-12
    r0, r1 = T.rank_of(d0, 1e-10), T.rank_of(d1, 1e-10)
    return [n - r0, 2 * n - r0 - r1, n - r1]


def sectors_at_a_cone_point(rng):
    """(5) the frame's sectors on the cusp torus under the geometric representation (B1368): meridian a -> z [[1,1],[0,1]], longitude
    lambda -> -[[1, 2 sqrt3 i],[0, 1]] (tr -2, Calegari; the character is trivial on lambda).  Spin 1/2 (V2 (x) C_z): acyclic for every
    z, so at a cone point the doublets are Witt -- no choice.  Spin 0 with character z: acyclic unless z = 1, where H* = (1, 2, 1)."""
    Ua = np.array([[1, 1], [0, 1]], dtype=complex)
    Ul = -np.array([[1, 2 * np.sqrt(3) * 1j], [0, 1]], dtype=complex)
    assert np.abs(Ua @ Ul - Ul @ Ua).max() < 1e-12
    zs = [1.0, -1.0, 2.0, np.exp(0.7j), 0.3 + 1.2j] + list(rng.normal(size=4) + 1j * rng.normal(size=4))
    half = [torus_cohomology(z * Ua, Ul) for z in zs]
    zero = [torus_cohomology(np.array([[z]]), np.array([[1.0 + 0j]])) for z in zs]
    return {"spin 1/2 link cohomology (all z sampled)": sorted(set(tuple(h) for h in half)),
            "spin 0 link cohomology at z = 1": zero[0], "spin 0 link cohomology at z != 1": sorted(set(tuple(h) for h in zero[1:]))}


def main():
    t0 = time.time()
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)
    rec = {"cohomology": {}, "M1 phases": [], "M1 collapsing circles": [], "M2 phases": None}
    log("B1502 THE LOCAL MODELS' CHIRALITY -- own-code verification")
    expected = {"S6": [1, 0, 0, 0, 0, 0, 1], "S3xS3": [1, 0, 0, 2, 0, 0, 1], "CP3": [1, 0, 1, 0, 1, 0, 1], "F12": [1, 0, 2, 0, 2, 0, 1]}
    for name, L in T.LINKS.items():
        link = L()
        betti, harm, d2 = relative_cohomology(link)
        entry = {"Betti": betti, "d^2 on invariant forms": d2, "outer": {}}
        assert betti == expected[name], (name, betti)
        for oname, o in link.outer.items():
            A = outer_on_m(link, o)
            entry["outer"][oname] = {str(k): action_on_cohomology(harm, A, k) for k in (2, 3, 4)}
        rec["cohomology"][name] = entry
        log("(1) %-6s Betti %s (d^2 = %.1e on invariant forms)%s" % (
            name, betti, d2, "".join("; %s on H^2, H^3, H^4: traces %s, invariants %s" % (
                o, [v["trace"] for v in d.values()], [v["invariants"] for v in d.values()]) for o, d in entry["outer"].items())))
    f = rec["cohomology"]["F12"]["outer"]
    s3 = rec["cohomology"]["S3xS3"]["outer"]
    no_u1 = all(f[o][k]["invariants"] == 0 for o in f for k in ("2", "4"))
    log("    => M2 (every torus-fixing element is L_a R_P^{+-1}): H^2(Y/Gamma; Q) = H^4(Y/Gamma; Q) = 0 for every finite Gamma "
        "containing one: %s" % no_u1)
    log("    => M1: H^2(S3 x S3) = H^4 = 0, so H^2(Y/Gamma; Q) = H^4(Y/Gamma; Q) = 0 for every finite Gamma; sigma on H^3: trace %s "
        "(L(sigma) = 1 - (%s) + 1 = %s, B1501's Lefschetz number)" % (
            s3["sigma"]["3"]["trace"], s3["sigma"]["3"]["trace"], round(2 - s3["sigma"]["3"]["trace"])))
    rec["no C-field U(1) and no rational flux at the apex"] = bool(no_u1)
    # (2)
    tf = torus_fixed_points_on_f12()
    rec["torus links"] = {"S3xS3": "H_2 = 0 (Betti above)", "F12": tf}
    log("(2) torus links: S3 x S3 has H_2 = 0; on F12 the maximal torus fixes the %d Weyl points (|t.p - p| <= %.1e), so its orbit "
        "the Coxeter torus is null-homologous" % (tf["Weyl points"], tf["worst |t.p - p| over the torus"]))
    # (3)
    ot = m1_orbit_types()
    rec["M1 orbit types"] = ot
    log("(3) M1: SU(2)^3 on X_k = S3 x H: stabiliser dimension %d at a principal point (orbit S3 x S3), %d on the zero section "
        "(orbit S3)" % (ot["principal stabiliser dim (orbit dim 9 - s)"], ot["zero-section stabiliser dim"]))
    rng = np.random.default_rng(1502)
    for k in (1, 2, 3):
        for ang in (np.pi / 4, np.pi / 5, 2 * np.pi / 7):
            r = m1_phase(k, ang, rng)
            rec["M1 phases"].append(r)
        c = m1_collapsing_circle(k)
        rec["M1 collapsing circles"].append(c)
        log("    phase X_%d: fixed set of (t, t, t) found from %s seeds per element, off-diagonal part <= %.1e, tangent dimension %s; "
            "the circle collapsing at p = 0 is %s, norm %s (2 pi)^2 = the lattice minimum: %s" % (
                k, [x["fixed seeds"] for x in rec["M1 phases"][-3:]], max(x["largest off-diagonal part"] for x in rec["M1 phases"][-3:]),
                sorted(set(x["tangent dimension"] for x in rec["M1 phases"][-3:])), c["collapsing circle (q-vector)"],
                c["norm (2 pi)^2"], c["shortest"]))
    # (4)
    rec["M2 phases"] = m2_phases()
    for name, v in rec["M2 phases"].items():
        log("(4) M2: %s maps the U(2)_j containing T as %s; preserved: %s" % (name, v["U(2)_j -> n U(2)_j n^-1"], v["preserved"] or "none"))
    # (5)
    sec = sectors_at_a_cone_point(rng)
    rec["frame sectors at a cone point"] = sec
    log("(5) the frame's sectors on the cusp torus (geometric representation, B1368): spin 1/2 link cohomology %s for every z sampled "
        "(acyclic: at a cone point the doublets carry no choice); spin 0: %s at z = 1 (the choice, B1500), %s otherwise" % (
            sec["spin 1/2 link cohomology (all z sampled)"], sec["spin 0 link cohomology at z = 1"], sec["spin 0 link cohomology at z != 1"]))
    ok = (no_u1 and tf["worst |t.p - p| over the torus"] < 1e-12
          and sec["spin 1/2 link cohomology (all z sampled)"] == [(0, 0, 0)] and sec["spin 0 link cohomology at z = 1"] == [1, 2, 1]
          and sec["spin 0 link cohomology at z != 1"] == [(0, 0, 0)]
          and all(x["fixed seeds"] > 0 and x["largest off-diagonal part"] < 1e-9 and x["tangent dimension"] == 3 for x in rec["M1 phases"])
          and all(c["shortest"] for c in rec["M1 collapsing circles"])
          and not rec["M2 phases"]["R_P"]["preserved"] and not rec["M2 phases"]["R_P^2"]["preserved"]
          and len(rec["M2 phases"]["transposition (12), excluded"]["preserved"]) == 1
          and ot["principal stabiliser dim (orbit dim 9 - s)"] == 3 and ot["zero-section stabiliser dim"] == 6)
    rec["all checks pass"] = bool(ok)
    log("ALL CHECKS PASS" if ok else "CHECK FAILED")
    log("%.1f s" % (time.time() - t0))
    (HERE / "local_models_chirality.json").write_text(json.dumps(T.jsonable(rec), indent=1))
    (HERE / "local_models_chirality_run.txt").write_text("\n".join(lines) + "\n")
    return rec


if __name__ == "__main__":
    main()
