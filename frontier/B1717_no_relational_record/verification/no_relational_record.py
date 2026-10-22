"""B1717 (P-278): does a non-scalar relational record exist?  On B1675's private modules V_k = K/B (k = 2: dim 4; k = 3: dim 2) the
moves act; End_G(V_k) and Hom_G(V_2, V_3) for G = <L, R> and for <L, R, P, -I>."""
import sys, glob, importlib.util, contextlib, io, numpy as np
import pathlib, json
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
f = glob.glob(str(ROOT / "frontier" / "B1675_*" / "verification" / "main_check" / "v2_w34_independent.py"))[0]
OUT = {}
spec = importlib.util.spec_from_file_location("w34", f); m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
def induced(blk, phi):
    """the matrix of phi^* on K/B in a fixed basis: K = B (+) C, C a complement inside K"""
    K, Bc = blk.K, blk.Bcols
    # orthonormal basis of K; split off B (B is inside K)
    PB = Bc @ np.conj(Bc.T)
    Cm = K - PB @ K; u, s, vh = np.linalg.svd(Cm); C = u[:, : (s > 1e-8).sum()]      # complement of B in K
    assert C.shape[1] == blk.private, (C.shape, blk.private)
    P = blk.pullback(phi)
    img = P @ C                                   # in K (check), then project to K/B along B: coordinates on C
    assert np.linalg.norm(img - K @ (np.conj(K.T) @ img)) < 1e-8 * max(1, np.linalg.norm(img))
    basis = np.hstack([C, Bc]); coef = np.linalg.lstsq(basis, img, rcond=None)[0]
    return coef[: C.shape[1], :]
def commutant_dim(As, Bs):
    """dim {X : X A_g = B_g X} for the pairs (A_g on the source, B_g on the target)"""
    n, mm = As[0].shape[0], Bs[0].shape[0]
    rows = [np.kron(A.T, np.eye(mm)) - np.kron(np.eye(n), B) for A, B in zip(As, Bs)]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int((s < 1e-9).sum() + (n * mm - len(s)))
blocks = {k: m.Block(k) for k in (2, 3)}
for gens in (("L", "R"), ("L", "R", "P", "I")):
    A = {k: [induced(blocks[k], m.AUT[g]) for g in gens] for k in blocks}
    OUT["<%s>" % ", ".join(gens)] = {"dim_V2": A[2][0].shape[0], "dim_V3": A[3][0].shape[0], "End_V2": commutant_dim(A[2], A[2]), "End_V3": commutant_dim(A[3], A[3]), "Hom_V2_V3": commutant_dim(A[2], A[3]), "Hom_V3_V2": commutant_dim(A[3], A[2])}
    print("G =", "<" + ", ".join(gens) + ">", "| dim V_2, V_3:", A[2][0].shape[0], A[3][0].shape[0],
          "| End_G(V_2):", commutant_dim(A[2], A[2]), "| End_G(V_3):", commutant_dim(A[3], A[3]),
          "| Hom_G(V_2, V_3):", commutant_dim(A[2], A[3]), "| Hom_G(V_3, V_2):", commutant_dim(A[3], A[2]))
    for k in blocks: print("   k=%d eigenvalues of L: %s" % (k, np.round(np.linalg.eigvals(A[k][0]), 4)))
# Hom_G(rho_Q, V_k): G acts on rho_Q = C^2 by the lifts g_phi (each up to sign; every sign choice tried)
def lift(phi):
    rows = []
    for x in (1, 2):
        Y = m.R2(phi[x]); X = m.rho[x]; rows.append(np.kron(X.T, np.eye(2)) - np.kron(np.eye(2), Y))
    u, sv, vh = np.linalg.svd(np.vstack(rows)); g = vh[-1].conj().reshape(2, 2, order="F"); return g / np.sqrt(np.linalg.det(g))
import itertools
for gens in (("L", "R"), ("L", "R", "P", "I")):
    G = [lift(m.AUT[g]) for g in gens]
    A = {k: [induced(blocks[k], m.AUT[g]) for g in gens] for k in blocks}
    best = {k: max(commutant_dim([s * g for s, g in zip(signs, G)], A[k]) for signs in itertools.product((1, -1), repeat=len(G))) for k in blocks}
    best_back = {k: max(commutant_dim(A[k], [s * g for s, g in zip(signs, G)]) for signs in itertools.product((1, -1), repeat=len(G))) for k in blocks}
    OUT["<%s>" % ", ".join(gens)].update({"Hom_rhoQ_Vk_max_over_signs": best, "Hom_Vk_rhoQ_max_over_signs": best_back})
    print("G =", gens, "| max over signs dim Hom_G(rho_Q, V_k):", best, "| Hom_G(V_k, rho_Q):", best_back)
# Burnside: a scalar commutant shows irreducibility only for a semisimple action, and L acts on V_3 non-semisimply; so
# the algebra the moves generate on V_k is computed: irreducible iff it is all of End(V_k) (dimension 16, 4)
def algebra_dim(mats, n_words=6):
    from itertools import product
    span = [np.eye(mats[0].shape[0], dtype=complex)]
    words = [np.eye(mats[0].shape[0], dtype=complex)]
    for _ in range(n_words):
        new = [w @ g for w in words for g in mats]
        words = new; span += new
        M = np.array([x.reshape(-1) for x in span]); r = np.linalg.matrix_rank(M, tol=1e-9)
        if r == mats[0].shape[0] ** 2: break
    return int(np.linalg.matrix_rank(np.array([x.reshape(-1) for x in span]), tol=1e-9))
for k in blocks:
    gens = [induced(blocks[k], m.AUT[g]) for g in ("L", "R")]
    gens = gens + [np.linalg.inv(g) for g in gens]
    OUT["Burnside_algebra_dim_V%d" % k] = algebra_dim(gens)
    print("Burnside: the algebra generated on V_%d has dimension %d (End = %d)" % (k, OUT["Burnside_algebra_dim_V%d" % k], gens[0].shape[0] ** 2))
# the control: on V_3 (+) V_3 the commutant must be M_2(C), dimension 4; on V_2 (+) V_3 it must be 2
A3 = [induced(blocks[3], m.AUT[g]) for g in ("L", "R")]; A2 = [induced(blocks[2], m.AUT[g]) for g in ("L", "R")]
dsum = lambda X, Y: np.block([[X, np.zeros((X.shape[0], Y.shape[1]))], [np.zeros((Y.shape[0], X.shape[1])), Y]])
OUT["control_End_V3_plus_V3"] = commutant_dim([dsum(a, a) for a in A3], [dsum(a, a) for a in A3])
OUT["control_End_V2_plus_V3"] = commutant_dim([dsum(a, b) for a, b in zip(A2, A3)], [dsum(a, b) for a, b in zip(A2, A3)])
print("control: End(V_3 + V_3) =", OUT["control_End_V3_plus_V3"], "(expect 4); End(V_2 + V_3) =", OUT["control_End_V2_plus_V3"], "(expect 2)")
if "--check" not in sys.argv:
    json.dump(OUT, open(pathlib.Path(__file__).resolve().parent / "no_relational_record.json", "w"), indent=1)
