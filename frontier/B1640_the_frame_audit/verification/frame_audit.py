#!/usr/bin/env python3
"""B1640 -- THE FRAME AUDIT (2026-10-13): three statements that took a frame or a convention for forced, checked with main's
own sealed instrument (B1635's couplings_on_the_ruled_branch.py, imported unchanged).

  A  degeneracy at omega on the ruled branch: B1635's own sealed read-outs, and live members of Tbar x T (B1618's Dirac
     tensor) and of mixed T x T (symmetric plus antisymmetric pieces)
  B  the hand of the multiplier: coupling dimensions by piece under the record's multiplier (lift^-1, as B1634) and under
     its complex conjugate (the transpose, or the other piece of V)
  C  the TM1 residual pair on the ruled branch: rho_theta(RL) and rho_theta(RRL) against the stabilisers of points of H

    python3 -B frame_audit.py      # writes frame_audit.json beside itself
"""
import importlib.util, io, contextlib, itertools, json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
B1635 = os.path.join(HERE, "..", "..", "B1635_couplings_on_the_ruled_branch", "verification")
spec = importlib.util.spec_from_file_location("b1635", os.path.join(B1635, "couplings_on_the_ruled_branch.py"))
c = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(c)
inv = np.linalg.inv
rng = np.random.default_rng(1640)
out = {}


def ratios(Y):
    s = np.linalg.svd(Y, compute_uv=False)
    return s / s[0]


def gaps(r):                                    # the smallest relative gap between the three singular values
    return float(min(r[0] - r[1], r[1] - r[2]))


# ---- A. degeneracy at omega -------------------------------------------------------------------------------------------
sealed = json.load(open(os.path.join(B1635, "couplings_on_the_ruled_branch.json")))
A = {"sealed_nondegenerate_at_omega": sealed["K5_nondegenerate_at_omega"],
     "sealed_masses": {k: sealed["K3_K5_masses"][k]["omega"][0] for k in sealed["K5_nondegenerate_at_omega"]}}
live = {}
for k in (4, 6):                                 # Tbar x T: Y -> rho Y rho^-1, B1635's own construction (weight k)
    full, mons, _ = c.equivariant_space(k, lambda M: M, lambda M: inv(M))
    for sd in range(3):
        co = rng.normal(size=full.shape[0]) + 1j * rng.normal(size=full.shape[0])
        r = ratios(c.evaluate(np.einsum("n,nrcm->rcm", co, full), mons, c.OMEGA, 0))
        live[f"TbT k={k} random {sd}"] = [round(float(x), 9) for x in r]
for k in (3, 5):                                 # T x T with symmetric and antisymmetric pieces together (as B1635: W = eta^18 Y)
    full, mons, _ = c.equivariant_space(k + 9, lambda M: inv(M).T, lambda M: inv(M))
    hol = c.cusp_condition(full, mons, 6)
    for sd in range(3):
        co = rng.normal(size=hol.shape[0]) + 1j * rng.normal(size=hol.shape[0])
        r = ratios(c.evaluate(np.einsum("n,nrcm->rcm", co, hol), mons, c.OMEGA, 18))
        live[f"TT mixed k={k} random {sd}"] = [round(float(x), 9) for x in r]
A["live"] = live
A["min_gap_live"] = min(gaps(v) for v in live.values())
out["A"] = A

# ---- B. the hand of the multiplier ------------------------------------------------------------------------------------
conv = {"record (rho = lift^-1; W = eta^18 Y)": (lambda M: inv(M).T, lambda M: inv(M), 9, 6),
        "conjugate (rho-bar; W = eta^6 Y)": (lambda M: inv(M.conj()).T, lambda M: inv(M.conj()), 3, 2)}
B = {}
for name, (left, right, shift, ordx) in conv.items():
    B[name] = {}
    for k in (1, 3, 5):
        b, mons, _ = c.equivariant_space(k + shift, left, right)
        b = c.cusp_condition(b, mons, ordx)
        B[name][f"k={k}"] = {p: int(c.restrict_piece(b, p).shape[0]) for p in ("D", "O+", "O-")}
out["B"] = B

