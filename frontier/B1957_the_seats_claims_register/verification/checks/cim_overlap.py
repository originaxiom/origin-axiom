"""B1957: the closed-fibre triple overlap of agy-002's gate 2, rebuilt by main (data-free).
Three zero modes on the torus E_tau = C / (Z + tau Z): two of flux 3 with spin structure (1/2, 1/2) and the conjugate of
one of flux 6 with spin structure (0, 0), each displaced by a Wilson line zeta:
    psi_j(z) = (2 M Im tau)^(1/4) exp(i pi M w Im w / Im tau) theta[(j + alpha)/M, beta](M w, M tau),  w = z + zeta,
the standard zero modes of a magnetised torus (Cremades, Ibanez, Marchesano, hep-th/0404229, section 4).
Y_ijk = integral over the cell of psi_i(z; zeta_L) psi_j(z; zeta_R) conj(psi_k(z; zeta_H)), by quadrature only.
What is tested: each zero mode solves the zero-mode equation; the modes are orthonormal; the integrand is doubly periodic
exactly when the fluxes, spins and Wilson lines balance; the images of the modes under tau -> tau + 1 and tau -> -1/tau
lie in the span of the modes (the transport matrix is unitary), so that Y is covariant; and what breaks each of these.
Nothing of the seat's code is imported or run."""
import numpy as np
NW = 40


def psi(M, al, be, z, tau, zeta):
    """the M zero modes at the points z (array), as an array of shape (M,) + z.shape"""
    w = np.asarray(z, complex) + zeta; y = tau.imag; n = np.arange(-NW, NW + 1)
    out = []
    for j in range(M):
        a = (j + al) / M; na = (n + a).reshape((-1,) + (1,) * w.ndim)
        e = 1j * np.pi * M * w * (w.imag / y) + 1j * np.pi * na ** 2 * M * tau + 2j * np.pi * na * (M * w + be)
        out.append(np.exp(e).sum(axis=0))
    return (2 * M * y) ** 0.25 * np.array(out)


def cell(tau, n):
    g = (np.arange(n) + 0.0) / n; X, Yg = np.meshgrid(g, g, indexing="ij"); return X + tau * Yg


def overlap(tau, zL, zR, zH, n=48, spins=((0.5, 0.5), (0.5, 0.5), (0.0, 0.0)), fluxes=(3, 3, 6)):
    z = cell(tau, n)
    pL = psi(fluxes[0], *spins[0], z, tau, zL); pR = psi(fluxes[1], *spins[1], z, tau, zR); pH = psi(fluxes[2], *spins[2], z, tau, zH)
    return np.einsum("ixy,jxy,kxy->ijk", pL, pR, pH.conj()) / n ** 2


def transport(M, al, be, tau, zeta, which, n=48):
    """<new mode a | old mode b> over the cell of tau: new = the mode at tau + 1 (T), or at -1/tau in the variable z/tau (S)"""
    z = cell(tau, n); old = psi(M, al, be, z, tau, zeta)
    new = psi(M, al, be, z, tau + 1, zeta) if which == "T" else psi(M, al, be, z / tau, -1 / tau, zeta / tau)
    return np.einsum("axy,bxy->ab", new, old.conj()) / n ** 2


def unit_err(U): return float(np.abs(U @ U.conj().T - np.eye(len(U))).max())


