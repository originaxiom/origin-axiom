import numpy as np
from setup import *

rng = np.random.default_rng(1)

# ---- group G
G = build_G()
print("|G| =", len(G))
# closure
closed = all(in_group(a[0] @ b[0], G) for a in G for b in G)
print("G closed under multiplication:", closed)
# the 24 signed perms of det 1 form a group of order 24
sp = signed_perms_det1()
print("# signed perms det+1:", len(sp))
spm = [x[0] for x in sp]
print("signed-perm group closed:", all(any(np.allclose(a @ b, c) for c in spm) for a in spm for b in spm))

print("inner_a in G:", in_group(a_in, G), " inner_b in G:", in_group(b_in, G))
print("P in G:", in_group(P, G), "  U=iP in G:", in_group(U, G))
print("eig P:", np.round(np.linalg.eigvals(P), 6), " (omega=%s)" % np.round(w, 6))
print("U^3 =", np.round(U @ U @ U, 6).diagonal(), "(scalar)  in G:", in_group(U @ U @ U, G))
for z in [-1, 1j, -1j, 1]:
    print("  iota=z*I, z=%s in G: %s" % (z, in_group(z * np.eye(3), G)))
print("  -I as det-1 signed perm? det(-I) =", round(np.linalg.det(-np.eye(3))))
print("characters (a,b) on axes:", [(int(a_in[i, i].real), int(b_in[i, i].real)) for i in range(3)])

# ---- inner-invariant subspace per tensor
print("\n== inner-invariant subspace ==")
for name, basis in [('Dirac(Tbar x T)', full_basis), ('TxT', full_basis), ('Sym2', sym_basis)]:
    ops = []
    for g in (a_in, b_in):
        f = tensor_ops(g)[name]
        A, res = op_matrix(f, basis)
        assert res < 1e-9
        ops.append(A - np.eye(len(basis)))
    S = np.vstack(ops)
    u, s, vh = np.linalg.svd(S)
    null = vh[np.sum(s > 1e-9):].conj().T  # coordinates in basis
    dim = null.shape[1]
    # convert to matrices
    mats = [sum(null[k, c] * basis[k] for k in range(len(basis))) for c in range(dim)]
    offdiag = max(np.abs(M - np.diag(np.diag(M))).max() for M in mats)
    print(name, "dim inv =", dim, " max offdiag entry in invariants =", offdiag)

# ---- U action on diagonal subspace, eigenanalysis
print("\n== U action on diag subspace ==")
roots24 = [np.exp(2j * np.pi * m / 24) for m in range(24)]


def sv_equal_test(D, tol=1e-10):
    sv = np.linalg.svd(np.diag(D), compute_uv=False)
    return sv, (sv.max() - sv.min()) < tol * max(1, sv.max())


def analyse(name, g, label):
    f = tensor_ops(g)[name]
    A, res = op_matrix(f, diag_basis)
    assert res < 1e-9
    ev = np.linalg.eigvals(A)
    print("%s [%s]: A_U eigenvalues (arg/2pi*24):" % (name, label), sorted(np.round((np.angle(ev) / (2 * np.pi) * 24) % 24, 6)),
          " |ev|:", np.round(np.abs(ev), 6))
    allok = True
    surviving = []
    maxspread = 0
    for m, lam in enumerate(roots24):
        u, s, vh = np.linalg.svd(A - lam * np.eye(3))
        r = np.sum(s > 1e-9)
        null = vh[r:].conj().T
        d = null.shape[1]
        if d == 0:
            continue
        surviving.append((m, d))
        for _ in range(300):
            c = rng.normal(size=d) + 1j * rng.normal(size=d)
            D = null @ c
            D = D * np.exp(2j * np.pi * rng.random())  # arbitrary phase
            sv, ok = sv_equal_test(D)
            maxspread = max(maxspread, sv.max() - sv.min())
            allok &= ok
    print("   surviving 24th-root eigenvalues lambda=e^{2 pi i m/24}: (m, eigenspace dim) =", surviving)
    print("   all U-eigenvectors (300 generic combos each) give 3 equal singular values:", allok, " max spread:", maxspread)
    # positive control: generic diagonal D (not eigenvector) has unequal values
    D = rng.normal(size=3) + 1j * rng.normal(size=3)
    print("   control: generic diag D singular values:", np.round(np.linalg.svd(np.diag(D), compute_uv=False), 4))
    return A


for name in ['Dirac(Tbar x T)', 'TxT', 'Sym2']:
    analyse(name, U, "U = i P")

# robustness: U = z * (signed 3-cycle) for all G-elements of 3-cycle type
print("\n== robustness over all G elements of 3-cycle type (U choices) ==")
cnt = 0
bad = 0
for g, z, S, sg in G:
    # 3-cycle type: underlying perm even, nonidentity
    P0 = np.abs(S)
    if np.allclose(P0, np.eye(3)) or sg != 1:
        continue
    cnt += 1
    for name in ['Dirac(Tbar x T)', 'TxT', 'Sym2']:
        f = tensor_ops(g)[name]
        A, res = op_matrix(f, diag_basis)
        for m, lam in enumerate(roots24):
            u, s, vh = np.linalg.svd(A - lam * np.eye(3))
            null = vh[np.sum(s > 1e-9):].conj().T
            d = null.shape[1]
            for _ in range(5 if d else 0):
                c = rng.normal(size=d) + 1j * rng.normal(size=d)
                sv, ok = sv_equal_test(null @ c)
                if not ok:
                    bad += 1
print("G elements of 3-cycle type tested:", cnt, " violations:", bad)

# ---- iota
print("\n== iota ==")
for name in ['Dirac(Tbar x T)', 'TxT', 'Sym2']:
    for z in [-1, 1j, -1j, 1]:
        f = tensor_ops(z * np.eye(3))[name]
        A, res = op_matrix(f, diag_basis)
        rho = A[0, 0]
        print("%-16s iota z=%-5s : rho(iota) on diag subspace = %s (scalar: %s); survives at weight parity: even=%s odd=%s" % (
            name, z, np.round(rho, 6), np.allclose(A, rho * np.eye(3)),
            abs(((+1) * rho) - 1) < 1e-9, abs(((-1) * rho) - 1) < 1e-9))

# ---- modular consistency (extra): U ~ [[0,-1],[1,1]], c w + d = e^{i pi/3}, U^3 = -I
print("\n== extra: consistency of rho(U)^3 = rho(iota) with weight-k eigenvalue lambda = (c w + d)^{-+k} ==")
cwd = 1 * w + 1
print("c w + d =", np.round(cwd, 6), "= e^{i pi/3}?", np.isclose(cwd, np.exp(1j * np.pi / 3)))
for name in ['Dirac(Tbar x T)', 'Sym2']:
    f = tensor_ops(U)[name]
    A, _ = op_matrix(f, diag_basis)
    for sign in (+1, -1):
        ks = []
        for k in range(12):
            lam = cwd ** (sign * k)
            u, s, vh = np.linalg.svd(A - lam * np.eye(3))
            if np.sum(s < 1e-9) > 0:
                ks.append(k)
        print("%-16s lambda=(cw+d)^(%+d k): weights k in 0..11 with a nonzero U-eigenvector: %s" % (name, sign, ks))
    # iota := rho(U)^3
    f3 = tensor_ops(U @ U @ U)[name]
    A3, _ = op_matrix(f3, diag_basis)
    print("   rho(U^3) on diag =", np.round(A3[0, 0], 6), "-> iota-allowed weight parity: ",
          "even" if abs(A3[0, 0] - 1) < 1e-9 else "odd")
