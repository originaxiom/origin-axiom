"""B1953 (data-free).  Frame C's coupling at the 24 points of order 5, as the symbol of one operator.
1. The law, point by point: Y(g tau, w) = c phi(g, w) U_L Y(tau, w g) U_R^dagger for g = T, S, with unitaries the same at all
   24 points (found from the pointwise Gramians), one modulus c for all points, and a phase phi(g, w).
2. The operator O(tau) = sum over the 24 points of zeta^(-ab) Y(tau, w) (x) D(w) on (families) (x) (the Weil space), D(a, b) =
   zeta^(ab/2) X^a Z^b: tested for O(g tau) = c (U_L x rho(g)) O(tau) (U_R x rho(g))^dagger with B1951's Weil representation rho.
3. Its split under the centre's parity, the two family Gramians (the Weil space traced over the 3 and over the 2), Parseval,
   and its component along hypercharge, the sum over the 24 points with the phase table.
Run at two base points; at -1/tau the end is carried by its own law (B1927), passed explicitly (P-864)."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1945_the_frames_cusp_exponents" / "verification"))
import determinant_law as DL
mp = DL.mp; CR = DL.FM.CR
PTS = [(i, j) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
BASES = (("0.13", 1.7), ("0.31", 1.2))
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])
D = lambda a, b: psi(3 * a * b) * np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)])
_ev, _V = np.linalg.eigh(P); VE, VO = _V[:, _ev > 0], _V[:, _ev < 0]
RHO = {"T": np.diag([psi(2 * x * x) for x in range(5)]), "S": np.array([[psi(x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)}
TRANS = {"T": (lambda a, b: (a, (b + a) % 5),), "S": (lambda a, b: (b % 5, (-a) % 5), lambda a, b: ((-b) % 5, a % 5))}
qn = lambda M: np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])


def frame(tx, ty, sec, end=None):
    """Y at the 24 points, both readings: {reading: array [a, b, 3, 3]}"""
    table = CR.canon
    if end is not None: CR.canon = lambda zz, e=end: {"L_2": e}
    try:
        out = {"S": np.zeros((5, 5, 3, 3), complex), "St": np.zeros((5, 5, 3, 3), complex)}
        for i, j in PTS:
            Ys = DL.parts(tx, ty, Fr(i, 5), Fr(j, 5), sec)[2]
            for rd in out: out[rd][i, j] = qn(Ys[rd])
    finally:
        CR.canon = table
    return out


def images(tx, ty, sec):
    t = mp.mpc(mp.mpf(tx), ty); s = -1 / t; t_f = complex(float(tx), ty); L0 = CR.canon(t_f)["L_2"]
    return {"t": frame(tx, ty, sec), "T": frame(mp.nstr(mp.mpf(tx) + 1, 30), ty, sec),
            "S": frame(mp.nstr(s.real, 40), float(s.imag), sec, end=L0 + math.log(abs(t_f)))}, abs(t_f)


def solve_unitary(pairs):
    rows = [np.kron(np.eye(3), B / np.trace(B).real) - np.kron((A / np.trace(A).real).T, np.eye(3)) for A, B in pairs]
    sv = np.linalg.svd(np.vstack(rows)); U = sv[2][-1].conj().reshape(3, 3).T
    return U / abs(np.linalg.det(U)) ** (1 / 3), sv[1][-1] / sv[1][0], sv[1][-2] / sv[1][0]


def law(Y0, Y1, gen):
    best = None
    for tr in TRANS[gen]:
        UL, nL, sL = solve_unitary([(Y0[tr(*w)] @ Y0[tr(*w)].conj().T, Y1[w] @ Y1[w].conj().T) for w in PTS])
        UR, nR, sR = solve_unitary([(Y0[tr(*w)].conj().T @ Y0[tr(*w)], Y1[w].conj().T @ Y1[w]) for w in PTS])
        if best is None or nL + nR < best[0]: best = (nL + nR, tr, UL, UR, max(nL, nR), min(sL, sR))
    _, tr, UL, UR, null, nxt = best; phi = {}; res = 0.0; mods = []
    for w in PTS:
        Zm = UL @ Y0[tr(*w)] @ UR.conj().T; c = np.vdot(Zm, Y1[w]) / np.vdot(Zm, Zm)
        res = max(res, np.abs(Y1[w] - c * Zm).max() / np.abs(Y1[w]).max()); phi[w] = c / abs(c); mods.append(abs(c))
    return dict(UL=UL, UR=UR, null=null, next=nxt, residual=res, phi=phi, modulus=(min(mods), max(mods)))


def phase_form(phi, gen):
    """the phases against zeta^(-a^2) (T) or zeta^(2ab) (S), up to one constant; returns the largest deviation in turns"""
    f = (lambda a, b: psi(-a * a)) if gen == "T" else (lambda a, b: psi(2 * a * b))
    ref = phi[(0, 1)] / f(0, 1)
    return max(abs(np.angle(phi[w] / (ref * f(*w)))) for w in PTS) / (2 * np.pi)


def order_of_phases(phi):
    ref = phi[(0, 1)]
    for n in (1, 5, 25, 125):
        if max(abs((phi[w] / ref) ** n - 1) for w in PTS) < 1e-8: return n
    return None


def O(Y, table=True):
    return sum(np.kron((psi(-a * b) if table else 1) * Y[a, b], D(a, b)) for a, b in PTS)


svn = lambda M: (lambda s: s / s[0])(np.linalg.svd(M, compute_uv=False))


def family_gramians(Om):
    R = Om.reshape(3, 5, 3, 5); H = {}
    for name, Vb in (("3", VE), ("2", VO)):
        H[name] = np.einsum("ixjy,yz,kxjz->ik", R, Vb @ Vb.conj().T, R.conj())
    return H


def ratios(Hm):
    e = np.sort(np.abs(np.linalg.eigvalsh((Hm + Hm.conj().T) / 2)))[::-1]; return [float(np.sqrt(e[1] / e[0])), float(np.sqrt(e[2] / e[0]))]


def phased_sum(Y):
    return sum(psi(-a * b) * Y[a, b] for a, b in PTS)


dev = lambda x, y: float(max(abs(a / b - 1) for a, b in zip(x, y)))


def analyse(tx, ty, sec, rd, Ys=None, absmod=None):
    if Ys is None: Ys, absmod = images(tx, ty, sec)
    Y0 = Ys["t"][rd]; r = {"abs_tau": absmod}
    O0 = O(Y0); E = np.kron(np.eye(3), VE); Od = np.kron(np.eye(3), VO)
    r["mixing_of_3_and_2"] = float(np.abs(E.conj().T @ O0 @ Od).max() / np.abs(O0).max())
    H0 = family_gramians(O0); plainG = 5 * sum(Y0[w] @ Y0[w].conj().T for w in PTS)
    r["parseval"] = float(np.abs(H0["3"] + H0["2"] - plainG).max() / np.abs(plainG).max())
    r["gramian_3"], r["gramian_2"], r["gramian_plain"] = ratios(H0["3"]), ratios(H0["2"]), ratios(plainG)
    s0 = svn(phased_sum(Y0)); r["phased_sum"] = [float(s0[1]), float(s0[2])]
    p0 = svn(sum(Y0[w] for w in PTS)); r["plain_sum"] = [float(p0[1]), float(p0[2])]
    for gen in ("T", "S"):
        Y1 = Ys[gen][rd]; lw = law(Y0, Y1, gen); O1 = O(Y1); g = {}
        g["law_residual"] = float(lw["residual"]); g["modulus"] = [float(lw["modulus"][0]), float(lw["modulus"][1])]
        g["unitary_null"], g["unitary_next"] = float(lw["null"]), float(lw["next"])
        g["phase_order"] = order_of_phases(lw["phi"]); g["phase_form_deviation"] = float(phase_form(lw["phi"], gen))
        g["O_singular_values"] = float(np.abs(svn(O1) / svn(O0) - 1).max()); g["O_without_table"] = float(np.abs(svn(O(Y1, False)) / svn(O(Y0, False)) - 1).max())
        best = min(float(np.abs(O1 - (np.vdot(L, O1) / np.vdot(L, L)) * L).max() / np.abs(O1).max())
                   for Wc in (RHO[gen], RHO[gen].conj().T) for L in [np.kron(lw["UL"], Wc) @ O0 @ np.kron(lw["UR"], Wc).conj().T])
        g["O_law_with_the_weil_representation"] = best
        H1 = family_gramians(O1)
        g["gramian_3"], g["gramian_2"] = dev(ratios(H1["3"]), r["gramian_3"]), dev(ratios(H1["2"]), r["gramian_2"])
        s1 = svn(phased_sum(Y1)); g["phased_sum"] = dev([s1[1], s1[2]], r["phased_sum"])
        p1 = svn(sum(Y1[w] for w in PTS)); g["plain_sum"] = dev([p1[1], p1[2]], r["plain_sum"])
        r[gen] = g
    return r


if __name__ == "__main__":
    out = {}
    for tx, ty in BASES:
        for sec in ("down", "up"):
            Ys, am = images(tx, ty, sec)
            for rd in ("S", "St"):
                r = analyse(tx, ty, sec, rd, Ys, am); out["%s+%si %s %s" % (tx, ty, sec, rd)] = r
                print("tau = %s + %si, %-4s, %-2s" % (tx, ty, sec, rd))
                for gen in ("T", "S"):
                    g = r[gen]
                    print("   %s: the law at all 24 points %.1e (unitaries fixed: %.0e / %.0e; one modulus %.6f); phases of order %s, off the form %s by %.1e turns"
                          % (gen, g["law_residual"], g["unitary_null"], g["unitary_next"], g["modulus"][1], g["phase_order"], "zeta^(-a^2)" if gen == "T" else "zeta^(2ab)", g["phase_form_deviation"]))
                    print("      the operator: singular values %.1e (without the table %.1e); with B1951's Weil representation %.1e; Gramians over the 3 and the 2: %.1e, %.1e; the phased sum %.1e; the plain sum %.1e"
                          % (g["O_singular_values"], g["O_without_table"], g["O_law_with_the_weil_representation"], g["gramian_3"], g["gramian_2"], g["phased_sum"], g["plain_sum"]))
                print("   the part mixing the 3 and the 2: %.1e; Parseval %.1e; ratios: over the 3 (%.6f, %.6f), over the 2 (%.6f, %.6f), plain Gramian (%.6f, %.6f), the phased sum (%.6f, %.6f)"
                      % (r["mixing_of_3_and_2"], r["parseval"], *r["gramian_3"], *r["gramian_2"], *r["gramian_plain"], *r["phased_sum"]), flush=True)
    (HERE / "weyl_operator.json").write_text(json.dumps(out, indent=1) + "\n")
