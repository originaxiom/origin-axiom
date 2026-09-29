"""B1501 post-run checks: the census against independent criteria (run after torus_link_census.py; reads census.json).

(1) Each class's fixed set against an independent criterion:
    - S6: the fixed subspace of the torus element on R^7 (1 + 2 x #trivial eigenvalue pairs): two antipodal points or a great 2-sphere.
    - S3xS3, left L_(t1,t2,t3): gK fixed iff g_i^-1 t_i g_i = d for one d, so fixed points exist iff t1, t2, t3 are conjugate in SU(2)
      (equal traces); the set is then the orbit of the maximal torus, a 2-torus.
    - S3xS3, twisted L_(1,1,k) sigma: gauge g1 = 1 gives g3 = d, g2 = d^-1 and d^3 = k: three points if k is not central, a point and
      the 2-sphere of order-3 (k = 1) or order-6 (k = -1) elements if it is.
    - CP3, left: the eigenlines of t on C^4; an eigenvalue of multiplicity m gives CP^(m-1).
    - F12, left: g's columns form an eigenbasis of t: six points (regular) or three 2-spheres (a double eigenvalue).
    - F12, twisted L_t R_P: g^-1 t g must lie in T P^-1, whose elements all have characteristic polynomial x^3 - 1; fixed points exist
      iff the eigenvalues of t are {c, c w, c w^2}.
(2) Lefschetz: chi(Fix gamma) = L(gamma) = chi(Y) for left translations (homotopic to the identity): S6 2, S3xS3 0, CP3 4, F12 6;
    L(sigma) = 3 on S3xS3 (sigma* on H^3 = Z^2 is [[-1, 1], [-1, 0]], trace -1; degree +1); L(R_P) = 0 on F12 (H*(SU(3)/T) is the
    regular representation of the Weyl group, where a 3-cycle has trace 0).  chi counts points 1, spheres 2, tori 0.
(3) Any torus's shape recomputed without the census pipeline, from the lattice and the metric in closed form.
(4) Reproducibility: every torus class and a fixed sample of the others re-run in this fresh process; the records must agree.
"""
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def _load():
    spec = importlib.util.spec_from_file_location("b1501_census", HERE / "torus_link_census.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def comp_signature(rec):
    return sorted((c["dim"], c["topology"]["type"]) for c in rec["components"])


def expected_signature(rec):
    """the independent criterion (1), as a sorted list of (dim, type)"""
    q = [Fraction(x) for x in rec["q"]]
    link, outer = rec["link"], rec["outer"]
    if link == "S6":
        qs = [q[0] % 1, q[1] % 1, (-q[0] - q[1]) % 1]
        triv = sum(1 for x in qs if x == 0)
        return [(0, "point"), (0, "point")] if triv == 0 else [(2, "sphere")]
    if link == "S3xS3" and outer is None:
        tr = [round(np.cos(2 * np.pi * float(x)), 12) for x in q]
        return [(2, "torus")] if len(set(tr)) == 1 else []
    if link == "S3xS3":
        kappa = q[2] % 1
        central = kappa in (Fraction(0), Fraction(1, 2))
        return [(0, "point"), (2, "sphere")] if central else [(0, "point")] * 3
    if link == "CP3":
        a, b = q
        ev = [a % 1, b % 1, (-a) % 1, (-b) % 1]
        mult = {}
        for e in ev:
            mult[e] = mult.get(e, 0) + 1
        out = []
        for m in mult.values():
            out.append({1: (0, "point"), 2: (2, "sphere")}[m])
        return sorted(out)
    if link == "F12" and outer is None:
        ev = [q[0] % 1, q[1] % 1, (-q[0] - q[1]) % 1]
        if len(set(ev)) == 3:
            return [(0, "point")] * 6
        return [(2, "sphere")] * 3
    if link == "F12":
        ev = sorted([q[0] % 1, q[1] % 1, (-q[0] - q[1]) % 1])
        c = ev[0]
        coxeter = sorted([c % 1, (c + Fraction(1, 3)) % 1, (c + Fraction(2, 3)) % 1]) == ev
        return [(2, "torus")] if coxeter else []
    raise ValueError(rec["label"])


LEFSCHETZ_LEFT = {"S6": 2, "S3xS3": 0, "CP3": 4, "F12": 6}
LEFSCHETZ_TWISTED = {"S3xS3": 3, "F12": 0}


def euler_char(rec):
    chi = 0
    for c in rec["components"]:
        chi += {"point": 1, "sphere": 2, "torus": 0}[c["topology"]["type"]]
    return chi


def sigma_on_H3():
    """sigma on S3 x S3 = SU(2)^3/diag in the coordinates (u1, u2) = (g1 g2^-1, g2 g3^-1): (u1, u2) -> ((u1 u2)^-1, u1).
    Inversion on S3 has degree -1 (its differential at 1 is -1 on su(2)), multiplication pulls the fundamental class back to the sum."""
    deg_inv = round(np.linalg.det(-np.eye(3)))
    M = np.array([[deg_inv, 1], [deg_inv, 0]])            # columns: sigma*(e1) = deg_inv (e1 + e2), sigma*(e2) = e1
    top = deg_inv * (-1)                                  # sigma*(e1 e2) = deg_inv (e1 + e2) e1 = deg_inv e2 e1 = -deg_inv e1 e2
    return M, int(1 - np.trace(M) + top)


def f12_coxeter_torus_shape():
    """the torus fixed by L_{c0} R_P on SU(3)/T, c0 = diag(1, w, w^2), in closed form: g^-1 c0 g = P^-1 for g built from the
    eigenvectors of P^-1 (the discrete Fourier basis); the fixed set is T . gT, with period lattice {X in t : exp X in Z(SU(3))}
    (the coweight lattice) and metric |pi_m(Ad_{g^-1} X)|^2"""
    w = np.exp(2j * np.pi / 3)
    P = np.zeros((3, 3), dtype=complex)
    P[1, 0], P[2, 1], P[0, 2] = 1, 1, 1
    Pinv = P.conj().T
    evals, vecs = np.linalg.eig(Pinv)
    c0 = np.diag([1, w, w * w])
    # order the eigenvectors so that g c0-eigenvalues match: g^-1 c0 g = Pinv  <=>  Pinv = g^-1 c0 g, i.e. g^-1 = V diag... solve
    # Pinv = V D V^-1 with D = diag(evals); want D = c0 up to order: permute
    order = [int(np.argmin(np.abs(evals - lam))) for lam in np.diag(c0)]
    V = vecs[:, order]
    V = V / np.linalg.norm(V, axis=0)
    g = V.conj().T                                        # g^-1 c0 g = V c0 V^-1 = Pinv  (V unitary)
    g = g / np.linalg.det(g) ** (1 / 3)
    assert np.abs(g.conj().T @ c0 @ g - Pinv).max() < 1e-12
    H = [np.diag([1j, 0, -1j]), np.diag([0, 1j, -1j])]

    def vf(X):
        Y = g.conj().T @ X @ g
        Y = Y - np.diag(np.diag(Y))                       # project to m (off-diagonal)
        return Y
    # the coweight lattice: q with exp(2 pi (q1 H1 + q2 H2)) = diag(e^{2 pi i q1}, e^{2 pi i q2}, e^{-2 pi i (q1 + q2)}) central,
    # i.e. q1 = q2 and 3 q1 in Z: generated by (1/3, 1/3) and (0, 1)
    basis = [np.array([1 / 3, 1 / 3]), np.array([0.0, 1.0])]
    Xs = [2 * np.pi * (b[0] * H[0] + b[1] * H[1]) for b in basis]
    for X in Xs:
        e = np.exp(np.diag(X))
        assert np.abs(e - e[0]).max() < 1e-12                                  # central
    G = np.array([[-0.5 * np.real(np.trace(vf(A) @ vf(B))) for B in Xs] for A in Xs]) / (2 * np.pi) ** 2
    # reduce
    a, b = np.array([1, 0]), np.array([0, 1])
    for _ in range(50):
        na, nb = a @ G @ a, b @ G @ b
        if nb < na:
            a, b = b, a
        mu = round((a @ G @ b) / (a @ G @ a))
        if mu == 0:
            break
        b = b - mu * a
    if a @ G @ b > 0:
        b = -b
    Gr = np.array([[a @ G @ a, a @ G @ b], [b @ G @ a, b @ G @ b]])
    tau = complex(Gr[0, 1] / Gr[0, 0], np.sqrt(np.linalg.det(Gr)) / Gr[0, 0])
    # the tangent vectors are in m entirely (Ad_{g^-1} t is orthogonal to t): the metric is the Killing metric on t
    orth = max(np.abs(np.diag(g.conj().T @ Hh @ g)).max() for Hh in H)
    return Gr, tau, orth


def main():
    T = _load()
    d = json.load(open(HERE / "census.json"))
    recs = d["records"]
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)
    # (1) independent criteria
    bad = [(r["label"], comp_signature(r), expected_signature(r)) for r in recs if comp_signature(r) != expected_signature(r)]
    log("(1) fixed sets against the independent criteria: %d of %d classes agree%s" % (len(recs) - len(bad), len(recs),
                                                                                       "" if not bad else "; DISAGREE: %s" % bad[:5]))
    # (2) Lefschetz
    badL = []
    for r in recs:
        L = LEFSCHETZ_LEFT[r["link"]] if r["outer"] is None else LEFSCHETZ_TWISTED[r["link"]]
        if euler_char(r) != L:
            badL.append((r["label"], euler_char(r), L))
    M, Ls = sigma_on_H3()
    assert Ls == 3
    log("(2) Lefschetz: sigma* on H^3(S3 x S3) = %s, L(sigma) = %d; chi(Fix) = L(gamma) on %d of %d classes%s" % (
        M.tolist(), Ls, len(recs) - len(badL), len(recs), "" if not badL else "; FAIL %s" % badL[:5]))
    # (3) closed-form torus shapes
    tori = [(r, c) for r in recs for c in r["components"] if c["topology"]["type"] == "torus"]
    f12 = [(r, c) for r, c in tori if r["link"] == "F12"]
    s3 = [(r, c) for r, c in tori if r["link"] == "S3xS3"]
    ok3 = True
    if f12:
        Gr, tau, orth = f12_coxeter_torus_shape()
        for r, c in f12:
            Gc = np.array(c["shape"]["Gram (units (2 pi)^2)"])
            ok3 &= np.abs(Gc - Gr).max() < 1e-9
        log("(3) F12 Coxeter torus in closed form: Ad_{g^-1} t is orthogonal to t (to %.1e); Gram %s (2 pi)^2, tau = %.12f + %.12f i; "
            "the census's %d F12 torus components agree: %s" % (orth, np.round(Gr, 12).tolist(), tau.real, tau.imag, len(f12), ok3))
    if s3:
        Gref = np.array([[2, -1], [-1, 2]]) / 3
        ok_s3 = all(np.abs(np.array(c["shape"]["Gram (units (2 pi)^2)"]) - Gref).max() < 1e-9 for r, c in s3)
        ok3 &= ok_s3
        log("(3) S3xS3: all %d torus components have the Gram of U(1)^3/U(1) in the normal metric, [[2/3, -1/3], [-1/3, 2/3]]: %s"
            % (len(s3), ok_s3))
    # (4) reproducibility in a fresh process
    torus_labels = sorted(set(r["label"] for r, c in tori))
    others = [r for r in recs if r["label"] not in torus_labels]
    rng = np.random.default_rng(1501)
    sample = [others[i]["label"] for i in sorted(rng.choice(len(others), size=min(12, len(others)), replace=False))]
    classes = {T.class_label(c): c for name, L in T.LINKS.items() for c in T.enumerate_classes(L())}
    links = {name: L() for name, L in T.LINKS.items()}
    byl = {r["label"]: r for r in recs}
    mism = []
    for lab in torus_labels + sample:
        cls = classes[lab]
        r2 = T.run_class(links[cls["link"]], cls)
        r1 = byl[lab]
        same = (r1["converged"] == r2["converged"] and comp_signature(r1) == comp_signature(r2)
                and [c["seeds"] for c in r1["components"]] == [c["seeds"] for c in r2["components"]])
        for c1, c2 in zip(r1["components"], r2["components"]):
            if "shape" in c1:
                same &= abs(c1["shape"]["tau"][0] - c2["shape"]["tau"][0]) < 1e-12 and abs(c1["shape"]["tau"][1] - c2["shape"]["tau"][1]) < 1e-12
                same &= c1["H_F"]["H_F"] == c2["H_F"]["H_F"]
        if not same:
            mism.append(lab)
    log("(4) reproducibility: %d torus classes and %d others re-run in a fresh process; %s" % (
        len(torus_labels), len(sample), "all records agree" if not mism else "MISMATCH %s" % mism))
    ok = not bad and not badL and ok3 and not mism
    log("POST-RUN CHECKS: %s" % ("ALL PASS" if ok else "FAIL"))
    (HERE / "post_run_checks_run.txt").write_text("\n".join(lines) + "\n")
    (HERE / "post_run_checks.json").write_text(json.dumps({"criteria disagreements": bad, "lefschetz failures": badL,
                                                           "closed-form shapes agree": bool(ok3), "reproducibility mismatches": mism,
                                                           "rerun": torus_labels + sample, "all pass": bool(ok)}, indent=1))
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