SECTORS = (("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6))
POINTS = ((0.23 + 1.37j, (1 / 5, 2 / 5)), (-0.31 + 1.53j, (3 / 10, 7 / 10)), (0.11 + 1.19j, (2 / 15, 4 / 15)), (0.37 + 0.93j, (2 / 5, 1 / 5)))

if __name__ == "__main__":
    rng = np.random.default_rng(20261117)
    # 0: the zero-mode equation, orthonormality, and the selection rule
    tau = 0.23 + 1.37j; zeta = 0.07 + 0.11j; h = 1e-5; z0 = np.array([0.31 + 0.42 * tau])
    worst = 0.0
    for M, sp in ((3, (0.5, 0.5)), (6, (0.0, 0.0))):
        f = lambda z: psi(M, *sp, z, tau, zeta)
        dbar = ((f(z0 + h) - f(z0 - h)) / (2 * h) + 1j * (f(z0 + 1j * h) - f(z0 - 1j * h)) / (2 * h)) / 2
        worst = max(worst, float(np.abs(dbar + np.pi * M * (z0 + zeta) / (2 * tau.imag) * f(z0)).max() / np.abs(f(z0)).max()))
    print("Z0: the zero-mode equation (d/dzbar + pi M w / (2 Im tau)) psi = 0, by central differences: relative residual %.1e" % worst)
    z = cell(tau, 48); g3 = psi(3, 0.5, 0.5, z, tau, zeta); g6 = psi(6, 0, 0, z, tau, zeta)
    G3 = np.einsum("axy,bxy->ab", g3, g3.conj()) / 48 ** 2; G6 = np.einsum("axy,bxy->ab", g6, g6.conj()) / 48 ** 2
    print("Z1: the modes are orthonormal over the cell: flux 3 %.1e, flux 6 %.1e" % (np.abs(G3 - np.eye(3)).max(), np.abs(G6 - np.eye(6)).max()))
    # 1: the whole lock, at four moduli and points, three sectors
    P = Q = Uq = Tc = Sc = Sel = Conv = 0.0
    for tau, (a, b) in POINTS:
        w = a * tau + b; zp = np.array([0.31 + 0.42 * tau])
        for name, qL, qR in SECTORS:
            zL, zR = qL * w, qR * w; zH = (zL + zR) / 2
            ig = lambda zz: np.einsum("ix,jx,kx->ijk", psi(3, 0.5, 0.5, zz, tau, zL), psi(3, 0.5, 0.5, zz, tau, zR), psi(6, 0, 0, zz, tau, zH).conj())
            P = max(P, np.abs(ig(zp + 1) - ig(zp)).max(), np.abs(ig(zp + tau) - ig(zp)).max())
            Y = overlap(tau, zL, zR, zH); Conv = max(Conv, np.abs(overlap(tau, zL, zR, zH, n=64) - Y).max())
            for i in range(3):
                for j in range(3):
                    for k in range(6):
                        if (k - i - j - 1) % 3 != 0: Sel = max(Sel, abs(Y[i, j, k]))
            U = {(s, x): transport(3 if x != "H" else 6, *((0.5, 0.5) if x != "H" else (0.0, 0.0)), tau, {"L": zL, "R": zR, "H": zH}[x], s) for s in "TS" for x in "LRH"}
            Uq = max(Uq, max(unit_err(u) for u in U.values()))
            YT = overlap(tau + 1, zL, zR, zH); YS = overlap(-1 / tau, zL / tau, zR / tau, zH / tau)
            Tc = max(Tc, np.abs(YT - np.einsum("ia,jb,kc,abc->ijk", U["T", "L"], U["T", "R"], U["T", "H"].conj(), Y)).max())
            Sc = max(Sc, np.abs(YS - np.einsum("ia,jb,kc,abc->ijk", U["S", "L"], U["S", "R"], U["S", "H"].conj(), Y)).max())
    print("L1: 12 cases (4 moduli and points of orders 5, 10, 15, 5; up, down, lepton): the integrand's double periodicity %.1e; quadrature 48 against 64 %.1e" % (P, Conv))
    print("L2: the transport matrices of all three fields under T and S are unitary to %.1e; Y(tau + 1) and Y(-1/tau) against the transported Y: %.1e and %.1e" % (Uq, Tc, Sc))
    print("L3: selection rule: Y_ijk vanishes unless k = i + j + 1 mod 3: largest forbidden entry %.1e" % Sel)
    # 2: Y depends on the Wilson lines only through zeta_L - zeta_R
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4; s = 0.13 - 0.29j
    d = np.abs(overlap(tau, w + s, 2 * w + s, 1.5 * w + s) - overlap(tau, w, 2 * w, 1.5 * w)).max()
    e = np.abs(overlap(tau, -3 * w, 6 * w, 1.5 * w) - overlap(tau, 9 * w, 18 * w, 13.5 * w)).max()
    print("L4: a common shift of the three Wilson lines changes Y by %.1e; so the lepton's Y at w equals the down quark's at 9 w: %.1e" % (d, e))
    # 3: the transport matrices in closed form
    worstT = worstS = worstZ = 0.0
    for tau, (a, b) in POINTS:
        for M, sp in ((3, (0.5, 0.5)), (6, (0.0, 0.0))):
            U0 = {s: transport(M, *sp, tau, 0.0, s) for s in "TS"}
            j = np.arange(M) + sp[0]
            dT = np.exp(1j * np.pi * j ** 2 / M); T = np.diag(dT); ph = U0["T"][0, 0] / T[0, 0]; worstT = max(worstT, np.abs(U0["T"] - ph * T).max(), abs(abs(ph) - 1))
            S = np.exp(-2j * np.pi * np.outer(j, j) / M) / np.sqrt(M) * np.exp(2j * np.pi * sp[1] * (j[:, None] - j[None, :]) / M)
            worstS = max(worstS, np.abs(U0["S"] - np.sqrt(-1j * tau) / abs(tau) ** 0.5 * S).max())
            for zeta in (0.2 * tau + 0.4, -0.9 * tau + 1.8, 0.07 + 0.11j):                       # the same matrices at every Wilson line, up to phases
                for s in "TS":
                    Uz = transport(M, *sp, tau, zeta, s); worstZ = max(worstZ, np.abs(np.abs(Uz) - np.abs(U0[s])).max())
    print("L5: at zero Wilson line the transports are T = diag exp(i pi (j + alpha)^2 / M) up to one phase (%.1e) and" % worstT)
    print("    S = sqrt(-i tau / |tau|) exp(2 pi i beta (j - k) / M) exp(-2 pi i (j + alpha)(k + alpha) / M) / sqrt(M) exactly (%.1e): the finite Fourier transform, of weight 1/2" % worstS)
    print("    with a Wilson line the entries keep their absolute values (%.1e); only phases change" % worstZ)
    # 4: what breaks it
    tau = 0.23 + 1.37j; w = 0.2 * tau + 0.4; zL, zR = w, 2 * w; zH = (zL + zR) / 2; zp = np.array([0.31 + 0.42 * tau])
    print("C1: flux 3 with spin structure (0, 0): the image under T leaves the span: unitarity fails by %.2f (under S: %.1e)" % (unit_err(transport(3, 0, 0, tau, zL, "T")), unit_err(transport(3, 0, 0, tau, zL, "S"))))
    for lab, sp in (("(1/2, 0)", (0.5, 0.0)), ("(0, 1/2)", (0.0, 0.5))):
        print("C1: flux 3 with spin structure %s: unitarity under T fails by %.2f, under S by %.2f" % (lab, unit_err(transport(3, *sp, tau, zL, "T")), unit_err(transport(3, *sp, tau, zL, "S"))))
    ig = lambda zz, zh, spH=(0.0, 0.0): np.einsum("ix,jx,kx->ijk", psi(3, 0.5, 0.5, zz, tau, zL), psi(3, 0.5, 0.5, zz, tau, zR), psi(6, *spH, zz, tau, zh).conj())
    print("C2: Wilson lines out of balance (zeta_H moved by 0.1 tau): periodicity under z + 1 fails by %.2f" % np.abs(ig(zp + 1, zH + 0.1 * tau) - ig(zp, zH + 0.1 * tau)).max())
    print("C3: the Higgs's spin structure (1/2, 0): periodicity under z + 1 fails by %.2f" % np.abs(ig(zp + 1, zH, (0.5, 0.0)) - ig(zp, zH, (0.5, 0.0))).max())
    f5 = lambda zz: np.einsum("ix,jx,kx->ijk", psi(3, 0.5, 0.5, zz, tau, zL), psi(3, 0.5, 0.5, zz, tau, zR), psi(5, 0.0, 0.0, zz, tau, zH).conj())
    print("C4: fluxes out of balance (3 + 3 against 5): periodicity under z + tau fails by %.2f" % np.abs(f5(zp + tau) - f5(zp)).max())