# ---- C. the TM1 residual pair -----------------------------------------------------------------------------------------
S2, T2 = np.array([[0, -1], [1, 0]]), np.array([[1, 1], [0, 1]])
rS, rT = c.rS, c.rT                              # the theta multiplier at weight 1 on (th2^2, th3^2, th4^2), up to eta's character
mpow = lambda A, n: np.linalg.matrix_power(A, n) if n >= 0 else np.linalg.matrix_power(inv(A), -n)
ipow = lambda A, n: np.linalg.matrix_power(A, n) if n >= 0 else np.linalg.matrix_power(np.round(inv(A)).astype(int), -n)


def rho(M):
    """rho(M) for M in SL(2, Z), by reducing M to +-T^b with left factors T^-q and S^-1."""
    M = np.array(M, int); acc = np.eye(3, dtype=complex)
    while M[1, 0] != 0:
        q = M[0, 0] // M[1, 0]
        M = ipow(T2, -q) @ M; acc = mpow(rT, -q) @ acc
        M = ipow(S2, -1) @ M; acc = inv(rS) @ acc
    s, b = M[0, 0], M[0, 1] * M[0, 0]
    return inv(acc) @ (mpow(rT, b) * (1 if s == 1 else -1))


def shares_lines(Am, Bm):                        # every eigenline of Am is an eigenline of Bm, and conversely
    def one(X, Y):
        _, V = np.linalg.eig(X)
        return all(np.linalg.norm(Y @ v - (v.conj() @ Y @ v) / (v.conj() @ v) * v) < 1e-9 for v in V.T)
    return one(Am, Bm) and one(Bm, Am)


def prop(X, Y):                                   # X = lambda Y for a scalar lambda (rho is fixed up to eta's character)
    i = np.unravel_index(np.argmax(abs(Y)), Y.shape)
    return bool(np.allclose(X, X[i] / Y[i] * Y, atol=1e-9))


Lm, Rm = np.array([[1, 1], [0, 1]]), np.array([[1, 0], [1, 1]])
C = {"homomorphism_checks": prop(rho(S2) @ rho(S2), np.eye(3)) and prop(rho(S2 @ T2 @ T2 @ S2 @ T2), rS @ rT @ rT @ rS @ rT)
     and prop(rho(Rm @ Lm), rho(Rm) @ rho(Lm)) and prop(rho(Rm @ Rm @ Lm), rho(Rm) @ rho(Rm) @ rho(Lm))
     and not prop(rho(Rm @ Lm), rho(Lm) @ rho(Rm))}
for name, M in (("RL", Rm @ Lm), ("RRL", Rm @ Rm @ Lm)):
    hits = []
    for a, b, cc, d in itertools.product(range(-4, 5), repeat=4):
        if a * d - b * cc != 1 or abs(a + d) >= 2 or cc == 0:
            continue
        E = np.array([[a, b], [cc, d]])
        if shares_lines(rho(M), rho(E)):
            t = a + d
            hits.append({"E": [a, b, cc, d], "order_in_PSL": {-1: 3, 1: 3, 0: 2}[t],
                         "fixed_point": [round((a - d) / (2 * cc), 6), round(float(np.sqrt(4 - t * t) / (2 * abs(cc))), 6)]})
    C[name] = {"trace": int(np.trace(M)), "rho_eigenvalues": [[round(float(z.real), 6), round(float(z.imag), 6)] for z in np.linalg.eigvals(rho(M))],
               "elliptic_sharing_all_eigenlines": hits,
               "orders": sorted({h["order_in_PSL"] for h in hits})}
out["C"] = C

json.dump(out, open(os.path.join(HERE, "frame_audit.json"), "w"), indent=1)
print("A  sealed Tbar x T non-degenerate at omega:", len(A["sealed_nondegenerate_at_omega"]), "| live min gap", round(A["min_gap_live"], 4))
for k, v in live.items():
    print("    ", k, v)
for name, row in B.items():
    print("B ", name, row)
for name in ("RL", "RRL"):
    print("C ", name, "elliptic elements sharing every eigenline:", len(C[name]["elliptic_sharing_all_eigenlines"]), "orders", C[name]["orders"],
          [h["fixed_point"] for h in C[name]["elliptic_sharing_all_eigenlines"][:2]])
print("C  homomorphism checks", C["homomorphism_checks"])
